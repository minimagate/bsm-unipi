---
type: lecture-note
course: Aritmetica
date: '2026-10-05'
title: Divisione euclidea, massimo comun divisore e identità di Bézout
source_transcript: _transcripts/Aritmetica/2026-10-05 - Divisione euclidea, massimo comun divisore e identità
  di Bézout.md
source_hash: sha256:28c0aa73c00135ac5102eb318ec64f56061f5cf6299b0c70cd77edc926fa9374
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-05T14:38:58.042Z'
vault_path: Notes/Aritmetica/Lectures/2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout.md
vault_hash: 2dccb27e23ca84292ca43ac2722141e438b7b254ff67559f4652e5a3ed07ca09
---

## 1. Approssimazione mediante multipli

Dividere un intero $a$ per un intero non nullo $b$ vuol dire approssimare $a$ con un multiplo di $b$:

$$
a \approx qb.
$$

La differenza tra $a$ e il multiplo scelto è il **resto**:

$$
r=a-qb.
$$

Per avere una [[Divisione euclidea|divisione euclidea]] ben definita non basta scrivere un’uguaglianza qualsiasi di questo tipo: servono condizioni che rendano il resto piccolo e, soprattutto, che garantiscano l’unicità della rappresentazione.

La condizione standard è

$$
0\le r<|b|.
$$

Quando $b>0$ diventa semplicemente

$$
0\le r<b.
$$

Compare il [[Valore assoluto|valore assoluto]] perché la grandezza del divisore va sempre intesa come quantità positiva. Se il divisore è negativo, per esempio, il resto deve comunque essere non negativo e minore della sua grandezza.

---

## 2. Teorema della divisione euclidea

### Enunciato

Siano $a,b\in\mathbb Z$ con $b\neq 0$. Allora esistono, e sono unici, due interi $q,r\in\mathbb Z$ tali che

$$
a=qb+r
$$

e

$$
0\le r<|b|.
$$

L’intero $q$ si chiama **quoziente**, e $r$ si chiama **resto** della divisione euclidea di $a$ per $b$.

Il teorema contiene due affermazioni distinte:

1. **esistenza**: almeno una coppia $(q,r)$ soddisfa le condizioni;
2. **unicità**: non possono esistere due coppie diverse che le soddisfino entrambe.

---

## 3. Dimostrazione dell’esistenza

### 3.1. Caso $b>0$

Consideriamo l’insieme degli interi non negativi che si ottengono sottraendo ad $a$ dei multipli di $b$:

$$
S=\{a-qb\mid q\in\mathbb Z,\ a-qb\ge 0\}.
$$

Prima di tutto bisogna verificare che $S$ non sia vuoto.

- Se $a\ge 0$, con $q=0$ si ottiene $a\in S$.
- Se $a<0$, scegliendo un intero $q$ abbastanza negativo, il numero $a-qb$ diventa non negativo.

Quindi $S\subseteq\mathbb N$ ed è non vuoto. Per il [[Principio del minimo|principio del buon ordinamento]], $S$ ha un minimo. Chiamiamolo $r$:

$$
r=a-q_0b,
$$

per un certo $q_0\in\mathbb Z$. Per costruzione,

$$
r\ge 0.
$$

Resta da dimostrare che $r<b$.

Supponiamo per assurdo che $r\ge b$. Allora

$$
r-b\ge 0.
$$

Inoltre,

$$
r-b=(a-q_0b)-b=a-(q_0+1)b.
$$

Quindi $r-b\in S$. Ma $r-b<r$, in contraddizione con la scelta di $r$ come minimo di $S$.

Dunque necessariamente

$$
0\le r<b.
$$

Infine, da $r=a-q_0b$ si ricava

$$
a=q_0b+r.
$$

Con $q=q_0$ abbiamo la divisione euclidea.

---

### 3.2. Caso generale $b\neq 0$

