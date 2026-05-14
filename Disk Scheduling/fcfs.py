import matplotlib.pyplot as plt

DISK_MIN = int(input("Enter minimum disk range: "))
DISK_MAX = int(input("Enter maximum disk range: "))

n = int(input("Enter number of requests: "))
requests = list(map(int,input("Enter disk requests: ").split()))

head = int(input("Enter head position: "))

sequence = [head] + requests

movements = sum(abs(sequence[i+1]-sequence[i]) for i in range(len(sequence)-1))

print("Sequence : ", sequence)
print("Total Head Movements: ",movements)

order = list(range(len(sequence)))

plt.figure()
plt.plot(sequence,order,marker='o')

for i in range(len(sequence)):
    plt.text(sequence[i],i,str(sequence[i]))

plt.xlabel("Requests")
plt.ylabel("Order")
plt.title("FCFS Disk Scheduling Algorithm")

plt.xlim(DISK_MIN-0.5, DISK_MAX+0.5)
plt.ylim(-0.5,len(sequence))

plt.grid(True)
plt.show()
