from src.components.model_trainer import ModelTrainer


class ModelTrainingPipeline:

    def main(self):
        data_validation = ModelTrainer()
        data_validation.initiate_model_training()


if __name__ == '__main__':
    try:
        obj = ModelTrainer()
        obj.main()
    except Exception as e:
        raise e

