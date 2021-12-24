/****************************************************************************** 
 * Module      : None                                                         * 
 * File Name   : types.h                                                      * 
 * Description : Header file for common types used                            * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#ifndef TYPES_H_
#define TYPES_H_

#include "types.h"
#include "common.h"

/****************************************************************************** 
 *                                                                            * 
 *                                 Datatypes                                  * 
 *                                                                            * 
 ******************************************************************************/

/* Error status data-type */
typedef uint8_t E_status;

/* Increase readability */
typedef uint8_t channel_t;
typedef uint8_t port_t;
typedef uint8_t pin_t;
typedef uint8_t diomode_t;
typedef uint8_t diodata_t;
typedef uint8_t color_t;

/* Default DIO data-type */
typedef struct
{
    port_t port;
    pin_t pin;
} dio_ch;

/* LED channel data-type */
typedef dio_ch led_ch;

/* Button channel data-type */
typedef dio_ch button_ch;

/* Button status data-type */
typedef uint8_t ButtonStatusType;

/* Task data-type */
typedef struct
{
    bool is_enabled;        /* Task enable flag */
	uint8_t period;	        /* Task periodicity */
    void (*code)(void);     /* Task pointer to function */
} Task_t;


#endif /* TYPES_H_ */
