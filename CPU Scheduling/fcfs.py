
#-------------------------------------------------FCFS Scheduling-----------------------------------------------

import random
import matplotlib.pyplot as plt

n = int(input("Enter number of processes : "))

processes=[]

print("Randomly Generated Arrival Times(AT) and Burst Times: ")

for i in range(n):
    at = random.randint(0,5)
    bt = random.randint(1,6)
    processes.append([f"P{i+1}",at,bt])
    print(f"P{i+1} -> AT: {at} , BT: {bt}")

processes.sort(key = lambda x:x[1])

current_time = 0
timeline=[]

total_wt=0
total_tat=0

print("\nPID\tAT\tBT\tWT\tTAT")

for p in processes:
    pid,at,bt = p

    if current_time<at:
        current_time = at
    
    wt = current_time - at
    tat = wt+bt


    print(f"{pid}\t{at}\t{bt}\t{wt}\t{tat}")
    
    timeline.append([pid,current_time,bt])
    total_wt +=wt
    total_tat+=tat

    current_time+=bt

print("\nTotal Waiting Time: ",round(total_wt/n,2))
print("Total Turn Around Time: ",round(total_tat/n,2))

fig,ax = plt.subplots()

for task in timeline:
    ax.barh(1,task[2],left=task[1],color='purple',edgecolor='black')
    ax.text(task[1]+task[2]/2,1,task[0],ha='center',va='center',color='black',fontsize=10)

plt.xlabel("Time")
plt.yticks([])
plt.title("FCFS Scheduling - Gantt Chart")

plt.show()