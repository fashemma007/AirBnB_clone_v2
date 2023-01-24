#!/usr/bin/python3
"""web server distribution"""
from fabric.api import *
from fabric.state import commands, connections
import os.path

env.hosts = ['54.89.25.106', '52.3.241.66']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/school"


def do_clean(number=0):
    """deletes out-of-date archives"""
    local('ls -t ~/AirBnB_Clone_V2/versions/').split()
    with cd("/data/web_static/releases"):
        target = sudo("ls -t .").split()
    paths = "/data/web_static/releases"
    number = int(number)
    if number == 0:
        num = 1
    else:
        num = number
    if len(target) > 0:
        if len(target) == number or len(target) == 0:
            pass
        else:
            cl = target[num:]
            for i in range(len(cl)):
                local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(target[-1]))
        rem = target[num:]
        for j in range(len(rem)):
            sudo('rm -rf {}/{}'.format(paths, rem[-1].strip(".tgz")))
    else:
        pass
