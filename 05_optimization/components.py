import bk7084 as bk
import numpy as np
from numpy.random import randint, rand
import math

"""
Materials are used to define the appearance of a mesh.
"""
material_stone_bricks = bk.Material()
material_stone_bricks.textures = {
    "diffuse_texture": bk.res_path("../03_textures/assets/stone_bricks_col.jpg"),
    "normal_texture": bk.res_path("../03_textures/assets/stone_bricks_nrm.png"),
    "specular_texture": bk.res_path("../03_textures/assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("../03_textures/assets/stone_bricks_gloss.jpg"),
}

material_basic_bricks = bk.Material()
material_basic_bricks.specular = bk.Color(0.1, 0.1, 0.1)
material_basic_bricks.textures = {
    "diffuse_texture": bk.res_path("assets/brick.jpg"),
}

material_basic_floor = bk.Material()
material_basic_floor.diffuse = bk.Color(0.8, 0.5, 0.5)

material_basic_window = bk.Material()
material_basic_window.textures = {
    "diffuse_texture": bk.res_path("assets/window.jpg"),
}

material_basic_ground = bk.Material()
material_basic_ground.textures = {
    "diffuse_texture": bk.res_path("assets/grass.jpg"),
}

material_glass_window = bk.Material()
material_glass_window.textures = {
    "diffuse_texture": bk.res_path("assets/window_wall.jpg"),
}

material_glass_window_entrance = bk.Material()
material_glass_window_entrance.textures = {
    "diffuse_texture": bk.res_path("assets/base_window_entrance.jpg"),
}

material_concrete_ground = bk.Material()
material_concrete_ground.textures = {
    "diffuse_texture": bk.res_path("assets/concrete.jpg"),
}                                   

material_dark = bk.Material()
material_dark.textures = {
    "diffuse_texture": bk.res_path("assets/dark.jpg"),
}    

material_darker = bk.Material()
material_darker.textures = {
    "diffuse_texture": bk.res_path("assets/darker.jpg"),
}    

material_highrise_floor = bk.Material()
material_highrise_floor.diffuse = bk.Color(0.6, 0.6, 0.6)

material_glass_facade = bk.Material()
material_glass_facade.textures = {
    "diffuse_texture": bk.res_path("assets/glassfacade.jpeg"),
}

material_skyscraper_wall = bk.Material()
material_skyscraper_wall.textures = {
    "diffuse_texture": bk.res_path("assets/HighRiseGlass0055_1_350.jpg"),
}

material_skyscraper_floor = bk.Material()
material_skyscraper_floor.textures = {
    "diffuse_texture": bk.res_path("assets/grass.jpg"),
}

material_skyscraper_door = bk.Material()
material_skyscraper_door.textures = {
    "diffuse_texture": bk.res_path("assets/door_skyscraper2.png"),
}

class SkyscraperWall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_skyscraper_wall):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperWallMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class SkyscraperWallConcrete(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_dark):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperWallConcreteMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]        

