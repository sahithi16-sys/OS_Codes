import math

page_size = int(input("Enter Page Size : "))
process_size = int(input("Enter Process Size : "))
memory_size = int(input("Enter Memory Size : "))

if page_size<=0 or process_size<=0 or memory_size<=0:
    print("ERROR! Sizes cannot be negative")
    exit()
elif page_size & (page_size-1):
    print("ERROR! Page size must be in powers of 2")
    exit()
elif memory_size<process_size:
    print("ERROR! Process Size cannot be greater than Memory Size")
    exit()
elif memory_size%page_size!=0:
    print("ERROR! Memory size must be divisible by Process Size")
    exit()

num_pages = math.ceil(process_size/page_size)
num_frames = memory_size//page_size

if num_frames < num_pages:
    print("ERROR! Unable to allocate pages to frames")
    exit()

offset_bits = int(math.log2(page_size))
page_bits = math.ceil(math.log2(num_pages))
frame_bits = math.ceil(math.log2(num_frames))
physical_bits = frame_bits + offset_bits

print("Number of Pages : ",num_pages)
print("Number of Frames : ",num_frames)

page_table=[-1]*num_pages

for p in range(num_pages):
    while True:
        frame = int(input(f"Enter frame number to allocate for Page{p} : "))
        if 0<=frame<num_frames and frame not in page_table:
            page_table[p]=frame
            break
        print("Invalid or unavailable Frame Number. Try again!")

print("Page Allocation")
for p in range(num_pages):
    print(f"Page Number {p} -> Frame Number {page_table[p]}")

print("Byte -> (Page,Offset) -> Frame -> Physical Address")

for byte in range(process_size):
    page_no = byte//page_size
    offset = byte%page_size
    frame_no = page_table[page_no]

    physical_address = frame_no*page_size + offset

    byte_bin = format(byte,f'0{page_bits + offset_bits}b')
    page_bin = format(page_no,f'0{page_bits}b')
    offset_bin = format(offset,f'0{offset_bits}b')
    frame_bin = format(frame_no,f'0{frame_no}b')
    physical_bin = format(physical_address,f'{physical_bits}b')

    print(f"Byte {byte} ({byte_bin}) -> (Page {page_no} ({page_bin}) , Offset {offset} ({offset_bits})) -> Frame {frame_no} ({frame_bin}) -> Physical Address {physical_address} ({physical_bin})")
