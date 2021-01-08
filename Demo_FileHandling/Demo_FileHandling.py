# Copy of data from 1 file to another file

fw = open("Demo_FileHandling/FH_copy.txt", 'w')
with open("Demo_FileHandling/FH.txt", 'r') as fr:
    for data in fr:
        fw.write(data)

fw.close()