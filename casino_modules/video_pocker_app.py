from module_questionbooleenne import *
from module_gain import partie

bankroll = int(input("Veuillez insérer de l'argent, svp : "))
mise = int(input("Faites vos jeux : "))

def mise_possible(bankroll: int, mise: int):
    while not(bankroll >= mise > 0):
        mise = int(input("La mise doit être inférieure ou égale à votre cagnotte, merci de modifier votre mise : "))
    return mise

mise = mise_possible(bankroll, mise)
print(mise)

while bankroll - mise >= 0:
    resultat, bankroll = partie(mise, bankroll)
    print(resultat)
    print(f'Il reste {bankroll}€ dans votre cagnotte')
    if bankroll == 0:
        print('C\'est perdu...')
        break
    else:
        if reponse_booleenne('Voulez-vous continuer à jouer ?'):
            mise = int(input("Faites vos jeux : "))
            mise = mise_possible(bankroll, mise)
        else:
            print(f'Vous récuperez {bankroll}€, bien joué !')
            break