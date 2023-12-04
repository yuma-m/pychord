import sys

from setuptools import setup, find_packages
version = '1.2.1'

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 6)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""PyChords only supports Python 3.6 and above.""")
    sys.exit(1)

setup(
    name='pychord',
    version=version,
    description="A library to handle musical chords in python.",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='music chord',
    author='Yuma Mihira',
    author_email='info@yuma.cloud',
    url='https://github.com/yuma-m/pychord',
    license='MIT',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    zip_safe=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    test_suite='test',
    python_requires=">=3.6",
)
