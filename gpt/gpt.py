import gpt_2_simple as gpt2
import os

END_CHAR = [".", "!", "?"]

class Gpt:

    def __init__(self, modelType, side, tokenDir, checkpointDir, outputDir):
        self.modelType = modelType
        self.side = side
        self.outputDir = os.path.join(outputDir, side)
        self.tokenDir = os.path.join(tokenDir, side)
        self.checkpointDir = checkpointDir
        self.loadBaseModel()
        self.sess = gpt2.start_tf_sess()

    def loadBaseModel(self):
        if not os.path.isdir(os.path.join("models", self.modelType)):
            print("INFO: Téléchargement du modèle {} ...".format(self.modelType))
            gpt2.download_gpt2(model_name=self.modelType)

    def train(self, step):
        gpt2.finetune(self.sess,
                      os.path.join(self.tokenDir, self.side + ".csv"),
                      model_name=self.modelType,
                      run_name=self.side,
                      checkpoint_dir=self.checkpointDir,
                      steps=step)

    def loadModel(self):
        gpt2.load_gpt2(self.sess,
                       checkpoint_dir=self.checkpointDir,
                       run_name=self.side)

    def generateSentencesFile(self):

        file = open(os.path.join(self.outputDir, self.side + ".txt"), "a")

        for i in range(500):

            output = gpt2.generate(self.sess,
                                   run_name=self.side,
                                   checkpoint_dir=self.checkpointDir,
                                   return_as_list=True,
                                   length=100000)

            print("INFO: {}/10000".format(i * 20))

            for sentence in output:
                file.write(sentence)

        file.close()

    def cleanGenerateFile(self):

        source = open(os.path.join(self.outputDir, self.side + ".txt"), "r")
        cible = open(os.path.join(self.outputDir, self.side + ".txt_tmp"), "w+")

        lines = source.readlines()

        for line in lines:

            cleanLine = line.replace("<|startoftext|>", "").replace("<|endoftext|>", "")
            if len(cleanLine.split(" ")) > 6 and cleanLine[-1] in END_CHAR:
                cible.write(cleanLine)

        source.close()
        cible.close()

        os.remove(os.path.join(self.outputDir, self.side + ".txt"))
        os.rename(os.path.join(self.outputDir, self.side + ".txt_tmp"),
                  os.path.join(self.outputDir, self.side + ".txt"))
