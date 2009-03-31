import unittest
from filesafe import Chroot

class ChrootTests(unittest.TestCase):
    def test_chroot(self):
        etc = Chroot('/etc')
        self.assertEquals(etc('/etc/filename'), '/etc/filename', 'File exists in chroot')
        self.assertRaises(IOError, etc, '/filename')
        self.assertRaises(IOError, etc, '/etc2')
        self.assertRaises(IOError, etc, '/etc')

if __name__ == '__main__':
    unittest.main()
