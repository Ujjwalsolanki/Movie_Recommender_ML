from src.components.data_transformation import DataTransformation


class DataTransformationTrainingPipeline:

    def main(self):
        data_validation = DataTransformation()
        data_validation.initiate_data_transformation()


if __name__ == '__main__':
    try:
        obj = DataTransformation()
        obj.main()
    except Exception as e:
        raise e

