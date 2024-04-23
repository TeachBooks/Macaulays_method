# Julia: Influence lines

> De methode van Macaulay is een methode waarmee interne krachten voor een constructie met belastingen kan worden bepaald. Macaulay maakt gebruik van singulariteitsfuncties om discontinue belastingen op constructies overzichtelijk te beschrijven. De methode van Macaulay is zowel voor eendimensionale als tweedimensionale constructies toepasbaar.
> Invloedslijnen worden toegepast in de mechanica om de meest ongunstige posities van krachten te vinden. Echter is er nog geen onderzoek verricht naar de toepassing van Macaulay’s methode met invloedslijnen. Daarom is er gekeken naar hoe deze invloedslijnen kunnen worden gecombineerd met de methode van Macaulay om het bepalen van invloedslijnen overzichtelijker te maken. De onderzoeksvraag van dit rapport luidt: _Hoe kan Macaulay’s methode worden toegepast met invloedslijnen voor zowel eendimensionale als tweedimensionale constructies?_
> 
> Voor het toepassen van de methode van Macaulay met invloedslijnen op eendimensionale constructies, wordt er gekeken in het bekende xzassenstelsel. De bewegende puntlast wordt hierbij aangenomen op een onbekende positie op $x = a$ zoals weergegeven in {numref}`figuur_1_julia`. De krachtsverdeling wordt hierbij omschreven aan de hand van singulariteits functies met de desbetreffende orde.
> Door middel van integreren worden vergelijkingen verkregen die zowel afhangen van $x$ als $a$. Daarom kan met deze methode in één vergelijking op een overzichtelijke manier zowel alle interne krachten (waarbij $a$ een gespecificeerde waarde heeft) als alle invloedsfactoren (waarbij $x$ een gespecificeerde waarde heeft) worden bepaald.
> 
> ```{figure} ./figures/Figuur_1_Julia.jpg
> :height: 200 px
> :name: figuur_1_julia
>
> Methode voor eendimensionaal
> ```
> 
> De krachtsverdeling bij tweedimensionale constructies wordt beschreven aan de hand van de differentiaalvergelijkingen voor extensie en buiging. Er wordt hierbij gekeken in een nieuw geïntroduceerd st-assenstelsel. De bewegende eenheidslast wordt beschreven als een kracht die altijd verticaal naar beneden gericht is en bevindt zich op een onbekende positie $s = a$. De kracht wordt hierbij in beide richtingen beschreven door het implementeren van goniometrische verhoudingen. Deze vergelijkingen zijn afhankelijk van de hoek $\alpha$ die de constructie met de horizontale lijn maakt zoals geschematiseerd in {numref}`figuur_2_julia`.
>
> ```{figure} ./figures/Figuur_2_julia.png
> :height: 200 px
> :name: figuur_2_julia
>
> Methode voor tweedimensionaal
> ```
>
> Met deze methode worden vergelijkingen verkregen die zowel afhangen van $s$ als $a$. Hierdoor kunnenook voor tweedimensionale constructies alle interne krachten en invloedsfactoren overzichtelijk worden bepaald.
>
> Hieruit valt te concluderen dat de bedachte methode toepasbaar is voor het bepalen van invloedslijnen met de methode voor Macaulay. Deze methode is zowel voor eendimensionale als tweedimensionale constructies toepasbaar. De bedachte methode is overzichtelijk aangezien er met één vergelijking alle mogelijke scenario’s kunnen worden bekeken voor zowel interne krachten als invloedsfactoren. Deze methode kan vervolgens worden toegepast bij het bepalen van de meest ongunstige posities van krachten in constructies wat van belang is bij het ontwerpen van civiele projecten.

{cite:ts}`jankie_2023`

## Documenten
- [TU Delft Education repository](http://resolver.tudelft.nl/uuid:d6869e59-57a0-4dca-9d4d-19050a0e1a89)
- [GitHub repository](https://github.com/JuliaJankie/Macaulay-s-toegepast-met-invloedslijnen), examples also shown in this book: [example 1](./Macaulay-s-toegepast-met-invloedslijnen/Eendimensionale_voorbeelden.ipynb) and [example 2](./Macaulay-s-toegepast-met-invloedslijnen/Tweedimensionale_voorbeelden.ipynb)