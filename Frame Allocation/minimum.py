import matplotlib.pyplot as plt

n = int(input("Enter number of processes : "))

page_sizes = []

for i in range(n):
    x = int(input(f"Enter page size for P{i+1} : "))
    page_sizes.append(x)

total = int(input("Enter total number of frames : "))
threshold = int(input("Enter minimum number of frames for each process : "))

if threshold*n > total:
    print("Allocation is not possible with given number of threshold frames")
    exit()

counts = [threshold]*n
frames = [0]*total

idx=0

for pid in range(n):
    for j in range(counts[pid]):
        if idx<total:
            frames[idx]=pid+1
            idx+=1
        else:
            break

print("Process\tFrames Allocated")
for i in range(len(counts)):
    print(f"P{i+1}\t{counts[i]}")

plt.figure(figsize = (12,3))

colors = ["red","blue","yellow","green","purple","white"]

for i,f in enumerate(frames):
    
    if f==0:
        text="free"
    else:
        text = "P" + str(f)
    
    plt.barh(0,1,1,left=i,color=colors[f-1],edgecolor="black")

    plt.text(i+0.5,0,text,ha="center",va="center")

plt.xlim(0,total)
plt.yticks([])

plt.xlabel("Frames")
plt.title("Minimum Frame Allocation")

plt.show()
    
