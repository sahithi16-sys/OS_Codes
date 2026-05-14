n = int(input("Enter number of processes : "))
m = int(input("Enter number of resources : "))

total = list(map(int,input(f"Enter {m} total resources : ").split()))

if len(total)!=m:
    print("ERROR : Total vector size must be equal to number of resources!")
    exit()

max = []
print("Enter Max Matrix : ")

for i in range(n):
    row=list(map(int,input(f"Enter 3 values for P{i+1} : ").split()))  
    if len(row)!=m:
        print("ERROR : Invalid number of resources!")
        exit()
    max.append(row)

allocation = []

print("Enter Allocation Matrix : ")

for i in range(n):
    row=[]
    row=list(map(int,input(f"Enter 3 values for P{i+1} : ").split()))  
    
    if len(row)!=m:
        print("ERROR : Invalid number of resources!")
        exit()
    for j in range(m):
        if row[j] > max[i][j]:
            print("ERROR : Allocated Resources cannot be more than the maximum possible resources!")
            exit()
    allocation.append(row)

need=[]

for i in range(n):
    row = []
    for j in range(m):
        x = max[i][j] - allocation[i][j]
        if x<0:
            print("ERROR : Need value cannot be negative!")
            exit()
        row.append(x)
    need.append(row)

allocated = [0]*m

for j in range(m):
    for i in range(n):
        allocated[j] += allocation[i][j]

available=[0]*m

for j in range(m):
    available[j] = total[j] - allocated[j]

work = available.copy()

print("Initial Work : ",work)

finish = [False]*n
safe_seq=[]
step=1
alloc= False

while True:
    for i in range(n):
        if not finish[i] and all(need[i][j]<=work[j] for j in range(m)):
            
            finish[i]= True
            alloc=True
            safe_seq.append(i+1)

            print(f"Step {step} : Process P{i+1} executes")
            print("Work Before : ",work)
            for j in range(m):
                work[j]+=allocation[i][j]
            print("Work After : ",work)
    
    if not alloc:
        break
    if all(finish):
        break

if all(finish):
    print("System is in Safe State")
    print("Safe sequence : ",safe_seq)
else:
    print("System is in Unsafe/Deadlock State")





