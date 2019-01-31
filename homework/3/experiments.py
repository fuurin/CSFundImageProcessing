###############################################################################################################################
##### I recomend not to execute this script, but install jupyter notebook by pip and browse the ipynb file of the report. #####
###############################################################################################################################

from lesson3Code.pokemonTournament.pokemonDef import Monster,superEffective,notEffective,noEffect
import lesson3Code.pokemonTournament.pokemonFunctions as pf

listOfNamesAndTypes=pf.readPokemonTypesFromFile("lesson3Code/pokemonTournament/listOfPokemon1.txt")
pokeList=pf.readPokemonListFromFile("lesson3Code/pokemonTournament/listOfPokemon2.txt")

pokedex={}
for monster in pokeList:
    pokedex[monster.name]=monster

for name,listOfTypes in listOfNamesAndTypes:
    for t in listOfTypes:
        pokedex[name].variety.append(t)



import numpy as np
from copy import copy

def copyMonster(p):
    return Monster(*[copy(f) for f in p])

pid = np.random.randint(0, len(pokeList))
p1 = copyMonster(pokeList[pid])
p2 = copyMonster(p1)
print(p1)
print(p2)

p1.hitpoint[1] = 0

print(p1)
print(p2)
print(pokeList[pid])



def SingleRoundRobinExperiment(p, enemy_list=pokeList, k=1, battle=pf.battle, skip_same=False, verbose=False):
    results = np.zeros(len(enemy_list), dtype=[('w','i'), ('l', 'i'), ('d', 'i')]) # win, loss, draw
    for idx, enemy in enumerate(enemy_list):
        if skip_same and p.name == enemy.name: continue
        for i in range(k):
            result = battle(copyMonster(p), copyMonster(enemy))
            if result == 0: results[idx]['w'] += 1
            elif result == 1: results[idx]['l'] += 1
            else: results[idx]['d'] += 1
    return results



def RoundRobinExperiment(k=1, battle=pf.battle, verbose=False):
    get_result = lambda p: SingleRoundRobinExperiment(p, k=k, battle=battle, verbose=verbose)
    results = np.array([get_result(p) for p in pokeList]) # battles results win-loss-draw, the indices represents pokemon indices

    if verbose:
        ranking = results['w'].sum(axis=0).argsort()
        strongest = pokeList[ranking[0]]
        print("The strongest pokemon is", strongest.name, "id:", strongest.index)
        print("The strongest pokemon parameter", strongest)
        print("Strongest Pokemon Top 10")
        for i in ranking[:10]:
            print(pokeList[i])
    
    return results



import pickle
k = 100

try:
    # raise Exception # For creating new pickle data
    with open('data/normal_result.pkl', 'rb') as f:
        normal_result = pickle.load(f)
        print('normal result is loaded from the pickle file')
except:
    normal_result = RoundRobinExperiment(k, verbose=True)
    with open('data/normal_result.pkl', mode='wb') as f:
        pickle.dump(normal_result, f)
finally:
    normal_ranking = [pokeList[p] for p in normal_result['w'].sum(axis=0).argsort()]



print(normal_ranking[0])



def SpeedBattle(p1, p2, resetHP=True, verbose=False):
    
    max_rounds = 100
    effectiveness = 0.3
    expected_defense_rate = 0.75 # Setting this the lowest, accuracy increased
    
    if resetHP:
        pf.ResetHP(p1)
        pf.ResetHP(p2)
    
    if noEffect(p1, p2) and noEffect(p2, p1): return 2
    
    attackCenter1=1
    if superEffective(p1, p2): attackCenter1+=effectiveness
    if notEffective(p1, p2): attackCenter1-=effectiveness
    if noEffect(p1, p2): attackCenter1 = 0


    attackCenter2=1
    if superEffective(p2, p1): attackCenter2+=effectiveness
    if notEffective(p2, p1): attackCenter2-=effectiveness
    if noEffect(p2, p1): attackCenter2 = 0

    
    get_damage1 = max(0, (round(p2.attack * attackCenter2) - round(p1.defense * expected_defense_rate)))
    survive_rounds1 = min(max_rounds, (float(p1.hitpoint[1]) / get_damage1)) if get_damage1 > 0 else max_rounds
    get_damage2 = max(0, (round(p1.attack * attackCenter1) - round(p2.defense * expected_defense_rate)))
    survive_rounds2 = min(max_rounds, (float(p2.hitpoint[1]) / get_damage2)) if get_damage2 > 0 else max_rounds
        
    if survive_rounds1 == survive_rounds2: 
        if survive_rounds1 >= max_rounds: return 2
        if p1.speed == p2.speed: return 2
        return 0 if p1.speed > p2.speed else 1
    
    return 0 if survive_rounds1 > survive_rounds2 else 1



