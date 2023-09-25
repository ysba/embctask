#include "main.h"
#include "[[MAIN_TASK_NAME_LOWERCASE]]_private.h"


void [[MAIN_TASK_NAME_LOWERCASE]]_init() {
    memset(&[[MAIN_TASK_NAME_LOWERCASE]], 0, sizeof([[MAIN_TASK_NAME_LOWERCASE]]));
    /* place other initialization code here */
}


void [[MAIN_TASK_NAME_LOWERCASE]]_main_task() {

    if ([[MAIN_TASK_NAME_LOWERCASE]].flags.bits.timer_skip == false) {
        if (tick_compare([[MAIN_TASK_NAME_LOWERCASE]].timer) == 0)
            return;
    }
    
    [[MAIN_TASK_NAME_LOWERCASE]].timer_last_value = [[MAIN_TASK_NAME_LOWERCASE]].timer;


    switch([[MAIN_TASK_NAME_LOWERCASE]].state) {[[MAIN_TASK_CASES]]
    }


    if ([[MAIN_TASK_NAME_LOWERCASE]].timer == [[MAIN_TASK_NAME_LOWERCASE]].timer_last_value)
        [[MAIN_TASK_NAME_LOWERCASE]].flags.bits.timer_skip = true;
    else
        [[MAIN_TASK_NAME_LOWERCASE]].flags.bits.timer_skip = false;
}
