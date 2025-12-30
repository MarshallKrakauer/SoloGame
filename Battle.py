
from Card import Card
from CardSide import CardSide
from Player import Player

class Battle:
    def __init__(self, player_card: Card, opponent_card: Card, player_character: Player):
        self.player_card = player_card
        self.opponent_card = opponent_card
        player_side: CardSide = player_card.active_side
        opponent_side: CardSide = opponent_card.active_side
        self.player_side = player_side
        self.opponent_side = opponent_side
        self.apply_player_damage = False
        self.apply_opponent_damage = False
        self.player_character = player_character
        #variable_name: Type = initial_value

    # A beats G, G beat C, C beats A
    def apply_rock_paper_scissors(self):
        player_attack_type = self.player_side.attack_type
        opponent_attack_type = self.opponent_side.attack_type
        if player_attack_type == opponent_attack_type:
            return 'equal'
        elif (player_attack_type == 'A' and opponent_attack_type == 'G'
            or player_attack_type == 'C' and opponent_attack_type == 'A'
            or player_attack_type == 'G' and opponent_attack_type == 'C'):
            return 'player'
        else:
            print('confirm opponent victory')
            return 'opponent'

    def apply_speed(self):
        player_speed = self.player_side.attack_speed
        opponent_speed = self.opponent_side.attack_speed
        if player_speed == opponent_speed:
            return 'equal'
        elif player_speed > opponent_speed:
            return 'player'
        else:
            return 'opponent'

    def apply_power(self, speed_advantage='equal'):
        opponent_power = self.opponent_side.attack_power
        player_power = self.player_side.attack_power
        if speed_advantage == 'equal':
            self.apply_player_damage = player_power >= opponent_power
            self.apply_opponent_damage = opponent_power >= player_power
        elif speed_advantage == 'opponent':
            self.apply_player_damage = player_power > opponent_power
            self.apply_opponent_damage = opponent_power >= player_power
        else:
            self.apply_player_damage = player_power >= opponent_power
            self.apply_opponent_damage = opponent_power > player_power

    def apply_damage(self, damage_receiver='player'):
        if damage_receiver == 'player':
            self.player_character.apply_damage(self.opponent_side.attack_damage)
        elif damage_receiver == 'opponent':
            self.opponent_card.apply_damage(self.player_side.attack_damage)


    def fight_battle(self):
        # Apply Rock-Paper-Scissors
        rps_result = self.apply_rock_paper_scissors()
        if rps_result == 'player':
            self.apply_opponent_damage = True
        elif rps_result == 'opponent':
            self.apply_player_damage = True
        else:
            speed_result = self.apply_speed()
            self.apply_power(speed_result)

        if self.apply_opponent_damage:
            self.apply_damage('opponent')

        if self.apply_player_damage:
            self.apply_damage('player')

if __name__ == "__main__":
    player_one = Player(10, [],[],[],[])

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