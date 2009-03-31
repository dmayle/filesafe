#
from os import path
from re import compile

INVALID_FILE_CHARS = compile(r'[?%*:|"<>/]')
INVALID_DIR_CHARS = compile(r'[?%*:|"<>]')
filetypes = {'dir': INVALID_DIR_CHARS,
             'file': INVALID_FILE_CHARS}

class Chroot(object):
    def __init__(self, chrootpath, sanitize_method=None):
        if sanitize_method not in [None, 'strip', 'encode']:
            sanitize_method = None
        self.sanitize_method = sanitize_method

        # For safety reasons, the chroot path must start with a seperator to
        # remove directory confusion. e.g. /etc and /etc2
        self.chroot = path.abspath(self.__sanitize('dir', chrootpath)) + path.sep

        if not path.isdir(self.chroot):
            raise IOError

    def __sanitize(self, filetype, dirname):
        if not self.sanitize_method:
            if filetypes[filetype].search(dirname):
                raise IOError
            return dirname
        raise NotImplementedError('The only sanitization method currently supported is none')

    def __call__(self, filepath):
        filechroot = path.abspath(self.__sanitize('dir', filepath))

        # Test
        if not filechroot.startswith(self.chroot):
            raise IOError
        if filechroot == self.chroot:
            raise IOError

        # Return the modified version.  We should change this to edit the
        # passed in variable.  Less confusion
        return filechroot
