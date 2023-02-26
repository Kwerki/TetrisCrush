import pygame
import csv

class Score():
    def __init__(self):
        self.font = pygame.font.SysFont('arial', 16)
        self.score_text = self.font.render('Score', False, (154,50,205))
        self.highscore_text = self.font.render('Highscore', False, (154,50,205))
        self.score = 0

    def set_score(self, score):
        self.score = self.score + score

    def save_score(self):
        with open('scores.csv', 'r') as file:
            reader = csv.reader(file)
            scores = [int(row[0]) for row in reader]
        scores.append(self.score)
        scores = sorted(scores, reverse=True)
        scores = scores[:5]
        with open('scores.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for s in scores:
                writer.writerow([s])

    def draw_score(self, screen):
        score = self.font.render(str(self.score),False,(154,50,205)) #Zeichnen des Scores
        screen.blit(self.score_text,(410,30))
        screen.blit(score,(430,60))
        screen.blit(self.highscore_text,(410,100))
        high_scores = self.read_scores()
        for i, high_score in enumerate(high_scores):
            high_score_text = self.font.render(str(high_score),False,(154,50,205))
            screen.blit(high_score_text, (430, 130 + (i*20)))

    def read_scores(self):
        scores = []
        with open('scores.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                scores.append(int(row[0]))
        return scores