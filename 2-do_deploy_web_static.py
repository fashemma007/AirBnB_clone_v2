#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
import os.path

env.hosts = ['54.89.25.106', '52.3.241.66']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        arc = archive_path.split("/")  # split file path using /
        archive = arc[-1]
        base = archive.strip('.tgz')  # select the archive
        put(archive_path, '/tmp/')  # transfer the archive to server's /tmp
        main = "/data/web_static/releases/{}".format(base)
        # create a directory for the archive extraction
        sudo('mkdir -p {}'.format(main))
        sudo('tar -xzf /tmp/{} -C {}/'.format(archive, main))
        sudo('rm /tmp/{}'.format(archive))
        sudo('mv {}/web_static/* {}/'.format(main, main))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(main))
        return True
    except Exception:
        return False
