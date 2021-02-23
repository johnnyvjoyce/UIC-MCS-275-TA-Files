# Credit: Prof David Dumas, MCS 275 Spring 2021

outfile = open("mcs275ws7prob3data.txt","w") # delete if it exists!
outfile.write("{} {}\n".format("i","i**2"))
for i in range(32):
    outfile.write("{} {}\n".format(i,i**2))
outfile.close()

infile = open("mcs275ws7prob3data.txt","r")
max_seen = -1
for line in infile:
    fields = line.strip().split(" ")
    if len(fields) != 2:
        continue
    try:
        x = int(fields[1])
    except ValueError:
        # first line doesn't contain an integer
        # just skip it
        continue
    if x > max_seen:
        max_seen = x
infile.close()
print("The largest square appearing in the file is:",max_seen)