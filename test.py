# Combined list
combined_list = [['SCORE', 'Stalin'], ['SCORE', 'Andrew Tate'], ['SCORE', 'Agüero Melo'], ['SCORE', 'Stalin'], ['SCORE', 'Andrew Tate']]

team_sprites = {
    "Campeon": ["team1", ["team1p1", "El Pete Hernández"], ["team1p2", "Mr Worldwide"], ["team1p3", "Fecundo Ovario"]],
    "Morao": ["team2", ["team2p1", "Rufino Pepino"], ["team2p2", "Mr Clean"], ["team2p3", "DJ Mario"]],
    "LSD": ["team3", ["team3p1", "Stalin"], ["team3p2", "Andrew Tate"], ["team3p3", "Agüero Melo"]]
}

def identify_team(player_name, team_sprites):
    for team, player_list in team_sprites.items():
        for player_entry in player_list[1:]:
            if player_name in player_entry:
                return team
    return None  # Return None if player not found in any team

def analyze_scores(combined_list):
    # Initialize dictionaries to store scores per player
    scores_per_player = {}
    
    # Counters for total scores and fails
    total_score = 0
    total_fail = 0

    # Iterate through the combined list
    for score, player in combined_list:
        # Count scores per player
        if score == 'SCORE':
            scores_per_player[player] = scores_per_player.get(player, 0) + 1
            total_score += 1
        # Count fails per player
        else:
            total_fail += 1

    # Create a list of sublists containing player and score count with team names
    player_scores_list = []
    for player, score_count in scores_per_player.items():
        team = identify_team(player, team_sprites)
        player_scores_list.append([player, score_count])

    # Create a list for total scores and fails with team names
    team = identify_team(player, team_sprites)
    total_scores_and_fails = [[team,'Total score', total_score], [team,'Total fail', total_fail]]


    # Return the list of player scores and total scores and fails with team names
    return player_scores_list, total_scores_and_fails

# Call the function and save the result
player_scores, total_scores_and_fails = analyze_scores(combined_list)
print()
import os

def update_top_scores(scores_list, file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Read existing scores from the file
        with open(file_path, 'r') as file:
            scores = [line.strip().split(", ") for line in file.readlines()]
    else:
        scores = []

    # Dictionary to store scores by name
    scores_dict = {score[0]: int(score[1]) for score in scores}

    # Update scores or add new scores
    for score in scores_list:
        name = score[0]
        value = score[1]
        if name in scores_dict:
            scores_dict[name] += value  # If name already exists, sum the new score to the existing one
        else:
            scores_dict[name] = value   # If name doesn't exist, add it to the dictionary

    # Write the updated scores back to the file
    with open(file_path, 'w') as file:
        for name, score in scores_dict.items():
            file.write(name + ', ' + str(score) + '\n')

update_top_scores([['Rufino Pepino', 2], ['Mr Clean', 2], ['DJ Mario', 1]], "Top_shooters.txt")

