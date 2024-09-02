from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
    return requirements


setup(
    name='NPN_Cognizant_project',
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)