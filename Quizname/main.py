from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print(r"""
             .-')                         .-') _                                          
           .(  OO)                       (  OO) )                                         
          (_)---\_)  ,--. ,--.   ,-.-'),(_)----.        .-----.  .----.  .-----..------.  
          '  .-.  '  |  | |  |   |  |OO|       |       / ,-.   \/  ..  \/ ,-.   |   ___|  
         ,|  | |  |  |  | | .-') |  |  '--.   /        '-'  |  .  /  \  '-'  |  |  '--.   
        (_|  | |  |  |  |_|( OO )|  |(_(_/   /            .'  /|  |  '  |  .'  /`---.  '. 
          |  | |  |  |  | | `-' ,|  |_.'/   /___        .'  /__'  \  /  '.'  /__.-   |  | 
          '  '-'  '-('  '-'(_.-(_|  |  |        |      |       |\  `'  /|       | `-'   / 
           `-----'--' `-----'    `--'  `--------'      `-------' `---'' `-------'`----''  
             
              """)
question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
quiz=QuizBrain(question_bank)
while quiz.still():

    quiz.next_question()
    quiz.display()

print(f'You Have Completed The Quiz Your Final score is {quiz.score}')
