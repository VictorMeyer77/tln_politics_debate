#from dataGen.tweeterApi import TweeterApi
#from textGenerator import TextGenerator
from gpt.tokenizer import Tokenizer
from gpt.gpt import Gpt

TWEET_DIR = "C:/Users/Utilisateur/Work/ESGI/TLN/tln_politics_debate/data"
"""
def doawnload_dataset():

    TweeterApi("@alexiscorbiere", TWEET_DIR).run()
    TweeterApi("@AQuatennens", TWEET_DIR).run()
    TweeterApi("@mbompard", TWEET_DIR).run()
    TweeterApi("@JLMelenchon", TWEET_DIR).run()
    TweeterApi("@ManonAubryFr", TWEET_DIR).run()
    TweeterApi("@Anne_Hidalgo", TWEET_DIR).run()
    TweeterApi("@yjadot", TWEET_DIR).run()
    TweeterApi("@alicecoffin", TWEET_DIR).run()
    TweeterApi("@Deputee_Obono", TWEET_DIR).run()
    TweeterApi("@Clem_Autain", TWEET_DIR).run()
    TweeterApi("@faureolivier", TWEET_DIR).run()
    TweeterApi("@benoithamon", TWEET_DIR).run()
    TweeterApi("@najatvb", TWEET_DIR).run()
    TweeterApi("@PrudhommeLoic", TWEET_DIR).run()
    TweeterApi("@n_arthaud", TWEET_DIR).run()
    TweeterApi("@EvaJoly", TWEET_DIR).run()
    TweeterApi("@MartineAubry", TWEET_DIR).run()

"""

#doawnload_dataset()

#Tokenizer("data", "output/token", "test01")
gpt = Gpt("124M", "test01", "output/token")
gpt.train(10, 1000)
#gpt.loadModel()
gpt.generate()

