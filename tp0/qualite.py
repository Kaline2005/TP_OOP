#Trois problèmes de test 
# identation non respectée
#Les apostrophes utilisées ne sont pas des apostrophes simples standard (’ au lieu de ')
#le paramètre d n'est jamais utilisé dans la fonction, il est donc inutile et peut être supprimé.

#Autre solution possible :
def cout_deplacement_propre(d, t, x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if t == 'R':
        c = dist * 1.0
    elif t == 'H':
        c = dist * 1.5
    elif t == 'S':
        c = dist * 2.0
    else:
        c = dist * 3.0
    print("cout:", c)
    return c
