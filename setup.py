"""Setup script for ASCII Art Generator."""

from setuptools import setup, find_packages
import os

# Read README for long description
long_description = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

setup(
    name="ascii-art-generator",
    version="4.0.0",
    author="Querulantenkind",
    description="A comprehensive terminal-based ASCII art generator with TUI editor, custom palettes, and advanced effects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ascii-art-generator",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    include_package_data=True,
    package_data={
        "palettes": ["*.json"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Text Processing :: Fonts",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Core dependencies (optional - core features work without these)
    ],
    extras_require={
        "image": [
            "Pillow>=10.0.0",
        ],
        "qr": [
            "qrcode[pil]>=7.4.0",
        ],
        "video": [
            "opencv-python>=4.5.0",
        ],
        "all": [
            "Pillow>=10.0.0",
            "qrcode[pil]>=7.4.0",
            "opencv-python>=4.5.0",
        ],
    },
    py_modules=[
        "ascii_art_generator",
        "ascii_art_pro",
        "ascii_art_editor",
    ],
    entry_points={
        "console_scripts": [
            "ascii-art=ascii_generator.cli:main",
            "ascii-art-generator=ascii_art_generator:main",
            "ascii-art-pro=ascii_art_pro:main",
            "ascii-art-editor=ascii_art_editor:main",
            "aag=ascii_art_generator:main",
            "aag-pro=ascii_art_pro:main",
            "aag-editor=ascii_art_editor:main",
        ],
    },
    keywords="ascii art generator terminal cli text image pattern animation",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ascii-art-generator/issues",
        "Source": "https://github.com/yourusername/ascii-art-generator",
        "Documentation": "https://github.com/yourusername/ascii-art-generator/blob/main/README.md",
    },
)

