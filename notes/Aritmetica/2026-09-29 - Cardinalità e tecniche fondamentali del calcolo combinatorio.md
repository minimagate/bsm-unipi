---
type: lecture-note
course: Aritmetica
date: '2026-09-29'
title: Cardinalità e tecniche fondamentali del calcolo combinatorio
source_transcript: _transcripts/Aritmetica/2026-09-29 - Cardinalità e tecniche fondamentali del calcolo
  combinatorio.md
source_hash: sha256:3a1a9b90f978be42eca4f10664786c7c66fea21c2fd6366a213efbe68b857999
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-29T10:52:19.306Z'
vault_path: Notes/Aritmetica/Lectures/2026-09-29 - Cardinalità e tecniche fondamentali del calcolo combinatorio.md
vault_hash: 1de786ec65e72d9ec140b41b85d931fc56f6beed8f255a9514efe5c79ca92d3d
---

## 1. Dimostrazioni per induzione e calcolo di somme

Conviene distinguere due cose:

- **dimostrare per induzione** una formula già proposta;
- **calcolare** una somma, cioè trovarne una forma chiusa.

Il [[Principio di induzione|principio di induzione]] permette di dimostrare che un enunciato $P(n)$ è vero per ogni $n\geq 1$, ma non ci dà la formula da dimostrare. Se la formula non è nota, bisogna prima trovarla con un altro ragionamento.

### Esempio: somma dei numeri dispari

Vogliamo dimostrare che, per ogni $n\geq 1$,

$$
\sum_{i=0}^{n-1}(2i+1)=n^2.
$$

L’enunciato $P(n)$ è quindi:

$$
P(n):\qquad \sum_{i=0}^{n-1}(2i+1)=n^2.
$$

### Passo base

Per $n=1$:

$$
\sum_{i=0}^{1-1}(2i+1)
=
\sum_{i=0}^{0}(2i+1)
=
2\cdot 0+1
=
1
=
1^2.
$$

Quindi $P(1)$ è vera.

### Passo induttivo

Supponiamo vera $P(n)$, cioè l’ipotesi induttiva

$$
\sum_{i=0}^{n-1}(2i+1)=n^2.
$$

Dobbiamo dimostrare $P(n+1)$:

$$
\sum_{i=0}^{n}(2i+1)=(n+1)^2.
$$

Separiamo l’ultimo addendo:

$$
\sum_{i=0}^{n}(2i+1)
=
\sum_{i=0}^{n-1}(2i+1)+(2n+1).
$$

Con l’ipotesi induttiva:

$$
\sum_{i=0}^{n}(2i+1)
=
n^2+2n+1
=
(n+1)^2.
$$

Quindi $P(n+1)$ è vera. Per il principio di induzione,

$$
\boxed{\sum_{i=0}^{n-1}(2i+1)=n^2\qquad\forall n\geq 1.}
$$

Il passaggio chiave è accorgersi che la somma per $n+1$ contiene tutti gli addendi della somma per $n$, più il nuovo addendo $i=n$.

---

## 2. Double counting: contare lo stesso insieme in due modi

Una tecnica fondamentale del calcolo combinatorio è il **[[Double counting|double counting]]**, o conteggio doppio.

L’idea: se contiamo lo stesso insieme finito in due modi diversi, i due risultati devono coincidere.

### Interpretazione geometrica della somma dei dispari

Prendiamo un quadrato di $n\times n$ quadratini. Il numero totale di quadratini è

$$
n^2.
$$

Lo stesso quadrato si può dividere in **cornici concentriche**:

- la cornice numero $0$ contiene $1$ quadratino;
- la cornice numero $1$ contiene $3$ quadratini;
- la cornice numero $2$ contiene $5$ quadratini;
- la cornice numero $3$ contiene $7$ quadratini;
- in generale, la cornice numero $i$ contiene $2i+1$ quadratini.

Le cornici sono disgiunte e ricoprono tutto il quadrato. Quindi il numero totale di quadratini è anche

$$
1+3+5+\cdots +(2n-1)
=
\sum_{i=0}^{n-1}(2i+1).
$$

Siccome il totale è $n^2$, otteniamo di nuovo

$$
\sum_{i=0}^{n-1}(2i+1)=n^2.
$$

È un esempio di conteggio doppio: i quadratini sono contati una prima volta come elementi di un quadrato $n\times n$ e una seconda volta come elementi delle cornici.

