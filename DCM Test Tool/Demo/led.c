/****************************************************************************** 
 * Module      : Led                                                          * 
 * File Name   : led.c                                                        * 
 * Description : Source file for led module                                   * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#include "led.h"

/****************************************************************************** 
 * Name         : LED_Init                                                    * 
 * Inputs       : channel                                                     * 
 * Outputs      : None                                                        * 
 * Return Value : E_status                                                    * 
 * Description  : Initializes led as o/p.                                     * 
 ******************************************************************************/
E_status LED_Init(channel_t channel)
{
    /* Returns E_OK if initialization was successful. */ 
    return DIO_InitPin(led[channel].port, led[channel].pin, OUTPUT);
}

/****************************************************************************** 
 * Name         : LED_On                                                      * 
 * Inputs       : channel                                                     * 
 * Outputs      : None                                                        * 
 * Return Value : E_status                                                    * 
 * Description  : Turns on led.                                               * 
 ******************************************************************************/
E_status LED_On(channel_t channel)
{
    /* Returns E_OK if setting pin was successful. */
    return DIO_WritePin(led[channel].port, led[channel].pin, DIO_HIGH);
}

/****************************************************************************** 
 * Name         : LED_Off                                                     * 
 * Inputs       : channel                                                     * 
 * Outputs      : None                                                        * 
 * Return Value : E_status                                                    * 
 * Description  : Turns off led.                                              * 
 ******************************************************************************/
E_status LED_Off(channel_t channel)
{
    /* Returns E_OK if clearing pin was successful. */
    return DIO_WritePin(led[channel].port, led[channel].pin, DIO_LOW);
}
