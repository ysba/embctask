#include "main.h"
#include "[[MAIN_TASK_NAME_LOWERCASE]]_private.h"


[[MAIN_TASK_NAME_LOWERCASE]]_t [[MAIN_TASK_NAME_LOWERCASE]];


void [[MAIN_TASK_NAME_LOWERCASE]]_set_main_state([[MAIN_TASK_NAME_LOWERCASE]]_state_t new_state) {
    [[MAIN_TASK_NAME_LOWERCASE]].sub_state = 0;
    [[MAIN_TASK_NAME_LOWERCASE]].state = new_state;
}
