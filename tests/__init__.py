import os
from database import *

# Delete old library.db
if os.path.exists("library.db"):
    os.remove("library.db")

# Create a new one with sample data
init_database()
add_sample_data()