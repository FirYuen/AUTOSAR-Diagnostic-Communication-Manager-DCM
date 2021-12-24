#ifndef UART_STDIO_H_
#define UART_STDIO_H_

#include <stdint.h>
#include <stdbool.h>
#include "inc/hw_memmap.h"
#include "driverlib/sysctl.h"
#include "driverlib/uart.h"
#include "driverlib/pin_map.h"
#include "driverlib/gpio.h"

/****************************************************************************** 
 *                                                                            * 
 *                               Configuration                                * 
 *                                                                            * 
 ******************************************************************************/

/* Baud Rate */
#define UART_BAUDRATE   (115200)

/* End-of-Frame byte (EOF) */
#define UART_EOF        (0x00)

/****************************************************************************** 
 *                                                                            * 
 *                              Shared Variables                              * 
 *                                                                            * 
 ******************************************************************************/

/* UART0 buffer for TX */
extern uint8_t g_UART0_BufferTX[16];

/* UART0 buffer for RX */
extern uint8_t g_UART0_BufferRX[16];

/* UART0 delivered bytes counter */
extern uint8_t g_UART0_DeliveredBytes;

/* UART0 message delivery flag */
extern bool g_UART0_DeliveryFlag;

/* UART0 transmit flag */
extern bool g_UART0_TransmitFlag;

/****************************************************************************** 
 *                                                                            * 
 *                            Function Prototypes                             * 
 *                                                                            * 
 ******************************************************************************/

/* Initializes UART0 */
extern void UART0_Init(void);

/* Prints string to console */
extern void UART0_printf(const char *);

/* Receives UART0 Message into RX Buffer if any */
extern void UART0_ReceiveMsg(void);

/* Transmits Message over UART0 from TX Buffer if any */
extern void UART0_TransmitMsg(void);


#endif /* UART_STDIO_H_ */
