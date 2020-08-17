# read file
import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Functions can only run on Linux Systems."
    print("Doing Something.")

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            print(file.read())
    except FileNotFoundError as file_error:
        print(file_error)
finally:
    print('Cleaning up. irrespective of any exceptions.')