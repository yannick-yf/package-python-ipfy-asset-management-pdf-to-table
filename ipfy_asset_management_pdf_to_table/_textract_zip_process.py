from dataclasses import dataclass
import pandas as pd
import zipfile
import glob
import os

class TextractZipProcessResult(pd.DataFrame):
    musid: int
    place_id: str
    countryprecision: str
    avz_dptnum: int

@dataclass
class TextractZipToDataFrame:
        
    def unzip_textract_zip_file(
        path_to_zip_file: str,
        directory_to_extract_to: str
        ) -> pd.DataFrame:
        """
        Process and tranform data in Zip to pd.DataFrame
        Zip file is obtained from a manual process of using AWS textract services
        This class worked only for a specifc type of docuements from a specific bank
        """

        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)

        list_unzipped_files = os.listdir(directory_to_extract_to)

        # # initialize list elements
        # data = [10,20,30,40,50,60]
        
        # # Create the pandas DataFrame with column name is provided explicitly
        # df = pd.DataFrame(data, columns=['Numbers'])

        return list_unzipped_files