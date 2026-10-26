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

