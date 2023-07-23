import time
import sys
from src.data_generator import DataGenerator
from src.file_monitor import FileMonitor


def start_data_generator():
    try:
        data_generator = DataGenerator()
        data_generator.write_data_to_file()
    except Exception as e:
        print("Error in Data Generator " + str(e))


def start_file_monitor(retry_count=0):
    try:
        file_monitor = FileMonitor()
        file_monitor.monitor_file()
    except FileNotFoundError as e:
        if retry_count < 10:
            print("Retrying After 30 seconds")
            retry_count += 1
            time.sleep(3)
            start_file_monitor(retry_count)
        else:
            print("File Not Found Error in File Monitor: "+str(e))
    except Exception as e:
        print("Error in File Monitor " + str(e))


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) >= 2 and sys.argv[1] == "data_generator":
        start_data_generator()
    else:
        start_file_monitor()
