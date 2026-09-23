def get_weather(city):
    weather_data = {
        "erode": "Sunny, 31°C",
        "chennai": "Cloudy, 29°C",
        "coimbatore": "Partly cloudy, 28°C"
    }

    return weather_data.get(city.lower(), "Weather information not available")


def check_room_capacity(room, students):
    rooms = {
        "Room A": 60,
        "Room B": 40,
        "Room C": 100
    }

    capacity = rooms.get(room)

    if capacity is None:
        return "Room not found"

    if capacity >= students:
        return f"{room} is suitable. Available seats: {capacity - students}"
    else:
        return f"{room} is not suitable. Shortage: {students - capacity} seats"