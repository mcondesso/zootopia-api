import os

from api import get_animal_data
from file_utils import load_env_file, load_file, write_file


def get_serialized_animal_data(animal_data):
    """Serializes animal data into an HTML list item string.

    Args:
        animal_data (dict): Dictionary containing animal data.

    Returns:
        str: HTML string representing the animal data.
    """
    text = '<li class="cards__item">\n'
    name = animal_data.get("name", None)
    if name:
        text += f'<div class="card__title">{name}</div>\n'
    text += '<div class="card__text">\n'
    text += '<ul>'

    taxonomy = animal_data.get("taxonomy", None)
    if taxonomy:
        scientific_name = taxonomy.get("scientific_name", None)
        if scientific_name:
            text += f"<li><strong>Scientific name</strong>: {scientific_name}<br/></li>\n"

    locations = animal_data.get("locations", None)
    if locations:
        text += f"<li><strong>Location</strong>: {locations[0]}<br/></li>\n"

    characteristics = animal_data.get("characteristics", None)
    if characteristics:
        diet = characteristics.get("diet", None)
        if diet:
            text += f"<li><strong>Diet</strong>: {diet}<br/></li>\n"
        animal_type = characteristics.get("type", None)
        if animal_type:
            text += f"<li><strong>Type</strong>: {animal_type}<br/></li>\n"

    text += '</ul>\n</div>\n</li>\n'
    return text


def get_animals_html(animals_data):
    """Generates HTML strings for a list of animals.

    Args:
        animals_data (list): List of dictionaries containing animal data.

    Returns:
        str: Combined HTML string for all animals.
    """
    animal_texts = []
    for animal in animals_data:
        text = get_serialized_animal_data(animal)
        animal_texts.append(text)
    return "\n".join(animal_texts)


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
