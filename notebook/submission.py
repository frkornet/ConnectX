def my_random_agent(obs, config):
    EMPTY=0
    from random import choice
    return choice([c for c in range(config.columns) if obs.board[c] == EMPTY])
def my_random_agent(obs, config):
    EMPTY=0
    from random import choice
    return choice([c for c in range(config.columns) if obs.board[c] == EMPTY])
