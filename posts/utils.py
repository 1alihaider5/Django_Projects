import requests


def get_holidays(country="pk", year=2025):
    api_key = "X7OQbLOYl35gU4ycJts1Dx1ue2VyiFCG"
    url = f"https://calendarific.com/api/v2/holidays?api_key={api_key}&country={country}&year={year}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get("response", {}).get("holidays", [])
    else:
        return []
