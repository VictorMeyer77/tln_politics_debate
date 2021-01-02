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
        print("INFO: Début du téléchargement des tweets...")
        doawnloadDataset("output/data", tweeterToken)

    if sys.argv[1] == "train":

        if len(sys.argv) < 5:
            print("ERROR: train prend 4 arguments.\n Lire le README.md.")
            sys.exit()

        trainGpt(sys.argv[3],
                 sys.argv[2],
                 "output/data",
                 "output/token",
                 "output/checkpoint",
                 int(sys.argv[4]))

    if sys.argv[1] == "generate":

        if len(sys.argv) < 3:
            print("ERROR: generate prend 1 argument.\n Lire le README.md.")
            sys.exit()

        generateFile(sys.argv[2], "output/token", "output/generate", "output/checkpoint")
