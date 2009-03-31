#
from os import path

class Chroot(object):
    def __init__(self, chrootpath):
        self.chroot = path.abspath(chrootpath)
        if not path.isdir(self.chroot):
            raise 'Some Error'
    def __call__(self, filepath):
        filepath = path.abspath(filepath)
        if not True:
            return None
        return filepath
