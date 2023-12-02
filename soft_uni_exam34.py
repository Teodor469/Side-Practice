class Heroes:
    def __init__(self, hero_name, hp, mp) -> None:
        self.hero_stats = {}
        self.hero_name = hero_name
        self.max_hp = 100
        self.max_mp = 200
        self.hp = min(hp, self.max_hp)
        self.mp = min(mp, self.max_mp)

    def cast_spell(self, spell_name, mana_needed):
        if self.mp >= mana_needed:
            self.mp -= mana_needed
            print(f"{self.hero_name} has successfully cast {spell_name} and now has {self.mp} MP!" )
        else:
            print(f"{self.hero_name} does not have enough MP to cast {spell_name}!")

    def take_damage(self, damage, attacker):
        self.hp = max(0, self.hp - damage)
        if self.hp > 0:
            print(f"{self.hero_name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!")
        else:
            self.hp < 0
            del self.hero_stats[self.hero_name]
            print(f"{self.hero_name} has been killed by {attacker}!")

    def recharge(self, amount):
        pass