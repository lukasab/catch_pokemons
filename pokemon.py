from collections import defaultdict

def get_input():
    return input()

def catch_pokemons(initial_x_position = 0, initial_y_position = 0):
    x_counter, y_counter = initial_x_position, initial_y_position
    pokemons_captured = 1
    visited_positions = defaultdict(int)
    visited_positions[(x_counter,y_counter)] = 1
    movements = list(get_input())
    for movement in movements:
        if movement == "N":
            y_counter += 1
        elif movement == "S":
            y_counter -= 1
        elif movement == "E":
            x_counter += 1
        elif movement == "O":
            x_counter -= 1

        if visited_positions[(x_counter, y_counter)] == 0:
            visited_positions[(x_counter, y_counter)] = 1
            pokemons_captured += 1
    print(pokemons_captured)
    return pokemons_captured

if __name__ == "__main__":
    catch_pokemons()
