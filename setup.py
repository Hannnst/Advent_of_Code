from setuptools import setup, find_packages

setup(
    name='advent_of_code',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'fetch_advent=fetchAdvent:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A module to fetch and save Advent of Code tasks and test data.',
    url='https://github.com/Hannnst/Advent_of_Code',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)