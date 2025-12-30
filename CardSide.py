class CardSide:
    def __init__(self, attack_type, attack_speed, attack_power, starting_health=1):
        self.attack_type = attack_type  # Initialize instance attributes
        self.attack_speed = attack_speed
        self.attack_power = attack_power

        # Power 5 Deals 2 damage, 1 deals 0, all others are 1
        if self.attack_power >= 4:
            self.attack_damage = 1
        elif self.attack_power <= 1:
            self.attack_damage = 0
        else:
            self.attack_damage = 1

        self.starting_health = starting_health
        self.is_alive = True

    def __str__(self):
        return (
            f"Type: {self.attack_type}\n"
            f"Speed: {self.attack_speed}\n"
            f"Power: {self.attack_power}\n"
            f"Starting Health: {self.starting_health}"
        )

# Example Usage:
if __name__ == "__main__":
    # Create an instance of the class
    my_instance = CardSide('A', 2,2)

    # Print the object (uses the __str__ method)
    print(my_instance)
