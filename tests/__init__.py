import unittest
from filesafe import Chroot

class ChrootTests(unittest.TestCase):
    def test_chroot(self):
        etc = Chroot('/etc')
        self.assertEquals(etc('/etc/filename'), '/etc/filename', 'File exists in chroot')
        self.assertFalse(etc('/filename'), 'File is outside of chroot')
if __name__ == '__main__':
    unittest.main()
