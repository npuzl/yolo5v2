from setuptools import find_packages
from setuptools import setup

install_requires = [
    'six',
    'tf-slim>=1.1',
]

setup(
    name='slim',
    version='0.1',
    install_requires=install_requires,
    include_package_data=True,
    packages=find_packages(),
    description='tf-slim',
)