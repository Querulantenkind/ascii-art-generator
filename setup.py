"""Setup script for ASCII Art Generator."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ascii-art-generator",
    version="1.0.0",
    author="Querulantenkind",
    description="A terminal-based ASCII art generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pyfiglet>=1.0.2",
        "Pillow>=10.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ascii-art=ascii_generator.cli:main",
        ],
    },
)

