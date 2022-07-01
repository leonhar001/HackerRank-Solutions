import re #regular expression

string = input()
string = sorted(string, reverse=True)
string = ''.join(map(str,string))

hasNumbers = bool(re.search('\d',string)) #check numbers existence
hasLetters = bool(re.search('[a-zA-Z]',string)) #check letters existence

lettersSplitNumbers = re.split('(\d+)', string) #split numbers and letters

letters = []
if(hasLetters):
    letters = sorted(lettersSplitNumbers[0]) #sort all types of letters
    letters = sorted(letters, key =lambda x:x.isupper())  # sort uppercase letters
    
numbers = []
if(hasNumbers):
    numbers = list(map(int, lettersSplitNumbers[1])) #convert numbers strings to int
    numbers = sorted(numbers)
    numbers = sorted(numbers, key=lambda x:x%2==0) #sort even/odd digits 

print(''.join(map(str,letters))+''.join(map(str,numbers)))
