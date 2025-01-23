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

class MySkyscraperDubai:
    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        self.building = app.spawn_building()
        self.building.set_visible(True)

        self.init_corner(app, int(num_floors * 14 / 46), max_width, Vec3(-4, 0, -4))
        self.init_left(app, num_floors, max_width / 3, Vec3(-3, 0, 0))
        self.init_right(app, int(num_floors * 44 / 46), max_width / 3, Vec3(0, 0, -3))
        self.init_left(app, int(num_floors * 40 / 46), max_width / 3, Vec3(-3, 0, 2))
        self.init_right(app, int(num_floors * 38 / 46), max_width / 3, Vec3(2, 0, -3))
        self.init_left(app, int(num_floors * 34 / 46), max_width / 3, Vec3(-3, 0, 4))
        self.init_right(app, int(num_floors * 32 / 46), max_width / 3, Vec3(4, 0, -3))
        self.init_left(app, int(num_floors * 28 / 46), max_width / 3, Vec3(-3, 0, 6))
        self.init_right(app, int(num_floors * 24 / 46), max_width / 3, Vec3(6, 0, -3))
        self.init_left(app, int(num_floors * 22 / 46), max_width / 3, Vec3(-3, 0, 8))
        self.init_right(app, int(num_floors * 18 / 46), max_width / 3, Vec3(8, 0, -3))
        self.init_left(app, int(num_floors * 14 / 46), max_width / 3, Vec3(-3, 0, 10))
        self.init_right(app, int(num_floors * 11 / 46), max_width / 3, Vec3(10, 0, -3))
        self.init_left(app, int(num_floors * 9 / 46), max_width / 3, Vec3(-3, 0, 12))
        self.init_right(app, int(num_floors * 6 / 46), max_width / 3, Vec3(12, 0, -3))
        self.init_corner(app, int(num_floors * 2 / 46), max_width, Vec3(2, 0, 2))

    def init_right(self, app, num_floors, max_width, translation: Vec3):
        translation_transform = Mat4.from_translation(translation)
        for i in range(num_floors):
            if i == 4 or i == 10 or i == 16 or i == 22 or i == 28 or i == 34:
                floorright1 = app.add_mesh(SkyscraperFloorRight(max_width, max_width), parent=self.building)
                floorright1.set_transform(translation_transform * Mat4.from_translation(Vec3(0, 0, 0)))
                floorright1.set_visible(True)
                floorright2 = app.add_mesh(SkyscraperFloorRight(max_width, max_width), parent=floorright1)
                floorright2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                floorright2.set_visible(True)
                #last_anchor = floorright2
                translation_transform = translation_transform * Mat4.from_translation(Vec3(0, max_width, 0))
                wall1 = app.add_mesh(SkyscraperWallSmallConcrete(max_width, max_width), parent=floorright1)
                wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width)))
                wall1.set_visible(True)
                wall2 = app.add_mesh(SkyscraperWallWideConcrete(max_width, max_width), parent=floorright1)
                wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                wall2.set_visible(True)
                wall3 = app.add_mesh(SkyscraperWallSmallConcrete(max_width, max_width), parent=floorright1)
                wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width)) * Mat4.from_rotation_y(180, True))
                wall3.set_visible(True)
                wall4 = app.add_mesh(SkyscraperWallWideConcrete(max_width, max_width), parent=floorright1)
                wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                wall4.set_visible(True)  
            else:
                floorright1 = app.add_mesh(SkyscraperFloorRight(max_width, max_width), parent=self.building)
                floorright1.set_transform(translation_transform * Mat4.from_translation(Vec3(0, 0, 0)))
                floorright1.set_visible(True)
                floorright2 = app.add_mesh(SkyscraperFloorRight(max_width, max_width), parent=floorright1)
                floorright2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                floorright2.set_visible(True)
                translation_transform = translation_transform * Mat4.from_translation(Vec3(0, max_width, 0))
                wall1 = app.add_mesh(SkyscraperWallSmall(max_width, max_width), parent=floorright1)
                wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width)))
                wall1.set_visible(True)
                wall2 = app.add_mesh(SkyscraperWallWide(max_width, max_width), parent=floorright1)
                wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                wall2.set_visible(True)
                wall3 = app.add_mesh(SkyscraperWallSmall(max_width, max_width), parent=floorright1)
                wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width)) * Mat4.from_rotation_y(180, True))
                wall3.set_visible(True)
                wall4 = app.add_mesh(SkyscraperWallWide(max_width, max_width), parent=floorright1)
                wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                wall4.set_visible(True)

    def init_left(self, app, num_floors, max_width, translation: Vec3):
        translation_transform = Mat4.from_translation(translation)
        for i in range(num_floors):
            if i == 4 or i == 10 or i == 16 or i == 22 or i == 28 or i == 34:
                floorleft1 = app.add_mesh(SkyscraperFloorLeft(max_width, max_width), parent=self.building)
                floorleft1.set_transform(translation_transform * Mat4.from_translation(Vec3(0, 0, 0)))
                floorleft1.set_visible(True)
                floorleft2 = app.add_mesh(SkyscraperFloorLeft(max_width, max_width), parent=floorleft1)
                floorleft2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                floorleft2.set_visible(True)
                translation_transform = translation_transform * Mat4.from_translation(Vec3(0, max_width, 0))
                wall1 = app.add_mesh(SkyscraperWallWideConcrete(max_width, max_width), parent=floorleft1)
                wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
                wall1.set_visible(True)
                wall2 = app.add_mesh(SkyscraperWallSmallConcrete(max_width, max_width), parent=floorleft1)
                wall2.set_transform(Mat4.from_translation(Vec3(max_width, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                wall2.set_visible(True)
                wall3 = app.add_mesh(SkyscraperWallWideConcrete(max_width, max_width), parent=floorleft1)
                wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
                wall3.set_visible(True)
                wall4 = app.add_mesh(SkyscraperWallSmallConcrete(max_width, max_width), parent=floorleft1)
                wall4.set_transform(Mat4.from_translation(Vec3(-max_width, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                wall4.set_visible(True) 
            else:
                floorleft1 = app.add_mesh(SkyscraperFloorLeft(max_width, max_width), parent=self.building)
                floorleft1.set_transform(translation_transform * Mat4.from_translation(Vec3(0, 0, 0)))
                floorleft1.set_visible(True)
                floorleft2 = app.add_mesh(SkyscraperFloorLeft(max_width, max_width), parent=floorleft1)
                floorleft2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                floorleft2.set_visible(True)
                translation_transform = translation_transform * Mat4.from_translation(Vec3(0, max_width, 0))
                wall1 = app.add_mesh(SkyscraperWallWide(max_width, max_width), parent=floorleft1)
                wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
                wall1.set_visible(True)
                wall2 = app.add_mesh(SkyscraperWallSmall(max_width, max_width), parent=floorleft1)
                wall2.set_transform(Mat4.from_translation(Vec3(max_width, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                wall2.set_visible(True)
                wall3 = app.add_mesh(SkyscraperWallWide(max_width, max_width), parent=floorleft1)
                wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
                wall3.set_visible(True)
                wall4 = app.add_mesh(SkyscraperWallSmall(max_width, max_width), parent=floorleft1)
                wall4.set_transform(Mat4.from_translation(Vec3(-max_width, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                wall4.set_visible(True)

    def init_corner(self, app, num_floors, max_width, translation: Vec3):
        translation_transform = Mat4.from_translation(translation)
        for i in range(num_floors):
            if i == 0:
                floor1 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=self.building)
                floor1.set_transform(translation_transform * Mat4.from_translation(Vec3(0, 0, 0)))
                floor1.set_visible(True)
                floor2 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=floor1)
                floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                floor2.set_visible(True)
                translation_transform = translation_transform * Mat4.from_translation(Vec3(0, max_width, 0))
                wall1 = app.add_mesh(SkyscraperDoor(max_width, max_width), parent=floor1)
                wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
                wall1.set_visible(True)
                wall2 = app.add_mesh(SkyscraperDoor(max_width, max_width), parent=floor1)
                wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                wall2.set_visible(True)
                wall3 = app.add_mesh(SkyscraperDoor(max_width, max_width), parent=floor1)
                wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
                wall3.set_visible(True)
                wall4 = app.add_mesh(SkyscraperDoor(max_width, max_width), parent=floor1)
                wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                wall4.set_visible(True)  
            else:
                floor1 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=self.building)
                floor1.set_transform(translation_transform * Mat4.from_translation(Vec3(0, 0, 0)))
                floor1.set_visible(True)
                floor2 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=floor1)
                floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
                floor2.set_visible(True)
                translation_transform = translation_transform * Mat4.from_translation(Vec3(0, max_width, 0))
                wall1 = app.add_mesh(SkyscraperWallConcrete(max_width, max_width), parent=floor1)
                wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
                wall1.set_visible(True)
                wall2 = app.add_mesh(SkyscraperWallConcrete(max_width, max_width), parent=floor1)
                wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                wall2.set_visible(True)
                wall3 = app.add_mesh(SkyscraperWallConcrete(max_width, max_width), parent=floor1)
                wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
                wall3.set_visible(True)
                wall4 = app.add_mesh(SkyscraperWallConcrete(max_width, max_width), parent=floor1)
                wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                wall4.set_visible(True)  


class MySkyscraper:
    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        self.building = app.spawn_building()
        self.building.set_visible(True)

        self.init_skyscraper(app, num_floors, max_width, Vec3(0, 0, 0))
        self.init_skyscraper(app, int(num_floors * 14 / 15), max_width, Vec3(0, 0, 3))
        self.init_skyscraper(app, int(num_floors * 14 / 15), max_width, Vec3(3, 0, 0))
        self.init_skyscraper(app, int(num_floors * 13 / 15), max_width, Vec3(0, 0, 6))
        self.init_skyscraper(app, int(num_floors * 13 / 15), max_width, Vec3(6, 0, 0))
        self.init_skyscraper(app, int(num_floors * 13 / 15), max_width, Vec3(3, 0, 3))


    def init_skyscraper(self, app, num_floors, max_width, translation: Vec3):
        translation_transform = Mat4.from_translation(translation)
        for i in range(num_floors):
            floor1 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=self.building)
            floor1.set_transform(translation_transform * Mat4.from_translation(Vec3(0.5, 0, 0.5)))
            floor1.set_visible(True)
            floor2 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)
            translation_transform = translation_transform * Mat4.from_translation(Vec3(0, max_width, 0))
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
            
            floor3 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=self.building)
            floor3.set_transform(translation_transform * Mat4.from_translation(Vec3(-0.5, 0, -0.5)))
            floor3.set_visible(True)
            floor4 = app.add_mesh(SkyscraperFloor(max_width, max_width), parent=floor3)
            floor4.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor4.set_visible(True)
            translation_transform = translation_transform * Mat4.from_translation(Vec3(0, max_width, 0))
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
            floor1 = app.add_mesh(
                BasicFloor(max_width, max_width), parent=self.building
            )
            # Place the base component higher each time (i)
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor1.set_visible(True)
            floor2 = app.add_mesh(BasicFloor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)
            wall1 = app.add_mesh(BasicWindowWall(max_width, max_width), parent=floor1)
            wall1.set_transform(
                Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2))
            )
            wall1.set_visible(True)
            wall2 = app.add_mesh(BasicWall(max_width, max_width), parent=floor1)
            wall2.set_transform(
                Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0))
                * Mat4.from_rotation_y(90, True)
            )
            wall2.set_visible(True)
            wall3 = app.add_mesh(BasicWall(max_width, max_width), parent=floor1)
            wall3.set_transform(
                Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2))
                * Mat4.from_rotation_y(180, True)
            )
            wall3.set_visible(True)
            wall4 = app.add_mesh(BasicWall(max_width, max_width), parent=floor1)
            wall4.set_transform(
                Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0))
                * Mat4.from_rotation_y(-90, True)
            )
            wall4.set_visible(True)

