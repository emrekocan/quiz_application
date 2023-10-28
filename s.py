#question

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        Question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {Question.text}')

        for q in Question.choices:
            print('-'+ q)

        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

        self.displayQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('score: ', self.score)
    def displayProgress(self):
        totalQuestion = len(self.questions)
        QuestionNumber = self.questionIndex + 1

        if QuestionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {QuestionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question('en iyi programlama dili hangisidir?', ['c#', 'python', 'javascript'], 'python')
q2 = Question('en popüler programlama dili hangisidir?', ['c#', 'python', 'javascript'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir?', ['c#', 'python', 'javascript'], 'python')
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.loadQuestion()