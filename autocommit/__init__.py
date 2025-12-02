from .cli import cli


# So that cli becomes part of the autocommit package
# Makes your package easier to import
# Makes the CLI function visible at top-level
# Keeps your package clean and well-structured
# Helps IDEs and tools find your functions
# Follows Python best practices




#File	      Purpose (One Line)
#setup.py	  Turns your project into a pip-installable package and creates the autocommit CLI command.
#init.py	  Makes autocommit/ a Python package and exposes cli() for top-level use.
#cli.py	      The actual working application—reads diff, calls Gemini, commits, pushes.
#publish.yml  Automatically builds & publishes the package when a release is created.