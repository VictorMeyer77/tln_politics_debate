from dataGen.tweeterApi import TweeterApi
from dataGen.userTL import UserTL
#from textGenerator import TextGenerator
#from model.gpt import Gpt
from gpt.tokenizer import Tokenizer
from gpt.gpt import Gpt


def doawnload_dataset():

    UserTL("@alexiscorbiere", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@AQuatennens", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@mbompard", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    #UserTL("@JLMelenchon", TweeterApi().getApi(), ").run()
    UserTL("@ManonAubryFr", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@Anne_Hidalgo", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@yjadot", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@alicecoffin", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@Deputee_Obono", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@Clem_Autain", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@faureolivier", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@benoithamon", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@najatvb", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@PrudhommeLoic", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@n_arthaud", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@EvaJoly", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()
    UserTL("@MartineAubry", TweeterApi().getApi(), "/home/victor/esgi/M2/tln/tln_politics_debate/data").run()



doawnload_dataset()
#UserTL("@JLMelenchon", TweeterApi().getApi(), ").run()

#Tokenizer("output/token", "test01")
#gpt = Gpt("124M", "test01")
#gpt.train(1, 5)
#gpt.loadModel()
#gpt.generate()

