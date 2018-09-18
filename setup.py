import setuptools

import q

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=q.name,
    version=q.__version__,
    author="Ján Janech",
    author_email="janik@janik.ws",
    description="A simple software library helping with processing collections.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janusko/pycq",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite="tests",
    install_requires=[
        'typing;python_version<"3.5"',
    ]
)
