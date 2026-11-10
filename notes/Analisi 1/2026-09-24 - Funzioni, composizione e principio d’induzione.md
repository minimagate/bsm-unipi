---
type: lecture-note
course: Analisi 1
date: '2026-09-24'
title: Funzioni, composizione e principio d’induzione
source_transcript: _transcripts/Analisi 1/2026-09-24 - Funzioni, composizione e principio d’induzione.md
source_hash: sha256:46df7e14e14bf379b34dceae4d7f4844f65cdcb90f65d7c1ceb0baa246c6a7d7
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-24T09:13:47.266Z'
vault_path: Notes/Analisi 1/Lectures/2026-09-24 - Funzioni, composizione e principio d’induzione.md
vault_hash: 5ae7d0637b81a7b29870ce9e43116b1db98bc307373154baad2b8e7925ec791a
---

# Funzioni, composizione e principio d’induzione

## 1. Funzioni tra insiemi

### 1.1 La descrizione operativa

Siano $A$ e $B$ due [[Insieme|insiemi]]. Operativamente, una [[Funzione|funzione]] da $A$ in $B$ è fatta di tre ingredienti:

1. un insieme di partenza $A$;
2. un insieme di arrivo $B$;
3. una legge che a ogni elemento di $A$ associa uno e un solo elemento di $B$.

Si scrive

$$
f\colon A\to B.
$$

Per ogni $a\in A$, la legge associa un unico elemento $b\in B$, che si indica con

$$
b=f(a).
$$

Nota bene: una funzione non è soltanto la formula $f(a)$, ma l’insieme formato da insieme di partenza, insieme di arrivo e legge di associazione.

La condizione fondamentale è:

- da ogni elemento di $A$ deve partire una freccia;
- da ogni elemento di $A$ deve partire una sola freccia;
- la freccia deve arrivare in un elemento di $B$.

Non è invece necessario che ogni elemento di $B$ sia raggiunto da una freccia, né che elementi distinti di $A$ abbiano immagini distinte.

### 1.2 Rappresentazione mediante frecce

Una funzione $f\colon A\to B$ si può rappresentare con un diagramma:

- a sinistra gli elementi di $A$;
- a destra quelli di $B$;
- da ogni elemento di $A$ si traccia una sola freccia verso il corrispondente elemento di $B$.

Più elementi distinti di $A$ possono finire nello stesso elemento di $B$: in questo caso più frecce arrivano nello stesso punto.

Un elemento di $B$ può anche non essere raggiunto da nessuna freccia. Appartiene comunque all’insieme di arrivo $B$, ma non all’immagine della funzione.

### 1.3 Insieme di arrivo e immagine

Bisogna distinguere bene:

- **insieme di arrivo**: l’insieme $B$ dichiarato nella scrittura $f\colon A\to B$;
- **immagine**: l’insieme degli elementi di $B$ che sono effettivamente raggiunti da almeno una freccia.

L’immagine di $f$ è quindi

$$
f(A)=\{f(a)\mid a\in A\}.
$$

L’insieme di arrivo può contenere elementi che non stanno nell’immagine.

Il termine “codominio” a volte si usa come sinonimo di insieme di arrivo, ma può creare confusione con l’immagine. Meglio parlare esplicitamente di insieme di partenza, insieme di arrivo e immagine.

---

## 2. Il grafico di una funzione

Sia $f\colon A\to B$. Il grafico di $f$ vive nel [[Prodotto cartesiano|prodotto cartesiano]] $A\times B$, cioè nell’insieme delle coppie ordinate $(a,b)$ con $a\in A$ e $b\in B$.

Il grafico è

$$
\operatorname{Graf}(f)
=
\{(a,b)\in A\times B\mid b=f(a)\}.
$$

È una definizione “per proprietà”: si considerano tutte le coppie di $A\times B$ e si selezionano quelle che soddisfano la proprietà

$$
b=f(a).
$$

La funzione si può quindi identificare rigorosamente con il suo grafico.

### 2.1 Definizione rigorosa di funzione

