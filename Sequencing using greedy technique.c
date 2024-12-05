#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int profit;
    int deadline;
} Job;

int compare_jobs(const void *a, const void *b) {
    Job *job1 = (Job *)a;
    Job *job2 = (Job *)b;
    double ratio1 = (double)job1->profit / job1->deadline;
    double ratio2 = (double)job2->profit / job2->deadline;
    return ratio2 - ratio1;  // Descending order of profit per deadline
}

void job_sequencing(Job jobs[], int n) {
    qsort(jobs, n, sizeof(Job), compare_jobs);

    int max_profit = 0;
    Job scheduled_jobs[n];
    int num_scheduled = 0;

    for (int i = 0; i < n; i++) {
        if (jobs[i].deadline > num_scheduled) {
            scheduled_jobs[num_scheduled] = jobs[i];
            max_profit += jobs[i].profit;
            num_scheduled++;
        }
    }

    printf("Maximum profit: %d\n", max_profit);
    printf("Sequence of jobs:\n");
    for (int i = 0; i < num_scheduled; i++) {
        printf("Job %d (profit %d, deadline %d)\n", i + 1, scheduled_jobs[i].profit, scheduled_jobs[i].deadline);
    }
}

int main() {
    Job jobs[] = {
        {20, 2},
        {10, 1},
        {30, 3},
        {5, 2}
    };
    int n = sizeof(jobs) / sizeof(jobs[0]);

    job_sequencing(jobs, n);

    return 0;
}

