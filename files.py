tempfile = open('Leons_Diary.txt')

listofFile = tempfile.readlines()

tempfile.close()


listofFile.append('20th Oct')

#change s to $
for i in range(len(listofFile)):
    tempVar1 = listofFile.pop(i)
    tempVar2 = tempVar1.replace('s', '$')
    listofFile.insert(i, tempVar2)

tempfile = open('Leons_Diary.txt','w')
#convert list to string
writeout = ''
for i in listofFile:
    writeout = writeout + i

#write file

tempfile.write(writeout)
tempfile.close()
#type(tempfile)
#help(tempfile)
