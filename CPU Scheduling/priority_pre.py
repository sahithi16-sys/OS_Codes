import random
import matplotlib.pyplot as plt


n = int(input("Enter number of processes: "))

processes=[]
print("Randomly Generated Arrival Times(AT) , Burst Times(BT) and Priority: ")

for i in range(n):
    at = random.randint(0,5)
    bt = random.randint(1,6)
    priority = random.randint(1,5)
    processes.append([f"P{i+1}",at,bt,priority])
    print(f"P{i+1} -> AT: {at} , BT: {bt}, Priority : {priority}")

current_time=0
completed=0
timeline=[]
rem_bt = [p[2] for p in processes]

wt_list=[0]*n
tat_list=[0]*n

prev=-1

while completed<n:
    idx=-1
    min_pr=float('inf')

    for i in range(n):
        if processes[i][1]<=current_time and rem_bt[i]>0:
            if idx==-1 or processes[i][3]<min_pr or (processes[i][3]==min_pr and processes[i][1]<processes[idx][1]):
                idx=i
                min_pr=processes[i][3]
    
    if idx==-1:
        current_time+=1
        continue

    pid,at,bt,priority = processes[idx]

    if prev!=idx:
        timeline.append([pid,current_time,1])
    else:
        timeline[-1][2]+=1

    rem_bt[idx]-=1
    prev=idx
    current_time+=1

    if rem_bt[idx]==0:
        completed+=1
        tat_list[idx]=current_time-at
        wt_list[idx]=tat_list[idx]-bt

print("\nPID\tAT\tBT\tPR\tWT\tTAT")

for i in range(n):
    pid,at,bt,priority = processes[i]
    print(f"{pid}\t{at}\t{bt}\t{priority}\t{wt_list[i]}\t{tat_list[i]}")

print("Average Waiting Time: ",round(sum(wt_list)/n,2))
print("Average Turn Around Time: ",round(sum(tat_list)/n,2))

fig,ax=plt.subplots()

for task in timeline:
    ax.barh(1,task[2],left=task[1],color='yellow',edgecolor='red')
    ax.text(task[1]+task[2]/2,1,task[0],ha='center',va='center')

plt.xlabel("Time")
plt.yticks([])
plt.title("Priority Preemptive Gantt Chart")

plt.show()

