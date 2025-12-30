from Card import Card
from CardSide import CardSide
from Battle import Battle
from Player import Player

def run_rps_advantage_battle():
    player_one = Player(10, [], [], [], [])
    # Player Character
    player_side_1 = CardSide(attack_type='A', attack_speed=2, attack_power=2)
    player_side_2 = CardSide(attack_type='A', attack_speed=2, attack_power=2)
    player_card = Card(front_side=player_side_1, back_side=player_side_2)

    # Opponent Card
    opponent_side_1 = CardSide(attack_type='G', attack_speed=3, attack_power=2)
    opponent_side_2 = CardSide(attack_type='G', attack_speed=2, attack_power=1)
    opponent_card = Card(front_side=opponent_side_1, back_side=opponent_side_2)

    battle_one = Battle(player_card,opponent_card,player_one)
    battle_one.fight_battle()
    print("BATTLE ONE RESULTS")
    print('###### Opponent Info ######')
    print(opponent_card)
    print('###### Player Info   ######')
    print(player_one)

    battle_two = Battle(player_card, opponent_card, player_one)
    battle_two.fight_battle()
    print("BATTLE TWO RESULTS")
    print('###### Opponent Info ######')
    print(opponent_card)
    print('###### Player Info   ######')
    print(player_one)

    battle_three = Battle(player_card, opponent_card, player_one)
    battle_three.fight_battle()
    print("BATTLE THREE RESULTS")
    print('###### Opponent Info ######')
    print(opponent_card)
    print('###### Player Info   ######')
    print(player_one)

def run_rps_disadvantage_battle():
    player_one = Player(10, [], [], [], [])
    # Player Character
    player_side_1 = CardSide(attack_type='C', attack_speed=2, attack_power=2)
    player_side_2 = CardSide(attack_type='C', attack_speed=2, attack_power=2)
    player_card = Card(front_side=player_side_1, back_side=player_side_2)

    # Opponent Card
    opponent_side_1 = CardSide(attack_type='G', attack_speed=3, attack_power=2)
    opponent_side_2 = CardSide(attack_type='G', attack_speed=2, attack_power=1)
    opponent_card = Card(front_side=opponent_side_1, back_side=opponent_side_2)

    battle_one = Battle(player_card, opponent_card, player_one)
    battle_one.fight_battle()
    print("BATTLE ONE RESULTS")
    print('###### Opponent Info ######')
    print(opponent_card)
    print('###### Player Info   ######')
    print(player_one)

    battle_two = Battle(player_card, opponent_card, player_one)
    battle_two.fight_battle()
    print("BATTLE TWO RESULTS")
    print('###### Opponent Info ######')
    print(opponent_card)
    print('###### Player Info   ######')
    print(player_one)

    battle_three = Battle(player_card, opponent_card, player_one)
    battle_three.fight_battle()
    print("BATTLE THREE RESULTS")
    print('###### Opponent Info ######')
    print(opponent_card)
    print('###### Player Info   ######')
    print(player_one)

if __name__ == "__main__":
    run_rps_disadvantage_battle()
