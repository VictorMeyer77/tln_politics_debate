from dataGen.tweeterApi import TweeterApi
from gpt.tokenizer import Tokenizer
from gpt.gpt import Gpt


def doawnloadDataset(tweetsDir, tweeterToken, side):

    if side == "gauche":

        TweeterApi("@alexiscorbiere", tweetsDir, tweeterToken, side).run()
        TweeterApi("@AQuatennens", tweetsDir, tweeterToken, side).run()
        TweeterApi("@mbompard", tweetsDir, tweeterToken, side).run()
        TweeterApi("@JLMelenchon", tweetsDir, tweeterToken, side).run()
        TweeterApi("@ManonAubryFr", tweetsDir, tweeterToken, side).run()
        TweeterApi("@Anne_Hidalgo", tweetsDir, tweeterToken, side).run()
        TweeterApi("@yjadot", tweetsDir, tweeterToken, side).run()
        TweeterApi("@alicecoffin", tweetsDir, tweeterToken, side).run()
        TweeterApi("@Deputee_Obono", tweetsDir, tweeterToken, side).run()
        TweeterApi("@Clem_Autain", tweetsDir, tweeterToken, side).run()
        TweeterApi("@faureolivier", tweetsDir, tweeterToken, side).run()
        TweeterApi("@benoithamon", tweetsDir, tweeterToken, side).run()
        TweeterApi("@najatvb", tweetsDir, tweeterToken, side).run()
        TweeterApi("@PrudhommeLoic", tweetsDir, tweeterToken, side).run()
        TweeterApi("@n_arthaud", tweetsDir, tweeterToken, side).run()
        TweeterApi("@EvaJoly", tweetsDir, tweeterToken, side).run()
        TweeterApi("@MartineAubry", tweetsDir, tweeterToken, side).run()

    if side == "droite":

        TweeterApi("@MLP_officiel", tweetsDir, tweeterToken, side).run()
        TweeterApi("@J_Bardella", tweetsDir, tweeterToken, side).run()
        TweeterApi("@lepenjm", tweetsDir, tweeterToken, side).run()
        TweeterApi("@f_philippot", tweetsDir, tweeterToken, side).run()
        TweeterApi("@Stephane_Ravier", tweetsDir, tweeterToken, side).run()
        TweeterApi("@dupontaignan", tweetsDir, tweeterToken, side).run()
        TweeterApi("@louis_aliot", tweetsDir, tweeterToken, side).run()
        TweeterApi("@f_philippot", tweetsDir, tweeterToken, side).run()
        TweeterApi("@ECiotti", tweetsDir, tweeterToken, side).run()
        TweeterApi("@cestrosi", tweetsDir, tweeterToken, side).run()
        TweeterApi("@damienabad", tweetsDir, tweeterToken, side).run()
        TweeterApi("@NicolasSarkozy", tweetsDir, tweeterToken, side).run()
        TweeterApi("@xavierbertrand", tweetsDir, tweeterToken, side).run()
        TweeterApi("@datirachida", tweetsDir, tweeterToken, side).run()
        TweeterApi("@francoisbaroin", tweetsDir, tweeterToken, side).run()
        TweeterApi("@alainjupper", tweetsDir, tweeterToken, side).run()
        TweeterApi("@nadine_morano", tweetsDir, tweeterToken, side).run()


def trainGpt(modelType, modelName, tweetsDir, tokenDir, checkpointDir, step):
    Tokenizer(tweetsDir, tokenDir, modelName)
    gpt = Gpt(modelType, modelName, tokenDir, checkpointDir)
    gpt.train(step)


def generateFile(modelName, modelType, tokenDir, generateDir, chekpointDir):
    gpt = Gpt(modelType, modelName, tokenDir, chekpointDir)
    gpt.loadModel()
    gpt.generateSentencesFile(generateDir)
