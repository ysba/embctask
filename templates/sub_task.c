#include "main.h"
#include "[[MAIN_TASK_NAME_LOWERCASE]]_private.h"

typedef enum {
    [[SUB_TASK_STATE_LIST]]
} [[MAIN_TASK_NAME_LOWERCASE]]_sub_state_[[SUB_TASK_NAME_LOWERCASE]]_t;

void [[MAIN_TASK_NAME_LOWERCASE]]_sub_task_[[SUB_TASK_NAME_LOWERCASE]]() {
    
    switch (([[MAIN_TASK_NAME_LOWERCASE]]_sub_state_[[SUB_TASK_NAME_LOWERCASE]]_t) [[MAIN_TASK_NAME_LOWERCASE]].sub_state) {[[SUB_TASK_CASES]]
    }
}