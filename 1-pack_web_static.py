#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static.
"""

from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    # Current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # Name of the archive
    archive_name = f"web_static_{timestamp}.tgz"
    # Folder to store the archives
    versions_folder = "versions"

    # Create the versions folder if it doesn't exist
    if not os.path.exists(versions_folder):
        os.makedirs(versions_folder)

    # Command to create the .tgz archive
    cmd = f"tar -cvzf {versions_folder}/{archive_name} web_static"

    # Run the command
    result = c.local(cmd, capture=True)

    # Check if the command executed successfully
    if result.succeeded:
        return f"{versions_folder}/{archive_name}"
    else:
        return None

