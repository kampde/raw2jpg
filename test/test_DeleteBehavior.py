from unittest import TestCase
from unittest.mock import Mock

from behaviors import DeleteBehavior


class TestDeleteBehavior(TestCase):
    def setUp(self):
        self.os = Mock()
        self.sut = DeleteBehavior(os_mod=self.os)

    def test_apply_deletes_the_file(self):
        self.sut.apply('some/raw/file')
        self.os.remove.assert_called_once_with('some/raw/file')

