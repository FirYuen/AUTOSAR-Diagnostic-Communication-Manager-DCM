/******************************************************************************
 * Module      : diodrv                                                       *
 * File Name   : diodrv.c                                                     *
 * Description : Source file for diodrv module                                *
 * Created on  : Mar 23, 2020                                                 *
 ******************************************************************************/

#include "diodrv.h"
#include "diodrv_regs.h"

/******************************************************************************
 * Name         : DIO_InitPin                                                 *
 * Inputs       : port, pin & mode                                            *
 * Outputs      : None                                                        *
 * Return Value : E_status                                                    *
 * Description  : Initializes DIO pins and return E_OK if successful.         *
 ******************************************************************************/
E_status DIO_InitPin(port_t port, pin_t pin, diomode_t mode)
{
uint32_t base;                              /* Port base address */

    /* Check if selected port not is supported by hardware. */
    if (port > MAX_PORT)
    {
        return E_NOT_OK;                    /* Return E_NOT_OK. */
    }

    base = PORT(port);                      /* Get base address. */
    HWREG(SYSCTL_RCGC) |= (1U << port);     /* Enable port clock. */

    /* Identify mode. */
    if (OUTPUT == mode)                     /* Check if mode is o/p. */
    {
        HWREG(base|DIR) |= pin;             /* Set direction as o/p. */
    }
    else if ((INPUT_PU == mode) || (INPUT_PD == mode))
    {
        HWREG(base|LOCK) = GPIO_LOCK_KEY;   /* Unlock port. */
        HWREG(base|CR) |= pin;              /* Enable change register. */
        HWREG(base|DIR) &= ~pin;            /* Set Direction. */

        if (INPUT_PU == mode)
        {
            HWREG(base|PUR) |= pin;         /* Enable pull-up resistor. */
        }
        else /* PULL-DOWN */
        {
            HWREG(base|PDR) |= pin;         /* Enable pull-down resistor. */
        }
    }
    else /* UNKNOWN MODE */
    {
        return E_NOT_OK;                    /* Return E_NOT_OK. */
    }

    HWREG(base|DEN) |= pin;                 /* Enable digital pin. */
    return E_OK;                            /* Return E_OK. */
}

/******************************************************************************
 * Name         : DIO_ReadPin                                                 *
 * Inputs       : port & pin                                                  *
 * Outputs      : data                                                        *
 * Return Value : E_status                                                    *
 * Description  : Reads DIO pins.                                             *
 ******************************************************************************/
E_status DIO_ReadPin(port_t port, pin_t pin, diodata_t* data)
{
uint32_t base;                              /* Port base address */
uint8_t pin_data;                           /* Pin data */

    /* Check if selected port is not supported by hardware & pointer is null. */
    if ((port > MAX_PORT) || (NULL_PTR == data))
    {
        return E_NOT_OK;                    /* Return E_NOT_OK. */
    }

    base = PORT(port);                      /* Get base address. */
    pin_data = HWREG(base|DATA) & pin;      /* Get required pin data. */

    /* Identify pin_data. */
    if (DIO_LOW == pin_data)
    {
        *data = DIO_LOW;                        /* Change data to low. */
    }
    else /* HIGH */
    {
        *data = DIO_HIGH;                       /* Change data to high. */
    }

    return E_OK;                            /* Return E_OK. */
}

/******************************************************************************
 * Name         : DIO_WritePin                                                *
 * Inputs       : port, pin & data                                            *
 * Outputs      : None                                                        *
 * Return Value : E_status                                                    *
 * Description  : Changes actual DIO pins voltage.                            *
 ******************************************************************************/
E_status DIO_WritePin(port_t port, pin_t pin, diodata_t data)
{
uint32_t base;                              /* Port base address */

    /* Check if selected port is not supported by hardware. */
    if (port > MAX_PORT)
    {
        return E_NOT_OK;                    /* Return E_NOT_OK. */
    }

    base = PORT(port);                      /* Get base address. */

    /* Identify Data. */
    if (DIO_HIGH == data)
    {
        HWREG(base|DATA) |= pin;            /* Set pin to high. */
    }
    else if (DIO_LOW == data)
    {
        HWREG(base|DATA) &= ~pin;           /* Set pin to low. */
    }
    else /* UNDEFINED */
    {
        return E_NOT_OK;                    /* Return E_NOT_OK. */
    }

    return E_OK;                            /* Return E_NOT_OK. */
}
