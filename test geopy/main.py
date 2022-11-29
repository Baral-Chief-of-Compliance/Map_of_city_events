from geopy import Yandex

place = "Баумана                    38Б, Мурманск"
location = Yandex(api_key='aaca613a-fe9d-47d2-95f3-cd1714593fff').geocode(place)

print(location.address)
print("долгота " + str(location.longitude))
print("широта "+str(location.latitude))