from setuptools import setup, find_packages
from typing import List

def get_requirements(filename: str)->List[str]:
    """
    This function will return the list of requirements
    """
    with open(filename) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Ankit",
    author_email="ankit@example.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)