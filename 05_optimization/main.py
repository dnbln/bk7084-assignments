import bk7084 as bk
from buildings import *
from city import City
from optimizer import Optimizer

"""
Exercise 05: City Optimization
------------------------------

Welcome to the final project of this course! In this project, you will implement
a city optimization algorithm that optimizes the displacement of buildings in
a city grid to maximize the sunlight exposure of the city.

Before you start, try to run this file (main.py) and see what it looks like. You
should see a city grid with some buildings. The starting scene is quite dark, so
you can press the J key to toggle the dynamic light where the sun rotates around
the city. You can also press the K key to toggle the ground visibility to see
the city grid more clearly.

Before we implement the optimization algorithm, let's first understand how the
city grid and the buildings are represented in the code. 

Task 1: Check out the City class in the city.py file read carefully the comments
        in the code then answer the following questions:
        - How is the city grid represented in the code?
        - How is a building represented in the code?
        - How do we get the building at a specific row and column?
        - How do we set the building at a specific row and column?
        - How do we get the type of the building at a specific row and column?
        - How do we swap two buildings at different rows and columns?
        - How do we compute the sunlight scores of the city?
        - How do we print the city grid in the console?
        - How do we initialize the city grid?

In the last exercise, you were asked to implement your own building classes: the
Skyscraper, Highrise and Office classes. In this exercise, we will reuse the
these classes.

Task 2: Copy the Skyscraper, Highrise, and Office classes from the previous
        exercise to the buildings.py file. Do not copy the House and Park classes.
        
Task 3: Finish the implementation of `construct_building` method in the City
        class to enable spawning buildings of different types. This method should
        construct a building at a specific row and column.

Now if you run this file again, you should see the city grid with your own signature
buildings.

# Optimization 

Now let's implement the optimization algorithm. The goal of the optimization
algorithm is to maximize the sunlight exposure of the city. The sunlight exposure
of the city is computed by summing up the sunlight exposure of each building in
the city at each time step. 

In the City class, we have provided you with the `compute_sunlight_scores` method
that computes the sunlight exposure of the whole city. This method returns a list
of sunlight scores for each time of the day. The length of the list is the number
of time steps in a day (11 in this case).

The optimization algorithm is implemented in the Optimizer class (optimizer.py). It
accepts a City object as input and optimizes the city grid of the City object.

The Optimizer class has two methods: `step` and `optimize`. The `step` method performs 
a single optimization step. The `optimize` method runs the optimizer for a fixed number
of steps.

These two methods are already implemented for you. The `step` method is the core of
your optimization algorithm. Before you implement your own optimization algorithm,
you should first define some rules that your city grid should follow. For example,
you can define that the city grid should not have any adjacent buildings of the same
type. Then you can implement the `step` method to enforce this rule. In the existing
implementation, it randomly swaps two buildings in the city grid. You should replace
this implementation with your own optimization algorithm.

As for the `optimize` method, you should add a stopping criterion to stop the optimization
when the score does not improve anymore. You can also add other stopping criteria if you
want. You can also change the number of optimization steps.

Task 4: Implement your own optimization algorithm in the `step`, `optimize` methods of
        the Optimizer class.
        
Good luck and have fun!
"""

win = bk.Window()
win.set_title("BK7084 - Lab 5 - City Optimization")
win.set_size(800, 800)
win.set_resizable(True)

app = bk.App()
camera = app.create_camera(pos=Vec3(18, 18, 26), look_at=Vec3(0, 0, 0), fov_v=60.0, near=0.1, far=360.0, background=bk.Color.ICE_BLUE)
camera.set_as_main_camera()

inclination = np.pi / 8
center_pos = Vec3(0, np.cos(inclination), np.sin(inclination))
starting_pos = Mat3.from_rotation_z(-np.pi * 0.5) * center_pos
light = app.add_directional_light(Vec3(0.0) - starting_pos, bk.Color(0.8, 0.8, 0.8))