# The result is deterministic. So it is enough for k to be 1.
speed_result = RoundRobinExperiment(battle=SpeedBattle, verbose=True)
speed_ranking = [pokeList[p] for p in speed_result['w'].sum(axis=0).argsort()]



import time

startNormal = time.time()
RoundRobinExperiment() # 8 sec when max round was 1000
endNormal = time.time()
print("Normal Battle Elapsed Time:", endNormal - startNormal)

startSpeed = time.time()
RoundRobinExperiment(battle=SpeedBattle)
endSpeed = time.time()
print("Speed Battle Elapsed Time:", endSpeed - startSpeed)



normal_ranking_id = np.array([p.index for p in normal_ranking]) 
speed_ranking_id = np.array([p.index for p in speed_ranking])
same_places = normal_ranking_id == speed_ranking_id
print(f"same places: {sum(same_places)} / {len(same_places)}")



import math

def std_rank_error(ranking, offset=0, verbose=False):
    normal_ranking_list = list(normal_ranking)
    ranking_error = []
    for rank, p in enumerate(ranking):
        diff = (normal_ranking_list.index(p) - rank - offset)
        if verbose: print(rank, normal_ranking_list.index(p), p.name, diff)
        ranking_error.append(diff ** 2)

    return math.sqrt(sum(ranking_error) / len(ranking_error))

print("Standard Rank Error:", std_rank_error(speed_ranking))



import matplotlib.pyplot as plt

speed_ranking_id = [p.index for p in speed_ranking]
intervals = np.array_split(speed_ranking_id, 15)
y = [std_rank_error([pokeList[p] for p in interval], offset=speed_ranking_id.index(interval[0])) for interval in intervals]
x = [f"{speed_ranking_id.index(interval[0])}~{speed_ranking_id.index(interval[-1])}" for interval in intervals]
plt.bar(x,y)
plt.title("Standard Rank Error(SRE) Increases in Mid Rank Pokemon Area")
plt.xlabel("Rank Intervals")
plt.xticks(x, rotation=45)
plt.ylabel("SRE")
# plt.show()
print("SREs")
print([round(y_i, 2) for y_i in y])



strongest = normal_ranking[0]
print(strongest)



print("Pokemon Defense Ranking")
defense_ranking = np.argsort([p.defense for p in pokeList])[::-1]
for p in defense_ranking[:10]:
    print(pokeList[p])



print("Pokemon Attack Ranking")
attack_ranking = np.argsort([p.attack for p in pokeList])[::-1]
for p in attack_ranking[:10]:
    print(pokeList[p])



round(180 * 0.7) # defense is multiplied 0.7 in worst case in pf.battle.



effective_varieties = ['Grass', 'Electric', 'Fighting', 'Rock', 'Steel']
effective_pokeList = [p for p in pokeList if np.any([v in p.variety for v in effective_varieties]) or p.attack > 126]
winnable_pokeList = [p for p in effective_pokeList if p.attack * 1.3 * 1.2 > 180 * 0.7]
print("\n# of Pokemons who can give a damage to Cloyster:", len(winnable_pokeList), "/", len(pokeList))

for p in winnable_pokeList:
    print(p)



k = 100
cloyster = pokedex["Cloyster"]
challengers = winnable_pokeList

win_times = np.zeros(len(challengers), dtype='i')
for i, challenger in enumerate(challengers):
    for _ in range(k):
        if pf.battle(challenger, cloyster) == 0: 
            win_times[i] += 1
            
