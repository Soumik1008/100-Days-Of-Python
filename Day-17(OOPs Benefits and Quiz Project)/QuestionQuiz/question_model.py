class Question:
    def __init__(self,q_text,q_answer):
        self.text = q_text
        self.answer = q_answer
        
ques = Question("India is great","True")
print(ques.text)