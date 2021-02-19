import typer
import os


# Class definitions


class ResultObj(object):
    def __init__(self, file: str, **kwargs):
        self.file = file
        for k, value in kwargs.items():
            setattr(self, k, value)

    def __str__(self):
        return self.file

    def __repr__(self):
        return self.file

    def write_result_files(self, target_folder):
        file, _ = self.file.split(".")
        new_file_name = f"{file}.txt"
        target_file = os.path.join(target_folder, new_file_name)
        f = open(target_file, "a")
        f.write("Test")
        f.close()


class FileObj(object):
    """File Obj for file data storage and process logic

    Each File obj represent a File to a .PF file.
    """

    def __init__(self, file, file_path):
        """Initialize the input file data

        :param file: file name
        :param file_path: full file path
        """
        self.file = file
        self.file_path = file_path

    def __repr__(self):
        return self.file

    def __str__(self):
        return self.file

    def process(self):
        """Process the

        :return: ResultObj
        """
        with open(self.file_path, "r") as f:
            data = f.read()
        return self.parse_data(data)

    def parse_data(self,data):
        result = {}
        return ResultObj(self.file, **result)


# util function
def prefix_folder_path(file, folder):
    return (file, os.path.join(folder, file))


def main(folder: str):
    print(os.getlogin())
    # Get the target folder
    typer.echo(f"Checking {folder}")
    # list all files
    files = os.listdir(folder)
    # make list of full file path
    abs_file_list = [prefix_folder_path(file, folder) for file in files]
    # make list of file instances for every files
    file_obj_list = [FileObj(*file) for file in abs_file_list]
    # process file objects and generate array of result objects
    result_obj_list = [file_obj.process() for file_obj in file_obj_list]
    # generate final result files
    # make a new dir results
    result_directory = os.path.join(folder, "results")
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)
    # write results in to a text file (later to excel file)
    for result in result_obj_list:
        result.write_result_files(result_directory)


if __name__ == "__main__":
    typer.run(main)
    print("Complete")
