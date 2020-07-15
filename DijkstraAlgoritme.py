# de kaart met alle locaties en verbonden punten met afstanden in meters.
kaart = {"meldkamer": {"esso": 280, "vondelbrug": 150},
         "esso": {"rotsoord": 110, "lidl": 230},
         "rotsoord": {"kinderopvang": 235},
         "lidl": {"esso": 230, "kinderopvang": 130},
         "kinderopvang": {"oranjebrug": 100, "lidl": 130},
         "oranjebrug": {"cafetaria 'Kleyne reick'": 200, "mijdrechtstraat2": 210, "kinderopvang": 100},
         "cafetaria 'Kleyne reick'": {"oranjebrug": 200, "mijdrechtstraat": 200, "pizzeria toscana": 175},
         "pizzeria toscana": {"cafetaria 'Kleyne reick'": 175, "domino's": 350},
         "domino's": {"pizzeria toscana": 350, "grafisch lyceum utrecht": 90},
         "grafisch lyceum utrecht": {"domino's": 90, "croesestraat": 200, "roc": 300},
         "roc": {"grafisch lyceum utrecht": 300},
         "vondelbrug": {"roc": 250, "jutfaseweg": 230},
         "jutfaseweg": {"vondelbrug": 230, "mijdrechtstraat2": 150, "croesestraat": 250},
         "mijdrechtstraat2": {"mijdrechtstraat": 125, "jutfaseweg": 150, "oranjebrug": 210},
         "mijdrechtstraat": {"mijdrechtstraat2": 125, "huisartsenpraktijk": 110},
         "huisartsenpraktijk": {"mijdrechtstraat": 110, "croesestraat": 200},
         "croesestraat": {"huisartsenpraktijk": 200, "jutfaseweg": 250, "grafisch lyceum utrecht": 200}}


def dijkstra(graph, start, finish):
    shortest_distance = {}
    previous_point = {}
    unknown_points = graph
    infinity = float('inf')
    path = []

    # maakt alle waardes oneindig hoog zodat hij later weet welke onbezocht zijn.
    for i in unknown_points:
        shortest_distance[i] = infinity
    shortest_distance[start] = 0

    # checkt het punt met de kleinste waarde en veranderd hem naar punt i.
    while unknown_points:
        smallest_point = None
        for i in unknown_points:
            if smallest_point is None:
                smallest_point = i
            elif shortest_distance[i] < shortest_distance[smallest_point]:
                smallest_point = i

    #checkt of er een kortere route is dan de bekende route en als dat er is, dan vervangt hij hem.
        for connected_point, meters in graph[smallest_point].items():
            if meters + shortest_distance[smallest_point] < shortest_distance[connected_point]:
                shortest_distance[connected_point] = meters + shortest_distance[smallest_point]
                previous_point[connected_point] = smallest_point
        unknown_points.pop(smallest_point)

    # checkt of het pad mogelijk is, als niet meer infinity is is het punt bereikbaar en returnt hij het pad er naar
    # toe.
    current_location = finish
    while current_location != start:
        try:
            path.insert(0, current_location)
            current_location = previous_point[current_location]
        except KeyError:
            print('Path not reachable')
            break

    path.insert(0, start)
    if shortest_distance[finish] != infinity:
        return path
