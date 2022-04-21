from setuptools import setup, find_packages
import sys

if sys.version_info < (3, 4):
    requires.append('enum34')

version = '1.0.0'
homepage = 'https://github.com/Saferite-Data-Team'
description = 'Saferite Data Team Library'
requires = ['requests']

setup(
    name='saferite-data-team',
    version = version,
    description=description,
    url=homepage,
    author='Saferite Data Team',
    author_email='data-team@saferitesolutions.com',
    license='',
    install_requires=['requests~=2.27'],
    packages=find_packages()
)