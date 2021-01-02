import gpt_2_simple as gpt2
import os


class Gpt:

    def __init__(self, modelType, modelName, tokenDir):
        self.modelType = modelType
        self.modelName = modelName
        self.tokenDir = tokenDir
        self.loadBaseModel()
        self.sess = gpt2.start_tf_sess()

    def loadBaseModel(self):
        if not os.path.isdir(os.path.join("models", self.modelType)):
            print("INFO: Téléchargement du modèle {} ...".format(self.modelType))
            gpt2.download_gpt2(model_name=self.modelType)

    def train(self, batchSize, step):
        gpt2.finetune(self.sess,
                      os.path.join(self.tokenDir, self.modelName + ".csv"),
                      model_name=self.modelType,
                      batch_size=batchSize,
                      run_name=self.modelName,
                      steps=step)

    def loadModel(self):
        gpt2.load_gpt2(self.sess,
                       run_name=self.modelName)

    def generate(self):
        output = gpt2.generate(self.sess,
                               run_name=self.modelName,
                               return_as_list=True,
                               length=100)
        print("-----------")
        print(output[0])
