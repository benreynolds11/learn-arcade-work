import arcade
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flappy Zombie"

MIN_HEIGHT = 50
GAP_SIZE = 120

# sounds and images from kenney.nl
SOUNDS = {'point': arcade.load_sound("impactMetal_light_003.ogg"),
          'die': arcade.load_sound("impactPlate_heavy_001.ogg")}
pipe = [arcade.Sprite("lollipopBase.png")]


class Pipe(arcade.Sprite):

    def __init__(self, image, scale=1):
        super().__init__(image, scale)
        self.horizontal_speed = -1.5

    def random_pipe(self, sprites, height):

        bottom_pipe = self(pipe)
        bottom_pipe.top = random.randrange(sprites['base'].height + MIN_HEIGHT, height - GAP_SIZE - MIN_HEIGHT)
        bottom_pipe.left = sprites['background'].width

        top_pipe = self(pipe)
        top_pipe.bottom = bottom_pipe.top + GAP_SIZE
        # top_pipe.bottom = random.randrange(bottom_pipe.top + MIN_GAP, height - MIN_HEIGHT)

        return bottom_pipe, top_pipe

    def update(self):
        self.center_x += self.horizontal_speed


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Sprite lists
        self.sprites = None
        self.zombie_list = None
        self.zombie_sprite = None
        self.pipe_sprites = None
        self.pipe_list = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):

        # Sprite Lists
        self.zombie_list = arcade.SpriteList()
        self.pipe_sprites = arcade.SpriteList()
        self.pipe_list = arcade.SpriteList()

        # Score
        self.score = 0

        self.zombie_sprite = arcade.Sprite("character_zombie_idle.png", 20)
        self.zombie_sprite.center_x = 50
        self.zombie_sprite.center_y = 50
        self.zombie_list.append(self.zombie_sprite)

        # Create the pipe
        start_pipe1 = Pipe(self.sprites, self.height)
        self.pipe_sprites.append(start_pipe1)

    def on_draw(self):

        arcade.start_render()
        self.zombie_list.draw()
        self.pipe_sprites.draw()

        # Draw the score
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.zombie_sprite.center_x = x
        self.zombie_sprite.center_y = y

    def on_update(self, delta_time):

        new_pipe = None

        # Remove pipe that is no longer on the screen
        for pipe in self.pipe_sprites:
            if pipe.right <= 0:
                pipe.kill()
            elif len(self.pipe_sprites) == 2 and pipe.right <= random.randrange(self.width // 2, self.width // 2 + 15):
                new_pipe = True

            if new_pipe:
                self.pipe_sprites.append(new_pipe)

            self.zombie_list.update()
            self.pipe_sprites.update()

            if self.zombie.center_x >= self.pipe_sprites[0].center_x and not self.pipe_sprites[0].scored:
                arcade.play_sound(SOUNDS['point'])
                self.score += 1
            self.pipe_sprites[0].scored = True
            self.pipe_sprites[1].scored = True
            print(self.score)

            hit = arcade.check_for_collision_with_list(self.zombie, self.pipe_sprites)

            if any(hit):
                output = f"Game Over"
                arcade.draw_text(output, 500, 400, arcade.color.WHITE, 60)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
