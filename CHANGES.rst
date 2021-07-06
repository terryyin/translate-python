Changelog
---------

3.6.1
-----

* Add LibreTranslate

3.5.0
-----

* Add sphinx documentation
* Update readme.

3.4.1
-----

* Makefile: Add a make release command
* Add twine to dev requirements.

3.4.0
-----

* Refactor: Create a folder to add all providers instead to let in a single file
* Add Microsoft provider
* Add more documentation to all providers (Translated-MyMemory and Microsoft Translator)
* Add arguments to change the default provider using translate-cli


3.3.0
-----

* Refactor translate-cli (command line interface) Using Click library instead of ArgParser
* Unify translate-cli and main to avoid duplicate code
* Add documentation to be used on helper commands on translate-cli
* Remove unnecessary code
* Refactor setup to complete information in the PKG-INFO used by PyPI


3.2.1
-----

* Change the license from "BEER-WARE" to MIT

3.2.0
-----

* Add multiple providers suport

3.1.0
-----

* Apply Solid Principles
* Organize Project
* Add pre-commit, pytest
* Add new Make file
* Add new test cases

3.0.0
-----

* General Refactor
* Remove urllib to use requests
* Refactor methods names removing google from then
* Apply PEP8
* Change contructor to keep it the code simple

2.0.0 (2017-11-08)
------------------

* initial release using changes file