class HighriseTaipei:
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
        self.num_floors = num_floors
        self.max_width = max_width
        self.building = app.spawn_building()  # Assuming a building object is spawned in the app
        self.building.set_visible(True)

        R = max(max_width,max_width) / 2
        r= (R * math.sqrt(3)) / 2
        
        # Loop to create each floor and its components
        for i in range(self.num_floors):
            # Hexagonal floor for this level
            if i == 1:
                floor1 = app.add_mesh(HighriseFloor(max_width, max_width), parent=self.building)
                floor1.set_transform( Mat4.from_scale(Vec3( 0.9, 1 , 0.9)) *Mat4.from_translation(Vec3(0, max_width * i, 0)))
                floor1.set_visible(True)

                floor2 = app.add_mesh(HighriseFloor(max_width, max_width), parent=floor1)
                floor2.set_transform(Mat4.from_scale(Vec3( 0.9, 1 , 0.9)) * Mat4.from_translation(Vec3(0, max_width, 0)))
                floor2.set_visible(True)
                groundfloorwall1 = app.add_mesh(SlantedWall(max_width, max_width), parent=floor1)
                groundfloorwall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
                groundfloorwall1.set_visible(True)
                groundfloorwall2 = app.add_mesh(SlantedWall(max_width, max_width), parent=floor1)
                groundfloorwall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                groundfloorwall2.set_visible(True)
                groundfloorwall3 = app.add_mesh(SlantedWall(max_width, max_width), parent=floor1)
                groundfloorwall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
                groundfloorwall3.set_visible(True)
                groundfloorwall4 = app.add_mesh(SlantedWall(max_width, max_width), parent=floor1)
                groundfloorwall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                groundfloorwall4.set_visible(True)

            elif i == 0:
                floor1 = app.add_mesh(HighriseFloor(max_width, max_width), parent=self.building)
                floor1.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
                floor1.set_visible(True)

                floor2 = app.add_mesh(HighriseFloor(max_width, max_width), parent=floor1)
                floor2.set_transform(Mat4.from_scale(Vec3( 0.9, 1 , 0.9)) * Mat4.from_translation(Vec3(0, max_width, 0)))
                floor2.set_visible(True)
                groundfloorwall5 = app.add_mesh(SlantedGlassDoorWall(max_width, max_width), parent=floor1)
                groundfloorwall5.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
                groundfloorwall5.set_visible(True)
                groundfloorwall6 = app.add_mesh(SlantedWall(max_width, max_width), parent=floor1)
                groundfloorwall6.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
                groundfloorwall6.set_visible(True)
                groundfloorwall7 = app.add_mesh(SlantedWall(max_width, max_width), parent=floor1)
                groundfloorwall7.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
                groundfloorwall7.set_visible(True)
                groundfloorwall8 = app.add_mesh(SlantedWall(max_width, max_width), parent=floor1)
                groundfloorwall8.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
                groundfloorwall8.set_visible(True)

            else:
                floor = app.add_mesh(BasicHexagonRoof( max_width,  max_width), parent=self.building)
                floor.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
                floor.set_visible(True)
            
                # Hexagonal roof for this level (it will be placed one level higher)
                roof = app.add_mesh(BasicHexagonRoof( max_width, max_width), parent=floor)
                roof.set_transform(Mat4.from_scale(Vec3( 1.2, 1 , 1.2)) * Mat4.from_translation(Vec3(0, max_width, 0)))  # Move roof up by max_width
                roof.set_visible(True)

                
                # Create 6 walls for the hexagonal building
                for j in range(6):
                # Calculate the angle for each wall (since there are 6 walls in a hexagon)
                    angle = math.radians(60 * j +30)  # 60 degrees per side

                # Calculate the position of each wall (at the midpoint of the hexagon side)
                    x_position = r * math.cos(angle)  # Position along X axis
                    z_position = r * math.sin(angle)  # Position along Z axis

                # Create the wall with the calculated max width (side length of the hexagon)
                    wall = app.add_mesh(SlantedRectangleWall(max_width, max_width), parent=floor)
                # Position the wall at the correct position (on the side of the hexagon)
                    wall.set_transform(
                    Mat4.from_translation(Vec3(x_position, max_width/2, z_position)) * Mat4.from_rotation_y(60-60*j, True)
                 )
                    wall.set_visible(True)
                    # Add the antenna on the top of the building
        self._add_antenna(app)

    def _add_antenna(self, app):
        """Adds a detailed antenna to the top of the building."""
        
        antenna_base = app.add_mesh(HighriseFloor(self.max_width, self.max_width), parent=self.building)
        antenna_base.set_transform(Mat4.from_scale(Vec3(0.2,1,0.2)) *Mat4.from_translation(Vec3(0, self.num_floors * self.max_width, 0)))
        antenna_base.set_visible(True)

        antenna_base2 = app.add_mesh(HighriseFloor(self.max_width, self.max_width), parent=antenna_base)
        antenna_base2.set_transform(Mat4.from_scale(Vec3(1,0.4,1)) *Mat4.from_translation(Vec3(0, self.max_width, 0)))
        antenna_base2.set_visible(True)
        Antennabox1 = app.add_mesh(Antennabox(self.max_width, self.max_width), parent=antenna_base)
        Antennabox1.set_transform(Mat4.from_scale(Vec3(1,0.4,1)) *Mat4.from_translation(Vec3(0, self.max_width / 2, self.max_width / 2)))
        Antennabox1.set_visible(True)
        Antennabox2 = app.add_mesh(Antennabox(self.max_width, self.max_width), parent=antenna_base)
        Antennabox2.set_transform(Mat4.from_scale(Vec3(1,0.4,1)) *Mat4.from_translation(Vec3(self.max_width / 2, self.max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
        Antennabox2.set_visible(True)
        Antennabox3 = app.add_mesh(Antennabox(self.max_width, self.max_width), parent=antenna_base)
        Antennabox3.set_transform(Mat4.from_scale(Vec3(1,0.4,1)) *Mat4.from_translation(Vec3(0, self.max_width / 2, -self.max_width / 2)) * Mat4.from_rotation_y(180, True))
        Antennabox3.set_visible(True)
        Antennabox4 = app.add_mesh(Antennabox(self.max_width, self.max_width), parent=antenna_base)
        Antennabox4.set_transform(Mat4.from_scale(Vec3(1,0.4,1)) *Mat4.from_translation(Vec3(-self.max_width / 2, self.max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
        Antennabox4.set_visible(True)
        for i in range(3):
            angle = math.radians(120 * i)
            pole = app.add_mesh(Antennapole(self.max_width , self.max_width ), parent= antenna_base2)
            pole.set_transform(Mat4.from_scale(Vec3(1,2,1)) *
                Mat4.from_translation(Vec3(
                    (math.sqrt(3) *self.max_width / 6) * math.cos(angle),
                    self.max_width / 2,
                    (math.sqrt(3) *self.max_width / 6) * math.sin(angle)
                )) * Mat4.from_rotation_y(90 -120 * i, True)
            )
            pole.set_visible(True)

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


office_floor_model = bk.Mesh.load_from(bk.res_path("./assets/office_floor.obj"))
office_base_model = bk.Mesh.load_from(bk.res_path("./assets/office_base.obj"))
office_roof_model = bk.Mesh.load_from(bk.res_path("./assets/office_roof.obj"))


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

    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        self.building = app.spawn_building()
        self.building.set_visible(True)
        self.pre_transform = (
                Mat4.from_translation(Vec3(0, 1.4, 0))
                * Mat4.from_scale(Vec3(0.5))
        )
        base = app.add_mesh(office_base_model, parent=self.building)
        base_height = 2.0
        base.set_visible(True)
        for i in range(1, self.num_floors-1):
            floor = app.add_mesh(office_floor_model, parent=base)
            floor.set_transform(Mat4.from_translation(Vec3(0, 3 * i + base_height, 0)))
            floor.set_visible(True)
        roof = app.add_mesh(office_roof_model, parent=base)
        roof.set_visible(True)
        roof.set_transform(Mat4.from_translation(Vec3(0, 3 * (self.num_floors-1) + base_height, 0)))


# pre-loaded park model
park_model = bk.Mesh.load_from(bk.res_path("./assets/park.obj"))


class Park:
    def __init__(self, app):
        self.building = app.add_mesh(park_model)
        self.building.set_visible(True)
        angle = random.randint(0, 3) * 90
        self.pre_transform = (
            Mat4.from_translation(Vec3(0, 1.4, 0))
            * Mat4.from_scale(Vec3(0.5))
            * Mat4.from_rotation_y(angle, True)
        )


# pre-loaded house model
house_model = bk.Mesh.load_from(bk.res_path("./assets/house.obj"))


class House:
    def __init__(self, app):
        self.building = app.add_mesh(house_model)
        self.building.set_visible(True)
        angle = random.randint(0, 3) * 90
        self.pre_transform = (
            Mat4.from_scale(Vec3(0.5))
            * Mat4.from_translation(Vec3(0, 6.8, 0))
            * Mat4.from_rotation_y(angle, True)
        )

class EWI:
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
        if num_floors % 2 == 0:
            raise ValueError("Number of floors must be odd")

        self.num_floors = num_floors
        # Spawn the building and save the reference to the building
        self.building = app.spawn_building()
        self.building.set_visible(True)

        p = PerlinNoise(octaves=3, seed=random.randint(0, 1000000))

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

        hexcount = 30
        hexscale = max_width / (3 * hexcount - 1)
        hexscalem = Mat4.from_scale(Vec3(hexscale, hexscale, hexscale))
        d = hexscale * np.sqrt(3) / 2
        pdc = 10
        ewi_inside_ratio = 0.7
        ewi_inside_height = 0.03 * max_width
        ewi_outside_height = 0.05 * max_width

        for hxi in range(hexcount-1):
            hexall = app.add_mesh(HexallHigher(), parent=last_anchor)
            hexall.set_transform(Mat4.from_translation(Vec3(-max_width / 2 + 2.5 * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale), 0, max_width / 2)) * hexscalem)
            hexall.set_visible(True)
        for hxi in range(hexcount-1):
            hexall = app.add_mesh(HexallHigher(), parent=last_anchor)
            hexall.set_transform(Mat4.from_translation(Vec3(-max_width / 2 + 2.5 * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale), 0, -max_width / 2)) * Mat4.from_rotation_y(180, True) * hexscalem)
            hexall.set_visible(True)
        for hxi in range(hexcount-1):
            hexall = app.add_mesh(HexallHigher(), parent=last_anchor)
            hexall.set_transform(Mat4.from_translation(Vec3(max_width / 2, 0, -max_width / 2 + 2.5 * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale)))* Mat4.from_rotation_y(90, True) * hexscalem)
            hexall.set_visible(True)
        for hxi in range(hexcount-1):
            hexall = app.add_mesh(HexallHigher(), parent=last_anchor)
            hexall.set_transform(Mat4.from_translation(Vec3(-max_width / 2, 0, -max_width / 2 + 2.5 * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale))) * Mat4.from_rotation_y(270, True) * hexscalem)
            hexall.set_visible(True)

        for i in range(self.num_floors):
            if i % 2 == 0:
                run_cnt = hexcount
                sclcoef = 1
            else:
                run_cnt = hexcount - 1
                sclcoef = 2.5

            cy = d * i

            for hxi in range(run_cnt):
                hexall = app.add_mesh(Hexall(), parent=last_anchor)
                cx = -max_width / 2 + sclcoef * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale)
                pd = np.abs(p.noise((cx, cy, max_width / 2)))
                hexall.set_transform(Mat4.from_translation(Vec3(cx, d, max_width / 2 - pd * max_width / pdc)) * hexscalem)
                hexall.set_visible(True)

                hexall_inside = app.add_mesh(HexallInside(), parent=hexall)
                hexall_inside.set_transform(Mat4.from_scale(Vec3(1, 1, 3)))
                hexall_inside.set_visible(True)
            for hxi in range(run_cnt):
                hexall = app.add_mesh(Hexall(), parent=last_anchor)
                cx = -max_width / 2 + sclcoef * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale)
                pd = np.abs(p.noise((cx, cy, -max_width / 2)))
                hexall.set_transform(Mat4.from_translation(Vec3(cx, d, -max_width / 2 + pd * max_width / pdc)) * Mat4.from_rotation_y(180, True) * hexscalem)
                hexall.set_visible(True)

                hexall_inside = app.add_mesh(HexallInside(), parent=hexall)
                hexall_inside.set_transform(Mat4.from_scale(Vec3(1, 1, 3)))
                hexall_inside.set_visible(True)
            for hxi in range(run_cnt):
                hexall = app.add_mesh(Hexall(), parent=last_anchor)
                cz = -max_width / 2 + sclcoef * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale)
                pd = np.abs(p.noise((max_width / 2, cy, cz)))
                hexall.set_transform(Mat4.from_translation(Vec3(max_width / 2 - pd * max_width / pdc, d, cz)) * Mat4.from_rotation_y(90, True) * hexscalem)
                hexall.set_visible(True)

                hexall_inside = app.add_mesh(HexallInside(), parent=hexall)
                hexall_inside.set_transform(Mat4.from_scale(Vec3(1, 1, 3)))
                hexall_inside.set_visible(True)
            for hxi in range(run_cnt):
                hexall = app.add_mesh(Hexall(), parent=last_anchor)
                cz = -max_width / 2 + sclcoef * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale)
                pd = np.abs(p.noise((-max_width / 2, cy, cz)))
                hexall.set_transform(Mat4.from_translation(Vec3(-max_width / 2 + pd * max_width / pdc, d, cz)) * Mat4.from_rotation_y(270, True) * hexscalem)
                hexall.set_visible(True)

                hexall_inside = app.add_mesh(HexallInside(), parent=hexall)
                hexall_inside.set_transform(Mat4.from_scale(Vec3(1, 1, 3)))
                hexall_inside.set_visible(True)
            floor1 = app.add_mesh(BasicFloor(max_width, max_width), parent=last_anchor)
            floor1.set_transform(Mat4.from_translation(Vec3(0, 0, 0)))
            # floor1.set_visible(True)

            floor2 = app.add_mesh(BasicFloor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, d, 0)))
            # floor2.set_visible(True)

            last_anchor = floor2
        for hxi in range(hexcount-1):
            hexall = app.add_mesh(HexallLower(), parent=last_anchor)
            hexall.set_transform(Mat4.from_translation(Vec3(-max_width / 2 + 2.5 * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale), d, max_width / 2)) * hexscalem)
            hexall.set_visible(True)
        for hxi in range(hexcount-1):
            hexall = app.add_mesh(HexallLower(), parent=last_anchor)
            hexall.set_transform(Mat4.from_translation(Vec3(-max_width / 2 + 2.5 * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale), d, -max_width / 2)) * Mat4.from_rotation_y(180, True) * hexscalem)
            hexall.set_visible(True)
        for hxi in range(hexcount-1):
            hexall = app.add_mesh(HexallLower(), parent=last_anchor)
            hexall.set_transform(Mat4.from_translation(Vec3(max_width / 2, d, -max_width / 2 + 2.5 * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale)))* Mat4.from_rotation_y(90, True) * hexscalem)
            hexall.set_visible(True)
        for hxi in range(hexcount-1):
            hexall = app.add_mesh(HexallLower(), parent=last_anchor)
            hexall.set_transform(Mat4.from_translation(Vec3(-max_width / 2, d, -max_width / 2 + 2.5 * hexscale + hxi / (hexcount - 1) * (max_width - 2 * hexscale))) * Mat4.from_rotation_y(270, True) * hexscalem)
            hexall.set_visible(True)
        

        floor1 = app.add_mesh(EWIRooftop(max_width, max_width), parent=last_anchor)
        floor1.set_transform(Mat4.from_translation(Vec3(0, 0, 0)) * Mat4.from_scale(Vec3(ewi_inside_ratio, 1, ewi_inside_ratio)))
        floor1.set_visible(True)

        last_anchor = floor1

        for i in range(10):
            w1 = app.add_mesh(EWITopInside(), parent=last_anchor)
            w1.set_transform(Mat4.from_translation(Vec3(0, ewi_inside_height / 2, max_width / 2)) * Mat4.from_scale(Vec3(max_width, ewi_inside_height, 1)))
            w1.set_visible(True)

            w2 = app.add_mesh(EWITopInside(), parent=last_anchor)
            w2.set_transform(Mat4.from_translation(Vec3(max_width / 2, ewi_inside_height / 2, 0)) * Mat4.from_rotation_y(90, True) * Mat4.from_scale(Vec3(max_width, ewi_inside_height, 1)))
            w2.set_visible(True)

            w3 = app.add_mesh(EWITopInside(), parent=last_anchor)
            w3.set_transform(Mat4.from_translation(Vec3(0, ewi_inside_height / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True) * Mat4.from_scale(Vec3(max_width, ewi_inside_height, 1)))
            w3.set_visible(True)

            w4 = app.add_mesh(EWITopInside(), parent=last_anchor)
            w4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, ewi_inside_height / 2, 0)) * Mat4.from_rotation_y(-90, True) * Mat4.from_scale(Vec3(max_width, ewi_inside_height, 1)))
            w4.set_visible(True)

            floor2 = app.add_mesh(EWIRooftop(max_width, max_width), parent=last_anchor)
            floor2.set_transform(Mat4.from_translation(Vec3(0, ewi_inside_height, 0)))
            floor2.set_visible(True)

            last_anchor = floor2
        
        floor1 = app.add_mesh(EWIRooftop(max_width, max_width), parent=last_anchor)
        floor1.set_transform(Mat4.from_scale(Vec3(1 / ewi_inside_ratio, 1, 1 / ewi_inside_ratio)))
        floor1.set_visible(True)
        last_anchor = floor1

        for i in range(10):
            w1 = app.add_mesh(EWITopOutside(), parent=last_anchor)
            w1.set_transform(Mat4.from_translation(Vec3(0, ewi_outside_height / 2, max_width / 2)) * Mat4.from_scale(Vec3(max_width, ewi_outside_height, 1)))
            w1.set_visible(True)

            w2 = app.add_mesh(EWITopOutside(), parent=last_anchor)
            w2.set_transform(Mat4.from_translation(Vec3(max_width / 2, ewi_outside_height / 2, 0)) * Mat4.from_rotation_y(90, True) * Mat4.from_scale(Vec3(max_width, ewi_outside_height, 1)))
            w2.set_visible(True)

            w3 = app.add_mesh(EWITopOutside(), parent=last_anchor)
            w3.set_transform(Mat4.from_translation(Vec3(0, ewi_outside_height / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True) * Mat4.from_scale(Vec3(max_width, ewi_outside_height, 1)))
            w3.set_visible(True)

            w4 = app.add_mesh(EWITopOutside(), parent=last_anchor)
            w4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, ewi_outside_height / 2, 0)) * Mat4.from_rotation_y(-90, True) * Mat4.from_scale(Vec3(max_width, ewi_outside_height, 1)))
            w4.set_visible(True)

            floor3 = app.add_mesh(EWIRooftop(max_width, max_width), parent=last_anchor)
            floor3.set_transform(Mat4.from_translation(Vec3(0, ewi_outside_height, 0)))
            floor3.set_visible(True)

            last_anchor = floor3
