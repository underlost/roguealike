class BasicMonster:

    def take_turn(self, target, game_map, entities):
        #print('The ' + self.owner.name + ' wants a hug
        results = []
        monster = self.owner

        if game_map.fov[monster.x, monster.y]:
            if monster.distance_to(target) >= 2:
                monster.move_to(target.x, target.y, game_map, entities)
            elif target.class_type.hp > 0:
                #print('The {0} demands a hug! You are scared'.format(monster.name))
                attack_results = monster.class_type.attack(target)
                results.extend(attack_results)
        return results
