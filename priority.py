
from __future__ import print_function

def main():
    bt = [4, 6, 3, 5, 7]
    prio=[2,3,1,4,5]
    TurnAT = 0
    wt = 0
    avwt=0
    print("Enter total number of processes in range 1-5:")
    n=int(raw_input())
    print("\n  Process no.    Waiting Time   Turnaround Time")
    i = 0
    while i < n:
        j = 0
        while j < n:
            if (prio[i] < prio[j]):
                swap = bt[i]
                bt[i] = bt[j]
                bt[j] = swap
            j += 1
        i += 1
    i = 0
    while i < n:
        TurnAT = bt[i] + wt
        avwt += wt
        print(i + 1,  "\t\t\t\t ", wt, "\t\t\t\t ", TurnAT)
        wt += bt[i]
        i += 1
    avwt /= i
    print("\n  Average Waiting Time", avwt)

    return 0;


main()