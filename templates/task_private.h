#ifndef __[[MAIN_TASK_NAME_UPPERCASE]]_PRIVATE__
#define __[[MAIN_TASK_NAME_UPPERCASE]]_PRIVATE__


typedef enum {
    [[MAIN_TASK_STATE_LIST]]
} [[MAIN_TASK_NAME_LOWERCASE]]_state_t;


typedef struct {
    [[MAIN_TASK_NAME_LOWERCASE]]_state_t state;
    int sub_state;
    tick_t timer;
    tick_t timer_last_value;    
    union {
        uint16_t val;
        struct {
            bool timer_skip:1;
        } bits;
    } flags;
} [[MAIN_TASK_NAME_LOWERCASE]]_t;


void [[MAIN_TASK_NAME_LOWERCASE]]_set_main_state([[MAIN_TASK_NAME_LOWERCASE]]_state_t new_state);

[[SUB_TASK_FUNCTION_LIST]]
extern [[MAIN_TASK_NAME_LOWERCASE]]_t [[MAIN_TASK_NAME_LOWERCASE]];

#endif
