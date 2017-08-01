class Mage:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        results = []
        self.hp -= amount
        if self.hp <= 0:
            results.append({'dead': self.owner})
        return results

    def attack(self, target):
        results = []
        damage = self.power - target.class_type.defense

        if damage > 0:
            results.append({'message': '{0} attacks {1} for {2} hit points.'.format(self.owner.name.capitalize(), target.name, str(damage))})
            results.extend(target.class_type.take_damage(damage))
        else:
            print('{0} attacks {1} but does no damage.'.format(self.owner.name.capitalize(), target.name))
        return results

class Warrior:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        results = []
        self.hp -= amount
        if self.hp <= 0:
            results.append({'dead': self.owner})
        return results

    def attack(self, target):
        results = []
        damage = self.power - target.class_type.defense
        if damage > 0:
            results.append({'message': '{0} attacks {1} for {2} hit points.'.format(self.owner.name.capitalize(), target.name, str(damage))})
            results.extend(target.class_type.take_damage(damage))
        else:
            print('{0} attacks {1} but does no damage.'.format(self.owner.name.capitalize(), target.name))
        return results
