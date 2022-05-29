from abc import ABC, abstractmethod

class DimTableJob(ABC):

    def algorithm(self, queue_name):
        file_path = self.get_sqs_message(queue_name)
        file_data = self.read_file_from_s3(file_path)
        formated_data = self.prepare_data(file_data)
        self.populate_bridge_table(formated_data)
        insert_data = self.compare_and_update_data(formated_data)
        update_data_file_path = self.save_to_s3(insert_data)
        self.copy_to_redshift(update_data_file_path)

    def get_sqs_message(self, queue_name: str):
        return print(f"Getting data from sqs {queue_name}")

    def read_file_from_s3(self, file_path):
        return print(f"readind data from s3 {file_path}")

    @abstractmethod
    def prepare_data(self, file_data):
        ...

    def populate_bridge_table(self, formated_data):
        return print(f"populating bridge table ")

    @abstractmethod
    def compare_and_update_data(self, formated_data):
        ...

    def save_to_s3(self, insert_data):
        return print(f"Saving files into S3 ")

    def copy_to_redshift(self, update_data_file_path):
        return print(f"Copying data to redshift from {update_data_file_path}")


class DimContactJob(DimTableJob):

    def prepare_data(self, file_data):
        return print("Preparando os dados de Contato")

    def compare_and_update_data(self, formated_data):
        return print("Comparing Contacts data")



