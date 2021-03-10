from lesson_pytest.file_helper import Api, FileHelper
import pytest
import os
from unittest import mock


@pytest.fixture
def temp_file(tmp_path):
    f = tmp_path / 'filename'
    f.write_text('CONTENT')
    return f

@pytest.fixture
def api():
    api = Api('api_key_secret')
    yield api
    api.close()

@pytest.fixture
def fh(api):
    fh = FileHelper(api)
    return fh


class TestFileHelper:
    def test_init(self):
        api = object()
        fh = FileHelper(api)
        assert fh.api is api

    def test_remove_file(self, fh, temp_file):
        fh.remove_file(temp_file)
        assert os.path.exists(temp_file) is False

    def test_upload_file(self, moked_prepare_file):
        fake_api = mock.MagicMock()

        # expected_data = object()
        # moked_prepare_file.return_value = expected_data

        fake_filepath = 'zapel'
        fh = FileHelper(fake_api)
        fh.upload_file(fake_filepath)

        # fake_api.request.assert_called()
        # fake_api.request.assert_called_once()
        fake_api.request.assert_called_once_with('POST', moked_prepare_file.return_value)

        moked_prepare_file.assert_called_once_with(fh, fake_filepath)