Una funzione $f\colon A\to B$ è un sottoinsieme $G$ di $A\times B$ tale che

$$
\forall a\in A\ \exists!\, b\in B
\quad\text{tale che}\quad
(a,b)\in G.
$$

Il simbolo $\exists!$ significa “esiste uno e un solo”.

In altre parole, $G\subseteq A\times B$ è il grafico di una funzione se e solo se:

- per ogni $a\in A$ esiste almeno un $b\in B$ tale che $(a,b)\in G$;
- per ogni $a\in A$ ne esiste al massimo uno.

Quindi, per ogni elemento di partenza, deve esserci esattamente una coppia del grafico con quell’elemento come prima componente.

La formulazione rigorosa evita il termine intuitivo “legge”, che può essere poco preciso: partendo dal concetto di insieme, la funzione viene definita come un particolare sottoinsieme del prodotto cartesiano.

---

## 3. Composizione di funzioni

Siano

$$
f\colon A\to B,
\qquad
g\colon B\to C.
$$

Poiché l’insieme di arrivo di $f$ coincide con l’insieme di partenza di $g$, si può applicare prima $f$ e poi $g$.

La [[Composizione di funzioni|funzione composta]] si indica con

$$
g\circ f\colon A\to C
$$

e si definisce ponendo

$$
(g\circ f)(a)=g(f(a)).
$$

Occhio all’ordine: la funzione applicata per prima è quella più a destra.

Il procedimento è:

$$
a\in A
\overset{f}{\longmapsto}
f(a)\in B
\overset{g}{\longmapsto}
g(f(a))\in C.
$$

Dunque $g\circ f$ significa “prima $f$, poi $g$”.

> [!example] Esempio
> Siano $f,g\colon\mathbb{R}\to\mathbb{R}$ con $f(x)=x+1$ e $g(x)=x^2$. Allora $(g\circ f)(x)=(x+1)^2$, mentre $(f\circ g)(x)=x^2+1$. In generale $g\circ f\neq f\circ g$: l’ordine conta.

### 3.1 Definizione mediante grafici

Supponiamo di identificare $f$ e $g$ con i loro grafici:

$$
F\subseteq A\times B,
\qquad
G\subseteq B\times C.
$$

Il grafico $H$ della composizione $g\circ f$ è un sottoinsieme di $A\times C$ definito da

$$
H
=
\{(a,c)\in A\times C
\mid
\exists b\in B:
(a,b)\in F
\ \text{e}\
(b,c)\in G
\}.
$$

Il significato è questo: la coppia $(a,c)$ appartiene al grafico della composizione se esiste un elemento intermedio $b\in B$ tale che

$$
b=f(a)
\qquad\text{e}\qquad
c=g(b).
$$

Pertanto

$$
c=g(f(a)).
$$

Questa definizione è più rigorosa, ma all’inizio meno intuitiva della descrizione con le frecce.

---

## 4. Iniettività, suriettività e biettività

Iniettività e suriettività dipendono dagli insiemi di partenza e di arrivo. Non ha senso chiedersi se una formula sia “iniettiva” o “suriettiva” senza specificare la funzione completa, cioè da quale insieme a quale insieme si va.

### 4.1 Funzioni iniettive

Una funzione $f\colon A\to B$ è **iniettiva** se elementi distinti di $A$ hanno immagini distinte in $B$:

$$
\forall a_1,a_2\in A,
\qquad
a_1\neq a_2
\Longrightarrow
f(a_1)\neq f(a_2).
$$

In termini di frecce: non esistono due frecce distinte che arrivano nello stesso elemento di $B$.

La formulazione equivalente, ottenuta con la contronominale dell’implicazione, è

$$
\forall a_1,a_2\in A,
\qquad
f(a_1)=f(a_2)
\Longrightarrow
a_1=a_2.
$$

Per dimostrare che una funzione non è iniettiva basta trovare due elementi distinti $a_1\neq a_2$ tali che

$$
f(a_1)=f(a_2).
$$

### 4.2 Funzioni suriettive

Una funzione $f\colon A\to B$ è **suriettiva** se ogni elemento dell’insieme di arrivo è raggiunto da almeno una freccia:

$$
\forall b\in B\ \exists a\in A
\quad\text{tale che}\quad
f(a)=b.
$$

In altre parole,

$$
f(A)=B.
$$

Per dimostrare che una funzione non è suriettiva basta trovare un elemento $b\in B$ che non sia immagine di nessun elemento di $A$.

### 4.3 Funzioni biettive

Una funzione è **[[Funzione biettiva|biettiva]]** se è contemporaneamente iniettiva e suriettiva.

Quindi:

$$
f\text{ biettiva}
\Longleftrightarrow
f\text{ iniettiva e suriettiva}.
$$

In termini di frecce:

- l’iniettività garantisce che non arrivino due frecce nello stesso punto;
- la suriettività garantisce che ogni punto dell’insieme di arrivo sia raggiunto;
- la biettività significa che ogni elemento di $B$ è raggiunto da esattamente una freccia.

---

## 5. Esempio: la funzione $x\mapsto x^2$

Consideriamo la formula

$$
f(x)=x^2.
$$

La risposta alla domanda “è iniettiva o suriettiva?” dipende dagli insiemi di partenza e di arrivo.

### 5.1 $f\colon\mathbb{R}\to\mathbb{R}$

La funzione non è iniettiva perché

$$
f(1)=1=f(-1),
$$

pur essendo $1\neq -1$.

Non è neppure suriettiva, perché nessun numero reale negativo è immagine di un numero reale:

$$
x^2\geq 0
\qquad\forall x\in\mathbb{R}.
$$

Quindi:

$$
f\colon\mathbb{R}\to\mathbb{R}
\quad\text{non è né iniettiva né suriettiva}.
$$

### 5.2 $f\colon\mathbb{R}\to[0,+\infty)$

La funzione resta non iniettiva, per lo stesso motivo, ma diventa suriettiva: ogni $y\geq 0$ è il quadrato di $\sqrt y$.

Quindi è suriettiva ma non iniettiva.

### 5.3 $f\colon[0,+\infty)\to\mathbb{R}$

La funzione è iniettiva, perché su $[0,+\infty)$ non esistono due elementi distinti con lo stesso quadrato.

Non è suriettiva su $\mathbb{R}$, perché non assume valori negativi.

### 5.4 $f\colon[0,+\infty)\to[0,+\infty)$

In questo caso la funzione è sia iniettiva sia suriettiva, dunque biettiva.

Questo esempio mostra che iniettività e suriettività non sono proprietà della sola formula, ma della funzione completa, con i suoi insiemi di partenza e di arrivo.

---

## 6. Funzioni invertibili

Una funzione $f\colon A\to B$ si dice **[[Funzione inversa|invertibile]]** se esiste una funzione

$$
g\colon B\to A
$$

tale che

$$
g(f(a))=a
\qquad\forall a\in A
$$

e

$$
f(g(b))=b
\qquad\forall b\in B.
$$

La funzione $g$ si chiama funzione inversa di $f$ e si indica con

$$
f^{-1}\colon B\to A.
$$

Le due identità si possono scrivere come

$$
f^{-1}\circ f=\operatorname{id}_A,
\qquad
f\circ f^{-1}=\operatorname{id}_B.
$$

La funzione inversa “inverte le frecce” di $f$.

### 6.1 Perché serve la biettività

Una funzione è invertibile se e solo se è biettiva.

#### Mancanza di iniettività

Se due elementi distinti $a_1,a_2\in A$ vengono mandati nello stesso elemento $b\in B$, allora

$$
f(a_1)=f(a_2)=b.
$$

Invertendo le frecce, da $b$ dovrebbero partire due frecce, una verso $a_1$ e una verso $a_2$. Questa non sarebbe una funzione.

Quindi una funzione invertibile deve essere iniettiva.

#### Mancanza di suriettività

Se esiste $b\in B$ non raggiunto da nessuna freccia di $f$, invertendo le frecce non si saprebbe dove mandare $b$. L’inversa non sarebbe definita su tutto $B$.

Perciò una funzione invertibile deve essere suriettiva.

Ne segue la proposizione fondamentale:

$$
f\text{ è invertibile}
\Longleftrightarrow
f\text{ è biettiva}.
$$

L’idea è che, per invertire tutte le frecce, deve esserci esattamente una freccia da ogni elemento di $A$ verso ogni elemento di $B$.

---

## 7. Iniettività, suriettività e composizione

Siano

$$
f\colon A\to B,
\qquad
g\colon B\to C.
$$

La composizione è

$$
g\circ f\colon A\to C.
$$

### 7.1 Composizione di funzioni iniettive

Se $f$ e $g$ sono iniettive, allora $g\circ f$ è iniettiva.

Infatti, siano $a_1,a_2\in A$ tali che $a_1\neq a_2$. Poiché $f$ è iniettiva,

$$
f(a_1)\neq f(a_2).
$$

Poiché anche $g$ è iniettiva,

$$
g(f(a_1))\neq g(f(a_2)).
$$

Pertanto

$$
(g\circ f)(a_1)\neq (g\circ f)(a_2),
$$

e quindi $g\circ f$ è iniettiva.

Come catena logica:

$$
a_1\neq a_2
\Longrightarrow
f(a_1)\neq f(a_2)
\Longrightarrow
g(f(a_1))\neq g(f(a_2)).
$$

### 7.2 Composizione di funzioni suriettive

Se $f$ e $g$ sono suriettive, allora $g\circ f$ è suriettiva.

Sia $c\in C$. Poiché $g$ è suriettiva, esiste $b\in B$ tale che

$$
g(b)=c.
$$

Poiché $f$ è suriettiva, esiste $a\in A$ tale che

$$
f(a)=b.
$$

Allora

$$
(g\circ f)(a)=g(f(a))=g(b)=c.
$$

Quindi ogni $c\in C$ è raggiunto dalla composizione.

### 7.3 Se la composizione è iniettiva

Se $g\circ f$ è iniettiva, allora necessariamente $f$ è iniettiva.

Dimostrazione per assurdo. Supponiamo che $f$ non sia iniettiva. Esistono allora $a_1\neq a_2$ tali che

$$
f(a_1)=f(a_2).
$$

Applicando $g$ a entrambi i membri si ottiene

$$
g(f(a_1))=g(f(a_2)),
$$

cioè

$$
(g\circ f)(a_1)=(g\circ f)(a_2),
$$

in contraddizione con l’iniettività di $g\circ f$.

L’idea intuitiva è:

> ciò che $f$ unisce, $g$ non può separare.

Se due elementi diventano uguali dopo $f$, tutte le applicazioni successive continueranno a dare lo stesso risultato.

### 7.4 Se la composizione è suriettiva

Se $g\circ f$ è suriettiva, allora necessariamente $g$ è suriettiva.

Infatti, se un elemento di $C$ non fosse raggiunto da $g$, non potrebbe essere raggiunto neppure dalla composizione $g\circ f$, che applica $g$ come ultimo passaggio.

Formalmente, dato $c\in C$, dalla suriettività di $g\circ f$ esiste $a\in A$ tale che

$$
(g\circ f)(a)=c.
$$

Ponendo $b=f(a)\in B$, si ha

$$
g(b)=c.
$$

Quindi $g$ è suriettiva.

---

## 8. Immagine e controimmagine

Sia $f\colon A\to B$.

### 8.1 Immagine di un sottoinsieme

Dato un sottoinsieme $E\subseteq A$, l’[[Immagine e controimmagine|immagine]] di $E$ tramite $f$ è

$$
f(E)=\{f(a)\in B\mid a\in E\}.
$$

In forma equivalente:

$$
f(E)=\{b\in B\mid \exists a\in E,\ f(a)=b\}.
$$

L’immagine $f(E)$ è l’insieme degli arrivi di tutte le frecce che partono dagli elementi di $E$.

In particolare, se $E=A$ si ottiene l’immagine della funzione:

$$
f(A)=\{f(a)\mid a\in A\}.
$$

La definizione di $f(E)$ è per elenco: si prendono gli elementi di $E$, si applica la funzione e si raccolgono i risultati.

### 8.2 Controimmagine di un sottoinsieme

Dato un sottoinsieme $D\subseteq B$, la controimmagine di $D$ tramite $f$ è

$$
f^{-1}(D)
=
\{a\in A\mid f(a)\in D\}.
$$

Qui $f^{-1}(D)$ non indica necessariamente la funzione inversa: è la controimmagine di $D$, e la definizione ha senso anche quando $f$ non è invertibile.

La controimmagine è l’insieme delle partenze delle frecce che arrivano in $D$.

In termini di proprietà, si selezionano tutti gli $a\in A$ la cui immagine $f(a)$ appartiene a $D$.

> [!example] Esempio
> Sia $f\colon\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$. Allora $f([-1,2])=[0,4]$ (il quadrato di $-1$ è $1$, ma il valore più piccolo è $0$, raggiunto in $x=0$). La controimmagine di $\{4\}$ è $f^{-1}(\{4\})=\{-2,2\}$, mentre $f^{-1}(\{-1\})=\varnothing$, perché nessun quadrato è negativo.

---

## 9. Il principio d’induzione

### 9.1 Predicati con una variabile naturale

Sia $P(n)$ un predicato che dipende da $n\in\mathbb{N}$.

Un predicato è una frase che, al variare di $n$, può risultare vera o falsa.

Il [[Principio di induzione|principio d’induzione]] permette di dimostrare che $P(n)$ è vera per ogni $n\in\mathbb{N}$ verificando due condizioni:

1. **passo base**:
   $$
   P(0)\text{ è vera};
   $$

2. **passo induttivo**:
   $$
   \forall n\in\mathbb{N},
   \quad
   P(n)\Longrightarrow P(n+1).
   $$

Se entrambe le condizioni sono soddisfatte, allora

$$
\forall n\in\mathbb{N},\quad P(n)\text{ è vera}.
$$

Nel passo induttivo si assume vera $P(n)$: è l’**ipotesi induttiva**. Sotto questa ipotesi si dimostra $P(n+1)$, che è la **tesi induttiva**.

#### 9.2 Interpretazione intuitiva: le tessere del domino

Si possono immaginare le proposizioni

$$
P(0),P(1),P(2),P(3),\ldots
$$

come tessere del domino.

- Il passo base $P(0)$ garantisce che la prima tessera cada.
- Il passo induttivo garantisce che, se cade la tessera $n$, cade anche la tessera $n+1$.

Quindi:

$$
P(0)\Rightarrow P(1)\Rightarrow P(2)\Rightarrow P(3)\Rightarrow\cdots
$$

L’argomento intuitivo spiega il meccanismo, ma una dimostrazione rigorosa deve esplicitare passo base e passo induttivo.

---

### 10. Somma dei quadrati

La formula da dimostrare è

$$
\sum_{k=0}^{n} k^2
=
\frac{n(n+1)(2n+1)}{6}.
$$

Il simbolo di sommatoria significa

$$
\sum_{k=0}^{n} k^2
=
0^2+1^2+2^2+\cdots+n^2.
$$

#### 10.1 Passo base

Per $n=0$:

$$
\sum_{k=0}^{0} k^2=0^2=0,
$$

mentre

$$
\frac{0(0+1)(2\cdot 0+1)}{6}=0.
$$

Quindi $P(0)$ è vera.

Come ulteriore controllo, per $n=1$:

$$
0^2+1^2=1
$$

e

$$
\frac{1\cdot 2\cdot 3}{6}=1.
$$

#### 10.2 Passo induttivo

Supponiamo vera l’ipotesi induttiva

$$
\sum_{k=0}^{n} k^2
=
\frac{n(n+1)(2n+1)}{6}.
$$

Dobbiamo dimostrare

$$
\sum_{k=0}^{n+1} k^2
=
\frac{(n+1)(n+2)(2n+3)}{6}.
$$

Si parte dal membro sinistro della tesi e si separa l’ultimo termine:

$$
\begin{aligned}
\sum_{k=0}^{n+1} k^2
&=
\sum_{k=0}^{n} k^2+(n+1)^2\\
&=
\frac{n(n+1)(2n+1)}{6}+(n+1)^2\\
&=
\frac{n(n+1)(2n+1)+6(n+1)^2}{6}\\
&=
\frac{(n+1)\left(n(2n+1)+6(n+1)\right)}{6}\\
&=
\frac{(n+1)(2n^2+7n+6)}{6}\\
&=
\frac{(n+1)(n+2)(2n+3)}{6}.
\end{aligned}
$$

L’ultima uguaglianza segue da

$$
(n+2)(2n+3)=2n^2+7n+6.
$$

La dimostrazione usa una **catena di uguaglianze**: ogni espressione è uguale alla successiva, quindi la prima è uguale all’ultima.

L’induzione permette di verificare la formula senza dover scoprire, durante la dimostrazione, perché abbia proprio quella forma. L’intuizione può suggerire la formula guardando i primi casi; l’induzione ne dimostra poi la validità in generale.

---

### 11. Somma geometrica finita

Per $a\neq 1$ si vuole dimostrare la formula

$$
\sum_{k=0}^{n} a^k
=
\frac{a^{n+1}-1}{a-1}.
$$

Scritta esplicitamente:

$$
1+a+a^2+\cdots+a^n
=
\frac{a^{n+1}-1}{a-1}.
$$

#### 11.1 Passo base

Per $n=0$:

$$
\sum_{k=0}^{0}a^k=a^0=1,
$$

mentre

$$
\frac{a^{0+1}-1}{a-1}
=
\frac{a-1}{a-1}
=1,
$$

purché $a\neq 1$.

#### 11.2 Passo induttivo

Ipotesi induttiva:

$$
\sum_{k=0}^{n}a^k
=
\frac{a^{n+1}-1}{a-1}.
$$

Tesi:

$$
\sum_{k=0}^{n+1}a^k
=
\frac{a^{n+2}-1}{a-1}.
$$

Si separa l’ultimo termine:

$$
\begin{aligned}
\sum_{k=0}^{n+1}a^k
&=
\sum_{k=0}^{n}a^k+a^{n+1}\\
&=
\frac{a^{n+1}-1}{a-1}+a^{n+1}\\
&=
\frac{a^{n+1}-1+(a-1)a^{n+1}}{a-1}\\
&=
\frac{a^{n+2}-1}{a-1}.
\end{aligned}
$$

Anche qui il passaggio chiave è isolare l’ultimo termine per poter usare l’ipotesi induttiva.

#### 11.3 Attenzione al caso $a=1$

La formula contiene il denominatore $a-1$, quindi richiede

$$
a\neq 1.
$$

Se invece $a=1$, la somma diventa

$$
\sum_{k=0}^{n}1^k
=
\underbrace{1+1+\cdots+1}_{n+1\text{ termini}}
=
n+1.
$$

I termini sono $n+1$, non $n$: gli indici vanno da $0$ a $n$ inclusi.

È un tipico caso in cui un denominatore che può annullarsi deve far scattare subito un controllo.

---

### 12. Disuguaglianza di Bernoulli

La [[Disuguaglianza di Bernoulli|disuguaglianza di Bernoulli]] afferma che

$$
(1+x)^n\geq 1+nx
$$

per ogni $n\in\mathbb{N}$ e per ogni $x\geq -1$.

Il caso $x=-1$ è ammesso, anche se nella dimostrazione si può inizialmente lavorare con $x>-1$ per evitare alcune complicazioni sul segno.

#### 12.1 Organizzazione del predicato

La proposizione contiene due parametri, $n$ e $x$. Per applicare l’induzione su $n$ si fissa o si quantifica prima $x$ e si considera il predicato

$$
P(n):\quad
\forall x\geq -1,\quad
(1+x)^n\geq 1+nx.
$$

A quel punto l’unico parametro libero è $n$.

#### 12.2 Passo base

Per $n=0$:

$$
(1+x)^0=1
$$

e quindi

$$
(1+x)^0=1\geq 1=1+0x.
$$

Il passo base è verificato.

#### 12.3 Passo induttivo

Ipotesi induttiva:

$$
(1+x)^n\geq 1+nx
\qquad\text{per ogni }x\geq -1.
$$

Tesi:

$$
(1+x)^{n+1}\geq 1+(n+1)x.
$$

Si parte dal membro sinistro:

$$
\begin{aligned}
(1+x)^{n+1}
&=(1+x)^n(1+x)\\
&\geq (1+nx)(1+x)\\
&=1+x+nx+nx^2\\
&=1+(n+1)x+nx^2\\
&\geq 1+(n+1)x.
\end{aligned}
$$

L’ultimo passaggio usa

$$
n\geq 0,
\qquad
x^2\geq 0,
$$

da cui

$$
nx^2\geq 0.
$$

#### 12.4 Dove si usa l’ipotesi $x\geq -1$

L’ipotesi $x\geq -1$ equivale a

$$
1+x\geq 0.
$$

Viene usata nel passaggio

$$
(1+x)^n\geq 1+nx
\Longrightarrow
(1+x)^n(1+x)\geq (1+nx)(1+x).
$$

Una disuguaglianza si può moltiplicare per una quantità non negativa senza cambiare verso. Se invece si moltiplicasse per una quantità negativa il verso si invertirebbe e la catena non sarebbe più valida.

Nel caso $x=-1$ il fattore $1+x$ è nullo e la dimostrazione continua a funzionare. Infatti:

$$
(1-1)^n=0^n
$$

e, per $n\geq 1$,

$$
0\geq 1-n,
$$

che è vero.

---

### 13. Un’induzione a partire da un indice diverso da zero

Vediamo per quali $n$ vale

$$
n!\geq 2^n.
$$

Ricordiamo che

$$
n!=1\cdot 2\cdot 3\cdots n,
\qquad
0!=1.
$$

#### 13.1 Esplorazione dei primi casi

Si calcolano i primi valori:

- per $n=0$:
  $$
  0!=1\geq 1=2^0;
  $$

- per $n=1$:
  $$
  1!=1\not\geq 2;
  $$

- per $n=2$:
  $$
  2!=2\not\geq 4;
  $$

- per $n=3$:
  $$
  3!=6\not\geq 8;
  $$

- per $n=4$:
  $$
  4!=24\not\geq 16;
  $$

- per $n=5$:
  $$
  5!=120\geq 32.
  $$

Il primo valore da cui la disuguaglianza sembra essere vera è $n=4$. La proposizione corretta è quindi:

$$
n!\geq 2^n
\qquad\text{per }n=0\text{ oppure per ogni }n\geq 4.
$$

L’induzione si applica separatamente:

- il caso $n=0$ si verifica direttamente;
- per dimostrare la validità per ogni $n\geq 4$ si parte dal passo base $n=4$.

#### 13.2 Passo base per $n=4$

$$
4!=24\geq 16=2^4.
$$

#### 13.3 Passo induttivo

Ipotesi induttiva, per $n\geq 4$:

$$
n!\geq 2^n.
$$

Tesi:

$$
(n+1)!\geq 2^{n+1}.
$$

Si procede così:

$$
\begin{aligned}
(n+1)!
&=(n+1)n!\\
&\geq (n+1)2^n\\
&\geq 2\cdot 2^n\\
&=2^{n+1}.
\end{aligned}
$$

Il secondo passaggio usa l’ipotesi induttiva moltiplicata per $n+1$. Il verso si conserva perché

$$
n+1>0.
$$

Poi si usa $n+1\geq 2$, certamente vero per $n\geq 1$.

Quindi la proprietà vale per ogni $n\geq 4$.

#### 13.4 Il meccanismo di caduta non deve necessariamente partire da zero

In questo esempio:

- $P(0)$ è vera, ma $P(1),P(2),P(3)$ sono false;
- il meccanismo induttivo vale da $n\geq 1$;
- la prima tessera utile che cade è $P(4)$;
- da $P(4)$ si ottengono $P(5),P(6),\ldots$.

