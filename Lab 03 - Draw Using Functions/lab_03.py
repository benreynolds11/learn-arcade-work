import arcade

arcade.open_window(800,600,"Lab 3 Picture Window")
arcade.set_background_color(arcade.color.LIGHT_BLUE)

arcade.start_render()

# Draw cloud
arcade.draw_circle_filled(390, 500, 30, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(430, 500, 30, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(450, 470, 30, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(400, 470, 30, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(415, 480, 30, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(415, 520, 20, arcade.color.LIGHT_GRAY)
arcade.draw_circle_filled(415, 450, 20, arcade.color.LIGHT_GRAY)

# Draw kite
arcade.draw_polygon_filled(((100, 350), (125, 400), (100, 425), (75,400)), arcade.color.RED)
arcade.draw_line(100, 350, 100, 425, arcade.color.WHITE)
arcade.draw_line(75, 400, 125, 400, arcade.color.WHITE)
arcade.draw_line(100, 350, 0, 0, arcade.color.WHITE)




arcade.finish_render()

arcade.run()