import re
import time
import os

current_directory = os.path.dirname(os.path.abspath(__file__))


class FileMonitor(object):
    def __init__(self, **kwargs):
        self.log_interval = kwargs.get("log_interval", 30)  # default 30 seconds
        self.relative_path = kwargs.get("relative_path", "generated_data/")
        self.search_log_relative_path = kwargs.get("search_log_relative_path", "log_data/")
        self.search_log_file_name = kwargs.get("search_log_file_name", "search_results.log")
        self.keyword = kwargs.get("keyword", "CDS")
        self.max_log_size = kwargs.get("max_log_size", 1024*1024)  # default 1MB

    def monitor_file(self):
        try:
            if not self.keyword:
                raise Exception("Please enter a keyword to search for count.")

            # Create the directory if it does not exist
            os.makedirs(os.path.join(current_directory, self.search_log_relative_path), exist_ok=True)

            search_log_file_name = os.path.join(current_directory, self.search_log_relative_path+self.search_log_file_name)

            while True:
                file_list = os.listdir(os.path.join(current_directory, self.relative_path))
                count = 0
                # iterate over all the files in the directory because we have implemented batching for files.
                for file in file_list:
                    file_name = os.path.join(current_directory, self.relative_path+file)

                    with open(file_name, "r") as file:
                        content = file.read()

                    count += len(re.findall(r'\b{}\b'.format(self.keyword), content))

                with open(search_log_file_name, "a") as log_file:
                    log_file.write(f"{file_name} - {count}\n")

                # Check log file size
                log_size = os.path.getsize(search_log_file_name)

                if log_size >= self.max_log_size:
                    # Create backup of log file and rename it
                    backup_file_name = f"{search_log_file_name}_{int(time.time())}.log"
                    os.rename(search_log_file_name, backup_file_name)

                time.sleep(self.log_interval)

        except FileNotFoundError as e:
            print(f"File not found. ", str(e))
            raise FileNotFoundError
