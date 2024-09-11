import random


class Creature:
    """
    Represents a generic creature in the RPG game.
    """

    def __init__(self, name, hp, ac):
        """
        Initializes a Creature instance.

        Args:
            name (str): The name of the creature.
            hp (int): The creature's hit points.
            ac (int): The creature's armor class.
        """
        self.name = name
        self.hp = hp
        self.ac = ac

    def take_damage(self, damage):
        """
        Reduces the creature's HP by the given damage amount.
        """
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} takes {damage} damage! HP: {self.hp}")

    def attack(self, target, weapon):
        """
        Attacks the target creature using the specified weapon, considering S.P.E.C.I.A.L. stats.
        """
        if weapon.range > 0 and self.distance_to(target) > weapon.range:
            print(f"{self.name} is too far away to attack with {weapon.name}!")
            return

        # Accuracy calculation
        hit_chance = weapon.accuracy
        if weapon.range > 0:  # Ranged weapon
            if isinstance(self, PlayerCharacter):
                hit_chance += (
                    self.special["Perception"] - 5
                ) * 0.05  # Adjust based on Perception which has logic I dunno yet.

        if random.random() > hit_chance:
            print(f"{self.name}'s attack with {weapon.name} missed!")
            return

        # Damage calculation
        damage = weapon.damage
        if weapon.damage_type == "melee" and isinstance(self, PlayerCharacter):
            damage += (self.special["Strength"] - 5) * 2  # Adjust based on Strength

        # Critical hit calculation (Luck influences crit chance)
        crit_chance = weapon.crit_chance
        if isinstance(self, PlayerCharacter):
            crit_chance += (self.special["Luck"] - 5) * 0.01  # Adjust based on Luck

        if random.random() <= crit_chance:
            damage *= weapon.crit_multiplier
            print("Critical hit!")

        target.take_damage(damage)
        print(
            f"{self.name} attacks {target.name} with {weapon.name} for {damage} damage!"
        )

    def distance_to(self, other):
        """
        Calculates the distance between this creature and another creature.

        Args:
            other (Creature): The other creature.

        Returns:
            int: The distance between the two creatures. (logic here)
        """
        # Placeholder implementation - logic here which I dunno currently
        return 5  # Assume a distance of 5 units currently.


class PlayerCharacter(Creature):
    """
    Represents a player-controlled character in the RPG game.
    """

    def __init__(self, name, hp, ac):
        """
        Initializes a PlayerCharacter instance.

        Args:
            name (str): The name of the player character.
            hp (int): The player character's hit points.
            ac (int): The player character's armor class.
        """
        super().__init__(name, hp, ac)
        self.special = {  # S.P.E.C.I.A.L. stats
            "Strength": 5,
            "Perception": 5,
            "Endurance": 5,
            "Charisma": 5,
            "Intelligence": 5,
            "Agility": 5,
            "Luck": 5,
        }
        self.perks = []  # List to store acquired perks

    def add_perk(self, perk_name):
        """
        Adds a perk to the player character's perk list.
        """
        self.perks.append(perk_name)
        print(f"{self.name} acquired the perk: {perk_name}")


class NPC(Creature):
    """
    Represents a non-player character in the RPG game.
    """

    def __init__(self, name, hp, ac):
        """
        Initializes an NPC instance.

        Args:
            name (str): The name of the NPC.
            hp (int): The NPC's hit points.
            ac (int): The NPC's armor class.
        """
        super().__init__(name, hp, ac)


class FeralGhoul(NPC):
    """
    Represents a Feral Ghoul, a dangerous mutated creature.
    """

    def __init__(self, name="Feral Ghoul", hp=30, ac=6):
        """
        Initializes a Feral Ghoul instance.
        """
        super().__init__(name, hp, ac)

    def attack(self, target):
        """
        Feral Ghouls have a chance to inflict radiation poisoning on their target.
        """
        super().attack(target, Weapon("Claws", "melee", 12))  # Base claw attack
        if random.random() < 0.3:  # 30% chance to inflict radiation poisoning
            target.take_damage(5)  # Additional radiation damage cause fuck you.
            print(f"{target.name} suffers from radiation poisoning!")


