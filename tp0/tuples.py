def afficher_releve(releve):
    nom_capteur,valeur,unite = releve #On récupère les 3 valeurs du tubles dans releve
    return f"Capteur {nom_capteur} : {valeur} {unite}" #on retourne une chaine de caractères avec les valeurs du tuple pour verifier la validité de la fonction avec assert par la suite

releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"
assert afficher_releve(releve2) == "Capteur laser_arriere : 1.1 m" #renvoie 1.1  et pas 1.10
assert afficher_releve(releve3) == "Capteur gyroscope : 87.5 deg"

def recalibrer(releves,nom_capteur,valeur):
     
     for i in range(len(releves)):
          if releves[i][0] == nom_capteur: #On vérifie que le nom du relève correspond à celui que l'on veut modifier
                nouvelle_valeur = valeur
                releves[i] = (nom_capteur, nouvelle_valeur, releves[i][2]) #On remplace l'ancien tuple par un nouveau tuple avec la nouvelle valeur
                break
     return releves

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3
