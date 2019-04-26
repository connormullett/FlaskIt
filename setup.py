
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='FlaskIt',
    install_requires=[
        'click'
    ],
    entry_points={
        'console_scripts':
            'flaskit=src.main:main'
    }
)

