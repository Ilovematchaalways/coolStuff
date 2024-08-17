#also I run all this on visual studio code - as my IDE and i run them from run python run in the terminal
#just taking a varibale and giving it a value . going to do a hat and give it a value or name or number.
#alexis 
# just going to put my name in the hat 

#yellow_hat = "alexis "
#now I want yellow hat to take in input, so use input function and ask a question
#yellow_hat=input("What are you thinking about?")
#when i print this is will just ask that question 
#my answer was ice cream , so after i answered i pressed enter , ICe cream was typed out because that was in input answer i did 
#meaning my answer ice cream was now the vaule of the variable yellow_hat by way of puting that answer in 

#yellow_hat = 5  
 #if i do this second line , it will first assign value of alexis, but go to the second line and override it and then print out 5 for the value assigned to yellow_hat 

#doing to delete yellow_hat 
#del yellow_hat
#when i run it shows nameError : name 'yellow_hat is not defined, because i just deleted it , becuase when i tried to print it , it was already deleted with del function


#now im going to have it print out the value that is assignmented to the yellow hat. 
#print(yellow_hat)
#print(type(yellow_hat))
#will be = <class 'int'> because of 5 , or will be = <class 'string'> because of alexis 




#print(yellow_hat)

#now doing condtional logic, anything i enter will either be true or false
#print(6==4)
#the == double = is running a test of equallity are they = equal lol
#is 6 = to 4 = no false  and when i ran it did print out FALSE 
#print(5!=4)
#just asking  with != not equals  so that 5 is not = to 4 whichis true 


#differnt thing lol 





#now im going to combind variable and oprts 

#I've never been married but pretending like I have set vaule to 4 differnt husbands
#Alexis_Husbands = 8
#just putting how many husbands should be acceptiable lol in a lifetime 10 
#hey if it doesn't work try try again lol 
#Respectable_amount = 10
#check it 
#print(Alexis_Husbands == Respectable_amount)
#will come back as false , so yasss cheers to more husbands 
#this is just checking if i am in the RESPECTed amount of divorces ;) 6 more to go lolllll

#now going to use if statement to check different criteria 
#checking if my amount of current husbands is in the amount of Respectable ;) 
#if Alexis_Husbands < Respectable_amount:
    #if the amount of current husbands is acceptable it will print out yasss girl lets go meet more men 
 #   print("yes girl divorce your husband and lets go meet more MEN")
#it was accept lol and it printed out ^^ the above thing 
##now i want some fall back 
#elif Alexis_Husbands == Respectable_amount:
  #  print("sis what are you doing :/ ")

#if i got two many husbands 
#else:
 #   print("sis you need to go take care of your man , go cook some food ")

#now MORE COMPLEX FUNCTIONS YAAAAAAAYYY = what is a function sis =a block of code you can package together with a name and it does something ;) 
    
#print("Alexis you are the Test ")
#print("Alexis you are the Test ")
#print("Alexis you are the Test ")
#^^those are just examples I put test instead of best on purpose 
#wow i didn't spell best correctly, but i don't want to go to every line to fix it , need function
#defined a function, but i haven't called it yet , this is just what will happen when i call it.

#def print_please():
    #just entering text within function
   # text = "Alexis is the best"
   # print(text)
   # print(text)
    #print(text)

# Now this is calling print_please
#print_please() # print 3 timed
#print_please() #prints 3 more times
#print_please() #prints 3 more times 
# so output shuld be printed 9 times alexis is the best 


#now the function wants me to pass some value or text
#this is just to showcase passing vaules into function 
#def print_please(text):

   # print(text)
   

# Now this is calling function, now passing in a value or parameter 
#print_please("Alexis is so smart") # print 3 timed

# so output shuld be printed 9 times alexis is so smart 



#now putting if statement within a function - 
#based on trees around me, I want to know type , and color of leafs
#def trees_around_me (trees,howmany):
    #if howmany < 10:
      #  print("I need to plant more" ,trees,"in a hurry" , howmany)
   # elif howmany == 10:
       # print("WE have enough trees",trees,)
    #else:
       # print("Trees are so beautiful")

#calling function, pass two functions 
#trees_around_me("willows",7)
#okay i tested it works, now testing with other trees 
#trees_around_me("oak",11)
#trees_around_me("walnut",15) 
#trees_around_me("ginkgo",10)
#trees_around_me("baobob ",9)
#trees_around_me("cedar",4)
#trees_around_me("linden",35)
#trees_around_me("elm",4000)
#trees_around_me("birch",10000000)
#it workssss yassssssssssss 


#now how to get a value back from function
#how many cups of matcha i will drink in just randomly doing 10 
#def drink_matcha_tenyears(amount):
    #new_matcha =amount + 10
    #finding out new amount 
    #the function will take amount of matcha I drink and add 10 to it 
    #return new_matcha

#now calling function , and return that new value as variable
#assigning the output to how much match ill drink
#Wow_thats_alotofmatcha = drink_matcha_tenyears(2) 
#testing 
#Wow_thats_alotofmatcha = drink_matcha_tenyears(45) #came back as 55 it works 
#now will print it out 
#print(Wow_thats_alotofmatcha)
#it should be 12, because 2 cups now, in future i will drink 12 




#now loops while and for loops

#while
#this will go all the was up to 9
#x=0
#so if x is less than 10 
#while(x<10):
 #print it out 
 #print(x)
 #this is incrementing x so it doesn't run on it will stop at 9 because of the +1 x =1 and will stop at 9 
# x=x+1


#for loop 
#for x in range(5,100):
   #the loop will grow through thisrange 
   #print(x)
#print it outtttttttt :) will start at 5, and end at 99


#now four loop for my favorite drinks 
#drinks=["matcha", "coffee","tea","mocktail", "wine","water" ]

#creating variable  T for type
#for T in drinks:
#what if I want to know all drinks  I like beofre wine, use a if statement and use break to stop it 
   # if(T=="wine"):break # output should be matcha coffee tea mocktail 
    #it works yes ! 
    #now what if i want the list but want to skip wine being on the list use continue 
    #if(T =="wine"):continue # output should be matcha, coffee, tea, mocktail , water , 
    #yes it worksssssssss
    #print(T)









