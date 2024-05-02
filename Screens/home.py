def home_screen(screen, Hbackground, GTITLE, font, WIDTH, HEIGHT, hovered_index, options):
    screen.blit(Hbackground, (0, 0))

    # Calculate y coordinate for the title
    title_y = HEIGHT / 10

    # Calculate x coordinate for the title
    title_x = WIDTH // 2

    # Render the title sprite
    title_rect = GTITLE.get_rect(midtop=(title_x, title_y))
    screen.blit(GTITLE, title_rect)

    # Render the version text
    version_text = "CE SOCCER"
    version_surface = font.render(version_text, True, (123, 3, 35)) 
    version_rect = version_surface.get_rect(topleft=(10, HEIGHT - 50))  # Bottom left corner with some padding
    screen.blit(version_surface, version_rect)

    # Render the info text
    info_text = "© 2024 | COSTA RICA"
    info_surface = font.render(info_text, True, (123, 3, 35)) 
    info_rect = info_surface.get_rect(topright=(WIDTH - 10, HEIGHT - 50))  # Bottom right corner with some padding
    screen.blit(info_surface, info_rect)

    # Calculate total available space between text
    total_height = HEIGHT * 2 / 3

    # Calculate gap between options
    gap = total_height / len(options)

    # Calculate initial y coordinate for options
    options_y = title_rect.bottom + gap / 2  # Adjust this value to control the vertical offset

    # Render options
    for i, option in enumerate(options):
        option_color = (127, 0, 255) if i == hovered_index else (0, 0, 128)
        text_surface = font.render(option, True, option_color)
        text_rect = text_surface.get_rect(midtop=(title_x, options_y + i * gap))
        screen.blit(text_surface, text_rect)
