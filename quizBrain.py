
class QuizBrain: 
    def __init__(self, quiz_bank): 
        self.quiz_bank = quiz_bank 
        self.question_idx = 0 
        self.score = 0

    def still_has_questions(self): 
        return self.question_idx < len(self.quiz_bank) 
    
    def ask_next_question(self): 
        question = self.quiz_bank[self.question_idx]
        answer = input(f'Question {self.question_idx + 1}: {question.question}') 
        if answer.lower() == question.correct_answer.lower(): 
            self.score += 1 
            print('Good Job, Your asnwer was correct')
        else: 
            print('Sorry, this answer was incorrect')
        
        self.question_idx += 1

        if self.question_idx == len(self.quiz_bank): 
            print(f'Thanks for playing, your total score was {self.score}')


    