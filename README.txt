Student ID : 40197190
Name: Riddhi Shah
Course: COMP 6651 

Project: Plagiarism detector

My project is implemented using Python as a programming language. I have used some in built libraries such as os, string, re, sys, collections, Counter,functools and reduce.
The project is plagiarism detector which helps to determine if contents of two files are matching or not. 
We have many algorithms that can be used to implement this project, such as Longest common subsequence(LCS), Edit distance, KMP, etc. I have implemented using LCS algorithm. 
I have also implemented a method for Bag of words where I have store frequency of words in both the files and try to match their frequencies and determining similar words that are used in both the files but it was not giving out better results for the algorith. 

Steps:
1. Pre processing of data:
- creating array of list of strings. 
- converting the characters to lowercase in order to save some time later while processing data for comparison. 
- removing punctuation as it is really helpful when you want to match strings and check for their similarity 
- discarding whitespaces. 
- excluding stop words that is most commonly used words in English language and tried to decrease the runtime by comparing only the necessary contents of files. 
In our list we only have distinct elements for our algorithm. 

2. LCS algorithm:
-   for i in range(a + 1):
        for j in range(b + 1):            
            if i == 0 or j == 0 :
                LCS[i][j] = 0
            elif X[i-1] == Y[j-1]:
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    return LCS[a][b]
- creates a DP array of size a rows and b columns thats stores DP value for our algorithm
- threshold value for checking plagiarism is set to 45
- if plagiarism is detected it will print 1 else 0.

3. Explanation:
- The algorithm finds LCS between characters of two files after applying pre processing on files. 
- It detects the common subsequence to determine if the contents of two files are matching. For calculating the result percentage we have used the length of LCS.
- The percentage of result is calulated using (length of LCS/length of second file)*100. 
- Based on the result we determine if that value is greater than or less than the threshold value for Plagiarism.

4. Running time of algorithm:
- Time complexity of the algorithm is O(a*b) 
- a is the size of file 1 and b is the size of file 2. 

References
https://www.youtube.com/watch?v=sSno9rV8Rhg
https://stackoverflow.com/questions/8257655/lcs-algorithm-example
https://stackoverflow.com/questions/13465351/removing-punctuation-python