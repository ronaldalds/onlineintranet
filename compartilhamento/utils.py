center_lng = -5.176168
center_lat = -40.680138

kml = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
    '<Placemark>\n'
    '<name>View-centered placemark</name>\n'
    '<Point>\n'
    '<coordinates>%.6f,%.6f</coordinates>\n'
    '</Point>\n'
    '</Placemark>\n'
    '</kml>'
) % (center_lng, center_lat)

print('Content-Type: application/vnd.google-earth.kml+xml\n')
print(kml)
