#include "uart_stdio.h"

/* UART0 buffer for TX */
uint8_t g_UART0_BufferTX[16] = {0};

/* UART0 buffer for RX */
uint8_t g_UART0_BufferRX[16] = {0};

/* UART0 delivered bytes counter */
uint8_t g_UART0_DeliveredBytes = 0;

/* UART0 message delivery flag */
bool g_UART0_DeliveryFlag;

/* UART0 transmit flag */
bool g_UART0_TransmitFlag;

void UART0_Init(void)
{
    /* Set MCU clock. */
    SysCtlClockSet(SYSCTL_SYSDIV_5|
                   SYSCTL_USE_PLL|
                   SYSCTL_XTAL_16MHZ|
                   SYSCTL_OSC_MAIN);

    /* Enable UART0 module & its port. */
    SysCtlPeripheralEnable(SYSCTL_PERIPH_UART0);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOA);

    /* Configure UART0 pins. */
    GPIOPinConfigure(GPIO_PA0_U0RX);
    GPIOPinConfigure(GPIO_PA1_U0TX);
    GPIOPinTypeUART(GPIO_PORTA_BASE,
                    GPIO_PIN_0|GPIO_PIN_1);
    
    /* Enable UART0 interrupt if needed. */
    UARTIntEnable(UART0_BASE, UART_INT_RX | UART_INT_RT);
    
    /* Configure UART0. */
    UARTConfigSetExpClk(UART0_BASE, 
                        SysCtlClockGet(),
                        UART_BAUDRATE,
                        (UART_CONFIG_WLEN_8|
                         UART_CONFIG_PAR_NONE|
                         UART_CONFIG_STOP_ONE));

    /* Send EOF for initialization. */
    //UARTCharPut(UART0_BASE, UART_EOF);
}

void UART0_printf(const char *str)
{
uint32_t index;                 /* string index */

    /* Loop over until a 'null character'. */
    for(index = 0; (str[index] != '\0'); ++index)
	{
        /* Send char. */
		UARTCharPut(UART0_BASE, str[index]);
	}
}

void UART0_TransmitMsg(void)
{
uint8_t index;

    if (g_UART0_TransmitFlag == true)
    {
        g_UART0_TransmitFlag = false;

        index = 0;
        while (g_UART0_BufferTX[index] != UART_EOF)
        {
            UARTCharPut(UART0_BASE, g_UART0_BufferTX[index]);
            ++index;
        }
        UARTCharPut(UART0_BASE, UART_EOF);
    }
}


void UART0_ReceiveMsg(void)
{
static uint8_t index = 0;
uint8_t rx_char;

    if (g_UART0_DeliveryFlag == false)
    {
        if (UARTCharsAvail(UART0_BASE))
        {
            rx_char = UARTCharGet(UART0_BASE);

            g_UART0_BufferRX[index] = rx_char;
            ++index;

            if (rx_char == UART_EOF)
            {
                g_UART0_DeliveredBytes = (index - 1);
                index = 0;
                g_UART0_DeliveryFlag = true;
            }
        }
    }
}
