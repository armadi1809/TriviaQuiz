import data
from questionModel import QuestionModel
from quizBrain import QuizBrain
import html

def create_question_from_json(question_json):
    return QuestionModel(html.unescape(question_json['question']), html.unescape(question_json['correct_answer']), html.unescape(question_json['incorrect_answers'])) 

if __name__ == "__main__": 
    question_json = data.get_data() 
    question_bank = list(map(create_question_from_json, question_json))
    # print(question_bank)

    quiz = QuizBrain(question_bank) 

    while quiz.still_has_questions() : 
        quiz.ask_next_question()


