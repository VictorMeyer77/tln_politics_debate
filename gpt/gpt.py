import gpt_2_simple as gpt2
import os


class Gpt:

    def __init__(self, modelType, modelName, tokenDir, checkpointDir):
        self.modelType = modelType
        self.modelName = modelName
        self.tokenDir = tokenDir
        self.checkpointDir = checkpointDir
        self.loadBaseModel()
        self.sess = gpt2.start_tf_sess()

    def loadBaseModel(self):
        if not os.path.isdir(os.path.join("models", self.modelType)):
            print("INFO: Téléchargement du modèle {} ...".format(self.modelType))
            gpt2.download_gpt2(model_name=self.modelType)

    def train(self, step):
        gpt2.finetune(self.sess,
                      os.path.join(self.tokenDir, self.modelName + ".csv"),
                      model_name=self.modelType,
                      run_name=self.modelName,
                      checkpoint_dir=self.checkpointDir,
                      steps=step)

    def loadModel(self):
        gpt2.load_gpt2(self.sess,
                       checkpoint_dir=self.checkpointDir,
                       run_name=self.modelName)

    def generateSentencesFile(self, outputDir):
        output = gpt2.generate(self.sess,
                               run_name=self.modelName,
                               checkpoint_dir=self.checkpointDir,
                               return_as_list=True,
                               length=100)

        file = open(os.path.join(outputDir, self.modelName + ".txt"), "w+")

        for sentence in output:
            file.write(sentence)

        file.close()
