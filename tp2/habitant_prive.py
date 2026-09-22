class Habitant: 
    def __init__(self,nom,age,adresse,animaux=None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}#On n'écrit pas animaux={} dans le init sinon le dict serait partagé par tous les habitant.

    #getters (lecture)
    def get_nom(self): 
        return self.__nom

    def get_age(self):
        return self.__age

    def get_adresse(self):
        return self.__adresse

    def get_animaux(self):
        return self.__animaux
    
    #setters 
    def set_nom(self,nom): #le setter permet de modifier l'attribut 
        self.__nom = nom 

    def set_age(self,age):
        if age < 0: #on peux vérifier que la valeur de l'attribut est cohérente
            raise ValueError("L'age ne peut pas etre negatif")
        self.__age = age

    def set_adresse(self,adresse):
        self.__adresse = adresse

    def set_animaux(self,animaux):
        self.__animaux = animaux 

    #les methodes
    def affichage_adresse(self):
        print(f"{self.__nom} habite à {self.__adresse}")

    def compte_animal(self,animal):
        return self.__animaux.get(animal,0) #on cherche la clé avec get. Si elle existe on l'a récupère. Sinon on renvoie 0

h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.get_nom() == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"

h1.set_age(26) #on modifie l'âge de l'habitant
assert h1.get_age() == 26 #On vérifie que l'âge a bien été modifié
try:
   h1.set_age(-5) 
   assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass




class Habitant2: 
    def __init__(self,nom,age,adresse,animaux=None):
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}#On n'écrit pas animaux={} dans le init sinon le dict serait partagé par tous les habitant.

    #getters (lecture)
    def get_nom(self): 
        return self.__nom

    def get_adresse(self):
        return self.__adresse

    def get_animaux(self):
        return self.__animaux
    
    #setters 
    def set_nom(self,nom): #le setter permet de modifier l'attribut 
        self.__nom = nom 

    def set_adresse(self,adresse):
        self.__adresse = adresse

    def set_animaux(self,animaux):
        self.__animaux = animaux 


    #les methodes
    @property 
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age < 0 or age > 130: #on peux vérifier que la valeur de l'attribut est cohérente
            raise ValueError("L'age ne peut pas etre negatif ou superieur a 130")
        self.__age = age

    def affichage_adresse(self):
        print(f"{self.__nom} habite à {self.__adresse}")

    def compte_animal(self,animal):
        return self.__animaux.get(animal,0) #on cherche la clé avec get. Si elle existe on l'a récupère. Sinon on renvoie 0


h1 = Habitant2("Aldric", 25, "Rue A", {"vaches": 3})
assert h1.get_nom() == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0
h1.affichage_adresse() # affiche "Aldric habite a Rue A"

h1.age = 26 #on modifie l'âge de l'habitant
assert h1.age == 26
try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass


