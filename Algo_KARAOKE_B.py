import random

class player:
    def __init__(self,nom):
        self.nom = str(nom)
        self.scores = [0,0,0,0,0]
        self.total = 0

    def moyenne(self):
        self.total = self.scores[0]+self.scores[1]+self.scores[2]+self.scores[3]+self.scores[4]
        self.total = self.total / 500
        self.total = self.total * 100

    def affiche(self):
        print(self.nom)
        print("MEILLEURS SCORES")
        for i in range(len(self.scores)):
         print ("chanson",i+1,"score =", self.scores[i])
        print("MOYENNE =",self.total)
    
save = 0

class karaoke:
    def __init__(self):
        self.chanson = ["Tell me why - BACSTREET BOYS","Cheddar - NEPAL","Xan - LUV RESVAL"]
        self.joueur =[]

    def affiche_chansons(self):
        print("LISTE CHANSON")
        for i in range(len(self.chanson)):
            print(self.chanson[i])

    def ajoute_joueur(self):
        self.joueur[save] = player("joueur")

RAP_Quizz = karaoke

RAP_Quizz.ajoute_joueur
RAP_Quizz.joueur[save]
