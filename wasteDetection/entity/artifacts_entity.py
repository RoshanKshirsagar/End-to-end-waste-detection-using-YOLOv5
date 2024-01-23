from dataclasses import dataclass


# data ingestion related artifacts
@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str
    feature_store_path: str
    

# data validation related artifacts
@dataclass
class DataValidationArtifact:
    validation_status: bool