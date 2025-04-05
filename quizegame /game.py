questions =('What is the longest river in the world? ',
           'Who was the first President of the United States? ',
           'What is the chemical symbol for water?',
           'What is the value of π (pi) to two decimal places?')
options = (
    ('A) Nile River', 'B) Amazon River', 'C) Yangtze River', 'D) Mississippi River'),
    ('A) George Washington', 'B) Abraham Lincoln', 'C) Thomas Jefferson', 'D) John Adams'),
    ('A) H2O', 'B) CO2', 'C) O2', 'D) NaCl'),
    ('A) 3.14', 'B) 3.15', 'C) 3.16', 'D) 3.17')
)
aswers=('b','a','c','b')
guess=[]
score=0
question_num=0



for i in range(len(questions)):
    print('_______________________________')
    print(questions[i])  # Print the current question
    for option in options[i]:  # Print the options for the current question
        print(option)
    
    # Ask for the user's guess
    guess.append(input('Enter A, B, C, or D: ').lower())
    # Check if the guess is correct
    if guess[i] == aswers[i]:
        print('Correct!') 
        score += 1
    else:
        print('Wrong! The correct answer is:', aswers[i])
print("correct option are ",aswers)
print(f'your score is ',score)
