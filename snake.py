import random

GRID_WIDTH = 20
GRID_HEIGHT = 20

def create_grid(width, height):
    return [[' '] * width for _ in range(height)]

def initialize_game():
    snake = [(GRID_HEIGHT // 2, GRID_WIDTH // 2 - 1),
             (GRID_HEIGHT // 2, GRID_WIDTH // 2),
             (GRID_HEIGHT // 2, GRID_WIDTH // 2 + 1)] # Starts length 3, middle, moving right. Head is last element.
    direction = (0, 1) # (row_change, col_change) for right
    food = place_food(snake)
    return snake, direction, food

def place_food(snake):
    while True:
        food_pos = (random.randint(0, GRID_HEIGHT - 1), random.randint(0, GRID_WIDTH - 1))
        if food_pos not in snake:
            return food_pos

def move_snake(snake, direction, food):
    head_row, head_col = snake[-1]
    new_head = (head_row + direction[0], head_col + direction[1])

    # Check for collision with walls - this is just for the move, actual game collision check is separate
    if not (0 <= new_head[0] < GRID_HEIGHT and 0 <= new_head[1] < GRID_WIDTH):
        return [], False, True # Indicate game over by returning empty snake

    snake.append(new_head)
    food_eaten = (new_head == food)

    if not food_eaten:
        snake.pop(0) # Remove tail if no food eaten

    return snake, food_eaten, False # Return updated snake, food_eaten status, and game_over status

def check_collision(snake):
    head_row, head_col = snake[-1]

    # Wall collision (already handled in move_snake for immediate game over, but keeping separate for clarity)
    if not (0 <= head_row < GRID_HEIGHT and 0 <= head_col < GRID_WIDTH):
        return True

    # Self-collision
    if snake[-1] in snake[:-1]:
        return True
    
    return False

def render(snake, food):
    grid = create_grid(GRID_WIDTH, GRID_HEIGHT)
    for r, c in snake:
        if 0 <= r < GRID_HEIGHT and 0 <= c < GRID_WIDTH: # Ensure within bounds for rendering
            grid[r][c] = 'S'
    if food:
        grid[food[0]][food[1]] = 'F'

    # Render borders
    border_h = '+-' + '--' * GRID_WIDTH + '+'
    print(border_h)
    for row in grid:
        print('|' + ' '.join(row) + ' |')
    print(border_h)

def game_loop():
    snake, direction, food = initialize_game()
    game_over = False

    print("Initial Game State:")
    render(snake, food)

    # Simple demonstration of movement and collision
    # For a real game, this would involve continuous input and updates.

    # Simulate a few moves
    for i in range(5):
        print(f"\nMove {i+1}:")
        snake, food_eaten, game_over_move = move_snake(snake, direction, food)
        if game_over_move:
            game_over = True
            print("Game Over! (Wall collision)")
            break
        
        if food_eaten:
            food = place_food(snake) # Place new food if eaten
            print("Food Eaten!")
        
        if check_collision(snake):
            game_over = True
            print("Game Over! (Self collision)")
            break
        
        render(snake, food)

    if not game_over:
        print("\nGame continues... (end of demo moves)")

if __name__ == "__main__":
    game_loop()
