class QuizBrain:
  def __init__(self, q_list):
    self.q_number = 0
    self.q_list = q_list
    self.score = 0

  def still_have_questions(self):
    return self.q_number < len(self.q_list)
  
  def next_question(self):
    current_question = self.q_list[self.q_number] 
    self.q_number += 1
    guess = input(f"Q.no {self.q_number}: {current_question.text} (True/False): ")
    self.check_answer(guess,current_question.answer)

  def check_answer(self,guess,correct):
    if guess.lower() == correct.lower():
      self.score += 1
      print("you got it\n")
    else:
      print("wrong answer")
    print(f"The correct Answer is {correct} ")
    print(f"your current score is {self.score} / {self.q_number}\n")



 


