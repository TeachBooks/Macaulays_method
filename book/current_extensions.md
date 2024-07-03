# Complete description of current extensions

Dit rapport zal een overzicht bevatten van de opgedane kennis met betrekking tot de methode van Macaulay. Dit rapport is bedoeld voor personen met mechanica kennis die nog onbekend zijn met de methode van Macaulay. In dit rapport zal de methode van Macaulay worden toegelicht en zal er worden aangegeven hoe deze toegepast kan worden.

Dit rapport bestaat uit 4 hoofdstukken:

1.  De methode van Macaulay

2.  Modelleren van krachten, opleggingen en verbindingen

3.  Invloedslijnen met Macaulay

4.  Oplossen van 2D constructies

In dit rapport wordt er gerefereerd naar de werken van {cite:ts}`vanderwulp_2023`, {cite:ts}`jankie_2023`, {cite:ts}`alex_2024` en {cite:ts}`mark_2024` en wordt er hevig gebruik gemaakt van citaties en parafraseringen.

## 1.  De methode van Macaulay

(hoofdstuk_1_1)=
### 1.1 Belastingvergelijking

Uit de balkentheorie van Euler-Bernoulli kunnen de differentiaalvergelijkingen voor buiging {eq}`vgl_1` en extensie {eq}`vgl_2` worden afgeleid. Begrip over de afleiding en het gebruik van deze vergelijkingen wordt als voorkennis beschouwd.

```{math}
:label: vgl_1
EI\frac{d^{4}w}{dx^{4}} + q_{z}
```

```{math}
:label: vgl_2
EA\frac{d^{2}w}{dx^{2}} + q_{x}
```

Over het algemeen worden deze vergelijkingen gebruikt door liggers eerst in verschillende delen met gelijke belasting op te splitsen. Vervolgens kan ieder deel beschreven worden met de differentiaalvergelijking en wordt er gebruik gemaakt van overgangsvoorwaarden.

Bij de methode van Macaulay wordt er op een andere manier gebruik gemaakt van deze differentiaalvergelijkingen. De methode van Macaulay maakt gebruik van singulariteitsfuncties om de belasting op een ligger te beschrijven. Dit heeft als grote voordeel dat een ligger niet opgesplitst hoeft te worden in verschillende delen. Het gedrag van een ligger kan zo in één vergelijking worden beschreven.

### 1.2  Singulariteitsfuncties

Zoals hierboven aangegeven maakt de methode van Macaulay gebruik van singulariteitsfuncties. Dit is een familie van functies die gebaseerd is op de Dirac-delta functie. Het differentiëren en integreren van deze Dirac-delta functie vormt deze familie. De singulariteitsfunctie is wiskundig als volgt gedefinieerd:

Voor $n\  \geq \ 0$:

```{math}
:label: vgl_3
f\left( x \right) \equiv {\left\langle {x - \bar x} \right\rangle ^n} = \left\{ \begin{array}{l}
{\left( {x - \bar x} \right)^n} & x \ge \bar x \\
0 &  x < \bar x
\end{array} \right.
```

Voor $n < \ 0$:

```{math}
:label: vgl_4
f\left( x \right) \equiv {\left\langle {x - \bar x} \right\rangle ^n} = 0
```

Hierin geeft $\bar x$ de positie aan waar de singulariteit voorkomt, en is $n$ de orde van de functie.

Hierbij is {eq}`vgl_4` aangepast waarbij er origineel op $x=\bar x$ geldt $f\left(x\right)=\infty$. Dit heeft echter geen betekening voor het balkmodel.

Het integreren van de singulariteitsfunctie is afhankelijk van zijn orde en is als volgt gedefinieerd:

```{math}
:label: vgl_5
\int {{{\left\langle {x - \bar x} \right\rangle }^n}{\rm{d}}x}  = \left\{ \begin{array}{l}
{\left( {x - \bar x} \right)^{n + 1}} & n < 0\\
\cfrac{{{{\left( {x - \bar x} \right)}^{n + 1}}}}{{n + 1}} & n \ge 0
\end{array} \right.
```

Een aantal voorbeelden zijn hieronder weergegeven

#### Voorbeeld $n = -1$

Voor $n = -1$ evalueert de functie {eq}`vgl_4` voor het gehele domein naar 0. Als de originele definitie wordt aangehouden met $f\left(\bar x\right)=\infty$ staat deze functie ook wel bekend als de Dirac-Delta functie.

#### Voorbeeld $n = 0$

Voor $n=0$ evalueert de functie {eq}`vgl_4` tot een stapfunctie, ook wel bekend als de Heaviside.
```{figure} figures/heaviside.svg
---
name: Figuur_3
align: center
---
Plot of $\left\langle {x - \bar x} \right\rangle ^0$
```

#### Voorbeeld $n = 1$
Voor $n=1$ geeft de functie {eq}`vgl_4` een linear verband na $\bar x$.
```{figure} figures/unitramp.svg
---
name: Figuur_4
align: center 
---
Plot of $\left\langle {x - \bar x} \right\rangle ^1$
```

### 1.3  Oplossingsstrategie

De eerste stap bij het oplossen van een probleem met de methode van Macaulay is het opstellen van de belastingvergelijking in de langs- en loodrechte richting. Hiervoor wordt de hele constructie gemodelleerd in één vergelijking per richting. Deze vergelijking kan vervolgens ingevuld worden als $q$ in de differentiaalvergelijkingen in `ref`(hoofdstuk_1_1). Hoe verschillende onderdelen van een constructie gemodelleerd kunnen worden in deze vergelijking is beschreven in `ref`(hoofdstuk_2).

Als de belastingvergelijking is gevonden kan deze geïntegreerd worden. Dit geeft vergelijkingen die de normaalkrachten, dwarskracht, het moment, de rotatie, de doorbuiging en extensie van de staaf beschrijven. In deze vergelijkingen staan nog onbekende reactiekrachten en integratieconstanten.

Om deze onbekende reactiekrachten en integratieconstanten op te lossen kunnen de randvoorwaarden worden opgesteld. Met deze randvoorwaarden kunnen de onbekende waardes worden gevonden.

De gevonden waardes voor de reactiekrachten en integratieconstanten kunnen worden ingevuld in de vergelijkingen. Dit geeft de vergelijkingen die het gedrag van de staaf beschrijven.

(hoofdstuk_2)=
## 2.  Modelleren van belastingen, opleggingen en verbindingen

### 2.1 Modelleren van belastingen

Voor het modeleren van belastingen op de constructie wordt gebruik gemaakt van singulariteitsfuncties. Dit maakt het mogelijk om de volledige constructie in één regel (per richting) te beschrijven en daarmee de differentiaalvergelijking op te lossen. Er zal nu toegelicht worden hoe verschillende krachten beschreven kunnen worden met singulariteitsfuncties.

Belastingen kunnen worden beschreven door de een singulariteitsfunctie van bijbehorende orde te vermenigvuldigen met de waarde van de kracht of verbinding. Naar aanleiding van het assenstelsel wordt een kracht positief of negatief gemodelleerd.

