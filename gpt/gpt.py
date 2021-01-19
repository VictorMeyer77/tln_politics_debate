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

        i = 0

        while i < 2000:

            output = gpt2.generate(self.sess,
                                   run_name=self.side,
                                   checkpoint_dir=self.checkpointDir,
                                   return_as_list=True,
                                   length=1000)

            for sentence in output[0].split("\n"):

                cleanSentence = sentence.replace("<|startoftext|>", "").replace("<|endoftext|>", "").strip()

                if len(cleanSentence.split(" ")) > 7 and cleanSentence[-1] in END_CHAR:
                    file.write(cleanSentence + "\n")
                    i += 1

        file.close()