# Photo slideshow, een concept probleem voor heuristieken op de UvA 

de vakomschrijving is te vinden op [heuristieken.nl](heuristieken.nl)

### Photo slideshow
De opdracht is gebaseerd op photo slideshow, de opdracht voor de qualifier round van Google Hash code 2019.

Het is (voor zover ik dit soort problemen snap) een NP compleet probleem. Elke toegevoegde slide maakt de tijd voor het uitrekenen minstens met een factor n+1 groter, waarbij n het aantal fotos is. Kortom: Het aantal mogelijkheden als er n verticale slides zijn is n!. Hier komt nog een bepaalde exponent bij als horizontale slides worden meegerekend. (Staat hier niet voor het geval dit ooit een echte opdracht wordt ;))

### generator functie
Voor het makkelijk maken van problem sets en het maken van makkeljke problem sets heb ik een kort pythonscriptje geschreven om deze te genereren. Bij het opstarten vraagt het om de hoeveelheid regels en het .in bestand
#### Wat staat er in een .in bestand?
Het volgende moet er in staan:
regel 0: Het percentage Horizontale slides: een geheel getal wat de randomfunctie stuurt in het 'V' of 'H' van een slide

regel 1: De getallen n, m, i, j voor een rudimentaire pyramidevormige normaalverdeling: het minimum aantal tags n, maximum aantal tags m, gemiddeld aantal tags i, de hoogte van het gemiddelde j. Het programma rekent dan 2 functies uit aan de hand van deze verdeling.

regel 2 tot en met het einde: Als het niet de laatste regel is, dan zal het programma 1 van de tags op de regel kiezen, anders zal het aangevuld worden met de tags op de laatste regel tot de hoeveelheid tags die volgens de formule is bepaald is gehaald.

De tags zijn in lowercase unicode, a t/m z en onderstreepjes. Ze worden gescheiden door spaties.

## Hieronder staan enigzins gefundeerde meningen

#### Dingen die koel zijn aan deze opdracht
Er zijn 2 manieren om deze opdracht op te lossen: De straightforward manier, met een algoritme om de verschillende combinaties te heuristieken, of een queue oplossing, waarbij het prograama bepaalt of hij de slide voor of na de huidige slideshow zet.

#### Eventuele problemen
Pruning: Weinig. Een manier van pruning is om de overlap aan tags alvast te evalueren en als er een overlap is van meer dan 80% dan zal dit waarschijnlijk een suboptimale oplossing zijn.
