import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_task(day: int, year: int) -> str:
    """
    Fetch the task description for the given day and year from Advent of Code.

    Args:
        day (int): The day of the task to fetch.
        year (int): The year of the Advent of Code.

    Returns:
        str: The task description as plain text.
    """
    url = f"https://adventofcode.com/{year}/day/{day}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        task_description = soup.find('article').get_text(separator='\n', strip=True)
        return task_description
    else:
        raise Exception(f"Failed to fetch day {day} task. Status code: {response.status_code}")

def save_task_to_file(day: int, task_description: str, folder: str):
    """
    Save the task description to a Python file with a template for solution code.
    Does not overwrite if the file already exists.
    """
    
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"day{day}.py")

    # Check if file already exists
    if os.path.exists(filename):
        print(f"{filename} already exists. Skipping file creation.")
        return  # Exit the function if the file already exists

    # Save task description as a docstring with template
    with open(filename, 'w') as file:
        docstring = f'"""{task_description}"""\n\n'
        file.write(docstring)
        file.write(create_template(day))  # Adds the template with main, part 1, and part 2
    
    print(f"Saved task for day {day} to {filename}")

def create_template(day: int) -> str:
    """
    Generate a template for the solution file, including main(), part 1, and part 2.
    """
    template = f"""
def main():
    \"\"\"Main function to execute the solution for Day {day}.\"\"\"
    with open('input_day{day}.txt', 'r') as f:
        data = f.read().strip().split('\\n')
    
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

def part1(data):
    \"\"\"Solve Part 1 of Day {day} task.

    Args:
        data (list): List of strings representing the input data.

    Returns:
        The solution to Part 1 of the task.
    \"\"\"
    # TODO: Implement solution for Part 1
    pass

def part2(data):
    \"\"\"Solve Part 2 of Day {day} task.

    Args:
        data (list): List of strings representing the input data.

    Returns:
        The solution to Part 2 of the task.
    \"\"\"
    # TODO: Implement solution for Part 2
    pass

if __name__ == "__main__":
    main()
"""
    return template

def main():
    current_year = 2023
    folder = "testfolder"  # Use the current year as the folder name

    for day in range(1, 26):  # Loop through each day, 1 to 25
        try:
            task_description = fetch_task(day, current_year)
            save_task_to_file(day, task_description, folder)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
