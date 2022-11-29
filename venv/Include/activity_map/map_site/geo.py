from geopy import Yandex


def get_longitude(place):
    location = Yandex(api_key='aaca613a-fe9d-47d2-95f3-cd1714593fff').geocode(place)
    return location.longitude


def get_latitude(place):
    location = Yandex(api_key='aaca613a-fe9d-47d2-95f3-cd1714593fff').geocode(place)
    return location.latitude

