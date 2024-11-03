import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400  # Width and height of the game window
GRID_SIZE = 20  # Size of the grid cells
PLAYER_COLOR = (0, 255, 0)  # Color of the player (green)
COIN_COLOR = (255, 215, 0)  # Color of the coins (gold)
OBSTACLE_COLOR = (255, 0, 0)  # Color of the obstacles (red)

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")

# Player class
class Player:
    def __init__(self):
        self.position = [0, 0]  # Starting position of the player
        self.coins_collected = 0  # Count of coins collected

    def move(self, direction):
        if direction == "up" and self.position[1] > 0:
            self.position[1] -= GRID_SIZE
        elif direction == "down" and self.position[1] < HEIGHT - GRID_SIZE:
            self.position[1] += GRID_SIZE
        elif direction == "left" and self.position[0] > 0:
            self.position[0] -= GRID_SIZE
        elif direction == "right" and self.position[0] < WIDTH - GRID_SIZE:
            self.position[0] += GRID_SIZE

# Game loop
def main():
    player = Player()
    coins = [[random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                   random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE]
             for _ in range(5)]  # Generate 5 random coins
    obstacles = [[random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                   random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE]
                 for _ in range(2)]  # Generate 2 random obstacles

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.move("up")
        if keys[pygame.K_DOWN]:
            player.move("down")
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")

        # Check for coin collection
        if player.position in coins:
            coins.remove(player.position)
            player.coins_collected += 1
            print(f"Coins collected: {player.coins_collected}")

        # Drawing
        screen.fill((0, 0, 0))  # Clear the screen with black color
        pygame.draw.rect(screen, PLAYER_COLOR, (player.position[0], player.position[1], GRID_SIZE, GRID_SIZE))  # Draw player

        for coin in coins:
            pygame.draw.rect(screen, COIN_COLOR, (coin[0], coin[1], GRID_SIZE, GRID_SIZE))  # Draw coins

        for obstacle in obstacles:
            pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle[0], obstacle[1], GRID_SIZE, GRID_SIZE))  # Draw obstacles

        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__ == "__main__":
    main()