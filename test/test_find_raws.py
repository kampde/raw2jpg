from unittest import TestCase
from unittest.mock import Mock, call

from rawlib import find_raws
from test.utils import configure_return_value


class TestFindRaws(TestCase):
    def test_find_raws_retyrns_raw_files_in_folder(self):
        self.folder = 'a/fake/dir'
        self.listdir = Mock()
        self.listdir.side_effect = configure_return_value('os.listdir',
                                                          [(call(self.folder),
                                                            ['a.nef',
                                                             'B.NEF',
                                                             'a.jpg',
                                                             'foo.txt',
                                                             '.raw2jpg.conf',
                                                             '.hidden',
                                                             'nef',
                                                             ])])
        self.assertEqual([self.folder + '/a.nef', self.folder + '/B.NEF'],
                         find_raws(self.folder, listdir=self.listdir))
