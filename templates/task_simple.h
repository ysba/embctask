#ifndef __[[MAIN_TASK_NAME_UPPERCASE]]__
#define __[[MAIN_TASK_NAME_UPPERCASE]]__


typedef enum {
    [[MAIN_TASK_STATE_LIST]]
} [[MAIN_TASK_NAME_LOWERCASE]]_state_t;


void [[MAIN_TASK_NAME_LOWERCASE]]_init();
void [[MAIN_TASK_NAME_LOWERCASE]]_main_task();

#endif
