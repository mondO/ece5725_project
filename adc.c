#include <stdio.h>
#include <time.h>

#include <wiringPi.h>
#include <ads1115.h>
#define MY_BASE 2222
  

int main() {
    ads1115Setup (MY_BASE, 0x48) ;
    digitalWrite(1, 2); // set gain to 2
    digitalWrite(1, 860); // set data rate to 860 samples/sec
    int ch0 = analogRead (MY_BASE + 0) ;
    int ch3 = analogRead (MY_BASE + 3) ;
    printf("hello world! %d, %d\n", ch0, ch3);

    int samples[1000];
    int i;
    time_t start_time, end_time;
    double runtime;
    time(&start_time);
    for (i = 0; i < 1000; i++) {
        samples[i] = analogRead(MY_BASE + 3);
    }
    time(&end_time);
    runtime = difftime(end_time, start_time);
    printf("1000 samples collected in %f seconds, rate=%f samples/second", runtime, 1000.0/runtime);

    return 0;

}
