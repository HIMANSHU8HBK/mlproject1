from setuptools import Require, find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will re
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name="mlproject1",
    version='0.0.1',
    author="HIMANSHU8HBK",
    author_email='kautkarhimanshu37@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    setup_requires=['setuptools_scm'],
)
