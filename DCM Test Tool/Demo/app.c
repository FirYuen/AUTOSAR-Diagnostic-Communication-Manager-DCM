#include "app.h"
#include "button.h"
#include "indicator_led.h"
#include "uart_stdio.h"

//0x12 0x34 0x56 0x78 0x00

void logic(void)
{
static int c = 0;

    UART0_printf("Magdy!");

    if (g_UART0_DeliveryFlag)
    {
        g_UART0_DeliveryFlag = false;
        if ((g_UART0_BufferRX[0] == 0x12) &&
            (g_UART0_BufferRX[1] == 0x34) &&
            (g_UART0_BufferRX[2] == 0x56) &&
            (g_UART0_BufferRX[3] == 0x78) &&
            (g_UART0_BufferRX[4] == 0x00))
        {
            IndicatorLED_SetColor((++c)%5);
        }

        if ((g_UART0_BufferRX[0] == 0xff) &&
            (g_UART0_BufferRX[1] == 0xff) &&
            (g_UART0_BufferRX[2] == 0xff) &&
            (g_UART0_BufferRX[3] == 0x00))
        {
            IndicatorLED_SetColor(COLOR_GREEN);
        }
    }
}

Task_t Task[] =
{
    {
        .is_enabled = true,
        .code = UART0_ReceiveMsg,
        .period = 1
    },
    {
        .is_enabled = true,
        .code = UART0_TransmitMsg,
        .period = 1
    },
    {
        .is_enabled = true,
        .code = logic,
        .period = 10
    }
};

void Task_Init(void)
{
    IndicatorLED_Init();
    IndicatorLED_SetColor(COLOR_GREEN);
    
    Button_Init(SW1_CH);
    Button_Init(SW2_CH);
    
    UART0_Init();
}

const uint8_t Num_Of_Tasks = (sizeof(Task) / sizeof(Task_t));


