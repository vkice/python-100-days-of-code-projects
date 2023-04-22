### Custom code starts here ###
class Quiz:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
        
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f'\tQ. {self.question_number}: {current_question.text} (True/False)?: ').title()
        self.check_answer(user_input, current_question.answer)

            
    
    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer: # User must enter true, no validating and asking again
            print("Correct!")
            self.score += 1
        else: # Anything but true
            print("Wrong!")
        print(f"The correct answer is {current_answer}.\nYour current score is {self.score}/{self.question_number}\n")
        
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)