Se $b<0$, applichiamo il caso precedente al numero positivo $|b|$. Esistono allora $q'\in\mathbb Z$ e $r\in\mathbb Z$ tali che

$$
a=q'|b|+r,
\qquad
0\le r<|b|.
$$

Siccome $|b|=-b$, si ha

$$
a=q'(-b)+r=(-q')b+r.
$$

Con $q=-q'$ otteniamo

$$
a=qb+r,
\qquad
0\le r<|b|.
$$

Quindi l’esistenza vale per ogni $b\neq 0$.

---

## 4. Dimostrazione dell’unicità

Supponiamo che lo stesso intero $a$ abbia due rappresentazioni euclidee:

$$
a=q_1b+r_1
$$

e

$$
a=q_2b+r_2,
$$

con

$$
0\le r_1<|b|,
\qquad
0\le r_2<|b|.
$$

Sottraendo le due uguaglianze:

$$
q_1b+r_1=q_2b+r_2,
$$

quindi

$$
(q_1-q_2)b=r_2-r_1.
$$

Il membro sinistro è un multiplo di $b$. Perciò, se $q_1\neq q_2$, allora

$$
|r_2-r_1|\ge |b|.
$$

D’altra parte, siccome entrambi i resti stanno nell’intervallo $[0,|b|)$,

$$
|r_2-r_1|<|b|.
$$

È una contraddizione. Dunque

$$
q_1=q_2.
$$

Sostituendo nell’uguaglianza iniziale segue anche

$$
r_1=r_2.
$$

Quindi quoziente e resto sono unici.

> [!warning]
> Non basta scrivere $a=qb+r$. Senza la condizione $0\le r<|b|$ la rappresentazione non è unica: si può sempre sostituire $q$ con $q+1$ e $r$ con $r-b$.

> [!example] Esempio
> Per $a=-17$ e $b=5$: $-17=(-4)\cdot 5+3$ con $0\le 3<5$, quindi $q=-4$ e $r=3$. Anche $-17=(-3)\cdot 5-2$ è un’uguaglianza vera, ma il resto $-2$ è negativo, e non va bene.

---

## 5. Divisibilità

### Definizione

Siano $a,b\in\mathbb Z$. Si dice che $a$ **divide** $b$, e si scrive

$$
a\mid b,
$$

se esiste un intero $k\in\mathbb Z$ tale che

$$
b=ka.
$$

In questo caso $a$ è un **divisore** di $b$, e $b$ è un **multiplo** di $a$. Questa è la [[Divisibilità|divisibilità]].

Attenzione al verso della relazione:

$$
a\mid b
\quad\Longleftrightarrow\quad
b=ka.
$$

Per esempio,

$$
2\mid 6
$$

perché $6=3\cdot 2$, mentre

$$
6\nmid 2.
$$

In generale, $a\mid b$ non implica $b\mid a$.

### Proprietà fondamentali

La relazione di divisibilità sugli interi è:

- **riflessiva**:

  $$
  a\mid a,
  $$

  perché $a=1\cdot a$;

- **transitiva**: se $a\mid b$ e $b\mid c$, allora $a\mid c$;

- **non simmetrica** in generale;

- **antisimmetrica sugli interi non negativi**: se $a,b\in\mathbb N$ e $a\mid b$ e $b\mid a$, allora $a=b$.

La transitività si dimostra direttamente. Se

$$
b=k_1a
\qquad\text{e}\qquad
c=k_2b,
$$

allora

$$
c=k_2b=k_2(k_1a)=(k_1k_2)a,
$$

quindi $a\mid c$.

Su $\mathbb N$, la divisibilità è dunque un esempio di relazione d’ordine parziale.

---

## 6. Relazioni e ordine

Una relazione $\mathcal R$ su un insieme $X$ è un insieme di coppie ordinate $(x,y)$ con $x,y\in X$. Si scrive

$$
x\mathcal R y
$$

quando la coppia $(x,y)$ appartiene alla relazione.

