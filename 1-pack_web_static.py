#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Function that compress a folder (to targz) with Fabric
    """
    try:
        name = "web_static_" + datetime.now().strftime('%Y%m%d%H%M%S')
        local("mkdir -p versions")
        local("tar -czvf versions/" + name + ".tgz web_static")
        return name
    except Exception:
        return None
