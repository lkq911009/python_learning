


def life_generator():
    lives = 3
    while lives > 0:
        yield f"You have {lives} {'lives' if lives > 1 else 'live'} left"
        lives -= 1
    yield "Game Over"



lose_live = life_generator()
print(next(lose_live))