Le proprietà principali sono:

- **riflessività**:

  $$
  \forall x\in X,\quad x\mathcal R x;
  $$

- **simmetria**:

  $$
  x\mathcal R y\Longrightarrow y\mathcal R x;
  $$

- **antisimmetria**:

  $$
  x\mathcal R y\ \text{e}\ y\mathcal R x
  \Longrightarrow x=y;
  $$

- **transitività**:

  $$
  x\mathcal R y\ \text{e}\ y\mathcal R z
  \Longrightarrow x\mathcal R z.
  $$

Una relazione d’ordine parziale è riflessiva, antisimmetrica e transitiva. Se in più ogni coppia di elementi è confrontabile, si parla di **ordine totale**.

La relazione $\ge$ sui numeri reali è un ordine totale. Geometricamente, la relazione

$$
a\ge b
$$

corrisponde ai punti del piano che stanno sulla retta o nel semipiano appropriato rispetto alla retta $y=x$.

La divisibilità, invece, non è un ordine totale: tra $2$ e $3$, per esempio, nessuno dei due divide l’altro.

---

## 7. Massimo comun divisore

### Definizione

Siano $a,b\in\mathbb Z$, non entrambi nulli. Un intero positivo $d$ si dice **divisore comune** di $a$ e $b$ se

$$
d\mid a
\qquad\text{e}\qquad
d\mid b.
$$

Il **[[Massimo comun divisore|massimo comun divisore]]** di $a$ e $b$, indicato con

$$
\gcd(a,b)
$$

oppure con

$$
\operatorname{MCD}(a,b),
$$

è il massimo tra i divisori comuni positivi di $a$ e $b$.

Equivalentemente, $\gcd(a,b)$ è l’unico intero positivo $d$ tale che:

1. $d\mid a$ e $d\mid b$;
2. ogni divisore comune positivo di $a$ e $b$ divide $d$.

La seconda formulazione è spesso più utile di “il massimo tra i divisori comuni”, perché si generalizza meglio e mette in luce la proprietà caratteristica del MCD.

Siccome $1$ divide ogni intero, l’insieme dei divisori comuni positivi non è vuoto. È anche finito quando $a$ e $b$ non sono entrambi nulli. Quindi il massimo comun divisore esiste.

Per convenzione lo si prende sempre positivo:

$$
\gcd(a,b)>0.
$$

In particolare,

$$
\gcd(a,b)=\gcd(|a|,|b|).
$$

---

## 8. Proprietà del massimo comun divisore

Se $d=\gcd(a,b)$, allora:

$$
d\mid a,
\qquad
d\mid b.
$$

Inoltre, se $c$ è un divisore comune di $a$ e $b$, allora

$$
c\mid d.
$$

Il massimo comun divisore è unico. Infatti, se $d$ e $d'$ fossero due massimi comuni divisori positivi, ciascuno sarebbe un divisore comune e quindi

$$
d\mid d'
\qquad\text{e}\qquad
d'\mid d.
$$

Essendo entrambi positivi, questo implica

$$
d=d'.
$$

La positività è importante: se ammettessimo anche divisori negativi, ogni divisore avrebbe il suo opposto e non ci sarebbe un massimo rispetto all’ordine usuale degli interi.

---

## 9. Algoritmo di Euclide

Il teorema della divisione euclidea permette di calcolare il MCD in modo efficiente, con l’[[Algoritmo di Euclide|algoritmo di Euclide]].

Per semplicità, supponiamo $a\ge b>0$. Si eseguono divisioni successive:

$$
\begin{aligned}
a &= q_1b+r_1, &&0\le r_1<b,\\
b &= q_2r_1+r_2, &&0\le r_2<r_1,\\
r_1 &= q_3r_2+r_3, &&0\le r_3<r_2,\\
&\ \vdots\\
r_{n-2} &= q_nr_{n-1}+r_n, &&0\le r_n<r_{n-1},\\
r_{n-1} &= q_{n+1}r_n+0.
\end{aligned}
$$

