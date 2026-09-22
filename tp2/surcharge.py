from multipledispatch import dispatch

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

@dispatch(object,str)
def set_info(habitant,nom): #On est pas dans la classe on a donc pas de self. Mais habitant joue le même rôle que self il definit l'objet sur lequel on travaille
    habitant.nom = nom
   
@dispatch(object,str,int)
def set_info(habitant,nom,age):
    habitant.nom = nom
    habitant.age = age

h2 = Habitant("Bob", 40, "Rue C")
set_info(h2, "Robert") # met a jour le nom seulement
set_info(h2, "Robert", 41) # met a jour le nom et l’age