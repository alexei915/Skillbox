import random

fst_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
sec_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [fst_team[i] if fst_team[i] > sec_team[i] else sec_team[i] for i in range(20)]

print(f'Первая команда: {fst_team}')
print(f'Вторая команда: {sec_team}')
print(f'Победители тура: {winners}')
