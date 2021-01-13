from command import *
import json
import sys

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
        doawnloadDataset("output/data", tweeterToken, sys.argv[2])

    if sys.argv[1] == "train":

        if len(sys.argv) < 5:
            print("ERROR: train prend 4 arguments.\n Lire le README.md.")
            sys.exit()

        assert sys.argv[2] in ["gauche", "droite"]

        trainGpt(sys.argv[3],
                 sys.argv[2],
                 "output/data",
                 "output/token",
                 "output/generate",
                 "output/checkpoint",
                 int(sys.argv[4]))

    if sys.argv[1] == "generate":

        if len(sys.argv) < 4:
            print("ERROR: generate prend 2 argument.\n Lire le README.md.")
            sys.exit()

        assert sys.argv[2] in ["gauche", "droite"]

        generateFile(sys.argv[2], sys.argv[3], "output/token", "output/generate", "output/checkpoint")
