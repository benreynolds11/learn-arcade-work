# Import the "arcade" library
import arcade

arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw grass
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.csscolor.GREEN)

# Draw the sun
arcade.draw_circle_filled(800, 600, 100, arcade.color.YELLOW)

# Draw the house
arcade.draw_lrtb_rectangle_filled(200, 600, 500, 125, arcade.color.DARK_BROWN)
arcade.draw_triangle_filled(625, 500, 175, 500, 400, 900, arcade.color.LIGHT_BROWN)

# Draw the door
arcade.draw_lrtb_rectangle_filled(350, 450, 225, 125, arcade.color.LIGHT_BROWN)
arcade.draw_line(400, 125, 400, 225, arcade.color.BLACK, 2)
arcade.draw_point(410, 175, arcade.color.BLACK, 10)
arcade.draw_point(390, 175, arcade.color.BLACK, 10)

# Draw the ellipse windows
arcade.draw_ellipse_filled(525, 250, 50, 100, arcade.color.WHITE, 3)
arcade.draw_ellipse_filled(275, 250, 50, 100, arcade.color.WHITE, 3)
arcade.draw_line(275, 200, 275, 300, arcade.color.BLACK, 2)
arcade.draw_line(250, 250, 300, 250, arcade.color.BLACK, 2)
arcade.draw_line(525, 200, 525, 300, arcade.color.BLACK, 2)
arcade.draw_line(500, 250, 550, 250, arcade.color.BLACK, 2)

# Draw the rectangle window
arcade.draw_lrtb_rectangle_filled(300, 500, 450, 350, arcade.color.WHITE)
arcade.draw_line(400, 350, 400, 450, arcade.color.BLACK, 3)
arcade.draw_line(300, 400, 500, 400, arcade.color.BLACK, 3)

# Draw the sidewalk
arcade.draw_lrtb_rectangle_filled(350, 450, 125, 0, arcade.color.GRAY)

# Finish drawing
arcade.finish_render()

# Keep window open until someone closes it
arcade.run()