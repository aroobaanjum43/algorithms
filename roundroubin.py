
from __future__ import print_function

def main():

    processes={}
    Exectime=[]
    arrivaltime=[]
    runningQueue=[]
    ts=0
    wt=0
    tat=0
    x=0

    print ("Enter time slice")
    ts=input()
    n=input("Enter total number of processes: ")
    for i in range(0,n):
        print ("Enter execution time of process :",i)
        et=input()
        Exectime.append(et)
	print ("Enter arrival timeof process ",i)
	at=input()
	arrivaltime.append(at)
        processes[i+1]=[Exectime[i]]

    for i in range (0,n):
	    for j in range (0,n):
		    if(arrivaltime[i]<arrivaltime[j]):
			    temp=arrivaltime[i]
			    arrivaltime[i]=arrivaltime[j]
			    arrivaltime[j]=temp

    print ("Process ID  \tarrival time \t  Waiting time")
    for i in range(0,n):
            tat = Exectime[i] + wt
            print(i, "\t\t\t", wt, "\t\t\t", tat)
            wt += Exectime[i]
            awt += wt

    return 0
main()