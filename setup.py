# -*- encoding: UTF-8 -*-
from setuptools import setup, find_packages

setup(
    name="x-tools",
    version="0.1",
    author="telzhou",
    author_email="btczhou618@gmail.com",
    url="https://github.com/telzhou618/x-tools",
    description="tools is a collection of tools developed in Python",
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'requests',
        'click',
        'tqdm',
        'jsonlines'
    ],
    entry_points={
        'console_scripts': [
            'x-tools=tools.tools:main'
        ]
    },
)
