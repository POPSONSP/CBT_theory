"""
PROJECT:
Write a cbt theory programme for a school whereby the students will be requested to sit for an exam,
respond to 10 random questions and at the end of the exams the score will be printed
"""
import time
nt=0
uname=["philip","sheriff","cosmos"]
passcode=["1234","5467","9867"]
user=input("provide your username: ").strip
user_pass=input("provide your passcode: ").strip           
if user in uname and user_pass==passcode[uname.index(user)]:
    print("welcome you can proceed to your examination page you have 50 minute ")
    questions=["1. Define a Noun ?", "2. Nigeria gain her independence in what year ?", "3.What is the three essential needs of human ?", 
           "4.SQI is what type of School ?", "5. Who is the president of Nigeria ?",
             "6. Who is the elected president in the 2023 election ?",
           "7.Nigeria National flag has how many coloursand namely ?", "8. Water refered to as tasteful,colourful and enzymes filled is said to be ?", 
           "9. Python can be refered to as ?", "10.Charges regarded as been positievely charged is know as ?"]
    answers= ["A noun is a name of any person animal, place or thing", "1960", "food, clothing and shelter", "coding", "president muhammadu buhari", "bola ahmed tinubu", "2, green and white", "bad","programming language", "proton"]
    score = 0
    for p in range(10):
        print(questions[p])
        time.sleep(2)
        user_answer = input("type in your prefered answer: ").strip
        if user_answer == answers[p].lower():
            print("Correct")
            score += 10
        else:
            print("Wrong")
            score -= 5
        nt+=1

    print(f"Congratulation, Your exam is over and your total score is {score}")
    
else:
    print("you have not registered for this exam")
    user=input("provide your username: ").strip
    user_pass=input("provide your passcode: ").strip