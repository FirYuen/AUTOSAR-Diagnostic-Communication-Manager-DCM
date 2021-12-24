/****************************************************************************** 
 * Module      : Button                                                       * 
 * File Name   : button.h                                                     * 
 * Description : Header file for button module                                * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#ifndef BUTTON_H_
#define BUTTON_H_

#include "common.h"
#include "diodrv.h"

/****************************************************************************** 
 *                                                                            * 
 *                                Definitions                                 * 
 *                                                                            * 
 ******************************************************************************/

/* Possible switches states */ 
#define IS_PRESSED    	( DIO_LOW )
#define IS_NOT_PRESSED	( DIO_HIGH )

/* Tiva C on-board switches */
#define SW1_CH      	( 0 )
#define SW2_CH      	( 1 )

/****************************************************************************** 
 *                                                                            * 
 *                              Shared Variables                              * 
 *                                                                            * 
 ******************************************************************************/

/* Shared Switch 1 status */
extern ButtonStatusType g_SW1_Status;

/* Shared Switch 2 status */
extern ButtonStatusType g_SW2_Status;
   
/****************************************************************************** 
 *                                                                            * 
 *                               Configuration                                * 
 *                                                                            * 
 ******************************************************************************/

/* Button channels */
static button_ch button[] =
{
    { /* Channel 0: TiVA-C on-board SW1 */
        .port = PORT_F,
        .pin  = PIN_0,
    },
  
    { /* Channel 1: TiVA-C on-board SW2 */
        .port = PORT_F,
        .pin  = PIN_4
    }
};

/****************************************************************************** 
 *                                                                            * 
 *                            Function Prototypes                             * 
 *                                                                            * 
 ******************************************************************************/

/* Initializes selected button. */
extern E_status Button_Init(channel_t);

/* Reads selected button status. */
extern E_status Button_UpdateStatus(channel_t, diodata_t* status);


#endif /* BUTTON_H_ */
