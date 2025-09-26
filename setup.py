'''This file is used to Creating my project as a package / and to install it using pip'''

from setuptools import setup, find_packages
from typing import List

#  
def get_requirements(file_path: str) -> List[str]:
    '''
    To make my install_required to fetch data from requirements.txt file and install line by line
    * This function will return the list of requirements
    '''
    HYPEHN_E_DOT='-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "")for req in requirements]
        if HYPEHN_E_DOT in requirements:
            requirements.remove(HYPEHN_E_DOT)
    return requirements
   
   



#here we are setting up meta deta of my packages
setup(
    name="Ml_Project",
    version="0.1",
    author="Md Aman",
    author_email="aman.nit.cse@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
    ],
)