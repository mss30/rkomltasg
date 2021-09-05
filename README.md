# My Random Objects Generator

A simple API which generates four (4) types of printable random objects and store
them in a single file, each object will be separated by a ",". These are the 4 objects:
alphabetical strings, real numbers, integers, alphanumerics.

Sample extracted output:

hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, lizierdjfklaasf,
123192u3kjwekhf, 89181811238,122, nmarcysfa900jkifh , 3.781, 2.11, ....

Output file size is limit by an app level config variable named `OUTPUT_FILE_MAX_SIZE`.

### Accessing the Application

URL to access the application is `localhost:5000`.

The application provide three different APIs:
- generate - To generate the required file on server
- download - To download the generated file
- report - To calculate number of different objects in the generated file

**MSS**
