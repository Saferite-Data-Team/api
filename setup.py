from setuptools import setup, find_packages

version = '0.1'
homepage = 'https://github.com/Saferite-Data-Team'
description = 'Saferite Data Team Library'
requires = ['requests']

setup(
    name='saferite-data-team',
    version = '1.0.0',
    description=description,
    url=homepage,
    author='Saferite Data Team',
    author_email='data-team@saferitesolutions.com',
    license='',
    install_requires=['requests~=2.27'],
    packages=find_packages()
)