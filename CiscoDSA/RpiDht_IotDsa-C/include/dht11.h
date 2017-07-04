/*
 *  dht.c:
 *      read temperature and humidity from DHT11 or DHT22 sensor
 */
 
#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
 
#define MAX_TIMINGS     85
#define DHT_PIN         7       /* GPIO-22 */
 
void read_dht_data(float* Temperature, float* Humidity);

