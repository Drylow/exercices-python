mdp = input("Entrez le mot de passe : ")

if len(mdp) < 6:
    if len(mdp) == 0:
        print("Le mot de passe ne peut pas être vide.")
    else:
        print("Le mot de passe doit contenir au moins 6 caractères.")
elif mdp == "fsociety":
    print("Accès accordé, mot de passe correct.")
else:
    print("Accès refusé, mot de passe incorrect.")