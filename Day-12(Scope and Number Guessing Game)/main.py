player_health = 12

# def game():
#     def drink_portion():
#         potion_strength = 10
#         print(player_health)
        
#     drink_portion()
    
# print(player_health)

game_level = 3
def create_enemy():
    enemies = ["Aliens","Zombies","Skeleton"]
    if game_level<5:
        new_enemy = enemies[0]
        
    print(new_enemy)
    
create_enemy()

enemies = 1
def increase_enemies():
    print(f"enemies inside function:{enemies}")
    return enemies+1
    
enemies = increase_enemies()
print(f"enemies outside function:{enemies}")

#Global Constants
PI =3.14
URL="www.youtube.com"
TWITTER_HANDLE="ashishkumar@24"