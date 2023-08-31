from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirments
    '''
    EDOT ='-e .'
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        
        if EDOT in requirements:
            requirements.remove(EDOT)            
    
setup(
    name='MLProject',
    version='0.0.1',
    author='Vijaya',
    author_mail='ahirejadhavvijaya@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'))  #['pandas','seaborn','numpy'])

    