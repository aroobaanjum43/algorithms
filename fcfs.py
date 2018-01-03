# FIRST COME FIRST SERVE ALGOOO
#THE WAITING TIME IN THIS IS DEPEND ON EXECUTION DURATION OF PREVIOUS PROCESS
#INITIALY EVERY PROCESS HAS WAITING TIME 0 BECAUSE IT IS NON PREEMTIVE...

from __future__ import print_function

def main():
    Bt = [4, 6, 3, 5, 7]
    TurnAT = 0
    Wt = 0
    avwt=0
    print("Enter total number of processes in range 1-5:")
    n=int(raw_input())
    print("\n  Process no.    Burst Time  Waiting Time   Turnaround Time")
    i=0
    while i<n:
        TurnAT=Bt[i]+Wt       #because Wt=ft-at-bt
        avwt += Wt
        print(i+1,"\t\t\t\t " ,Bt[i],"\t\t\t\t "  , Wt,"\t\t\t\t " ,  TurnAT)
        Wt += Bt[i]
        i+=1
    avwt /= i
    print("\n  Average Waiting Time", avwt)


    return 0;

main()
