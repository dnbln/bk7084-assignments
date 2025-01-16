from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=
        cythonize(
        [
            "main.py",
            "buildings.py",
            "city.py",
            "optimizer.py",
            "components.py"
        ], annotate=True),
)