ranking = win_times.argsort()[::-1]
for idx in ranking:
    print(f"Challenger {challengers[idx].name} Win Rate: {win_times[idx]}/{k}")



def natural_enemies(p, enemy_list=pokeList, k=10, ranking=normal_ranking, battle=pf.battle, top=6, verbose=False):
    results = SingleRoundRobinExperiment(p, k=k, enemy_list=enemy_list, battle=battle, verbose=verbose)
    loss_times = results['l']
    
    # Higher possibility of loss, and then higher ranking
    id_ranking = [p.index for p in ranking]
    
    # the index is pokeID, and has negative loss_time and rank
    loss_times = np.array([(-loss_time, id_ranking.index(idx)) for idx, loss_time in enumerate(loss_times)], dtype=[('l', 'i'), ('r', 'i')])
    
    # firstly, order by negative loss_time, secondly, by ranking
    strongest_natural_enemy_ids = loss_times.argsort(order=['l', 'r'])[:top]
        
    if verbose:
        print(f"{p.index}. Natural Enemies to {p.name}")
        for idx, i in enumerate(strongest_natural_enemy_ids):
            print(f"{idx+1}. {pokeList[i].name}, loss-times: {-loss_times[i][0]} / {k}")
        print()

    return [pokeList[i] for i in strongest_natural_enemy_ids]

def natural_enemies_list(plist=pokeList, enemy_list=pokeList, k=10, ranking=normal_ranking, battle=pf.battle, top=6, verbose=False):
    return [natural_enemies(p, enemy_list=enemy_list, k=k, ranking=ranking, battle=battle, top=top, verbose=verbose) for p in plist]



try:
    # raise Exception # For creating new pickle file
    with open("data/natural_enemies_list.pkl", "rb") as f:
        ne_list = pickle.load(f)
        print("natural enemies list is loaded from pickle file")
except:
    ne_list = natural_enemies_list(k=1000, verbose=True)
    with open("data/natural_enemies_list.pkl", "wb") as f:
        pickle.dump(ne_list, f)



with open("data/natural_enemies_result.pkl", "rb") as f:
    ne_result = pickle.load(f)

print(ne_result)



k = 100000
loss_count = 0
ne_loss_list = []
for i in range(k):
    enemy_id = np.random.randint(len(pokeList))
    enemy = copyMonster(pokeList[enemy_id])
    natural_enemy = copyMonster(ne_list[enemy_id][0])
    result = pf.battle(natural_enemy, enemy, verbose=False)
    if result == 1:
        loss_count += 1
        ne_loss_list.append((natural_enemy, enemy))
        print("Natural Enemy Lose!")
        print("Natural Enemy:", natural_enemy.name)
        print('vs')
        print("Enemy:", enemy.name)
        print()

print(f"Natural Enemy Lose: {loss_count} times. Win rate: {1 - float(loss_count) / k}")



print(set([(ne_loss_pair[0].name, ne_loss_pair[1].name) for ne_loss_pair in ne_loss_list]))



def team_battle(team1, team2, battle_num=1, battle=pf.battle, verbose=False, run_first=True):
    team_pokemon_num = 6
    
    team1 = [copyMonster(p) for p in team1]
    team2 = [copyMonster(p) for p in team2]
    
    run_first_limit = math.ceil(battle_num / 2)
    
    # reset HP
    for p in range(team_pokemon_num):
        pf.ResetHP(team1[p])
        pf.ResetHP(team2[p])
    
    if verbose:
        print("\n======== Team Battle =======\n")
        print("Team1")
        for p in range(team_pokemon_num): print(team1[p])
        print()
        print("Team2")
        for p in range(team_pokemon_num): print(team2[p])
        print()
    
    team1_win = 0
    team2_win = 0
    
    for i in range(battle_num):
        if verbose:
            print(f"\n======= Battle {i + 1} =======\n")
        
        # reset HP
        for p in range(team_pokemon_num):
            pf.ResetHP(team1[p])
            pf.ResetHP(team2[p])
        
        team1_remain = team_pokemon_num
        team2_remain = team_pokemon_num
        
        # Team Battle Start
        while team1_remain > 0 and team2_remain > 0:
            p1 = team1[-team1_remain]
            p2 = team2[-team2_remain]
            
            if verbose:
                print(f"{p1.name} vs {p2.name}")
                print(p1)
                print(p2)
            
            result = battle(p1, p2, resetHP=False, verbose=False)
            if result == 0: 
                team2_remain -= 1
                if verbose:
                    print(f"team1 {p1.name} win")
            elif result == 1: 
                team1_remain -= 1
                if verbose:
                    print(f"team2 {p2.name} win")
            else:
                team1_remain -=1
                team2_remain -=1
                if verbose:
                    print("Draw")
            
            if verbose:
                print(f"Team1 remain: {team1_remain}")
                print(f"Team2 remain: {team2_remain}")
                print()
        
        if team1_remain > team2_remain:
            team1_win += 1
            if verbose: print("Team1 win")
        elif team1_remain < team2_remain:
            team2_win += 1
            if verbose: print("Team2 win")
        else :
            if verbose: print("Draw")
        
        if run_first and (team1_win >= run_first_limit or team2_win >= run_first_limit):
            if verbose: print(f"{run_first_limit} battles run first")
            break
    
    return (team1_win, team2_win)



