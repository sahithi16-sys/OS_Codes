import random
import matplotlib.pyplot as plt


n = int(input("Enter number of processes: "))

processes=[]

print("Randomly Generated Arrival Times(AT) , Burst Times(BT) and Priority :")

for i in range(n):
    at = random.randint(0,5)
    bt = random.randint(1,6)
    priority = random.randint(1,5)
    processes.append([f"P{i+1}",at,bt,priority])
    print(f"P{i+1} -> AT: {at} , BT: {bt}, Priority : {priority}")


current_time = 0
completed = 0
timeline=[]
visited = [False]*n
total_tat = 0
total_wt=0

print("\nPID\tAt\tBT\tWT\tTAT")

while completed<n:
    min_pr = float('inf')
    idx=-1

    for i in range(n):
        if processes[i][1] <= current_time and not visited[i]:
            if idx==-1 or processes[i][3]<min_pr or (processes[i][3]==min_pr and processes[i][1] < processes[idx][1]):
                idx=i
                min_pr = processes[i][3]
    
    if idx==-1:
        current_time+=1
        continue

    pid,at,bt,pr=processes[idx]

    if current_time<at:
        current_time=at
    
    wt = current_time - at
    tat = bt+wt

    total_tat +=tat
    total_wt+=wt
    print(f"{pid}\t{at}\t{bt}\t{wt}\t{tat}")
    timeline.append([pid,current_time,bt])
    current_time +=bt
    completed+=1
    visited[idx]=True

print("\nTotal Waiting Time: ",round(total_wt/n,2))
print("Total Turn Around Time: ",round(total_tat/n,2))


fig,ax = plt.subplots()

for task in timeline:
    ax.barh(1,task[2],left=task[1],color='yellow',edgecolor='black')
    ax.text(task[1]+task[2]/2,1,task[0],ha='center',va='center')

plt.xlabel("Time")
plt.yticks([])
plt.show()