print("Building city...")
city = City(app, 32, 32, 8)
city.initialize_from(
"""SK PK SK PK SK PK SK OF SK ET SK HS SK HS SK ET HR PK SK PK SK ET SK OF SK ET SK HS SK ET SK HS
ET OF ET PK HS ET PK OF OF PK OF OF PK ET OF ET OF OF OF OF OF OF OF OF PK PK OF ET ET HS ET OF
SK ET SK OF SK OF SK OF SK OF SK ET SK OF SK PK HR OF SK ET SK PK SK PK SK ET SK OF SK HS SK ET
ET OF PK OF OF OF ET HS HS HS PK OF ET OF HS PK OF OF OF OF ET PK HS PK OF OF OF ET OF ET ET OF
SK PK SK OF SK ET SK OF SK OF SK PK SK PK SK OF SK HS SK OF SK OF SK HS SK HS SK PK SK HS SK PK
OF OF PK OF PK ET HS OF PK OF OF OF OF OF OF ET HS OF OF PK OF HS OF ET PK ET PK ET HS OF PK ET
HR PK SK PK SK OF HR ET HR HS HR HS HR PK HR ET SK OF HR OF HR PK HR ET HR ET HR OF SK OF HR PK
ET OF HS PK OF PK OF HS OF ET OF HS ET ET OF OF OF OF OF PK PK ET OF OF OF HS OF OF PK PK PK ET
HR ET HR OF HR PK HR ET HR OF HR OF HR OF PK OF HR HS HR HS HR HS HR OF HR OF HR OF HR PK HR OF
OF HS HS OF HS OF OF PK ET ET OF OF OF OF OF HS OF PK OF OF OF PK OF ET HS OF OF OF OF ET OF PK
HR PK HR ET HR OF HR OF HR PK SK OF HR PK HR OF HR PK HR PK HR PK HR ET HR HS HR OF HR PK HR OF
PK OF OF ET ET HS HS PK OF PK OF OF PK OF OF HS PK OF ET OF OF PK OF ET PK ET ET OF ET OF ET ET
HR OF HR OF HR ET HR OF HR OF HR PK HR OF HR HS HR ET HR HS HR PK HR PK HR OF HR ET HR PK HR ET
PK OF ET PK OF HS OF OF OF PK ET OF OF OF OF OF OF ET HS OF PK OF OF HS OF PK PK HS OF HS PK ET
HR OF HR ET HR HS HR HS HR ET HR PK HR OF HR HS HR HS HR PK HR PK HR PK HR HS HR PK HR PK HR PK
PK HS HS OF HS OF OF PK ET PK ET OF ET PK HS PK OF PK OF PK OF PK OF OF OF OF OF ET OF PK OF PK
HR HS HR PK HR OF HR PK HS OF HS PK HS PK HS HS HS HS HS ET HS PK OF OF PK HS OF HS OF ET HS HS
ET OF OF HS PK OF PK HS ET OF OF PK HS PK HS ET HS OF HS HS OF PK PK PK PK PK OF PK HS PK PK PK
HS HS HS HS OF HS HS PK HS HS HS HS OF HS HS OF HS OF HS HS OF ET OF PK HS ET OF HS HS HS PK HS
PK OF HS OF OF HS OF ET OF OF ET OF PK ET HS HS OF ET OF HS PK HS PK HS HS HS HS ET PK PK OF HS
HS HS PK HS PK HS HS HS HS HS HS HS PK PK HS ET OF ET HS HS HS HS OF OF HS OF HS ET OF PK OF HS
OF HS HS OF OF OF ET OF OF HS PK HS OF ET PK HS HS HS HS OF PK HS OF PK HS HS HS HS HS HS HS HS
HS HS HS OF HS HS ET HS HS HS HS HS OF HS HS HS HS HS HS HS HS HS OF HS HS PK OF HS HS OF HS OF
HS OF HS HS HS OF OF HS OF OF HS HS PK HS OF HS OF HS PK PK OF HS HS HS HS HS HS PK ET PK PK PK
HS HS OF HS HS HS PK OF HS HS HS OF HS ET HS HS HS ET PK HS HS PK HS HS HS HS HS HS HS OF HS HS
HS HS PK HS PK HS PK HS HS OF HS OF HS PK HS HS OF HS HS PK HS HS HS HS HS HS OF HS ET HS PK ET
HS HS OF HS HS OF HS HS HS HS HS HS HS PK HS HS HS HS HS HS HS OF HS HS HS HS HS HS ET HS OF HS
HS HS HS HS HS HS OF HS HS HS ET OF HS HS HS OF HS OF HS HS PK ET OF HS HS OF HS ET ET HS PK HS
HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS OF HS HS HS HS HS HS HS OF HS HS HS HS HS HS
HS HS HS HS HS HS OF HS HS HS HS HS OF HS OF HS HS HS HS HS HS OF HS HS ET OF PK ET OF HS HS HS
HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS HS
HR HS HS HS HS HS HS OF HS OF HS HS HS HS HS HS HS HS OF PK HS ET PK HS HS HS OF HS ET HS HS PK"""
)
city.print_plots()


