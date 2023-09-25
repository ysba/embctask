#ifndef __TICK_H__
#define __TICK_H__

typedef unsigned int tick_t;

extern tick_t tick_count;

bool tick_compare(unsigned int val);
                
#define tick_set(val) (tick_count+val)

#endif
