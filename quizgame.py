def quiz_game():
    guesses=[]
    your_correct_answers=0
    question_num=1

    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("Enter option(A,B,C,D):")
        guess=guess.upper()
        guesses.append(guess)
        your_correct_answers+=check_answer(questions.get(key),guess)
        question_num+=1
    display_score(your_correct_answers,guesses)

def check_answer(answer,guess):
    if answer==guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
def display_score(your_correct_answers,guesses):
    print("-------------")
    print("Results:")
    print("-------------")
    print("Correct Answers:")
    for j in questions:
        print(questions.get(j),end=" ")
    print()
    print("Your answers:")
    for i in guesses:
        print(i,end=" ")
    print()

    score=int(your_correct_answers)
    print("Your score is: "+str(score)+" out of 5")
    if score==5:
        print("Congralutions")

def play_again():
    response=input("Do you want to play again?(Yes or No):")
    response=response.upper()
    if response=="YES":
        return True
    else:
        return False


questions={
    "What is the function key used for refreshing page?": "B",
    "What is the gas used for fire extinguishing?":"C",
    "How many kilograms is 1 ton?":"D",
    "Where is the headquarters of Indian Railway situated?":"A",
    "In which year India got independence?":"C"
}
options=[
    ["A. F3","B. F5","C. F7","D. F4"],
    ["A. Hydrogen","B. Oxygen","C. Carbon Dioxide","D. Nitrogen"],
    ["A. 10","B. 50","C. 100","D. 1000"],
    ["A. New Delhi","B. Mumbai","C. Chennai","D. Hyderabad"],
    ["A. 1945","B. 1946","C. 1947","D. 1949"]
]
quiz_game()
while play_again():
    quiz_game()
print("Wokey Bei..")

