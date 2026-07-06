import os
from .db_builder import build_database_if_missing
from .analyzer import analyze

# Auto-builds the database from JSONs on first import
build_database_if_missing()

# Expose the API to the user
__all__ = ["analyze"]