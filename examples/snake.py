import pygame
import random
import time
from datetime import datetime


# kleuren
kleur_accent = (0, 200, 0)
kleur_slang = (0, 255, 0)
kleur_achtergrond = (0, 0, 0)
kleur_tekst = (0, 255, 0)
kleur_game_over = (255, 0, 0)
kleur_voedsel = (255, 0, 0)

# schermgrootte
breedte = 800
hoogte = 600
veld_grootte = 20

# Snelheid van het spel
spel_snelheid = 5


class Food:
    def __init__(self, breedte, hoogte):
        self.breedte = breedte
        self.hoogte = hoogte
        self.plaats_voedsel()

    def plaats_voedsel(self):
        self.x = round(random.randrange(0, self.breedte - veld_grootte) / veld_grootte) * veld_grootte
        self.y = round(random.randrange(0, self.hoogte - veld_grootte) / veld_grootte) * veld_grootte

    def teken(self, venster):
        pygame.draw.rect(venster, kleur_voedsel, pygame.Rect(self.x, self.y, veld_grootte, veld_grootte))


class Snake:
    def __init__(self, startx, starty):
        self.x = startx
        self.y = starty
        self.lijst_slang = [[startx, starty]]
        self.lengte_slang = 1
        self.x_verandering = 0
        self.y_verandering = 0

    def beweeg(self):
        self.x += self.x_verandering
        self.y += self.y_verandering
        slang_kop = [self.x, self.y]
        self.lijst_slang.append(slang_kop)
        # Verwijder de staart als dat nodig is:
        if len(self.lijst_slang) > self.lengte_slang:
            del self.lijst_slang[0]

    def teken(self, venster):
        for segment in self.lijst_slang:
            pygame.draw.rect(venster, kleur_slang, pygame.Rect(segment[0], segment[1], veld_grootte, veld_grootte))
            pygame.draw.rect(venster, kleur_accent, pygame.Rect(segment[0] + 4, segment[1] + 4, veld_grootte - 8, veld_grootte - 8))

    def is_buiten_veld(self, breedte, hoogte):
        return self.x >= breedte or self.x < 0 or self.y >= hoogte or self.y < 0

    def raakt_zichzelf(self):
        game_over = False
        for segment in self.lijst_slang[:-1]:  # alle segmenten zonder de kop
            if segment == [self.x, self.y]:    # één van de segmenten is gelijk aan de kop
                game_over = True
        return game_over


# Initialiseren van de pygame-module
pygame.init()

# Creëer een venster met opgegeven breedte en hoogte
venster = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Snake')


# Functie om de score op het scherm te tonen
def toon_score(score, venster):
    font = pygame.font.Font(None, 36)
    scoretekst = font.render(f"Score: {score}", True, kleur_tekst)
    venster.blit(scoretekst, (10, 10))


def toon_tijd(tijd, venster):
    font = pygame.font.Font(None, 30)
    tekst = font.render(f"Speeltijd: {tijd} seconden", True, kleur_tekst)
    venster.blit(tekst, (10, hoogte - 30))  # in de linkeronderhoek


# def sla_op_in_csv(score, tijdstip):
#     with open('highscores.csv', mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([score, tijdstip])


# def haal_hoogste_score_op():
#     try:
#         with open('highscores.csv', mode='r') as file:
#             reader = csv.reader(file)
#             highscores = list(reader)
#             highest_score = max(int(row[0]) for row in highscores)
#             return highest_score
#     except FileNotFoundError:
#         return 0


