import pygame

def start_screen(screen, Hfont, WIDTH, HEIGHT):
    # Fill the screen with a solid color (e.g., black)
    screen.fill((0, 0, 0))

    # Render a text message at the center of the screen
    text = Hfont.render("GAME START!", True, (255, 255, 255))  # White text
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Center of the screen
    screen.blit(text, text_rect)
