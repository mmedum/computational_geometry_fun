#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <limits.h>
#define CLOCK CLOCK_PROCESS_CPUTIME_ID


// returns the difference in milliseconds.
long timespec_diff(struct timespec *strt, struct timespec *stp) {
    return (stp->tv_sec-strt->tv_sec-1)*1000+(1000000000+stp->tv_nsec-strt->tv_nsec)/1000000;
}

int run_algo(int n, int step){
    int *A,sum;
    FILE *pFile;
    long i,j;
    struct timespec ptime,ctime;
    // Allocate and initialize array A so -O3 does not annoy us.
    A = (int *)malloc(n*sizeof(int));
    for (i=0; i<n ; i++) A[i]=i;
    // We now prepare to do the thing ...
    long X=1024*1024*128;
    long max=X/n*step;
    // Get the current time.
    clock_gettime(CLOCK,&ptime);
    // Insert a nop instruction so we can easily find this place in the assembly code if
    // we ever wish so.
    asm ("nop");
    // The real thing ...
    for (j=0 ; j<max ; j++)
        for (i=0; i<n; i=i+step){
            sum += A[i];
        }
    // a nop again...
    asm ("nop");
    // Get the finishing time
    clock_gettime(CLOCK,&ctime);
    printf("size: %ld, step: %d and time Elapsed: %ld milliseconds\n",n*sizeof(int),step,timespec_diff(&ptime,&ctime));
    pFile = fopen("output.csv", "a");
    fprintf(pFile, "%ld,%d,%ld\n",n*sizeof(int),step,timespec_diff(&ptime,&ctime));
    fclose(pFile);
    free(A);
    // Return something to fool -O3
    return sum%2;
}

void run_test(int n, int step){
    int i, number;
    // max is 2^20
    for(i=step; i<1048576; i=i*2){
        number = n;
        do {
            run_algo(number, i);
            number = number * 2;
        } while( number < INT_MAX/sizeof(int));
    }
}

int main(int argn,char **argv){
    int n, step;
    // Read ’n’ and the ’step’ size.
    sscanf(argv[1], "%d",&n);
    sscanf(argv[2], "%d",&step);
    run_test(n, step);
    return 0;
}

