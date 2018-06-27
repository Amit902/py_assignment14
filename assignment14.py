#Q1- Write a Python program to read last n lines of a file.
#first method

#first method
f=open("test.txt","r")
content=f.readlines()
n=int(input("enter the number of lines from last you want to print :"))
for x in range(len(content)-n,len(content)):
    print(content[x])
f.close()

#second method
f=open("test.txt","r")
count=0
a=0
for line in f:
    count+=1

f.seek(0)
for line in f:
    a+=1
    if a>=count-5:
        print(line)
f.close()

# #Q2- Write a Python program to count the frequency of words in a file.

f=open('test.txt','r')
d={}
for word in f.read().split():
    if word not in d:
        d[word]=1
    else:
        d[word]+=1
for i,j in d.items():
    print(i,j)

f.close()


#Q3- Write a Python program to copy the contents of a file to another file.

with open('test.txt','r') as f1:
    with open("test4.txt","w") as f2:
        for lines in f1:
            f2.write(lines)

#Q.4- Write a Python program to combine each line from

first file with the corresponding line in second file.

with open('test2.txt') as f1, open('test4.txt') as f2:
    for line1, line2 in zip(f1, f2):
        print(line1 + line2)



#Q.5- Write a Python program to write 10 random numbers into a file.
# Read the file and then sort the numbers and then store it to another file.

import os
import random
randomlist=[]
for x in range(100):
    randomlist.append(x)
random.shuffle(randomlist)

with open("test6.txt","w") as f:
    for x in range(10):
        f.write(str(randomlist[x])+"\n")

os.remove("test8.txt")
with open("test6.txt","r+") as f:
    with open("test8.txt","w") as f1:
        randomlist1=f.readlines()
        for x in range(len(randomlist1)):
            randomlist1[x]=int(randomlist1[x])
        randomlist1.sort()

        for x in randomlist1:
            f1.write(str(x)+"\n")