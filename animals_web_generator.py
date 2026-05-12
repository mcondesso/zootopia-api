import os

from data_fetcher import get_animal_data
from website_generator import load_env_file, load_file, write_file


def main():
    """Main function to load, process, and save animal data."""

    load_env_file()
    API_KEY = os.getenv("API_KEY")

    animal_name = input("Enter the name of an animal: ").lower().strip()

    animals_data = get_animal_data(API_KEY, animal_name)
    if not animals_data:
        animals_text = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
    else:
        animals_text = get_animals_html(animals_data)

    template_text = load_file("animals_template.html")

    updated_template = template_text.replace(
        "__REPLACE_ANIMALS_INFO__",
        animals_text,
    )

    write_file("animals.html", updated_template)
    print("Generated animals.html successfully.")


if __name__ == "__main__":
    main()
