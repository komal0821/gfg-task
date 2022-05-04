# Python3 program to print 
#  even length words in a string

def printwords(s):
    s = s.split(' ')

    # iterate in words of string 
    for word in s:
     # if length is even
      if len(word)%2==0:
        print(word)

#Driver code
s= "I am Komal"
printwords(s)
