n = int(input("Enter number of disks: "))

disk=[-1]*n

print("Enter indices of used blocks: ")
filled = list(map(int,input().split()))

for i in filled:
    disk[i]="USED"

print("Initial Disk Status: ")
print(disk)

f = int(input("Enter number of files(>=3): "))

files=[]

for i in range(f):
    name = input("Enter file name: ")
    size=int(input(f"Enter blocks required for file {name}: "))
    files.append((name,size))

temp_disk = disk.copy()

for name,size in files:
    allocated=[]
    
    for i in range(n-size+1):
        if all(temp_disk[j]==-1 for j in range(i,i+size)):
            for j in range(i,i+size):
                temp_disk[j]= "USED"
                allocated.append(j)
            break    
        
    if allocated:
        print(f"{name} : Blocks = ",allocated)
        print("Diagram: ","->".join(f"[{a}]" for a in allocated))
    else:
        print(f"{name} : Allocation failed")
    