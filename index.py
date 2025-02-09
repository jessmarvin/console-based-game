import random

def player_menu():
    print("Choose an action:")
    print("1. Attack")
    print("2. Defend")
    print("3. Use Potion")
    print("4. Run")
    print("5. End Game")
    
    choice = input("Enter your choice (1-5): ")
    while choice not in {'1', '2', '3', '4', '5'}:
        choice = input("Invalid choice. Enter a number between 1 and 5: ")
    return int(choice)

def generate_enemy():
    enemies = ["Mark", "John", "Rhenz", "Ryan", "Ivan"]
    return random.choice(enemies), random.randint(30, 50)  

def calculate_damage(strength):
    modifier = random.uniform(0.8, 1.2)
    return int(strength * modifier)

def calculate_experience(current_exp, gained_exp):
    return current_exp + gained_exp

def calculate_health(current_health, damage):
    return max(current_health - damage, 0)

def check_level_up(exp, threshold):
    return exp >= threshold

def start():
    player_health = 100
    player_exp = 0
    player_strength = 10
    potions = 3
    level_threshold = 100
    
    print("Welcome to the game!")
    
    while player_health > 0:
        enemy_name, enemy_health = generate_enemy()
        print(f"You have encountered {enemy_name} (HP: {enemy_health})")
        
        while enemy_health > 0 and player_health > 0:
            action = player_menu()
            
            if action == 1: 
                damage = calculate_damage(player_strength)
                enemy_health = calculate_health(enemy_health, damage)
                print(f"You dealt {damage} damage. {enemy_name} has {enemy_health} HP left.")
                player_exp = calculate_experience(player_exp, 10)
            elif action == 2: 
                print("You brace for impact, reducing damage.")
                enemy_damage = max(random.randint(5, 15) // 2, 1)
            elif action == 3: 
                if potions > 0:
                    player_health = min(player_health + 20, 100)
                    potions -= 1
                    print(f"You used a potion! Remaining potions: {potions}. HP: {player_health}")
                else:
                    print("You have no potions left!")
                continue
            elif action == 4:  
                print("You successfully ran away!")
                break
            elif action == 5:  
                print("Game Over")
                return
            
            if enemy_health > 0:  
                enemy_damage = random.randint(5, 15)
                player_health = calculate_health(player_health, enemy_damage)
                print(f"{enemy_name} attacks! You take {enemy_damage} damage. Your HP: {player_health}")
            
        if check_level_up(player_exp, level_threshold):
            print("Congratulations! You leveled up! Strength increased.")
            player_strength += 5
            player_exp = 0  
            level_threshold += 50  
        
    print("Game Over! You fought bravely.")
    
start()
