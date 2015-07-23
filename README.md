Python decorators in detail
===========================
EuroPython 2015 training session.


# Installation

- Download / checkout / clone this repository and enter its folder.
- Install **Python 2.7**: https://www.python.org/downloads/ (sorry, no Py3k yet :disappointed: )
- Install **pip**: https://pypi.python.org/pypi/pip
- Install **virtualenv**: `pip install virtualenv`
- Create and enable a virtualenv:

```shell
$ virtualenv decorators_venv
New python executable in /WHAT/EVER/PATH/decorators/bin/python
Installing setuptools, pip...done.
$ source /WHAT/EVER/PATH/decorators/bin/activate
```

- Install the **requirements.txt** file:

```shell
$ pip install -r requirements.txt
Downloading/unpacking git+git://github.com/pablito56/pydemo.git (from -r requirements.txt (line 3))
...
Successfully installed Pygments nose readline pydemo
Cleaning up...
```


# Usage

All the training content is written down in Python scripts and designed to be executed with [pydemo](https://github.com/pablito56/pydemo "pydemo GitHub repository") interactive interpreter:
```shell
$ pydemo mod_00_welcome.py
Loaded 1 files, 7 code blocks
Python 2.7.2 (default, Oct 11 2012, 20:14:37)
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(DemoHistoryConsole)
>>>
#-*- coding: utf-8 -*-
'''
MOD 00: What is Python?
'''

'\nMOD 00: What is Python?\n'
>>>
#===============================================================================
# EXERCISE: Execute the following command:
#     $ python -c "import this"
#===============================================================================

>>>
#===============================================================================
# From official website ( http://www.python.org/ ):
#
#     Python is a programming language that lets you work more quickly and integrate
#     your systems more effectively. You can learn to use Python and see almost
#     immediate gains in productivity and lower maintenance costs.
#
#===============================================================================

>>>
```

New explanations and examples will appear in the interpreter when pressing INTRO without introducing a command. It is also posible to manually execute other code to play around with the examples.
