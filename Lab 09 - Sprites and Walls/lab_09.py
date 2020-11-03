import random
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 50

MOVEMENT_SPEED = 5

NUMBER_OF_COINS = 100


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.player_list = None

        self.coin_list = None
        self.score = 0

        # Set up the player
        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None
        # Sound from kenney.nl
        self.coin_sound = arcade.load_sound("impactMetal_light_003.ogg")

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("sports_yellow.png", 1)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        for x in range(0, 1000, 100):
            for y in range(0, 1000, 32):
                # Randomly skip a box so the player can find a way through
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("block_04.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        # Create bottom edge
        for x in range(0, 1000, 30):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = x
            self.wall_list.append(wall)

        # Create left edge
        for y in range(0, 1000, 30):
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_y = y
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[0, 1000],
            [32, 1000],
            [64, 1000],
            [96, 1000],
            [128, 1000],
            [160, 1000],
            [192, 1000],
            [224, 1000],
            [256, 1000],
            [288, 1000],
            [320, 1000],
            [352, 1000],
            [384, 1000],
            [416, 1000],
            [448, 1000],
            [480, 1000],
            [512, 1000],
            [544, 1000],
            [576, 1000],
            [608, 1000],
            [640, 1000],
            [672, 1000],
            [704, 1000],
            [736, 1000],
            [768, 1000],
            [800, 1000],
            [832, 1000],
            [864, 1000],
            [896, 1000],
            [928, 1000],
            [960, 1000],
            [992, 1000]]

        # Loop through coordinates to create top edge
        for coordinate in coordinate_list:
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[1000, 0],
            [1000, 32],
            [1000, 64],
            [1000, 96],
            [1000, 128],
            [1000, 160],
            [1000, 192],
            [1000, 224],
            [1000, 256],
            [1000, 288],
            [1000, 320],
            [1000, 352],
            [1000, 384],
            [1000, 416],
            [1000, 448],
            [1000, 480],
            [1000, 512],
            [1000, 544],
            [1000, 576],
            [1000, 608],
            [1000, 640],
            [1000, 672],
            [1000, 704],
            [1000, 736],
            [1000, 768],
            [1000, 800],
            [1000, 832],
            [1000, 864],
            [1000, 896],
            [1000, 928],
            [1000, 960],
            [1000, 992]]

        # Loop through coordinates to create right edge
        for coordinate in coordinate_list:
            wall = arcade.Sprite("crate_01.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for i in range(NUMBER_OF_COINS):

            # Image from kenney.nl
            coin = arcade.Sprite("environment_12.png", .6)

            coin_placed_successfully = False

            while not coin_placed_successfully:
                coin.center_x = random.randrange(0, 1000)
                coin.center_y = random.randrange(0, 1000)

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 500, 500, arcade.color.BLACK, 36)

        if len(self.coin_list) == 0:
            output = f"Game over."
            arcade.draw_text(output, 500, 400, arcade.color.WHITE, 60)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        self.physics_engine.update()

        if len(self.coin_list) > 0:
            for coin in coin_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.coin_sound)

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
