def format_name(string_to_process: str) -> str:
    """
    Takes a string and processes it to format it in a name way.
    :param string_to_process: The string the user wishes to process.
    :return: Formatted string.
    """
    string_to_process = string_to_process.lstrip()
    list_to_process = string_to_process.split(",")
    string_to_process = list_to_process[1] + list_to_process[0]
    string_to_process = string_to_process.strip()
    string_to_process = string_to_process.title()
    list_to_process = string_to_process.split("   ")
    string_to_process = "".join(list_to_process)
    return string_to_process

def format_title(string_to_process: str) -> str:
    """
    Takes a string and formats it like a title.
    :param string_to_process: The string the user wishes to process.
    :return: Formatted string.
    """
    string_to_process = string_to_process.replace(" ", "")
    string_to_process = string_to_process.replace(",", " ")
    string_to_process = string_to_process.replace("::", " ")
    string_to_process = string_to_process.title()
    return string_to_process

def format_list(string_to_process: str) -> str:
    """
    Takes a string and formats it like a list.
    :param string_to_process: The string the user wishes to process.
    :return: Formatted string.
    """
    string_to_process = string_to_process.replace(",", " | ")
    string_to_process = string_to_process.upper()
    return string_to_process

def process_numbers(numbers_to_process: str) -> str:
    """
    Takes some numbers and returns the total and average.
    :param numbers_to_process: The numbers the user wishes to process.
    :return: The total and average.
    """
    numbers_to_process = numbers_to_process.strip()
    list_to_process = numbers_to_process.split(",")

    total = 0
    for item in list_to_process:
        total = total + int(item)

    avg = total / len(list_to_process)
    return f"The total is: {total}. The average is {avg}."

print("""
How would you like to process the string?

1. Format a name.
2. Format a title.
3. Format a list.
4. Process numbers.

Enter your choice:
""")

user_choice = int(input())

string_to_process = input("Enter the string to process: ")

if user_choice  == 1:
    print(f"")