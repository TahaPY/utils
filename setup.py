from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='utils-tahapy',
    version='0.0.2',
    packages=[''],
    url='https://github.com/TahaPY/hundo-utils',
    license='MIT',
    author='Alireza',
    author_email='mohammadtaharabie@gmail.com',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
