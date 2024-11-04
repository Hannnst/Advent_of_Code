import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import random
from colorama import Fore, Style, init

init(autoreset=True)

BASE_URL = "https://adventofcode.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

CHRISTMAS_COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW]

def fetch_advent_data(day: int, year: int, data_type: str) -> str:
    """
    Fetch either the task description or the test data for the given day and year from Advent of Code.
    """
    url = f"{BASE_URL}/{year}/day/{day}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 404:
        print(f"{random.choice(CHRISTMAS_COLORS)}Failed to fetch day {day} {data_type}. Status code: {response.status_code}")
        sys.exit(1)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch day {day} {data_type}. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    if data_type == "description":
        return soup.find('article').get_text(separator='\n', strip=True)
    elif data_type == "test_data":
        return '\n'.join(block.get_text(strip=True) for block in soup.find_all('code'))
    else:
        raise ValueError("Invalid data_type. Use 'description' or 'test_data'.")

def save_to_file(filepath: str, content: str):
    """
    Save content to a file, creating directories if necessary.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    if os.path.exists(filepath):
        print(f"{random.choice(CHRISTMAS_COLORS)}{filepath} already exists. Skipping file creation.")
    else:
        with open(filepath, 'w') as file:
            file.write(content)
        print(f"{random.choice(CHRISTMAS_COLORS)}Saved to {filepath}")

def save_task_and_test_data(day: int, task_description: str, test_data: str, year_folder: str):
    """
    Save the task description and test data to files.
    """
    filename_task = os.path.join(year_folder, f"day{day}.py")
    filename_test_data = os.path.join(year_folder, "files", f"day{day}_test_input.txt")

    docstring = f'"""{task_description}"""\n\n'
    save_to_file(filename_task, docstring + create_template(day))
    save_to_file(filename_test_data, test_data)

def create_template(day: int) -> str:
    """
    Generate a template for the solution file, including main(), part 1, and part 2.
    """
    template_path = os.path.join(os.path.dirname(__file__), 'template.py')
    with open(template_path, 'r') as file:
        template = file.read()
    return template.format(day=day)

def main(year=datetime.now().year):
    year_folder = str(year)

    for day in range(1, 25):
        try:
            description = fetch_advent_data(day, year, "description")
            test_data = fetch_advent_data(day, year, "test_data")
            save_task_and_test_data(day, description, test_data, year_folder)
        except Exception as e:
            print(f"{random.choice(CHRISTMAS_COLORS)}{e}")

if __name__ == "__main__":
    year = sys.argv[1] if len(sys.argv) > 1 else datetime.now().year
    main(year)