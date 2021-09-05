from .utils import is_valid_alphabetical_string, is_valid_integer, is_valid_real_number


def generate_objects_report(file_name: str):
    """
    Generate report of the objects count in the given file

    :param file_name: Input file name
    :type file_name: str

    :returns Objects count
    :rtype object
    """

    alphanumerics_count = 0
    alphabetical_strings_count = 0
    integers_count = 0
    real_numbers_count = 0

    with open(file_name, 'r') as f:
        data = f.read()
        f.close()

    objects = data.split(',')

    for current in objects:
        if is_valid_alphabetical_string(current):
            alphabetical_strings_count += 1
        elif is_valid_integer(current):
            integers_count += 1
        elif is_valid_real_number(current):
            real_numbers_count += 1
        else:
            alphanumerics_count += 1

    return {
        'total_objects': len(objects),
        'alphanumerics': alphanumerics_count,
        'alphabetical_strings': alphabetical_strings_count,
        'integers': integers_count,
        'real_numbers': real_numbers_count,
    }