> [!note]
> Il double counting non è una semplice manipolazione algebrica. Per usarlo bene bisogna specificare con precisione quale insieme si sta contando e verificare che i due metodi contino davvero gli stessi elementi.

---

## 3. Che cosa significa contare

Nel corso, il calcolo combinatorio consiste nel contare gli oggetti di insiemi finiti.

Contare un insieme finito significa metterlo in corrispondenza biunivoca con un insieme standard di numeri naturali. Si usa di solito la notazione

$$
[r]=\{1,2,\ldots,r\}.
$$

Partire da $1$ invece che da $0$ è solo una convenzione: in certi contesti si potrebbe usare $\{0,\ldots,r-1\}$, basta restare coerenti.

### Cardinalità

La **[[Cardinalità|cardinalità]]** di un insieme finito $X$ è il numero di elementi di $X$ e si indica con una delle notazioni

$$
|X|,\qquad \#X,\qquad \operatorname{card}(X).
$$

Dire che $X$ ha cardinalità $r$ significa che esiste una funzione biiettiva

$$
f:[r]\longrightarrow X.
$$

In tal caso si scrive

$$
|X|=r.
$$

Per esempio, se un insieme ha cinque oggetti, numerarli come

$$
1,2,3,4,5
$$

vuol dire costruire una corrispondenza biunivoca tra l’insieme degli oggetti e $[5]$.

### Cardinalità come relazione di equivalenza

Due insiemi $X$ e $Y$ hanno la stessa cardinalità se e solo se esiste una biiezione

$$
f:X\longrightarrow Y.
$$

Si scrive

$$
|X|=|Y|
\quad\Longleftrightarrow\quad
\exists f:X\longrightarrow Y\text{ biiettiva}.
$$

Una [[Funzione biettiva|biiezione]] è una funzione che è insieme:

- **iniettiva**;
- **suriettiva**.

#### Dimostrazione della composizione

Se esistono biiezioni

$$
f:X\longrightarrow [r],
\qquad
g:[r]\longrightarrow Y,
$$

allora la [[Composizione di funzioni|composizione]]

$$
g\circ f:X\longrightarrow Y
$$

è ancora una biiezione, perché la composizione di funzioni biiettive è biiettiva.

Viceversa, se esiste una biiezione $h:X\to Y$, nel caso finito si può numerare $X$ e trasferire la numerazione a $Y$. Questo mostra che i due insiemi hanno lo stesso numero di elementi.

---

## 4. Funzioni, iniettività, suriettività e biiettività

Una funzione

$$
f:X\longrightarrow Y
$$

ha:

- $X$ come **dominio**;
- $Y$ come **codominio**;
- per ogni $x\in X$, un’unica immagine $f(x)\in Y$.

Attenzione a non confondere il codominio con l’[[Immagine e controimmagine|immagine]] della funzione:

$$
\operatorname{Im}(f)=\{f(x):x\in X\}\subseteq Y.
$$

La funzione è:

- **iniettiva** se elementi distinti del dominio hanno immagini distinte:
  
  $$
  x_1\neq x_2
  \Longrightarrow
  f(x_1)\neq f(x_2);
  $$

- **suriettiva** se ogni elemento del codominio è immagine di almeno un elemento del dominio:
  
  $$
  \forall y\in Y\ \exists x\in X:\ f(x)=y;
  $$

- **biiettiva** se è sia iniettiva sia suriettiva.

Due funzioni sono uguali se e solo se hanno lo stesso dominio, lo stesso codominio e coincidono su ogni elemento del dominio:

$$
f=g
\quad\Longleftrightarrow\quad
\forall x\in X,\ f(x)=g(x).
$$

Non basta che abbiano la stessa immagine come insieme: l’associazione tra elementi del dominio e immagini fa parte della funzione.

---

## 5. Il principio dei cassetti

Il **[[Principio dei cassetti|principio dei cassetti]]**, detto anche principio di Dirichlet o della piccionaia, afferma:

> Se si distribuiscono $n$ oggetti in $k$ cassetti con $n>k$, almeno un cassetto contiene almeno due oggetti.

In forma funzionale:

$$
f:X\longrightarrow Y,\qquad |X|>|Y|
$$

non può essere iniettiva.

