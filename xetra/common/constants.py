"""
File to store constants
"""

from enum import Enum
import enum

class S3FileTypes(Enum):
    """
    supported file types for S3BucketConnector
    """

    CSV = 'csv'
    PARQUET = 'parquest'

class MetaProcessFormat(Enum):
    """
    formation for MetaProcess class
    """

    META_DATE_FORMAT = '%Y-%m-%d'
    META_PROCESS_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    META_SOURCE_DATE_COL = 'source_date'
    META_PROCESS_COL = 'datetime_of_processing'
    META_FILE_FORMAT = 'csv'
    
