print("Welcome for the quiz game \n\n\n     GET Ready For The Quiz!")

playing= input("Do you want to play?   ")

if playing.lower() != "yes":
    quit()
    
print("Okey! Lets play")
score= 0

print("Answer the following questions:")

questions = [
    {"question": "What does STD stand for?", "answer": "sexually transmitted disease"},
    {"question": "What is the primary method to prevent pregnancy?", "answer": "contraception"},
    {"question": "What is the process of fertilizing an egg called?", "answer": "fertilization"},
    {"question": "What is the age of consent?", "answer": "18"},
    {"question": "What organ produces sperm in males?", "answer": "testicles"},
    {"question": "What is the female reproductive cell called?", "answer": "egg"},
    {"question": "What is the male reproductive cell called?", "answer": "sperm"},
    {"question": "What is the name of the female reproductive organ where a baby develops?", "answer": "uterus"},
    {"question": "What is the tube that carries urine and semen in males?", "answer": "urethra"},
    {"question": "What does HIV stand for?", "answer": "human immunodeficiency virus"},
    {"question": "What is the most effective way to prevent STDs?", "answer": "abstinence"},
    {"question": "What is the term for a long-term contraceptive inserted into the uterus?", "answer": "iud"},
    {"question": "What is the name of the hormone primarily responsible for male characteristics?", "answer": "testosterone"},
    {"question": "What is the hormone primarily responsible for female characteristics?", "answer": "estrogen"},
    {"question": "What is the process of a fertilized egg attaching to the uterus wall called?", "answer": "implantation"},
    {"question": "What does PMS stand for?", "answer": "premenstrual syndrome"},
    {"question": "What is the method of tracking ovulation by monitoring body temperature?", "answer": "fertility awareness"},
    {"question": "What is the barrier method of contraception called?", "answer": "condom"},
    {"question": "What is the natural cessation of menstruation in women called?", "answer": "menopause"},
    {"question": "What is the term for an unplanned pregnancy?", "answer": "unintended pregnancy"},
]

for q in questions:
    answer = input(q["question"] + " ")
    if answer.lower() == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"\nYour final score is: {score}/{len(questions)}")
if score == len(questions):
    print("Amazing! You got all the answers correct!")
elif score > len(questions) // 2:
    print("Good job! Keep learning.")
else:
    print("Don't worry! Keep studying and try again.")