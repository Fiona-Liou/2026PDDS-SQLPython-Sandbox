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
# STEP 3: Task 1:Total Flight Count -- Baseline Task
# ==============================================================================
"""
Baseline Task: Total Flight Count
TODO:   Write a SQL query to count the total number of flights in the Flights table.
        Return the count as a single value.
"""

# Type your SQL query below
sql_task_1 = """

"""

# Execute SQL query and fetch the result

result_task_1 = None  # Replace this with the code to execute the query and fetch the result