/******************************************************************************
 * Module      : diodrv                                                       *
 * File Name   : diodrv_regs.h                                                *
 * Description : Header file for hardware registers of diodrv module          *
 * Created on  : Mar 23, 2020                                                 *
 ******************************************************************************/

#ifndef DIODRV_REGS_H_
#define DIODRV_REGS_H_

/****************************************************************************** 
 *                                                                            * 
 *                                Definitions                                 * 
 *                                                                            * 
 ******************************************************************************/

/* H/W values */
#define MAX_PORT        ( 5 )
#define GPIO_LOCK_KEY   ( 0x4C4F434B )

/* Registers */
#define PORTA_BASE      ( 0x40004000 )
#define SYSCTL_RCGC     ( 0x400FE108 )
   
/* Function-like macros */
#define HWREG(b)        (*((volatile uint32_t *)(b)))
#define PORT(n)         ( PORTA_BASE | ((n & 0x4) << 15) | ((n & 0x3) << 12) )

/* Base address extensions */
#define DATA            ( 0x3FC )
#define DIR             ( 0x400 )
#define PUR             ( 0x510 )
#define PDR             ( 0x514 )
#define DEN             ( 0x51C )
#define LOCK            ( 0x520 )
#define CR              ( 0x524 )


#endif /* DIODRV_REGS_H_ */
