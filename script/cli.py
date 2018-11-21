
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

def execute1(cmd):
    exitcode, output = subprocess.getstatusoutput(cmd)
    return not exitcode, output

def execute2(cmd):
    subprocess.call(cmd.split(' '))

def execute3(cmd):
    subprocess.Popen(cmd.split(' ')).communicate()

def execute4(cmd):
    os.popen(cmd).read()

def execute5(cmd):
    args = cmd.split(' ')
    subprocess.Popen(os.P_WAIT, args[0], args).poll()