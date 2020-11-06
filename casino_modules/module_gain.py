from module_tirage import machine

# serie pour ordonner les valeurs chiffrées du tirage (on se basera sur les index)
serie = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']


def decompose_jeu(tirage_final: list):
    # tri des valeurs en fonction de l'index de la carte dans serie
    tirage_final.sort(key=lambda carte: serie.index(carte.split('-')[0]))
    print('tirage_final trié par valeur', tirage_final)

    # extraction des valeurs et des couleurs des 5 cartes tirées
    v_cartes = []
    c_cartes = []
    for carte in tirage_final:
        valeur, couleur = carte.split('-')
        v_cartes.append(valeur)
        c_cartes.append(couleur)
    print('v_cartes : ', v_cartes)
    print('c_cartes : ', c_cartes)
    return v_cartes, c_cartes


# combinaisons gagnantes
def quinte_royale(v_cartes: list):
    return v_cartes == ['10','J','Q','K','A']

def flush(c_cartes: list):
    if c_cartes.count(c_cartes[0]) != 5:
        return False
    return True

def quinte(v_cartes: list):
    for indice, valeur in enumerate(v_cartes[:-1]):
        valeur_suivante = v_cartes[indice + 1]
        if valeur == '5' and valeur_suivante == 'A':
            break
        if valeur_suivante != serie[serie.index(valeur) + 1]:
            return False
    return True

def cartes_identiques(v_cartes: list):
    repetition_cartes = {}
    for valeur in v_cartes:
        if valeur not in repetition_cartes:
            repetition_cartes[valeur] = 0
        repetition_cartes[valeur] += 1
    return repetition_cartes


# test des combinaisons
def test_combinaison(valeurs: list, couleurs: list):
    if quinte_royale(valeurs) and flush(couleurs):
        print('Bravo ! C\'est une Quinte Flush Royale !')
        return 250
    if quinte(valeurs):
        if flush(couleurs):
            print('Bravo ! C\'est une Quinte Flush !')
            return 50
        print('Bravo ! C\'est une Quinte !')
        return 4
    if flush(couleurs):
        print('Bravo ! C\'est un Flush !')
        return 6
    
    repetition_cartes = cartes_identiques(valeurs)
    # tri par ordre decroissant le nombre de cartes identiques
    combo = sorted(repetition_cartes.values(), reverse=True)
    if combo[0] == 4:
        print('Bravo ! C\'est un Carré !')
        return 25
    if combo[0] == 3:    
        if combo[1] == 2:
            print('Bravo ! C\'est un Full !')
            return 9
        print('Bravo ! C\'est un Brelan !')
        return 3
    if combo[0] == 2:
        if combo[1] == 2:
            print('Bravo ! C\'est une Double Paire !')
            return 2
        print('Bravo ! C\'est une Paire. Vous conservez votre mise.')
        return 1
    
    print('Mise perdue...ce sera pour une prochaine fois !')
    return 0


def calculer_gains(mise: int, coeff_combinaison: int):
    gains = mise * coeff_combinaison
    resultat = f'Vous remportez {gains}€.'
    return gains, resultat


def partie(mise: int, bankroll: int):
    tirage_final = machine()
    v_cartes, c_cartes = decompose_jeu(tirage_final)
    coeff_combinaison = test_combinaison(v_cartes, c_cartes)
    gains, resultat = calculer_gains(mise, coeff_combinaison)
    bankroll = bankroll - mise + gains
    return resultat, bankroll