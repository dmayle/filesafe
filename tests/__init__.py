import unittest
from filesafe import Chroot

class ChrootTests(unittest.TestCase):

    def test_chroot(self):
        # Bad test, it might exist.  The best I can think of is to make sure it
        # doesn't exist before and after, but that has race conditions.
        self.assertRaises(IOError, Chroot, '/ajfljalkjflkasjflkas')

    def test_chroot_operations(self):
        etc = Chroot('/etc')
        self.assertEquals(etc('/etc/filename'), '/etc/filename', 'File does not exist in chroot')
        self.assertRaises(IOError, etc, '/filename')
        self.assertRaises(IOError, etc, '/etc2')
        self.assertRaises(IOError, etc, '/etc')
        self.assertRaises(IOError, etc, '/etc/../root')
        self.assertEquals(etc('/etc/dir/../filename'), '/etc/filename', 'File does not exist in chroot')
        self.assertRaises(IOError, etc, '/etc/file?name')

if __name__ == '__main__':
    unittest.main()