#### Puntlast
Een puntlast geeft belasting op een enkele plek in de constructie. Een puntlast kan gemodelleerd worden met de Dirac-delta functie. Een puntlast met een waarde $F$, ter plaatse van punt $\bar x$ waarbij de staaf een hoek $\theta \left( \bar x \right)$ heeft, wordt gemodelleerd zoals getoond in {eq}`puntlast_1d` en {eq}`puntlast_2d`.

```{math}
:label: puntlast_1d
{{q\left(x\right) : F \left\langle x - \bar x \right\rangle^{- 1}}}
```

In 2d wordt de kracht ontbonden in de langs- en loodrechte richting:

```{math}
:label: puntlast_2d
\begin{align}
&q_z\left(x\right) : &F_{v} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left(\bar x\right) \right) &+F_{h} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left(\bar x\right) \right) \\
&q_x\left(x\right) : &- F_{v} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta\left(\bar x\right) \right) &+F_{h} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left(\bar x\right) \right)
\end{align}
```

#### Koppel
Een koppel werkt ook op een enkel punt in de constructie. Een koppel wordt beschreven door de orde $-2$ in de krachtenvergelijking van de loodrechte richting aangezien dit koppel geen invloed heeft op de langsrichting. Een koppel met waarde $T$ ter plaatse van punt $\bar x$ waarbij de staaf een hoek $\theta \left( \bar x \right)$ heeft, wordt als volgt gemodelleerd in 1D en 2D:

```{math}
:label: koppel_1d
q_z\left(x\right) : T \left\langle x - \bar x \right\rangle^{- 2}
```

```{math}
:label: koppel_2d
\begin{align}
&q_z\left(x\right): &T \left\langle x - \bar x \right\rangle^{- 2} \\
&q_x\left(x\right): &0
\end{align}
```

#### Uniform verdeelde belasting
Belasting die gelijkmatig verdeeld is over de constructie kan beschreven worden met twee Heaviside functies. Hierbij werkt de waarde van $q_{z}$ eerste vanaf $\bar x_1$ in de daadwerkelijke richtingen en dan vanaf $\bar x_2$ in tegengestelde richting, dit geeft een totaal van $0$ voor $x > \bar x_2$. Deze werking is in {numref}`Figuur_6` weergegeven.

```{figure} figures/image6.png
---
width: 600
name: Figuur_6
align: center
---
Modelleren van een uniform verdeelde belasting {cite:p}`vanderwulp_2023`
```

Dit kan beschreven worden met singulariteitsfuncties met groottes $q_v$ en $q_h$ van punt $\bar x_1$ tot $x_2$ waarbij de staaf een hoek $\theta \left( \bar x_1 \right)$ en $\theta \left( \bar x_2 \right)$ heeft in 1D en 2D:

```{math}
:label: Verveelde_belasting_1D
\begin{align}
&q_z\left(x\right)= &q_v \left\langle x - \bar x_1 \right\rangle^{- 1} &-q_v\left\langle x - \bar x_2 \right\rangle^{- 1} \\
&q_z\left(x\right)= &q_h \left\langle x - \bar x_1 \right\rangle^{- 1} &-q_h\left\langle x - \bar x_2 \right\rangle^{- 1}
\end{align}
```

```{math}
:label: Verveelde_belasting_2d
\begin{align}
&q_z\left(x\right): &q_{v} \left\langle x - \bar x_1 \right\rangle^{- 1} \cos \left( \theta \left(\bar x_1\right) \right) &-q_{v} \left\langle x_2 - \bar x \right\rangle^{- 1} \cos \left( \theta \left(\bar x_2\right) \right) \\ & &+ q_{h} \left\langle x - \bar x_1 \right\rangle^{- 1} \sin \left( \theta \left(\bar x_1\right) \right) &-q_{h} \left\langle x - \bar x_2 \right\rangle^{- 1} \sin \left( \theta \left(\bar x_2\right) \right) \\
& q_x \left(x \right) : &- q_{v} \left\langle x - \bar x_1 \right\rangle^{- 1} \sin \left( \theta \left(\bar x_1\right) \right) &+q_{v} \left\langle x - \bar x_2 \right\rangle^{- 1} \sin \left( \theta \left(\bar x_2\right) \right) \\ &&+q_{h} \left\langle x - \bar x_1 \right\rangle^{- 1} \cos \left( \theta \left(\bar x_1\right) \right) &- q_{h} \left\langle x - \bar x_2 \right\rangle^{- 1} \cos \left( \theta \left(\bar x_2\right) \right)
\end{align}
```

#### Lineair en parabolisch verdeelde belastingen
Belastingen die niet uniform maar lineair of parabolisch verdeeld zijn kunnen op eenzelfde manier gemodelleerd worden als de uniform verdeelde belasting.

(hoofdstuk_2.2)=
### 2.2 Modelleren van opleggingen en verbindingen voor buiging

Naast belastingen kunnen ook opleggingen en verbindingen worden gemodelleerd door middel van singulariteitsfuncties. Op de plek waar een oplegging of verbinding wordt toegevoegd gelden ook randvoorwaarden. Deze randvoorwaarden worden gebruikt om de vergelijkingen uiteindelijk op te lossen. Er zal nu worden toegelicht hoe verschillende opleggingen en verbindingen kunnen worden beschreven door middel van singulariteitsfuncties en welke randvoorwaarden daarbij horen. Er wordt in dit hoofdstuk alleen gekeken naar krachten loodrecht op de staaf en momenten. Krachten evenwijdig aan de staaf worden behandeld in het `ref`(hoofdstuk_2.3)Modelleren van opleggingen en verbindingen voor extensie.

#### Inklemming
Bij een inklemming kunnen een verticale oplegreactie en een inklemmingsmoment optreden. In {numref}`Figuur_7` is weergegeven hoe een inklemming gemodelleerd kan worden.

```{figure} figures/image7.png
---
width: 400
name: Figuur_7
align: center
---
Modelleren van een inklemming {cite:p}`vanderwulp_2023`
```

Dit kan beschreven worden met singulariteitsfuncties met ordes $-1$ en $-2$ met onbekende groottes $R_v$, $R_h$ en $T$ op punt $\bar x$ waarbij de staaf een hoek $\theta \left( \bar x \right)$ heeft in 1D en 2D:

```{math}
:label: inklemming_1d_krachten
\begin{align}
&q_z\left(x\right) : &R_{v} \left\langle x - \bar x \right\rangle^{- 1} &+ T \left\langle x - \bar x \right\rangle^{- 2} \\ &q_x\left(x\right) : &R_{h} \left\langle x - \bar x \right\rangle^{- 1}
\end{align}
```

```{math}
:label: inklemming_2d_krachten
\begin{align}
&q_z\left(x\right) : &R_{h} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) &+ R_{v} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) &+ T \left\langle x - \bar x \right\rangle^{- 2} \\ &q_x\left(x\right) : &R_{h} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) &- R_{v} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right)
\end{align}
```

Daarnaast introduceert een inklemming ook drie randvoorwaarden:

```{math}
:label: inklemming_vergelijkingen
\begin{align}
&\varphi \left( \bar x \right) = 0\\
&u_v \left(\bar x\right) = 0\\
&u_h \left(\bar x\right) = 0
\end{align}
```

