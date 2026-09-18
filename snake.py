import random

GRID_WIDTH = 20
GRID_HEIGHT = 20

# Directions as (dx, dy)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def initialize_game():
    """Initializes the game state."""
    # Snake starts length 3 in the middle, moving right
    snake = [
        (GRID_WIDTH // 2, GRID_HEIGHT // 2),  # Head
        (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
        (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)
    ]
    direction = RIGHT
    food = generate_food(snake)
    return snake, food, direction

def generate_food(snake):
    """Generates a random food position not on the snake."""
    while True:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if food not in snake:
            return food

def get_new_head(snake, direction):
    """Calculates the position of the new head based on current head and direction."""
    head_x, head_y = snake[0]
    dir_x, dir_y = direction
    new_head = (head_x + dir_x, head_y + dir_y)
    return new_head

def move_snake(snake, new_head, grows):
    """
    Updates the snake's body with the new head.
    If 'grows' is True, the snake grows; otherwise, the tail is removed.
    Returns the updated snake body.
    """
    new_snake = [new_head] + snake
    if not grows:
        new_snake.pop()
    return new_snake

def check_collision(snake, new_head):
    """
    Checks for collisions with walls or the snake's own body.
    Returns True if a collision occurs, False otherwise.
    """
    head_x, head_y = new_head

    # Wall collision
    if not (0 <= head_x < GRID_WIDTH and 0 <= head_y < GRID_HEIGHT):
        return True

    # Self-collision (start checking from the second segment as the new_head is already added temporarily)
    if new_head in snake:
        return True

    return False

def render_grid(snake, food):
    """Renders the game grid as a string."""
    grid = [[' ' for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    # Place snake
    for i, (x, y) in enumerate(snake):
        if i == 0:
            grid[y][x] = 'O' # Head
        else:
            grid[y][x] = 'o' # Body

    # Place food
    food_x, food_y = food
    grid[food_y][food_x] = '*'

    # Create string representation
    grid_str = ""
    grid_str += "+" + "-" * GRID_WIDTH + "+\n"
    for row in grid:
        grid_str += "|" + "".join(row) + "|\n"
    grid_str += "+" + "-" * GRID_WIDTH + "+"

    return grid_str

# Example of a simplified game loop function for demonstration, not part of core testable logic
def run_game_iteration(snake, food, direction):
    """
    Runs one iteration of the game, including movement, collision detection, and food eating.
    Returns new snake, new food, new direction, game_over status, and score_increase.
    """
    new_head = get_new_head(snake, direction)
    game_over = check_collision(snake, new_head)
    score_increase = 0

    if game_over:
        return snake, food, direction, True, 0

    grows = False
    if new_head == food:
        grows = True
        food = generate_food(snake + [new_head]) # Ensure new food is not on the growing snake
        score_increase = 1

    snake = move_snake(snake, new_head, grows)

    return snake, food, direction, False, score_increase
