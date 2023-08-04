def get_city_country(city,country,population=""):
    """return city and country"""
    if population:
        full_name = f"{city} {country} - population ={population}"
    else:
        full_name = f"{city} {country}"

    return full_name.title()
    