#### Scharnier- en roloplegging
Aangezien krachten in de richting van de staaf nog niet worden meegenomen, kunnen scharnier- en rolopleggingen op dezelfde manier worden gemodelleerd. In {numref}`Figuur_8` en {numref}`Figuur_15` is weergegeven hoe een scharnieroplegging gemodelleerd kan worden.

```{figure} figures/image8.png
---
width: 400
name: Figuur_8
align: center
---
Modelleren van en scharnieroplegging {cite:p}`vanderwulp_2023`
```

```{figure} figures/image15.png
---
width: 300
name: Figuur_15
align: center
---
Modelleren van een scharnieroplegging bij extensie {cite:p}`vanderwulp_2023`
```

Dit kan beschreven worden met singulariteitsfuncties met ordes $-1$ met onbekende groottes $R_v$, $R_h$ en $T$ op punt $\bar x$ waarbij de staaf een hoek $\theta \left( \bar x \right)$ heeft in 1D en 2D:

```{math}
:label: schranieropl_1d_krachten
\begin{align}
&q_z\left(x\right) : &R_{v} \left\langle x - \bar x \right\rangle^{- 1} \\ &q_x\left(x\right) : &R_{h} \left\langle x - \bar x \right\rangle^{- 1}
\end{align}
```

```{math}
:label: scharnieropl_2d_krachten
\begin{align}
&q_z\left(x\right) : &R_{h} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) &+ R_{v} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) \\
&q_x\left(x\right): &R_{h} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) &- R_{v} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right)
\end{align}
```

Daarnaast introduceert een scharnier ook twee randvoorwaarden:

```{math}
:label: scharnieropl_vergelijkingen
\begin{align}
&u_v \left(\bar x\right) = 0\\
&u_h \left(\bar x\right) = 0
\end{align}
```

Bij een rolscharnier vervallen de krachten en vergelijkingen in vrijgemaakte richting

#### Scharnier
Scharnierende verbindingen in constructies kunnen worden beschreven met singulariteitsfuncties van orde $-3$. Dit valt te beredeneren uit het feit dat scharnieren een sprong in de krommingslijn geven, en daar dus orde $0$ hebben. Terug differentiëren naar de belasting vergelijking geeft een singulariteitsfunctie van orde $-3$.

In {numref}`Figuur_9` is weergegeven hoe een scharnier gemodelleerd kan worden.

```{figure} figures/image9.png
---
width: 300
name: Figuur_9
align: center
---
Modelleren van een scharnier {cite:p}`vanderwulp_2023`, correctie {cite:p}`mark_2024`
```

Dit kan beschreven worden met singulariteitsfuncties met orde $-3$ met onbekende grootte $\Delta \varphi$ op punt $\bar x$ in zowel 1D als 2D met dezelfde vergelijking:

```{math}
:label: schranier_krachten
q_z\left(x\right) : EI \ \Delta \varphi \left\langle x - \bar x \right\rangle^{- 3}
```

Een scharnier introduceert ook een randvoorwaarde. Ter plaatse van het scharnier is het moment ($M$) gelijk aan $0$.

```{math}
:label: scharnier_vergelijking
M \left(\bar x\right) = 0
```


#### Schuifscharnier
Schuifscharnieren in een constructie kunnen worden beschreven met singulariteitsfuncties van orde $-4$. Zoals roterende scharnieren een sprong geven in de krommingslijn, geven schuifscharnieren een sprong in de doorbuigingslijn. Hieruit volgt dat schuifscharnieren in de belasting vergelijking beschreven worden met een singulariteitsfunctie van orde $-4$. 

In {numref}`Figuur_10` is weergegeven hoe een schuifscharnier gemodelleerd kan worden.

```{figure} figures/image10.png
---
width: 300
name: Figuur_10
align: center
---
Modelleren van een scharnier {cite:p}`vanderwulp_2023`, correctie {cite:p}`mark_2024`
```

Dit kan beschreven worden met singulariteitsfuncties met ordes $-4$ met onbekende grootte $\Delta u_z$ op punt $\bar x$:

```{math}
:label: schuifscharnier_krachten
q_z\left(x\right) : EI \ \Delta u_z \left\langle x - \bar x \right\rangle^{- 4}
```

Een schuifscharnier introduceert ook een randvoorwaarde. Ter plaatse van het schuifscharnier is de dwarskracht ($V$) gelijk aan $0$.

```{math}
:label: schuifscharnier_vergelijking
V \left(\bar x\right) = 0
```

#### Telescoopscharnieren
Deze scharnieren hebben axiale verplaatsing als vrijheidsgraad. Dit geeft een sprong in de vergelijking voor axiale verplaatsing ter plaatse van het scharnier. Deze spong kan gemodelleerd worden met de Heaviside functie. Terug differentiëren naar de belastingvergelijking geeft dan een singulariteitsfunctie met orde $-2$.

In {numref}`Figuur_16` is weergegeven hoe een telescoopscharnier gemodelleerd kan worden.

```{figure} figures/image16.png
---
width: 300
name: Figuur_16
align: center
---
Modelleren van telescoop scharnieren {cite:p}`vanderwulp_2023`
```

Dit kan beschreven worden met singulariteitsfuncties met ordes $-2$ met onbekende grootte $\Delta u_x$ op punt $\bar x$:

```{math}
:label: telescoopscharnier_krachten
q_x\left(x\right) : EA \ \Delta u_x \left\langle x - \bar x \right\rangle^{- 2}
```

Een telescoopscharnier introduceert ook een randvoorwaarde. Ter plaatse van het telescoopscharnier is de normaalkracht ($N$) gelijk aan $0$.

```{math}
:label: telescoopscharnier_vergelijking
N \left(\bar x\right) = 0
```

#### Verende opleggingen
Er zijn twee soorten verende opleggingen: verende opleggingen die verplaatsing tegengaan en verende opleggingen die rotatie tegen gaan. In beide gevallen wordt de veer gemodelleerd als kracht ter plaatse van de oplegging in de belasting vergelijking.

In {numref}`Figuur_11`, {numref}`Figuur_17` en {numref}`Figuur_12` is weergegeven hoe de veren gemodelleerd kunnen worden.

```{figure} figures/image11.png
---
width: 300
name: Figuur_11
align: center
---
Modelleren van een translerende verende oplegging {cite:p}`vanderwulp_2023`
```

```{figure} figures/image17.png
---
width: 300
name: Figuur_17
align: center
---
Modelleren van een verende scharnieroplegging bij extensie {cite:p}`vanderwulp_2023`
```

```{figure} figures/image12.png
---
width: 300
name: Figuur_12
align: center
---
Modelleren van een roterende verende oplegging {cite:p}`vanderwulp_2023`
```

Een verende oplegging in alle richtingen die verticale verplaatsing tegengaat wordt gemodelleerd als puntlast met een grootte van $F_{\text{veer},v}$, $F_{\text{veer},h}$, $T_{\text{veer}}$. 

Dit kan beschreven worden met singulariteitsfuncties met ordes $-1$ en $-2$ met onbekende groottes $R_v$, $R_h$ en $T$ op punt $\bar x$ waarbij de staaf een hoek $\theta \left( \bar x \right)$ heeft in 1D en 2D:

