

import random
import matplotlib.pyplot as plt
from collections import deque

n = int(input("Enter number of processes: "))
tq = int(input("Enter Time Quantum: "))

processes=[]

print("Randomly Generated Arrival Times(AT) and Burst Times(BT) : ")

for i in range(n):
    at = random.randint(0,5)
    bt = random.randint(1,6)
    processes.append([f"P{i+1}",at,bt])
    print(f"P{i+1} -> AT: {at} , BT: {bt}")

processes.sort(key = lambda x:x[1])

rem_bt = [p[2] for p in processes]

current_time=0
visited=[False]*n
completed=0
wt=[0]*n
tat=[0]*n
ct = [0]*n
q=deque()
timeline=[]

while completed<n:
    for i in range(n):
        if processes[i][1] <=current_time and not visited[i]:
            q.append(i)
            visited[i]=True
        
    if not q:
        current_time+=1
        continue
            
    idx=q.popleft()
    pid,at,bt = processes[idx]
    exec_time=min(tq,rem_bt[idx])

    timeline.append([pid,current_time,exec_time])

    current_time+=exec_time
    rem_bt[idx] -= exec_time
    
    for i in range(n):
        if processes[i][1] <=current_time and not visited[i]:
            q.append(i)
            visited[i]=True

    if rem_bt[idx]>0:
        q.append(idx)
    elif rem_bt[idx]==0:
        completed+=1
        ct[idx]=current_time
        tat[idx]=ct[idx] - at
        wt[idx] = tat[idx]-bt

print("\nPID\tAT\tBT\tWT\tTAT")

for i in range(n):
    pid,at,bt = processes[i]
    print(f"{pid}\t{at}\t{bt}\t{wt[i]}\t{tat[i]}")

print("Average Waiting Time: ",round(sum(wt)/n,2))
print("Average Turn Around Time: ",round(sum(tat)/n,2))

fig,ax=plt.subplots()

for task in timeline:
    ax.barh(1,task[2],left=task[1],color='yellow',edgecolor='skyblue')
    ax.text(task[1]+task[2]/2,1,task[0],ha='center',va='center')

plt.xlabel("Time")
plt.yticks([])
plt.title("Round Robin Scheduling Gantt Chart")

plt.show()
