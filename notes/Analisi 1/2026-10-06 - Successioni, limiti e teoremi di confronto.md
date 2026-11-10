---
type: lecture-note
course: Analisi 1
date: '2026-10-06'
title: Successioni, limiti e teoremi di confronto
source_files:
- AM1_26_L011.pdf
- AM1_26_L012.pdf
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Analisi 1/Lectures/2026-10-06 - Successioni, limiti e teoremi di confronto.md
vault_hash: eb555b9fa2721108d2317c603bbf9ef9439fdc3a22856b70059f9e816074450e
---

# Successioni, limiti e teoremi di confronto

## 1. Proprietà vere definitivamente e frequentemente

Sia $P(n)$ un predicato definito sui numeri naturali.

Si dice che $P(n)$ vale **[[Proprietà definitivamente vera|definitivamente]]** se è vero da un certo punto in poi, cioè se

$$
\exists n_0\in\mathbb{N}
\quad\text{tale che}\quad
\forall n\geq n_0,\ P(n)\text{ è vero}.
$$

Non importa cosa succede prima di $n_0$: per i primi indici $P(n)$ può essere vera oppure falsa.

Si dice invece che $P(n)$ vale **frequentemente** se è vera per infiniti valori di $n$. Equivalentemente,

$$
\forall n_0\in\mathbb{N},
\quad
\exists n\geq n_0
\quad\text{tale che}\quad
P(n)\text{ è vero}.
$$

In altre parole, per quanto si vada avanti nella successione si incontra ancora almeno un indice per cui $P(n)$ è vera. Questi infiniti indici non devono essere per forza consecutivi.

---

## 2. Successioni

### 2.1 Definizione

Una **[[Successione|successione]] di numeri reali** è, nella definizione più rigida, una funzione

$$
f\colon\mathbb{N}\to\mathbb{R}.
$$

Invece di scrivere $f(n)$ si usano di solito simboli come

$$
a_n,\qquad b_n,\qquad x_n,\qquad y_n.
$$

Conviene anche una definizione più elastica: per parlare di successione non serve che il termine sia definito per ogni $n\in\mathbb{N}$; basta che sia definito **definitivamente**, cioè per ogni $n$ abbastanza grande.

### 2.2 Esempi

La successione

$$
a_n=\frac{1}{n-4}
$$

è ben definita per ogni $n\geq 5$, quindi è una successione secondo la definizione elastica.

Anche

$$
b_n=\sqrt{n-2025}
$$

è una successione, perché è definita per ogni $n\geq 2025$.

Invece

$$
c_n=\sqrt{2025-n}
$$

non è una successione secondo questa convenzione: è definita solo per un numero finito di indici naturali e non da un certo punto in poi.

### 2.3 Come visualizzare una successione

Consideriamo, per esempio,

$$
a_n=\frac{1}{n}.
$$

Una successione si può rappresentare in almeno tre modi.

1. **Come grafico:** si disegnano nel piano i punti $(n,a_n)$.
2. **Come fotografia:** si segnano su una retta i valori $a_n$, scrivendo accanto a ciascuno il suo indice.
3. **Come video:** si immagina un punto che sta per un secondo nella posizione $a_1$, poi in $a_2$, poi in $a_3$ e così via.

La successione non è quindi solo l’insieme dei valori assunti: conta anche l’ordine con cui vengono percorsi.

---

## 3. Limite di una successione

Sia $(a_n)$ una successione di numeri reali. Quando $n\to+\infty$ si possono avere quattro situazioni:

$$
\lim_{n\to+\infty}a_n=
\begin{cases}
\ell\in\mathbb{R},\\
+\infty,\\
-\infty,\\
\text{non esiste}.
\end{cases}
$$

### 3.1 Limite uguale a $+\infty$

Si dice che

$$
\lim_{n\to+\infty}a_n=+\infty,
\qquad\text{oppure}\qquad
a_n\to+\infty,
$$

se

$$
\forall M\in\mathbb{R},
\quad
a_n\geq M
\quad\text{definitivamente}.
$$

Esplicitando il significato di “definitivamente”:

$$
\forall M\in\mathbb{R},
\quad
\exists n_0\in\mathbb{N}
\quad\text{tale che}\quad
\forall n\geq n_0,\ a_n\geq M.
$$

La soglia $M$ può essere grande quanto si vuole; l’indice $n_0$ dipende in generale da $M$.

### 3.2 Limite uguale a $-\infty$

Si dice che

