from setuptools import setup

setup(
    name="library",  
    version="0.1.0", 
    packages=['library'],
    author="Daniel Blanco Salazar",
    author_email="daniel.blanco-s@mail.escuelaing.edu.co",
    description="Una librería para operaciones con números complejos (implementación propia)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com//library", 
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)