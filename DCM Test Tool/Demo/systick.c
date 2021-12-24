/****************************************************************************** 
 * Module      : Systick                                                      * 
 * File Name   : systick.h                                                    * 
 * Description : Source file for systick module                               * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#include "systick.h"
#include "systick_regs.h"

/****************************************************************************** 
 *                                                                            * 
 *                              Global Variables                              * 
 *                                                                            * 
 ******************************************************************************/

/* Systick callback function */
static volatile void(*g_Systick_Callback)(void) = NULL_PTR;

/****************************************************************************** 
 * Name         : Systick_Start                                               * 
 * Inputs       : None                                                        * 
 * Outputs      : None                                                        * 
 * Return Value : None                                                        * 
 * Description  : Starts systick and enable systick interrupts.               * 
 ******************************************************************************/
void Systick_Start(void)
{
    /* Disable systick before configuration. */
	SYSTICK_CTRL = INITIALIZED_TO_ZERO;

    /* Set systick with configured tick value. */
	SYSTICK_RELOAD = (SYSTEM_CONFIGURED_CLK_KHZ * SYSTEM_CONFIGURED_TICK_MS);  

    /* Enable systick and enable interrupt mode. */
	SYSTICK_CTRL = SYSTICK_ENABLE;
}

/****************************************************************************** 
 * Name         : Systick_GetCallBack_Func                                    * 
 * Inputs       : fn_ptr                                                      * 
 * Outputs      : None                                                        * 
 * Return Value : None                                                        * 
 * Description  : Sets systick callback function.                             * 
 ******************************************************************************/
void Systick_SetCallBack(volatile void(*fn_ptr)(void))
{
    /* Set systick pointer to function. */
	g_Systick_Callback = fn_ptr;
}

/****************************************************************************** 
 * Name         : Systick_Handler                                             * 
 * Inputs       : None                                                        * 
 * Outputs      : None                                                        * 
 * Return Value : None                                                        * 
 * Description  : Systick Interrupt Handler.                                  * 
 ******************************************************************************/
void Systick_Handler(void)
{   
    /* Call callback function. */
	(*g_Systick_Callback)();
}

