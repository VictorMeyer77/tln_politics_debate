# POLITICS DEBATE
## ESGI 5IABD Cousin Cécile, Alexandre Matthieu, Fauvert Baptiste, Victor Meyer

Api générant un debat politique.  
La génération de texte est basée sur un modèle GPT2.  
Les données d'entrainement proviennent de comptes tweeter de politiques français de gauche et de droite.  

### Prérequis

Un fichier "tweeterToken.json" doit être placé dans le répertoire conf/  

        {
    
          "consumer_key": "",
          "consumer_secret": "",
          "access_token": "",
          "access_token_secret": ""
    
        }

Renseigner ses tokens de l'api tweeter:  
https://developer.twitter.com/en

### Environnement

Windows est vivement déconseillé
        
        conda upgrade conda  
        
        conda create -n politics_debate_env python=3.7.9
        
        conda activate politics_debate_env
        
        conda install tensorflow=1.15 spacy nltk
        
        pip install demoji tweepy gpt_2_simple flask
        
        python -m spacy download fr_core_news_lg


Lancer un terminal python

        import nltk
        
        nltk.download("stopwords")

### utilisation

Télécharger les tweets:  

        python main.py download droite/gauche

Lancer entrainement:  

        python main.py train droite/gauche 1000
        # 1000 -> epochs

Lancer la génération du fichiers de réponses:  

        python main.py generate droite/gauche

Lancer l'api de débat:  
        
        python main.py debate

### Utilisation API

Url de requête:

        http://127.0.0.1:5000/debate/ma question politique ?
        
Réponse:

    {
        "gauche": "La réponse de l'IA de gauche",
        "droite": "La réponse de l'IA de droite"
    }

### Modèles entrainés

https://drive.google.com/drive/folders/1OoufqWVBulq5zG-KblGSAzE5dyKgip64?usp=sharing

A placer dans le dossier checkpoint/	