team1 = [pokeList[p] for p in np.random.randint(0, len(pokeList),6)]
team2 = [pokeList[p] for p in np.random.randint(0, len(pokeList),6)]

team_battle(team1, team2, battle_num=1, verbose=True)
team_battle(team1, team2, battle_num=100, verbose=False)



strongest_team = normal_ranking[:6]



from itertools import permutations
all_teams = permutations(range(len(pokeList)), r=6)
print(151 ** 6)



from itertools import combinations
all_teams = combinations(range(len(pokeList)), r=1)
151*150*149*148*147*146 / (6*5*4*3*2)



import random

def random_battle(team, challenger_team_num=1000, battle_num=10, allow_same=False):
    winners = []
    for i in range(challenger_team_num):
        if allow_same:
            challenger_team = [pokeList[p] for p in np.random.randint(0, len(pokeList),6)]
        else:
            challenger_team = [pokeList[p] for p in random.sample(range(len(pokeList)),6)]
        (team_win, challenger_win) = team_battle(team, challenger_team, battle_num=battle_num)
        if team_win < challenger_win: 
            winners.append(challenger_team.copy())
    
    return winners



c = 10000
winners = random_battle(strongest_team, challenger_team_num=c)
print(f"Challenger Win Rate: {len(winners)} / {c}")
print()
for w in winners:
    for p in w: print(p)
    print()



def pteam(team):
    for p in team: print(p)
    print()

def team_training(k=10, battle_num=10, initial_team=None, battle=pf.battle, allow_same=False, verbose=False):
    pokeidx = range(len(pokeList))

    if initial_team is not None:
        team = initial_team()
    else:
        team = [pokeList[p] for p in random.sample(pokeidx,6)]
    
    if verbose: 
        print("======== Initial Team ========")
        pteam(team)

    consecutive_win_num = 0
    team_count = 1
    while consecutive_win_num < k:
        
        if allow_same:
            rival = [pokeList[p] for p in np.random.randint(0, len(pokeList), 6)]
        else:
            rival = [pokeList[p] for p in random.sample(pokeidx,6)]
        
        (team_win, rival_win) = team_battle(team, rival, battle=battle, battle_num=battle_num)
        
        if team_win < rival_win: 
            team = rival

            if verbose:
                print(f"======== {team_count}-th New Team =======")
                pteam(team)

            consecutive_win_num = 0
            team_count += 1
        else: 
            consecutive_win_num += 1
    
    if verbose:
        print(f"======== {team_count-1}-th team is the strongest team ========")
        pteam(team)

    return team, team_count-1



start_time = time.time()
strongest_team, team_count = team_training(k=100)
end_time = time.time()

print(f"======== {team_count-1}-th team is the strongest team ========")

pteam(strongest_team)

print("Training Team Elapsed Time: ", end_time - start_time)



print(team_battle(strongest_team, normal_ranking[:6], battle_num=100))



def pteams(teams):
    for i, team in enumerate(teams):
        print(f"team{i+1}")
        pteam(team)

