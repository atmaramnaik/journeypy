from setuptools import setup, find_packages
PACKAGE_NAME = 'journeypy'
setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    author="Atmaram Naik",
    author_email="naik_atmaram@yahoo.com",
    description="This Journey projects",
    license="MIT",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[
        'Private :: Do Not Upload to pypi server',
    ],
    install_requires=[
        'future',
        'six',
    ],
)