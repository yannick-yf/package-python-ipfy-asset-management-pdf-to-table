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
        #grid_data_list: dict
        ) -> pd.DataFrame:
        """
        Process and tranform to pd.DataFrame needed data from zip 
        Zip file is obtained from a manual process of using AWS textract services
        This class worked only for a specifc type of docuements from a specific bank
        """

        # initialize list elements
        data = [10,20,30,40,50,60]
        
        # Create the pandas DataFrame with column name is provided explicitly
        df = pd.DataFrame(data, columns=['Numbers'])

        return df