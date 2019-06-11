# Publishing (Perfect) Python Packages On PyPI

This repo hosts slides and references for a talk I've given at PyCon Australia '18; PyCon UK '18; Python Glasgow, June '19; and upcoming EuroPython '19.

PDF exports of different versions the slide deck can be found here (probably improving chronologically):

* [PyCon Australia Slides](publish_on_pypi-pyconau18.pdf)
* [PyCon UK Slides](publish_on_pypi-pyconuk18.pdf)
* [Python Glasgow](publish_on_pypi-python_glasgow19.pdf)

# References

I referred to a bunch of different resources and projects when writing this talk. The primary sources I can think of are listed here:

## [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)

The official packaging documentation from the Python Packaging Authority.

## [The Attrs Project](https://github.com/python-attrs/attrs)

This project has an excellent example of a non-trivial, but sensible setup.py. I've learned so much by following the evolution of this project.

## [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html)

So much more than a source of python package templates, you'll find a bunch of project templates for different languages and ecosystems.

## [Ionel's Python Library Template](https://github.com/ionelmc/cookiecutter-pylibrary)

My preferred Python library template, with configuration for testing, CI etc. It most closely matches the advice in this talk.

## [Hitchikers Guide to Python Packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html)

An outdated, but still useful guide to packaging in Python, from Tarek Ziadé.

## [Setuptools Documentation](https://setuptools.readthedocs.io/en/latest/)

The official documentation of the setuptools library. Comprehensive but sometimes a little dense.

## [PIP Documentation](https://pip.pypa.io/en/stable/)

Official documentation for the PIP tool.


# Alternative Package Managers

## [Poetry](https://github.com/sdispater/poetry)

Aims to replace setup.py _and_ PIP.

## [Flit](https://github.com/takluyver/flit)

Aims to replace setup.py with something simpler and more declarative.

## [Conda](https://docs.conda.io/en/latest/)

A competitor to pip, largely used in the data community. Able to install much more than just python modules!