$$
\lim_{n\to+\infty}a_n=-\infty,
\qquad\text{oppure}\qquad
a_n\to-\infty,
$$

se

$$
\forall M\in\mathbb{R},
\quad
a_n\leq M
\quad\text{definitivamente}.
$$

Equivalentemente,

$$
\forall M\in\mathbb{R},
\quad
\exists n_0\in\mathbb{N}
\quad\text{tale che}\quad
\forall n\geq n_0,\ a_n\leq M.
$$

Qui $M$ può essere anche molto negativo. Informalmente, a ogni soglia $M$ si associa un indice oltre il quale tutti i termini della successione stanno sotto $M$.

### 3.3 Limite finito

Si dice che

$$
\lim_{n\to+\infty}a_n=\ell\in\mathbb{R},
\qquad\text{oppure}\qquad
a_n\to\ell,
$$

se

$$
\forall\varepsilon>0,
\quad
\ell-\varepsilon\leq a_n\leq\ell+\varepsilon
\quad\text{definitivamente}.
$$

Equivalentemente,

$$
\forall\varepsilon>0,
\quad
|a_n-\ell|\leq\varepsilon
\quad\text{definitivamente}.
$$

Esplicitando tutti i quantificatori:

$$
\forall\varepsilon>0,
\quad
\exists n_0\in\mathbb{N}
\quad\text{tale che}\quad
\forall n\geq n_0,\ |a_n-\ell|\leq\varepsilon.
$$

Il numero $\varepsilon$ può essere scelto arbitrariamente vicino a $0$. La definizione chiede quindi che la distanza tra $a_n$ e $\ell$ diventi, da un certo punto in poi, piccola quanto si vuole. Questo è il **[[Limite di una successione|limite di una successione]]**.

> [!note]
> Nelle definizioni di limite, sostituire alcune disuguaglianze larghe con disuguaglianze strette non cambia il concetto. Per esempio, si può usare $|a_n-\ell|<\varepsilon$ al posto di $|a_n-\ell|\leq\varepsilon$.

### 3.4 Avvicinamento da destra e da sinistra

La notazione

$$
a_n\to\ell^+
$$

indica che $a_n\to\ell$ e che i termini si avvicinano a $\ell$ da valori maggiori di $\ell$:

$$
\forall\varepsilon>0,
\quad
\ell<a_n\leq\ell+\varepsilon
\quad\text{definitivamente}.
$$

Analogamente,

$$
a_n\to\ell^-
$$

significa che

$$
\forall\varepsilon>0,
\quad
\ell-\varepsilon\leq a_n<\ell
\quad\text{definitivamente}.
$$

---

## 4. Primi esempi di limiti

A livello intuitivo:

$$
n^2+27\to+\infty,
$$

$$
3-n^3\to-\infty,
$$

$$
\frac{1}{n-5}\to 0,
$$

mentre la successione

$$
a_n=(-1)^n=1,-1,1,-1,\ldots
$$

non ha limite.

### 4.1 Dimostrazione che $n^2\to+\infty$

Bisogna mostrare che, per ogni $M\in\mathbb{R}$, vale $n^2\geq M$ definitivamente.

- Se $M\leq0$, allora $n^2\geq M$ per ogni $n\in\mathbb{N}$.
- Se $M>0$, basta scegliere un intero $n_0\geq\sqrt{M}$. Per ogni $n\geq n_0$ si ha

$$
n^2\geq n_0^2\geq M.
$$

Quindi

$$
\lim_{n\to+\infty}n^2=+\infty.
$$

Un modo equivalente di scegliere l’indice è prendere, per $M>0$, un intero $n_0\geq M$ e $n_0\geq1$. Allora

$$
n^2\geq n_0^2\geq n_0\geq M
$$

per ogni $n\geq n_0$.

### 4.2 Dimostrazione che $\frac1n\to0^+$

Vogliamo mostrare che, per ogni $\varepsilon>0$,

$$
0<\frac1n\leq\varepsilon
$$

definitivamente. Per $n\geq1$,

$$
\frac1n\leq\varepsilon
\quad\Longleftrightarrow\quad
n\geq\frac1\varepsilon.
$$

Basta dunque scegliere un intero

$$
n_0\geq\max\left\{1,\frac1\varepsilon\right\}.
$$

Per ogni $n\geq n_0$ si ha $0<1/n\leq\varepsilon$, quindi

$$
\frac1n\to0^+.
$$

### 4.3 Perché $(-1)^n$ non ha limite

