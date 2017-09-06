#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#define CLOCK CLOCK_PROCESS_CPUTIME_ID


// returns the difference in milliseconds.
long timespec_diff(struct timespec *strt, struct timespec *stp) {
    return (stp->tv_sec-strt->tv_sec-1)*1000+(1000000000+stp->tv_nsec-strt->tv_nsec)/1000000;
}


int main(int argn,char **argv){
    int n,sum, *A,step;
    long i,j;
    struct timespec ptime,ctime;
    // Read ’n’ and the ’step’ size.
    sscanf(argv[1], "%d",&n);
    sscanf(argv[2], "%d",&step);
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
        for (i=0; i<n; i=i+step) sum += A[i];
    // a nop again...
    asm ("nop");
    // Get the finishing time
    clock_gettime(CLOCK,&ctime);
    printf("size: %ld, step: %d and time Elapsed: %ld milliseconds\n",n*sizeof(int),step,timespec_diff(&ptime,&ctime));
    // Return something to fool -O3
    return sum%2;
}
