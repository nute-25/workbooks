def reponse_booleenne(question: str):
    while True:
        reponse = input(question + ' Oui ou Non.\n').lower()
        if reponse == 'non' or reponse == 'n':
            return False
        if reponse == 'oui' or reponse == 'o':
            return True