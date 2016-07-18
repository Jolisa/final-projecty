from PyDictionary import PyDictionary
dictionary= PyDictionary()
#BeautifulSoup(html, "html.parser")




print (dictionary.meaning("indentation"))
french= input("Put in a french word for an english cognate:  ")

#def cognate():
#break individual letters of input word
firstletter= french[0]
print (firstletter)

#if key in dic.keys[0]==frenchletter:
    #print (key) 
liresults=[]
with open('wordsEng.txt', 'r')as inputfile:
    for line in inputfile:
        liresults.append(line.strip().split(','))
        #print (liresults)

a_words = []
for result in liresults:
    
    if (result[0][0] is 'a'):
        a_words.append(result[0])
print (a_words)

#as inputfile
#compare=open(filename,'r')




    #fp.seek (key[0]==individualletters:
        #write key 



    #get key in dictionary with 
    #searchphrase=



    #searchfile= open(dictionary)
    #for line in searchfile:
        #line= line.write
    
    
    
    
