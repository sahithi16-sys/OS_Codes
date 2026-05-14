import matplotlib.pyplot as plt

DISK_MIN = int(input("Enter minimum disk range: "))
DISK_MAX = int(input("Enter maximum disk range: "))

n = int(input("Enter number of disk requests: "))
requests = list(map(int,input("Enter requests: ").split()))
head = int(input("Enter initial head position: "))

direction = input("Enter direction (left/right) : ")

left = sorted([r for r in requests if r<head])
right = sorted([r for r in requests if r>=head])

sequence=[]

if direction != "left" and direction !="right":
    exit()
elif direction =="right":
    sequence=[head] + right + [DISK_MAX] + left[::-1]
else:
    sequence = [head] + left[::-1] + [DISK_MIN] + right

movements = sum(abs(sequence[i+1]-sequence[i]) for i in range(len(sequence)-1))

print("Sequence: ",sequence)
print("Total Movements: ",movements)

order = list(range(len(sequence)))
plt.figure()

plt.plot(sequence,order,marker='o')

for i in range(len(sequence)):
    plt.text(sequence[i],order[i],str(sequence[i]))

plt.xlabel("Requests")
plt.ylabel("Order")
plt.title("SCAN Disk Scheduling")

plt.xlim(DISK_MIN-0.5,DISK_MAX+0.5)
plt.ylim(-0.5,len(order)+0.5)

plt.grid(True)
plt.show()