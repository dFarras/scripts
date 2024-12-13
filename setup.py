from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="1.0.0",
    author="Diego Farras",
    author_email="diegofarrasguevara@gmail.com",
    description="A cli to retrieve AEMET information",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dFarras/scripts.git",
    packages=find_packages(),  # Automatically find your packages
    include_package_data=True,  # Include non-Python files from MANIFEST.in
    install_requires=[
        "click>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "aemet=aemet.common.aemet_cli:aemet",
            "pito=aemet.common.aemet_cli:pito",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)