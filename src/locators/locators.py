from pathlib import Path
from yaml import safe_load


def get_locators() -> dict:
    locators = {}

    for locator_file in Path("src", "locators").glob("*.yaml"):
        with open(locator_file, "r") as f:
            locators[locator_file.stem] = safe_load(f)

    return locators