def domestic_battle(teams, battle=pf.battle):
    teams_win_counts = np.zeros(len(teams), dtype='i')
    for t1 in range(len(teams)):
        for t2 in range(t1+1, len(teams)):
            (t1_win, t2_win) = team_battle(teams[t1], teams[t2], battle=battle)
            if t1_win > t2_win: teams_win_counts[t1] += 1
            if t1_win < t2_win: teams_win_counts[t2] += 1

    return teams_win_counts
        
def s_team_training(s=3, k=10, r=1, initial_teams=None, battle_num=10, battle=pf.battle, allow_same=False, verbose=False):
    pokeidx = range(len(pokeList))
    get_team = lambda : [pokeList[p] for p in random.sample(pokeidx, 6)]
    
    if initial_teams is not None:
        teams = [initial_teams[i] for i in range(s)]
    else:
        teams = [get_team() for i in range(s)]

    if verbose: 
        print("======== Initial Teams ========")
        pteams(teams)

    consecutive_win_num = 0
    team_count = 1
    while consecutive_win_num < k:
        
        if allow_same:
            rival = [pokeList[p] for p in np.random.randint(0, len(pokeList), 6)]
        else:
            rival = [pokeList[p] for p in random.sample(pokeidx,6)]
                
        results = []
        for team in teams:
            (team_win, rival_win) = team_battle(team, rival, battle=battle, battle_num=battle_num)
            results.append(team_win <= rival_win)
            
        
        if sum(results) >= round(s / r):
            
            teams_win_counts = domestic_battle(teams, battle)
            
            teams[np.argmin(teams_win_counts)] = rival

            if verbose:
                print(f"======== {team_count}-th New Teams =======")
                pteams(teams)

            consecutive_win_num = 0
            team_count += 1
        else: 
            consecutive_win_num += 1
    
    if verbose:
        print(f"======== {team_count-1}-th teams are the strongest teams ========")
        pteams(teams)

    return teams, team_count-1



try:
    # raise Exception # For creating new pickle data
    with open('data/strongest_teams.pkl', 'rb') as f:
        strongest_teams = pickle.load(f)
        print('strongest teams are loaded from the pickle file')
except:
    k = 10000
    
    start_time = time.time()
    strongest_teams, team_count = s_team_training(k=k, battle=pf.battle, verbose=True)
    end_time = time.time()

    print(f"Elapsed Time for s-Team Training Algorithm of k={k}: {end_time-start_time}[sec] \n")
    print(f"======== {team_count}-th teams are the strongest teams ========")
    pteams(strongest_teams)
    
    with open('data/strongest_teams.pkl', mode='wb') as f:
        pickle.dump(strongest_teams, f)



win_times = np.sum([domestic_battle(strongest_teams, battle=pf.battle) for i in range(100)], axis=0)
print(win_times)



print(strongest_teams[1])



normal_result_team = normal_ranking[:6]
pteam(normal_result_team)
print(team_battle(normal_result_team, strongest_teams[1], battle_num=1000))



try:
    # raise Exception # For creating new pickle data
    with open('data/strongest_teams_with_strongest_init.pkl', 'rb') as f:
        strongest_teams = pickle.load(f)
        print('strongest teams with strongest init are loaded from the pickle file')
except:
    s = 3
    k = 100000
    initial_teams = [normal_ranking[:6] for i in range(s)]
    random.shuffle(initial_teams[1])
    random.shuffle(initial_teams[2])
    
    start_time = time.time()
    strongest_teams, team_count = s_team_training(k=k, initial_teams=initial_teams, verbose=True)
    end_time = time.time()

    print(f"Elapsed Time for s-Team Training Algorithm of k={k}: {end_time-start_time}[sec] \n")
    print(f"======== {team_count}-th teams are the strongest teams ========")
    pteams(strongest_teams)
    
    with open('data/strongest_teams_with_strongest_init.pkl', mode='wb') as f:
        pickle.dump(strongest_teams, f)



print(np.sum([domestic_battle(strongest_teams, battle=pf.battle) for i in range(100)], axis=0))



(strongest_teams[0])



c_team = [copyMonster(pokedex['Cloyster']) for i in range(6)]
r_team = [copyMonster(pokedex['Rhydon']) for i in range(6)]

