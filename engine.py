import tdl

from components.player_type import Mage, Warrior

from settings import *
from handler import handle_keys
from functions import clear_all, render_all
from entity import Entity, get_blocking_entities_at_location
from game_state import GameStates
from map_util import make_map, GameMap

def main():

    root_console = tdl.init(screen_width, screen_height, title='Roguealike')
    con = tdl.Console(screen_width, screen_height)

    player_component = Mage(hp=30, defense=2, power=5)
    player = Entity(0, 0, '@', (255, 255, 255), 'Player', blocks=True, class_type=player_component)

    entities = [player]

    tdl.set_font('assets/arial10x10.png', greyscale=True, altLayout=True)

    game_map = GameMap(map_width, map_height)
    make_map(game_map, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities, max_monsters_per_room, colors)
    fov_recompute = True

    game_state = GameStates.PLAYERS_TURN

    while not tdl.event.is_window_closed():
        if fov_recompute:
            game_map.compute_fov(player.x, player.y, fov=fov_algorithm, radius=fov_radius, light_walls=fov_light_walls)
        render_all(con, entities, game_map, fov_recompute, root_console, screen_width, screen_height, colors)
        tdl.flush()

        clear_all(con, entities)

        fov_recompute = False

        for event in tdl.event.get():
            if event.type == 'KEYDOWN':
                user_input = event
                break
        else:
            user_input = None

        if not user_input:
            continue

        action = handle_keys(user_input)
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move and game_state == GameStates.PLAYERS_TURN:
            dx, dy = move
            destination_x = player.x + dx
            destination_y = player.y + dy

            if game_map.walkable[destination_x, destination_y]:
                target = get_blocking_entities_at_location(entities, destination_x, destination_y)
                if target:
                    #print('You hug ' + target.name )
                    player.class_type.attack(target)
                else:
                    player.move(dx, dy)
                    fov_recompute = True

                game_state = GameStates.ENEMY_TURN

        if exit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())

        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity.ai:
                    #print('The ' + entity.name + ' wants a hug.')
                    entity.ai.take_turn(player, game_map, entities)


            game_state = GameStates.PLAYERS_TURN

if __name__ == '__main__':
    main()
