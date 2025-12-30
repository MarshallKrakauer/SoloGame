from CardSide import CardSide
class Card:
    def __init__(self, front_side, back_side):
        self.front_side = front_side
        self.back_side = back_side
        self.active_side = self.front_side
        self.health = self.active_side.starting_health
        self.is_alive = True

    def switch_side(self):
        if self.active_side == self.front_side:
            self.active_side = self.back_side
        else:
            self.active_side = self.front_side

    def apply_damage(self, damage_value=1):
        self.health -= damage_value
        if self.health <= 0:
            self.is_alive = False
            self.health = 0
            if self.active_side == self.front_side:
                print("does it do the swtich side")
                self.switch_side()

    def revive_card(self):
        self.health = self.active_side.starting_health
        self.is_alive = True

    def __str__(self):

        if self.active_side == self.front_side:
            side_string = 'FRONT'
        else:
            side_string = 'BACK'
        return(
            f"ACTIVE SIDE ({side_string})\n"
            f"{self.active_side}\n"
            f"HEALTH INFO\n"
            f"Health: {self.health}\n"
            f"Is Alive: {self.is_alive}"
        )

if __name__ == "__main__":
    front_side = CardSide('A', 2,2)
    back_side = CardSide('A', 1,1)
    card1 = Card(front_side, back_side)
    card1.health += 1
    print(card1)
    card1.apply_damage()
    print(card1.active_side.attack_type)
