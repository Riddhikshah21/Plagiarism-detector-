import os
import string
import re
import sys
from collections import Counter
from functools import reduce


plag_threshold = 50

        
fileNames = sys.argv
file1= fileNames[1]
file2 = fileNames[2]


with open(file1,"r") as file:
    data1=file.read().split()
    

with open(file2,"r") as file:
    data2=file.read().split()
    


l1 = []
for i in data1:
    l1.append(i.lower())


s1 = []
for i in l1:
    s1.append(''.join(c for c in i if c not in string.punctuation))    


p1 = []
for i in s1:
    p1.append(i.split(' '))
list1 = reduce(lambda x,y: x+y, p1)




l2 = []
for i in data2:
    l2.append(i.lower())

s2 = []


for i in l2:
    s2.append(''.join(c for c in i if c not in string.punctuation))    



p2 = []
for i in s2:
    p2.append(i.split(' '))
list2 = reduce(lambda x,y: x+y, p2)


frequency_list1 = {}
frequency_list2 = {}


for i in list1:
    if i not in frequency_list1:
        frequency_list1[i] = 0
    frequency_list1[i]=frequency_list1[i]+1

for i in list2:
    if i not in frequency_list2:
        frequency_list2[i] = 0
    frequency_list2[i]=frequency_list2[i]+1





def LCS_algorithm(data1, data2):
    # a and b are length of two files that we are passing to the algorithm. 
    a = len(data1)
    b = len(data2)

    # creating a DP array(LCS) for storing the dp values for our algorithm. 
    # LCS array is of size (a x b) (a rows and b columns)
    LCS = [[None]*(b + 1) for i in range(a + 1)]

    for i in range(a + 1):
        for j in range(b + 1):
            # setting value to 0 for both 1st row and 1st column of the dp table.
            if i == 0 or j == 0 :
                LCS[i][j] = 0
            
            elif data1[i-1] == data2[j-1]:
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

    # LCS[a][b] contains the length of data1[0..n-1] & data2[0..m-1]
    return LCS[a][b]

#declaring stopwords
stopwords=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
newlist1=set(list1)
#removing stopwords from the arraylist. 
newlist1.difference_update(stopwords)
newlist1=list(newlist1)

newlist2=set(list2)
newlist2.difference_update(stopwords)
newlist2=list(newlist2)


LCS_obj=LCS_algorithm(newlist1, newlist2)
#calculating the LCS value to check plagiarism 
result =round((LCS_obj/len(newlist2))*100, 2)


#threshold is set to 50 
if result > plag_threshold:
    print(1) # plagiarism detected 
else:
    print(0) # no plagiarism detected 
