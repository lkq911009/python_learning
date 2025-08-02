from os import system
from pathlib import Path
import os


def clear_screen():
    """Clear the console screen."""
    system('cls' if os.name == 'nt' else 'clear')


def get_current_working_directory():
    """Get the current working directory."""
    return os.getcwd()


def get_sub_directories(parent_directory):
    return [d for d in parent_directory.iterdir() if d.is_dir()]


def read_a_recipe_from_category(category_path):
    categories = get_sub_directories(category_path)
    print("Available categories:")
    for category in categories:
        print(f"- {category.name}")

    category_name = input("Enter the category name: ")
    selected_category = category_path / category_name
    if not selected_category.exists():
        print(f"Category '{category_name}' does not exist.")
        return

    print(f"Recipes in category '{category_name}':")
    recipes = [recipe.stem for recipe in selected_category.glob("*.txt")]
    if len(recipes) == 0:
        print(f"No recipes found in '{selected_category}'.")
        return
    print(f"Recipes in '{selected_category}':")
    for recipe in recipes:
        print(f"- {recipe}")
    file_name = input("Enter the recipe file name (without .txt): ")
    file_path = selected_category / f"{file_name}.txt"
    if not file_path.exists():
        print(f"Recipe file '{file_name}.txt' does not exist in category '{category_name}'.")
        return

    read_a_file(file_path)


def read_a_file(file):
    with open(file, "r") as file:
        file_content = file.read()
        print(f"Content of receipe {file}:\n{file_content}\n")


def write_a_file(file, content):
    with open(file, "w") as file:
        file.write(content)
        print(f"Content written to {file} successfully.")


def print_action_options(options):
    print("\nChoose an action:")
    for key, value in options.items():
        print(f"{key}: {value}")


def get_user_choice():
    choice = input("Enter your choice: ")
    while choice not in action_options:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ")
    return choice


def create_a_recipe_in_category(category_path):
    print_available_categories(category_path)
    category_name = input("Enter the category name: ")
    selected_category = category_path / category_name
    recipe_name = input("Enter the recipe name: ")
    recipe_content = input("Enter the recipe content: ")
    recipe_file = selected_category / f"{recipe_name}.txt"
    write_a_file(recipe_file, recipe_content)


def create_a_category(parent_directory):
    new_category = input("Enter the new category name: ")
    new_category_path = parent_directory / new_category
    new_category_path.mkdir(exist_ok=True)
    print(f"New category '{new_category}' created.")


def print_available_categories(parent_directory):
    categories = get_sub_directories(parent_directory)
    if not categories:
        print("No categories available.")
        return
    print("Available categories:")
    for category in categories:
        print(f"- {category.name}")


def delete_a_recipe_in_catagory(parent_directory):
    print_available_categories(parent_directory)
    category_name = input("Enter the category name: ")
    selected_category = parent_directory / category_name
    if not selected_category.exists():
        print(f"Category '{category_name}' does not exist.")
        return

    recipes = [recipe.stem for recipe in selected_category.glob("*.txt")]
    if len(recipes) == 0:
        print(f"No recipes found in '{selected_category}'.")
        return

    print(f"Recipes in '{selected_category}':")
    for recipe in recipes:
        print(f"- {recipe}")

    recipe_name = input("Enter the recipe name to delete (without .txt): ")
    recipe_file = selected_category / f"{recipe_name}.txt"
    if not recipe_file.exists():
        print(f"Recipe file '{recipe_name}.txt' does not exist in category '{category_name}'.")
        return

    os.remove(recipe_file)
    print(f"Recipe '{recipe_name}.txt' deleted from category '{category_name}'.")



def delete_a_category(parent_directory):
    print_available_categories(parent_directory)
    category_name = input("Enter the category name to delete: ")
    selected_category = parent_directory / category_name
    if not selected_category.exists():
        print(f"Category '{category_name}' does not exist.")
        return

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete the category '{category_name}'? (yes/no): ")
    if confirm.lower() == 'yes':
        os.rmdir(selected_category)
        print(f"Category '{category_name}' deleted successfully.")
    else:
        print("Deletion cancelled.")

def handle_choice(choice, parent_directory):
    if choice == '1':
        read_a_recipe_from_category(parent_directory)
    elif choice == '2':
        create_a_recipe_in_category(parent_directory)
    elif choice == '3':
        create_a_category(parent_directory)
    elif choice == '4':
        delete_a_recipe_in_catagory(parent_directory)
    elif choice == '5':
        delete_a_category(parent_directory)
    elif choice == '6':
        print("Exiting the program.")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True


action_options = {'1': "Pick an existing recipe to read",
                  '2': "create a recipe in specific category",
                  '3': "create a new category",
                  '4': "delete recipe in specific category",
                  '5': "delete category",
                  '6': "Exit the program"}
current_working_directory = get_current_working_directory()
recipe_parent_directory = Path(current_working_directory, 'Recipes')

while True:
    clear_screen()
    print_action_options(action_options)
    user_choice = get_user_choice()
    if not handle_choice(user_choice, recipe_parent_directory):
        break
