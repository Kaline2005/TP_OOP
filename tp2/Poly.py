from abc import ABC,abstractmethod 

class Habitant(ABC): 
    def __init__(self,nom,prenom,age,adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse

    def affichage_adresse(self): #methode
        print(f"{self.nom} habite à {self.adresse}")

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        pass


    def __str__(self):
                return f"{self.nom}, {self.prenom}, {self.age} ans, habite à {self.adresse}"
    


class Adulte(Habitant): #classe qui hérite de la classe Habitant
    def __init__(self, nom, prenom, age, adresse):
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans")
        super().__init__(nom, prenom, age, adresse) #permet d'avoir accès aux attributs de la classe mère

    def calcul_nombre_annee_avant_retraite(self):
        age_retraite = 62
        if self.age >= age_retraite:
            return "Déjà à la retraite"
        return age_retraite - self.age

class Enfant(Habitant):
    def __init__(self, nom, prenom, age,adresse):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")
        super().__init__(nom, prenom, age, adresse)

    def calcul_nombre_annee_avant_retraite(self):
            return "Erreur : un enfant ne peut pas calculer sa retraite"

    
def affichage(h : Habitant):
        print(str(h))

Adulte = Adulte("Dupont", "Marie", 35, "Rue A")
Enfant = Enfant("Martin", "Lucas", 12, "Rue B")

affichage(Adulte)
affichage(Enfant)