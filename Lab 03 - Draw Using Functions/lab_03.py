import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_cloud(x, y):
    """draw a cloud"""
    arcade.draw_circle_filled(390 + x, 500 + y, 30, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(430 + x, 500 + y, 30, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(450 + x, 470 + y, 30, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(400 + x, 470 + y, 30, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(415 + x, 480 + y, 30, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(415 + x, 520 + y, 20, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(415 + x, 450 + y, 20, arcade.color.LIGHT_GRAY)


def draw_kite(x, y):
    """draw a kite"""
    arcade.draw_polygon_filled(((100 + x, 350 + y), (125 + x, 400 + y), (100 + x, 425 + y), (75 + x,400 + y)), arcade.color.RED)
    arcade.draw_line(100 + x, 350 + y, 100 + x, 425 + y, arcade.color.WHITE)
    arcade.draw_line(75 + x, 400 + y, 125 + x, 400 + y, arcade.color.WHITE)
    arcade.draw_line(100 + x, 350 + y, -800 + x, -800 + y, arcade.color.WHITE)


def draw_balloon(x, y):
    """draw a balloon"""
    arcade.draw_circle_filled(500 + x, 200 + y, 20, arcade.color.YELLOW)
    arcade.draw_line(500 + x, 180 + y, 537 + x, -600 + y, arcade.color.WHITE)
    arcade.draw_circle_filled(525 + x, 220 + y, 20, arcade.color.BLUE)
    arcade.draw_line(525 + x, 200 + y, 537 + x, -600 + y, arcade.color.WHITE)
    arcade.draw_circle_filled(550 + x, 220 + y, 20, arcade.color.RED)
    arcade.draw_line(550 + x, 200 + y, 537 + x, -600 + y, arcade.color.WHITE)
    arcade.draw_circle_filled(575 + x, 200 + y, 20, arcade.color.GREEN)
    arcade.draw_line(575 + x, 180 + y, 537 + x, -600 + y, arcade.color.WHITE)
    arcade.draw_circle_filled(515 + x, 190 + y, 20, arcade.color.PURPLE)
    arcade.draw_line(515 + x, 170 + y, 537 + x, -600 + y, arcade.color.WHITE)
    arcade.draw_circle_filled(545 + x, 190 + y, 20, arcade.color.ORANGE)
    arcade.draw_line(545 + x, 170 + y, 537 + x, -600 + y, arcade.color.WHITE)


def main():

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,"Lab 3 Picture Window")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

    draw_cloud(25, 50)
    draw_kite(15, 50)
    draw_balloon(30, 30)

    arcade.finish_render()
    arcade.run()

main()