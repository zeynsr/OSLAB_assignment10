import arcade

arcade.open_window(625,625, "ComplexLoops-BOX")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * 25 + 100
        y = row * 25+ 100
        if (row+column)%2==0:
            arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.BRILLIANT_ROSE,45)
        else:
            arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.DARK_BLUE_GRAY,45)

arcade.finish_render()
arcade.run()