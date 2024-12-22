from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_object:  # Correct variable name
        requirements = file_object.readlines()  # Use file_object here
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="regression_project",
    version="0.0.2",
    author="soheb",
    author_email="sohebabdul.abdul8@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages(),
)
