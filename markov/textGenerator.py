import markovify
import os
import spacy

class TextGenerator:

    def __init__(self):

        self.dataPath = "data/"
        self.text = ""
        self.model = None
        self.nlp = spacy.load("fr_core_news_lg")

    def loadData(self):

        for path in os.listdir(self.dataPath):

            if os.path.isfile(self.dataPath + path):
                file = open(self.dataPath + path, "r", encoding="latin-1")
                self.text += file.read()
                file.close()

    def writeData(self):

        file = open("data/data_tmp.txt", "w+")
        file.write(self.text)
        file.close()


    def train(self):

        self.model = markovify.Text(self.text)

    def get_vector(self, sentence):

        vector = []
        for token in self.nlp(sentence):
            vector.append([token.text, token.has_vector, token.vector_norm])

        return vector

    def is_wrong_word(self, vector):

        for token in vector:
            if token[2] < 0.0001:
                return True

        return False

    def similarity(self, sentence, word):

        avg = 0.0
        for w in sentence.split(" "):

            avg += self.nlp(w).similarity(self.nlp(word))

        return avg / len(sentence)


    def generate(self):

        if self.model is not None:
            sentence = self.model.make_short_sentence(280)

            print(sentence)

