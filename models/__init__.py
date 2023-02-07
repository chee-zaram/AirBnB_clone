#!/usr/bin/python3
"""For creating a new file storage instance for the application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