Infatti, se $f$ fosse iniettiva, elementi distinti di $X$ avrebbero immagini distinte in $Y$. Servirebbero allora in $Y$ almeno tanti elementi quanti ce ne sono in $X$, contro l’ipotesi $|X|>|Y|$.

Per esempio, se distribuiamo $10$ oggetti in $7$ cassetti, almeno un cassetto ne contiene almeno due.

Il principio dei cassetti si usa spesso per dimostrare che è impossibile costruire funzioni iniettive tra insiemi finiti di cardinalità diversa.

---

## 6. Cardinalità del prodotto cartesiano

Il [[Prodotto cartesiano|prodotto cartesiano]] di due insiemi $X$ e $Y$ è

$$
X\times Y
=
\{(x,y):x\in X,\ y\in Y\}.
$$

Gli elementi di $X\times Y$ sono **coppie ordinate**.

L’ordine conta:

$$
(x,y)\neq(y,x)
$$

in generale, anche quando $x$ e $y$ stanno nello stesso insieme. E $(x,x)$ è comunque una coppia ordinata, non un singolo elemento.

Se

$$
|X|=n,\qquad |Y|=m,
$$

allora

$$
|X\times Y|=nm.
$$

#### Motivazione

Per la prima componente ci sono $n$ possibilità. Per ciascuna, la seconda componente si sceglie in $m$ modi. Le scelte sono indipendenti, quindi il totale è

$$
\underbrace{m+\cdots+m}_{n\text{ volte}}
=
nm.
$$

Equivalentemente, si può disegnare il prodotto cartesiano come una tabella:

- le righe corrispondono agli elementi di $X$;
- le colonne corrispondono agli elementi di $Y$;
- ogni casella è una coppia ordinata.

Più in generale, per insiemi finiti $X_1,\ldots,X_r$,

$$
\left|X_1\times\cdots\times X_r\right|
=
|X_1|\cdots |X_r|.
$$

---

## 7. Numero di funzioni tra due insiemi finiti

Siano $X$ e $Y$ insiemi finiti con

$$
|X|=n,\qquad |Y|=m.
$$

Vogliamo contare l’insieme di tutte le funzioni

$$
f:X\longrightarrow Y.
$$

Indichiamo gli elementi del dominio con

$$
X=\{x_1,\ldots,x_n\}
$$

e quelli del codominio con

$$
Y=\{y_1,\ldots,y_m\}.
$$

Per costruire una funzione:

- $f(x_1)$ si può scegliere in $m$ modi;
- $f(x_2)$ si può scegliere in $m$ modi;
- e così via, fino a $f(x_n)$, sempre in $m$ modi.

Le scelte sono indipendenti: nessuno chiede che elementi diversi del dominio abbiano immagini diverse. Quindi la funzione può anche essere costante, cioè tale che tutti gli elementi di $X$ abbiano la stessa immagine.

Di conseguenza,

$$
|\{f:X\to Y\}|=
\underbrace{m\cdot m\cdots m}_{n\text{ fattori}}
=
m^n.
$$

Dunque:

$$
\boxed{|Y^X|=|Y|^{|X|}=m^n.}
$$

La notazione $Y^X$ indica a volte l’insieme di tutte le funzioni da $X$ a $Y$.

---

## 8. Conteggio delle funzioni iniettive

Siano ancora

$$
|X|=n,\qquad |Y|=m.
$$

Vogliamo contare le funzioni iniettive

$$
f:X\longrightarrow Y.
$$

Per costruirne una:

- l’immagine di $x_1$ si sceglie in $m$ modi;
- l’immagine di $x_2$ si sceglie in $m-1$ modi, perché non può coincidere con $f(x_1)$;
- l’immagine di $x_3$ si sceglie in $m-2$ modi;
- e così via: l’immagine di $x_n$ si sceglie in $m-n+1$ modi.

Quindi, se $n\leq m$, il numero di funzioni iniettive è

$$
m(m-1)(m-2)\cdots(m-n+1).
$$

Con i fattoriali:

$$
\boxed{
\frac{m!}{(m-n)!}
}.
$$

Infatti,

$$
m!
=
m(m-1)\cdots(m-n+1)(m-n)!.
$$

Se $n>m$ non esistono funzioni iniettive da $X$ a $Y$, per il principio dei cassetti: il numero è $0$.

In forma compatta:

