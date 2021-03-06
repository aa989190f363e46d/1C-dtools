from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='1C-dtools',
    version='0.0.1',
    packages=['onec_dtools'],
    url='https://github.com/Infactum/1C-dtools',
    license='MIT',
    author='infactum',
    author_email='infactum@gmail.com',
    description='Tools for working with 1C:Enterprise data files',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Database'
    ],
    keywords='1C 1C:Enterprise 1CD'
)
