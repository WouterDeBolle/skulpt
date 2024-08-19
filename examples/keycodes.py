import pygame

# schermgrootte
breedte = 800
hoogte = 600
veld_grootte = 20
kleur_tekst = (0, 255, 0)
kleur_achtergrond = (0, 0, 0)

# Initialiseren van de pygame-module
pygame.init()

# Creëer een venster met opgegeven breedte en hoogte
venster = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Test keys')


# Start de hoofdloop van het spel
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            venster.fill(kleur_achtergrond)
            font = pygame.font.Font(None, 36)
            tekst = font.render("You pressed key with code " + str(event.key), True, kleur_tekst)
            venster.blit(tekst, (breedte // 2 - tekst.get_width() // 2, hoogte // 2))
            pygame.display.update()

    pygame.display.update()

pygame.quit()
