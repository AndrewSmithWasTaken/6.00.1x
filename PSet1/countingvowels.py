#COUNTING VOWELS  (10 points possible)
#Assume s is a string of lower case xacters.
#
#Write a program that counts up the number of vowels contained 
#in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#For example, if s = 'azcbobobegghakl', your program should print:
#
#Number of vowels: 5
#For problems such as these, do not include raw_input statements 
#or define the variable s in any way. Our automated testing will 
#provide a value of s for you - so the code you submit in the 
#following box should assume s is already defined. 

s = "adefth"
vowelNum = 0

for i in s:
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
        vowelNum = vowelNum + 1
    
print("Number of vowels: " + str(vowelNum))
        


    

        