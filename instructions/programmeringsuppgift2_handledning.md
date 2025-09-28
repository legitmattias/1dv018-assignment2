Lite snabba anteckningar från handledningen, svar på min fråga:

"Har du några tips eller rekommendationer om hur man kan ta sig an A2":

Vi kan börja uppifrån och ned:

1. Länkad lista - implementera den och så upptäcker vi att vi har en nod som pekar på nästa nod, som pekar på en tredje nod osv. Listan blir längre och längre (det går förhoppningsvis ganska snabbt att lägga till nya) - i ett minnesblock är det ganska enkelt att hitta ett värde (för att man söker efter värdet på en viss position och i den positionen finns det oftast en länk till ett objekt)

I den länkade listan däremot, har man flera miljoner värden så måste man hela tiden fråga efter nästa, nästa, nästa osv och i värsta fall kan värdet vi letar efter ligga sist i listan (det kan ta lång tid) - lägger vi på något i blocket, då måste vi "putta" värdet ett snäpp - nackdelen med en "vanlig array" är att man får flytta på massa värden - hade vi haft en länkad lista så hade vi "flyttat isär dem" och lagt in ett nytt värde, det är en fördel med länkad lista 

2. Double ended - här har vi koll på "huvud och svans" på listan - vi kan lägga till och ta bort värden både i början och i slutet - det gör att vissa saker går fortare (en kö - man ställer sig först i kön) - där har vi funktioner vi kan lägga till

3. Binärt sökträd - hur mycket behöver vi kunna om awl träd? Det KAN komma något om hemtentan på det - på uppgiften har vi bara kört binärt träd - testa att stoppa in en sorterad lista och försök följa det binära trädet (inte så mycket till träd, det blir en länkad lista av allt) - börja där, sen lägger ni till height och size och contains (hur vi ska söka efter något) - ni kommer förhoppningsvis kunna lägga till rekursivt (för/efter i ordningen, störst till minst eller minst till störst). Undersök när ni ser nackdelar med binära träd, awl träden och sprejträd (?)

4. Hashning - använd en länkad lista (som ni skapat i uppgift 1, ni kan använda den ni skapat där)

5. Är inte speciellt svår - ofta heltal i exemplen men man kan skapa en tabell med en klass fordon eller något annat 

Jag tror att uppgifterna är ganska "rakt på" allihopa
