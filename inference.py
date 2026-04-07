def predict(city):
    city = city.lower()

    if city == "chennai":
        return "Cafe Aroma → Cozy place\nBeach Park → Lively place"
    elif city == "delhi":
        return "Lotus Cafe → Aesthetic\nCity Park → Calm"
    else:
        return "No data available for this city"
