from actions import *
from composants import Partie


def lancement_partie():
	print("Bienvenue !\nVous venez de lancez une partie de Splendor !")
	nj = init_nb_joueur()
	game = Partie(nj)
	game.joueurs.extend(init_joueurs(nj))
	game.jetons.update(init_jetons(nj))
	afficher_jeu(game)

	# test
	game.joueurs[0].jetons["rouge"] += 2
	game.joueurs[0].jetons["vert"] += 2
	game.joueurs[0].jetons["bleu"] += 2
	game.joueurs[0].jetons["noir"] += 2
	game.joueurs[0].jetons["blanc"] += 2
	game.joueurs[0].jetons["jaune"] += 2
	choisir_carte(game, 0)
	afficher_jeu(game)

	test = input("ok?")
	print(test)

	# for joueur in range(game.joueurs):
	# 	while not choix:
	# 		choix = int(input(f"""{joueur.name} doit choisir une action parmi les suivantes :\n
	# 		- (1) piocher 2 jetons
	# 		- (2) piocher 3 jetons
	# 		- (3) choisir une carte
	# 		- (4) reserver une carte
    #       - (5) jouer une carte réservée
	# 		- (6) afficher sa main
	# 		- (7) afficher le jeu"""))
	#
	# 		if choix == 1:
	# 			choix = pioche2jetons(joueur)
	# 		elif choix == 2:
	# 			choix = pioche3jetons(joueur)
	# 		elif choix == 3:
	# 			choix = acheter_carte(joueur)
	# 		elif choix == 4:
	# 			choix = reserver_carte(joueur)
	# 		elif choix == 5:
	# 			choix = afficher_main(joueur)
	# 		elif choix == 6:
	# 			choix = afficher_jeu
	# 		else:
	# 			print(f"Le choix de {joueur.name} n'est pas valide.")

	# 		joueur i choisi une action parmi :
	#           - pioche2jetons()
	#           - pioche3jetons()
	#           - choisir_carte()
	#           - reserver_carte()
	#           - afficher_main()
	#           si il choisit afficher_main, reproposer les actions
	#       après le choix d'action, contrôle :
	#           - du nombre de jetons : si > 10, le joueur doit en défausser
	#           - de l'acquisition d'un noble si mérité
	#           - du nombre de points : si >= 15, enclenche le dernier tour


lancement_partie()
