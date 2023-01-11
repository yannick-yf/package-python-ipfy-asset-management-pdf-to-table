"""Test Textract Zip Processs"""
import pandas as pd

from ipfy_asset_management_pdf_to_table import (
    TextractZipToDataFrame
)

def test_textract_zip_process():

    list_file_unzipped = TextractZipToDataFrame.unzip_textract_zip_file(
        path_to_zip_file = './ipfy_asset_management_pdf_to_table/data/pdf_awstextract_output_zip/Releve_n_001_du_02_01_2023.zip',
        directory_to_extract_to = './ipfy_asset_management_pdf_to_table/data/unzipped_files'
    )

    unifed_dataframe = TextractZipToDataFrame.get_csv_table_from_unzipped_file(
        directory_path_to_unzziped_zip = './ipfy_asset_management_pdf_to_table/data/unzipped_files'
    )

    assert len(list_file_unzipped) > 0
    assert unifed_dataframe is not None