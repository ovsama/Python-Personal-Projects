#This Python program creates a simple Multiple Choice Quiz.

#Create a list containing a bunch of questions for the quiz:
question_prompts =[
  "What color is water?\n(1) Blue\n(2) White\n(3) Colorless\n\n",                                           
  "What color is air?\n(1) Colorless\n(2) White\n(3) Yellow\n\n", 
  "What color is the sun?\n(1) Yellow\n(2) Colorless\n(3) White\n\n", 
    ]
 
#Create a class called 'Question':
class Question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

#Create a list of 'Question class' objects in order to store an answer for each prompt:
questions = [
     Question(question_prompts[0], "3"),
     Question(question_prompts[1], "1"),  
     Question(question_prompts[2], "3") 
 ]


#Create a function 'run_quiz' which allows running the quiz:
def run_quiz(questions):
    score=0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
                score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct") 

#Run the quiz:
run_quiz(questions)
















    
