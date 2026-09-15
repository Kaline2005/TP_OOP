def robots_double_mission(robots_exploration, robots_transport): #on retourne les robots qui sont capable de faire explo et tranp (intersection)
    return(robots_exploration & robots_transport)


def robots_toutes_missions(robots_exploration, robots_transport): #on retourne les robots qui sont capable de faire explo ou tranp (union)  
    return(robots_exploration | robots_transport)

def robots_exploration_seulement(robots_exploration, robots_transport): #on retourne les robots qui sont capable de faire explo mais pas tranp (difference)
    return(robots_exploration - robots_transport)


robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}


def ajouter_robot_mission(robots, robot): #on retourne un nouvel ensemble avec le robot ajouté
    return robots | {robot} 


def retirer_robot_mission(robots, robot): #on retourne un nouvel ensemble avec le robot retiré
    return robots - {robot}


ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")

assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
assert robots_transport == {"R5", "R9", "R7", "R3"}