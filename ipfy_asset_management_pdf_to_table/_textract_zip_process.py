from dataclasses import dataclass
from typing import List
import pandas as pd
import zipfile
import glob
import os

# class TextractZipProcessResult(pd.DataFrame):
#     musid: int
#     place_id: str
#     countryprecision: str
#     avz_dptnum: int

@dataclass
class TextractZipToDataFrame:
    """
    Class that take as input AWS textract manual zip output 
    Unzip the file and concat all the table found in the pdf
    Only valid on pdf from Credit Agricole Alsace
    """
        
    def unzip_textract_zip_file(
        path_to_zip_file: str,
        directory_to_extract_to: str
        ) -> List[str]:
        """
        Process and tranform data in Zip to pd.DataFrame
        Zip file is obtained from a manual process of using AWS textract services
        This class worked only for a specifc type of docuements from a specific bank
        """

        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)

        list_unzipped_files = os.listdir(directory_to_extract_to)

        return list_unzipped_files

    def get_csv_table_from_unzipped_file(
            directory_path_to_unzziped_zip: str
            ) -> pd.DataFrame:
            """
            Process and only keep the table.csv files needed
            Delete all non csv file from the unzipped folder
            """

            # Read all the file containing table into one unique table and return the table
            unifed_table = pd.concat(
                map(
                    pd.read_csv, glob.glob(
                        os.path.join(
                            directory_path_to_unzziped_zip, 
                            "table-*.csv")
                        )
                    )
                )
            
            if unifed_table.shape[0] == 0:
                unifed_table = pd.DataFrame()

            # Delete all the file in folder
            for f in os.listdir(directory_path_to_unzziped_zip):
                os.remove(os.path.join(directory_path_to_unzziped_zip, f))

            return unifed_table

