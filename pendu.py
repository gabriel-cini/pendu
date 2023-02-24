import pygame
import random



pygame.init()

width , height = 800,600

screen = pygame.display.set_mode(( width, height))
titre = pygame.display.set_caption( "Le jeu du Pendu")

pendu_image = []

for i in range(7):

    img = pygame.image.load("hangman"+str(i)+".png")
    pendu_image.append(img)

White = (255,255,255)
BLACK = (0,0,0)

lettre_fonts = pygame.font.SysFont("arial",34)
mot_fonts = pygame.font.SysFont("monospace",24)

in_game = False


                
    
with open("mots.txt", "r") as f:
    mots = f.read().splitlines()
    game_one = True

while game_one:
    mot_choisit = random.choice(mots).lower()
    lettre_trouver = []
    erreurs = 0

    affiche_mot = ""
    for lettre in mot_choisit:
        affiche_mot += "-"

    fin_de_jeu = False
    while not fin_de_jeu:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                game_one = False
                fin_de_jeu = True
            if events.type == pygame.KEYDOWN:
                insert = pygame.key.name(events.key)
                if insert in mot_choisit:
                    lettre_trouver.append(insert)
                    affiche_mot = ""
                    for lettre in mot_choisit:
                        if lettre in lettre_trouver:
                            affiche_mot += lettre
                        else:
                            affiche_mot += "-"
                                
                else:
                    erreurs +=1
            screen.fill(White)
            mot_surf = mot_fonts.render(affiche_mot,1,BLACK)
            mot_rect = mot_surf.get_rect()
            mot_rect.center = (width/2,450)
            screen.blit(mot_surf,mot_rect)
                            
            image_rect = pendu_image[erreurs].get_rect()
            image_rect.center = (width/2,300)
            screen.blit(pendu_image[erreurs], image_rect)
                    
            pygame.display.update()
            if erreurs ==6:
                fin_de_jeu = True
            elif affiche_mot == mot_choisit:
                fin_de_jeu = True
pygame.quit()




