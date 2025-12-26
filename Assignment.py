import tkinter as tk
import random


# -----------------------------------------------------
# CLASS: Player
# -----------------------------------------------------
class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 350
        self.y = 550
        self.speed = 10
        self.cooldown = False   # prevents shooting too fast

        # Player shape (triangle)
        self.id = canvas.create_polygon(
            self.x, self.y,
            self.x - 20, self.y + 30,
            self.x + 20, self.y + 30,
            fill="cyan"
        )

    def move_left(self, event=None):
        """Move player left."""
        if self.x > 30:
            self.x -= self.speed
            self.canvas.move(self.id, -self.speed, 0)

    def move_right(self, event=None):
        """Move player right."""
        if self.x < 670:
            self.x += self.speed
            self.canvas.move(self.id, self.speed, 0)

    def shoot(self):
        """Shoot a bullet if cooldown is not active."""
        if not self.cooldown:
            self.cooldown = True
            return Bullet(self.canvas, self.x, self.y - 10)

    def reset_cooldown(self):
        """Allow next shot."""
        self.cooldown = False


# -----------------------------------------------------
# CLASS: Bullet
# -----------------------------------------------------
class Bullet:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.speed = -8

        # bullet shape
        self.id = canvas.create_rectangle(
            x - 2, y - 10, x + 2, y,
            fill="yellow"
        )

    def move(self):
        """Move bullet upward."""
        self.canvas.move(self.id, 0, self.speed)
        self.y += self.speed

        # delete if above screen
        if self.y < 0:
            return False
        return True


# -----------------------------------------------------
# CLASS: Enemy
# -----------------------------------------------------
class Enemy:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y

        # enemy shape
        self.id = canvas.create_rectangle(
            x - 20, y - 20, x + 20, y + 20,
            fill="red"
        )

    def move(self, dx, dy):
        """Move enemy by dx, dy."""
        self.canvas.move(self.id, dx, dy)
        self.x += dx
        self.y += dy


# -----------------------------------------------------
# CLASS: Game
# -----------------------------------------------------
class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=700, height=600, bg="black")
        self.canvas.pack()

        self.running = True  # game state (false when game over)
        self.score = 0

        # display score
        self.score_text = self.canvas.create_text(
            100, 20, fill="white",
            font=("Arial", 16),
            text=f"Score: {self.score}"
        )

        self.player = Player(self.canvas)
        self.bullets = []
        self.enemies = []

        # enemy group movement
        self.enemy_direction = 1
        self.enemy_speed = 3

        self.create_enemy_rows()

        # keyboard
        root.bind("<Left>", self.player.move_left)
        root.bind("<Right>", self.player.move_right)
        root.bind("<space>", self.fire_bullet)

        self.update()

    def create_enemy_rows(self):
        """Create 15 enemies (5×3)."""
        start_x = 100
        start_y = 50
        spacing_x = 100
        spacing_y = 60

        for r in range(3):       # rows
            for c in range(5):   # columns
                x = start_x + c * spacing_x
                y = start_y + r * spacing_y
                enemy = Enemy(self.canvas, x, y)
                self.enemies.append(enemy)

    def fire_bullet(self, event=None):
        """Player fires a bullet."""
        bullet = self.player.shoot()
        if bullet:
            self.bullets.append(bullet)
            # reset cooldown after 250ms
            self.root.after(250, self.player.reset_cooldown)

    def move_enemies(self):
        """Classic Space Invaders movement."""
        move_down = False

        # Detect edge hit
        for enemy in self.enemies:
            if enemy.x >= 660 and self.enemy_direction == 1:
                move_down = True
            if enemy.x <= 40 and self.enemy_direction == -1:
                move_down = True

        # Move down + reverse direction
        if move_down:
            for enemy in self.enemies:
                enemy.move(0, 20)
            self.enemy_direction *= -1

        # Move horizontally
        for enemy in self.enemies:
            enemy.move(self.enemy_speed * self.enemy_direction, 0)

    def update(self):
        if not self.running:
            return  # stop updating

        # move bullets
        for bullet in self.bullets[:]:
            alive = bullet.move()
            if not alive:
                self.canvas.delete(bullet.id)
                self.bullets.remove(bullet)

        # move enemies
        self.move_enemies()

        # collisions
        self.handle_collisions()

        # check if enemies reached player
        for enemy in self.enemies:
            if enemy.y > 500:
                self.game_over("GAME OVER — Enemies Reached You!")
                return

        self.root.after(16, self.update)

    def handle_collisions(self):
        """Check bullet–enemy hits."""
        for enemy in self.enemies[:]:
            ex1, ey1, ex2, ey2 = self.canvas.coords(enemy.id)

            for bullet in self.bullets[:]:
                bx1, by1, bx2, by2 = self.canvas.coords(bullet.id)

                # hit detection
                if bx2 >= ex1 and bx1 <= ex2 and by2 >= ey1 and by1 <= ey2:
                    # delete objects
                    self.canvas.delete(enemy.id)
                    self.canvas.delete(bullet.id)

                    self.enemies.remove(enemy)
                    self.bullets.remove(bullet)

                    # update score
                    self.score += 100
                    self.canvas.itemconfig(
                        self.score_text, text=f"Score: {self.score}")

                    # make game harder
                    self.enemy_speed += 0.1

                    # win condition
                    if len(self.enemies) == 0:
                        self.game_over("YOU WIN!")
                    break

    def game_over(self, message):
        """Stop the game and show message."""
        self.running = False

        self.canvas.create_text(
            350, 300,
            fill="white",
            font=("Arial", 32),
            text=message
        )


# -----------------------------------------------------
# Run the game
# -----------------------------------------------------
root = tk.Tk()
root.title("Final Space Invaders Game")
game = Game(root)
root.mainloop()
