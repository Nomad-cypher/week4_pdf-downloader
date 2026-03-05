import unittest # Import test module
from unittest.mock import patch, Mock # Import mocking functions
from pdf_download import * # Import all functions and variables

class test_validator(unittest.TestCase):
    @patch('pypdf.PdfReader')
    def test_validatePDF(self, mock_reader):
        mock_response = Mock()

        validatePDF("some string")

        instance.mo


class test_download(unittest.TestCase):
    @patch('pd.isna')
    @patch('os.path.exists')
    @patch('urllib.request.urlopen')
    @patch('pdf_download.validatePDF')
    def test_downloadPDF(self, mock_isna, mock_exists, mock_urlopen, mock_validate):
        instance_isna = mock_isna.return_value

        downloadPDF("C/Documents/testfolder/testfile", 67)

        instance_isna.mock_isna.assert_called_with("C/Documents/testfolder/testfile")