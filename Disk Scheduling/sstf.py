import matplotlib.pyplot as plt

DISK_MIN = int(input("Enter minimum disk range: "))
DISK_MAX = int(input("Enter maximum disk range: "))

n = int(input("Enter number of requests: "))

requests = list(map(int,input("Enter disk requests: ").split()))
head = int(input("Enter initial head position: "))

req = requests.copy()
movements = 0
sequence = [head]
current = head

while req:
    closest = min(req,key = lambda x: abs(x-current))
    movements =movements +  abs(current-closest)
    req.remove(closest)
    sequence.append(closest)
    current = closest

print("Sequence : ", sequence)
print("Total Head Movements: ",movements)

order = list(range(len(sequence)))
plt.figure()
plt.plot(sequence,order,marker='o')

plt.xlabel("Requests")
plt.ylabel("Order")
plt.title("SSTF Disk Scheduling Algorithm")

for i in range(len(sequence)):
    plt.text(sequence[i],order[i],str(sequence[i]))

plt.xlim(DISK_MIN - 0.5,DISK_MAX + 0.5)
plt.ylim(-0.5,len(order)+0.5)

plt.grid(True)
plt.show()
