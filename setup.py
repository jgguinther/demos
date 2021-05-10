from labs import model_dir
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = [
        pkg for pkg in f.read().strip().split('\n')
            if not pkg.startswith('pkg-resources') and
               not pkg.startswith('cadCAD')
    ]

setup(
    name=model_dir,
    version='0.0.0',
    package_dir={"": model_dir},
    packages=find_packages(where=model_dir),
    install_requires=install_requires,
    python_requires='>=3.6.8'
)