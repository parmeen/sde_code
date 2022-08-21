# sde_code
21/8/2022 amazon sde code
Explain your approach and time and space complexity of your solution.

The command-line shell that you use only lets you delete processes that form a single contiguous segment of a given fixed size. The size of a contiguous segment is the number of contiguous processes in main memory. Find the minimum amount of main memory used by all your processes in your instance after you delete a contiguous segment of processes.

Example:
process = [10,4,8,13,20]
m = 2
process 1 10 kb
process 2 4 kb
process 3 8 kb
process 4 13 kb
process 5 20 kb

Select a fixed contiguous segment size of m = 2. The best single contiguous segment of size 2 to delete is the segment composed of process 5, which is 20 kb and process 4 which is 13 kb. This results in the minimum total main memory consumption of 10 kb + 4 kb + 8 kb = 22 kb.

Minimize memory has two parameters:
int process[n]: kilobytes occupied by each process
int m: the fixed number of contiguous applications in a segment
returns: int: the minimum amount of main memory taken up after the deletion of a contiguous segment of size m
