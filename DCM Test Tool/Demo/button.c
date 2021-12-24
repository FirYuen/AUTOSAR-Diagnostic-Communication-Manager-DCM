/******************************************************************************
 * Module      : Button                                                       *
 * File Name   : button.c                                                     *
 * Description : Source file for button module                                *
 * Created on  : Mar 23, 2020                                                 *
 ******************************************************************************/

#include "Button.h"

/****************************************************************************** 
 *                                                                            * 
 *                              Global Variables                              * 
 *                                                                            * 
 ******************************************************************************/

/* Global Switch 1 status */
ButtonStatusType g_SW1_Status = IS_NOT_PRESSED;

/* Global Switch 2 status */
ButtonStatusType g_SW2_Status = IS_NOT_PRESSED;

/******************************************************************************
 * Name         : Button_Init                                                 *
 * Inputs       : channel                                                     *
 * Outputs      : None                                                        *
 * Return Value : E_status                                                    *
 * Description  : Initializes button as i/p.                                  *
 ******************************************************************************/
E_status Button_Init(channel_t channel)
{
    /* Return E_OK if initialization is successful. */
    return DIO_InitPin(button[channel].port, button[channel].pin, INPUT_PU);
}

/******************************************************************************
 * Name         : Button_UpdateStatus                                         *
 * Inputs       : channel                                                     *
 * Outputs      : data                                                        *
 * Return Value : E_status                                                    *
 * Description  : Reads button status.                                        *
 ******************************************************************************/
E_status Button_UpdateStatus(channel_t channel, diodata_t* data)
{
    /* Check if data is not a null pointer. */
    if (NULL_PTR == data)
    {
        /* Return E_NOT_OK. */
        return E_NOT_OK;
    }

    /* Return E_OK if reading is successful. */
    return DIO_ReadPin(button[channel].port, button[channel].pin, data);
}
