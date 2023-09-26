# embctask
Source Code Generator for Embedded C Tasks.

The main goal is to automate the generation of Standard C source and header files with machine states for an application that runs on a bare-metal embedded software. The user only needs to define names for tasks, subtasks and states in a standard JSON file (as seen in the below example). The output is composed by source and header files with the application organized as a state machine structure ready to implement code.

With few changes, the structure can also be used with other type os applications, such as RTOS's (just skip the ``tick`` stuff).

The motivation is to save time avoiding the repetitive manual (and boring) effort of creating organized code. Also, the division into subtasks allow a bigger code to be created. Code with a single ``switch/case`` for all application states may be hard to maintain.

## tl;dr
* What does this do: generate base code for tasks in Standard C
* How does this do it: the user fills a default JSON with information about the application (see ``test`` directory)

## Usage
```sh
python embctask.py [path_to_json]/config.json
```

## Output
The ``output`` directory will contain all generated code (source and headers).

* There will be generated:
  * A pair of source and header with the same name of the main task.
  * A single source file for each sub-task.
  * A pair of source and header with the same name of the main task with the ``private`` suffix. The idea is to protect the internals of the application so it cannot be accessed outside its own scope. It is a way of emulating the use ``private`` access modifier of C++.
 
Your main code just to:
* Include a single header of the generated code.
* Call one initialization function.
* Call the task executaion once in the main loop.

The generated code contain only the structure with definition of states. User is can use it freely to keep the application organized in an easy way to maintain.

## Example

The following is a JSON file used to configure ``embctask`` for generating code.
* The application is called ``app_complex``. Any name could be used since respecting C standards.
* The application contain 3 sub-tasks: ``init``, ``run`` and ``result``.
* Eacho sub-task has their own states.

```JSON
{
	"main_task": "app_complex",
	"sub_tasks": [
		{
			"name": "init",
			"states": [
				"message",
				"do_something_1",
				"do_something_2",
				"wait"
			]
		},
		{
			"name": "run",
			"states": [
				"read_sensor",
				"serial_tx",
				"serial_rx",
				"do_something_1",
				"do_something_2",
				"do_something_3",
				"do_something_4"
			]
		},
		{
			"name": "result",
			"states": [
				"success",
				"error"
			]
		}
	]
}
```

To generate code, run the following command:

```sh
python embctask.py test/app_complex.json
```

The source files will be put in the ``output`` directory present where the command was executed. The source files can then be included in your C project.

To used it, please do as in the following C code snippet:
* Include the header file with the same name of the main task (``app_complex.h`` in this example)
* Call ``app_complex_init()`` before the main loop
* Call ``app_complex_task()`` once inside the main loop

```C
#include <stdlib.h>
#include "app_complex.h"
#include "tick.h"
// place other includes here

int main() {

  app_complex_init();
  // place other initialization calls here

  // main forever loop
  while(1) {
    // clear watchdog?
    // call other tasks
    app_complex_task();
  }
}
```
