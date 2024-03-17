def exercice1(tirage, motsPossibles):
    """cette fonction prend en arg une liste de lettres (tirage) et une liste de mots possibles (motsPossibles) et répond à l'exercice 1"""
    mots = []
    for mot in motsPossibles:
        ajouter = True
        for lettre in mot:
            if lettre not in tirage or mot.count(lettre) > tirage.count(lettre):
                ajouter = False
        if ajouter:
            mots.append(mot)
    mots.sort(key=lambda mot:len(mot), reverse= True)
    return mots[0]

#Tests => voir le fichier tests.py
