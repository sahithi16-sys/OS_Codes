import matplotlib.pyplot as plt

n = int(input("Enter number of processes : "))

page_sizes=[]

for i in range(n):
    x = int(input(f"Enter page size for P{i+1} : "))
    page_sizes.append(x)

total = int(input("Enter total number of frames : "))
threshold = int(input("Enter minimum number of frames : "))

total_pages = sum(page_sizes)
counts = [threshold]*n
fractions = []
remaining = total - (threshold*n)

for i in range(n):
    prop = (page_sizes[i]*remaining)/total_pages
    counts[i]+= int(prop)
    fractions.append(prop-int(prop))

leftover = total - sum(counts)

for i in sorted(range(n),key = lambda i : fractions[i],reverse=True)[:leftover]:
    counts[i]+=1

i=0

frames = [0]*total

idx = 0

for pid in range(n) :
    for j in range(counts[pid]):
        if idx<total:
            frames[idx]=pid+1
            idx+=1

print("Process\tFrames Allocated")
for i in range(len(counts)):
    print(f"P{i+1}\t{counts[i]}")


plt.figure(figsize=(12,3))

colors = ["red","blue","yellow","green","purple","white"]

for i,f in enumerate(frames):
    
    if f==0:
        text="Free"
    else:
        text= "P" + str(f)
    
    plt.barh(0,1,left=i,color=colors[f-1],edgecolor="black")
    plt.text(i+0.5,0,text,ha="center",va="center")

plt.xlim(0,total)
plt.yticks([])

plt.xlabel("Frames")
plt.title("Proportional Frame Allocation")

plt.show()
