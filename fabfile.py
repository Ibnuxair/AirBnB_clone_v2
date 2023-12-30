#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static.
"""

from fabric import task
from datetime import datetime

@task(name="do_pack")
def do_pack(c):
        # Create 'versions' folder if it doesn't exist
        versions_folder = "versions"
        c.run(f"mkdir -p {versions_folder}")

        # Current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        # Name of the archive
        archive_name = f"web_static_{timestamp}.tgz"

        # Command to create the .tgz archive
        cmd = f"tar -cvzf {versions_folder}/{archive_name} web_static"

        # Run the command
        result = c.run(cmd)

        # Check if the command executed successfully
        if result.ok:
            return f"{versions_folder}/{archive_name}"
        else:
            return None
