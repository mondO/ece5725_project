CC=gcc
CFLAGS=-I/usr/local/include -L/usr/local/lib -lwiringPi
OUTDIR=./build

adc_test: adc.o
	$(CC) $(CFLAGS) -o $(OUTDIR)/adc_test adc.o

raw: rawMCP3008.o
	$(CC) -Wall -pthread -o $(OUTDIR)/raw rawMCP3008.o -lpigpio -lrt
 
