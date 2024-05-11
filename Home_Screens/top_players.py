import pygame
from var_consts import *
import os

def top_scores_screen(screen, Hfont, Mbackground, Hbackground, selected_index):
    # Background gray coat  
    overlay = pygame.Surface((HWIDTH, HHEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_GRAY)
    screen.blit(Hbackground, (0,0))
    screen.blit(overlay, (0,0))

    # Insert menu pop-up
    top_scores_BG_rect = Mbackground.get_rect(center=(HWIDTH//2, HHEIGHT//2))
    screen.blit(Mbackground, top_scores_BG_rect)

    # Display title text
    title_text = "TOP SCORES"
    title_surface = Hfont.render(title_text, True, NAVY_BLUE)  
    title_text_rect = title_surface.get_rect(midtop=(HWIDTH/2, HHEIGHT/4))
    title_text_rect.y -= title_surface.get_height() 
    screen.blit(title_surface, title_text_rect)

    if Top_players[selected_index] == 1:
        # Load and display top scores
        file_path = "Top_shooters.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                # Read lines from the file and parse player names and scores
                scores = [line.strip().split(", ") for line in file]

            # Ensure only the top 3 scores are displayed
            scores = scores[:3]

            # If there are fewer than 3 scores, pad with empty slots
            while len(scores) < 3:
                scores.append(["-EMPTY-", "-"])

            # Calculate available vertical space for scores considering the background
            available_height = top_scores_BG_rect.bottom - (title_text_rect.bottom + 20)  # 20 for additional spacing
            num_scores = len(scores)

            if num_scores > 1:
                # Subtract the height occupied by the scores from the available height
                vertical_spacing = (available_height - (num_scores - 1) * 30) / num_scores  # Adjust vertical spacing
            else:
                vertical_spacing = 0

            for i, (player, score) in enumerate(scores):
                score_text = f"{i+1}. {player}: {score}"
                # Adjust vertical position by considering the space already occupied by the background
                score_text_rect = Hfont.render(score_text, True, WHITE).get_rect(midtop=(HWIDTH/2, title_text_rect.bottom + 20 + i * (30 + vertical_spacing)))
                screen.blit(Hfont.render(score_text, True, WHITE), score_text_rect)

        else:
            # If the file doesn't exist, or if there are no scores yet, display empty slots
            empty_text = "-EMPTY-"
            for i in range(3):
                empty_text_rect = Hfont.render(empty_text, True, WHITE).get_rect(midtop=(HWIDTH/2, title_text_rect.bottom + 20 + i * 30))
                screen.blit(Hfont.render(empty_text, True, WHITE), empty_text_rect)
    elif Top_players[selected_index] == 2:
        # Display team stats
        team_stats_file_path = "team_stats.txt"
        if os.path.exists(team_stats_file_path):
            with open(team_stats_file_path, 'r') as team_stats_file:
                # Read lines from the team stats file
                team_stats_lines = team_stats_file.readlines()

            # Calculate available vertical space for team stats considering the background
            available_height_team_stats = top_scores_BG_rect.bottom - (title_text_rect.bottom + 20)  # 20 for additional spacing
            num_team_stats = len(team_stats_lines)

            if num_team_stats > 0:
                # Subtract the height occupied by the team stats from the available height
                vertical_spacing_team_stats = (available_height_team_stats - (num_team_stats - 1) * 30) / num_team_stats  # Adjust vertical spacing

                for j, team_stat_line in enumerate(team_stats_lines):
                    team_stat_text = team_stat_line.strip()  # Remove leading/trailing whitespace
                    team_stat_text_rect = Hfont.render(team_stat_text, True, WHITE).get_rect(midtop=(HWIDTH/2, title_text_rect.bottom + 20 + j * (30 + vertical_spacing_team_stats)))
                    screen.blit(Hfont.render(team_stat_text, True, WHITE), team_stat_text_rect)
