from src.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:

    def main(self):
        data_validation = DataIngestion()
        data_validation.initiate_data_ingestion()


if __name__ == '__main__':
    try:
        obj = DataIngestion()
        obj.main()
    except Exception as e:
        raise e

