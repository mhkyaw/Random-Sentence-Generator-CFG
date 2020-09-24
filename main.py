import sys
import argparse
import random
import re

#setting up intial variables
arglist = sys.argv[1:]
list2 = []
condic = {}
treestring = '(ROOT'
mystring = ''



#function setting up the dictionary
def setup():
  for i in list2:
    key = i[1]
    x = i[0]

    #Keys with more than 1 value. Putting different values for the same key in a list fashion
    if i[1] not in condic:
      condic[key] = [i[2]]
    elif i[1] in condic:
      condic[key].append(i[2])
    
    #Adding the value into the list repeatedly the proper number of times according to the weighted value

    for j in range(int(x)-1):        
      condic[key].append(i[2])

  main()


#tree function
def recurtree(x):
  global treestring
  global mystring
  global value
  

  #same function as recur except this one has a different printing and string storing format which creates trees
  for i in x:
    #if terminal not reached, continue
    if i in condic:
      value = random.choice(condic[i])
      treestring = treestring + " (" + str(i)
      recurtree(value.split(' '))
    
    #if terminal reached, then add value to list
    if i not in condic:
      sent = ''.join(i)
      mystring = mystring + " " + sent
      treestring = treestring + " " + str(i)
    
  treestring = treestring + ")"

  
#recursive funciton for creating sentences
def recur(x):
  global mystring
  for i in x:
    #if terminal not reached, continue
    if i in condic:
      value = random.choice(condic[i])
      value = value.split(' ')
      recur(value)

    #if terminal reached, then add value to list
    if i not in condic:
      sent = ''.join(i)
      mystring = mystring + " " + sent


#function producing random sentences using the dictionary from the setup
def main():
  global mystring
  global treestring
  #initializing the random sentence generator starting with the roots
  initial = condic["ROOT"]

  value = random.choice(initial)

  #Leading to recursives to create a sentence or a tree depending on command line argument
  if arglist[0] != "-t": 
    value = value.split(' ')
    recur(value)
    print(mystring)
    print(' ')
    mystring = ''
  elif arglist[0] == "-t":
    recurtree(value)
    print(treestring)
    print('')
    treestring = '(ROOT'


if arglist[0] != "-t":
  f = open(str(arglist[0]), 'r')
  a = f.readlines()

  for i in range(len(a)):
    #combine the line into a list, where a tab is the determiner
    list1 = re.split('\t',a[i])
    
    #deletes the /n character or white space at the end of the line
    list1 = [s.rstrip() for s in list1]       
    #differentiate between comments, empty lines, and actual grammar rules
    firstelement = list1[0]
    
    #ignore comments
    if "#" in firstelement:
      pass

    #ignore empty lines
    elif firstelement != '':
      #add a counter to split the weight and the non terminal into two different elements in the list
      counter = 0 
      
      for i in firstelement:
        if i == " ":
          list1.insert(0,firstelement[:counter])
          list1.insert(1,firstelement[counter+1:])
          firstelement[counter:]
        else:
          counter += 1
      del list1[2]
      
      list2.append(list1)
    
  
  setup()


#Number of sentences to be generated
if arglist[1].isdigit():
  #one sentence is already generated no matter what so the required extra iterations will be one less than the total
  for i in range(int(arglist[1])-1):
    main()


elif arglist[2].isdigit() and arglist[0] == "-t":
  f = open(str(arglist[1]), 'r')
  a = f.readlines()

  for i in range(len(a)):
    #combine the line into a list, where a tab is the determiner
    list1 = re.split('\t',a[i])
    
    #deletes the /n character or white space at the end of the line
    list1 = [s.rstrip() for s in list1]       
    #differentiate between comments, empty lines, and actual grammar rules
    firstelement = list1[0]
    
    #ignore comments
    if "#" in firstelement:
      pass

    #ignore empty lines
    elif firstelement != '':
      #add a counter to split the weight and the non terminal into two different elements in the list
      counter = 0 
      
      for i in firstelement:
        if i == " ":
          list1.insert(0,firstelement[:counter])
          list1.insert(1,firstelement[counter+1:])
          firstelement[counter:]
        else:
          counter += 1
      del list1[2]
      
      list2.append(list1)
    
  #one sentence is already generated no matter what so the required extra iterations will be one less than the total
  setup()
  
  for i in range(int(arglist[2])-1):
    main()

    
  
  
  
  
