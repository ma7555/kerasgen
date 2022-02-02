import io
import os
import re

from setuptools import find_packages
from setuptools import setup


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent

setup(
    name="kerasgen",
    version="0.1.1",
    url="https://github.com/ma7555/kerasgen",
    license='MIT',

    author="Mahmoud Bahaa",
    author_email="mah.alaa@nu.edu.eg",

    description="A Keras/Tensorflow compatible image data generator for creating balanced batches",
    long_description = (this_directory / "README.md").read_text(),
    long_description_content_type='text/markdown',

    packages=find_packages(exclude=('tests',)),

    install_requires=[
    'tensorflow>=2.7',
    'numpy>=1.19',
    ],
    
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)