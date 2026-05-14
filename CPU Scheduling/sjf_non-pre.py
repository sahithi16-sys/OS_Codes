import random
import matplotlib.pyplot as plt

n = int(input("Enter number of processes: "))

processes=[]

for i in range(0,n):
    at = random.randint(0,5)
    bt = random.randint(1,6)
    processes.append([f"P{i+1}",at,bt])
    print(f"P{i+1}-> AT : {at} , BT : {bt}")

completed = 0
current_time = 0
total_tat = 0
total_wt = 0
timeline = []
visited = [False]*n

print("\nPID\tAT\tBT\tWT\tTAT")

while completed<n:

    min_bt = float('inf')
    idx=-1
    
    for i in range(n):
        if processes[i][1]<=current_time and not visited[i]:
            if processes[i][2]<min_bt:
                min_bt = processes[i][2]
                idx = i
            
            elif processes[i][2]==min_bt:
                if processes[i][1]<processes[idx][1]:
                    idx=i
    
    if idx==-1:
        current_time +=1
    else:
        pid,at,bt = processes[idx]
        wt = current_time - at
        tat=wt+bt
        visited[idx]=True
        total_wt +=wt
        total_tat +=tat
        completed+=1
        print(f"{pid}\t{at}\t{bt}\t{wt}\t{tat}")

        if current_time<at:
            current_time=at
        timeline.append((pid,current_time,bt))
        current_time+=bt


print("Average Waiting Time: ",round(total_wt/n,2))
print("Average Turn Around Time: ",round(total_tat/n,2))


fig,ax=plt.subplots()

for task in timeline:
    ax.barh(1,task[2],left=task[1],color='yellow',edgecolor='black')
    ax.text(task[1]+task[2]/2,1,task[0],ha='center',va='center')

plt.xlabel("Time")
plt.yticks([])
plt.title("SJF Non-Preemptive  Gantt Chart")

plt.show()