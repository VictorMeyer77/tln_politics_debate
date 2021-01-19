from flask import Flask
from debate.debate import Debate

def launchApi(outputPath, stopwordsPath, answerSize):

    app = Flask(__name__)
    debate = Debate(outputPath, stopwordsPath, answerSize)

    @app.route('/')
    def index():
        return "<h1>Politics debate API </h1>"

    @app.route('/debate/<question>')
    def about(question):

        return debate.getDebate(str(question))
    app.run()