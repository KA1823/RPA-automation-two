import time
from file import first_task, order_your_robot, download_csv, get_data_from_csv, get_robot, archive


def minimal_task():
    first_task()
    order_your_robot()
    download_csv()
    csv_data = get_data_from_csv()
    get_robot(csv_data)
    archive()


minimal_task()