$$
\#\{\text{funzioni iniettive }X\to Y\}
=
\begin{cases}
\dfrac{m!}{(m-n)!}, & n\leq m,\\[1.2ex]
0, & n>m.
\end{cases}
$$

Il prodotto dei fattori decrescenti si indica spesso, informalmente, con una notazione di permutazione, ma la forma con i fattoriali rende il conteggio più esplicito.

Per convenzione:

$$
0!=1.
$$

> [!example] Esempio
> Quante funzioni iniettive ci sono da $X=\{1,2,3\}$ a $Y=\{a,b,c,d,e\}$? Qui $n=3$ e $m=5$, quindi $5\cdot 4\cdot 3=\frac{5!}{2!}=60$.

---

## 9. Funzioni tra insiemi finiti con la stessa cardinalità

Se $X$ e $Y$ sono finiti e hanno la stessa cardinalità,

$$
|X|=|Y|=n,
$$

allora per una funzione

$$
f:X\longrightarrow Y
$$

valgono le equivalenze:

$$
f\text{ iniettiva}
\quad\Longleftrightarrow\quad
f\text{ suriettiva}
\quad\Longleftrightarrow\quad
f\text{ biiettiva}.
$$

#### Perché una funzione iniettiva è suriettiva

Se $f$ è iniettiva, le $n$ immagini degli $n$ elementi di $X$ sono tutte distinte. Siccome anche $Y$ ha esattamente $n$ elementi, queste immagini sono tutti gli elementi di $Y$. Quindi $f$ è suriettiva.

#### Perché una funzione non iniettiva non può essere suriettiva

Se $f$ non è iniettiva, almeno due elementi distinti di $X$ hanno la stessa immagine. Allora tra le immagini compaiono meno di $n$ elementi distinti. Siccome $Y$ ne contiene $n$, almeno un elemento del codominio resta escluso: la funzione non è suriettiva.

L’equivalenza dipende dalla finitezza. Per insiemi infiniti può esistere una funzione iniettiva ma non suriettiva da un insieme in sé stesso; per esempio,

$$
f:\mathbb{N}\longrightarrow\mathbb{N},
\qquad
f(n)=n+1
$$

è iniettiva ma non suriettiva, perché $0$ non appartiene alla sua immagine se $\mathbb N$ contiene $0$.

---

## 10. Insieme delle parti

Dato un insieme $X$, si indica con

$$
\mathcal{P}(X)
$$

o a volte con $P(X)$ l’**[[Insieme delle parti|insieme delle parti]]** di $X$, cioè l’insieme di tutti i [[Sottoinsieme|sottoinsiemi]] di $X$:

$$
\mathcal{P}(X)=\{A:A\subseteq X\}.
$$

Se $|X|=n$, allora

$$
\boxed{|\mathcal{P}(X)|=2^n.}
$$

#### Conteggio diretto

Per costruire un sottoinsieme $A\subseteq X$, ogni elemento di $X$ può essere:

1. inserito in $A$;
2. non inserito in $A$.

Per ciascuno degli $n$ elementi ci sono dunque $2$ possibilità indipendenti, e il numero totale di scelte è

$$
\underbrace{2\cdot 2\cdots 2}_{n\text{ fattori}}
=
2^n.
$$

Il conteggio include:

- il sottoinsieme vuoto $\varnothing$;
- il sottoinsieme $X$;
- tutti i sottoinsiemi intermedi.

Per esempio, se $X=\{a,b,c\}$, i sottoinsiemi sono:

- uno di cardinalità $0$: $\varnothing$;
- tre di cardinalità $1$: $\{a\}$, $\{b\}$, $\{c\}$;
- tre di cardinalità $2$: $\{a,b\}$, $\{a,c\}$, $\{b,c\}$;
- uno di cardinalità $3$: $\{a,b,c\}$.

In totale:

$$
1+3+3+1=8=2^3.
$$

---

## 11. Funzioni caratteristiche e corrispondenza con l’insieme delle parti

A ogni sottoinsieme $A\subseteq X$ si associa la sua **[[Funzione caratteristica|funzione caratteristica]]**

$$
\chi_A:X\longrightarrow \{0,1\},
$$

definita da

$$
\chi_A(x)=
\begin{cases}
1, & x\in A,\\
0, & x\notin A.
\end{cases}
$$

Il valore $1$ dice che l’elemento è stato inserito nel sottoinsieme, il valore $0$ che non lo è stato.

