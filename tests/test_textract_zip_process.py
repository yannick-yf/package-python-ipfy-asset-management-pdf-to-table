"""Test Textract Zip Processs"""
import pandas as pd

from ipfy_asset_management_pdf_to_table import (
    TextractZipToDataFrame
)

def test_textract_zip_process():

    list_file_unzipped = TextractZipToDataFrame.unzip_textract_zip_file(
        path_to_zip_file = './tests/data_example/example.zip',
        directory_to_extract_to = './tests/data_example/unzipped'
    )

    unifed_dataframe = TextractZipToDataFrame.get_csv_table_from_unzipped_file(
        directory_path_to_unzziped_zip =  './tests/data_example/unzipped'
    )

    assert len(list_file_unzipped) > 0
    assert unifed_dataframe is not None