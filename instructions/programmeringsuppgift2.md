
# Programmeringsuppgift 2

I programmeringsuppgift 2 skall ni implementera några algoritmer och datastrukturer från föreläsning 3-5.

**Viktig information:**
Alla problem skall lösas i Java eller Python.Observera även att det är tillåtet att använda Python eller något annat verktyg för att analysera resultaten, producera grafer, osv.

## Uppgifter

### Uppgift 1

Implementera en egen linked list, förklara för- resp nackdelar med vanlig lista (arraylist) ur kursens perspektib.

### Uppgift 2

Implementera en generisk deque (double-ended queue). Med en deque kan man lägga till och ta bort från början eller slutet av listan. Den kan alltså fungera som både stack och kö. Din implementation skall (minst) innehålla operationerna: size, isEmpty, addFirst, addLast, removeFirst och removeLast. Du skall även implementera en iterator för din deque. Din deque skall ha rimlig felhantering, dvs försök att hämta ut något från en tom lista och så vidare skall skapa exceptions.

### Uppgift 3

Implementera ett binärt sökträd som innehåller (minst) följande operationer: height, size, add, remove och contains. Du skall även implementera iteratorer som besöker noderna enligt in-, pre- och post-order genomgång. När du är övertygad om att din implementation fungerar så skall du lägga till en operation som tar bort det k största elementet, där k är en parameter. Om du t.ex. har ett träd som innehåller heltalen 1 till 10 och vill ta bort det tredje största värdet (k = 3) så skall åtta plockas bort. Din implementation skall skicka ett exception om det inte finns något k största värde.

### Uppgift 4

Implementera en generisk hashtabell som använder seperate chaining (använd den som man skapat i uppgift 1) för att hantera konflikter.

### Uppgift 5

Använd hashtabellen från uppgift 4 för att lagra information om fordon. Skapa en klass som minst innehåller registreringsnummer samt en hashfunktion (hashCode) som använder registreringsnumret för att räkna ut vilken hink ett objekt skall placeras i. Observera att objektet skall lagras i hashtabellen. Genomför ett experiment för att analysera hur bra din hashfunktion fungerar. Du kan t.ex. titta på antal konflikter.

## Instruktioner för inlämning av uppgift:

- Packa ihop alla dina filer som behövdes för att utföra programmeringsuppgiften i en ZIP-fil och skicka in för rättning här på MyMoodle.
- Detta är en individuell uppgift. Din lösning skall innehålla välstrukturerad programkod. Inkludera allt, inklusive eventuella Pythonprogram som du använt för dataanalys (dessa kommer endast att granskas om din analys inte verkar stämma).
- Beskriv i README.md hur man kompilerar och kör dina program.
- Texten i rapporten skall svara på frågorna som ställs i uppgifterna. Det är bra men inte nödvändigt att inkludera grafer. Tänk på att tydligt ange dina resultat/slutsatser.