La successione $(-1)^n$ non tende a $+\infty$: per esempio, non diventa mai definitivamente maggiore o uguale a $2025$. Non tende neppure a $-\infty$, perché non diventa mai definitivamente minore o uguale a $-37$.

E non può convergere a un numero reale $\ell$:

- se $\ell>1$, scegliendo $\varepsilon$ abbastanza piccolo l’intervallo $[\ell-\varepsilon,\ell+\varepsilon]$ resta sopra $1$ e non contiene alcun termine;
- se $\ell<-1$, si ragiona in modo simmetrico;
- se $-1<\ell<1$, un intorno abbastanza piccolo di $\ell$ non contiene né $-1$ né $1$;
- se $\ell=1$, con $\varepsilon=1$ i termini uguali a $-1$ restano fuori dall’intervallo $[0,2]$;
- se $\ell=-1$, con $\varepsilon=1$ restano fuori i termini uguali a $1$.

Poiché sia $1$ sia $-1$ compaiono infinite volte, nessuno dei quattro tipi di limite è possibile.

---

## 5. Affermazioni intuitive false

Alcune congetture plausibili non seguono dalla definizione di limite.

### 5.1 Divergere a $+\infty$ non implica crescere definitivamente

L’affermazione

> Se $a_n\to+\infty$, allora $(a_n)$ è definitivamente crescente

è falsa. Una successione può continuare a oscillare verso l’alto e verso il basso pur superando definitivamente ogni soglia. Per esempio,

$$
0,2,1,3,2,4,3,5,\ldots
$$

tende a $+\infty$, ma non è definitivamente crescente.

### 5.2 Convergere a $0$ non implica arrivare da un solo lato

L’affermazione

> Se $a_n\to0$, allora $a_n\to0^+$ oppure $a_n\to0^-$

è falsa. Per esempio,

$$
a_n=\frac{(-1)^n}{n}
$$

converge a $0$, ma cambia segno a ogni passo.

### 5.3 Convergere a $0^+$ non implica decrescere definitivamente

Anche l’affermazione

> Se $a_n\to0^+$, allora $(a_n)$ è definitivamente decrescente

è falsa: una successione può avvicinarsi a $0$ da valori positivi continuando a fare piccole oscillazioni.

### 5.4 Una successione limitata non deve avere limite

La successione

$$
0,1,0,1,0,1,\ldots
$$

assume solo valori in $[0,1]$, quindi è limitata, ma non converge.

---

## 6. Conseguenze della definizione di limite

### 6.1 Una successione che tende a $+\infty$ è limitata inferiormente

Se $a_n\to+\infty$, allora esiste $L\in\mathbb{R}$ tale che

$$
a_n\geq L
\qquad
\forall n.
$$

**Dimostrazione.** Applicando la definizione di limite con $M=2025$, esiste $n_0$ tale che

$$
a_n\geq2025
\qquad
\forall n\geq n_0.
$$

Restano da controllare solo i termini del prefisso finito che precede $n_0$. Si pone

$$
L=\min\{2025,a_0,a_1,\ldots,a_{n_0-1}\}.
$$

Allora $a_n\geq L$ per ogni $n$: prima di $n_0$ per definizione di minimo, da $n_0$ in poi perché $a_n\geq2025\geq L$.

### 6.2 Ogni successione convergente è limitata

Se $a_n\to\ell\in\mathbb{R}$, allora esistono $A,B\in\mathbb{R}$ tali che

$$
A\leq a_n\leq B
\qquad
\forall n.
$$

**Dimostrazione.** Nella definizione di limite scegliamo, per esempio, $\varepsilon=5$. Esiste $n_0$ tale che

$$
\ell-5\leq a_n\leq\ell+5
\qquad
\forall n\geq n_0.
$$

Si possono allora scegliere

$$
A=\min\{\ell-5,a_0,a_1,\ldots,a_{n_0-1}\},
$$

$$
B=\max\{\ell+5,a_0,a_1,\ldots,a_{n_0-1}\}.
$$

Questi due numeri controllano sia il prefisso finito sia tutti i termini successivi. La limitatezza si può esprimere in modo equivalente dicendo che esiste $L\geq0$ tale che

$$
|a_n|\leq L
\qquad
\forall n.
$$

> [!warning]
> Vale “convergente $\Rightarrow$ limitata”, ma il viceversa è falso, come mostra la successione alternata $0,1,0,1,\ldots$.

### 6.3 Permanenza del segno

Se

$$
a_n\to\ell>0,
$$

allora $a_n>0$ definitivamente. Questo è il teorema di **[[Permanenza del segno|permanenza del segno]]**.

