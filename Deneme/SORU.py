# QUİZ SORULARI HAZIRLAMA 
"""

# Question
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
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+ q)
        
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

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
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question('en iyi programlama dili hangisidir ?', ['C#','python','javascript','java'], 'python')
q2 = Question('en popüler programlama dili hangisidir ?', ['python','javascript','C#','java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q4 = Question('en çok sevilen programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q5 = Question('en kolay programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')

questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)

quiz.loadQuestion()

"""



#TÜRKÇESİ

class Test():
    def __init__(self, soru, secimler , cevap):
        self.soru = soru
        self.secimler = secimler
        self.cevap = cevap

    def verilen_cevap(self, cevap):
        return self.cevap == cevap

class Quiz:
    def __init__(self, test):
        self.test = test
        self.skor = 0
        self.soru_index = 0
    def soru_yeri(self ):
        return self.test[self.soru_index]

    def ekran_sorusu(self):
        test = self.soru_yeri()
        print(f' {self.soru_index + 1 }: {test.soru} ')

        for q in test.secimler:
            print('-' + q)

        cevap = input('Cevap: ')
        self.tahmin(cevap)
        self.soruyukle()

    def tahmin(self , cevap):
        test = self.soru_yeri()
        if test.verilen_cevap(cevap):
            self.skor += 1
        self.soru_index += 1        

    def soruyukle(self):
        if len(self.test) == self.soru_index:
            self.skorugoster()
        else:
            self.ilerlemegoster()
            self.ekran_sorusu()
    def skorugoster(self):
        print('Skor: ' , self.skor)
    
    def ilerlemegoster(self):
        tamamensorgulama = len(self.test)
        testNumarasi = self.soru_index + 1

        if testNumarasi > tamamensorgulama : 
            print('Sınav bitti..')
        else:
            print(f"Test {testNumarasi} of {tamamensorgulama} ".center(100 , '*'))                




t1 = Test('en iyi programlama dili hangisidir ?', ['C#','python','javascript','java'], 'python')
t2 = Test('en popüler programlama dili hangisidir ?', ['python','javascript','C#','java'], 'python')
t3 = Test('en çok kazandıran programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
t4 = Test('en çok sevilen programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
t5 = Test('en kolay programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')


testler = [t1, t2, t3 , t4, t5]

quiz = Quiz(testler)
quiz.soruyukle()


























