import importlib
import sys
import os
import pip
import subprocess
from sys import stdout


class PackageManager:

    def __init__(self):
        self.pip = [sys.executable, "-m", "pip"]

    def install_package(self, package_name):
        try:
            subprocess.call(self.pip + ["install", package_name])
        except CalledProcessError:
            print('Error!')
            print(package_name, 'is not installed')

    def check_cmd(self, cmd):
        importlib.import_module(cmd)
        for i in cmd.includes:
            try:
                importlib.import_module(i)
            except ImportError:
                print("test")
                self.install_package(i)