I resti positivi formano una successione strettamente decrescente:

$$
b>r_1>r_2>\cdots>r_n>0.
$$

Non esiste una successione infinita strettamente decrescente di naturali positivi, quindi il procedimento termina.

L’ultimo resto non nullo è il massimo comun divisore:

$$
\gcd(a,b)=r_n.
$$

### Perché l’algoritmo funziona

Dalla prima divisione,

$$
a=q_1b+r_1.
$$

Un intero divide sia $a$ sia $b$ se e solo se divide sia $b$ sia $r_1$. Infatti:

- se $d\mid a$ e $d\mid b$, allora

  $$
  d\mid(a-q_1b)=r_1;
  $$

- se $d\mid b$ e $d\mid r_1$, allora

  $$
  d\mid(q_1b+r_1)=a.
  $$

Quindi

$$
\gcd(a,b)=\gcd(b,r_1).
$$

Ripetendo il ragionamento a ogni passaggio:

$$
\gcd(a,b)
=\gcd(b,r_1)
=\gcd(r_1,r_2)
=\cdots
=\gcd(r_{n-1},r_n).
$$

Nell’ultima divisione,

$$
r_{n-1}=q_{n+1}r_n,
$$

quindi $r_n\mid r_{n-1}$ e

$$
\gcd(r_{n-1},r_n)=r_n.
$$

Ne segue che l’ultimo resto non nullo è proprio $\gcd(a,b)$.

---

## 10. Esempio di algoritmo di Euclide

Prendiamo $45$ e $17$:

$$
\begin{aligned}
45&=2\cdot17+11,\\
17&=1\cdot11+6,\\
11&=1\cdot6+5,\\
6&=1\cdot5+1,\\
5&=5\cdot1+0.
\end{aligned}
$$

L’ultimo resto non nullo è $1$, quindi

$$
\gcd(45,17)=1.
$$

Questo significa che $45$ e $17$ sono [[Numeri coprimi|coprimi]].

---

## 11. Identità di Bézout

### Enunciato

Per ogni $a,b\in\mathbb Z$, non entrambi nulli, esistono $u,v\in\mathbb Z$ tali che

$$
\gcd(a,b)=ua+vb.
$$

Questa uguaglianza si chiama **[[Identità di Bézout|identità di Bézout]]**.

Il teorema dice quindi che il MCD non è solo un divisore comune: si ottiene anche come combinazione lineare intera dei due numeri.

Nell’esempio precedente, siccome $\gcd(45,17)=1$, esistono $u,v\in\mathbb Z$ tali che

$$
1=45u+17v.
$$

---

## 12. Dimostrazione mediante l’algoritmo di Euclide

Ogni resto dell’algoritmo di Euclide è una combinazione lineare dei due numeri iniziali.

Infatti, dal primo passaggio:

$$
r_1=a-q_1b,
$$

quindi $r_1$ è combinazione lineare di $a$ e $b$.

Dal secondo passaggio:

$$
r_2=b-q_2r_1.
$$

Siccome $r_1$ è già combinazione lineare di $a$ e $b$, lo è anche $r_2$. Andando avanti allo stesso modo, ogni resto è una combinazione lineare di $a$ e $b$.

In particolare, l’ultimo resto non nullo, che coincide con $\gcd(a,b)$, è una combinazione lineare di $a$ e $b$.

---

## 13. Risalita all’indietro: esempio

Riprendiamo le uguaglianze:

$$
\begin{aligned}
45&=2\cdot17+11,\\
17&=11+6,\\
11&=6+5,\\
6&=5+1.
\end{aligned}
$$

Si parte dall’ultima uguaglianza e si esprime ogni resto in funzione dei precedenti:

$$
1=6-5.
$$

Dalla riga precedente,

$$
5=11-6,
$$

quindi

