team_a = set(range(1, 12))
team_b = set(range(1, 12))
game_was_terminated = False

sequence_of_cards = input().split()

for card in sequence_of_cards:
    if '-' in card:
        team, player_number = card.split('-')
        player_number = int(player_number)

        if team == 'A':
            team_a.discard(player_number)
        elif team == 'B':
            team_b.discard(player_number)

        if len(team_a) < 7 or len(team_b) < 7:
            game_was_terminated = True
            break

remaining_player_team_a = len(team_a)
remaining_player_team_b = len(team_b)

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if game_was_terminated:
    print("Game was terminated")