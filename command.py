from dataGen.tweeterApi import TweeterApi
from gpt.tokenizer import Tokenizer
from gpt.gpt import Gpt


def doawnloadDataset(tweetsDir, tweeterToken):
    TweeterApi("@alexiscorbiere", tweetsDir, tweeterToken).run()
    TweeterApi("@AQuatennens", tweetsDir, tweeterToken).run()
    TweeterApi("@mbompard", tweetsDir, tweeterToken).run()
    TweeterApi("@JLMelenchon", tweetsDir, tweeterToken).run()
    TweeterApi("@ManonAubryFr", tweetsDir, tweeterToken).run()
    TweeterApi("@Anne_Hidalgo", tweetsDir, tweeterToken).run()
    TweeterApi("@yjadot", tweetsDir, tweeterToken).run()
    TweeterApi("@alicecoffin", tweetsDir, tweeterToken).run()
    TweeterApi("@Deputee_Obono", tweetsDir, tweeterToken).run()
    TweeterApi("@Clem_Autain", tweetsDir, tweeterToken).run()
    TweeterApi("@faureolivier", tweetsDir, tweeterToken).run()
    TweeterApi("@benoithamon", tweetsDir, tweeterToken).run()
    TweeterApi("@najatvb", tweetsDir, tweeterToken).run()
    TweeterApi("@PrudhommeLoic", tweetsDir, tweeterToken).run()
    TweeterApi("@n_arthaud", tweetsDir, tweeterToken).run()
    TweeterApi("@EvaJoly", tweetsDir, tweeterToken).run()
    TweeterApi("@MartineAubry", tweetsDir, tweeterToken).run()


def trainGpt(modelType, modelName, tweetsDir, tokenDir, checkpointDir, step):
    Tokenizer(tweetsDir, tokenDir, modelName)
    gpt = Gpt(modelType, modelName, tokenDir, checkpointDir)
    gpt.train(step)


def generateFile(modelName, modelType, tokenDir, generateDir, chekpointDir):
    gpt = Gpt(modelType, modelName, tokenDir, chekpointDir)
    gpt.loadModel()
    gpt.generateSentencesFile(generateDir)
