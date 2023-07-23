
# File Monitoring System

## How to Use

1. Download this repository to your local machine.

2. Install Python 3.x if you haven't already.

3. Open a terminal or command prompt and navigate to the project directory.

4. Create Virtual Environment.

5. Run the Data Generator in root directory using below command.

```python
python3 main.py data_generator
```

5. Run the File Monitor in root directory using below command.

```python
python3 main.py
```

6. Random Data Generator would generate data at interval of 2 seconds in ``src/generated_data`` folder. Have also added batching. 
7. File Monitor will dump search log at interval of 30 seconds in ``src/log_data`` folder. Have also added batching.