optimizer = Optimizer(city)
run_optimizer = False

# Variables to avoid key spamming
is_key_1_pressed = False
is_key_2_pressed = False
is_key_j_pressed = False
is_key_k_pressed = False
is_key_l_pressed = False
is_key_o_pressed = False

enable_backface_culling = True
enable_wireframe = False
app.enable_backface_culling(enable_backface_culling)
app.enable_wireframe(enable_wireframe)
app.enable_shadows(True)
light_rotation = Mat3.identity()
dynamic_light = False
ground_visibility = True


@app.event
def on_update(input, dt, t):
    global enable_backface_culling
    global enable_wireframe
    global is_key_1_pressed
    global is_key_2_pressed
    global is_key_j_pressed
    global is_key_k_pressed
    global is_key_l_pressed
    global is_key_o_pressed
    global light_rotation
    global dynamic_light
    global ground_visibility
    global run_optimizer

    if input.is_key_pressed(bk.KeyCode.Key1):
        if not is_key_1_pressed:
            is_key_1_pressed = True
            enable_backface_culling = not enable_backface_culling
            app.enable_backface_culling(enable_backface_culling)
    if input.is_key_released(bk.KeyCode.Key1):
        is_key_1_pressed = False

    if input.is_key_pressed(bk.KeyCode.Key2):
        if not is_key_2_pressed:
            is_key_2_pressed = True
            enable_wireframe = not enable_wireframe
            app.enable_wireframe(enable_wireframe)
    if input.is_key_released(bk.KeyCode.Key2):
        is_key_2_pressed = False

    if input.is_key_pressed(bk.KeyCode.J):
        if not is_key_j_pressed:
            is_key_j_pressed = True
            dynamic_light = not dynamic_light
    if input.is_key_released(bk.KeyCode.J):
        is_key_j_pressed = False

    if input.is_key_pressed(bk.KeyCode.K):
        if not is_key_k_pressed:
            is_key_k_pressed = True
            ground_visibility = not ground_visibility
            city.set_ground_visibility(ground_visibility)
    if input.is_key_released(bk.KeyCode.K):
        is_key_k_pressed = False

    if input.is_key_pressed(bk.KeyCode.L):
        if not is_key_l_pressed:
            is_key_l_pressed = True
            optimizer.step(True)
    if input.is_key_released(bk.KeyCode.L):
        is_key_l_pressed = False

    if input.is_key_pressed(bk.KeyCode.O):
        if not is_key_o_pressed:
            is_key_o_pressed = True
            run_optimizer = not run_optimizer
    if input.is_key_released(bk.KeyCode.O):
        is_key_o_pressed = False

    city.update(dt, t)

    if dynamic_light:
        light_rotation = Mat3.from_rotation_z(dt * 0.2) * light_rotation
        pos = light_rotation * starting_pos
        if pos.y >= 0.0:
            light.set_directional_light(Vec3(0.0) - pos)
            app.enable_lighting(True)
        else:
            light_rotation = Mat3.from_rotation_z(dt * 0.4) * light_rotation
            app.enable_lighting(False)
    else:
        pos = light_rotation * starting_pos
        light.set_directional_light(Vec3(0.0) - pos)

    if run_optimizer:
        optimizer.step(True)


app.run(win)
