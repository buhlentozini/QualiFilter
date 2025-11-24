from setuptools import setup, find_packages

setup(
    name="qualifilter",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0"
    ],
    entry_points={
        "console_scripts": [
            "qualifilter=qualifilter.cli:main",
        ],
    },
)
