"""Test Textract Zip Processs"""
import pandas as pd

from ipfy_asset_management_pdf_to_table import (
    TextractZipToDataFrame
)

def test_textract_zip_process_example_1():

    textract_zip = TextractZipToDataFrame(directory_to_extract_to = './tests/data_example/unzipped')

    list_file_unzipped= textract_zip.unzip_textract_zip_file(
        path_to_zip_file = './tests/data_example/example_1.zip'
    )

    unified_dataframe = textract_zip.get_csv_table_from_unzipped_file()

    assert len(list_file_unzipped) > 0
    assert unified_dataframe is not None

def test_textract_zip_process_example_2():

    textract_zip = TextractZipToDataFrame(directory_to_extract_to = './tests/data_example/unzipped')

    list_file_unzipped= textract_zip.unzip_textract_zip_file(
        path_to_zip_file = './tests/data_example/example_2.zip'
    )

    unified_dataframe = textract_zip.get_csv_table_from_unzipped_file()

    assert len(list_file_unzipped) > 0
    assert unified_dataframe is not None

def test_textract_zip_process_example_CANEXT_CC():

    textract_zip = TextractZipToDataFrame(directory_to_extract_to = './tests/data_example/unzipped')

    list_file_unzipped= textract_zip.unzip_textract_zip_file(
        path_to_zip_file = './tests/data_example/example_CANEXT_CC.zip'
    )

    unified_dataframe = textract_zip.get_csv_table_from_unzipped_file()

    assert len(list_file_unzipped) > 0
    assert unified_dataframe is not None

def test_textract_zip_process_example_CA_CC():

    textract_zip = TextractZipToDataFrame(directory_to_extract_to = './tests/data_example/unzipped')

    list_file_unzipped= textract_zip.unzip_textract_zip_file(
        path_to_zip_file = './tests/data_example/example_CA_CC.zip'
    )

    unified_dataframe = textract_zip.get_csv_table_from_unzipped_file()

    assert len(list_file_unzipped) > 0
    assert unified_dataframe is not None

def test_textract_zip_process_example_CA_CEL():

    textract_zip = TextractZipToDataFrame(directory_to_extract_to = './tests/data_example/unzipped')

    list_file_unzipped= textract_zip.unzip_textract_zip_file(
        path_to_zip_file = './tests/data_example/example_CA_CEL.zip'
    )

    unified_dataframe = textract_zip.get_csv_table_from_unzipped_file()

    assert len(list_file_unzipped) > 0
    assert unified_dataframe is not None

def test_textract_zip_process_example_BB_CC():

    textract_zip = TextractZipToDataFrame(directory_to_extract_to = './tests/data_example/unzipped')

    list_file_unzipped= textract_zip.unzip_textract_zip_file(
        path_to_zip_file = './tests/data_example/example_BB_CC.zip'
    )

    unified_dataframe = textract_zip.get_csv_table_from_unzipped_file()

    assert len(list_file_unzipped) > 0
    assert unified_dataframe is not None

def test_textract_zip_process_example_CA_LVTA():

    textract_zip = TextractZipToDataFrame(directory_to_extract_to = './tests/data_example/unzipped')

    list_file_unzipped= textract_zip.unzip_textract_zip_file(
        path_to_zip_file = './tests/data_example/example_CA_LVTA.zip'
    )

    unified_dataframe = textract_zip.get_csv_table_from_unzipped_file()

    assert len(list_file_unzipped) > 0
    assert unified_dataframe is not None