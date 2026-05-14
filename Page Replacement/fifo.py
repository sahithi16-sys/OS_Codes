import matplotlib.pyplot as plt

n = int(input("Enter number of pages in reference string : "))

frame_count = int(input("Enter number of frames : "))

ref_string = list(map(int,input("Enter Reference String: ").split()))

history,frames = [],[]

hits,faults,pointer = 0,0,0

for page in ref_string:
    if page in frames:
        hits+=1
    else:
        faults+=1
        if frame_count > len(frames):
            frames.append(page)
        else:
            frames[pointer]=page
            pointer = (pointer+1)%frame_count

    history.append(frames.copy())

print("Page Hits : ",hits)
print("Page Faults : ",faults)

plt.figure(figsize = (n*0.6 + 3,frame_count+1))

for step in range(len(history)):
    frames = history[step]

    for i in range(frame_count):
        if i<len(frames):
            value = frames[i]
        else:
            value=""
        
        plt.text(step,i,str(value),bbox=dict(facecolor='lightblue',edgecolor='black'))

plt.xticks(range(n),ref_string)
plt.yticks(range(frame_count),[f"P{b}" for b in range(frame_count)])

plt.xlim(-0.5,n+0.5)
plt.ylim(frame_count-0.5,-0.5)

plt.title("FIFO Page Replacement Algorithm")
plt.grid(True)
plt.show()