class Deathclaw(NPC):
    """
    Represents a Deathclaw,
    an extremely powerful and deadly creature that will definitely kill you.
    """

    def __init__(self, name="Deathclaw", hp=200, ac=15):
        """
        Initializes a Deathclaw instance.
        """
        super().__init__(name, hp, ac)

    def attack(self, target):
        """
        Deathclaws have a high critical hit chance and will pwn you
        """
        if random.random() < 0.5:  # 50% chance for power attack
            super().attack(target, Weapon("Power Attack", "melee", 50, crit_chance=0.4))
        else:
            super().attack(target, Weapon("Claws", "melee", 25, crit_chance=0.2))


class Raider(NPC):
    """
    This represents a raider of the wasteland, 
    typically pretty easy to kill but has a chance
    to inflict pretty decent damage with crits
    """

    def __init__(self, name="Raider", hp=75, ac=5):
        """
        initializes a raider instance
        """

        super().__init__(name, hp, ac)

    def attack(self, target):
        """
        Raider has a gun and can probably kill you if you are not cool
        """
        if random.random() < 0.1:  # 10% chance of headshot
            super().attack(target, Weapon("Headshot", "range", 25, crit_chance=0.1))
        else:
            super().attack(target, Weapon("Gunshot", "range", 15, crit_chance=0.2))


class Weapon:
    """
    Represents a weapon in the RPG game.
    """

    def __init__(
        self,
        name,
        damage_type,
        damage,
        range=0,
        accuracy=0.8,
        crit_chance=0.1,
        crit_multiplier=1.5,
    ):
        """
        Initializes a Weapon instance.

        Args:
            name (str): The name of the weapon.
            damage_type (str): The type of damage the weapon inflicts (e.g., "melee", "ballistic", "energy")
            Which I have not added yet.
            damage (int): The base damage the weapon deals.
            range (int,): The weapon's range in units (0 for melee). Defaults to 0.
            accuracy (float): The probability of hitting the target (0.0 to 1.0).
            crit_chance (float): The probability of landing a critical hit (0.0 to 1.0).
            crit_multiplier (float): The damage multiplier for critical hits.
        """
        self.name = name
        self.damage_type = damage_type
        self.damage = damage
        self.range = range
        self.accuracy = accuracy
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier


def battle(player, enemy):
    """
    Simulates a battle between the player and an enemy which is why its named battle.
    """
    while player.hp > 0 and enemy.hp > 0:
        # Player's turn
        print("\nPlayer's turn:")
        print("Available actions:")
        print("1. Attack with Combat Knife")
        print("2. Attack with Laser Rifle")
        print("3. Attack with Rifle")
        # ... (If I felt more creative I would add more actions. )

        action_choice = input("Choose an action (1/2/3): ")

        if action_choice == "1":
            player.attack(enemy, knife)
        elif action_choice == "2":
            player.attack(enemy, laser_rifle)
        elif action_choice == "3":
            player.attack(enemy, rifle)
        else:
            print("Invalid action choice!")

        if enemy.hp <= 0:
            print(f"{player.name} wins!")
            break

        # Enemy's turn
        print("\nEnemy's turn:")
        enemy.attack(player)  # Surprise! The enemy can attack too.

        if player.hp <= 0:
            print(f"{enemy.name} killed yo ass!")
            break


if __name__ == "__main__":
    # Create the player character could I suggest nathan as the name?
    player_name = input("Enter your character's name, Nathan is a great one: ")
    player = PlayerCharacter(player_name, 100, 10)
    player.special["Strength"] = 10
    player.special["Perception"] = 9
    player.special["Luck"] = 5

    # Choose an enemy
    enemy_choice = input("Choose an enemy (raider/ghoul/deathclaw): ")
    if enemy_choice == "raider":
        enemy = Raider()
    elif enemy_choice == "ghoul":
        enemy = FeralGhoul()
    elif enemy_choice == "deathclaw":
        enemy = Deathclaw()
    else:
        print("Invalid enemy choice!")
        exit()

    # Create weapons I dunno why I didn't create a lightsaber...
    knife = Weapon("Combat Knife", "melee", 15)
    laser_rifle = Weapon(
        "Laser Rifle", "energy", 30, range=20, accuracy=0.8, crit_chance=0.2
    )
    rifle = Weapon(
        "Rusty Rifle", "ballistic", 45, range=15, accuracy=0.7, crit_chance=0.3
    )

    # Start the battle! or dont, its your choice I guess.
    battle(player, enemy)
