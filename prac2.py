import random
def get_hangman_stage(remaining_attempts):
    max_attempts = 6
    stages = ["""
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """]
    return stages[max_attempts - remaining_attempts]
    
listOfWord=["word","try","run"]
#word=random.choice(listOfWord)
word="hello"
LenOfWord=len(word)
tries=6
UserGuess=list('-' * LenOfWord)
print(*UserGuess)

while tries>0:
 UserChar=input("Enter char ")    
 if UserChar in word:
     for CharIndex in range(LenOfWord):
         if UserChar == word[CharIndex]:
              UserGuess[CharIndex]=UserChar
     print(*UserGuess)
     if('-' not in UserGuess):
            print("You Win")
            break
 else:
    #print("ERROR Guess,try agian")
    tries-=1
    print(get_hangman_stage(tries))
    
    
else:
    print("faild")    



            


