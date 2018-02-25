from setuptools import setup, find_packages
version = '0.2.9'

try:
    import pypandoc
    read_md = lambda f: pypandoc.convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='pychord',
    version=version,
    description="A library to handle musical chords in python.",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        ],
    keywords='music chord',
    author='Yuma Mihira',
    author_email='info@yurax2.com',
    url='https://github.com/yuma-m/pychord',
    license='MIT',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    zip_safe=True,
    long_description=read_md('README.md'),
    test_suite='test',
)
