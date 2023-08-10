import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="asyncapi-schema-pydantic",
    version="1.0.1",
    description="AsyncAPI (v2) specification schema as pydantic class",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/albertnadal/asyncapi-schema-pydantic",
    author="Albert Nadal Garriga",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=["pydantic>=1.8.2", "PyYAML~=6.0"],
    python_requires=">=3.7",
)
