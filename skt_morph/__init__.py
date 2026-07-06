import os
from .db_builder import build_database_if_missing

# This automatically checks if the DB exists on the user's PC when they import your package.
# If it doesn't, it builds it instantly from the bundled JSON files.
build_database_if_missing()

# We will add future imports here, e.g., 
# from .analyzer import analyze
# from .generator import decline