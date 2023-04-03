def final_series(game_results):
    team_a_wins = 0
    team_b_wins = 0
    
    for game in game_results:
        if game[0] > game[1]:
            team_a_wins += 1
        else:
            team_b_wins += 1
        
        if team_a_wins == 4:
            print(f"Team A won with a score of {team_a_wins}-{team_b_wins}")
        elif team_b_wins == 4:
            print(f"Team B won with a score of {team_b_wins}-{team_a_wins}")