class SkyscraperWallSmall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_skyscraper_wall):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperWallSmallMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class SkyscraperWallSmallConcrete(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_dark):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperWallSmallContreteMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class SkyscraperWallWide(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_skyscraper_wall):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperWallWideMesh"
        self.positions = [
            [-w, -h / 2, 0],
            [w, -h / 2, 0],
            [w, h / 2, 0],
            [-w, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [2, 0], [2, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class SkyscraperWallWideConcrete(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_dark):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperWallWideConcreteMesh"
        self.positions = [
            [-w, -h / 2, 0],
            [w, -h / 2, 0],
            [w, h / 2, 0],
            [-w, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [2, 0], [2, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class SkyscraperFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_darker):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperFloorMesh"
        # self.materials = materials
        self.positions = [
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]

class SkyscraperFloorLeft(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_darker):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperFloor2Mesh"
        # self.materials = materials
        self.positions = [
            [-w, 0, -h / 2],
            [w, 0, -h / 2],
            [w, 0, h / 2],
            [-w, 0, h / 2],
        ]
        self.texcoords = [[0, 0], [2, 0], [2, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]

class SkyscraperFloorRight(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_darker):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperFloor3Mesh"
        # self.materials = materials
        self.positions = [
            [-w / 2, 0, -h],
            [w / 2, 0, -h],
            [w / 2, 0, h],
            [-w / 2, 0, h],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 2], [0, 2]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]


class SkyscraperRoof(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_skyscraper_door):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SkyscraperDoorMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]



class BasicWall(bk.Mesh):
    """
    Create a basic wall mesh with the given size and material.
    This class is a subclass of bk.Mesh, so it can be used as a mesh. For example,
    you can create a mesh instance by `mesh = BasicWallMesh(...)`, and then add it to
    a scene by `app.add_mesh(mesh)`. It's the same as using `mesh = create_basic_wall(...)`.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_basic_bricks):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicWallMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]


class BasicFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_basic_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicFloorMesh"
        # self.materials = materials
        self.positions = [
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]


class BasicWindowWall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicWindowWallMesh"
        # self.materials = materials
        self.positions = [
            [-w/2, -h/2, 0.0], [w/2, -h/2, 0.0], [w/2, h/2, 0.0], [-w/2, h/2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
        ]
        self.texcoords = [
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0],
            [0.3, 0.3], [0.7, 0.3], [0.7, 0.7], [0.3, 0.7],
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0]
        ]
        self.triangles = [
            [0, 1, 5], [0, 5, 4], [1, 2, 6], [1, 6, 5], [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7],
            [8, 9, 10], [8, 10, 11],
        ]
        self.materials = [
            material_basic_bricks,
            material_basic_window,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]

class GlassWindowWall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, w=1, h=1, m=material_glass_window):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "GlassWindowWallMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]
    
class GlassWindowEnterance(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, w=1, h=1, m=material_glass_window_entrance):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "GlassWindowEnteranceMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]


class Hexall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, m=material_glass_window):
        super().__init__()
        self.name = "HexallMesh"
        p = [[0, 0, 0]]+[[np.cos(i * 2 * np.pi / 6), np.sin(i * 2 * np.pi / 6), 0] for i in range(6)]
        self.positions = p
        self.texcoords = [[0.5 + x / 2, 0.5 - y / 2] for [x, y, _] in p]
        self.triangles = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 1]]
        self.materials = [m]

class HexallHigher(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, m=material_glass_window):
        super().__init__()
        self.name = "HexallHigherMesh"
        p = [[0, 0, 0]] + [[np.cos(i * 2 * np.pi / 6), np.sin(i * 2 * np.pi / 6), 0] for i in range(0, 4)]
        self.positions = p
        self.texcoords = [[0.5 + x / 2, 0.5 - y / 2] for [x, y, _] in p]
        self.triangles = [[0, 1, 2], [0, 2, 3], [0, 3, 4]]
        self.materials = [m]

class HexallLower(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, m=material_glass_window):
        super().__init__()
        self.name = "HexallLowerMesh"
        p = [[0, 0, 0]] + [[np.cos(i * 2 * np.pi / 6), np.sin(i * 2 * np.pi / 6), 0] for i in range(3, 7)]
        self.positions = p
        self.texcoords = [[0.5 + x / 2, 0.5 - y / 2] for [x, y, _] in p]
        self.triangles = [[0, 1, 2], [0, 2, 3], [0, 3, 4]]
        self.materials = [m]

class HexallInside(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, m=material_glass_window):
        super().__init__()
        self.name = "HexallInside1Mesh"
        p = [[np.cos(i * 2 * np.pi / 6), np.sin(i * 2 * np.pi / 6), 0] for i in range(6)] + [[np.cos(i * 2 * np.pi / 6), np.sin(i * 2 * np.pi / 6), -1] for i in range(6)]
        self.positions = p
        self.texcoords = [[0.5 + x / 2, 0.5 - y / 2] for [x, y, _] in p]
        self.triangles = [[0, 6, 1], [1, 6, 7], [1, 7, 2], [2, 7, 8], [2, 8, 3], [3, 8, 9], [3, 9, 4], [4, 9, 10], [4, 10, 5], [5, 10, 11], [5, 11, 0], [0, 11, 6]]
        self.materials = [m]

class EWITopInside(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, w=1, h=1, m=material_glass_window):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "EWITopInsideMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class EWITopOutside(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, w=1, h=1, m=material_glass_window):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "EWITopOutsideMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class EWIRooftop(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, w=1, h=1, m=material_glass_window):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "EWIRooftopMesh"
        self.positions = [
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ]
        self.texcoords = [[0.1, 0.1], [0.1, 0.1], [0.1, 0.1], [0.1, 0.1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]
class SlantedWall(bk.Mesh):
    """
    Create a basic wall mesh with the given size and material.
    This class is a subclass of bk.Mesh, so it can be used as a mesh. For example,
    you can create a mesh instance by `mesh = BasicWallMesh(...)`, and then add it to
    a scene by `app.add_mesh(mesh)`. It's the same as using `mesh = create_basic_wall(...)`.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_glass_facade):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SlantedWallMesh"
        height_slantedwall = h / math.cos( math.atan(0.05)) 
        offset_z = -0.1 * w / 2
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [0.9*w / 2, height_slantedwall / 2, offset_z],
            [-0.9*w / 2, height_slantedwall / 2, offset_z],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]

class SlantedGlassDoorWall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SlantedDoorWallMesh"
        height_slantedwall = h / math.cos( math.atan(0.05)) 
        offset_z = -0.1 * w / 2
        # self.materials = materials
        self.positions = [
            [-w/2, -h/2, 0.0], [w/2, -h/2, 0.0], [0.9*w/2, height_slantedwall/2, offset_z], [-0.9*w/2, height_slantedwall/2, offset_z],
            [-w*0.15, -h/2, 0.0], [w*0.15, -h/2, 0.0], [w*0.15, h*0.15, 0.0], [-w*0.15, h*0.15, 0.0],
            [-w*0.15, -h/2, 0.0], [w*0.15, -h/2, 0.0], [w*0.15, h*0.15, 0.0], [-w*0.15, h*0.15, 0.0],
        ]
        self.texcoords = [
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0],
            [0.3, 0.0], [0.6, 0.0], [0.6, 0.65], [0.3, 0.65],
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0]
        ]
        self.triangles = [
            [0, 4, 7], [0, 3, 7], [3, 7, 2], [2, 7, 6], [2, 6, 1], [1, 6, 5],
            [8, 9, 10], [8, 10, 11],
        ]
        self.materials = [
            material_glass_facade,
            material_basic_window,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 6, 0),
            bk.SubMesh(6, 8, 1),
        ]

class HighriseFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_highrise_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "HighriseFloorMesh"
        # self.materials = materials
        self.positions = [
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]

class BasicHexagonRoof(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_basic_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicHexagonRoofMesh"
        
        # Calculate the 6 vertices of the hexagon
        positions = []
        for i in range(6):
            angle = math.radians(i * 60)  # 360 degrees / 6 sides = 60 degrees
            x = (w / 2) * math.cos(angle)
            z = (h / 2) * math.sin(angle)
            positions.append([x, 0, z])  # y=0 for flat roof
        
        # Define the center point of the hexagon for the texture
        center = [0, 0, 0]  # This will be the center of the hexagon
        positions.append(center)

        self.positions = positions
        
        # Hexagon has 6 triangles, one for each side, connecting center to vertices
        self.triangles = [[6, 1, 0],  [6, 2, 1], [6, 3, 2], [6, 4, 3], [6, 5, 4], [6, 0, 5]]
        
        # UV Mapping: Simple mapping, assuming square texture and each triangle having unique texcoords
        texcoords = []
 
# Calculate the 6 outer vertices of the hexagon
        for i in range(6):
            angle = math.radians(i * 60)  # 0°, 60°, 120°, 180°, 240°, 300°
            x =  0.5 + 0.5 * math.cos(angle)
            y =  0.5 + 0.5 * math.sin(angle)
            texcoords.append([x, y])
        center_coords = [0.5, 0.5]
        texcoords.append(center_coords)
        self.texcoords = texcoords
        
        self.materials = [m]

class SlantedRectangleWall(bk.Mesh):
    """
    Create a single rectangular wall mesh that surrounds one side of a hexagonal roof.
    The length of the wall is based on the side length of the hexagon.
    """
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_glass_facade):
        super().__init__()
        self.w = w  # Width (distance between opposite vertices of the hexagon)
        self.h = h  # Height of the wall
        self.name = "SlantedRectangleWallMesh"
        
       # Calculate the hexagon's side length from the distance between opposite sides (w)
        height_wall = h / math.cos( math.atan(0.05))
        hex_side_length =  w / 2  # Formula for hexagon side length
        offset_z = 0.2 * (hex_side_length * math.sqrt(3)) / 2
        # Create the positions for a single rectangular wall (coordinates for 2 triangles)
        positions = [
            [-hex_side_length / 2, -height_wall / 2, 0],  # Bottom-left corner
            [hex_side_length / 2, -height_wall / 2, 0],   # Bottom-right corner
            [1.2*hex_side_length / 2, height_wall / 2, offset_z],    # Top-right corner
            [-1.2*hex_side_length / 2, height_wall / 2, offset_z]    # Top-left corner
        ]
        
        self.positions = positions
        
        # Create the 2 triangles that make up the single rectangular wall
        self.triangles = [
            [0, 1, 2], [0, 2, 3]  # Two triangles for the front face of the wall
        ]
        
        # Define UV coordinates for the wall (simple square mapping)
        self.texcoords = [
            [0, 0], [0.5, 0], [0.5, 1], [0, 1]  # Simple UV mapping for the rectangular wall
        ]

        self.materials = [m]

