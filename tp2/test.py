import unittest

from habitant_prive import Habitant2
from village import Village
from Heritage import Adulte, Enfant


# TESTS HABITANT

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant et l'encapsulation."""

    def setUp(self):
        self.habitant = Habitant2("Aldric",25,"Rue A",{"vaches": 3})

    def test_age_setter_valide(self):
        """Vérifie qu'on peut modifier l'âge avec une valeur valide."""
        self.habitant.age = 26

        self.assertEqual(self.habitant.age, 26)

    def test_age_setter_invalide(self):
        """Cas limite : âge négatif."""
        with self.assertRaises(ValueError):
            self.habitant.age = -5

    def test_compte_animal(self):
        """Vérifie qu'on compte correctement un animal."""
        self.assertEqual(
            self.habitant.compte_animal("vaches"),3)

    def test_compte_animal_non_possede(self):
        """Cas limite : l'habitant ne possède pas cet animal."""
        self.assertEqual(self.habitant.compte_animal("moutons"),0)



# TESTS VILLAGE

class TestVillage(unittest.TestCase):

    def test_ajout_composition(self):
        """Vérifie l'ajout d'un habitant par composition."""

        village = Village("PyTown")

        village.ajouter_habitant_composition("Maude",20,"Rue Orange",{"moutons": 3})

        self.assertEqual(len(village.get_habitants()),1)

        self.assertEqual(village.get_habitants()[0].get_nom(),"Maude")

    def test_ajout_aggregation(self):
        """Vérifie l'ajout d'un habitant existant par agrégation."""

        village = Village("PyTown")

        lila = Habitant2("Lila",28,"Rue Soleil",{"poules": 10})

        village.ajouter_habitant_aggregation(lila)

        self.assertIn(lila,village.get_habitants())

    def test_meme_habitant_deux_villages(self):
        """Cas limite :"""

        village1 = Village("PyTown")
        village2 = Village("VillageVoisin")

        lila = Habitant2("Lila",28,"Rue Soleil",{"poules": 10})

        village1.ajouter_habitant_aggregation(lila)
        village2.ajouter_habitant_aggregation(lila)

        self.assertIn(lila,village1.get_habitants())

        self.assertIn(lila,village2.get_habitants())

        self.assertEqual(len(village1.get_habitants()),1)

        self.assertEqual(len(village2.get_habitants()),1)


# TESTS HERITAGE

class TestHeritage(unittest.TestCase):

    def test_retraite_adulte(self):
        """Un adulte de 20 ans doit avoir 42 ans avant la retraite."""

        adulte = Adulte("Pierre","Marie",20,"Rue Coquelicot")

        self.assertEqual(adulte.calcul_nombre_annee_avant_retraite(),42)

    def test_retraite_enfant(self):
        """Un enfant ne peut pas calculer sa retraite."""

        enfant = Enfant("Banana","Martine",12,"Rue Banane")

        self.assertIn("enfant",enfant.calcul_nombre_annee_avant_retraite())

    def test_enfant_age_invalide(self):
        """Cas limite : un enfant de 20 ans doit provoquer une ValueError."""

        with self.assertRaises(ValueError):
            Enfant("Oups","Test",20,"Rue C")

if __name__ == "__main__":
    unittest.main(verbosity=2)