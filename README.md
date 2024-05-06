Capital One Auto-Reimburser
===========================

[project](https://sr.ht/~logankirkland/capital-one-reimburse/) /
[repo](https://git.sr.ht/~logankirkland/capital-one-reimburse) /
[mailing list](https://lists.sr.ht/~logankirkland/capital-one-reimburse) /
[issues](https://todo.sr.ht/~logankirkland/capital-one-reimburse)

Warning
-------
This code uses automation tools to access your account. Review the terms
of service for your account and use this tool at your own risk.

Description
-----------

One feature of the Capital One Venture X credit card is the ability
to reimburse yourself for covered purchases using accrued points.
Unfortunately the UI for this process requires so many clicks that I
find my wrist is tired before I have been able to process all the
charges. This tool uses selenium to automate this reimbursement process.

Installation
------------

1. Install [Google Chrome](https://www.google.com/chrome/)
2. Download the version of chromedriver matching the version of your
   Chrome browser installation. See the
   [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
   site for download links. Extract and copy the binary to the root 
   directory of this project.
3. (Recommended) [Set up and activate](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
   a Python virtual environment
4. Install requirements: `python -m pip install -r requirements.txt`

Usage
-----

1. Edit `parameters.yaml` with your account credentials.
2. Run `python capital_one_reimburse.py`

Dependencies
------------

This code uses the following dependencies:

- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver),
  which is licensed under GPL-3.0.
- [selenium](https://github.com/SeleniumHQ/Selenium), which is licensed
  under Apache-2.0.
- This project is based on my [Selenium Tools library](https://git.sr.ht/~logankirkland/selenium-tools),
  which is licensed under MIT.