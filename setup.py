from setuptools import setup, find_packages
import pathlib
PACKAGE_NAME = 'journeypy'
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    description="This Are workflow Journey library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/atmaramnaik/journeypy.git",
    author="Atmaram Naik",
    author_email="naik_atmaram@yahoo.com",

    license="MIT",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        'future',
        'six',
    ],
    entry_points={
        "console_scripts": [
            "journey=journeypy.__main__:main",  
        ]
    },
)