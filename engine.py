import tdl

from handler import handle_keys
from functions import clear_all, render_all
from entity import Entity


def main():
    screen_width = 80
    screen_height = 50

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', (255, 255, 0))
    entities = [npc, player]

    tdl.set_font('assets/arial10x10.png', greyscale=True, altLayout=True)

    render_all(con, entities, root_console, screen_width, screen_height)

    while not tdl.event.is_window_closed():
        con.draw_char(player_x, player_y, '@', bg=None, fg=(255, 255, 255))
        root_console.blit(con, 0, 0, screen_width, screen_height, 0, 0)
        tdl.flush()

        con.draw_char(player_x, player_y, ' ', bg=None)

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

        if move:
            dx, dy = move
            player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            tdl.set_fullscreen(not tdl.get_fullscreen())

if __name__ == '__main__':
    main()
