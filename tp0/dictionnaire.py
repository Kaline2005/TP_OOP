def quantite_piece(pieces_stock, modele, piece):
    return pieces_stock[modele][piece]

def consommer_piece(pieces_stock, modele, piece, quantite):
    if pieces_stock[modele][piece] >= quantite:
        pieces_stock[modele][piece] -= quantite


pieces_stock = {"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40}, "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},}
assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7
