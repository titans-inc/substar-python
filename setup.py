from setuptools import setup, find_packages
from substar import __version__

setup(
    author='Devi Prasad',
    author_email='deviprsd21@gmail.com',
    description='',
    name='SubStar',
    license='GPLv3',
    long_description=open('README.md').read(),
    packages=find_packages(),
    platforms='any',
    url='https://github.com/titans-inc/substar-python',
    version=__version__,
    classifiers=[
        'Programming Language :: Python'
    ]
)