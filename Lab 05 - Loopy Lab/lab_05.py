import arcade

column_length = 10
row_length = 10
left_side = 5
bottom_side = 5

def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = column * column_length + left_side
            y = row * row_length + bottom_side
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = column * column_length + left_side + 300
            y = row * row_length + bottom_side

            if column % 2:
                print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK))
            else:
                print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))


def draw_section_3():
    for row in range(30):
        for column in range(30):
            x = column * column_length + left_side + 600
            y = row * row_length + bottom_side

            if row % 2:
                print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK))
            else:
                print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))

def draw_section_4():
    for row in range(30):
        for column in range(30):
            x = column * column_length + left_side + 900
            y = row * row_length + bottom_side

            if row % 2 and column % 2:
                print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))
            else:
                print(arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK))


def draw_section_5():
    for row in range(30):
        for column in range(row, 30):
            x = column * column_length + left_side
            y = row * row_length + bottom_side + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    for row in range(30):
        for column in range(30-row):
            x = column * column_length + left_side + 300
            y = row * row_length + bottom_side + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_7():
    for row in range(30):
        for column in range(1 + row):
            x = column * column_length + left_side + 600
            y = row * row_length + bottom_side + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    for row in range(30):
        for column in range(29 - row, 30):
            x = column * column_length + left_side + 900
            y = row * row_length + bottom_side + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
