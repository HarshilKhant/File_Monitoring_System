import os
import time
from src.helpers.common_helpers.random_string_generator import RandomStringGenerator

current_directory = os.path.dirname(os.path.abspath(__file__))


class DataGenerator(object):

    def __init__(self, **kwargs):

        self.relative_path = kwargs.get("relative_path", "generated_data/")
        self.max_file_size = kwargs.get("max_file_size", 1024*1024)  # default 1MB
        self.max_write_loop = kwargs.get("max_write_loop", 100)
        self.time_interval = kwargs.get("time_interval", 2)
        self.file_name = kwargs.get("file_name", "random_data.txt")
        self.keyword = kwargs.get("keyword", "CDS")
        self.probability = kwargs.get("probability", 0.5)


    def write_data_to_file(self):
        write_loop = 1
        file_name = os.path.join(current_directory, self.relative_path+self.file_name)

        # Create the directory if it does not exist
        os.makedirs(os.path.join(current_directory, self.relative_path), exist_ok=True)

        while True:
            # Random String Generator with keyword and its probability
            random_string_generator = RandomStringGenerator(probability=self.probability, keyword=self.keyword)
            random_data = random_string_generator.generate_random_string()

            # Use 'with' statement for file handling to ensure proper closure
            with open(file_name, "a") as file:
                file.write(random_data + "\n")

            write_loop += 1

            file_size = os.path.getsize(file_name)

            if file_size > self.max_file_size:
                # Backup the data file and create new file.
                backup_file_name = f"{file_name}_{int(time.time())}.txt"
                os.rename(file_name, backup_file_name)
            elif write_loop > self.max_write_loop:
                # close resource for better OS resource utilization for some iterations
                file.close()

            time.sleep(self.time_interval)  # to control rate at which data is generated


