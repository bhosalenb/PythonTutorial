# copy of data from 1 file to another file

fw = open("Demo_FileHandling/FH1_copy.jpeg", 'wb')

with open("Demo_FileHandling/FH1.jpeg", 'rb') as fr:
    for data in fr:
        fw.write(data)

fw.close()