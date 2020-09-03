# Import the "arcade" library
import arcade

arcade.open_window(600,600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.BLUE)

# Get ready to draw
arcade.start_render()




# Finish drawing
arcade.finish_render()

# Keep window open until someone closes it
arcade.run()