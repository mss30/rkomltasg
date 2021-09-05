import os

from .utils import get_random_object


# Run this loop while the file size touches 2MB which is 2000000 Bytes in decimal number system.
def random_objects_generator(output_file_name, output_file_max_size):
    """
    Create a file of random objects with a maximum size

    :param output_file_name: Output file name
    :type output_file_name: str
    :param output_file_max_size: Output file max size
    :type output_file_max_size: int
    """
    open(output_file_name, 'w')

    with open(output_file_name, 'a') as f:
        # Just to avoid comma at the end of file
        f.write(str(get_random_object()))
        f.flush()

        while os.stat(output_file_name).st_size < output_file_max_size:
            f.write(',' + str(get_random_object()))
            f.flush()

        f.close()