def game_over_scherm(score, speeltijd):
    font = pygame.font.Font(None, 50)
    hoofdtekst = font.render(f"Game Over! Score: {score}", True, kleur_game_over)

    kleiner_font = pygame.font.Font(None, 30)
    speeltijd_tekst = kleiner_font.render(f"Speeltijd: {speeltijd} seconden", True, kleur_game_over)
    instructie = kleiner_font.render("Druk op Enter om opnieuw te spelen of Esc om af te sluiten", True,
                                     kleur_game_over)
    venster.blit(hoofdtekst,
                 (breedte // 2 - hoofdtekst.get_width() // 2, hoogte // 2 - hoofdtekst.get_height() // 2))
    venster.blit(speeltijd_tekst,
                 (breedte // 2 - speeltijd_tekst.get_width() // 2, hoogte // 2 + hoofdtekst.get_height()))
    venster.blit(instructie,
                 (breedte // 2 - instructie.get_width() // 2, hoogte // 2 + hoofdtekst.get_height() + 30))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    venster.fill(kleur_achtergrond)  # Vul het scherm met een zwarte achtergrond
                    game_lus()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()


def animatie():
    klok = pygame.time.Clock()
    s = [[180, 120], [180, 100], [160, 100], [140, 100], [120, 100], [100, 100], [100, 120], [100, 140],
         [100, 160], [120, 160], [140, 160], [160, 160], [180, 160], [180, 180], [180, 200], [180, 220],
         [160, 220], [140, 220], [120, 220], [100, 220], [100, 200]]
    apple = [100, 200]

    pygame.draw.rect(venster, kleur_voedsel, pygame.Rect(tuple(apple), (veld_grootte, veld_grootte)))
    pygame.display.flip()
    klok.tick(8)

    for positie in s:
        pygame.draw.rect(venster, kleur_tekst, pygame.Rect(tuple(positie), (veld_grootte, veld_grootte)))
        pygame.display.flip()
        klok.tick(8)

    font = pygame.font.SysFont("console", 64, True)
    text_surface = font.render("NAKE", True, kleur_voedsel)
    venster.blit(text_surface, (220, 180))

    pygame.display.flip()
    time.sleep(2)


# Start de hoofdloop van het spel
def game_lus():
    food = Food(breedte, hoogte)
    snake = Snake(breedte // 2, hoogte // 2)
    score = 0
    game_over = False
    animatie()
    start_tijd = pygame.time.get_ticks()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and snake.x_verandering == 0:
                    snake.x_verandering = -veld_grootte
                    snake.y_verandering = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and snake.x_verandering == 0:
                    snake.x_verandering = veld_grootte
                    snake.y_verandering = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and snake.y_verandering == 0:
                    snake.y_verandering = -veld_grootte
                    snake.x_verandering = 0
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and snake.y_verandering == 0:
                    snake.y_verandering = veld_grootte
                    snake.x_verandering = 0
                elif event.key == pygame.K_p:
                    gepauzeerd = True
                    pauze_font = pygame.font.Font(None, 36)
                    pauze_tekst = pauze_font.render("Pauze (Druk op P om door te gaan)", True, kleur_tekst)
                    venster.blit(pauze_tekst, (breedte // 2 - pauze_tekst.get_width() // 2, hoogte // 2))
                    pygame.display.update()
                    while gepauzeerd:
                        for pauze_event in pygame.event.get():
                            if pauze_event.type == pygame.KEYDOWN and pauze_event.key == pygame.K_p:
                                gepauzeerd = False

        snake.beweeg()
        if snake.is_buiten_veld(breedte, hoogte) or snake.raakt_zichzelf():
            game_over = True

        venster.fill(kleur_achtergrond)  # Vul het scherm met een zwarte achtergrond
        food.teken(venster)
        snake.teken(venster)
        toon_score(score, venster)
        huidige_tijd = pygame.time.get_ticks()
        verstreken_tijd = (huidige_tijd - start_tijd) / 1000
        toon_tijd(verstreken_tijd, venster)

        if snake.x == food.x and snake.y == food.y:
            food.plaats_voedsel()
            snake.lengte_slang += 1
            score += 10

        pygame.display.update()
        time.sleep(1 / spel_snelheid)

    print(f"Jouw score is {score}")
    # sla_op_in_csv(score, datetime.now())
    # hoogste_score = haal_hoogste_score_op()
    # print(f"De highscore is {hoogste_score}")
    game_over_scherm(score, verstreken_tijd)


# Start de hoofdloop van het spel
game_lus()
