from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-gp",
    version="0.0.1",
    author="Gaby-Pavan",
    author_email="gabriellypavan@gmail.com",
    description="Package for image processing",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gaby-Pavan/image-processing-gp.git",
    packages=find_packages(),
    install_requires=requirements,
)
