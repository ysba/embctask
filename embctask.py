import argparse
import os
import json


class EmbCTask:
    def __init__(self, config_path):
        self.config_path = config_path
        self.output_path = "output"


    def gen_task_source(self):
        with open("templates/task.c", "r") as file_handle:
            source = file_handle.read()
        with open("templates/main_task_cases.c", "r") as file_handle:
            case = file_handle.read()
        case = case.replace("[[MAIN_TASK_NAME_UPPERCASE]]", self.config["main_task"].upper())
        case = case.replace("[[MAIN_TASK_NAME_LOWERCASE]]", self.config["main_task"])
        source = source.replace("[[MAIN_TASK_NAME_LOWERCASE]]", self.config["main_task"])
        main_task_cases = ""
        for sub_task in self.config["sub_tasks"]:
            temp = case.replace("[[SUB_TASK_NAME_UPPERCASE]]", sub_task["name"].upper())
            temp = temp.replace("[[SUB_TASK_NAME_LOWERCASE]]", sub_task["name"])
            main_task_cases += temp
        source = source.replace("[[MAIN_TASK_CASES]]", main_task_cases)
        with open(f"{self.output_path}/{self.config['main_task']}.c", "w") as file_handle:
            file_handle.write(source)
        

    def gen_task_header(self):
        with open("templates/task.h", "r") as file_handle:
            header = file_handle.read()
        header = header.replace("[[MAIN_TASK_NAME_UPPERCASE]]", self.config["main_task"].upper())
        header = header.replace("[[MAIN_TASK_NAME_LOWERCASE]]", self.config["main_task"])
        with open(f"{self.output_path}/{self.config['main_task']}.h", "w") as file_handle:
            file_handle.write(header)


    def gen_task_private_source(self):
        with open("templates/task_private.c", "r") as file_handle:
            source = file_handle.read()
        source = source.replace("[[MAIN_TASK_NAME_LOWERCASE]]", self.config["main_task"])
        with open(f"{self.output_path}/{self.config['main_task']}_private.c", "w") as file_handle:
            file_handle.write(source)


    def gen_task_private_header(self):
        with open("templates/task_private.h", "r") as file_handle:
            header = file_handle.read()
        header = header.replace("[[MAIN_TASK_NAME_UPPERCASE]]", self.config["main_task"].upper())
        header = header.replace("[[MAIN_TASK_NAME_LOWERCASE]]", self.config["main_task"])
        state_list = f"{self.config['main_task'].upper()}_STATE_{self.config['sub_tasks'][0]['name'].upper()} = 0,\n\t"
        for sub_task in self.config["sub_tasks"][1:]:
            state_list += f"{self.config['main_task'].upper()}_STATE_{sub_task['name'].upper()},\n\t"
        header = header.replace("[[MAIN_TASK_STATE_LIST]]", state_list)
        function_list = ""
        for sub_task in self.config["sub_tasks"]:
            function_list += f"{self.config['main_task']}_sub_task_{sub_task['name']}();\n"
        header = header.replace("[[SUB_TASK_FUNCTION_LIST]]", function_list)
        with open(f"{self.output_path}/{self.config['main_task']}_private.h", "w") as file_handle:
            file_handle.write(header)


    def gen_sub_tasks_source(self):
        with open("templates/sub_task_cases.c", "r") as file_handle:
            case = file_handle.read()
        case = case.replace("[[MAIN_TASK_NAME_UPPERCASE]]", self.config["main_task"].upper())
        for sub_task in self.config["sub_tasks"]:
            with open("templates/sub_task.c", "r") as file_handle:
                source = file_handle.read()
            source = source.replace("[[MAIN_TASK_NAME_LOWERCASE]]", self.config["main_task"])
            source = source.replace("[[SUB_TASK_NAME_LOWERCASE]]", sub_task["name"])
            state_list = f"{self.config['main_task'].upper()}_SUB_STATE_{sub_task['name'].upper()}_{sub_task['states'][0].upper()} = 0,\n\t"
            for sub_state in sub_task["states"][1:]:
                state_list += f"{self.config['main_task'].upper()}_SUB_STATE_{sub_task['name'].upper()}_{sub_state.upper()},\n\t"
            source = source.replace("[[SUB_TASK_STATE_LIST]]", state_list)
            sub_task_cases = ""
            for sub_state in sub_task["states"]:
                temp = case.replace("[[SUB_TASK_NAME_UPPERCASE]]", sub_task["name"].upper())
                temp = temp.replace("[[SUB_TASK_STATE_UPPERCASE]]", sub_state.upper())
                sub_task_cases += temp
            source = source.replace("[[SUB_TASK_CASES]]", sub_task_cases)
            with open(f"{self.output_path}/{self.config['main_task']}_{sub_task['name']}.c", "w") as file_handle:
                file_handle.write(source)


    def gen_simple_task_source(self):
        with open("templates/task_simple.c", "r") as file_handle:
            source = file_handle.read()
        with open("templates/simple_task_cases.c", "r") as file_handle:
            case = file_handle.read()
        case = case.replace("[[MAIN_TASK_NAME_UPPERCASE]]", self.config["main_task"].upper())
        source = source.replace("[[MAIN_TASK_NAME_LOWERCASE]]", self.config["main_task"])
        simple_task_cases = ""
        for state in self.config["states"]:
            temp = case.replace("[[SIMPLE_TASK_STATE_UPPERCASE]]", state.upper())
            simple_task_cases += temp
        source = source.replace("[[MAIN_TASK_CASES]]", simple_task_cases)
        with open(f"{self.output_path}/{self.config['main_task']}.c", "w") as file_handle:
            file_handle.write(source)
        

    def gen_simple_task_header(self):
        with open("templates/task_simple.h", "r") as file_handle:
            header = file_handle.read()
        header = header.replace("[[MAIN_TASK_NAME_UPPERCASE]]", self.config["main_task"].upper())
        header = header.replace("[[MAIN_TASK_NAME_LOWERCASE]]", self.config["main_task"])
        state_list = f"{self.config['main_task'].upper()}_STATE_{self.config['states'][0].upper()} = 0,\n\t"
        for state in self.config["states"][1:]:
            state_list += f"{self.config['main_task'].upper()}_STATE_{state.upper()},\n\t"
        header = header.replace("[[MAIN_TASK_STATE_LIST]]", state_list)
        with open(f"{self.output_path}/{self.config['main_task']}.h", "w") as file_handle:
            file_handle.write(header)


    def run(self):
        with open(self.config_path, "r") as file_handle:
            self.config = json.load(file_handle)

        self.output_path += f"/{self.config['main_task']}"
        os.makedirs(self.output_path, exist_ok=True)

        if "sub_tasks" in self.config:
            print("generating with sub-tasks")
            self.gen_task_source()
            self.gen_task_header()
            self.gen_task_private_source()
            self.gen_task_private_header()
            self.gen_sub_tasks_source()
        elif "states" in self.config:
            print("generating single task")
            self.gen_simple_task_source()
            self.gen_simple_task_header()
        else: 
            print("error")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="embctask", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("cfg", help="Configuration file (JSON)")
    args = parser.parse_args()
    config = vars(args)

    app = EmbCTask(config["cfg"])
    app.run()
