# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        line = line.strip()
        colon_pos = line.find(':')
        value = line[colon_pos+1:].strip()
        total += float(value)
       
average = total/count
print("Average spam confidence:", average)