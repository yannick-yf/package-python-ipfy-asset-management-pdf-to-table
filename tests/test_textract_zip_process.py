"""Test Textract Zip Processs"""
import pandas as pd

from ipfy_asset_management_pdf_to_table import (
    TextractZipProcessResult, TextractZipToDataFrame
)

def test_textract_zip_process():

    df = TextractZipToDataFrame.unzip_textract_zip_file()

    assert df.shape[0] > 0