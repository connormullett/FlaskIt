
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='FlaskIt',
    author='Connor Mullett',
    description='Flask API starter',
    long_description=read('README.rst'),
    keywords='flask api',
    packages=['src'],
    license='MIT',
    install_requires=[
        'click'
    ],
    version='1.0.0',
    url='https://github.com/connormullett/FlaskIt',
    entry_points={
        'console_scripts':
            'flaskit=src.main:main'
    }
)

