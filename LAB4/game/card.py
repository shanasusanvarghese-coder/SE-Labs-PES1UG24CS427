import pygame

SUITS = {
    "hearts": "♥",
    "diamonds": "♦",
    "clubs": "♣",
    "spades": "♠",
}

RANK_LABELS = {
    11: "J", 12: "Q", 13: "K", 14: "A"
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.numeric_rank = rank
        self.rank_str = RANK_LABELS.get(rank, str(rank))

    def draw(self, surface, rect, font, small_font):
        pygame.draw.rect(surface, (250, 250, 245), rect, border_radius=12)
        pygame.draw.rect(surface, (35, 35, 45), rect, 2, border_radius=12)
        color = (190, 35, 45) if self.suit in ("hearts", "diamonds") else (30, 30, 35)
        symbol = SUITS[self.suit]
        label = font.render(self.rank_str, True, color)
        suit = font.render(symbol, True, color)
        surface.blit(label, (rect.x + 14, rect.y + 12))
        surface.blit(suit, (rect.x + 14, rect.y + 58))
        center_rank = font.render(self.rank_str, True, color)
        center_suit = font.render(symbol, True, color)
        surface.blit(center_rank, center_rank.get_rect(center=(rect.centerx, rect.centery - 20)))
        surface.blit(center_suit, center_suit.get_rect(center=(rect.centerx, rect.centery + 25)))
        footer = small_font.render(self.suit.title(), True, color)
        surface.blit(footer, footer.get_rect(center=(rect.centerx, rect.bottom - 18)))
