/******************************************************************************
 * Module      : diodrv                                                       *
 * File Name   : diodrv.h                                                     *
 * Description : Header file for diodrv module                                *
 * Created on  : Mar 23, 2020                                                 *
 ******************************************************************************/

#ifndef DIODRV_H_
#define DIODRV_H_

#include "common.h"
#include "types.h"

/****************************************************************************** 
 *                                                                            * 
 *                                Definitions                                 * 
 *                                                                            * 
 ******************************************************************************/

/* Ports */
#define PORT_A          ( 0 )
#define PORT_B          ( 1 )
#define PORT_C          ( 2 )
#define PORT_D          ( 3 )
#define PORT_E          ( 4 )
#define PORT_F          ( 5 )

/* Pins */
#define PIN_0           ( 1U << 0 )
#define PIN_1           ( 1U << 1 )
#define PIN_2           ( 1U << 2 )
#define PIN_3           ( 1U << 3 )
#define PIN_4           ( 1U << 4 )
#define PIN_5           ( 1U << 5 )
#define PIN_6           ( 1U << 6 )
#define PIN_7           ( 1U << 7 )

/* Modes */
#define OUTPUT          ( 0 )
#define INPUT_PU        ( 1 )
#define INPUT_PD        ( 2 )

/* Standard o/p pin states */
#define DIO_LOW         ( 0 )
#define DIO_HIGH        ( 1 )

/******************************************************************************
 *                                                                            *
 *                            Function Prototypes                             *
 *                                                                            *
 ******************************************************************************/

/* Initializes DIO pins. */
extern E_status DIO_InitPin(port_t, pin_t, diomode_t);

/* Reads DIO pins (i/p). */
extern E_status DIO_ReadPin(port_t, pin_t, diodata_t* data);

/* Changes DIO pins (o/p). */
extern E_status DIO_WritePin(port_t, pin_t, diodata_t data);


#endif /* DIODRV_H_ */
