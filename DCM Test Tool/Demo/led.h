/****************************************************************************** 
 * Module      : Led                                                          * 
 * File Name   : led.h                                                        * 
 * Description : Header file for led module                                   * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#ifndef LED_H_
#define LED_H_

#include "types.h"
#include "common.h"
#include "diodrv.h"

/****************************************************************************** 
 *                                                                            * 
 *                                Definitions                                 * 
 *                                                                            * 
 ******************************************************************************/

/* LED channels */
#define LED_IND_R_CH    ( 0 )
#define LED_IND_B_CH    ( 1 )
#define LED_IND_G_CH    ( 2 )

/****************************************************************************** 
 *                                                                            * 
 *                               Configuration                                * 
 *                                                                            * 
 ******************************************************************************/

/* LED channels configuration */
static const led_ch led[] =
{
    { /* Channel 0: Red LED */
        .port = PORT_F,
        .pin  = PIN_1
    },
  
    { /* Channel 1: Blue LED */
        .port = PORT_F,
        .pin  = PIN_2
    },
  
    { /* Channel 2: Green LED */
        .port = PORT_F,
        .pin  = PIN_3
    }
};

/****************************************************************************** 
 *                                                                            * 
 *                            Function Prototypes                             * 
 *                                                                            * 
 ******************************************************************************/

/* Initializes selected LED. */
extern E_status LED_Init(channel_t);

/* Turns on selected LED. */
extern E_status LED_On(channel_t);

/* Turns off selected LED. */
extern E_status LED_Off(channel_t);


#endif /* LED_H_ */
