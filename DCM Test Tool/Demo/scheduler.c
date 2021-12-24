/****************************************************************************** 
 * Module      : Scheduler                                                    * 
 * File Name   : scheduler.h                                                  * 
 * Description : Source file for scheduler module                             * 
 * Created on  : Mar 23, 2020                                                 * 
 ******************************************************************************/

#include "scheduler.h"
#include "app.h"
#include "led.h"
#include "systick.h"

/****************************************************************************** 
 *                                                                            * 
 *                         Static Function Prototypes                         * 
 *                                                                            * 
 ******************************************************************************/

/* Calculates greatest common divisor */
static uint32_t GCD(uint32_t x, uint32_t y);

/* Calculates Lowest common multiple */
static uint32_t LCM(uint32_t x, uint32_t y);

/* Calculates hyper-period */
static uint32_t Calculate_HyperPeriod(void);

/****************************************************************************** 
 *                                                                            * 
 *                              Global Variables                              * 
 *                                                                            * 
 ******************************************************************************/

/* Global variable to store Hyper-period */
static volatile uint32_t g_Hyperperiod = 0;

/* Global variable to increment with every timer tick */
static uint32_t g_Tick_Count = 0;

/******************************************************************************
 * Name         : Scheduler_Init                                              *
 * Inputs       : None                                                        *
 * Outputs      : None                                                        *
 * Return Value : None                                                        *
 * Description  : Initializes scheduler.                                      *
 ******************************************************************************/
void Scheduler_Init(void)
{
    /* Pass function to be called every Systick. */
	Systick_SetCallBack(&Scheduler_NewTimerTick);

    /* Initialize tasks. */
	Task_Init();
    
    /* Calculate hyper-period */
	g_Hyperperiod = Calculate_HyperPeriod();
    
    /* Starts Systick timer */
	Systick_Start();

	/* Enable global interrupt. */
    asm(" CPSIE I");
}

/******************************************************************************
 * Name         : Scheduler_Init                                              *
 * Inputs       : None                                                        *
 * Outputs      : None                                                        *
 * Return Value : None                                                        *
 * Description  : Initializes scheduler.                                      *
 ******************************************************************************/
volatile void Scheduler_NewTimerTick(void)
{
    /* Increment tick count. */
	++g_Tick_Count;
}

/******************************************************************************
 * Name         : Scheduler_Init                                              *
 * Inputs       : None                                                        *
 * Outputs      : None                                                        *
 * Return Value : None                                                        *
 * Description  : Initializes scheduler.                                      *
 ******************************************************************************/
void Scheduler_Loop(void)
{
static uint32_t CurrentTickCount = 0;

    for (;;)
	{
        /* Starting at index 0. */
        uint8_t index = 0;

        /* Loop over tasks and execute enabled tasks. */
		for (; index < Num_Of_Tasks; ++index) if (Task[index].is_enabled)
        {
            /* Check periodicity. */
            if((g_Tick_Count % Task[index].period) == 0)
            {
                /* Execute task. */
                Task[index].code();
            }
        }
        
        /* Check if tick count reached hyper-period. */
		if (g_Tick_Count == g_Hyperperiod)
		{
            /* Reset tick count. */
            g_Tick_Count = 0;
            CurrentTickCount = 0;
		}
        
        /* Prevent multiple calls of tasks. */
        while (g_Tick_Count == CurrentTickCount)
        {
            // DO NOTHING, WAIT FOR SYSTICK INTERRUPT
        }
        
        /* Update 'CurrentTickCount'. */
        CurrentTickCount = g_Tick_Count;
	}
}

/******************************************************************************
 * Name         : GCD                                                         *
 * Inputs       : number_1, number_2                                          *
 * Outputs      : None                                                        *
 * Return Value : GCD                                                         *
 * Description  : Calculates greatest common divisor.                         *
 ******************************************************************************/
static uint32_t GCD(uint32_t x, uint32_t y)
{
    /* Check if x not equal y. */
	while (x != y)
	{
        /* Check if x is greater than y. */
		if (x > y)
		{
            /* Calculates new x. */
			x -= y;
		}
		else /* X <= Y */
		{
            /* Calculates new y. */
            y -= x;
		}
	}
    
    /* Returns GCD. */
	return x;
}

/******************************************************************************
 * Name         : LCM                                                         *
 * Inputs       : number_1, number_2                                          *
 * Outputs      : None                                                        *
 * Return Value : LCM                                                         *
 * Description  : Calculates lowest common multiple.                          *
 ******************************************************************************/
static uint32_t LCM(uint32_t x, uint32_t y)
{
uint32_t divisor = 1;               /* Common divisor */
uint32_t lcm = 1;                   /* Lowest common multiple value */

    /* Calculate GCD of x and y. */
	divisor = GCD(x, y);      

    /* Calculates LCM of x and y. */
    lcm = (x * y) / divisor;
    
    /* Return lowest common multiple */
	return lcm;
}

/******************************************************************************
 * Name         : Calculate_HyperPeriod                                       *
 * Inputs       : None                                                        *
 * Outputs      : None                                                        *
 * Return Value : None                                                        *
 * Description  : Calculates hyper-period.                                    *
 ******************************************************************************/
static uint32_t Calculate_HyperPeriod(void)
{
uint8_t index = 1;                          /* Looping index */
uint32_t hyperperiod = Task[0].period;      /* First task period */
	
    /* Loop over tasks period to get hyper-period. */
    while (index < Num_Of_Tasks)
    {
        /* Calculate least common multiple. */
		hyperperiod = LCM(hyperperiod, Task[index].period);
        
        /* Increase index by 1. */
		++index;
	}
    
    /* Return hyper-period. */
	return hyperperiod;
}
