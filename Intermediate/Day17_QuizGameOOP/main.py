### Custom code starts here ###
import requests
from question_model import Question
from quiz_brain import Quiz

# Trivia questions generated from https://opentdb.com/api_config.php
## 10 Easy Video Game questions True/False
url = "https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=boolean"
question_data = requests.get(url).json()

# Convert the Trivia API JSON into our question bank
question_bank = []
for question in question_data["results"]:
    question_bank.append(Question(text=question["question"], answer=question["correct_answer"]))
quiz = Quiz(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You have finished the quiz, thanks for playing!\nYour final score is {quiz.score}/{quiz.question_number}\n\n")