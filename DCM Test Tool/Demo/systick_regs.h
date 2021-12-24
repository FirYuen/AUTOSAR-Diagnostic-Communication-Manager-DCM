/****************************************************************************** 
 * Module      : Systick                                                      * 
 * File Name   : systick_regs.h                                               * 
 * Description : Header file for registers of systick module                  * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#ifndef SYSTICK_REGS_H_
#define SYSTICK_REGS_H_

/****************************************************************************** 
 *                                                                            * 
 *                                Definitions                                 * 
 *                                                                            * 
 ******************************************************************************/

/* NVIC control register */
#define NVIC_ST_CTRL_R          (*((volatile uint32_t *)0xE000E010))

/* NVIC reload register */
#define NVIC_ST_RELOAD_R        (*((volatile uint32_t *)0xE000E014))

/* NVIC current register */
#define NVIC_ST_CURRENT_R       (*((volatile uint32_t *)0xE000E018))

/* Systick control register */
#define SYSTICK_CTRL            NVIC_ST_CTRL_R

/* Systick reload value register */
#define SYSTICK_RELOAD          NVIC_ST_RELOAD_R

/* Systick current value register */
#define SYSTICK_CURRENT_VALUE   NVIC_ST_CURRENT_R


#endif /* SYSTICK_REGS_H_ */