```{math}
:label: verend_1d_krachten
\begin{align}
&q_z\left(x\right) : &F_{\text{veer},v} \left\langle x - \bar x \right\rangle^{- 1} &+ T_{\text{veer}} \left\langle x - \bar x \right\rangle^{- 2} \\
&q_x\left(x\right) : &F_{\text{veer},h} \left\langle x - \bar x \right\rangle^{- 1}
\end{align}
```

```{math}
:label:  verend_2d_krachten
\begin{align}
&q_z\left(x\right) : &F_{\text{veer},h} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) &+ F_{\text{veer},v} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) &+ T_{\text{veer}} \left\langle x - \bar x \right\rangle^{- 2} \\ &q_x\left(x\right) : &R_{\text{veer},h} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) &- R_{\text{veer},v} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right)
\end{align}
```

De randvoorwaardes die hierbij worden geintroduceerd zijn bevatten de veerconstantes $K_T$, $K_V$ en $K_N$:

```{math}
:label: verend_vergelijkingen
\begin{align}
&\varphi \left( \bar x \right) = &- \cfrac{T_{\text{veer}}}{K_M}\\
&u_v \left(\bar x\right) = &- \cfrac{F_{\text{veer},v}}{K_V}\\
&u_h \left(\bar x\right) = &- \cfrac{F_{\text{veer},h}}{K_N}
\end{align}
```

Een deels verende oplegging is natuurlijk ook mogelijk met het weglaten van de desbetreffende termen.

#### Verende verbindingen
Verende verbindingen worden gemodelleerd als de verbinding waar het om gaat met een andere 
randvoorwaarde.

In {numref}`Figuur_14`, numref}`Figuur_18` en {numref}`Figuur_13` is weergegeven hoe de verende verbindingen gemodelleerd kunnen worden.

```{figure} figures/image14.png
---
width: 300
name: Figuur_14
align: center
---
Modelleren van een roterende verende verbinding {cite:p}`vanderwulp_2023`, correctie {cite:p}`mark_2024`
```

```{figure} figures/image18.png
---
width: 300
name: Figuur_18
align: center
---
Modelleren van verende telescoopscharnieren {cite:p}`vanderwulp_2023`
```

```{figure} figures/image13.png
---
width: 300
name: Figuur_13
align: center
---
Modelleren van een translerende verende verbinding {cite:p}`vanderwulp_2023`, correctie {cite:p}`mark_2024`
```

De veer wordt dus beschreven als een scharnier met krachten met een grootte van $F_{\text{veer},V}$, $F_{\text{veer},N}$, $T_{\text{veer}}$. Dit kan beschreven worden met singulariteitsfuncties met orde $-3$ met onbekende grootte $\Delta \varphi$, $\Delta u_z$, $\Delta u_x$ op punt $\bar x$ in 1D:

```{math}
:label: schranier_verend_krachten
\begin{align}
$q_z\left(x\right) : $EI \ \Delta \varphi \left\langle x - \bar x \right\rangle^{- 3} $+ T_{\text{veer}} \left\langle x - \bar x \right\rangle^{- 2} \\
&& EI \ \Delta u_z \left\langle x - \bar x \right\rangle^{- 4} $+ F_{\text{veer},V} \left\langle x - \bar x \right\rangle^{- 1}
$q_x\left(x\right) : $EA \ \Delta u_x \left\langle x - \bar x \right\rangle^{- 2} $+ F_{\text{veer},N} \left\langle x - \bar x \right\rangle^{- 1} \\
\end{align}
```

In 2D worden de reactiekrachten berekend in het lokale assenstelsel maar moeten deze worden omgeschreven naar het globale assenstelsel in de belastingsvergelijking.

De bijbhorende voorwaardes zijn dan als volgt:

```{math}
:label: scharnier_vervend_vergelijking
\begin{align}
&M \left(\bar x\right) = &T_{\text{veer}} = &-K_M \cdot \Delta \varphi \\
&V \left(\bar x\right) = &F_{\text{veer},V} = &-K_V \cdot \Delta u_z \\
&N \left(\bar x\right) = &F_{\text{veer},N} = &-K_N \cdot \Delta u_x
\end{align}
```

Ook hier is een deels verende verbinding is natuurlijk ook mogelijk met het weglaten van de desbetreffende termen.

## 3.  Invloedslijnen met Macaulay

De methode van Macaulay kan worden gebruikt om invloedslijnen te berekenen. In dit hoofdstuk zal worden toegelicht hoe de methode hierbij kan worden ingezet. Hierbij zal de focus liggen op de basis van invloedslijnen met Macaulay, door te beschrijven hoe invloedslijnen berekend kunnen worden voor eendimensionale constructies.

### Methode
De eerste stap voor het berekenen van invloedslijnen met de methode van Macaulay is het beschrijven van de krachtsverdeling op de ligger. Hierbij worden alle krachten die op de ligger spelen gedefinieerd op een positie $x$, waarin $x$ de variabele is die de positie op de ligger beschrijft. De puntlast waarvoor de invloedslijnen worden bepaald wordt gedefinieerd op een positie $x = \bar x_F$. Deze methode is weergegeven in figuur {numref}`Figuur_19`.

```{figure} figures/image19.png
---
width: 300
name: Figuur_19
align: center
---
Methode voor invloedslijnen met Macaulay  {cite:p}`jankie_2023`
```

Vervolgens kan de belastingvergelijking worden geïntegreerd naar $x$. Dit zal resulteren in vergelijkingen met onbekende reactiekrachten en integratieconstanten.

De randvoorwaarden kunnen worden opgesteld. Deze worden gebruikt om de onbekende reactiekrachten en integratieconstanten uit de vergelijkingen op te lossen.

Invullen van de gevonden waardes voor de onbekenden in de geïntegreerde belastingvergelijking resulteert in de gewenste functies. Deze functies hangen af van $x$ en $\bar x_F$. Waarin voor $x$ een positie op de ligger ingevuld kan worden en $\bar x_F$ de locatie van de puntlast beschrijft. Zo kan de invloed van een puntlast op locatie $\bar x_F$ op de staafeigenschappen op locatie $x$ worden bepaald.

## 4.  Oplossen van geknikte, vertakte en gesloten constructies

De Macaulay methode kan worden uitgebreid zodat het ook toepasbaar is op tweedimensionale, inclusief geknikte, vertakte en gesloten, constructies. De belangrijkste sterktepunten van het model zijn dat het systematisch en robuust is doordat het is gebaseerd op de principes van evenwicht en continuïteit, de snedekrachten en verplaatsingen van elk punt kunnen worden bepaald doordat de functie continue is en dat de oplossingsvoorwaarden geringer in tal en eenvoudiger zijn dan voor de traditionele integratiemethode.

### 4.1 Assenstelsel

