# -*- coding: utf-8 -*-
"""

Please note the following:
    1. I have organized this Python session as a motivation for my young brothers and sisters. 
    2. IF YOU CAN DREAM IT, YOU CAN DO IT!!!!
    3. May be you have slow progress, BUT quitting won't speed it up!! 
                              Do more and make your dreams come TRUE
                              
   These few code lines taken on Wed. 7/11/2018 at 6.00:9.00 pm.
   
   © Ali Mohamed AbdelAziz
     FaceBook: Ali Mohamed AbdelAziz
     Insta: The.Egyptian.Traveler

"""
# Output commands!
# This line to print a string, note that the string enclsoed by ""
print("You Are Stronger Than You Think!!")
print('*'*50,"\nYou Are limitless\n Just belive in your self!!\n",'*'*50)



# input commands
# The following line read an input then convert it to integer. The input is 
#stored at variable named "My_input" Note that you can 
#convert the input to float or leave it as string
My_input=int(input("Please enter an integer number= "))
print("The number you have just entered is= ",My_input)
####### Looping and lists
################################################### for loop
for counter in (10,50):
    print ("Print just two numbers",counter)
    
    ## Normal for syntax with step=1 (increment it will print ranges 10:50)
for counter in range (10,50):
    print ("Normal for syntax",counter)  
    
        ## Normal for syntax with step=2 (it will print ranges 10:50:2)
for counter in range (10,50,2):
    print ("Use of steps",counter)  
    
     ## Normal for syntax with step=-2 (it will print ranges 50:10:-2)
for counter in range (50,10,-2):
    print ("Use of steps",counter) 
 
    ##### While loop
    x=1
    while x<10:
        print(x)
        x=x+1
        
      ##### infinte  loop
      # Note: to break infinte loop please press CTRL + C
    x=1
    while x<10:
        print(x)
      #  x=x+1      
    
########
print(" len() is a function to retrive length of string")
My_String="Hello_Ali_is_here!!"
print("The length of the string is ",len(My_String))
print(My_String[0])
print(My_String[1])
print(My_String[2])
print(My_String[3])
print(My_String[4])

######################

print(My_String[3:6] ," ----> evaluates to 'lo_', same as My_String[3:6:1]\n")
print(My_String[3:6:2], "----> evaluates to 'l_' \n")
print(My_String[::], "----> evaluates to 'Hello_Ali_is_here'  same as My_String[0:len(My_String):1]\n")
print(My_String[::-1], "----> evaluates to '!!ereh_si_ilA_olleH' , same as My_String[-1:-(len(My_String)+1):-1]\n")
print(My_String[4:1:-2] ,"----> evaluates to 'ol' \n")
#################### String Concatenation

print('y'+ My_String[1:len(My_String)] )

####### Loops
for index in range(len(My_String)):
 if My_String[index] == 'H' or My_String[index] == 'o':
  print("There is an H or o")


for char in My_String:
 if char == 'H' or char == 'o':
  print("There is an H or o")
  

     

################################################### for loop in lists 
   
MyList=[10,20,30,40,50]    
for counter in MyList:
    print ("It will print all VALUES in the list",counter)
    
   
MyList=[10,20,30,40,50]    
for counter in range (len(MyList)):
    print ("It will print just INDICES",counter)    
################################################### lISTS
MyList=[10,20,30,40,50]    
print("Just print the list",MyList)
# add number to the list using append
MyList.append(60)
print("Just print the list after appending new number",MyList)
# add number to the list using concatenatation
MyList=MyList+[70]
print("Just print the list after concatenating  new number",MyList)
# Remove a number from the list using remove(value)
MyList.remove(70)
print("Just print the list after removing one number using remove",MyList)
# delete a number from the list using del(index)
del MyList[4]
print("Just print the list after removing one number using del",MyList)

  #################### Function
#Keyword followed by function name(parameters or arguments)  
def is_even_with_return( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

is_even_with_return(3) 
print(is_even_with_return(3) )

######## Scope examples
#Function scopes and global variable TRICKS!!!
def Scope_Fun(x):
     x+=1
     print("x inside function",x)
     print("Y is a global variable and declared before function call!!",y)
    # print("z is a global variable BUT declared AFTER function call!!"+
     #      "so you cant print it and you will recieve ERROR",z)

     return x
 
    
x=5 
y=10  
Scope_Fun(x)
print("x outside function",x)
## Please uncomment Z after you understand the code!!
#z=15
  
# Void Functions Example 
#Void function is a function that return  nothing e.g. printing comands

def Print_Name_Card():
    print('='*50,"\n\n\t© Ali Mohamed AbdelAziz\n\t FaceBook: Ali Mohamed AbdelAziz\n\t",
          "Insta: The.Egyptian.Traveler\n\n\t\t GOOD LUCK\n\n",'='*50)
    
    
Print_Name_Card()  
