CC=gcc
CFLAGS=-I/usr/local/include -L/usr/local/lib -lwiringPi

adc_test: adc.o
	$(CC) $(CFLAGS) -o adc_test adc.o
