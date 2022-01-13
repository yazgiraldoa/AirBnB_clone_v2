#!/usr/bin/python3
"""
Fabric script that distributes an archive
to your web servers, using the function do_deploy
"""
from fabric.api import *
from datetime import datetime

env.hosts = ['34.138.220.245', '34.235.143.24']


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


def do_deploy(archive_path):
    """
    Function that deploys a local file to a server
    """
    try:
        f_path = "/data/web_static/releases/"
        file_ext = archive_path.split("/")[-1]
        file = file_ext.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}".format(f_path, file))
        run("tar -xzf /tmp/{} -C {}{}".format(file_ext, f_path, file))
        run("rm /tmp/{}".format(file_ext))
        run("mv {}{}/web_static/* {}{}/".format(f_path, file, f_path, file))
        run("rm -rf {}{}/web_static".format(f_path, file))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(f_path, file))
        return True
    except Exception as e:
        return False