**Dimostrazione.** Nella definizione di limite scegliamo

$$
\varepsilon=\frac{\ell}{2}.
$$

Definitivamente si ha

$$
\ell-\frac\ell2
\leq a_n
\leq
\ell+\frac\ell2,
$$

cioè

$$
\frac\ell2\leq a_n\leq\frac{3\ell}{2}.
$$

Poiché $\ell/2>0$, segue che $a_n>0$ definitivamente.

Più in generale, se $a_n\to\sqrt{17}$, allora

$$
4\leq a_n\leq5
$$

definitivamente: basta scegliere $\varepsilon>0$ abbastanza piccolo da avere

$$
4\leq\sqrt{17}-\varepsilon
\qquad\text{e}\qquad
\sqrt{17}+\varepsilon\leq5.
$$

---

## 7. Teoremi di confronto

### 7.1 Confronto con un limite infinito

Siano $(a_n)$ e $(b_n)$ due successioni tali che

$$
a_n\leq b_n
$$

definitivamente.

Valgono le seguenti implicazioni:

1. se $a_n\to+\infty$, allora $b_n\to+\infty$;
2. se $b_n\to-\infty$, allora $a_n\to-\infty$.

**Dimostrazione del primo punto.** Per ipotesi esiste $n_0$ tale che $a_n\leq b_n$ per ogni $n\geq n_0$.

Fissato $M\in\mathbb{R}$, dal fatto che $a_n\to+\infty$ segue l’esistenza di $n_1$ tale che

$$
a_n\geq M
\qquad
\forall n\geq n_1.
$$

Posto

$$
n_2=\max\{n_0,n_1\},
$$

per ogni $n\geq n_2$ si ha

$$
b_n\geq a_n\geq M.
$$

Poiché $M$ è arbitrario, $b_n\to+\infty$. Il secondo punto si dimostra in modo analogo.

> [!warning]
> Da $a_n\leq b_n$ e $b_n\to5$ non si può dedurre in generale il limite di $a_n$. La successione $(a_n)$ potrebbe convergere a un valore $\ell\leq5$, tendere a $-\infty$ oppure non avere limite.

Nemmeno le disuguaglianze strette passano necessariamente al limite. Per esempio,

$$
a_n=5-\frac3n,
\qquad
b_n=5-\frac1n.
$$

Per ogni $n\geq1$ si ha $a_n<b_n$ e $b_n\to5^-$, ma entrambe le successioni convergono a $5$.

### 7.2 Teorema dei carabinieri

Il **[[Teorema dei carabinieri|teorema dei carabinieri]]**: siano $(a_n)$, $(b_n)$ e $(c_n)$ tre successioni. Supponiamo che

$$
a_n\leq b_n\leq c_n
$$

definitivamente e che

$$
a_n\to\ell,
\qquad
c_n\to\ell,
$$

con $\ell\in\mathbb{R}$. Allora

$$
b_n\to\ell.
$$

**Dimostrazione.** Fissiamo $\varepsilon>0$.

Poiché $a_n\to\ell$, esiste $n_a$ tale che

$$
\ell-\varepsilon\leq a_n\leq\ell+\varepsilon
\qquad
\forall n\geq n_a.
$$

Poiché $c_n\to\ell$, esiste $n_c$ tale che

$$
\ell-\varepsilon\leq c_n\leq\ell+\varepsilon
\qquad
\forall n\geq n_c.
$$

Infine esiste $n_0$ tale che

$$
a_n\leq b_n\leq c_n
\qquad
\forall n\geq n_0.
$$

Per ogni

$$
n\geq\max\{n_a,n_c,n_0\}
$$

si ottiene

$$
\ell-\varepsilon
\leq a_n
\leq b_n
\leq c_n
\leq\ell+\varepsilon.
$$

In particolare,

$$
\ell-\varepsilon\leq b_n\leq\ell+\varepsilon
$$

definitivamente. Per definizione, $b_n\to\ell$.

Nella dimostrazione servono solo due delle quattro disuguaglianze disponibili: $\ell-\varepsilon\leq a_n$ e $c_n\leq\ell+\varepsilon$.

> [!example] Esempio
> Per calcolare $\lim_{n\to+\infty}\frac{\sin n}{n}$ si osserva che $-\frac1n\leq\frac{\sin n}{n}\leq\frac1n$ e che entrambi gli estremi tendono a $0$: per il teorema dei carabinieri, anche $\frac{\sin n}{n}\to0$.
