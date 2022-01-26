players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new_sql = []
for player, score in players.items():
    players_points = player[0], player[1], score[0], score[1], score[2]
    new_sql.append(players_points)

print(new_sql)
