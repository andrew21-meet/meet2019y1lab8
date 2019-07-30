import turtle

word_letters = [ ]
letters = [ ] 
word = input("what is your SECRET word? ")


for space in range(1, 100):
    print (".")

for i in range (20):
    char = word[i]
    word_letters.append(char)
    word_length=  len(word_letters)

letter = input("input a letter ")
letters.append(letter)

for correct in range (word_length):
    if word[correct] == letter:
        print ("Success!")
        break
    else:
        print ("Wrong!  you have 5 tries left")
        break

letter = input("input another letter ")

for correct in range (100):
    if word[correct] == letter:
        print ("Success!")
        letters.append(letter)
        break
    else:
        print ("Wrong!  you have 4 tries left")
        break

letter = input("input another letter ")


for correct in range (100):
    if word[correct] == letter:
        print ("Success!")
        break
        letters.append(letter)
    else:
        print ("Wrong!  you have 3 tries left")
        break

letter = input("input another letter ") 

for correct in range (100):
    if word[correct] == letter:
        print ("Success!")
        letters.append(letter)
        break
    else:
        print ("Wrong!  you have 2 tries left")
        break

letter = input("input another letter ")

for correct in range (100):
    if word[correct] == letter:
        print ("Success!")
        letters.append(letter)
        break
    else:
        print ("Wrong!  you have 1 try left")
        break


letter = input("input another letter ")

for correct in range (100):
    if word[correct] == letter:
        print ("Success!")
        letters.append(letter)
        break
    else:
        print ("Wrong!  You lost!")
        break


        
    





