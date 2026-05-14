import matplotlib.pyplot as plt

n = int(input("Enter number of pages in reference string:"))
frame_count = int(input("Enter number of frames : "))
ref_string = list(map(int,input("Enter reference string : ").split()))

history,frames=[],[]

hits,faults=0,0

for i,page in enumerate(ref_string):
    if page in frames:
        hits+=1
    else:
        faults+=1
        if len(frames)<frame_count:
            frames.append(page)
        else:
            future = ref_string[i+1:]
            indices = []
            for f in frames:
                if f in future:
                    indices.append(future.index(f))
                else:
                    indices.append(float('inf'))
            
            victim = indices.index(max(indices))
            frames[victim]=page
    history.append(frames.copy())

print("Page Hits : ",hits)
print("Page Faults : ",faults)

plt.figure(figsize = (n*0.6+3,frame_count+1))

for step in range(n):
    frames = history[step]
    for i in range(frame_count):
        if i<len(frames):
            value = frames[i]
        else:
            value = ""
    
        plt.text(step,i,str(value),bbox=dict(facecolor='lightblue',edgecolor='black'))

plt.xticks(range(n),ref_string)
plt.yticks(range(frame_count),[f"F{b+1}" for b in range(frame_count)])

plt.xlim(-0.5,n+0.5)
plt.ylim(frame_count-0.5,-0.5)


plt.title("LRU Page Replacement Algorithm")

plt.grid(True)
plt.show()