import fr_core_news_lg
import os
from debate.politician import Politician
from nltk.corpus import stopwords

class Debate:

    def __init__(self, outputPath, stopwordsPath, answerSize):
        print("INFO: Chargement lexique \"fr_core_news_lg\"...")
        nlp = fr_core_news_lg.load()
        print("INFO: Rassemblement des stop words français...")
        sw = stopwords.words('french') + self.readStopwords(stopwordsPath)
        print("INFO: Chargement politique de gauche...")
        self.leftPolitician = Politician(os.path.join(outputPath, "gauche/gauche.txt"), sw, nlp, answerSize)
        print("INFO: Chargement politique de droite...")
        self.rigthPolitician = Politician(os.path.join(outputPath, "droite/droite.txt"), sw, nlp, answerSize)

    @staticmethod
    def readStopwords(path):
        file = open(path, "r")
        selfStopwords = []
        for line in file.readlines():
            selfStopwords.append(line.replace("\n", ""))
        file.close()
        return selfStopwords

    def getDebate(self, question):

        jsonBuffer = "{\"gauche\": \""
        jsonBuffer += self.leftPolitician.generateAnswer(question)
        jsonBuffer += "\", \"droite\": \""
        jsonBuffer += self.rigthPolitician.generateAnswer(question) + "\"}"

        return jsonBuffer
