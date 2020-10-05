#This code checks to see if a user input string is a palindrome.


def is_palindrome(word):
    if len(word)> 2:            #checks to see if the string > 2 letters
        for i in range(0, int(len(word)/2)):       #loop from 0 to length/2
            if word[i] != word[len(word)-i-1]:    #compares letters: 1st/last, 2nd/2nd last, etc.
                return False
            else:
                return True

word = input('Enter a value for a:\n')      #requests word from user
tf = is_palindrome(word)

if(tf):
    print("Yes")
else:
    print("No")


