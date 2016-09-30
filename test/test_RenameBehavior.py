from unittest import TestCase
from unittest.mock import Mock

from behaviors import RenameBehavior


class TestRenameBehavior(TestCase):
    def setUp(self):
        self.os = Mock()
        self.sut = RenameBehavior(os_mod=self.os)

    def test_apply_renames_the_file(self):
        self.sut.apply('some/raw/file')
        self.os.rename.assert_called_once_with('some/raw/file',
                                               'some/raw/file.discarded')

