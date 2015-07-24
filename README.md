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
Loaded 1 files, 4 code blocks
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(DemoHistoryConsole)
>>>
#=======================================================
#=======================================================
#     Welcome to PYTHON OBJECTS ESSENTIALS training
#=======================================================
#=======================================================

>>>
#=======================================================
# - REQUIREMENTS:
#    - Code at https://github.com/pablito56/decorators
#    - Follow README.md instructions
#=======================================================

>>>
print "- BIO:"
print "\tPablo Enfedaque Vidal"
print "\t@pablitoev56"
print "\tTechnical Manager @ Skyscanner"

- BIO:
	Pablo Enfedaque Vidal
	@pablitoev56
	Technical Manager @ Skyscanner
>>>
print "READY?"

READY?
>>>
No more demo code available. Execute '%reload_files [FILENAMES]' to reload
```

New explanations and examples will appear in the interpreter when pressing INTRO without introducing a command. It is also posible to manually execute other code to play around with the examples.
