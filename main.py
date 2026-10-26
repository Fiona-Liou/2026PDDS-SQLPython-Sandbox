"""
PDDS Workshop: Python & SQLite3 On-Hand Workshop
Database: AirlineDB_2026.DB
"""

# Importing the required libraries
import os
import sqlite3

# ==============================================================================
# STEP 1: Locate Database File
# Using os.path prevents "unable to open database" errors caused by different VS Code working dirs.
# ==============================================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "AirlineDB_2026.db")
if not os.path.exists(DB_PATH):
    print(f"[Error] Database file not found at: {DB_PATH}")
    print("Please make sure AirlineDB_2026.db is in the same folder as this script.")
    exit(1)

# ==============================================================================
# STEP 2: Connect to SQLite Database
# ==============================================================================



# ==============================================================================
# STEP 3: Task & Try
# ==============================================================================
"""
Task 1: Total Flight Count -- Baseline Question
TODO:   Write a SQL query to count the total number of flights in the Flights table.
        Return the count as a single value.
"""

# Type your SQL query below
sql_task_1 = """

"""

# Execute SQL query and fetch the result

# Replace this with the code to execute the query and fetch the result
result_task_1 = None

print("Task 1: Total Flight Count")
print(f"Total number of flights: {result_task_1}")
# Expected Output: 19

"""
Task 2: Flight Summary by Origin City
TODO:   Modify the SQL query below to show:
        origin city, count of flights, and average fare (rounded to 2 decimal places)
        Group by origin and order by flight count descending.
"""

# Type your SQL query below
sql_task_2 = """

"""
# Execute SQL query and fetch the result

# Replace this with the code to execute the query and fetch the result
result_task_2 = None

print("Task 2: Flight Summary by Origin City")
print("Origin City | Flight Count | Average Fare")
# Print all the results

# Expected Output:
# Origin City | Flight Count | Average Fare
# Los Angeles | 8 | 475.59
# ...

"""
Task 3: Join Flight with Aircraft
TODO:   Find which aircraft model is used for each flight from Madison.
"""

# Type your SQL query below
sql_task_3 = """

"""

# Execute SQL query and fetch the result

# Replace this with the code to execute the query and fetch the result
result_task_3 = None

print("Task 3: Join Flight with Aircraft")
print("Flight Number | Destination | Aircraft Name | Aircraft Model | Fare")
# Print all the results

# Expected Output:
# Flight Number | Destination | Aircraft Name | Aircraft Model | Fare
# 4884 | Chicago | Piper | Archer III | 112.45
# ...