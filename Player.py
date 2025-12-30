class Player:
    def __init__(self, health, deck, discard_pile, combo_list, power_list):
        self.health = health
        self.deck = deck
        self.discard_pile = discard_pile
        self.combo_list = combo_list
        self.power_list = power_list
        self.is_alive = True

    def apply_damage(self, damage_amount):
        self.health -= damage_amount
        if self.health <= 0:
            self.health = 0
            self.is_alive = False

    def __str__(self):
        return str(self.health) + str(self.is_alive)
