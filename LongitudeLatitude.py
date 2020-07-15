# Deze functie split de latitudes en longitudes van een plek
def splitter(dijkstra_results, alle_locaties):
    lat = []
    long = []
    for i in range(len(alle_locaties)):
        for j in range(len(dijkstra_results)):
            if dijkstra_results[j] == alle_locaties[i][0]:
                lat.append(alle_locaties[i][1])
                long.append((alle_locaties[i][2]))

    return lat, long