Per esempio, se

$$
X=\{a,b,c\},
\qquad
A=\{a,c\},
$$

allora

$$
\chi_A(a)=1,\qquad
\chi_A(b)=0,\qquad
\chi_A(c)=1.
$$

Il sottoinsieme $A$ determina completamente $\chi_A$, e viceversa: dalla funzione caratteristica si ricostruisce il sottoinsieme come

$$
A=\{x\in X:\chi_A(x)=1\}.
$$

Quindi la corrispondenza

$$
A\longmapsto \chi_A
$$

è una biiezione tra $\mathcal{P}(X)$ e l’insieme delle funzioni da $X$ a $\{0,1\}$:

$$
\mathcal{P}(X)
\longleftrightarrow
\{0,1\}^X.
$$

Siccome

$$
|\{0,1\}^X|
=
2^{|X|},
$$

otteniamo di nuovo

$$
|\mathcal{P}(X)|=2^{|X|}.
$$

È una seconda dimostrazione, più formale, della cardinalità dell’insieme delle parti.

---

## 12. Uguaglianza e inclusione tra insiemi

Due insiemi $A$ e $B$ sono uguali se e solo se hanno esattamente gli stessi elementi:

$$
A=B
\quad\Longleftrightarrow\quad
\forall x,\ x\in A\Longleftrightarrow x\in B.
$$

Per dimostrare un’uguaglianza tra insiemi conviene spesso dimostrare le due inclusioni:

$$
A\subseteq B
\qquad\text{e}\qquad
B\subseteq A.
$$

L’inclusione $A\subseteq B$ significa:

$$
\forall x\in A,\ x\in B.
$$

La sua negazione è:

$$
A\not\subseteq B
\quad\Longleftrightarrow\quad
\exists x\in A\text{ tale che }x\notin B.
$$

Di conseguenza, se $A\neq B$ almeno una delle due inclusioni fallisce:

$$
A\neq B
\quad\Longleftrightarrow\quad
A\not\subseteq B
\ \text{oppure}\
B\not\subseteq A.
$$

Se le ipotesi sono simmetriche rispetto ad $A$ e $B$, si può a volte procedere “senza perdita di generalità” supponendo che fallisca, per esempio, $A\subseteq B$. Allora esiste un elemento

$$
x\in A\setminus B.
$$

Occhio: questa tecnica si usa solo quando le due situazioni sono davvero simmetriche.

---

## 13. Sottoinsiemi di cardinalità fissata e coefficienti binomiali

Sia $X$ un insieme con $|X|=n$. Vogliamo contare i sottoinsiemi di $X$ con cardinalità $r$.

Questo numero si indica con

$$
\binom{n}{r}
$$

e si legge “$n$ su $r$”: è il [[Coefficiente binomiale|coefficiente binomiale]].

Per costruire una $r$-upla ordinata di elementi distinti si può scegliere:

- il primo elemento in $n$ modi;
- il secondo in $n-1$ modi;
- il terzo in $n-2$ modi;
- e così via.

Il numero di $r$-uple ordinate di elementi distinti è quindi

$$
n(n-1)\cdots(n-r+1)
=
\frac{n!}{(n-r)!}.
$$

Però ogni sottoinsieme di $r$ elementi è stato contato $r!$ volte, una per ciascun ordinamento dei suoi elementi. Perciò:

$$
\boxed{
\binom{n}{r}
=
\frac{n!}{r!(n-r)!}
}.
$$

Il fattore $r!$ serve proprio a cancellare l’ordine.

> [!example] Esempio
> Quanti sottoinsiemi di $2$ elementi ha $\{a,b,c,d,e\}$? Le coppie ordinate di elementi distinti sono $5\cdot 4=20$, e ogni sottoinsieme è contato $2!=2$ volte, quindi $\binom{5}{2}=\frac{20}{2}=10$.

### Casi limite

Per convenzione:

$$
\binom{n}{0}=1,
\qquad
\binom{n}{n}=1,
$$

perché esiste un solo sottoinsieme vuoto e un solo sottoinsieme formato da tutti gli elementi di $X$.

Inoltre,

$$
\binom{n}{r}=0
\qquad\text{se }r>n.
$$

### Simmetria dei coefficienti binomiali

Vale la relazione

$$
\boxed{
\binom{n}{r}=\binom{n}{n-r}
}.
$$