Het model maakt gebruik van een globaal en een lokaal assenstelsel. Het globale assenstelsel bestaat uit een horizontale en een verticale as waarbij de positieve richtingen naar rechts en naar beneden wijzen. Het lokale assenstelsel bestaat uit een $x$-as en een $z$-as. De positieve $x$-as wordt afgebeeld met een blauwe pijl zichtbaar in {numref}`Figuur_20`en de positieve $z$-as is altijd een kwartslag met de klok mee t.o.v. de positieve $x$-as.

Alle belastingen werken langs de globale assen, verdeelde belastingen werken langs de lengte van de staaf (zoals eigengewicht) en hoeken worden gemeten van de positieve h-as naar de positieve x-as

De externe krachten en de verplaatsingen worden globaal genoteerd en de snedekracht-diagrammen lokaal. Er zijn twee vergelijkingen die de lokale as volgen. $q_{z}(x)$ is voor de krachten loodrecht op de staaf en integreert naar de dwarskrachtenvergelijking, enz. en $q_{x}(x)$ is voor de krachten parallel aan de staaf en integreert naar de normaalkrachtenvergelijking, enz.

```{figure} figures/image20_2.svg
---
width: 300
name: Figuur_20
align: center
---
Positieve assen in constructie  {cite:p}`alex_2024`
```

### 4.2 Modelleren van belastingen

De belastingen worden in 2D anders gemodelleerd dan in 1D. Er wordt in het model onderscheid gemaakt tussen een scharnier ($\varphi_{s}$), koppel ($T$), horizontale en verticale puntlast ($F_{h}\ en\ F_{v}$) en horizontale en verticale gelijkmatig verdeelde belasting ($q_{h}\ en\ q_{v}$). De vergelijking voor elke belasting is anders voor $q_{z}(x)$ en $q_{x}(x)$ en bestaan telkens uit een beginterm voor het aangrijppunt van de belasting en een systematische reeks hoektermen voor elke hoek waar de functie van $x$ langs gaat na het aangrijppunt van de belasting. De beginterm is telkens vergelijkbaar met de term voor 1D en de hoektermen zijn bepaald door te analyseren wat de invloed is van een hoek op de snedekrachtdiagrammen van een belasting.

In het volgende stuk is $\bar x$ de afstand langs de x-as tot het begin-/aangrijppunt van de belasting, de afstand langs de x-as tot hoekpunt $i$, $\theta$ de hoek van de positieve horizontale as naar de positieve x-as.

#### Koppel
Een koppel heeft geen invloed op de normaal- en dwarskrachten. Verder blijft het buigend moment van een koppel onveranderd bij een knikpunt. Daarom volgen vgl. {eq}`vgl_Tqz` en {eq}`vgl_Tqx`.

```{math}
:label: vgl_Tqz
q_{z}(x) = T\left\langle x - \bar x \right\rangle^{- 2}
```

```{math}
:label: vgl_Tqx
q_{x}(x) = 0
```

#### Puntlast
Bij de normaal- en dwarskrachtenlijn van een puntlast ontstaat een sprong als de functie een hoekpunt passeert. Tegelijkertijd ontstaat er een knik in de momentenlijn als de functie een hoekpunt passeert. Deze sprong en knik ontstaan door de verandering van de projectie van de puntlast. Daarom volgen vgl. {eq}`vgl_Fvqz` en {eq}`vgl_Fvqx`,

```{math}
:label: vgl_Fvqz
q_{z}\left(x\right) = F_{v}\left( \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) + \sum\limits_{i}^{n} \left\langle \bar x_i - \bar x \right\rangle^{0} \left\langle x - \bar x_{i} \right\rangle^{- 1}\left( \cos\left( \theta \left( \bar x_{i} \right) \right) - \cos\left( \theta \left( \bar x_{i-1} \right) \right) \right) \right) + F_{h}\left( \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) + \sum\limits_{i}^{n} \left\langle \bar x_i - \bar x \right\rangle^{0} \left\langle x - \bar x_{i} \right\rangle^{- 1}\left( \sin\left( \theta \left( \bar x_{i} \right) \right) - \sin\left( \theta \left( \bar x_{i-1} \right) \right) \right) \right)
```

```{math}
:label: vgl_Fvqx
q_{x}\left(x\right) = -F_{v}\left( \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) + \sum\limits_{i}^{n} \left\langle \bar x_i - \bar x \right\rangle^{0} \left\langle x - \bar x_{i} \right\rangle^{- 1}\left( \sin\left( \theta \left( \bar x_{i} \right) \right) - \sin\left( \theta \left( \bar x_{i-1} \right) \right) \right) \right) + F_{h}\left( \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) + \sum\limits_{i}^{n} \left\langle \bar x_i - \bar x \right\rangle^{0} \left\langle x - \bar x_{i} \right\rangle^{- 1}\left( \cos\left( \theta \left( \bar x_{i} \right) \right) - \cos\left( \theta \left( \bar x_{i-1} \right) \right) \right) \right)
```

Met $\bar x$ de locatie van de kracht, en $n$ het aantal knikken met voor elke knik $i$ een bijbehorende coordinaat $\bar x_i$ en hoek $\theta \left( \bar x_i \right)$.

#### Gelijkmatig verdeelde belasting
Bij de normaal- en dwarskrachtenlijn van een uniform verdeelde belasting ontstaat zowel een sprong als een knik als de functie een hoekpunt passeert. De knik ontstaat door de verandering van de projectie van de verdeelde belasting. De sprong daarentegen ontstaat door een verandering in de projectie van de arbitrale belasting vervangend puntlast. Daarom volgen vgl. {eq}`vgl_qvqz`, {eq}`vgl_qhqz`, {eq}`vgl_qvqx` en {eq}`vgl_qhqx`.

```{math}
:label: vgl_qvqz
q_{z}(x) = q_{v}\left( \left\langle x - b \right\rangle^{0}\cos\left( \theta_{b} \right)\  + \sum_{}^{}\left( \left( {\left\langle x - a_{i} \right\rangle}^{0} + \left\langle x - a_{i} \right\rangle^{- 1}\left( a_{i} - b \right) \right)\left( \cos\left( \theta_{i} \right) - \cos\left( \theta_{i - 1} \right) \right) \right) \right);\ \ voor\ a_{i} > b
```

```{math}
:label: vgl_qhqz
q_{z}(x) = q_{h}\left( \left\langle x - b \right\rangle^{0}\sin\left( \theta_{b} \right) + \sum_{}^{}\left( \left( {(\left\langle x - a_{i} \right\rangle}^{0} + \left\langle x - a_{i} \right\rangle^{- 1}\left( a_{i} - b \right) \right)\left( \sin\left( \theta_{i} \right) - \sin\left( \theta_{i - 1} \right) \right) \right) \right)\ \ ;\ \ voor\ a_{i} > b
```

```{math}
:label: vgl_qvqx
q_{x}(x) = - q_{v}\left( \left\langle x - b \right\rangle^{0}\sin\left( \theta_{b} \right) + \sum_{}^{}\left( \left( {(\left\langle x - a_{i} \right\rangle}^{0} + \left\langle x - a_{i} \right\rangle^{- 1}\left( a_{i} - b \right) \right)\left( \sin\left( \theta_{i} \right) - \sin\left( \theta_{i - 1} \right) \right) \right) \right)\ \ ;\ \ voor\ a_{i} > b
```

