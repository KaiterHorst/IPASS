import DijkstraAlgoritme
import Chatbot
import LongitudeLatitude
import gmplot
import webbrowser

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

allelocaties = [["meldkamer", 52.077571, 5.123575], ["esso", 52.075063, 5.123028], ["rotsoord", 52.075017, 5.121657],
                ["lidl", 52.072918, 5.122761], ["kinderopvang", 52.073010, 5.120779],
                ["oranjebrug", 52.073201, 5.118899],
                ["cafetaria 'Kleyne reick'", 52.073963, 5.116336], ["mijdrechtstraat", 52.075240, 5.118087],
                ["vondelbrug", 52.078115, 5.121647], ["jutfaseweg", 52.076266, 5.120640],
                ["Mijdrechtstraat2", 52.074921, 5.119898], ["roc", 52.076266, 5.120640],
                ["grafisch lyceum utrecht", 52.078002, 5.115092],
                ["Balijelaan", 52.077527, 5.114335], ["pizzeria toscana", 52.074573, 5.114066],
                ["huisartsenpraktijk", 52.075700, 5.116458],
                ["croesestraat", 52.077110, 5.117451]]

while True:
    Chatbot.mainbot()

    # opent de het bestand met de locatie die de chatbot opgegeven heeft gekregen.
    with open('Locatie.txt', 'r') as f:
        finish = f.readlines()
    # Gebruikt het DijkstraAlgoritme om een route te maken vanaf de meldkamer naar de eindbestemming.
    # vervolgens wordt elke locatie in een latitude en een longitude gesplits.
    path = DijkstraAlgoritme.dijkstra(kaart, 'meldkamer', finish[0])
    lat = (LongitudeLatitude.splitter(path, allelocaties)[0])
    long = (LongitudeLatitude.splitter(path, allelocaties)[1])

    # dit gedeelte tekent de kaart en de route.
    gmapOne = gmplot.GoogleMapPlotter(52.0759687, 5.1187202, int(16.48))
    gmapOne.scatter(lat, long, 'red', size=10, marker=False)
    gmapOne.plot(lat, long, "blue", edgewidth=5)
    gmapOne.draw("map.html")

