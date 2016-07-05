# -*- coding: utf-8 -*-
import setuptools


setuptools.setup(
    version='0.0.1',
    name='flake8-unnamed-args',
    description='unnamed args flake8 extension',
    keywords='flake8 arg kwargs',
    author='Nikita Lyubchich',
    author_email='cybran111@gmail.com',
    url='https://github.com/nlyubchich/flake8-unnamed-args',
    license='MIT',
    py_modules=['unnamed_args'],
    zip_safe=False,
    install_requires=['flake8'],
    entry_points={
        'flake8.extension': [
            'E7 = unnamed_args:UnnamedArgsChecker',
        ],
    },
)
