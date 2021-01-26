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
        
        conda create -n politics_debate_env python=3.7.9
        
        conda activate politics_debate_env
        
        conda install tensorflow=1.15 spacy nltk
        
        pip install demoji tweepy gpt_2_simple flask
        
        python -m spacy download fr_news_core_lg


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

### Modèles entrainés

https://drive.google.com/drive/folders/1OoufqWVBulq5zG-KblGSAzE5dyKgip64?usp=sharing	
