import time
import RPA.Tables
from RPA.Browser.Selenium import Selenium
from robocorp.http import download
import RPA.Tables
from RPA.Archive import Archive

lib = Selenium()
arc = Archive()


def first_task():
    lib.open_available_browser("https://robotsparebinindustries.com/#/", maximized=True)


def order_your_robot():
    lib.click_element_when_visible('//a[contains(text(), "Order your robot!")]')
    time.sleep(2)


def download_csv():
    download(url="https://robotsparebinindustries.com/orders.csv", overwrite=True)


def get_data_from_csv():
    tables = RPA.Tables.Tables()
    table = tables.read_table_from_csv("orders.csv")
    print("Tables", table)
    orders = []
    for row in table:
        order = {}
        for column in table.columns:
            order[column] = row[column]
        orders.append(order)
    print("orders", orders)
    return orders


def get_robot(row):
    if row is not None:
        for item in row:
            print("item", item)
            try:
                lib.click_element_when_visible('//button[contains(text(), "OK")]')
                lib.select_from_list_by_value('//select[@id="head"]', item["Order number"])
                lib.select_radio_button("body", item["Body"])
                lib.input_text('//input[@type="number"]', item["Legs"])
                lib.input_text("address", item["Address"])
                lib.click_button_when_visible('//button[@id="preview"]')
                lib.click_button_when_visible('//button[@id="order"]')
                while True:
                    try:
                        lib.find_element("order-another")
                        break
                    except:
                        lib.click_button('order')
                lib.screenshot('robot-preview-image', f'output/robot+{item["Order number"]}.png')
                time.sleep(3)
                lib.screenshot('receipt', f'output/robot+{item["Order number"]}.png')
                lib.click_button('order-another')
            except:
                pass


def archive():
    arc.archive_folder_with_tar('./output', 'output.tar', recursive=True)
    arc.list_archive('output.tar')
