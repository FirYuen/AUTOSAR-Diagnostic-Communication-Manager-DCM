/****************************************************************************** 
 * Module      : Indicator LED                                                * 
 * File Name   : indicator_led.h                                              * 
 * Description : Header file for indicator led module                         * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#ifndef INDICATOR_LED_H_
#define INDICATOR_LED_H_

#include "common.h"
#include "led.h"

/****************************************************************************** 
 *                                                                            * 
 *                                Definitions                                 * 
 *                                                                            * 
 ******************************************************************************/

/* Colors */
#define COLOR_NONE      ( 0 )
#define COLOR_RED       ( 1 )
#define COLOR_GREEN     ( 2 )
#define COLOR_BLUE      ( 3 )
#define COLOR_WHITE     ( 4 )

/****************************************************************************** 
 *                                                                            * 
 *                            Function Prototypes                             * 
 *                                                                            * 
 ******************************************************************************/

/* Initializes all LEDs required */
extern E_status IndicatorLED_Init(void);

/* Set color of indicator LED */
extern void IndicatorLED_SetColor(color_t);


#endif /* INDICATOR_LED_H_ */
