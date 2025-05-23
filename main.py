import subprocess

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_element_by_xpath(driver: webdriver.Firefox, xpath: str):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                xpath,
            )
        )
    )


def check_tickets():
    ticket_page = "https://atleta.cc/e/zRLhtOq7pOcB/resale"

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    with webdriver.Firefox(
        service=Service(executable_path="/tmp/geckodriver"),
        options=options,
    ) as driver:
        driver.get(ticket_page)
        try:
            tickets = get_element_by_xpath(
                driver=driver,
                xpath="/html/body/div/div/div[2]/div[2]/div/div/div[1]/h5/span[1]",
            )
            n_tickets = tickets.text.split(" ")[0]

            if int(n_tickets) > 0:
                reserved_or_buy_button = get_element_by_xpath(
                    driver=driver,
                    xpath="/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/button",
                )
                print(
                    f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {n_tickets} available, {reserved_or_buy_button.text}"
                )
                if reserved_or_buy_button.text != "Reserved":
                    subprocess.run(["open", ticket_page])
                    subprocess.run(
                        ["open", "https://forms.4daagse.nl/registratienummer-vergeten"]
                    )
            else:
                print(
                    f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {n_tickets} available"
                )
        except Exception as e:
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]Error: Element not found or took too long to load.",
                e,
            )


if __name__ == "__main__":
    check_tickets()


# full_xpath_reserve_button = (
#     "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]"
# )
