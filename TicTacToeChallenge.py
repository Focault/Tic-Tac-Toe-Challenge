from Logic import initialize_game, run_game
from UI import hello

ROW_SIZE = (3,)


if __name__ == "__main__":
    resume = True
    hello()
    while resume:
        game_components = initialize_game(ROW_SIZE[0])
        resume = run_game(game_components)
