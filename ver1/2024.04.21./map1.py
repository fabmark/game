def load_world_from_file(filename):
    with open(filename, 'r') as file:
        world_data = []
        for line in file:
            world_data.append(list(map(int, line.split())))
    return world_data

def object_positions():
    # Define the starting position of the player and the positions of the coins
    player_position = (100, 500)  # Example player position
    coin_positions = [(60, 520), (80, 520)]  # Example coin positions
    return player_position, coin_positions

world_data = load_world_from_file("map1.txt")
