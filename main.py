from command import *
import json
import sys

NB_SENTENCE = 5
MODEL_TYPE = "124M"

if __name__ == "__main__":

    try:

        tweeterToken = json.load(open("conf/tweeterToken.json", "r"))

    except Exception as e:

        print("ERROR: Token API Tweeter incorrect.\n{}".format(e))
        sys.exit()

    if len(sys.argv) < 2:
        print("ERROR: Prend au moins argument.\nLire le README.md.")
        sys.exit()

    if sys.argv[1] == "download":

        if len(sys.argv) < 3:
            print("ERROR: doawnload prend un argument.\nLire le README.md")
            sys.exit()

        assert sys.argv[2] in ["gauche", "droite"]

        print("INFO: Début du téléchargement des tweets...")
        doawnload("output/data", tweeterToken, sys.argv[2])

    if sys.argv[1] == "train":

        if len(sys.argv) < 3:
            print("ERROR: train prend 2 arguments.\n Lire le README.md.")
            sys.exit()

        assert sys.argv[2] in ["gauche", "droite"]

        train(MODEL_TYPE,
              sys.argv[2],
              "output/data",
              "output/token",
              "output/generate",
              "output/checkpoint",
              int(sys.argv[3]))

    if sys.argv[1] == "generate":

        if len(sys.argv) < 4:
            print("ERROR: generate prend 2 argument.\n Lire le README.md.")
            sys.exit()

        assert sys.argv[2] in ["gauche", "droite"]

        generate(sys.argv[2], MODEL_TYPE, "output/token", "output/generate", "output/checkpoint")

    if sys.argv[1] == "debate":
        debate("output/generate", "conf/stopwords.txt", NB_SENTENCE)
