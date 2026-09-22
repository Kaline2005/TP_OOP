from habitant_prive import Habitant #pour importer la classe habitant 

class Village: 
    def __init__(self,nom):
        self.nom = nom
        self.__habitants = [] #On créer une liste vide pour stocker les habitants du village

    def ajouter_habitant_composition(self,nom,age,adresse,animaux=None):
        nouvel_habitant = Habitant(nom,age,adresse,animaux) #On crée un nouvel habitant
        self.__habitants.append(nouvel_habitant) #On ajoute l'habitant à la liste des habitants du village

    def ajouter_habitant_aggregation(self,habitant):
        self.__habitants.append(habitant) 

    def afficher_habitants(self):
        for habitant in self.__habitants:
            print(f"{habitant.get_nom()}") #get_nom() se situe dans habitant_prive. C'est utlise pour récuperer le noms des habitants

pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_aggregation(elise)
autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages
assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()

#La méthode illustre une relation de composition car on crée un habitant qui possède des caractéristiques à la classe habitant donc l'habitant appartient à la classe.
#Et un élément dans un village ne peut pas exister sans le village. Donc si on supprime le village, l'habitant est supprimé aussi. Ce qui est la définition de la composition.

#La méthode illustre une relation d'agrégation car on ajoute un habitant déjà existant à la liste des habitants du village. 
# Donc l'habitant peut exister sans le village. Ce qui est la définition de l'agrégation.
