#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import env
from fabric.api import run
from fabric.api import put
from os.path import exists

env.hosts = ['54.89.25.106', '52.3.241.66']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/id_rsa"

def do_deploy(archive_path):
    """
    Deploys static content to server
    Return
    --
    * archive_path
    * False : if archive_path doesn't exist
    """

    if exists(archive_path) is False:
        return False
    try:
        name = archive_path.split("/")[-1]
        folder = name.split(".")[0]
        path = "/data/web_static/releases/"
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')
        # extract contents
        run(f"tar -xzf /tmp/{name} -C {path}")
        # rename extracted folder to version's name
        run(f"mv {path}web_static {path}{folder}")
        # Delete the archive from the web server
        run(f"rm -rf /tmp/{name}")
        # Delete the sym-link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')
        # update symbolic link to point to the new version
        run(f"sudo ln -sf {path}{folder} /data/web_static/current")
        return True
    except Exception:
        return False
