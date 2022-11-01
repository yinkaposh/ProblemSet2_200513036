#!/usr/bin/env python
# coding: utf-8

# Question 1
# 
# What value is displayed when the last expression (a) is evaluated? Explain your answer by indicating what happens in every executed statement.
# 
# 

# In[11]:


a = 0
def b():
    global a
    a = c(a)
def c(a):
    return a + 2


# In[12]:


b()                                #a=2
b()                                #a=4
b()                                #a=6
a


# As"a" has been initialized as 0 ,it is also used in b and c. b() uses c() which add 2 to a's values. This way everytime b is called, c is called and 2 is added to a's value. Since, 'a' is global variable, a's value gets changed globally everytime b is called.

# Question 2
# 
# Function fileLength(), given to you, takes the name of a file as input and returns the length of the file:
# 
#         fileLength('midterm.py') 284 fileLength('idterm.py') Traceback (most recent call last): File "", line 1, in fileLength('idterm.py') File "/Users/me/midterm.py", line 3, in fileLength infile = open(filename) FileNotFoundError: [Errno 2] No such file or directory: 'idterm.py'
# 
# As shown above, if the file cannot be found by the interpreter or if it cannot be read as a text file, an exception will be raised. Modify function fileLength() so that a friendly message is printed instead:

# In[14]:


def file_length(f):                                          #creating function file_length()
    try:                                                    #errors checking while opening the file
        file = open(f, "r")                                     
        contents=file.read()                                               
        print('Given file length is : '+ str(len(contents)))         
        file.close()                                                   
    except:                                                           
        print('File '+f+' not found.')                        #printing message to show file not found


# In[15]:


file_length("PB2.py")


# Question 3
# 
# Write a class named Marsupial that can be used as shown below:
# 
#         m = Marsupial() m.put_in_pouch('doll') m.put_in_pouch('firetruck') m.put_in_pouch('kitten') m.pouch_contents() ['doll', 'firetruck', 'kitten']
# 
# Now write a class named Kangaroo as a subclass of Marsupial that inherits all the attributes of Marsupial and also: a. extends the Marsupial init constructor to take, as input, the coordinates x and y of the Kangaroo object, b. supports method jump that takes number values dx and dy as input and moves the kangaroo by dx units along the x-axis and by dy units along the yaxis, and c. overloads the str operator so it behaves as shown below.
# 
#         k = Kangaroo(0,0) print(k) I am a Kangaroo located at coordinates (0,0) k.put_in_pouch('doll') k.put_in_pouch('firetruck') k.put_in_pouch('kitten') k.pouch_contents() 'doll', 'firetruck', 'kitten' k.jump(1,0) k.jump(1,0) k.jump(1,0) print(k) I am a Kangaroo located at coordinates (3,0)

# In[16]:


class Marsupial(object):                     #class file Marsupial
  
    def __init__(self):                               
        self.mylist = []                     #creating mylist
    def put_in_pouch(self, item):            #creating put_in_pounch() function 
        self.mylist.append(item)
    def pouch_contents(self):                #creating pouch_contents() function
        return self.mylist 


# In[17]:


m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
m.pouch_contents()


# In[18]:


class Kangaroo(Marsupial):                      
    
    def __init__(self,x,y):                                     
        Marsupial.__init__(self)                 #extending init function
        self.x = x                                
        self.y = y
                                  
    def jump(self,dx,dy):                        #creating jump function 
        self.x = self.x + dx
        self.y = self.y + dy
        
    def __str__(self):                           
        return 'I am a Kangaroo located at coordinates ({},{})'.format(self.x,self.y)


# In[19]:


k = Kangaroo(0,0)
print(k)


# In[20]:


k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
k.pouch_contents()


# In[21]:


k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)


# Question 4
# 
# Write function collatz() that takes a positive integer x as input and prints the Collatz sequence starting at x. A Collatz sequence is obtained by repeatedly applying this rule to the previous number x in the sequence: x = { 𝑥/2 𝑖𝑓 𝑥 𝑖𝑠 𝑒𝑣𝑒𝑛 3𝑥 + 1 𝑖𝑓 𝑥 𝑖𝑠 𝑜𝑑𝑑 Your function should stop when the sequence gets to number 1. Your implementation must be recursive, without any loops.
# 
#     collatz(1) 1
# 
#         collatz(10) 10 5 16 8 4 2 1

