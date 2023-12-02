class Heroes:
    def __init__(self, hero_name, hp, mp) -> None:
        self.hero_name = hero_name
        self.max_hp = 100
        self.max_mp = 200
        self.hp = min(hp, self.max_hp)
        self.mp = min(mp, self.max_mp)

    def cast_spell(self, spell_name, mana_needed):
        if self.mp >= mana_needed:
            self.mp -= mana_needed
            return f"{self.hero_name} has successfully cast {spell_name} and now has {self.mp} MP!"
        else:
            return f"{self.hero_name} does not have enough MP to cast {spell_name}!"

    def take_damage(self, damage, attacker):
        self.hp = max(0, self.hp - damage)
        if self.hp > 0:
            return f"{self.hero_name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!"
        else:
            return f"{self.hero_name} has been killed by {attacker}!"

    def recharge(self, amount):
        recovered = min(self.max_mp - self.mp, amount)
        self.mp += recovered
        if self.mp > 200:
            self.mp = 200
        return f"{self.hero_name} recharged for {recovered} MP!"

    def heal(self, amount):
        recovered = min(self.max_hp - self.hp, amount)
        self.hp += recovered
        if self.hp > 100:
            self.hp = 100
        return f"{self.hero_name} healed for {recovered} HP!"

heroes = {}
number_of_heroes = int(input())

for _ in range(number_of_heroes):
    hero = input().split()
    hero_name, hp, mp = hero[0], int(hero[1]), int(hero[2])
    heroes[hero_name] = Heroes(hero_name, hp, mp)

while True:
    command = input().split(" - ")
    if command[0] == 'End':
        break

    action, hero_name, *args = command
    current_hero = heroes[hero_name]

    if action == "CastSpell":
        mp_needed, spell_name = int(args[0]), args[1]
        print(current_hero.cast_spell(spell_name, mp_needed))
    elif action == "TakeDamage":
        damage_taken, attacker = int(args[0]), args[1]
        print(current_hero.take_damage(damage_taken, attacker))
        if current_hero.hp <= 0:
            del heroes[hero_name]
    elif action == "Recharge":
        amount = int(args[0])
        print(current_hero.recharge(amount))
    elif action == "Heal":
        amount = int(args[0])
        print(current_hero.heal(amount))

for hero in heroes.values():
    print(f"{hero.hero_name}\n  HP: {hero.hp}\n  MP: {hero.mp}")
