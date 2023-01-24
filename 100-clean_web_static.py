#!/usr/bin/python3
"""Fabric script that compartmentalizes web servers deployments"""
import os
from fabric.api import local
from fabric.api import env
from fabric.api import run
from fabric.api import lcd, cd

env.hosts = ['54.89.25.106', '52.3.241.66']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/school"


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives
    """
    number = 1 if int(number) == 0 else int(number)
    # Delete all unnecessary archives
    # (all archives minus the number to keep) in the versions folder
    archives = sorted(os.listdir("versions"))
    # print(archives)
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local(f"rm ./{archive}") for archive in archives]
    # Delete all unnecessary archives
    # (all archives minus the number to keep) in the
    # /data/web_static/releases folder of both web servers
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [arch for arch in archives if "web_static_" in arch]
        [archives.pop() for i in range(number)]
        # print(archives)
        [run("rm -rf ./{}".format(a)) for a in archives]

