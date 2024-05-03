Selenium Tools
==============

[project](https://sr.ht/~logankirkland/selenium-tools/) / 
[repo](https://git.sr.ht/~logankirkland/selenium-tools) / 
[mailing list](https://lists.sr.ht/~logankirkland/selenium-tools) /
[issues](https://todo.sr.ht/~logankirkland/selenium-tools)

This is a simple template for a selenium web-based test library. It includes some tools
which help make selenium-based tests more robust and reliable.

- [Description](#description)
- [File structure](#file-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Command line usage](#command-line-usage)
- [Reporting](#reporting)

File structure
--------------

- `selenium-tools` - project root directory
    - `src` - source code root directory
        - `.venv` - Python virtual environment (created during installation)
        - `driver` - module containing basic selenium webdriver code
        - `locators` - selenium locators and related Python code
        - `pages` - code related to the Page Object Model
        - `tests` - test code
    - `chromedriver.exe` - chromedriver (created during installation)
    - `parameters.yaml` - test configuration file
    - `readme.md` - this readme
    - `requirements.txt` - Python requirements for installation using pip

Installation
------------

### Prerequisites

This guide assumes the following prerequisites have been met:

- Chrome browser installed

### Create Python virtual environment

Change directory to the project root directory, then execute the following command to
create the virtual environment:

```shell
python -m venv .venv
```

Then activate the virtual environment using the command appropriate for your shell.
See [the documentation](https://docs.python.org/3/library/venv.html#how-venvs-work) for
more info.

### Download chromedriver

Download the version of chromedriver matching the version of your Chrome browser
installation. See
the [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/) site
for download links. Extract the `.zip` file and copy the chromeriver file to the root
project directory.

### Install Python requirements

The required Python modules are listed in `requirements.txt`. Install them in your
activated virtual environment using:

```shell
python -m pip install -r requirements.txt
```

Configuration
-------------

Test configuration parameters are contained in `parameters.yaml`.

Command line usage
------------------

In the base project directory with the configured virtual environment activated, execute
the following to run all tests in the `tests.py` module:

```shell
python -m unittest tests
```

Run a specific test suite using:

```shell
python -m unittest tests.ExampleTestSuite
```

Run a specific test case using:

```shell
python -m unittest tests.ExampleTestSuite.test_example_test
```

See [unittest documentation](https://docs.python.org/3/library/unittest.html) for more
details.

Reporting
---------

TODO