/****************************************************************************** 
 * Module      : Scheduler                                                    * 
 * File Name   : scheduler.h                                                  * 
 * Description : Header file for scheduler module                             * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#ifndef SCHEDULER_H_
#define SCHEDULER_H_

/****************************************************************************** 
 *                                                                            * 
 *                            Function Prototypes                             * 
 *                                                                            * 
 ******************************************************************************/

/* Initializes scheduler */
extern void Scheduler_Init(void);

/* Increments ticks for scheduler */
extern volatile void Scheduler_NewTimerTick(void);

/* Main scheduler component */
extern void Scheduler_Loop(void);

#endif /* SCHEDULER_H_ */
