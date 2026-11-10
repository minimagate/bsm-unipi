---
type: lecture-note
course: Geometria 1
date: '2026-10-01'
title: Fattorizzazione dei polinomi e radici complesse
source_transcript: _transcripts/Geometria 1/2026-09-30 - Fattorizzazione dei polinomi e radici complesse.md
source_hash: sha256:c9f34d88caaaaceb4074db546fd127fa27b26a7317006679f7f3151b619bf750
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-30T09:26:54.384Z'
original_date: '2026-09-30'
date_adjustment: Shifted forward one day to keep one note per course and date.
vault_path: Notes/Geometria 1/Lectures/2026-10-01 - Fattorizzazione dei polinomi e radici complesse.md
vault_hash: ec5185be98394094474de72bfe6fbe73e88e026c2b7d14057224873e89aff852
---
## 1. Teorema fondamentale dell’algebra e fattorizzazione lineare

Il **[[Teorema fondamentale dell'algebra|teorema fondamentale dell’algebra]]** afferma che ogni [[Polinomio|polinomio]] non costante a coefficienti complessi ha almeno una radice complessa:

> Se $P(z)\in\mathbb{C}[z]$ ha grado almeno $1$, allora esiste $z_0\in\mathbb{C}$ tale che
>
> $$
> P(z_0)=0.
> $$

La dimostrazione del teorema fondamentale dell’algebra arriverà più avanti. Oggi invece si dimostra, per induzione sul grado, una sua conseguenza immediata ma molto importante.

## 2. Corollario: fattorizzazione completa in fattori lineari

### Enunciato

Sia $n\in\mathbb{N}$, $n\geq 1$, e sia $P(z)\in\mathbb{C}[z]$ un polinomio di grado $n$. Allora esistono $a\in\mathbb{C}\setminus\{0\}$ e $z_1,\dots,z_n\in\mathbb{C}$ tali che

$$
P(z)=a(z-z_1)(z-z_2)\cdots(z-z_n).
$$

I numeri $z_1,\dots,z_n$ sono le [[Radice di un polinomio|radici]] del polinomio, contate con la loro molteplicità.

Il coefficiente $a$ è il coefficiente del termine di grado massimo di $P$.

### Dimostrazione per induzione

Indichiamo con $P_n$ la proposizione (si usa il [[Principio di induzione|principio di induzione]]):

> Ogni polinomio complesso di grado $n$ si può scrivere come prodotto del proprio coefficiente direttivo e di $n$ fattori lineari.

#### Passo base

Consideriamo un polinomio di grado $1$:

$$
P(z)=a_1z+a_0,
\qquad a_1\neq 0.
$$

Raccogliendo $a_1$ si ottiene

$$
P(z)
=a_1\left(z+\frac{a_0}{a_1}\right)
=a_1\left(z-\left(-\frac{a_0}{a_1}\right)\right).
$$

Quindi, ponendo

$$
z_1=-\frac{a_0}{a_1},
$$

si ha

$$
P(z)=a_1(z-z_1).
$$

La proposizione $P_1$ è dunque vera.

#### Passo induttivo

Supponiamo vera la proposizione per un certo grado $n\geq 1$: ogni polinomio complesso di grado $n$ ammette una fattorizzazione del tipo

$$
Q(z)=a(z-z_1)\cdots(z-z_n).
$$

Dimostriamo che allora vale per i polinomi di grado $n+1$.

Sia $P(z)$ un polinomio complesso di grado $n+1$. Per il teorema fondamentale dell’algebra, essendo $P$ non costante, esiste $z_1\in\mathbb{C}$ tale che

$$
P(z_1)=0.
$$

Dividendo $P(z)$ per il polinomio di primo grado $z-z_1$, si ottiene

$$
P(z)=(z-z_1)Q(z)+r,
$$

dove $r$ è un polinomio di grado minore di $1$, quindi una costante.

Valutando in $z=z_1$:

$$
P(z_1)=(z_1-z_1)Q(z_1)+r=r.
$$

Poiché $P(z_1)=0$, segue che $r=0$. Pertanto

$$
P(z)=(z-z_1)Q(z).
$$

Questo è il teorema del fattore (spesso presentato come conseguenza della regola di Ruffini):

$$
P(z_1)=0
\quad\Longleftrightarrow\quad
z-z_1\text{ divide }P(z).
$$

Il polinomio $Q(z)$ ha grado $n$, perché $P$ ha grado $n+1$ e $z-z_1$ ha grado $1$. Per l’ipotesi induttiva,

$$
Q(z)=a(z-z_2)\cdots(z-z_{n+1}).
$$

Sostituendo:

$$
P(z)
=(z-z_1)Q(z)
=a(z-z_1)(z-z_2)\cdots(z-z_{n+1}).
$$

Questo dimostra $P_{n+1}$ e quindi, per induzione, la proposizione vale per ogni $n\geq 1$.

## 3. Fattorizzazione e radici

Attenzione a non confondere una semplice divisione con resto con una fattorizzazione.

Se si divide $P(z)$ per $z-z_1$, in generale si ottiene

$$
P(z)=(z-z_1)Q(z)+r.
$$

Questa non è ancora una fattorizzazione, perché c’è il termine additivo $r$.

Se invece $z_1$ è una radice, allora $P(z_1)=0$ e il resto è nullo. In tal caso:

$$
P(z)=(z-z_1)Q(z),
$$

che è davvero una fattorizzazione in prodotto di due polinomi.

L’idea è questa:

- una radice $z_1$ permette di estrarre il fattore $z-z_1$;
- una volta scritto il polinomio come prodotto di fattori, il prodotto si annulla se e solo se almeno uno dei fattori si annulla.

Infatti,

$$
P(z)=a(z-z_1)\cdots(z-z_n)
$$

implica

$$
P(z)=0
\quad\Longleftrightarrow\quad
z=z_1\ \text{oppure}\ z=z_2\ \text{oppure}\ \cdots\ \text{oppure}\ z=z_n.
$$

Le radici del polinomio sono dunque le radici dei singoli fattori lineari.

## 4. Molteplicità delle radici

Nella fattorizzazione

$$
P(z)=a(z-z_1)\cdots(z-z_n)
$$

i numeri $z_1,\dots,z_n$ non sono necessariamente distinti: una stessa radice può comparire più volte.

Per esempio,

$$
P(z)=(z-1)^5
$$

ha una sola radice distinta, $1$, ma con molteplicità $5$.

### Definizione

Si dice che $z_0$ è una radice di **molteplicità** $k$ di $P$ se

$$
P(z)=(z-z_0)^kQ(z),
$$

dove $Q(z)$ è un polinomio tale che

$$
Q(z_0)\neq 0.
$$

Equivalentemente, $k$ è il massimo esponente per cui $(z-z_0)^k$ divide $P(z)$:

$$
(z-z_0)^k\mid P(z),
\qquad
(z-z_0)^{k+1}\nmid P(z).
$$

In pratica: trovata una radice $z_0$, si divide $P$ per $z-z_0$; se il quoziente ha ancora la stessa radice si divide di nuovo, e così via finché la radice non compare più.

Per esempio:

$$
P(z)=(z-1)^5.
$$

Dividendo una prima volta per $z-1$ si ottiene $(z-1)^4$; dividendo una seconda volta si ottiene $(z-1)^3$, e così via. Il fattore $z-1$ può essere estratto esattamente cinque volte.

### Esempio con radici di molteplicità diverse

Consideriamo

$$
P(z)=(z-1)^2(z-3)^4(z-5)^3.
$$

Il grado è

$$
2+4+3=9.
$$

Le radici distinte sono:

- $1$, con molteplicità $2$;
- $3$, con molteplicità $4$;
- $5$, con molteplicità $3$.

Contandole con la loro molteplicità, si ottengono complessivamente $9$ radici.

Ecco cosa significa che un polinomio di grado $n$ ha $n$ radici: sono contate con molteplicità, non sono per forza $n$ valori distinti.

## 5. Un polinomio di grado $n$ non può avere più di $n$ radici

La fattorizzazione completa mostra anche che un polinomio non nullo di grado $n$ non può avere più di $n$ radici, contate con molteplicità.

Infatti, supponiamo di aver estratto tutte le radici:

$$
P(x)
=
Q(x)\prod_{j=1}^k (x-x_j)^{m_j},
$$

dove gli $x_j$ sono radici distinte e $m_j$ sono le rispettive molteplicità.

Il numero totale di radici contate con molteplicità è

$$
m_1+\cdots+m_k.
$$

Poiché ciascun fattore $(x-x_j)^{m_j}$ ha grado $m_j$, il prodotto dei fattori estratti ha grado

$$
m_1+\cdots+m_k.
$$

Se $\deg P=n$, allora necessariamente

$$
m_1+\cdots+m_k\leq n.
$$

Se il polinomio residuo $Q$ avesse ancora una radice $x_0$ diversa dalle radici già estratte, allora

$$
P(x_0)
=
Q(x_0)\prod_{j=1}^k (x_0-x_j)^{m_j}.
$$

Per costruzione $Q(x_0)=0$, mentre tutti gli altri fattori sono diversi da zero. Quindi si potrebbe estrarre un ulteriore fattore lineare, aumentando il grado totale dei fattori estratti. Quando il grado totale ha già raggiunto $n$ ciò è impossibile, perché il polinomio residuo deve essere costante.

Di conseguenza:

> Un polinomio non nullo di grado $n$ ha al massimo $n$ radici, contate con molteplicità.

Nel caso dei polinomi complessi, il teorema fondamentale dell’algebra garantisce inoltre che un polinomio di grado $n$ possiede esattamente $n$ radici complesse contate con molteplicità.

## 6. Notazione di divisibilità

La barretta verticale indica la [[Divisibilità|divisibilità]].

Per polinomi o numeri interi, la scrittura

$$
A\mid B
$$

significa che $A$ divide $B$, cioè che esiste un polinomio o numero $C$ tale che

$$
B=AC.
$$

Se invece $A$ non divide $B$, si scrive

$$
A\nmid B.
$$

Per esempio,

$$
z-z_0\mid P(z)
$$

significa che esiste un polinomio $Q(z)$ tale che

$$
P(z)=(z-z_0)Q(z).
$$

Per il teorema del fattore:

$$
P(z_0)=0
\quad\Longleftrightarrow\quad
z-z_0\mid P(z).
$$

## 7. Induzione matematica

La dimostrazione della fattorizzazione è un esempio di dimostrazione per induzione.

Quando un enunciato dipende da un numero naturale $n$, $P_n$ indica la proposizione relativa al valore $n$.

Per dimostrare che $P_n$ è vera per ogni $n$ a partire da un certo valore iniziale si procede in due passi.

### Metodo induttivo standard

1. **Passo base:** si dimostra che $P_1$ è vera.
2. **Passo induttivo:** si dimostra che, per ogni $n$,
   $$
   P_n\Longrightarrow P_{n+1}.
   $$

Da questi due passaggi segue che $P_n$ è vera per ogni $n\geq 1$.

Bisogna dire da quale valore parte $n$. Cambiare l’indice (per esempio usare $n-1$ invece di $n$) è solo una scelta di notazione: nessuna versione è “più corretta”, basta indicare chiaramente il dominio dell’indice.

### Forma equivalente dell’induzione

È equivalente dimostrare:

1. $P_1$ è vera;
2. se sono vere tutte le proposizioni
   $$
   P_1,P_2,\dots,P_n,
   $$
   allora è vera $P_{n+1}$.

Qui l’ipotesi induttiva comprende tutti i casi precedenti, non solo quello immediatamente precedente. A seconda del problema, una forma può essere più comoda dell’altra.

## 8. Polinomi a coefficienti reali come caso particolare

I numeri reali sono contenuti nei [[Numero complesso|numeri complessi]]:

$$
\mathbb{R}\subseteq\mathbb{C}.
$$

Somma e prodotto di numeri reali coincidono con quelli eseguiti in $\mathbb{C}$ e danno ancora un numero reale: $\mathbb{R}$ è quindi chiuso rispetto a tali operazioni.

Di conseguenza, un polinomio a coefficienti reali è anche un polinomio a coefficienti complessi. Il teorema fondamentale dell’algebra si applica quindi anche ai polinomi reali, ma garantisce radici in $\mathbb{C}$, non necessariamente in $\mathbb{R}$.

Un polinomio a coefficienti reali può dunque avere:

- radici tutte reali;
- alcune radici reali e alcune non reali;
- soltanto radici non reali.

Occhio: coefficienti reali non implicano radici tutte reali.

## 9. Coniugio delle radici di un polinomio reale

### Proposizione

Sia

$$
P(z)=a_nz^n+a_{n-1}z^{n-1}+\cdots+a_1z+a_0
$$

un polinomio a coefficienti reali, cioè $a_j\in\mathbb{R}$ per ogni $j$.

Se $z_0\in\mathbb{C}$ è una radice di $P$, allora anche il suo [[Coniugio complesso|coniugato]] $\overline{z_0}$ è una radice:

$$
P(z_0)=0
\quad\Longrightarrow\quad
P(\overline{z_0})=0.
$$

Quindi le radici non reali di un polinomio reale compaiono a coppie coniugate.

Se $z_0$ è reale, allora $\overline{z_0}=z_0$ e la proposizione non aggiunge nulla.

> [!example] Esempio
> $z^2+1$ ha coefficienti reali e radici $i$ e $-i$, che sono coniugate. Invece $z-i$ ha la sola radice $i$: i suoi coefficienti non sono tutti reali.

### Dimostrazione

Poiché $P(z_0)=0$, consideriamo il coniugato di questa uguaglianza:

$$
\overline{P(z_0)}=\overline{0}=0.
$$

Sviluppando:

$$
P(z_0)
=
a_nz_0^n+a_{n-1}z_0^{n-1}+\cdots+a_1z_0+a_0.
$$

Usando le proprietà del coniugio,

$$
\overline{u+v}=\overline{u}+\overline{v},
\qquad
\overline{uv}=\overline{u}\,\overline{v},
$$

e

$$
\overline{z_0^k}=\overline{z_0}^{\,k},
$$

si ottiene

$$
\overline{P(z_0)}
=
\overline{a_n}\,\overline{z_0}^{\,n}
+\overline{a_{n-1}}\,\overline{z_0}^{\,n-1}
+\cdots
+\overline{a_1}\,\overline{z_0}
+\overline{a_0}.
$$

Poiché i coefficienti sono reali,

$$
\overline{a_j}=a_j.
$$

Pertanto

$$
\overline{P(z_0)}
=
a_n\overline{z_0}^{\,n}
+a_{n-1}\overline{z_0}^{\,n-1}
+\cdots
+a_1\overline{z_0}
+a_0
=
P(\overline{z_0}).
$$

Ma $\overline{P(z_0)}=0$, dunque

$$
P(\overline{z_0})=0.
$$

## 10. Molteplicità delle radici coniugate

Il coniugio rispetta anche le molteplicità.

Supponiamo che $z_0\notin\mathbb{R}$ sia una radice di $P$ di molteplicità $m$. Allora

$$
P(z)=(z-z_0)^mQ(z),
$$

dove $Q(z_0)\neq 0$.

Poiché anche $\overline{z_0}$ è una radice, il fattore $z-\overline{z_0}$ divide $P(z)$; inoltre la molteplicità di $\overline{z_0}$ è uguale a quella di $z_0$.

Le radici non reali compaiono quindi a coppie:

$$
z_0,\overline{z_0},
$$

con la stessa molteplicità.

Graficamente, le radici di un polinomio reale sono simmetriche rispetto all’asse reale del piano complesso.

## 11. Il fattore quadratico associato a una coppia coniugata

Se $z_0\notin\mathbb{R}$ è una radice di un polinomio reale, allora anche $\overline{z_0}$ è una radice. Di conseguenza, il prodotto dei due fattori lineari

$$
(z-z_0)(z-\overline{z_0})
$$

divide il polinomio.

Sviluppando:

$$
\begin{aligned}
(z-z_0)(z-\overline{z_0})
&=z^2-(z_0+\overline{z_0})z+z_0\overline{z_0}.
\end{aligned}
$$

Ora,

$$
z_0+\overline{z_0}=2\operatorname{Re}(z_0)\in\mathbb{R},
$$

e

$$
z_0\overline{z_0}=|z_0|^2\in\mathbb{R}.
$$

Pertanto il fattore quadratico

$$
(z-z_0)(z-\overline{z_0})
=
z^2-(z_0+\overline{z_0})z+z_0\overline{z_0}
$$

ha coefficienti reali.

Questo mostra che un polinomio reale può essere fattorizzato, in $\mathbb{R}[z]$, in:

- fattori lineari associati alle radici reali;
- fattori quadratici associati alle coppie di radici complesse coniugate.

Dividendo per questo fattore quadratico si restano nei reali: il quoziente di un polinomio reale per un polinomio reale è ancora reale, quando la divisione è esatta.

## 12. Esempio di fattorizzazione reale

Se un polinomio reale ha radici $1$, $3$ e $5$ con molteplicità rispettivamente $2$, $4$ e $3$, allora

$$
P(z)=a(z-1)^2(z-3)^4(z-5)^3,
\qquad a\in\mathbb{R}\setminus\{0\}.
$$

Se invece possiede una radice non reale $z_0$ di molteplicità $m$, allora possiede anche $\overline{z_0}$ di molteplicità $m$, e compare il fattore

$$
\bigl((z-z_0)(z-\overline{z_0})\bigr)^m.
$$

Le radici non reali non cambiano il numero totale di radici contate con molteplicità: una radice e la sua coniugata formano una coppia, ma ciascuna conta.

## 13. Formula risolutiva per i polinomi di secondo grado complessi

Consideriamo il polinomio

$$
P(z)=az^2+bz+c,
\qquad a\neq 0,
$$

con $a,b,c\in\mathbb{C}$.

La formula risolutiva è formalmente la stessa del caso reale:

$$
z_{1,2}
=
\frac{-b\pm\sqrt{\Delta}}{2a},
$$

dove

$$
\Delta=b^2-4ac.
$$

La differenza è che ora $\Delta$ può essere un numero complesso. Nei complessi ogni numero ha radici quadrate: se $\Delta\neq 0$ ce ne sono due, opposte, cioè $w_1,w_2$ tali che

$$
w_1^2=\Delta,
\qquad
w_2=-w_1.
$$

La scrittura

$$
\pm\sqrt{\Delta}
$$

indica quindi le due scelte date dalle due radici quadrate di $\Delta$.

Se $\Delta=0$, l’unica radice quadrata è $0$ e il polinomio ha una radice doppia:

$$
z=-\frac{b}{2a}.
$$

## 14. Radici quadrate di un numero complesso

Sia

$$
w=re^{i\theta},
\qquad r\geq 0.
$$

Le radici quadrate di $w$ hanno modulo $\sqrt r$ e argomenti

$$
\frac{\theta}{2}
\quad\text{e}\quad
\frac{\theta}{2}+\pi.
$$

Quindi sono opposte tra loro:

$$
\sqrt{w}
=
\pm\sqrt r\,e^{i\theta/2}.
$$

Geometricamente, le due radici quadrate sono i due vertici di un poligono regolare di ordine $2$ sulla circonferenza di raggio $\sqrt r$.

È il caso $n=2$ della regola generale per le [[Radice n-esima di un numero complesso|radici]] $n$-esime di un numero complesso (qui scritto con la [[Forma polare|forma polare]] $re^{i\theta}$).

## 15. Esempio di equazione quadratica complessa

Consideriamo, nella forma ricostruita dalla formula usata a lezione, il polinomio

$$
P(z)=z^2+(1-i)z.
$$

In questo caso

$$
a=1,\qquad b=1-i,\qquad c=0.
$$

Il discriminante è

$$
\Delta=(1-i)^2.
$$

Calcoliamo:

$$
(1-i)^2
=1-2i+i^2
=1-2i-1
=-2i.
$$

Una radice quadrata di $-2i$ è $1-i$, perché

$$
(1-i)^2=-2i.
$$

Le due radici quadrate sono quindi

$$
\pm(1-i).
$$

La formula risolutiva dà

$$
z_{1,2}
=
\frac{-(1-i)\pm(1-i)}{2}.
$$

Da cui:

$$
z_1=0,
$$

e

$$
z_2=-(1-i)=-1+i.
$$

Infatti il polinomio è già fattorizzato:

$$
P(z)=z(z+1-i),
$$

e le sue radici sono $0$ e $-1+i$.

L’esempio mostra anche che, se i coefficienti non sono tutti reali, le radici non compaiono per forza a coppie coniugate.

## 16. Radici $n$-esime dell’unità

Per trovare le soluzioni di

$$
z^n=1,
$$

(le [[Radice n-esima dell'unità|radici dell’unità]]) si scrive $z$ in forma polare:

$$
z=re^{i\theta}.
$$

Poiché

$$
1=e^{2\pi i k}
$$

per ogni $k\in\mathbb{Z}$, l’equazione diventa

$$
r^n e^{in\theta}=e^{2\pi i k}.
$$

Confrontando moduli e argomenti:

$$
r^n=1
\quad\Longrightarrow\quad
r=1,
$$

e

$$
n\theta=2\pi k.
$$

Pertanto

$$
\theta=\frac{2\pi k}{n}.
$$

Le soluzioni distinte si ottengono scegliendo

$$
k=0,1,\dots,n-1.
$$

Quindi le radici $n$-esime dell’unità sono

$$
z_k=e^{2\pi i k/n},
\qquad k=0,1,\dots,n-1.
$$

Geometricamente sono i vertici di un poligono regolare di $n$ lati inscritto nella circonferenza unitaria.

## 17. Esempio: soluzioni di $z^6=1$

Per

$$
z^6=1,
$$

si ha

$$
|z|=1,
\qquad
\arg(z)=\frac{2\pi k}{6}
=\frac{k\pi}{3},
\qquad k=0,1,\dots,5.
$$

Le sei soluzioni sono:

$$
\begin{aligned}
z_0&=e^{0}=1,\\
z_1&=e^{i\pi/3}
=\frac12+i\frac{\sqrt3}{2},\\
z_2&=e^{2i\pi/3}
=-\frac12+i\frac{\sqrt3}{2},\\
z_3&=e^{i\pi}=-1,\\
z_4&=e^{4i\pi/3}
=-\frac12-i\frac{\sqrt3}{2},\\
z_5&=e^{5i\pi/3}
=\frac12-i\frac{\sqrt3}{2}.
\end{aligned}
$$

Questi punti sono i vertici di un esagono regolare sulla circonferenza unitaria.

Poiché il polinomio $z^6-1$ ha coefficienti reali, le radici non reali compaiono in coppie coniugate:

$$
\frac12+i\frac{\sqrt3}{2}
\quad\text{e}\quad
\frac12-i\frac{\sqrt3}{2},
$$

così come

$$
-\frac12+i\frac{\sqrt3}{2}
\quad\text{e}\quad
-\frac12-i\frac{\sqrt3}{2}.
$$

Si può anche ottenere una fattorizzazione algebrica usando la differenza di cubi:

$$
z^6-1=(z^3-1)(z^3+1).
$$

Poi:

$$
z^3-1=(z-1)(z^2+z+1),
$$

e

$$
z^3+1=(z+1)(z^2-z+1).
$$

Quindi

$$
z^6-1
=
(z-1)(z+1)(z^2+z+1)(z^2-z+1).
$$

I due fattori quadratici producono le quattro radici non reali.

Lo stesso esercizio si può quindi affrontare in modi diversi:

- usare la forma polare e la formula generale per le radici $n$-esime;
- fattorizzare algebricamente il polinomio;
- sfruttare la simmetria delle radici e le coppie coniugate.

Va bene qualunque procedimento corretto, purché i passaggi siano giustificati e i teoremi usati nel modo giusto.
