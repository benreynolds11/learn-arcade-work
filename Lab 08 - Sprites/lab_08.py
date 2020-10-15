import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.3
SPRITE_SCALING_COIN = .25
SPRITE_SCALING_WHEEL = .25
COIN_COUNT = 30
WHEEL_COUNT = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lab 8"


class Coin(arcade.Sprite):

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # Reset the coin to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class Wheel(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.wheel_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ORANGE_RED)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wheel_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            # Position the coins
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Create the wheels
        for i in range(WHEEL_COUNT):

            # Create the wheel instance
            # Wheel image from kenney.nl
            wheel = Wheel("platformPack_tile011.png", SPRITE_SCALING_WHEEL)

            # Position the wheels
            wheel.center_x = random.randrange(SCREEN_WIDTH)
            wheel.center_y = random.randrange(SCREEN_HEIGHT)
            wheel.change_x = random.randrange(-3, 4)
            wheel.change_y = random.randrange(-3, 4)

            # Add the wheel to the lists
            self.wheel_list.append(wheel)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.wheel_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.coin_list) == 0:
            arcade.draw_text("GAME OVER!", 100, 200, arcade.color.WHITE, 100)

    def on_mouse_motion(self, x, y, dx, dy):

        if len(self.coin_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.coin_list.update()

        if len(self.coin_list) > 0:
            self.wheel_list.update()

        # Generate a list of all sprites that collided with the player
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.wheel_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.wheel_list)
        for wheel in hit_list:
            wheel.remove_from_sprite_lists()
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()