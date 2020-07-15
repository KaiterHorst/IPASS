import requests
# Vervang de <plak hier uw code> met uw identificatie code.
url = "https://api.telegram.org/bot<plak hier uw code>/"


# haalt chat id op
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# haalt message text op
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# haalt de laatste last_update op
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# deze functie stuurt een bericht naar de gebruiker
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response


def mainbot():
    update_id = last_update(url)["update_id"]
    geldigelocaties = ["meldkamer", "esso", "rotsoord", "lidl", "kinderopvang", "oranjebrug",
                       "cafetaria 'Kleyne reick'", "mijdrechtstraat", "vondelbrug", "jutfaseweg", "mijdrechtstraat2",
                       "roc", "grafisch lyceum utrecht", "balijelaan", "pizzeria toscana", "huisartsenpraktijk",
                       "croesestraat"]

    location = []
    hulp = []
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            # /start laat de bot beginnen
            if get_message_text(update).lower() == "/start":
                location.clear()
                hulp.clear()
                send_message(get_chat_id(update), 'Hallo mijn naam is Finn\nWelke hulp heeft u nodig?\n'
                                                  'U kunt kiezen uit 1: Politie, 2: Brandweer of 3: Medische hulp')

            # Checkt welke hulp de gebruiker nodig heeft
            elif get_message_text(update).lower() == "politie" or get_message_text(update).lower() == "1":
                hulp.clear()
                hulp.append("politie")
                send_message(get_chat_id(update), "U heeft gekozen voor politie.\nWat is uw locatie?")

            elif get_message_text(update).lower() == "brandweer" or get_message_text(update).lower() == "2":
                hulp.clear()
                hulp.append("brandweer")
                send_message(get_chat_id(update), "U heeft gekozen voor brandweer.\nWat is uw locatie?")

            elif get_message_text(update).lower() == "medische hulp" or get_message_text(update).lower() == "3":
                hulp.clear()
                hulp.append("medische hulp")
                send_message(get_chat_id(update), "U heeft gekozen voor medische hulp.\nWat is uw locatie?")

            # Als iemand eerst een locatie stuurt vraagt hij om de hulp.
            elif get_message_text(update).lower() in geldigelocaties and len(hulp) == 0:
                send_message(get_chat_id(update), "Maak eerst een keuze wat voor hulp u wilt.\n"
                                                  "Kies uit 1: politie, 2: brandweer of 3: medische hulp.\n"
                                                  "let op spelling of gebruik de getallen")
                location.clear()

            # De gebruiker heeft een de hulp en een locatie gekozen
            elif get_message_text(update).lower() in geldigelocaties and len(hulp) != 0:
                location.clear()
                location.append(get_message_text(update).lower())
                send_message(get_chat_id(update), "De hulp die u nodig heeft is: "
                             + hulp[0] + "\nEn uw locatie is: " + location[0]
                             + "\nAls dit klopt typ dan: bevestig")

            # Dit zorgt ervoor dat het alleen nut heeft om bevestig te typen als hij locatie en hulp heeft ingevuld.
            # Schrijft de opgegeven eindbestemming naar een txt file zodat locatie en hulp gewist kunnen worden voor
            # de volgende ronde.
            elif get_message_text(update).lower() == "bevestig":
                if len(geldigelocaties) != 0 and len(hulp) != 0:
                    send_message(get_chat_id(update), "De " + hulp[0] + ' is onder weg naar ' + location[0])
                    with open('Locatie.txt', 'w') as bestemming:
                        bestemming.write(location[0])
                    location.clear()
                    hulp.clear()
                    break

            # Checkt of de locatie goed geschreven is zodat het algoritme hem herkent.
            elif get_message_text(update).lower() not in geldigelocaties and len(hulp) != 0:
                send_message(get_chat_id(update), "Dat is geen geldige locatie.\nProbeer een andere en let op spelling.")

            # Vraagt de gebruiker om geldige hulp in te vullen.
            else:
                send_message(get_chat_id(update), "Ik begrijp het niet.\n"
                                                  "Kies uit 1: politie, 2: brandweer of 3: medische hulp.\n"
                                                  "let op spelling of gebruik de getallen")

            update_id += 1
