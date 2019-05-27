## Beschrijving

Het doel van de opdracht is om een slideshow te maken aan de hand van een scorefunctie.

Deze opdracht is gebaseerd op ['Photo slideshow' van de Google Hashcode 2019 kwalificatieronde.](https://storage.googleapis.com/coding-competitions.appspot.com/HC/2019/hashcode2019_qualification_task.pdf)

## Intro
Daan gaat graag op (werk-)vakantie en maakt veel vakantiefoto's. Om zijn studenten niet al te veel vervelen wil hij een diashow maken die de aandacht van iedereen er bij kan houden. Gelukkig is Daan heel handig geweest door alle foto's op een relevante manier te taggen.

## De vakantiefoto's van Daan [makkelijk]
De dataset is [hier](daans_vakantiefotos_easy.txt) te vinden.

### Wat is een foto?

De dataset begint met een cijfer *N*, deze geeft het aantal foto's in de dataset aan. Daarna volgen *N* regels met de beschrijving van de foto's.

Een voorbeeld van beschrijvingen van foto's kan zijn:

```
V 3 selfie daan athene
V 5 groep daan athene university_of_athens research_group
V 6 groep daan athene acropolis parthenon grappig
```

De eerste letter geeft de oriëntatie van de foto aan: horizontaal of verticaal. Voor deze case zijn alle foto's verticaal georiënteerd. Het cijfer *M* geeft aan hoeveel tags de foto bevat en vervolgens *M* tags, gescheiden door een spatie. De tags zijn lowercase letters en kunnen underscores ( _ ) bevatten.

### Score

De 'interessantheidsscore' (zeg het 5 keer snel achter elkaar) van een diashow is gebaseerd op de opvolgende slides en de overlap in tags die ze hebben. 

De score is het minimum van deze 3 uitkomsten tussen 2 opvolgende slides:

* Het aantal gemeenschappelijke tags tussen de slides
* Het aantal tags die wel in de ene slide zitten en niet in de ander
* Het aantal tags die wel in de andere slide zitten maar niet in de ene

Als we het voorbeeld van de eerder genoemde beschrijvingen nemen:

https://imgur.com/J4iB4Lg

Er zijn 2 gemeenschappelijke tags (daan, athene), de eerste slide heeft 1 tag die de tweede niet heeft (selfie) en de tweede heeft 3 tags die de eerste niet heeft (university_of_athens, groep, research_group)

De score voor deze slides zou dus 1 zijn. De volgende heeft als score 2 (3, 2, 3 voor de punten respectievelijk).

De score voor de gehele slideshow is alle scores bij elkaar opgeteld, in dit geval dus 1 + 2 = 3

### De diashow

#### Opdracht 1:
Schrijf een programma die de foto's achter elkaar kan zetten en de score kan uitrekenen.

#### Opdracht 2:
Schrijf een algoritme dat de foto's op een zo interessant mogelijke manier achter elkaar zet.

## De vakantiefoto's van Daan [medium]
De dataset is [hier] te downloaden.

#### Wat is een slide?
De dataset en beschrijvingen zijn vergelijkbaar met die van de vorige opdracht, echter, de foto's kunnen nu ook horizontaal georiënteerd zijn.

Hoewel verticale foto's één voor één gepresenteerd langskomen, nemen horizontale foto's slechts de helft van het scherm in, en worden dus in tweetallen gepresenteerd. Een slide met 2 horizontale foto's combineert alle tags die de 2 foto's apart hebben. 

Voorbeeld:
```
4 H selfie daan osaka achtbaan
4 H selfie daan osaka sakura
```
Geeft als slide
```
selfie daan osaka achtbaan sakura
```
Alle regels voor het maken van een slideshow zijn hetzelfde.

#### Opdracht 3:
Schrijf een algoritme die slides maakt en en ze op een zo interessant mogelijke manier achter elkaar zet.

## De festivalselfies van Clint [moeilijk]
De dataset is [hier] te downloaden.

#### Opdracht 4:
Schrijf een algoritme die slides maakt en ze op een zo interessant mogelijke manier achter elkaar zet.
