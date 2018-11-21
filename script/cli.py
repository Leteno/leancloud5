
import os, subprocess

def execute(cmd, path):
    """
    return subprocess ok, OUTPUT
    """

    oldPath = os.getcwd()
    os.chdir(path)

    exitcode, output = subprocess.getstatusoutput(cmd)

    os.chdir(oldPath)

    ok = not exitcode

    return ok, output
