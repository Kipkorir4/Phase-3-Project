# database/__init__.py

import sqlite3

# Establish a connection to the boot camp database
# The path './lib/database/bootcamp.db' can be adjusted as necessary
conn = sqlite3.connect('./lib/database/bootcamp.db')
cursor = conn.cursor()
