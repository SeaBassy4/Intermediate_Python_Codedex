players = [
    {
        'name': 'Keylor_Navas',
        'position': 'goalkeeper',
        'age': 38,
        'height': 185,
        'weight': 174
    },
    {
        'name': 'Pablo_Bennevendo',
        'position': 'defense',
        'age': 25,
        'height': 175,
        'weight': 146
    },
    {
        'name': 'Rubén_Duarte',
        'position': 'defense',
        'age': 29,
        'height': 180,
        'weight': 163
    },
    {
        'name': 'Nathan_Silva',
        'position': 'defense',
        'age': 28,
        'height': 183,
        'weight': 183
    },
    {
        'name': 'Pablo_Alfonso_Monroy',
        'position': 'defense',
        'age': 23,
        'height': 170,
        'weight': 150
    },
    {
        'name': 'Jonathan_Flores',
        'position': 'defense',
        'age': 19,
        'height': 178,
        'weight': 155
    },
    {
        'name': 'Álvaro_Angulo',
        'position': 'defense',
        'age': 28,
        'height': 175,
        'weight': 159
    },
    {
        'name': 'Angel_Azuaje',
        'position': 'striker',
        'age': 20,
        'height': 182,
        'weight': 170
    },
    {
        'name': 'Dennis_Ramirez',
        'position': 'striker',
        'age': 18,
        'height': 178,
        'weight': 163
    },
    {
        'name': 'Emiliano_Villaseñor',
        'position': 'midfield',
        'age': 17,
        'height': 176,
        'weight': 148
    },
    {
        'name': 'Alejandro_Juárez',
        'position': 'midfield',
        'age': 16,
        'height': 157,
        'weight': 108
    },
    {
        'name': 'Alan_Medina',
        'position': 'midfield',
        'age': 27,
        'height': 170,
        'weight': 161
    }
]


print(players)

for player in players:
    if player['name'] == 'Alan_Medina':
        player['height'] = 172  
        break  

print(players)