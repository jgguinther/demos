from labs import model_dir
from setuptools import setup, find_packages

# Comment Out: in future Users will have created requirements.txt off platform
# import os
# os.system("pip3 freeze | grep -v 'pkg-resources' | grep -v 'cadCAD' > requirements.txt")
# os.system("pip3 freeze > requirements.txt")

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
# Step 1 - this file (setup.py) will be added to project root
# Step 2 - run the following command: `python3 setup.py bdist_wheel`
# Step 3 - send dist/*.whl to S3 bucket
# Step 4 - send .whl url along with job request
# Step 5 - endpoint GET .whl with url and installs it
# Step 6 - De-serialize Job
# Transient Step: remove ser utils on k8S service and scheduler.py