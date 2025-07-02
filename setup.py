
from setuptools import setup, find_packages

setup(
    name="sqs_substitution_tool",
    version="0.1.0",
    author="Naveen Dandu",
    author_email="your_email@example.com",
    description="A toolkit for performing substitution-based SQS-style POSCAR generation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/naveen-dandu/sqs_substitution_tool",
    packages=find_packages(),
    install_requires=["pymatgen", "numpy", "pandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
