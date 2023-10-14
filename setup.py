import setuptools
import os

setuptools.setup(
    name="pytools", # Replace with your own username
    version="0.1",
    author="Maximilien Lehujeur",
    author_email="maximilien.lehujeur@gmail.com",
    description="",
    long_description="",
    long_description_content_type="",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
    ],
    scripts=[
        "pytools/pytprof.py",
        "pytools/pymprof.py",
        ],
    install_requires=['memory-profiler', 'line-profiler'],
    python_requires='>=3.7')
