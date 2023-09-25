#include "main.h"

tick_t tick_count = 0;

bool tick_compare(tick_t val) {
    if((int)(val - tick_count) <= (int)(0))
        return true;
    else
        return false;
}
