from setuptools import setup, find_packages

setup(
    name="ai_daily",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
    ],
    entry_points={
        "console_scripts": [
            "ai_daily=src.cli:main",
        ],
    },
) 