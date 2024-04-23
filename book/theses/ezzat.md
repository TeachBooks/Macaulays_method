# Ezzat: Curved beams

> De methode van Macaulay is een methode die de mogelijkheid biedt om zowel de interne krachten als de vervormingen van construties te analyseren. De discontiue belastingen die op de constructie werken zijn in één vergelijking te beschrijven door gebruik van de singulariteitsfunctie te maken. Hierdoor kan de volledige constructiee op een gestructureerde manier worden gemodelleerd met slechts één differenti aalvergelijking.
>
> In het werkelijkheid kunnen liggers schuin geplaatst zijn of een gebogen vorm hebben. Echter, is er nog geen onderzoek gedaan naar de toepassing van Macaulay’s methode met niet rechte liggers. Dit rapport probeert de volgende vraag en de te beantwoorden:
>
>Hoe kan de methode van Macaulay worden toegepast met betrekking tot zowel schuine liggers als
kromme liggers?

>Om de schuine liggers te kunnen analyseren, worden de evenwichtsvergelijkingen eerst opgesteld voor een hellingssnede (snede van een balk die onder hoek $\theta$ staat met de horizontale as).
> 
> ```{figure} ./figures/Figuur_1_ezzat.png
> :height: 200 px
> :name: figuur_1_ezzat
>
> Hellingsnede
> ```
> 
> Daarmee worden de volgende differentiaalvergelijkingen verkregen die later worden toegepast op verschillende constructies.
>
> $$\begin{align}   & \frac{dV}{dx}=-\sin \left( \theta  \right)\cdot {{q}_{x}}-\cos \left( \theta  \right)\cdot {{q}_{z}} \\   & \frac{dN}{dx}=-\cos \left( \theta  \right)\cdot {{q}_{x}}+\sin \left( \theta  \right)\cdot {{q}_{x}} \\   & \frac{dM}{dx}=\frac{V}{\cos \left( \theta  \right)} \\  \end{align}$$
>
> Er blijkt dat deze differentiaalvergelijkingen de juiste waarden geven voor zowel de interne krachten als de vervormingen van de constructies.
>
> Op dezelfde manier worden differentiaalvergelijkingen afgeleid voor een kniksnede (snede van een geknikte constructie waar de eerste staaf onder een hoek $\theta$ staat met de horizontale as en de tweede staaf onder een hoek $\Delta\theta$ staat ten opzicht van de eerste staaf).
>
> ```{figure} ./figures/Figuur_2_ezzat.png
> :height: 200 px
> :name: figuur_2_ezzat
>
> Kniksnede
> ```
>
> Onder de aanname dat een kromme lijn is een opeenvolging van lijnsegmenten die elkaar opvlogen met kleine hoekverschillen, kan $\Delta\theta$ als klein worden beschouwd. Door deze aanname, in combinatie van de drie evenwichtsvergelijkingen voor de kinksnede, worden opnieuw dezelfde differentiaalvergelijkingen verkregen die al eerder zijn afgeleid voor de hellingssnede. Het enige verschil nu is dat de hoek $\theta$ niet langer constant maar varieert telkens wanneer de kromme van richting verandert. De hoek $\theta$ kan zowel globaal (globale $\theta$ is de afgeleide van de construc􀆟efunc􀆟e) als lokaal (lokale $\theta$ is de hoek onder elke lijnsegment van de kromme) worden bepaald. Het blijkt dat het toepassen van de lokale $\theta$ een nauwkeurige analyse oplevert van zowel de krachten als de doorbuiging.
>
> ```{figure} ./figures/Figuur_3_ezzat.png
> :height: 200 px
> :name: figuur_3_ezzat
>
> Globale en lokale $\theta$
> ```
>
> Dit onderzoek illustreert de veelzijdigheid van de Macaulay-methode en presenteert nieuwe inzichten in het omgaan met schuine en kromme liggers, inclusief een innovatieve aanpak voor geknikte constructies.

{cite:ts}`ezzat_2024`

## Documenten
- [TU Delft Education repository](http://resolver.tudelft.nl/uuid:e82c8dd5-fbc1-46a3-b022-048d70425e2c)
- [GitHub repository](https://github.com/Ezzat1998/De-methode-van-Macaulay), examples also shown in this book:
   - [Code example kinked structure](./De-methode-van-Macaulay/geknikte_constructie.ipynb)
   - [Code example variants integrating](./De-methode-van-Macaulay/Varianten-(1).ipynb)
   - [Code example 1 to 3](./De-methode-van-Macaulay/Voorbeelden-1-t_m-3.ipynb)
   - [Code example 4 and 5](./De-methode-van-Macaulay/Voorbeelden-4-en-5.ipynb)