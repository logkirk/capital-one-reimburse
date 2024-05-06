from selenium.common import TimeoutException
from yaml import safe_load

from src.driver.webdriver import ChromeDriver
from src.pages.login import LoginPage
from src.pages.purchases import PurchasesPage
from src.utility.utility import random_sleep


with open("parameters.yaml", "r") as f:
    parameters = safe_load(f)


driver = ChromeDriver()

login_page = LoginPage(driver, parameters)
login_page.open()
login_page.log_in()

purchase_page = PurchasesPage(driver, parameters)
purchase_page.open()

reimbursed = []
while True:
    purchase_page = PurchasesPage(driver, parameters)
    purchase_page.open()
    try:
        card = purchase_page.get_first_purchase_card()
    except TimeoutException:
        break  # No more redeemable purchases
    purchase_page.action_chain.click(card).perform()  # Must interact to load card text
    date = purchase_page.get_purchase_date(card)
    merchant = purchase_page.get_purchase_merchant(card)
    cost = purchase_page.get_purchase_cost(card)
    miles_available, miles_redeemed, remaining_miles, confirmation = (
        purchase_page.reimburse(card)
    )
    print(
        f"Reimbursed transaction: {date} {merchant} {cost}\n"
        f"    Miles available: {miles_available}\n"
        f"    Miles redeemed: {miles_redeemed}\n"
        f"    Miles remaining: {remaining_miles}\n"
        f"    Confirmation: {confirmation}"
    )
    reimbursed.append(
        (
            date,
            merchant,
            cost,
            miles_available,
            miles_redeemed,
            remaining_miles,
            confirmation,
        )
    )
    random_sleep(0, 1)

with open("report.csv", "w+") as f:
    f.writelines(
        [
            "date,merchant,cost,miles_available,miles_redeemed,remaining_miles,confirmation\n"
        ]
        + [
            f'"{i[0]}","{i[1]}","{i[2]}","{i[3]}","{i[4]}","{i[5]}","{i[6]}"\n'
            for i in reimbursed
        ]
    )
