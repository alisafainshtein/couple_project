import initPygame
import screen
import soldier
import consts
import game_field
game_matrix = []
screen.initalize_game_metrix(game_matrix)
soldier_object = soldier.create_soldier_image()
flag_object = screen.create_flag_image()
game_field.init_object(game_matrix, soldier_object)
game_field.init_object(game_matrix, flag_object)
pick_bush_places = game_field.random_bushes()
while initPygame.initialize_pygame():
    while #not flag or bomb - consts bulian
        player_move = game_field.input_move()
        if player_move == #arrows
            game_field.move_soldier()
        elif player_move == #enter
            game_field.show_bushes()

    if flag:
        game_field.win_messege()
    elif bomb:
        game_field.lose_messege()