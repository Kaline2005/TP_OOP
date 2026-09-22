class Livre:
    def __init__(self,titre,auteur,nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages

    def resume(self):
        return f"{self.titre} est un livre écrit par {self.auteur} et contient {self.nb_pages} pages"

    def lire(self,pages):
        if pages > self.nb_pages:
            return "Vous ne pouvez pas dépasser le nombre de pages du livre"
        else:
            self.nb_pages -= pages
            return f"Vous avez lu {pages} pages. Il reste {self.nb_pages} pages à lire"

Oiseau = Livre("L'Oiseau", "Jean Dupont", 250)
print(Oiseau.resume())
Pages = 50
print(Oiseau.lire(Pages))

      
