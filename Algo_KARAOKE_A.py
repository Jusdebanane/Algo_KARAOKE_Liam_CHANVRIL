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
    

chanson =["chanson1","chanson2","chanson3","chanson4","chanson5"]
score = 0
chanson_choisie = 0

player1 = player("1")
player2 = player("2")

player1.nom = input("JOUEUR 1/ votre nom? : ")
player2.nom = input("JOUEUR 2/ votre nom? : ")

joueur = player1

while(True):
    
    
    print("C'est au tour de ",joueur.nom)

    print("Choisissez une chanson:")
    for i in range(len(chanson)):
        print(i+1,":",chanson[i])
    chanson_choisie = int(input("votre choix:"))
    if(chanson_choisie>5):
        print("Cette chanson n'est pas dans la liste !")
    else:
        score = random.randint(50,100)

        print("Votre score : ", score)
        if(score>player1.scores[chanson_choisie -1]):
            player1.scores[chanson_choisie -1] = score
        
        joueur.moyenne()
        joueur.affiche()
        if (joueur == player1):
            joueur = player2
        else:
            joueur = player1