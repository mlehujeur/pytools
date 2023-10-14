import setuptools
import os
import subprocess


class MakeTheDoc(setuptools.Command):
    description = "Generate Documentation Pages using Sphinx"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(
            ['sphinx-build docs/sources docs/_build'], shell=True)
        

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
    cmdclass={
        'doc': MakeTheDoc,
        },
    install_requires=[
        'memory-profiler', 'line-profiler',
        'sphinx', 'sphinx-rtd-theme', 'myst-parser',  
        ],
    python_requires='>=3.7')
