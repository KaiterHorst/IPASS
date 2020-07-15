READ ME
1 Zorg dat de volgende pip installs goed zijn uitgevoerd
	-pip install webbrowser, 
	-pip install gmplot, 
	-pip install requests
  Als het niet lukt volg deze tutorial https://www.youtube.com/watch?v=AdUZArA-kZw met de naam van de package die je wilt installeren.

2. Zorg dat je een telegram account geregristreerd heb zodat je een bot kunt aanmaken en berichten kan sturen.

3. De Chatbot gebruikt een key om te identificeren.
   Een tutorial voor hoe je een token genereerd zie je hier: https://www.youtube.com/watch?v=RqzmQpI3kFU&t=216s
   In Chatbot.py op regel 3 staat url = "https://api.telegram.org/bot<plak hier jouw token>/"

4. Zorg dat Chatbot.py, DijkstraAlgoritme.py, LongitudeLatitude.py, Main.py en Locatie.txt in het zelfde project staan
   zodat de Main.py de imports zonder moeite kunnen worden uitgevoerd.

5. Nu ben je klaar om Main.py te runnen

6. Open je telegram bot in telegram en typ /start
   Als je een error krijgt run Main.py opnieuw dat kan komen omdat het het eerste bericht is.

7. Volg de instructies van de bot
   Als de bot om uw locatie vraagt kies dan 1 uit geldige locaties
   (Chatbot.py, regel 36 geldige locaties)

8. Nu is er een map.html aangemaakt in uw project.
   Open die map

9. Op regel 6 staat een link: https://maps.googleapis.com/maps/api/js?libraries=visualization
   Klik die met uw rechtermuisknop en kies open in browser en dan kies je chrome.

10. Als alles goed is uitgevoerd ziet u nu de route vanuit de meldkamer naar uw locatie met een blauwe lijn aangegeven.
    De punten waar hij langs komt zijn aangegeven met een rode cirkel.
