# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.



import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'à ce que l'usager appuie sur Enter.
    '''
    try:
        input("Appuyez Enter pour continuer. ")
    except SyntaxError:
        pass

def prepare_paquet():
    '''()->list of str
       Retourne une liste des chaînes de caractères qui représentent toutes les cartes,
       sauf le valet noir.
    '''
    paquet = []
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val + couleur)
    paquet.remove('J\u2663')  # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Mélange la liste des chaînes de caractères qui représentent le paquet des cartes.    
    '''
    random.shuffle(p)

def donne_cartes(p):
    '''(list of str)-> tuple of (list of str,list of str)
       Retourne deux listes qui représentent les deux mains des cartes.  
       Le donneur donne une carte à l'autre joueur, une à lui-même,
       et ça continue jusqu'à la fin du paquet p.
    '''
    donneur = []
    autre = []

    while len(p) > 0:
        # Donne une carte à l'autre joueur (Humain)
        autre.append(p.pop())
        if len(p) > 0:
            # Donne une carte au donneur (Robot)
            donneur.append(p.pop())

    return (donneur, autre)

     
def elimine_paires(p):
    
      '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
      p.sort()
      i = 0
      res = []
      while i < len(p) - 1:
        if p[i][0] == p[i + 1][0]:  # paire trouvée, sauter à la prochaine carte
            i += 2
        else:
            res.append(p[i])
            i += 1
      if i == len(p) - 1:  # ajouter la dernière carte si non appariée
        res.append(p[i])
      random.shuffle(res)  # mélanger la main sans paires
      return res



def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparés par des espaces.
    '''
    print(" ".join(p))

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n >= 1
     '''
     while True:
         try:
             choix = int(input(f"SVP entrez un entier de 1 à {n}: "))
             if 1 <= choix <= n:
                 return choix
             else:
                 print(f"Erreur: veuillez entrer un nombre entre 1 et {n}.")
         except ValueError:
             print("Erreur: veuillez entrer un entier valide.")

def joue():
    '''()->None
    Cette fonction joue le jeu.'''
    
    p = prepare_paquet()
    melange_paquet(p)
    tmp = donne_cartes(p)
    donneur = tmp[0]
    humain = tmp[1]

    print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
    print("Votre main de cartes est:")
    affiche_cartes(humain)
    print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
    print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    attend_le_joueur()
    
    donneur = elimine_paires(donneur)
    humain = elimine_paires(humain)
    
    # Boucle de jeu
    while donneur and humain:
        print("*"*80)
        print("Votre tour.")
        print("Votre main est:")
        affiche_cartes(humain)
        
        print(f"J'ai {len(donneur)} cartes. Si 1 est la position de ma première carte et {len(donneur)} la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
        position = entrez_position_valide(len(donneur))
        
        carte_prise = donneur[position - 1]
        print(f"Vous avez demandé ma {position}ème carte.\n La voilà. C'est un {carte_prise}.\n Avec {carte_prise} ajouté,votre main est:")
        humain.append(carte_prise)
        affiche_cartes(humain)
        
         
        
        print(f"Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
        humain=elimine_paires(humain)
        affiche_cartes(humain)
        attend_le_joueur()
        
        # Tour de Robot
        if humain:
          print("*"*80)
          print("Mon tour.")
          carte_robot = random.choice(humain)
          position=humain.index(carte_robot)+1
          print(f"J'ai pris votre {position}ème carte: {carte_robot}.")
          humain.remove(carte_robot)
          donneur.append(carte_robot)
          donneur = elimine_paires(donneur)
        else:
            print("Vous n'avez plus de cartes")
            
    attend_le_joueur()
    print("*"*80)
    #Le gagnant
    if humain==[]:
        print("J'ai terminé toutes les cartes.\nFélicitations! Vous, Humain, vous avez gagné."
)

    else :
        print("J'ai terminé toutes les cartes.\nVous avez perdu! Moi, Robot, j'ai gagné.")
        
# Programme principal
joue()
