best_player = ""
best_goals = 0
hat_trick = False

while True:
    player = input()
    if player == "END":
        break
    goals = int(input())
    
    if goals >= 3:
        hat_trick = True
    
    if goals > best_goals:
        best_player = player
        best_goals = goals
    
    if best_goals >= 10:
        break

print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {best_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_goals} goals.")