class SlantedRectangleWindowWall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "SlantedRectangleWindowWallMesh"
        # self.materials = materials
        height_wall = h / math.cos( math.atan(0.05))
        hex_side_length =  w / 2  # Formula for hexagon side length
        offset_z = 0.2 * (hex_side_length * math.sqrt(3)) / 2
        self.positions = [
            [-hex_side_length/2, -height_wall/2, 0.0], [hex_side_length/2, -height_wall/2, 0.0], [1.2*hex_side_length/2, height_wall/2, offset_z], [-1.2*hex_side_length/2, height_wall/2, offset_z],
            [-hex_side_length*0.2, -height_wall*0.2, 0.0], [hex_side_length*0.2, -height_wall*0.2, 0.0], [hex_side_length*0.2, height_wall*0.2, 0.0], [-hex_side_length*0.2, height_wall*0.2, 0.0],
            [-hex_side_length*0.2, -height_wall*0.2, 0.0], [hex_side_length*0.2, -height_wall*0.2, 0.0], [hex_side_length*0.2, height_wall*0.2, 0.0], [-hex_side_length*0.2, height_wall*0.2, 0.0],
        ]
        self.triangles = [
            [0, 1, 5], [0, 5, 4], [1, 2, 6], [1, 6, 5], [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7],
            [8, 9, 10], [8, 10, 11],
        ]
        self.texcoords = [
            [0.0, 0.0], [0.5, 0.0], [0.5, 1.0], [0, 1.0],
            [0.15, 0.3], [0.35, 0.3], [0.35, 0.7], [0.15, 0.7],
            [0.0, 0.0], [0.5, 0.0], [0.5, 1.0], [0, 1.0]
        ]
        
        self.materials = [
            material_glass_facade,
            material_basic_window,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]
        
class Antennapole(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_basic_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "AntennapoleMesh"
        # self.materials = materials
        offset_z = (math.sqrt(3)/6 * -w)
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [0, h, offset_z]
        ]
        self.texcoords = [[0, 0], [1, 0], [0.5, 2]]
        self.triangles = [[0, 1, 2]]
        self.materials = [m]

class Antennabase(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_highrise_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "AntennabaseMesh"
        # self.materials = materials

        self.positions = [
            [-w / 2, 0, -w / 2],
            [w / 2, 0, -w /2],
            [0, 0, w/2]
        ]
        self.texcoords = [[0, 0], [1, 0], [0.5, 1]]
        self.triangles = [[0, 2, 1]]
        self.materials = [m]

class Antennabox(bk.Mesh):
    """
    Create a basic wall mesh with the given size and material.
    This class is a subclass of bk.Mesh, so it can be used as a mesh. For example,
    you can create a mesh instance by `mesh = BasicWallMesh(...)`, and then add it to
    a scene by `app.add_mesh(mesh)`. It's the same as using `mesh = create_basic_wall(...)`.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_highrise_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "AntennaboxMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h/ 2, 0],
            [-w / 2, h/ 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]