print(team_battle(c_team, r_team, battle_num=100))



cr_team = [
    copyMonster(pokedex['Rhydon']),
    copyMonster(pokedex['Cloyster']),
    copyMonster(pokedex['Rhydon']),
    copyMonster(pokedex['Rhydon']),
    copyMonster(pokedex['Rhydon']),
    copyMonster(pokedex['Cloyster'])
]

print(team_battle(c_team, cr_team, battle_num=100))
print(team_battle(r_team, cr_team, battle_num=100))



crd_team = [
    copyMonster(pokedex['Rhydon']),
    copyMonster(pokedex['Cloyster']),
    copyMonster(pokedex['Dragonite']),
    copyMonster(pokedex['Cloyster']),
    copyMonster(pokedex['Rhydon']),
    copyMonster(pokedex['Cloyster'])
]

print(team_battle(c_team, crd_team, battle_num=100))
print(team_battle(r_team, crd_team, battle_num=100))
print(team_battle(cr_team, crd_team, battle_num=100))



winners = random_battle(c_team, battle_num=1000, allow_same=True)
if len(winners) > 0:
    pteams(winners)
else:
    print("No team could beat Cloyster Team.")



winners = random_battle(cr_team, battle_num=1000, allow_same=True)
if len(winners) > 0:
    pteams(winners)
else:
    print("No team could beat Cloyster Rhydon Team.")



winners = random_battle(crd_team, battle_num=1000, allow_same=True)
if len(winners) > 0:
    pteams(winners)
else:
    print("No team could beat Cloyster Rhydon Dragonite Team.")



try:
    # raise Exception # For creating new pickle data
    with open('data/strongest_teams_with_strongest_init_same.pkl', 'rb') as f:
        strongest_teams = pickle.load(f)
        print('strongest teams with strongest init are loaded from the pickle file')
except:
    s = 3
    k = 100000
    initial_teams = [c_team, cr_team, crd_team]
    
    start_time = time.time()
    strongest_teams, team_count = s_team_training(k=k, initial_teams=initial_teams, allow_same=True, verbose=True)
    end_time = time.time()

    print(f"Elapsed Time for s-Team Training Algorithm of k={k}: {end_time-start_time}[sec] \n")
    print(f"======== {team_count}-th teams are the strongest teams ========")
    pteams(strongest_teams)
    
    with open('data/strongest_teams_with_strongest_init_same.pkl', mode='wb') as f:
        pickle.dump(strongest_teams, f)



result = np.sum([domestic_battle(strongest_teams) for i in range(100)], axis=0)
print(result)
strongest_team = strongest_teams[result.argmax()]
pteam(strongest_team)



def natural_enemies_team(team, natural_enemies_list=ne_list, allow_same=False):
    ne_team = []
    for p in team:
        nes = ne_list[p.index]
        if allow_same:
            ne_team.append(nes[0])
        else:
            for ne in nes:
                if ne not in ne_team:
                    ne_team.append(ne)
                    break
    return ne_team



def ne_random_battle(challenger_team_num=1000, battle_num=10, allow_same=False):
    winners = []
    for i in range(challenger_team_num):
        if allow_same:
            challenger_team = [pokeList[p] for p in np.random.randint(0, len(pokeList),6)]
        else:
            challenger_team = [pokeList[p] for p in random.sample(range(len(pokeList)),6)]
        ne_team = natural_enemies_team(challenger_team, allow_same=allow_same)
        (ne_team_win, challenger_win) = team_battle(ne_team, challenger_team, battle_num=battle_num)
        if ne_team_win < challenger_win: 
            winners.append(challenger_team.copy())
    
    return winners



winners = ne_random_battle(challenger_team_num=10000)
if len(winners) > 0:
    pteams(winners)
else:
    print("No team could beat its natural enemies team.")



winners = ne_random_battle(challenger_team_num=10000, allow_same=True)
if len(winners) > 0:
    pteams(winners)
else:
    print("No team could beat its natural enemies team.")



crd_ne_team = natural_enemies_team(crd_team, allow_same=True)
print(team_battle(crd_team, crd_ne_team, battle_num=1000))