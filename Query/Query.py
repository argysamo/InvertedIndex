#!/usr/bin/python

import os,sys
'''This creates the new inv ind. only words inside'''

def Parser(FileName):
    try:
        with open(FileName,"r") as f:
            g = open("index.txt","w")
            for line in f:
                line = line.split("\t")
                g.write(line[0])
                g.write("\n")
    
            g.close() 
    except:
        print "Oops there is a problem....."
        exit()

'''This opens the new file(only words) and finds the word from the query'''


def FindLine(word):
    with open("index.txt","r") as f:
        x = list(f)
        count = 0
        for line in x:
            count +=1
            line = line.strip()
            if line == word:
                return count
                break
'''This opens the original inv index and finds the docId's'''

def FindDocs(line):
#memory efficient way to open a file
    with open("inv.txt","r") as g:
#list all elements --> easy parsing
        x = list(g)
#return the exact element we want        
        return x[int(line)-1]

'''This is for the AND between docs'''
        
def And(List1,List2):
#Inverse sort to use .pop()
    List1 = sorted(List1, reverse = True)
    List2 = sorted(List2, reverse = True)
    answer = []
    while List1 !=[] and List2 != []:
        x = List1.pop()
        y = List2.pop()
        if x == y:
            answer.append(x)
        else:
            if x<y :
                List2.append(y)
            else:
                List1.append(x)       
    return answer
    
'''This is for the OR between docs''' 

   
def Or(List1,List2):
    answer = []
    if len(List1) > len(List2):
        for i in List1:
            answer.append(i)
        for j in List2:
            if j not in answer:
                answer.append(j)
                
    else:
        for i in List2:
            answer.append(i)
        for j in List1:
            if j not in answer:
                answer.append(j)  
    return answer
'''This returns the exact DocId and not a number'''

def WhichDoc(Dictionary,List):
    answer = []
    for i in List:
        for Key,Value in Dictionary.items():
            if int(i) == int(Value):
                answer.append(Key)
                
    return answer   


def main():
    Dictionary = {}
    Dictionary["pg4300.txt"] = '1'
    Dictionary["pg5000.txt"] = '2'
    Dictionary["pg20417.txt"] = '3'
    List = []
    Relation = []
    Words = []
    #open the file and make the new one
    try:
        print "Give me the full name of your inverted index"
        FileName = raw_input (">")
        Parser(FileName)
    except:
        print " Give me the correct name and/or the full path of file"
        exit()
    # take as input how many words is the query
    try:
        print "Please give how many words is your query"
        x = int(raw_input(">"))
        
    except:
        print "Give me a number please....."
        exit()
    #Make an iteration from 0 to WordInput-1    
    for i in range(0,x):
            print "Give me the word number:%d" %(i+1)
            word = raw_input(">")
    # Check but not input Word is "1"
            if i != x-1: 
                print "Now give me the relation between %s and the next word(and/or)" %word
                relation = raw_input(">")
                if relation!="and" and relation!="or":
                    print "Wrong input. Give only and/or .... Next time"
                    exit()
                Relation.append(relation)
            Words.append(word)
    for i in Words:
        WordDocs =[]
        word,value = FindDocs(FindLine(i)).split("\t")
        value = value.split("|")
        value.remove("")
        for docs in value:            
            docs = docs.split(":")
            WordDocs.append(Dictionary[docs[0]])            
        List.append(WordDocs)
    if x == 1:
        print List[0]
    elif x == 2:    
        if Relation[0] == "and":
            print WhichDoc(Dictionary,And(List[0],List[1]))
        elif Relation[0] == "or" :
            print WhichDoc(Dictionary,Or(List[0],List[1]))
        else:
            exit()
                        
            
if __name__ == "__main__":
    main()
