from setuptools import setup,find_packages
from typing import List
def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements        


setup(       
    name="End-to-End-ML-Project",
    version="1.0.0",
    author="Mohamed Asaad Elbadawy",
    author_email="mohamed.asaad.elbadawy@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)