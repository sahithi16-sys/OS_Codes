n = int(input("Enter number of disks(>=20) : "))

disk = [-1]*n

print("Enter indices of Used Blocks : ")
filled = list(map(int,input().split()))

for i in filled:
    disk[i]="USED"

print("Initial Disk Status : ")
print(disk)

f = int(input("Enter number of files(>=3) : "))

files=[]

for _ in range(f):
    name = input("Enter file name : ")
    size = int(input(f"Enter number of blocks for file {name} : "))
    files.append((name,size))

temp_disk = disk.copy()

for name,size in files:
    free_blocks = [i for i in range(n) if temp_disk[i]==-1]

    if len(free_blocks) <size+1:
        print(f"{name}-> Allocation Failed")
        continue

    inode = int(input(f"Enter inode for file {name} : "))
    allocated = list(map(int,input(f"Enter disk indices for {name} : ").split()))

    if inode in range(n) and temp_disk[inode]==-1 and all(b in range(n) and temp_disk[b]==-1 for b in allocated):
        temp_disk[inode] = "INOODE"
        for b in allocated:
            temp_disk[b]="USED"
        
        print(f"{name} : INODE = {inode}")
        print("Blocks : ",allocated)
        print(f"Diagram : {inode} -> ", allocated)
    else:
        print(f"{name} -> Allocation Failed due to invalid/used blocks")