$$
1=6-(11-6)=2\cdot6-11.
$$

Dalla seconda riga,

$$
6=17-11,
$$

perciò

$$
1=2(17-11)-11=2\cdot17-3\cdot11.
$$

Infine, dalla prima riga,

$$
11=45-2\cdot17.
$$

Sostituendo:

$$
\begin{aligned}
1
&=2\cdot17-3(45-2\cdot17)\\
&=2\cdot17-3\cdot45+6\cdot17\\
&=8\cdot17-3\cdot45.
\end{aligned}
$$

Dunque un’identità di Bézout è

$$
1=(-3)\cdot45+8\cdot17.
$$

L’ordine dei termini non conta; equivalentemente,

$$
1=8\cdot17-3\cdot45.
$$

---

## 14. Conseguenze dell’identità di Bézout

Se

$$
d=\gcd(a,b),
$$

l’identità di Bézout garantisce l’esistenza di $u,v\in\mathbb Z$ tali che

$$
d=ua+vb.
$$

In particolare, se $\gcd(a,b)=1$, allora

$$
ua+vb=1
$$

per opportuni interi $u,v$.

Questa proprietà caratterizza i numeri coprimi:

$$
\gcd(a,b)=1
\quad\Longleftrightarrow\quad
\exists\,u,v\in\mathbb Z:\ ua+vb=1.
$$

L’identità di Bézout serve anche per risolvere le [[Equazione diofantea lineare|equazioni diofantee lineari]] del tipo

$$
ax+by=c.
$$

Una condizione necessaria perché abbia soluzioni intere è

$$
\gcd(a,b)\mid c.
$$

La necessità segue dal fatto che $\gcd(a,b)$ divide ogni combinazione lineare intera di $a$ e $b$.

---

## 15. Osservazioni metodologiche

Durante la dimostrazione è importante distinguere chiaramente:

- ciò che si vuole dimostrare;
- le ipotesi disponibili;
- l’esistenza di un oggetto;
- l’unicità dell’oggetto;
- la proprietà che caratterizza l’oggetto.

Per esempio, nella divisione euclidea:

- l’esistenza si dimostra con il principio del buon ordinamento dei naturali;
- l’unicità si dimostra confrontando due possibili divisioni;
- la condizione $0\le r<|b|$ è essenziale per entrambe.

Allo stesso modo, per il MCD non basta osservare che esiste un divisore comune: bisogna dimostrare che esiste un massimo e che è unico. L’algoritmo di Euclide dà poi un metodo concreto per trovarlo, mentre la risalita all’indietro fornisce esplicitamente i coefficienti dell’identità di Bézout.

> [!warning]
> Errori frequenti:
>
> - confondere $a\mid b$ con $b\mid a$;
> - dimenticare che il divisore nella divisione euclidea deve essere non nullo;
> - usare la condizione $0\le r<b$ quando $b$ è negativo, invece di $0\le r<|b|$;
> - chiamare “massimo comun divisore” un qualunque divisore comune;
> - fermarsi al primo resto senza verificare che sia l’ultimo resto non nullo;
> - nella risalita di Bézout, sostituire un resto con l’espressione sbagliata della riga precedente.

## 16. Schema complessivo

La struttura logica dei risultati è:

$$
\text{divisione euclidea}
\Longrightarrow
\text{resti successivi}
\Longrightarrow
\text{algoritmo di Euclide}
\Longrightarrow
\gcd(a,b)
\Longrightarrow
\text{identità di Bézout}.
$$

La divisione euclidea garantisce che a ogni passo il resto diminuisca strettamente, e questo assicura la terminazione dell’algoritmo. L’invarianza dei divisori comuni lungo i passaggi mostra che l’ultimo resto non nullo è il MCD. Infine, poiché ogni resto è combinazione lineare dei numeri iniziali, anche il MCD ammette una rappresentazione del tipo

$$
\gcd(a,b)=ua+vb.
$$