La ragione combinatoria è che scegliere un sottoinsieme $A\subseteq X$ con $r$ elementi equivale a scegliere il suo complementare

$$
X\setminus A,
$$

che ha $n-r$ elementi.

La corrispondenza

$$
A\longmapsto X\setminus A
$$

è una biiezione tra:

- i sottoinsiemi di $X$ con cardinalità $r$;
- i sottoinsiemi di $X$ con cardinalità $n-r$.

---

## 14. Relazione tra funzioni iniettive, tuple ordinate e sottoinsiemi

Le funzioni iniettive

$$
f:[r]\longrightarrow X
$$

corrispondono alle $r$-uple ordinate

$$
(x_1,\ldots,x_r)
$$

di elementi distinti di $X$, ponendo

$$
x_i=f(i).
$$

Il numero di tali funzioni è

$$
n(n-1)\cdots(n-r+1)
=
\frac{n!}{(n-r)!}.
$$

Se invece dell’ordine conta solo il sottoinsieme formato dagli elementi scelti, bisogna identificare tutte le $r!$ permutazioni della stessa $r$-upla. Si ottiene:

$$
\frac{1}{r!}\cdot\frac{n!}{(n-r)!}
=
\frac{n!}{r!(n-r)!}
=
\binom{n}{r}.
$$

La distinzione è essenziale:

- una **tupla ordinata** tiene conto della posizione degli elementi;
- un **sottoinsieme** non tiene conto dell’ordine.

Per esempio, le tuple

$$
(a,b,c)
\qquad\text{e}\qquad
(b,a,c)
$$

sono diverse, mentre i sottoinsiemi

$$
\{a,b,c\}
\qquad\text{e}\qquad
\{b,a,c\}
$$

sono lo stesso insieme.

---

## 15. Conteggio mediante quozienti: evitare il sovracconteggio

Nel calcolo combinatorio capita spesso di contare un insieme in modo non biunivoco: ogni oggetto viene contato più volte.

Se ogni oggetto viene contato esattamente $k$ volte e il conteggio complessivo dà $N$, il numero corretto di oggetti è

$$
\frac{N}{k}.
$$

Funziona solo se il numero di volte in cui ogni oggetto viene contato è sempre lo stesso.

#### Esempio generale

Supponiamo di voler contare i sottoinsiemi di cardinalità $r$ di un insieme con $n$ elementi.

Contiamo prima le $r$-uple ordinate di elementi distinti:

$$
\frac{n!}{(n-r)!}.
$$

Ogni sottoinsieme di cardinalità $r$ compare esattamente $r!$ volte, perché i suoi elementi si possono ordinare in $r!$ modi. Il conteggio corretto è quindi

$$
\frac{\frac{n!}{(n-r)!}}{r!}
=
\binom{n}{r}.
$$

Il punto essenziale è che il sovracconteggio sia uniforme. Se oggetti diversi sono contati un numero diverso di volte, non basta dividere per un unico fattore.

---

## 16. Collegamento tra le principali tecniche

Le tecniche viste sono manifestazioni diverse della stessa idea di fondo: ridurre il problema a un conteggio più semplice.

- Per calcolare una somma, si può usare l’induzione oppure un double counting geometrico.
- Per contare un insieme finito, lo si mette in corrispondenza con $[n]$.
- Per contare le coppie, si moltiplicano le cardinalità.
- Per contare le funzioni, si fa una scelta indipendente per ogni elemento del dominio.
- Per contare le funzioni iniettive, si impedisce di riusare immagini già scelte.
- Per contare i sottoinsiemi, si registra per ogni elemento la scelta “inserito/non inserito”.
- Per contare i sottoinsiemi di cardinalità fissata, si contano prima gli ordinamenti e poi si elimina il sovracconteggio dovuto alle permutazioni.
- Per dimostrare l’impossibilità dell’iniettività, si usa il principio dei cassetti.
- Per dimostrare che due insiemi hanno la stessa cardinalità, si costruisce una biiezione.

Il calcolo combinatorio richiede quindi di individuare con precisione:

1. quali sono gli oggetti da contare;
2. se l’ordine conta;
3. se sono ammesse ripetizioni;
4. se le scelte sono indipendenti;
5. se ogni oggetto viene contato una sola volta o più volte;
6. se il sovracconteggio è uniforme.