```{math}
:label: vgl_qhqx
q_{x}(x) = q_{h}\left( \left\langle x - b \right\rangle^{0}\cos\left( \theta_{b} \right) + \sum_{}^{}\left( \left( {(\left\langle x - a_{i} \right\rangle}^{0} + \left\langle x - a_{i} \right\rangle^{- 1}\left( a_{i} - b \right) \right)\left( \cos\left( \theta_{i} \right) - \cos\left( \theta_{i - 1} \right) \right) \right) \right)\ \ ;\ \ voor\ a_{i} > b
```


### 4.3 Vergelijking voor horizontale en verticale verplaatsingen

De doorbuiging ($u_{z}(x)$) en extensie ($u_{x}(x)$) zijn voor tweedimensionale constructies hele abstracte termen die niet bruikbaar zijn voor de oplossingsvoorwaarden. Daarom moeten ze worden gebruikt als invoer voor de vergelijkingen van de horizontale en verticale verplaatsing van de constructie ($u_{h}(x)$ en $u_{v}(x)$). De vergelijkingen stellen telkens dat de invloed van de doorbuiging en extensie van een staaf $ij$ ($u_{z,ij}(x)$ en $u_{x,ij}(x)$) op $u_{z}(x)$ en $u_{z}(x)$ gelijk aan nul is als $x < a_{i}$, een functie is als $a_{i} \leq x < a_{j}$ en constant is als $a_{j} \leq x$. Dit wordt afgebeeld in Figuur {numref}`Figuur_21` en {numref}`Figuur_22`. Vervolgens worden $u_{z,ij}(x)$ en $u_{x,ij}(x)$ vermenigvuldigd met een functie van de hoek van de staaf wat tot slot voor alle staven wordt opgesomd. Hieruit ontstaan vgl. {eq}`vgl_uv` en {eq}`vgl_uh`.

```{math}
:label: vgl_uv
u_{v}(x) = u_{z}(0)\cos\left( \theta_{0} \right) - u_{x}(0)\sin\left( \theta_{0} \right) +
\sum_{i = 0}^{i = n}\begin{pmatrix}\left( \left( u_{z}(x) - u_{z}\left( a_{i} \right) \right)\left\langle x - a_{i} \right\rangle^{0} - \left( u_{z}(x) - u_{z}\left( a_{j} \right) \right)\left\langle x - a_{j} \right\rangle^{0} \right)\cos\left( \theta_{i} \right) \\ - \left( \left( u_{x}(x) - u_{x}\left( a_{i} \right) \right)\left\langle x - a_{i} \right\rangle^{0} - \left( u_{x}(x) - u_{x}\left( a_{j} \right) \right)\left\langle x - a_{j} \right\rangle^{0} \right)\sin\left( \theta_{i} \right) \end{pmatrix}
```

```{math}
:label: vgl_uh
u_{h}(x) = u_{z}(0)\sin\left( \theta_{0} \right) + u_{x}(0)\cos\left( \theta_{0} \right) + \sum_{i = 0}^{i = n}\begin{pmatrix} \left( \left( u_{z}(x) - u_{z}\left( a_{i} \right) \right)\left\langle x - a_{i} \right\rangle^{0} - \left( u_{z}(x) - u_{z}\left( a_{j} \right) \right)\left\langle x - a_{j} \right\rangle^{0} \right)\sin\left( \theta_{i} \right) \\+ \left( \left( u_{x}(x) - u_{x}\left( a_{i} \right) \right)\left\langle x - a_{i} \right\rangle^{0} - \left( u_{x}(x) - u_{x}\left( a_{j} \right) \right)\left\langle x - a_{j} \right\rangle^{0} \right)\cos\left( \theta_{i} \right)
 \end{pmatrix}
```

```{figure} figures/image21.svg
---
width: 400
name: Figuur_21
align: center
---
De invloed van $u_{x,ij}\left(x\right)$ op $u_{x}\left(x\right)$  {cite:p}`alex_2024`
```

```{figure} figures/image22.svg
---
width: 400
name: Figuur_22
align: center
---
De invloed van $u_{z,ij}\left(x\right)$ op $u_{z}\left(x\right)$  {cite:p}`alex_2024`
```

### 4.4 Vertakte en gesloten constructies

Met de tot nu toe in dit hoofdstuk verstreken informatie kunnen geknikte constructies worden gemodelleerd met de Macaulay methode. Voor vertakte en gesloten constructies bestaan er drie bijzondere punten met unieke eigenschappen. Dit zijn het knooppunt ($a_k$), sprongpunt ($a_s$) en aansluitpunt ($a_a$).

```{figure} figures/Figuur_vertakt.svg
---
width: 300
name: Figuur_vertakt
align: center
---
Vertakte constructie {cite:p}`alex_2024`
```

```{figure} figures/Figuur_gesloten.svg
---
width: 300
name: Figuur_gesloten
align: center
---
Gesloten constructie {cite:p}`alex_2024`
```

#### Knooppunt
Het knooppunt is het punt waarbij de functie van $x$ voor het eerst langs een knoop gaat (zoals pijl 1 op knoop B in {numref}`Figuur_vertakt`). Op $a_k$ moet voor elke staaf $IJ$ waarnaar de functie niet direct de weg vervolgd drie onbekende krachten worden toegevoegd $V^{IJ}$, $H^{IJ}$ en $T^{IJ}$. Hierin vertegenwoordigd $V^{IJ}$ de verticale kracht, $H^{IJ}$ de horizontale kracht en $T^{IJ}$ de koppel voortkomend uit staaf $IJ$ werkend op knoop $I$.

#### Sprongpunt
Het sprongpunt, (zie {numref}`Figuur_sprongpunt`) is het punt waar de functie van $x$ in het globale assenstelsel een sprong maakt van punt $I$, wat een uiteinde of afsluiting is van een vertakking, naar punt $J$, wat een knoop is waar de functie van $x$ al eerder langs is geweest (zoals van punt C naar knoop B in figuur {numref}`Figuur_vertakt`). In het lokale assenstelsel verloopt de functie echter continue. Belastingen werkende op punt $I$ moeten gemodelleerd worden op $a_s^-$ en op punt $J$ op $a_s^+$. Op $a_s^+$ moeten ook de onbekende krachten $-V^{JK}$, $-H^{JK}$ en $-T^{JK}$ worden toegevoegd voor staaf $JK$ waarnaar de functie na de sprong de weg vervolgd. Verder moeten op $a_s^+$ de sprongconstanten $\varphi^{IJ}$, $u_z^{IJ}$ en $u_x^{IJ}$ toegevoegd worden voor de sprong in vervormingen tussen punt $I$ en $J$. Deze worden als volgt gemodelleerd:

```{math}
:label: vgl_sprong_phi_uz
$q_z\left(x\right)=EI\varphi^{ij}x-as+-3+EIuzijx-as+-4$
```
```{math}
:label: vgl_sprong_ux
$q_x\left(x\right)=EAu_x^{ij}x-as+-2$
```

```{figure} figures/sprongpunt.svg
---
width: 300
name: Figuur_sprongpunt
align: center
---
Modelleren van een sprongpunt {cite:p}`alex_2024`
```