# In[22]:


def collatz(x):                   #creating collatz function
   
    if x != 1:                   
        if x%2!=0:                #check if x is odd number
            print(int(x))         # print value
            collatz(3*x+1)       
        
        else:
            print(int(x))         
            collatz(x/2)          
  
    else:
        print(int(x));  


# In[23]:


collatz(1)


# In[24]:


collatz(10)


# Question 5
# 
# Write a recursive method binary() that takes a non-negative integer n and prints the binary representation of integer n.
# 
#         binary(0) 0 binary(1) 1 binary(3) 11 binary(9) 1001
# 

# In[26]:


def binary(n):
    
    if n>0:                           #if n is greater than it will calculate binary value
        return (n % 2 + 10*binary(int(n // 2)))
       
    else:
         return 0


# In[27]:


binary(0)


# In[28]:


binary(1)


# In[29]:


binary(3)


# In[30]:


binary(9)


# In[31]:


binary(-1)


# In[32]:


binary(-2)


# Question 6
# 
# Implement a class named HeadingParser that can be used to parse an HTML document, and retrieve and print all the headings in the document. You should implement your class as a subclass of HTMLParser, defined in Standard Library module html.parser. When fed a string containing HTML code, your class should print the headings, one per line and in the order in which they appear in the document. Each heading should be indented as follows: an h1 heading should have indentation 0, and h2 heading should have indentation 1, etc. Test your implementation using w3c.html.
# 
#         infile = open('w3c.html') content = infile.read() infile.close() hp = HeadingParser() hp.feed(content) W3C Mission Principles

# In[33]:


from html.parser import HTMLParser                               
class HeadingParser(HTMLParser):                      
    def __init__(self):                                                 
        HTMLParser.__init__(self)                           
        self.head =0                                                          
        self.intend = ""
    def handle_starttag(self, tag, attrs):              
        if tag[:-1]=='h':
            self.head = 'type'
    def handle_data(self, data):                             
        if self.head=="type":
            print(self.intend+ data)                         
            self.intend+= "    "
            self.head=0 


# infile = open('w3c.html')
# content = infile.read()
# infile.close()
# hp = HeadingParser()
# hp.feed(content)

# infile = open('w3c.html')
# content = infile.read()
# infile.close()
# hp = HeadingParser()
# hp.feed(content)

# Question 7
# 
# Implement recursive function webdir() that takes as input: a URL (as a string) and non-negative integers depth and indent. Your function should visit every web page reachable from the starting URL web page in depth clicks or less, and print each web page's URL. As shown below, indentation, specified by indent, should be used to indicate the depth of a URL.
# 
#     webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html' , 2, 0) http://reed.cs.depaul.edu/lperkovic/csc242/test1.html http://reed.cs.depaul.edu/lperkovic/csc242/test2.html http://reed.cs.depaul.edu/lperkovic/csc242/test4.html http://reed.cs.depaul.edu/lperkovic/csc242/test3.html http://reed.cs.depaul.edu/lperkovic/csc242/test4.html

# In[37]:


from html.parser import HTMLParser    
from urllib.request import urlopen
from urllib.parse import urljoin

class collector(HTMLParser):
    

    def __init__(self, url):
      
        HTMLParser.__init__(self)
        self.url = url
        self.links = []


    def append(self):
        
        return self.links


    def handle_starttag(self, url_tag, attributes):
        for i in attributes:
            mylinks = urljoin(self.url, a[1])
            if mylinks[:4] == 'http': 
                self.url_links.append(mylinks)
                i = 0
def webdir(url, depth, i):
   

    depth = depth - 1    
    print(i*'  ', url)         

    objective = urlopen(url).read().decode()
    collection = urlcollector(url)
    collection.feed(objective)
    urls = collection.append() 
 
    links = urls
    i= i + 4


    for link in links:
        if depth < 0 or i < 0:
            return 1
        else:
            webdir(link, depth, i)


# In[39]:


webdir('http://reed.cs.depaul.edu/lperkovic/test1.html', 2, 0)


# Question 8 Write SQL queries on the below database table that return:
# 
# a) All the temperature data.
# 
# b) All the cities, but without repetition.
# 
# c) All the records for India.
# 
# d) All the Fall records
# 
# e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters.
# 
# f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order.
# 
# g) The total annual rainfall for Cairo.
# 
# h) The total rainfall for each season.

# In[40]:


import sqlite3
con = sqlite3.connect('database_db')
cur = con.cursor()
cur.execute("CREATE TABLE database_d (City text, Country text, Season text, Temperature dec, Rainfall dec)")
cur.execute("INSERT INTO database_d VALUES ('Mumbai', 'India', 'Winter', 24.8, 5.9)")
cur.execute("INSERT INTO database_d VALUES ('Mumbai', 'India', 'Spring', 28.4, 16.2)")
cur.execute("INSERT INTO database_d VALUES ('Mumbai', 'India', 'Summer', 27.9, 1549.4)")
cur.execute("INSERT INTO database_d VALUES ('Mumbai', 'India', 'Fall', 27.6, 346.0)")
cur.execute("INSERT INTO database_d VALUES ('London', 'United Kingdom', 'Winter', 4.2, 207.7)")
cur.execute("INSERT INTO database_d VALUES ('London', 'United Kingdom', 'Spring', 8.3, 169.6)")
cur.execute("INSERT INTO database_d VALUES ('London', 'United Kingdom', 'Summer', 15.7, 157.0)")
cur.execute("INSERT INTO database_d VALUES ('London', 'United Kingdom', 'Fall', 10.4, 218.5)")
cur.execute("INSERT INTO database_d VALUES ('Cairo', 'Egypt', 'Winter', 13.6, 16.5)")
cur.execute("INSERT INTO database_d VALUES ('Cairo', 'Egypt', 'Spring', 20.7, 6.5)")
cur.execute("INSERT INTO database_d VALUES ('Cairo', 'Egypt', 'Summer', 27.7, 0.1)")
cur.execute("INSERT INTO database_d VALUES ('Cairo', 'Egypt', 'Fall', 22.2, 4.5)")
con.commit()
con.close()


# In[41]:


import sqlite3
con = sqlite3.connect('database_db')
cur = con.cursor()
cur.execute('SELECT Temperature FROM database_d ')
for record in cur:
    print(record)
cur.execute('SELECT DISTINCT City FROM database_d ')
for record in cur:
    print(record)
cur.execute('SELECT * FROM database_d  where Season="Fall"')
for record in cur:
    print(record)
cur.execute('SELECT * FROM database_d  where Country="India"')
for record in cur:
    print(record)
cur.execute('SELECT City,Country FROM database_d  where (Season ="Fall") AND (temperature>20) ORDER BY Temperature DESC')
for record in cur:
    print(record)
cur.execute('SELECT City,Country,Season FROM database_d  where (rainfall>200) AND (rainfall<400)')
for record in cur:
    print(record)
cur.execute('SELECT SUM(Rainfall) FROM database_d  where City="Cairo"')
Annual_rainfall=cur.fetchall()
print(Annual_rainfall)
cur.execute('SELECT SUM(Rainfall),Season FROM database_d  GROUP BY Season')
for record in cur:
    print(record)


# Question 9
# 
# Suppose list words is defined as follows:
# 
#         words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# 
# Write list comprehension expressions that use list words and generate the following lists:
# 
# a) ['THE', 'QUICK', 'BROWN', 'FOX', 'JUMPS', 'OVER', 'THE', 'LAZY', 'DOG']
# 
# b) ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# 
# c) [3, 5, 5, 3, 5, 4, 3, 4, 3] (the list of lengths of words in list words).
# 
# d) [['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]
# 
# (the list containing a list for every word of list words, where each list contains the word in uppercase and lowercase and the length of the word.)
# 
# e) ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'] (the list of words in list words containing 4 or more characters.)

# In[42]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
[a.upper() for a in words]


# In[43]:


[a.lower() for a in words]


# In[44]:


[len(a) for a in words]


# In[45]:


[[a.upper(),a.lower(),len(a)] for a in words]


# In[46]:


[a for a in words if len(a) >= 4]


# In[ ]:




