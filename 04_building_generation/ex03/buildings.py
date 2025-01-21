import random
from bk7084.math import *
from components import *


"""
This file contains the Skyscraper, Highrise, and Office classes.
These classes are used to generate buildings with different shapes and sizes.
The Skyscraper class is already implemented for you as an example.
You will need to implement the Highrise and Office classes yourself.

A building is made up of multiple components. Each component is a mesh. For
example, a skyscraper is made up of multiple floors, walls, and windows. Each
floor, wall, and window is a component. To generate a building, we need to
generate each component and place them in the correct position. 
 
But how do we place each component in the correct position? Of course, we can
place each component manually. But what if we want to translate the whole
building? We will need to translate each component individually. This is
tedious and error-prone.

Recall what we have learned in the hierarchy lecture, how do we construct the 
solar system? We parent each planet to the sun, and moon to each planet by 
multiplying the transformation of the parent right before the transformation
of the child. This way, all the children will be transformed correctly when
the parent is transformed.
 
We can do the same thing here. We can parent each component to a base 
component and only transform the base component. This way, all the children 
will be transformed correctly when the base component is transformed. This
time, we will use the app.spawn_building() function to spawn a base component
for us. The app.spawn_building() function will spawn a base component with
nothing in it. You can then parent other components to this base component.

Check out the `self.building` variable in the Skyscraper class. It is the base
component that we will use to parent other components. Go back to the main.py
file and you will see that we apply a transformation to the self.building
component. This transformation will be applied to all the children of the
self.building component. This is how we can translate the whole building.
"""


class Skyscraper:
    """A basic skyscraper class that procedurally generates
    a skyscraper given a number of floors and width.

    Args:
        app (bk.App):
            The app instance.
        num_floors (int):
            Number of floors to generate.
        max_width (float):
            The maximum width for each component.
    """
    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            # To place each floor higher than the previous one, we parent all
            # components to one 'base' component (floor1, see below). Then we
            # only have to move the base component up higher and the framework
            # takes care of the rest.
            floor1 = app.add_mesh(BasicFloor(max_width, max_width), parent=self.building)
            # Place the base component higher each time (i)
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor1.set_visible(True)
            floor2 = app.add_mesh(BasicFloor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)
            wall1 = app.add_mesh(BasicWindowWall(max_width, max_width), parent=floor1)
            wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            wall1.set_visible(True)
            wall2 = app.add_mesh(BasicWall(max_width, max_width), parent=floor1)
            wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            wall2.set_visible(True)
            wall3 = app.add_mesh(BasicWall(max_width, max_width), parent=floor1)
            wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            wall3.set_visible(True)
            wall4 = app.add_mesh(BasicWall(max_width, max_width), parent=floor1)
            wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            wall4.set_visible(True)

class MySkyscraperRandom:
    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        self.building = app.spawn_building()
        self.building.set_visible(True)
        last_anchor = self.building
        for i in range(self.num_floors):
            floor1 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=last_anchor)
            scale = random.normalvariate(0.93, 0.03)
            floor1.set_transform(Mat4.from_scale(Vec3(scale, scale, scale)) * Mat4.from_translation(Vec3(1, 0, 1)))
            floor1.set_visible(True)
            floor2 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)
            last_anchor = floor2
            wall1 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor1)
            wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            wall1.set_visible(True)
            wall2 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor1)
            wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            wall2.set_visible(True)
            wall3 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor1)
            wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            wall3.set_visible(True)
            wall4 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor1)
            wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            wall4.set_visible(True)
            
            floor3 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=last_anchor)
            floor3.set_transform(Mat4.from_scale(Vec3(scale, scale, scale)) * Mat4.from_translation(Vec3(-1, 0, -1)))
            floor3.set_visible(True)
            floor4 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=floor3)
            floor4.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor4.set_visible(True)

            last_anchor = floor4
            wall5 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor3)
            wall5.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            wall5.set_visible(True)
            wall6 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor3)
            wall6.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            wall6.set_visible(True)
            wall7 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor3)
            wall7.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            wall7.set_visible(True)
            wall8 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor3)
            wall8.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            wall8.set_visible(True)

class MySkyscraper:
    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        self.building = app.spawn_building()
        self.building.set_visible(True)
        last_anchor = self.building
        for i in range(self.num_floors):
            floor1 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=last_anchor)
            #scale = random.uniform(0.97, 0.999)
            #floor1.set_transform(Mat4.from_scale(Vec3(scale, scale, scale)) * Mat4.from_translation(Vec3(1, 0, 1)))
            floor1.set_transform(Mat4.from_translation(Vec3(1, 0, 1)))
            floor1.set_visible(True)
            floor2 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)
            last_anchor = floor2
            wall1 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor1)
            wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            wall1.set_visible(True)
            wall2 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor1)
            wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            wall2.set_visible(True)
            wall3 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor1)
            wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            wall3.set_visible(True)
            wall4 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor1)
            wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            wall4.set_visible(True)
            
            floor3 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=last_anchor)
            #floor3.set_transform(Mat4.from_scale(Vec3(scale, scale, scale)) * Mat4.from_translation(Vec3(-1, 0, -1)))
            floor3.set_transform(Mat4.from_translation(Vec3(-1, 0, -1)))
            floor3.set_visible(True)
            floor4 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=floor3)
            floor4.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor4.set_visible(True)

            last_anchor = floor4
            wall5 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor3)
            wall5.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            wall5.set_visible(True)
            wall6 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor3)
            wall6.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            wall6.set_visible(True)
            wall7 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor3)
            wall7.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            wall7.set_visible(True)
            wall8 = app.add_mesh(SkyscraperWall(max_width, max_width), parent=floor3)
            wall8.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            wall8.set_visible(True)         

class MySkyscraperGroundFloor:
    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            groundfloor1 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=self.building)
            groundfloor1.set_transform(Mat4.from_translation(Vec3(1, 2 * max_width * i, 1)))
            groundfloor1.set_visible(True)
            groundfloor2 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=groundfloor1)
            groundfloor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            groundfloor2.set_visible(True)
            groundwall1 = app.add_mesh(SkyscraperDoor(max_width, max_width), parent=groundfloor1)
            groundwall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            groundwall1.set_visible(True)
            groundwall2 = app.add_mesh(SkyscraperDoor(max_width, max_width), parent=groundfloor1)
            groundwall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            groundwall2.set_visible(True)
            groundwall3 = app.add_mesh(SkyscraperDoor(max_width, max_width), parent=groundfloor1)
            groundwall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            groundwall3.set_visible(True)
            groundwall4 = app.add_mesh(SkyscraperDoor(max_width, max_width), parent=groundfloor1)
            groundwall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            groundwall4.set_visible(True)


class Highrise:
    """A highrise class that procedurally generates
    a highrise building given a number of floors and width.

    Args:
        app (bk.App):
            The app instance.
        num_floors (int):
            Number of floors to generate.
        max_width (float):
            The maximum width for each component.
    """
    def __init__(self, app, num_floors, max_width):
        pass


class Office:
    """An office class that procedurally generates
    an office building given a number of floors and width.

    Args:
        app (bk.App):
            The app instance.
        num_floors (int):
            Number of floors to generate.
        max_width (float):
            The maximum width for each component.
    """
    def __init__(self, app: bk.App, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)

        base_floor = app.add_mesh(BasicFloor(max_width, max_width), parent=self.building)
        base_floor.set_visible(True)

        floor_height = max_width

        base_floor_2 = app.add_mesh(BasicFloor(max_width, max_width), parent=base_floor)
        base_floor_2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
        base_floor_2.set_visible(True)

        wall1 = app.add_mesh(GlassWindowEnterance(max_width, floor_height), parent=base_floor)
        wall1.set_transform(Mat4.from_translation(Vec3(0, floor_height / 2, max_width / 2)))
        wall1.set_visible(True)

        wall2 = app.add_mesh(GlassWindowWall(max_width, floor_height), parent=base_floor)
        wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, floor_height / 2, 0)) * Mat4.from_rotation_y(90, True))
        wall2.set_visible(True)

        wall3 = app.add_mesh(GlassWindowWall(max_width, floor_height), parent=base_floor)
        wall3.set_transform(Mat4.from_translation(Vec3(0, floor_height / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
        wall3.set_visible(True)

        wall4 = app.add_mesh(GlassWindowWall(max_width, floor_height), parent=base_floor)
        wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, floor_height / 2, 0)) * Mat4.from_rotation_y(-90, True))
        wall4.set_visible(True)

        last_anchor = base_floor_2

        for i in range(1, self.num_floors):
            # To place each floor higher than the previous one, we parent all
            # components to one 'base' component (floor1, see below). Then we
            # only have to move the base component up higher and the framework
            # takes care of the rest.
            floor1 = app.add_mesh(BasicFloor(max_width, max_width), parent=last_anchor)
            # Place the base component higher each time (i)
            # scale = random.normalvariate(0.93, 0.03)
            scale = random.uniform(0.8, 0.98)
            # scale = 1
            floor1.set_transform(
                Mat4.from_rotation_y(10 * np.pi / 180) *
                Mat4.from_scale(Vec3(scale, scale, scale)))
            floor1.set_visible(True)

            floor_height = max_width

            floor2 = app.add_mesh(BasicFloor(max_width, floor_height), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, floor_height, 0)))
            floor2.set_visible(True)

            last_anchor = floor2

            wall1 = app.add_mesh(GlassWindowWall(max_width, floor_height), parent=floor1)
            wall1.set_transform(Mat4.from_translation(Vec3(0, floor_height / 2, max_width / 2)))
            wall1.set_visible(True)

            wall2 = app.add_mesh(GlassWindowWall(max_width, floor_height), parent=floor1)
            wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, floor_height / 2, 0)) * Mat4.from_rotation_y(90, True))
            wall2.set_visible(True)

            wall3 = app.add_mesh(GlassWindowWall(max_width, floor_height), parent=floor1)
            wall3.set_transform(Mat4.from_translation(Vec3(0, floor_height / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            wall3.set_visible(True)

            wall4 = app.add_mesh(GlassWindowWall(max_width, floor_height), parent=floor1)
            wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, floor_height / 2, 0)) * Mat4.from_rotation_y(-90, True))
            wall4.set_visible(True)
        
        last_floor_base = last_anchor

        # wall1 = app.add_mesh(GlassWindowWall(max_width / 10, max_width / 5), parent=last_floor_base)
        # wall1.set_transform(Mat4.from_translation(Vec3(0, floor_height / 10, max_width / 2)))
        # wall1.set_visible(True)

        # wall2 = app.add_mesh(GlassWindowWall(max_width / 5, max_width / 10), parent=last_floor_base)
        # wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, floor_height / 10, 0)) * Mat4.from_rotation_y(90, True))
        # wall2.set_visible(True)

        # wall3 = app.add_mesh(GlassWindowWall(max_width / 10, max_width / 5), parent=last_floor_base)
        # wall3.set_transform(Mat4.from_translation(Vec3(0, floor_height / 10, -max_width/2)) * Mat4.from_rotation_y(180, True))
        # wall3.set_visible(True)

        # wall4 = app.add_mesh(GlassWindowWall(max_width / 5, max_width / 10), parent=last_floor_base)
        # wall4.set_transform(Mat4.from_translation(Vec3(-max_width/2, floor_height/10, 0)) * Mat4.from_rotation_y(-90, True))
        # wall4.set_visible(True)
