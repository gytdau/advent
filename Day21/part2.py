import itertools

weapons = [  # Exactly 1
    [8, 4, 0],
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0]
]
armor = [  # 0 to 1
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 4],
    [102, 0, 5],
    [0, 0, 0]  # Armor is optional
]
rings = [  # 0 to 2
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3],
    [0, 0, 0],
    [0, 0, 0]  # Two rings are optional
]

enemy_hp = 0
enemy_dmg = 0
enemy_armor = 0

with open("inputData.txt", "r") as infile:
    """
    Process inputData.txt to get the enemy values.
    """
    for line in infile:
        data = line.split()
        if data[0] == "Hit":
            enemy_hp = int(data[2])
        elif data[0] == "Damage:":
            enemy_dmg = int(data[1])
        else:
            enemy_armor = int(data[1])


def does_player_win(dmg, armor):
    """
    Does the player win against the boss with this amount of 'dmg' and 'armor' points?
    :param dmg: Amount of dmg points the player has
    :param armor: Amount of armor points the player has
    :return: True if the player wins against the boss; False otherwise
    """
    this_enemy_hp = enemy_hp
    this_enemy_dmg = enemy_dmg
    this_enemy_armor = enemy_armor
    this_player_hp = 100
    this_player_dmg = dmg
    this_player_armor = armor

    this_enemy_hit = max(1, this_enemy_dmg - this_player_armor)
    this_player_hit = max(1, this_player_dmg - this_enemy_armor)

    toggler = True
    while this_enemy_hp > 0 and this_player_hp > 0:
        if toggler:
            this_enemy_hp -= this_player_hit
        else:
            this_player_hp -= this_enemy_hit
        toggler = not toggler

    return this_enemy_hp <= 0


def get_stats(equipment):
    """
    Adds up the stats of the equipment
    :param equipment: A list with multiple lists inside - the inner lists are the equipment stats
    :return: Total cost, dmg, and armor points
    """
    dmg = 0
    armor_points = 0
    cost = 0

    for thing in equipment:
        dmg += thing[1]
        armor_points += thing[2]
        cost += thing[0]

    return cost, dmg, armor_points


possible_costs = []
possible_ring_combinations = list(itertools.combinations(rings, 2))
for weapon in weapons:
    for n_armor in armor:
        for rings in possible_ring_combinations:
            cost, dmg, armor_points = get_stats([weapon] + [n_armor] + list(rings))
            # This line was modified, to only add the cost if the player does not win
            if not does_player_win(dmg, armor_points):
                possible_costs.append(cost)

# This line was modified, to get the max instead of the min cost
print("Answer: " + str(max(possible_costs)))