players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

new_sql = []
for i_player, i_score in players.items():
    x = i_player[0], i_player[1], i_score[0], i_score[1], i_score[2]
    new_sql.append(x)

print(new_sql)
