import googlemaps
import folium
from datetime import datetime
import polyline
import geopy.distance

API_KEY = 'AIzaSyBrhDCbzeWtINOlos2Abc4O6lJFGV-haN8'
gmaps = googlemaps.Client(key=API_KEY)

origin = input("Enter the starting point: ")
destination = input("Enter the destination: ")

directions_result = gmaps.directions(origin, destination, departure_time=datetime.now())
total_distance = directions_result[0]['legs'][0]['distance']['value'] / 1000

route_map = folium.Map(location=[35.8617, 104.1954], zoom_start=5)
path_coordinates = polyline.decode(directions_result[0]['overview_polyline']['points'])

if total_distance < 300:
    end_location = (directions_result[0]['legs'][0]['end_location']['lat'], directions_result[0]['legs'][0]['end_location']['lng'])
   places_result = gmaps.places_nearby(location=end_location, radius=50000, type='gas_station')

    if places_result['results']:
        stations = places_result['results']
        distances = [geopy.distance.distance(end_location, (station['geometry']['location']['lat'], station['geometry']['location']['lng'])).km for station in stations]
        nearest_station_index = distances.index(min(distances))
        nearest_station = stations[nearest_station_index]

        folium.PolyLine(path_coordinates, color='blue').add_to(route_map)
        folium.Marker(
            location=(nearest_station['geometry']['location']['lat'], nearest_station['geometry']['location']['lng']),
            popup="Gas Station",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(route_map)
    else:
        print("No gas stations found.")

else:
travel_distance = 0
    last_station_coord = path_coordinates[0]

    for coord in path_coordinates[1:]:
        segment_distance = geopy.distance.distance(last_station_coord, coord).km
        travel_distance += segment_distance

        if travel_distance >= 300:
            places_result = gmaps.places_nearby(location=coord, radius=50000, type='gas_station')

            if places_result['results']:
                station = places_result['results'][0]
                folium.Marker(
                    location=(station['geometry']['location']['lat'], station['geometry']['location']['lng']),
                    popup="Gas Station",
                    icon=folium.Icon(color='red', icon='info-sign')
                ).add_to(route_map)
                travel_distance = 0
            else:
                print(f"No gas stations found near {coord}.")
 last_station_coord = coord

    folium.PolyLine(path_coordinates, color='blue').add_to(route_map)

route_map.save("route_map.html")
print("The map has been saved as route_map.html. Open it with a web browser.")
