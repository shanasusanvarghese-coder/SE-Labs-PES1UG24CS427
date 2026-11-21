import pygame
from game.deck import Deck

BG = (28, 39, 55)
WHITE = (245, 245, 245)
GREEN = (50, 180, 110)
RED = (220, 75, 75)
GOLD = (245, 190, 65)

class GameEngine:
    REVEAL_MS = 900

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.deck = Deck()
        self.current_card = self.deck.draw()
        self.previous_card = None
        self.score = 0
        self.streak = 0
        self.message = "Will the next card be HIGHER or LOWER?"
        self.message_color = WHITE
        self.reveal_timer = 0
        self.font = pygame.font.SysFont("arial", 30, bold=True)
        self.card_font = pygame.font.SysFont("arial", 34, bold=True)
        self.small_font = pygame.font.SysFont("arial", 16)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN or self.reveal_timer > 0:
            return
        if event.key in (pygame.K_h, pygame.K_UP):
            self.guess("higher")
        elif event.key in (pygame.K_l, pygame.K_DOWN):
            self.guess("lower")

    def guess(self, choice):
        next_card = self.deck.draw()
        self.previous_card = self.current_card
        self.current_card = next_card

        if next_card.numeric_rank == self.previous_card.numeric_rank:
            self.message = f"PUSH! Both cards were {next_card.rank_str}. Score and streak unchanged."
            self.message_color = GOLD
        else:
            is_higher = next_card.numeric_rank > self.previous_card.numeric_rank
            correct = (choice == "higher" and is_higher) or (choice == "lower" and not is_higher)
            if correct:
                self.streak += 1
                points = self.streak
                self.score += points
                self.message = f"CORRECT! +{points} point(s)  |  Streak: {self.streak}"
                self.message_color = GREEN
            else:
                self.streak = 0
                self.score = max(0, self.score - 1)
                self.message = "WRONG! Streak reset. -1 point."
                self.message_color = RED

        self.reveal_timer = self.REVEAL_MS

    def update(self, dt):
        if self.reveal_timer > 0:
            self.reveal_timer = max(0, self.reveal_timer - dt)

    def draw(self, screen):
        screen.fill(BG)
        title = self.font.render("HIGH-LOW CARD PREDICTOR", True, WHITE)
        screen.blit(title, title.get_rect(center=(self.width // 2, 38)))

        score_text = self.font.render(f"Score: {self.score}     Win streak: {self.streak}", True, GOLD)
        screen.blit(score_text, score_text.get_rect(center=(self.width // 2, 88)))

        label_font = pygame.font.SysFont("arial", 20, bold=True)
        if self.previous_card is not None and self.reveal_timer > 0:
            left_x, right_x = self.width // 2 - 190, self.width // 2 + 30
            left_label = label_font.render("PREVIOUS CARD", True, WHITE)
            right_label = label_font.render("NEW CARD", True, WHITE)
            screen.blit(left_label, left_label.get_rect(center=(left_x + 80, 145)))
            screen.blit(right_label, right_label.get_rect(center=(right_x + 80, 145)))
            self.previous_card.draw(screen, pygame.Rect(left_x, 165, 160, 220), self.card_font, self.small_font)
            self.current_card.draw(screen, pygame.Rect(right_x, 165, 160, 220), self.card_font, self.small_font)
        else:
            current_label = label_font.render("CURRENT CARD", True, WHITE)
            screen.blit(current_label, current_label.get_rect(center=(self.width // 2, 145)))
            self.current_card.draw(screen, pygame.Rect(self.width // 2 - 80, 165, 160, 220), self.card_font, self.small_font)

        msg = self.font.render(self.message, True, self.message_color)
        screen.blit(msg, msg.get_rect(center=(self.width // 2, 415)))

        controls = self.small_font.render("Press H / UP for HIGHER     |     Press L / DOWN for LOWER", True, WHITE)
        screen.blit(controls, controls.get_rect(center=(self.width // 2, 465)))
        remaining = self.small_font.render(f"Cards remaining: {self.deck.remaining}", True, WHITE)
        screen.blit(remaining, (12, 12))
