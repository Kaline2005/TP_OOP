class Habitant: 
    def __init__(self,nom,age,adresse,animaux=None):
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux if animaux is not None else {}  #On n'écrit pas animaux={} dans le init sinon le dict serait partagé par tous les habitant

    def affichage_adresse(self): #methode
        print(f"{self.nom} habite à {self.adresse}")

    def compte_animal(self,animal):
        return self.animaux.get(animal,0) #on cherche la clé avec get. Si elle existe on l'a récupère. Sinon on renvoie 0

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"