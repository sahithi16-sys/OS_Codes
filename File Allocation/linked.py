n = int(input("Enter number of disks : "))

disk = [-1]*n

filled = list(map(int,input("Enter indices of used blocks : ").split()))

for i in filled:
    disk[i]="USED"

print("Initial Disk Status : ")
print(disk)

f = int(input("Enter number of files(>=3) : "))
files = []

for _ in range(f):
    name = input("Enter file name : ")
    size = int(input(f"Enter blocks required for file {name} : "))
    files.append((name,size))

temp_disk = disk.copy()

for name,size in files:
    free_blocks = [i for i in range(n) if temp_disk[i]==-1]

    if len(free_blocks) < size:
        print(f"{name} : Allocation failed")
        continue

    allocated = list(map(int,input(f"Enter block indices for {name} : ").split()))

    if len(allocated)==size and all(b in range(n) and temp_disk[b]==-1 for b in allocated):
        for b in allocated:
            temp_disk[b]= "USED"
        
        print(f"{name} : Blocks = ",allocated)
        print("Diagram :", " ->".join(f"[{b}]" for b in allocated) , "->NULL")
    else:
        print(f"{name} : Allocation failed")