# embctask
Source Code Generator for Embedded C Tasks.

The main goal is to aumtomate the generation of Standard C source and header files with machine states for an application that runs on a bare-metal embedded software. The user needs only to define names for tasks, subtasks and states in a standard JSON file (as seen in the below example). The output is composed by source and header files with the application organized in a state machine structure ready to code.

With few changes, the structure can also be used with other type os applications, such as RTOS's (just skip the ``tick`` stuff).

Motivation is to save time avoiding the manual repetitive effort of organizing code. Also, the division into subtasks allow a bigger code to be created. Code with a single ``switch/case`` for all application states may be hard to maintain.

## Usage
```sh
python embctask.py [path_to_json]/config.json
```

## Output
The ``output`` directory will contain all generated code (source and headers).


## Example