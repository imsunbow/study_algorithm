player_lastname = []

for _ in range(int(input())):
    player = input()
    player_lastname.append(player[0])
    
set_player_lastname = set(player_lastname)

player_lastname_exceeds_five = []

for i in set_player_lastname:
    if player_lastname.count(i) >= 5:
        player_lastname_exceeds_five.append(i)
        
# player_lastname_exceeds_five.sort() #sort to print

if len(player_lastname_exceeds_five) > 0:
    print(''.join(sorted(player_lastname_exceeds_five)))
else:
    print("PREDAJA")
    