from setuptools import find_packages,setup
from typing import List
def get_requirments(file_path:str)->List[str]:
    """
    This function will return list of requirments
    """
    requirment=[]
    with open(file_path) as file_obj:
        requirment=file_obj.readlines()
        

setup(
    name='ML_Projects',
    author='sumit',
    version='0.0.1',
    author_email='samarthanayek@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')
)