#### Aansluitpunt
Het aansluitpunt is het punt waarbij de functie van x opnieuw langs een knoop gaat (zoals knoop B vanuit punt E in figuur {numref}`Figuur_gesloten`). $Op a_a^-$ moeten de drie onbekende krachten $-V^{IJ}$, ${-H}^{IJ}$ en $-T^{IJ}$ voor de staaf $IJ$  dat aansluit op punt $I$. Het aansluitpunt kan het einde zijn van de functie, maar de functie kan ook direct de weg vervolgen of een sprong maken. In dat geval gelden dezelfde regels als voor het sprongpunt (met of zonder sprongconstanten voor weg vervolgen of sprong maken)

## Overzicht modellering discontinuïteiten

In {numref}`table_twee` {cite:p}`alex_2024` wordt voorgeschreven welke oplossingsvoorwaarden gelden voor starre onstructies als lokale afstand $\bar x$ de benoemde eigenschap.

````{div} full-width
```{table} Onbekenden en vergelijkingen discontinuïteiten in 2D
:name: table_twee

| Situatie op $\bar x$| Belastingsvergelijing | Vergelijkingen | Onbekenden | 
| ---  | --------------------- | --------------------- | -------------------- |
| Beginpunt constructie | | $N\left(\bar x^-\right) = 0$ <br> $V\left(\bar x^-\right) = 0$ <br> $M\left(\bar x^-\right) = 0$ <br> | Integratieconstantes $C_V$, $C_M$, $C_N$ | 
| Eindpunt constructie | | $N\left(\bar x\right) = 0$ <br> $V\left(\bar x^+\right) = 0$ <br> $M\left(\bar x^+\right) = 0$ <br> | Integratieconstantes $C_w$, $C_{\varphi}$, $C_u$ |
| Puntlast | $\begin{align} &q_z\left(x\right) : &F_{v} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left(\bar x\right) \right) &+F_{h} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left(\bar x\right) \right) \\ &q_x\left(x\right) : &- F_{v} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta\left(\bar x\right) \right) &+F_{h} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left(\bar x\right) \right) \end{align}$ | | |
| Koppel | $\begin{align} &q_z\left(x\right): &T \left\langle x - \bar x \right\rangle^{- 2} \\ &q_x\left(x\right): &0 \end{align}$ | | | 
| Verdeelde belasting | $\begin{align} &q_z\left(x\right): &q_{v} \left\langle x - \bar x_1 \right\rangle^{- 1} \cos \left( \theta \left(\bar x_1\right) \right) &-q_{v} \left\langle x_2 - \bar x \right\rangle^{- 1} \cos \left( \theta \left(\bar x_2\right) \right) \\ & &+ q_{h} \left\langle x - \bar x_1 \right\rangle^{- 1} \sin \left( \theta \left(\bar x_1\right) \right) &-q_{h} \left\langle x - \bar x_2 \right\rangle^{- 1} \sin \left( \theta \left(\bar x_2\right) \right) \\ & q_x \left(x \right) : &- q_{v} \left\langle x - \bar x_1 \right\rangle^{- 1} \sin \left( \theta \left(\bar x_1\right) \right) &+q_{v} \left\langle x - \bar x_2 \right\rangle^{- 1} \sin \left( \theta \left(\bar x_2\right) \right) \\ &&+q_{h} \left\langle x - \bar x_1 \right\rangle^{- 1} \cos \left( \theta \left(\bar x_1\right) \right) &- q_{h} \left\langle x - \bar x_2 \right\rangle^{- 1} \cos \left( \theta \left(\bar x_2\right) \right) \end{align}$ |||
| Scharnierverbinding | $q_z\left(x\right) : EI \Delta \varphi_S \left\langle x - \bar x \right\rangle^{- 3}$ | $M \left(\bar x\right) = 0$| $\Delta \varphi_S$ |
| Schuifverbinding | $q_z\left(x\right): EI \Delta u_{S,z} \left\langle x - \bar x \right\rangle^{- 4}$ | $V \left(\bar x\right) = 0$| $\Delta u_{S,z}$ |
| Telescoopverbinding | $q_x\left(x\right) :EA \Delta u_{S,x} \left\langle x - \bar x \right\rangle^{- 2}$ | $N \left(\bar x\right) = 0$| $\Delta u_{S,x}$ |
| Verticale roloplegging | $q_z\left(x\right) : R_{h} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta\left( \bar x \right) \right) $<br> $q_x\left(x\right) : R_{h} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) $ | $u_h \left( \bar x \right) = 0$ | $R_h$ |
| Horizontale roloplegging | $q_z\left(x\right) : R_{v} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) $ <br> $q_x\left(x\right): - R_{v} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) $ | $u_v \left( \bar x \right) = 0 $|$R_v$ |
| Scharnierende oplegging | $q_z\left(x\right) : R_{h} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) + R_{v} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right)$<br> $q_x\left(x\right) : R_{h} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) - R_{v} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) $  |$u_v \left(\bar x\right) = 0$ <br> $u_h \left(\bar x\right) = 0$ | $R_h$, $R_v$ |
| Inklemming | $\begin{align} &q_z\left(x\right) : &R_{h} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) &+ R_{v} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) &+ T \left\langle x - \bar x \right\rangle^{- 2} \\ &q_x\left(x\right) : &R_{h} \left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) &- R_{v} \left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right)\end{align}$ | $\begin{align} &\varphi \left( \bar x \right) = 0\\ &u_v \left(\bar x\right) = 0\\ &u_h \left(\bar x\right) = 0 \end{align}$ | $R_h$, $R_v$, $T$ |
| Aansluitpunt | $q_z\left(x\right) : \Delta V \left\langle x - \bar x_1  \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right) - \Delta V \left\langle x - \bar x  \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right)$ <br> $ \qquad + \Delta H\left\langle x - \bar x_1 \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) - \Delta H\left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right)$ <br> $\qquad +\Delta T \left\langle x - \bar x_1 \right\rangle^{- 2}  - \Delta T \left\langle x - \bar x \right\rangle^{- 2} $ <br> $q_x\left(x\right) : -\Delta V \left\langle x - \bar x_1  \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right) + \Delta V \left\langle x - \bar x  \right\rangle^{- 1}\sin\left( \theta \left( \bar x \right) \right)$<br>$\qquad + \Delta H\left\langle x - \bar x_1 \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right)  - \Delta H\left\langle x - \bar x \right\rangle^{- 1}\cos\left( \theta \left( \bar x \right) \right)$  <br> met $\bar x_1$ de coordinaat van de eerste keer dat langs de vertakking is gegaan| $\varphi\left( \bar x \right) = \varphi \left( \bar x_1 \right)$ <br>$u_v\left( \bar x \right) = u_v \left( \bar x_1 \right)$ <br>$ u_h\left( \bar x \right) = u_h \left( \bar x_1 \right)$ | $\Delta H$, $\Delta V$, $\Delta T$ ||
| Sprongpunt naar andere vertakking | $q_z\left(x\right) : \Delta V \left\langle x - \bar x_1  \right\rangle^{- 1}\cos\left( \theta \left( \bar x_1 \right) \right) - \Delta V \left\langle x - \bar x_2  \right\rangle^{- 1}\cos\left( \theta \left( \bar x_2 \right) \right)$ <br> $ \qquad + \Delta H\left\langle x - \bar x_1 \right\rangle^{- 1}\sin\left( \theta \left( \bar x_1 \right) \right) - \Delta H\left\langle x - \bar x \right\rangle^{- 1}\sin\left( \theta \left( \bar x_2 \right) \right)$ <br> $\qquad +\Delta T \left\langle x - \bar x_1 \right\rangle^{- 2}  - \Delta T \left\langle x - \bar x_2 \right\rangle^{- 2}$ <br> $ \qquad + EI \Delta \varphi \left\langle x - \bar x_2 \right\rangle^{- 3} + EI \Delta u_z \left\langle x - \bar x_3 \right\rangle^{- 4}$ <br> $q_x\left(x\right) : -\Delta V \left\langle x - \bar x_1  \right\rangle^{- 1}\sin\left( \theta \left( \bar x_1 \right) \right) + \Delta V \left\langle x - \bar x_2  \right\rangle^{- 1}\sin\left( \theta \left( \bar x_2 \right) \right)$<br>$\qquad + \Delta H\left\langle x - \bar x_1 \right\rangle^{- 1}\cos\left( \theta \left( \bar x_1 \right) \right)  - \Delta H\left\langle x - \bar x_2 \right\rangle^{- 1}\cos\left( \theta \left( \bar x_2 \right) \right)$ <br> $\qquad + EI \Delta u_x \left\langle x - \bar x_2 \right\rangle^{- 2}$ <br> met $\bar x_1$ en $\bar x_2$ de coordinaat van de respectievelijk eerste en tweede keer dat langs de vertakking is gegaan en $\bar x_\text{sprong}$ de coordinaat voor de sprong.| $N\left(\bar x_\text{sprong}^{+}\right) = 0$ <br> $V\left(\bar x_\text{sprong}^{+}\right) = 0$ <br> $M\left(\bar x_\text{sprong}^{+}\right) = 0$ <br> $\varphi\left( \bar x_1 \right) = \varphi \left( \bar x_2 \right)$ <br> $u_v\left( \bar x_1 \right) = u_v \left( \bar x_2 \right)$ <br> $u_h\left( \bar x_1 \right) = u_h \left( \bar x_2 \right)$ <br> met $\bar x_1$ en $\bar x_2$ de coordinaat van de respectievelijk eerste en tweede keer dat langs de vertakking is gegaan en $\bar x_\text{sprong}$ de coordinaat voor de sprong.| $\Delta H$, $\Delta V$, $\Delta T$<br> $\Delta u_z$, $\Delta u_x$, $\Delta \varphi$ ||
| Knikpunt | $ q_z \left( x\right) : \sum\limits_{j}\sum\limits_{i}^{n} \left\langle \bar x_i - \bar x_{F_j} \right\rangle^{0} F_{v,j}  \left\langle x - \bar x_i \right\rangle^{- 1}\left( \cos\left( \theta \left( \bar x_i \right) \right) - \cos\left( \theta \left( \bar x_{i-1}^- \right) \right)  \right) $ <br> $\qquad + \sum\limits_{j}\sum\limits_{i}^n \left\langle \bar x_i - \bar x_{F_j} \right\rangle^{0}F_{h,j}  \left\langle x - \bar x_i \right\rangle^{- 1}\left( \sin\left( \theta \left( \bar x_i \right) \right) - \sin\left( \theta \left( \bar x_{i-1}^- \right) \right) \right) $ <br> $\qquad + \sum\limits_{j}\sum\limits_{i}^n \left\langle \bar x_i - \bar x_{q_j} \right\rangle^{0} q_{v,j} \left( {\left\langle x - \bar x_i \right\rangle}^{0} + \left\langle x - \bar x_i \right\rangle^{- 1}\left( \bar x_i - \bar x_{q_j} \right) \right)\left( \cos\left( \theta \left( \bar x_i \right) \right) - \cos\left( \theta \left( \bar x_{i-1}^- \right) \right) \right)$ <br> $ \qquad + \sum\limits_{j}\sum\limits_{i}^n\left\langle \bar x_i - \bar x_{q_j} \right\rangle^{0} q_{h,j} \left( {\left\langle x - \bar x_i \right\rangle}^{0} + \left\langle x - \bar x_u \right\rangle^{- 1}\left( \bar x_i - \bar x_{q_j} \right) \right)\left( \sin\left( \theta \left( \bar x_i \right) \right) - \sin\left( \theta \left( \bar x_{i-1}^- \right) \right) \right) $ <br> $ q_x \left( x\right) : \sum\limits_{j}\sum\limits_{i}^{n} \left(-\left\langle \bar x_i - \bar x_{F_j} \right\rangle^{0} F_{v,j}  \left\langle x - \bar x_i \right\rangle^{- 1}\left( \sin\left( \theta \left( \bar x_i \right) \right) - \sin\left( \theta \left( \bar x_{i-1}^- \right) \right)  \right) \right)$ <br> $\qquad + \sum\limits_{j}\sum\limits_{i}^n \left\langle \bar x_i - \bar x_{F_j} \right\rangle^{0}F_{h,j}  \left\langle x - \bar x_i \right\rangle^{- 1}\left( \cos\left( \theta \left( \bar x_i \right) \right) - \cos\left( \theta \left( \bar x_{i-1}^- \right) \right) \right) $ <br> $\qquad + \sum\limits_{j}\sum\limits_{i}^n \left( -\left\langle \bar x_i - \bar x_{q_j} \right\rangle^{0} q_{v,j} \left( {\left\langle x - \bar x_i \right\rangle}^{0} + \left\langle x - \bar x_i \right\rangle^{- 1}\left( \bar x_i - \bar x_{q_j} \right) \right)\left( \sin\left( \theta \left( \bar x_i \right) \right) - \sin\left( \theta \left( \bar x_{i-1}^- \right) \right) \right) \right)$ <br> $ \qquad + \sum\limits_{j}\sum\limits_{i}^n\left\langle \bar x_i - \bar x_{q_j} \right\rangle^{0} q_{h,j} \left( {\left\langle x - \bar x_i \right\rangle}^{0} + \left\langle x - \bar x_u \right\rangle^{- 1}\left( \bar x_i - \bar x_{q_j} \right) \right)\left( \cos\left( \theta \left( \bar x_i \right) \right) - \cos\left( \theta \left( \bar x_{i-1}^- \right) \right) \right) $ <br> NOG TOEVOEGEN VERPLAATSINGEN <br> met $n$ het aantal knikken met voor elke knik $i$ een bijbehorende hoek $\theta_i$ en voor elke $F_j$ en $q_j$ inclusing $H$, $V$ en $R$.|||


```
````



Als de functie springt naar een scharnierend verbonden staaf of scharnierend aansluit op een knooppunt, dan kunnen de oplosvergelijkingen voor de hoekverdraaiing weggelaten worden. Er hoeven dan ook geen alternatieve voorwaarden worden gesteld.