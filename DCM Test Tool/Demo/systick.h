/****************************************************************************** 
 * Module      : Systick                                                      * 
 * File Name   : systick.h                                                    * 
 * Description : Header file for systick module                               * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#ifndef SYSTICK_H_
#define SYSTICK_H_

#include "types.h"
#include "common.h"

/****************************************************************************** 
 *                                                                            * 
 *                                Definitions                                 * 
 *                                                                            * 
 ******************************************************************************/

/* Enable Systick timer interrupts */
#define SYSTICK_ENABLE              ( 0x07 )

/* System clock speed in kHz */
#define SYSTEM_CONFIGURED_CLK_KHZ   ( 16000 - 1 )

/* Systick period in ms */
#define SYSTEM_CONFIGURED_TICK_MS   ( 10 )

/****************************************************************************** 
 *                                                                            * 
 *                            Function Prototypes                             * 
 *                                                                            * 
 ******************************************************************************/

/* Starts systick */
extern void Systick_Start(void);

/* Sets systick callback function */
extern void Systick_SetCallBack(volatile void(*fn_ptr)(void));


#endif /* SYSTICK_H_ */
