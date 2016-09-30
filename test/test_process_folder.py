from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import call

from test.utils import configure_return_value
from rawlib import process_folder


class ProcessFolderTest(TestCase):
    def setUp(self):
        self.directory = 'a/fake/dir'

    def test_process_folder_calls_miniature_on_all_raw_files_in_folder(self):
        size = 'a fake size'
        find_raws = Mock()
        find_raws.side_effect = configure_return_value('rawlib.find_raws',
                                                       [(call(self.directory),
                                                         [self.directory + '/a.nef',
                                                          self.directory + '/b.nef'
                                                          ])])
        miniature = Mock()

        process_folder(self.directory,
                       size=size,
                       find_raws_fn=find_raws,
                       miniature_fn=miniature)

        miniature.assert_has_calls([call(self.directory + '/a.nef', size),
                                    call(self.directory + '/b.nef', size)])
