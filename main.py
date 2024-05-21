import random

# Based on Video by Mark Biernat: https://www.youtube.com/watch?v=IpJ5XKw8EZU
# Monte Carlo-based military simulation

# AR = Attacker Retreat
# DR = Defender Retreat
# DE = Defender Eliminated
# AE = Attacker Eliminated
# EX = Exchange

# Define the Combat Results Table (CRT)
crt = {
    (1, '1-2'): 'DR', (1, '1-1'): 'DR', (1, '2-1'): 'DE', (1, '3-1'): 'DE', (1, '4-1'): 'DE', (1, '5-1'): 'DE', (1, '6-1'): 'DE',
    (2, '1-2'): 'DR', (2, '1-1'): 'DR', (2, '2-1'): 'DR', (2, '3-1'): 'DR', (2, '4-1'): 'DE', (2, '5-1'): 'DE', (2, '6-1'): 'DE',
    (3, '1-2'): 'AR', (3, '1-1'): 'DR', (3, '2-1'): 'DR', (3, '3-1'): 'DR', (3, '4-1'): 'DR', (3, '5-1'): 'DR', (3, '6-1'): 'DE',
    (4, '1-2'): 'AR', (4, '1-1'): 'AR', (4, '2-1'): 'DR', (4, '3-1'): 'DR', (4, '4-1'): 'DR', (4, '5-1'): 'DR', (4, '6-1'): 'DR',
    (5, '1-2'): 'AR', (5, '1-1'): 'AR', (5, '2-1'): 'AR', (5, '3-1'): 'DR', (5, '4-1'): 'EX', (5, '5-1'): 'EX', (5, '6-1'): 'DR',
    (6, '1-2'): 'AE', (6, '1-1'): 'AR', (6, '2-1'): 'AR', (6, '3-1'): 'EX', (6, '4-1'): 'EX', (6, '5-1'): 'EX', (6, '6-1'): 'EX',
}

# Define terrain multipliers
terrain_multipliers = {
    'clear': 1,
    'forest': 2,
    'rough': 2,
    'road': 1,
    'creek': 1,
    'bridge': 1,
    'forest_rough': 2,
    'river': 2,
    'town': 2,
    'ford': 2,
    'trail': 1,
    'village': 2
}

def simulate_combat(attacker_strength, defender_strength, terrain, simulations=10000):
    results = {'DR': 0, 'AR': 0, 'DE': 0, 'AE': 0, 'EX': 0}
    terrain_multiplier = terrain_multipliers[terrain]
    effective_defender_strength = defender_strength * terrain_multiplier

    for _ in range(simulations):
        ratio = attacker_strength / effective_defender_strength
        if ratio >= 6:
            ratio_column = '6-1'
        elif ratio >= 5:
            ratio_column = '5-1'
        elif ratio >= 4:
            ratio_column = '4-1'
        elif ratio >= 3:
            ratio_column = '3-1'
        elif ratio >= 2:
            ratio_column = '2-1'
        elif ratio >= 1:
            ratio_column = '1-1'
        else:
            ratio_column = '1-2'
        
        die_roll = random.randint(1, 6)
        result = crt[(die_roll, ratio_column)]
        results[result] += 1

    return results

def main():
    # Set the combat strengths and terrain
    attacker_strength = int(input("Enter attacker strength: "))
    defender_strength = int(input("Enter defender strength: "))
    terrain = input("Enter terrain type (clear, forest, rough, road, creek, bridge, forest_rough, river, town, ford, trail, village): ").strip().lower()

    # Simulate the combat
    results = simulate_combat(attacker_strength, defender_strength, terrain)
    
    # Display the results
    total_simulations = sum(results.values())
    print("\nSimulation Results:")
    for result, count in results.items():
        print(f"{result}: {count} ({count / total_simulations * 100:.2f}%)")

if __name__ == "__main__":
    main()
