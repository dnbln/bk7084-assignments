import bk7084 as bk
import numpy as np
from numpy.random import randint, rand

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
    "diffuse_texture": bk.res_path("../assets/brick.jpg"),
}

material_basic_floor = bk.Material()
material_basic_floor.diffuse = bk.Color(0.8, 0.5, 0.5)

material_basic_window = bk.Material()
material_basic_window.textures = {
    "diffuse_texture": bk.res_path("../assets/window.jpg"),
}

material_basic_ground = bk.Material()
material_basic_ground.textures = {
    "diffuse_texture": bk.res_path("../assets/grass.jpg"),
}

material_glass_window = bk.Material()
material_glass_window.textures = {
    "diffuse_texture": bk.res_path("../assets/window_wall.jpg"),
}

material_glass_window_entrance = bk.Material()
material_glass_window_entrance.textures = {
    "diffuse_texture": bk.res_path("../assets/base_window_entrance.jpg"),
}

material_concrete_ground = bk.Material()
material_concrete_ground.textures = {
    # "diffuse_texture": bk.res_path("../assets/concrete.jpg"),
}                                   

material_round_tile = bk.Material()
material_round_tile.textures = {
    # "diffuse_texture": bk.res_path("../assets/medallion-round.jpg"),
}

material_skyscraper_wall = bk.Material()
material_skyscraper_wall.textures = {
    # "diffuse_texture": bk.res_path("../assets/HighRiseGlass0055_1_350.jpg"),
}

material_skyscraper_floor = bk.Material()
material_skyscraper_floor.textures = {
    # "diffuse_texture": bk.res_path("../assets/grass.jpg"),
}

material_skyscraper_door = bk.Material()
material_skyscraper_door.textures = {
    # "diffuse_texture": bk.res_path("../assets/door_skyscraper.png"),
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


class SkyscraperFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_skyscraper_floor):
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


class RoundTileFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=4, h=4, m=material_round_tile):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "RoundTileFloorMesh"
        self.positions = [
            [w / 2, 0, 0],
            [w / 4, h / 2, 0],
            [-w / 4, h / 2, 0],
            [-w / 2, 0, 0],
            [-w / 4, -h / 2, 0],
            [w / 4, -h / 2, 0],
        ]
        self.texcoords = [[0, 0], [2, 0], [1, 2], [-1, 2], [-2, 0], [-1, -2], [1, -2]]
        self.triangles = [[0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 1]]
        self.materials = [m]


class SkyscraperDoor(bk.Mesh):
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
