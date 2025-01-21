from bk7084.math import *
from components import *
import math
import random

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
        last_anchor = self.building
        for i in range(self.num_floors):
            # To place each floor higher than the previous one, we parent all
            # components to one 'base' component (floor1, see below). Then we
            # only have to move the base component up higher and the framework
            # takes care of the rest.

            # To place each floor higher than the previous one, we parent all
            # components to one 'base' component (floor1, see below). Then we
            # only have to move the base component up higher and the framework
            # takes care of the rest.
            floor1 = app.add_mesh(BasicFloor(max_width, max_width), parent=last_anchor)
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor1.set_visible(True)

            floor2 = app.add_mesh(BasicFloor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)
            groundfloorwall1 = app.add_mesh(BasicWindowWall(max_width, max_width), parent=floor1)
            groundfloorwall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            groundfloorwall1.set_visible(True)
            groundfloorwall2 = app.add_mesh(BasicWindowWall(max_width, max_width), parent=floor1)
            groundfloorwall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            groundfloorwall2.set_visible(True)
            groundfloorwall3 = app.add_mesh(BasicWindowWall(max_width, max_width), parent=floor1)
            groundfloorwall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            groundfloorwall3.set_visible(True)
            groundfloorwall4 = app.add_mesh(BasicWindowWall(max_width, max_width), parent=floor1)
            groundfloorwall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            groundfloorwall4.set_visible(True)

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
        self.num_floors = num_floors
        self.max_width = max_width
        self.building = app.spawn_building()  # Assuming a building object is spawned in the app
        self.building.set_visible(True)

        R = max(max_width,max_width) / 2
        r= (R * math.sqrt(3)) / 2
        
        # Loop to create each floor and its components
        for i in range(self.num_floors):
            # Hexagonal floor for this level


            floor = app.add_mesh(BasicHexagonRoof( max_width,  max_width), parent=self.building)
            floor.set_transform(Mat4.from_scale(Vec3(max(1.0 * (0.95 ** i), 0.5), max(1.0 * (0.95 ** i), 0.5), max(1.0 * (0.95 ** i), 0.5)))*Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor.set_visible(True)
            
            # Hexagonal roof for this level (it will be placed one level higher)
            roof = app.add_mesh(BasicHexagonRoof( max_width, max_width), parent=floor)
            roof.set_transform( Mat4.from_translation(Vec3(0, max_width, 0)))  # Move roof up by max_width
            roof.set_visible(True)
            
            # Create 6 walls for the hexagonal building
            for j in range(6):
                # Calculate the angle for each wall (since there are 6 walls in a hexagon)
                angle = math.radians(60 * j +30)  # 60 degrees per side

                # Calculate the position of each wall (at the midpoint of the hexagon side)
                x_position = r * math.cos(angle)  # Position along X axis
                z_position = r * math.sin(angle)  # Position along Z axis

                # Create the wall with the calculated max width (side length of the hexagon)
                wall_class = random.choice([BasicRectangleWall, BasicRectangleWindowWall])
                wall = app.add_mesh(wall_class(max_width, max_width), parent=floor)
                # Position the wall at the correct position (on the side of the hexagon)
                wall.set_transform(
                    Mat4.from_translation(Vec3(x_position, max_width/2, z_position)) * Mat4.from_rotation_y(60-60*j, True)
                )
                wall.set_visible(True)

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
        pass

class Hexagon:
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
        for i in range(self.num_floors):
            R = max(max_width,max_width) / 2
            r= (R * math.sqrt(3)) / 2
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