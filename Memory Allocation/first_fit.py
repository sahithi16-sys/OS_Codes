import matplotlib.pyplot as plt

n = int(input("Enter number of files : "))
m = int(input("Enter number of blocks : "))

files = list(map(int,input("Enter file sizes : ").split()))

blocks = list(map(int,input("Enter block size (-1 for USED) : ").split()))

for i in range(m):
    if blocks[i]==-1:
        blocks[i]="USED"

print("Files")
print("File\tFile Size")
for i in range(n) :
    print(f"F{i+1}\t{files[i]}")

print("Initial Memory")
print("Block\tBlock Size")
for i in range(m):
    print(f"B{i+1}\t{blocks[i]}")

allocation = [-1]*n

used=[False]*m
block_alloc = [-1]*m
free_blocks=[]

for i in range(m):
    if allocation[i]==-1:
        continue
    if not blocks[i]=="USED":
        free_blocks.append((i,blocks[i]))

for i in range(n):
    for idx,size in free_blocks:
        if not used[idx] and size>=files[i]:
            allocation[i] = idx
            used[idx]=True
            block_alloc[idx]=i
            break

print("File\tSize\tSegment")

for i in range(n):
    if allocation[i] == -1:
        print(f"F{i+1}\t{files[i]}MB\tNA")
    else:
        print(f"F{i+1}\t{files[i]}MB\tB{allocation[i]+1}")

plt.figure(figsize=(12,3))

for i in range(m):
    if blocks[i]=="USED":
        color="blue"
        value = "O"
    elif used[i]:
        color="yellow"
        value = f"F{block_alloc[i]+1}"
    else:
        color="white"
        value="-"

    plt.barh(0,1,left=i,color=color,edgecolor="black")
    plt.text(i+0.5,0,str(value),ha='center',va='center')

plt.xticks([])
plt.yticks([])

plt.xlabel("Blocks")

plt.title("First Fit Memory Allocation")
plt.show()