Le tessere $1,2,3$ sono come incollate: anche se esiste il meccanismo generale per passare da $n$ a $n+1$, quelle proposizioni non sono vere. L’induzione deve quindi partire da $4$.

---

### 14. Dimostrare un enunciato più forte

Consideriamo la somma

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}
=
\frac{1}{1\cdot 2}
+\frac{1}{2\cdot 3}
+\frac{1}{3\cdot 4}
+\cdots
+\frac{1}{n(n+1)}.
$$

Un primo tentativo potrebbe essere dimostrare direttamente che

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}\leq 1.
$$

Questo enunciato però è scomodo per induzione: aggiungendo un termine positivo a una quantità minore o uguale a $1$ non si ottiene automaticamente una quantità ancora minore o uguale a $1$.

Infatti, dall’ipotesi

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}\leq 1
$$

si otterrebbe soltanto

$$
\sum_{k=1}^{n+1}\frac{1}{k(k+1)}
\leq
1+\frac{1}{(n+1)(n+2)},
$$

che non basta per concludere che la somma sia minore o uguale a $1$.

#### 14.1 Un enunciato più forte

Calcolando i primi casi:

$$
\begin{aligned}
n=1&:\quad \frac12,\\
n=2&:\quad \frac12+\frac16=\frac23,\\
n=3&:\quad \frac12+\frac16+\frac1{12}=\frac34,\\
n=4&:\quad \frac45.
\end{aligned}
$$

Si riconosce la formula

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}
=
\frac{n}{n+1}.
$$

Questa formula è più forte della disuguaglianza desiderata, perché

$$
\frac{n}{n+1}\leq 1.
$$

Dimostrare l’uguaglianza implica quindi dimostrare anche la disuguaglianza.

La strategia generale è:

> può essere più facile dimostrare un enunciato più forte di quello richiesto.

Un enunciato più forte sembra, in linea di principio, più difficile, ma può avere una forma più adatta all’induzione.

#### 14.2 Dimostrazione della formula

La formula è

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}
=
\frac{n}{n+1}.
$$

Per $n=1$:

$$
\sum_{k=1}^{1}\frac{1}{k(k+1)}
=
\frac12
=
\frac{1}{2}.
$$

Supponiamo ora che

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}
=
\frac{n}{n+1}.
$$

Allora

$$
\begin{aligned}
\sum_{k=1}^{n+1}\frac{1}{k(k+1)}
&=
\sum_{k=1}^{n}\frac{1}{k(k+1)}
+\frac{1}{(n+1)(n+2)}\\
&=
\frac{n}{n+1}
+\frac{1}{(n+1)(n+2)}\\
&=
\frac{n(n+2)+1}{(n+1)(n+2)}\\
&=
\frac{n^2+2n+1}{(n+1)(n+2)}\\
&=
\frac{(n+1)^2}{(n+1)(n+2)}.
\end{aligned}
$$

Nota bene: l’ultima espressione non è ancora nella forma $\frac{n+1}{n+2}$; serve un ultimo passaggio, cioè semplificare il fattore $n+1$ (che è diverso da zero):

$$
\frac{n}{n+1}
+\frac{1}{(n+1)(n+2)}
=
\frac{n(n+2)+1}{(n+1)(n+2)}
=
\frac{n^2+2n+1}{(n+1)(n+2)}
=
\frac{(n+1)^2}{(n+1)(n+2)}
=
\frac{n+1}{n+2}.
$$

Quindi si ottiene proprio

$$
\sum_{k=1}^{n+1}\frac{1}{k(k+1)}
=
\frac{n+1}{n+2}.
$$

Pertanto la formula vale per ogni $n\geq 1$, e in particolare

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}
=
\frac{n}{n+1}
\leq 1.
$$

L’idea di cercare un enunciato più forte è uno dei passaggi in cui la dimostrazione richiede creatività: non basta applicare meccanicamente lo schema “passo base, ipotesi, tesi”; a volte bisogna modificare l’enunciato in una forma che renda possibile il passo induttivo.
