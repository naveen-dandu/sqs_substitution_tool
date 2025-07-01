from setuptools import setup, find_packages

setup(
    name="sqs_substitution_tool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pymatgen>=2022.0.17",
    ],
    entry_points={
        'console_scripts': [
            'sqs-substitute=scripts.sqs_prompt_substitute:main',
        ],
    },
    author="Naveen Dandu",
    description="A tool for pseudo-SQS random substitution in VASP POSCAR files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/naveen-dandu/sqs_substitution_tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)