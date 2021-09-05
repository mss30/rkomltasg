import random
import string

# Constants for generate object functions
MAX_GENERATED_STRING_SIZE = 40
MAX_GENERATED_NUMBER_RANGE = 2000000  # The max value here can be `sys.maxsize`


def is_valid_alphabetical_string(string_object: str):
    """
    Check weather the given string contain alphabets only.

    :param string_object: A random string object
    :type string_object: str

    :return: True if given string is valid alphabetical string, otherwise False
    :rtype bool
    """
    return string_object.isalpha()


def is_valid_integer(string_object: str):
    """
    Check weather the given string is integer of not.

    :param string_object: A random string object
    :type string_object: str

    :return: True if given string is valid integer, otherwise False
    :rtype bool
    """
    if string_object[0] == '-':
        return string_object[1:].isdigit()
    return string_object.isdigit()


def is_valid_real_number(string_object: str):
    """
    Check weather the given string is real number or not.

    :param string_object: A random string object
    :type string_object: str

    :return: True if given string is valid real number, otherwise False
    :rtype bool
    """
    try:
        return float(string_object)
    except ValueError:
        return False


def get_random_string(char_choice, max_string_size=MAX_GENERATED_STRING_SIZE):
    """
    Generate a random string with given character and range.

    :param char_choice: Id or List of ids
    :type char_choice: Sequence
    :param max_string_size: Maximum size of the string to be generated.
           Default value is defined by the constant MAX_STRING_SIZE
    :type max_string_size: int

    :returns: a random string
    :rtype: str
    """
    string_length = random.randrange(1, max_string_size)
    return ''.join(random.choice(char_choice) for _ in range(string_length))


def get_random_alphabetic_string():
    """
    Generate a random alphabetical string.

    Note: String with both upper and lower case will be generated as the requirements
    only specify the object type i.e. alphabetical strings

    :returns: a random string with alphabets only
    :rtype: str
    """
    return get_random_string(char_choice=string.ascii_letters)


def get_random_alphanumeric_string():
    """
    Generate a random alphanumeric string.

    Note: String with both upper and lower case will be generated as the requirements
    only specify the object type i.e. alphanumerics

    :returns: a random string with alphabets and digits
    :rtype: str
    """
    return get_random_string(char_choice=string.ascii_letters + string.digits)


def get_random_integer():
    """
    Generate a random integer within range of constant MAX_NUMBER (+ve + -ve).

    :returns: a random integer between a given range
    :rtype: int
    """
    return random.randint(-MAX_GENERATED_NUMBER_RANGE, MAX_GENERATED_NUMBER_RANGE)


def get_random_real_number():
    """
    Generate a random real number within range of constant MAX_NUMBER (+ve + -ve).

    :returns: a random real number between a given range
    :rtype: float
    """
    return random.uniform(-MAX_GENERATED_NUMBER_RANGE, MAX_GENERATED_NUMBER_RANGE)


def get_random_object():
    """
    Generate a random object from the given list i.e.
        - alphabetical string
        - alphanumeric string
        - integer
        - real number

    :returns: a random object
    :rtype: str or int or float
    """

    return random.choice([
        get_random_alphabetic_string,
        get_random_alphanumeric_string,
        get_random_integer,
        get_random_real_number
    ])()
