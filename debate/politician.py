
class Politician:

    def __init__(self, answerPath, stopwords, nlp, answerSize):

        self.nlp = nlp
        self.stopwords = stopwords
        self.answer = self.readAnswer(answerPath)
        self.nlpAnswer = self.getNlpAnswer()
        self.answerSize = answerSize

    @staticmethod
    def readAnswer(path):
        file = open(path, "r")
        answer = []
        for line in file.readlines():
            answer.append(line.replace("\n", ""))
        file.close()
        return answer

    def cleanSentence(self, sentence):

        cleanWords = ""
        for word in sentence.split(" "):

            if word.lower() not in self.stopwords and len(word) > 4:
                cleanWords += (word + " ")

        return cleanWords

    def getNlpAnswer(self):

        nlpAnswer = []
        for answer in self.answer:
            nlpAnswer.append(self.nlp(self.cleanSentence(answer)))

        return nlpAnswer

    def generateAnswer(self, sentence):

        scores = {}
        nlpSentence = self.nlp(self.cleanSentence(sentence))

        for i in range(len(self.answer)):
            scores[self.answer[i]] = nlpSentence.similarity(self.nlpAnswer[i])

        bestAnswers = list({k: v for k, v in sorted(scores.items(),
                                                    key=lambda item: item[1], reverse=True)}.items())[:self.answerSize]

        finalAnwser = ""
        for a in bestAnswers:
            finalAnwser += (a[0] + "\n")

        return finalAnwser
