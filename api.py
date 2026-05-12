import requests


def get_animal_data(api_key, animal_name):
    """
    Fetch animal data from the API Ninjas Animals API.

    Args:
        api_key: API key for authentication.
        animal_name: The name of the animal to query.

    Returns:
        dict: The JSON response from the API if successful, or an error message.
    """
    url = f"https://api.api-ninjas.com/v1/animals"
    headers = {"X-Api-Key": api_key}
    params = {"name": animal_name}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {e}"}
