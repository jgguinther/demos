import os
from setuptools import setup, find_packages
from labs import model_dir


# Comment Out: in future Users will have created requirements.txt off platform
# os.system("pip3 freeze > requirements.txt")

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name="simpkg",
    version='0.0.1',
    install_requires=install_requires,
    package_dir={"": model_dir},
    packages=find_packages(where=model_dir),
    python_requires='>=3.6.8'
)

# Step 1 - this file (setup.py) will be added to project root
# Step 2 - run the fllowing command: `python3 setup.py bdist_wheel`
# Step 3 - send dist/*.whl to S3 bucket
# Step 4 - send .whl url along with job request
# Step 5 - endpoint GET .whl with url and installs it
# Step 6 - De-serialize Job
# Transient Step: remove ser utils on k8S service and scheduler.py