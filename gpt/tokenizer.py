import demoji
import re
import os

demoji.download_codes()

END_CHAR = [".", "!", "?", "\n"]


class Tokenizer:

    def __init__(self, dataDir, tokenDir, modelName):

        self.dataDir = dataDir
        self.tokenDir = tokenDir + "/" + modelName + ".csv"

        self.run()

    def readData(self):

        text = ""

        for file in os.listdir(self.dataDir):

            path = os.path.join(self.dataDir, file)

            if os.path.isfile(path):

                file = open(path, "r")
                text += file.read()
                file.close()

        return text

    def run(self):

        data = self.readData()
        data = self.removeHttp(data)
        data = self.getSentences(data)

        data = self.removeRt(data)
        data = self.removeAnnouceSentence(data)
        data = self.removeStartHashTag(data)
        data = self.removeShortSentences(data)
        data = self.replaceHashtagAndMention(data)
        data = self.removeEmoji(data)

        self.writeTokens(data)

    @staticmethod
    def getSentences(text):

        tokens = []

        tokenBuffer = ""

        for char in text:

            tokenBuffer += char

            if char in END_CHAR:
                tokens.append(tokenBuffer)
                tokenBuffer = ""

        return tokens

    @staticmethod
    def removeShortSentences(tokens):

        longTokens = []

        for token in tokens:

            if len(token.split(" ")) > 10:
                longTokens.append(token)

        return longTokens

    @staticmethod
    def removeHttp(text):

        return re.sub(r"https://t\.co/.{10}", " ", text)

    @staticmethod
    def removeRt(tokens):

        cleanTokens = []

        for token in tokens:

            tokenBuffer = ""
            words = token.split(" ")

            for i in range(len(words)):

                if not (words[i] == "RT" or (i > 0 and words[i - 1] == "RT")):
                    tokenBuffer += (words[i] + " ")

            cleanTokens.append(tokenBuffer.strip())

        return cleanTokens

    @staticmethod
    def removeAnnouceSentence(tokens):

        cleanTokens = []

        for token in tokens:

            if token.count("#") + token.count("@") < 3:
                cleanTokens.append(token)

        return cleanTokens

    @staticmethod
    def removeStartHashTag(tokens):

        cleanTokens = []

        for token in tokens:

            words = token.split(" ")

            if not (len(words[0]) > 0 and words[0][0] == "#"):
                cleanTokens.append(token)

        return cleanTokens

    @staticmethod
    def replaceHashtagAndMention(tokens):

        cleanTokens = []

        for token in tokens:
            cleanTokens.append(token.replace("#", " ").replace("@", " ").strip())

        return cleanTokens

    @staticmethod
    def removeEmoji(tokens):

        cleanTokens = []

        for token in tokens:
            cleanTokens.append(demoji.replace(token, " ").strip())

        return cleanTokens

    def writeTokens(self, tokens):

        file = open(self.tokenDir, "w+")

        for token in tokens:
            file.write(token + "\n")

        file.close()
