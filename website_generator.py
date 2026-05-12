def load_file(file_path):
    """Loads the content of a file.

    Args:
        file_path (str): Path to the file to be loaded.

    Returns:
        str: Content of the file as a string.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def write_file(file_path, data):
    """Writes data to a file.

    Args:
        file_path (str): Path to the file where data will be written.
        data (str): Data to be written to the file.
    """
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(data)


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
    text += "<ul>"

    taxonomy = animal_data.get("taxonomy", None)
    if taxonomy:
        scientific_name = taxonomy.get("scientific_name", None)
        if scientific_name:
            text += (
                f"<li><strong>Scientific name</strong>: {scientific_name}<br/></li>\n"
            )

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

    text += "</ul>\n</div>\n</li>\n"
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
