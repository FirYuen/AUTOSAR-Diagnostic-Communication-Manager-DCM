/****************************************************************************** 
 * Module      : Indicator LED                                                * 
 * File Name   : indicator_led.c                                              * 
 * Description : Source file for indicator led module                         * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#include "indicator_led.h"

/****************************************************************************** 
 * Name         : IndicatorLED_Init                                           * 
 * Inputs       : None                                                        * 
 * Outputs      : None                                                        * 
 * Return Value : E_status                                                    * 
 * Description  : Initializes indicator LED.                                  * 
 ******************************************************************************/
E_status IndicatorLED_Init(void)
{
    /* Check if initialization is successful. */
    if ((LED_Init(LED_IND_R_CH) == E_OK) &&
        (LED_Init(LED_IND_G_CH) == E_OK) &&
        (LED_Init(LED_IND_B_CH) == E_OK))
    {
        return E_OK;                            /* Return E_OK. */
    }
    else /* ERROR */
    {
        return E_NOT_OK;                        /* Return E_NOT_OK. */
    }
}

/****************************************************************************** 
 * Name         : IndicatorLED_SetColor                                       * 
 * Inputs       : color                                                       * 
 * Outputs      : None                                                        * 
 * Return Value : None                                                        * 
 * Description  : Sets indicator LED specific color.                          * 
 ******************************************************************************/
void IndicatorLED_SetColor(color_t color)
{
    if (COLOR_WHITE == color)                   /* Check if color is white. */
    {
        LED_On(LED_IND_R_CH);                   /* Turn on Red channel. */
        LED_On(LED_IND_G_CH);                   /* Turn on Green channel. */
        LED_On(LED_IND_B_CH);                   /* Turn on Blue channel. */
    }
    else
    {
        /* Check if color is red. */
        if (COLOR_RED == color)
        {
            LED_On(LED_IND_R_CH);               /* Turn on red channel. */
        }
        else /* NOT RED */
        {
            LED_Off(LED_IND_R_CH);              /* Turn off red channel. */
        }
        
        /* Check if color is green. */
        if (COLOR_GREEN == color)
        {
            LED_On(LED_IND_G_CH);               /* Turn on green channel. */
        }
        else /* NOT GREEN */
        {
            LED_Off(LED_IND_G_CH);              /* Turn off green channel. */
        }
        
        /* Check if color is blue. */
        if (COLOR_BLUE == color)
        {
            LED_On(LED_IND_B_CH);               /* Turn on blue channel. */
        }
        else /* NOT BLUE */
        {
            LED_Off(LED_IND_B_CH);              /* Turn off blue channel. */
        }
    }
}
