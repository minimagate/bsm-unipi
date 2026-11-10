---
type: lecture-note
course: Analisi 1
date: '2026-10-07'
title: Successioni monotone, numero di Nepero e teoremi algebrici sui limiti
source_files:
- AM1_26_L013.pdf
- AM1_26_L014.pdf
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Analisi 1/Lectures/2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti.md
vault_hash: c1c9ac1515a00bfb0a45d7155d4d7fbfc0b21218355db7be5670ccedc769946c
---

# Successioni monotone, numero di Nepero e teoremi algebrici sui limiti

Questa nota prosegue [[2026-10-06 - Successioni, limiti e teoremi di confronto]].

## 1. Limitatezza

Una successione $(a_n)$ si dice:

- **limitata superiormente** se esiste $L\in\mathbb{R}$ tale che $a_n\leq L$ per ogni $n\in\mathbb{N}$;
- **limitata inferiormente** se esiste $L\in\mathbb{R}$ tale che $a_n\geq L$ per ogni $n\in\mathbb{N}$;
- **limitata** se è limitata sia superiormente sia inferiormente.

Equivalentemente, $(a_n)$ è limitata se

$$
\exists L\in\mathbb{R}
\quad\text{tale che}\quad
\forall n\in\mathbb{N},\ |a_n|\leq L,
$$

cioè se tutti i termini sono compresi tra $-L$ e $L$.

---

## 2. Monotonia

### 2.1 Definizione con termini consecutivi

Una successione $(a_n)$ si dice:

| Tipo | Condizione, per ogni $n\in\mathbb{N}$ |
|---|---|
| **strettamente crescente** | $a_{n+1}>a_n$ |
| **debolmente crescente** | $a_{n+1}\geq a_n$ |
| **strettamente decrescente** | $a_{n+1}<a_n$ |
| **debolmente decrescente** | $a_{n+1}\leq a_n$ |

### 2.2 Definizione equivalente con indici qualsiasi

Confrontando termini consecutivi si ottiene, per transitività, il confronto tra due termini qualsiasi. Le definizioni precedenti sono quindi equivalenti a:

| Tipo | Condizione |
|---|---|
| strettamente crescente | $m>n\ \Rightarrow\ a_m>a_n$ |
| debolmente crescente | $m>n\ \Rightarrow\ a_m\geq a_n$ |
| strettamente decrescente | $m>n\ \Rightarrow\ a_m<a_n$ |
| debolmente decrescente | $m>n\ \Rightarrow\ a_m\leq a_n$ |

> [!note]
> Nei casi deboli si può scrivere indifferentemente $m\geq n$ al posto di $m>n$: per $m=n$ la disuguaglianza larga è banalmente vera.

### 2.3 Monotonia e limitatezza

- Una successione debolmente crescente è **limitata inferiormente**: tutti i termini sono $\geq a_0$.
- Una successione debolmente decrescente è **limitata superiormente**: tutti i termini sono $\leq a_0$.

---

## 3. Teorema sulle successioni monotone

L’idea è che una [[Successione monotona|successione monotona]] ha solo due comportamenti possibili: converge a un numero reale oppure diverge, nel verso della monotonia. Non può oscillare senza limite.

### 3.1 Enunciato (versione crescente)

Sia $(a_n)$ una successione debolmente crescente (se è strettamente crescente, a maggior ragione). Allora

$$
a_n\to\ell\in\mathbb{R}\cup\{+\infty\}
$$

e inoltre

$$
\ell=\sup\{a_n : n\in\mathbb{N}\}.
$$

### 3.2 Dimostrazione

La dimostrazione usa la [[2026-09-28 - Assiomi dei reali e proprietà di completezza#15. Caratterizzazione del supremo|caratterizzazione del supremo]]. Si distinguono due casi.

**Caso 1: $\ell=\sup\{a_n\}=+\infty$.** Bisogna dimostrare che

$$
\forall M\in\mathbb{R},\qquad a_n\geq M\ \text{definitivamente}.
$$

- Si fissa $M\in\mathbb{R}$.
- Poiché il supremo è $+\infty$, per la caratterizzazione esiste $n_0\in\mathbb{N}$ tale che $a_{n_0}\geq M$.
- Per monotonia, per ogni $n\geq n_0$ si ha

$$
a_n\geq a_{n_0}\geq M.
$$

Quindi $a_n\to+\infty$.

**Caso 2: $\ell=\sup\{a_n\}\in\mathbb{R}$.** Bisogna dimostrare che

$$
\forall\varepsilon>0,\qquad \ell-\varepsilon\leq a_n\leq\ell+\varepsilon\ \text{definitivamente}.
$$

- Si fissa $\varepsilon>0$.
- Per la caratterizzazione del supremo esiste $n_0\in\mathbb{N}$ tale che $a_{n_0}\geq\ell-\varepsilon$.
- Per monotonia, per ogni $n\geq n_0$:

$$
a_n\geq a_{n_0}\geq\ell-\varepsilon.
$$

Questa è la disuguaglianza di sinistra. Quella di destra è vera per ogni $n$, non solo definitivamente: poiché $\ell$ è un [[Maggiorante|maggiorante]],

$$
a_n\leq\ell\leq\ell+\varepsilon
\qquad\forall n\in\mathbb{N}.
$$

Quindi $a_n\to\ell$.

### 3.3 Versione decrescente

Se $(a_n)$ è debolmente decrescente, allora

$$
a_n\to\ell=\inf\{a_n : n\in\mathbb{N}\}\in\mathbb{R}\cup\{-\infty\}.
$$

La dimostrazione è lasciata per esercizio ed è analoga alla precedente.

### 3.4 Corollario

Se $(a_n)$ è debolmente crescente e limitata superiormente, allora

$$
a_n\to\ell\in\mathbb{R}.
$$

Infatti il supremo di un insieme limitato superiormente è finito. Analogamente, una successione debolmente decrescente e limitata inferiormente converge a un limite reale.

### 3.5 Da che lato si arriva al limite?

Se $(a_n)$ è debolmente crescente e limitata superiormente, si può dire che $a_n\to\ell^-$?

**No, in generale.** Se $a_n=\ell$ definitivamente, i termini non stanno mai strettamente sotto $\ell$. Per una successione debolmente crescente, una volta che un termine vale $\ell$, tutti i successivi valgono $\ell$: devono essere $\geq\ell$ per monotonia e $\leq\ell$ perché $\ell$ è il supremo.

Se invece $(a_n)$ è **strettamente** crescente e limitata superiormente, allora davvero

$$
a_n\to\ell^-.
$$

*Spiegazione aggiunta:* se fosse $a_{n}=\ell$ per qualche $n$, si avrebbe $a_{n+1}>\ell$, contro il fatto che $\ell$ è un maggiorante; quindi $a_n<\ell$ per ogni $n$.

---

## 4. Il numero di Nepero $e$

### 4.1 Enunciato

Si considera la successione

$$
e_n:=\left(1+\frac1n\right)^n
\qquad\forall n\geq1.
$$

**Teorema.** La successione $(e_n)$ è debolmente crescente (anzi, strettamente) e limitata superiormente. Per il teorema sulle successioni monotone ha quindi un limite reale, che si indica con $e$: è il **[[Numero di Nepero|numero di Nepero]]**. Inoltre

$$
2<e<3,
\qquad
e=2{,}71828\ldots
$$

La dimostrazione si articola in tre fatti. In tutti gioca un ruolo la [[2026-09-24 - Funzioni, composizione e principio d’induzione#12. Disuguaglianza di Bernoulli|disuguaglianza di Bernoulli]]:

$$
(1+x)^n\geq1+nx
\qquad\forall n\in\mathbb{N},\ \forall x\geq-1.
$$

### 4.2 Fatto 1: $e_n\geq2$

Per ogni $n\geq1$, applicando Bernoulli con $x=\frac1n$:

$$
\left(1+\frac1n\right)^n\geq1+n\cdot\frac1n=2.
$$

Nella lezione questo fatto viene presentato come non necessario: una volta dimostrata la monotonia segue comunque $e_n\geq e_1=2$.

### 4.3 Fatto 2: $(e_n)$ è debolmente crescente

Basta dimostrare che $e_n\geq e_{n-1}$ per ogni $n\geq2$. Il trucco è riportare tutto a una potenza con **esponente comune $n$**:

$$
\begin{aligned}
e_n\geq e_{n-1}
&\iff\left(1+\frac1n\right)^n\geq\left(1+\frac1{n-1}\right)^{n-1}\\[4pt]
&\iff\left(\frac{n+1}{n}\right)^n\geq\left(\frac{n}{n-1}\right)^{n-1}\\[4pt]
&\iff\left(\frac{n+1}{n}\right)^n\geq\left(\frac{n}{n-1}\right)^{n}\cdot\frac{n-1}{n}\\[4pt]
&\iff\left(\frac{n+1}{n}\right)^n\left(\frac{n-1}{n}\right)^n\geq\frac{n-1}{n}\\[4pt]
&\iff\left(\frac{n^2-1}{n^2}\right)^n\geq\frac{n-1}{n}\\[4pt]
&\iff\left(1-\frac1{n^2}\right)^n\geq1-\frac1n.
\end{aligned}
$$

L’ultima disuguaglianza è proprio Bernoulli con $x=-\frac1{n^2}$, che è ammissibile perché $x\geq-1$ (qui $n\geq2$):

$$
\left(1-\frac1{n^2}\right)^n\geq1-n\cdot\frac1{n^2}=1-\frac1n.
$$

### 4.4 Fatto 3: $e_n\leq3$

**Idea (brutta copia).** Si sviluppa con il [[Binomio di Newton|binomio di Newton]]:

$$
\left(1+\frac1n\right)^n
=\sum_{k=0}^{n}\binom nk\frac1{n^k}
=1+n\cdot\frac1n+\frac{n(n-1)}{2!}\cdot\frac1{n^2}+\frac{n(n-1)(n-2)}{3!}\cdot\frac1{n^3}+\cdots
$$

In ogni termine il rapporto $\frac{n(n-1)\cdots(n-k+1)}{n^k}$ è $\leq1$, quindi

$$
e_n\leq1+1+\frac1{2!}+\frac1{3!}+\cdots+\frac1{n!}
\leq1+1+\frac12+\frac14+\frac18+\cdots+\frac1{2^{n-1}}
<1+1+1=3.
$$

**Strumenti usati.**

1. $\displaystyle\binom nk\frac1{n^k}\leq\frac1{k!}$ per ogni $1\leq k\leq n$;
2. $\displaystyle\frac1{k!}\leq\frac1{2^{k-1}}$, cioè $k!\geq2^{k-1}$ (facile induzione);
3. $\displaystyle\sum_{k=0}^{n-1}\frac1{2^k}=2-\frac1{2^{n-1}}$ (facile induzione).

**Dimostrazione (bella copia).**

$$
\begin{aligned}
e_n=\left(1+\frac1n\right)^n
&=\sum_{k=0}^{n}\binom nk\frac1{n^k}
&&\text{(binomio di Newton)}\\
&=1+\sum_{k=1}^{n}\binom nk\frac1{n^k}
&&\text{(si separa il termine }k=0)\\
&\leq1+\sum_{k=1}^{n}\frac1{k!}
&&\text{(uso 1)}\\
&\leq1+\sum_{k=1}^{n}\frac1{2^{k-1}}
&&\text{(uso 2)}\\
&=1+\sum_{k=0}^{n-1}\frac1{2^k}
&&\text{(shift degli indici)}\\
&=1+2-\frac1{2^{n-1}}<3.
&&\text{(uso 3)}
\end{aligned}
$$

### 4.5 Perché $2<e<3$ con disuguaglianze strette

Dai tre fatti segue subito $2\leq e\leq3$: il limite di una successione con termini in $[2,3]$ resta in $[2,3]$. Il fatto che $e_n<3$ per ogni $n$ **non** basta da solo a escludere $e=3$; nella lezione si osserva che basta tenersi un piccolo avanzo nelle stime abbondanti fatte sopra.

*Spiegazione aggiunta, una possibile scelta concreta:*

- per $k=3$ si ha $\frac1{3!}=\frac16<\frac14=\frac1{2^2}$, quindi per $n\geq3$ nella stima 2 si perde almeno $\frac14-\frac16=\frac1{12}$ e
  $$
  e_n\leq3-\frac1{12};
  $$
  passando al limite, $e\leq3-\frac1{12}<3$;
- dal lato opposto, $e_2=\left(\frac32\right)^2=\frac94$ e la successione è crescente, quindi $e\geq\frac94>2$.

---

## 5. Retta reale estesa

Si pone

$$
\overline{\mathbb{R}}:=\mathbb{R}\cup\{+\infty,-\infty\}.
$$

Questa è la **[[Retta reale estesa|retta reale estesa]]**.

**Prima comodità.** Scrivere $a_n\to\ell\in\overline{\mathbb{R}}$ significa che il limite esiste, finito o infinito: si esclude solo il quarto caso, quello del limite che non esiste.

**Seconda comodità.** Le quattro operazioni si estendono in modo ragionevole a $\overline{\mathbb{R}}$. Per esempio:

$$
7+\infty=+\infty,
\qquad
7-\infty=-\infty,
\qquad
+\infty+\infty=+\infty,
$$

$$
5\cdot(+\infty)=+\infty,
\qquad
-7\cdot(-\infty)=+\infty,
\qquad
\frac{18}{+\infty}=0\ \ (\text{anzi }0^+).
$$

### 5.1 Casi problematici

Non hanno un valore definito:

$$
+\infty-\infty,
\qquad
0\cdot(\pm\infty),
\qquad
\frac{\pm\infty}{\pm\infty},
\qquad
\frac00,
\qquad
\frac70.
$$

Il caso $\frac70$ diventa invece accettabile se si conosce il segno del denominatore:

$$
\frac7{0^+}=+\infty,
\qquad
\frac7{0^-}=-\infty.
$$

---

## 6. Teoremi algebrici sui limiti

### 6.1 Enunciato

I **[[Teoremi algebrici sui limiti|teoremi algebrici sui limiti]]**: siano $(a_n)$ e $(b_n)$ due successioni con

$$
a_n\to\ell_1\in\overline{\mathbb{R}},
\qquad
b_n\to\ell_2\in\overline{\mathbb{R}}.
$$

Allora

$$
a_n+b_n\to\ell_1+\ell_2,
\qquad
a_n-b_n\to\ell_1-\ell_2,
$$

$$
a_n\cdot b_n\to\ell_1\cdot\ell_2,
\qquad
\frac{a_n}{b_n}\to\frac{\ell_1}{\ell_2},
$$

**tranne nei casi problematici**, dove le operazioni sono intese in $\overline{\mathbb{R}}$.

> [!warning] Achtung! Achtung!
> Nei casi problematici, noti anche come **[[Forma indeterminata|forme indeterminate]]**, si deve intendere che il limite della somma, della differenza, ecc. **non è deducibile soltanto dai limiti dei due pezzi**. Non significa che il limite non esiste.

Esempi con la forma $+\infty-\infty$, tutti con $a_n=2n\to+\infty$:

| $b_n$ | $a_n-b_n$ | limite |
|---|---|---|
| $n$ | $n$ | $+\infty$ |
| $3n$ | $-n$ | $-\infty$ |
| $2n-42+\frac1n$ | $42-\frac1n$ | $42$ |
| $2n+(-1)^n$ | $-(-1)^n$ | non esiste |

In tutti i casi $b_n\to+\infty$, ma il comportamento della differenza cambia completamente.

### 6.2 Somma nel caso finito

**Ipotesi:** $a_n\to\ell_1\in\mathbb{R}$ e $b_n\to\ell_2\in\mathbb{R}$.
**Tesi:** $a_n+b_n\to\ell_1+\ell_2$.

**Brutta copia.** Si vuole $|(a_n+b_n)-(\ell_1+\ell_2)|\leq\varepsilon$ definitivamente. Per la disuguaglianza triangolare,

$$
|(a_n+b_n)-(\ell_1+\ell_2)|
=|(a_n-\ell_1)+(b_n-\ell_2)|
\leq|a_n-\ell_1|+|b_n-\ell_2|
\leq\frac\varepsilon2+\frac\varepsilon2=\varepsilon.
$$

**Bella copia.**

- Si fissa $\varepsilon>0$.
- Si usa la definizione di limite per $a_n$ e per $b_n$ con $\frac\varepsilon2$: esistono $n_a$, $n_b$ tali che
  $$
  |a_n-\ell_1|\leq\frac\varepsilon2\quad\forall n\geq n_a,
  \qquad
  |b_n-\ell_2|\leq\frac\varepsilon2\quad\forall n\geq n_b.
  $$
- Per ogni $n\geq\max\{n_a,n_b\}$ funziona il conto della brutta copia.

### 6.3 Somma con un termine che tende a $+\infty$

Se $a_n\to+\infty$ e $(b_n)$ è limitata inferiormente, allora

$$
a_n+b_n\to+\infty.
$$

L’ipotesi su $(b_n)$ è verificata, per esempio, se $b_n$ ha limite reale oppure se $b_n\to+\infty$ (si veda la nota precedente, §6.1–6.2). Il teorema copre quindi i casi $\ell+\infty$ e $+\infty+\infty$.

**Ipotesi:** $a_n\to+\infty$ e $b_n\geq B$ per ogni $n\in\mathbb{N}$.
**Tesi:** $a_n+b_n\to+\infty$.

**Brutta copia.** Usando direttamente $a_n\geq M$ si otterrebbe $a_n+b_n\geq M+B$, ma si vuole $a_n+b_n\geq M$. Conviene quindi applicare la definizione con una soglia spostata.

**Bella copia.**

- Si fissa $M\in\mathbb{R}$.
- Si usa la definizione di $a_n\to+\infty$ con la soglia $M-B$: esiste $n_0$ tale che
  $$
  a_n\geq M-B\qquad\forall n\geq n_0.
  $$
- Allora, per ogni $n\geq n_0$,
  $$
  a_n+b_n\geq(M-B)+B=M.
  $$

### 6.4 Prodotto nel caso finito

**Ipotesi:** $a_n\to\ell_1\in\mathbb{R}$ e $b_n\to\ell_2\in\mathbb{R}$.
**Tesi:** $a_n b_n\to\ell_1\ell_2$.

**Brutta copia.** Il trucco è aggiungere e togliere un **termine misto**:

$$
\begin{aligned}
|a_nb_n-\ell_1\ell_2|
&=|a_nb_n-a_n\ell_2+a_n\ell_2-\ell_1\ell_2|\\
&=|a_n(b_n-\ell_2)+\ell_2(a_n-\ell_1)|\\
&\leq|a_n|\cdot|b_n-\ell_2|+|\ell_2|\cdot|a_n-\ell_1|.
\end{aligned}
$$

Nel primo addendo $|b_n-\ell_2|$ è piccolo e $|a_n|$ non può essere enorme, perché $(a_n)$ è limitata; nel secondo $|\ell_2|$ è fisso e $|a_n-\ell_1|$ è piccolo. Si punta a rendere ciascun addendo $\leq\frac\varepsilon2$.

**Bella copia.**

- Si fissa $\varepsilon>0$.
- Poiché $(a_n)$ ha limite reale, è limitata: esiste $A\in\mathbb{R}$ tale che $|a_n|\leq A$ per ogni $n\in\mathbb{N}$.
- Si usa la definizione di limite per $b_n$ con $\frac{\varepsilon}{2A}$ e per $a_n$ con $\frac{\varepsilon}{2|\ell_2|}$:
  $$
  |b_n-\ell_2|\leq\frac{\varepsilon}{2A}\quad\forall n\geq n_b,
  \qquad
  |a_n-\ell_1|\leq\frac{\varepsilon}{2|\ell_2|}\quad\forall n\geq n_a.
  $$
- Per il conto della brutta copia, per ogni $n\geq\max\{n_a,n_b\}$:
  $$
  |a_nb_n-\ell_1\ell_2|
  \leq A\cdot\frac{\varepsilon}{2A}+|\ell_2|\cdot\frac{\varepsilon}{2|\ell_2|}
  =\frac\varepsilon2+\frac\varepsilon2=\varepsilon.
  $$

> [!warning] Divisione per zero
> Nella scelta precedente si potrebbe aver diviso per $0$, se $A=0$ oppure $\ell_2=0$. Per uscirne basta usare le due definizioni di limite con
> $$
> \frac{\varepsilon}{2A+25}
> \qquad\text{e}\qquad
> \frac{\varepsilon}{2|\ell_2|+37}.
> $$
> I denominatori sono strettamente positivi e il resto funziona allo stesso modo: si ottiene $|a_nb_n-\ell_1\ell_2|\leq\frac\varepsilon2+\frac\varepsilon2$ con margine.

---

## 7. Esercizi ed esempi

### 7.1 $\displaystyle\lim_{n\to+\infty}\left(n^2-n\cos n\right)=+\infty$

Così com’è, è una forma $+\infty-\infty$ con un pezzo oscillante. Si raccoglie:

$$
n^2-n\cos n=n\,(n-\cos n).
$$

Poiché $\cos n\leq1$,

$$
n-\cos n\geq n-1\to+\infty,
$$

quindi $n-\cos n\to+\infty$ per il [[2026-10-06 - Successioni, limiti e teoremi di confronto#7.1 Confronto con un limite infinito|confronto con un limite infinito]]. Il prodotto è della forma $(+\infty)\cdot(+\infty)=+\infty$.

### 7.2 $\displaystyle\lim_{n\to+\infty}\frac{n^2+3n+1}{2n^2-7}=\frac12$

> **Slogan:** chi comanda si raccoglie!

$$
\frac{n^2+3n+1}{2n^2-7}
=\frac{n^2\left(1+\frac3n+\frac1{n^2}\right)}{n^2\left(2-\frac7{n^2}\right)}
=\frac{1+\frac3n+\frac1{n^2}}{2-\frac7{n^2}}
\to\frac{1+0+0}{2-0}=\frac12,
$$

per i teoremi algebrici.

### 7.3 $\displaystyle\lim_{n\to+\infty}\frac{\sin n}{n}=0$

Più in generale,

$$
\lim_{n\to+\infty}\frac{\sin(\text{Mostro})}{n}=0,
$$

qualunque sia l’espressione “Mostro” dentro il seno. Infatti $-1\leq\sin(\text{Mostro})\leq1$ e, dividendo per $n>0$,

$$
-\frac1n\leq\frac{\sin(\text{Mostro})}{n}\leq\frac1n.
$$

Entrambi gli estremi tendono a $0$, quindi la conclusione segue dal [[2026-10-06 - Successioni, limiti e teoremi di confronto#7.2 Teorema dei carabinieri|teorema dei carabinieri]].

### 7.4 $\displaystyle\lim_{n\to+\infty}\frac{n^2+\arctan n}{n+\arctan(n^2)}=+\infty$

Si raccoglie chi comanda al numeratore e al denominatore:

$$
\frac{n^2\left(1+\dfrac{\arctan n}{n^2}\right)}{n\left(1+\dfrac{\arctan(n^2)}{n}\right)}
=n\cdot\frac{1+\dfrac{\arctan n}{n^2}}{1+\dfrac{\arctan(n^2)}{n}}.
$$

Per i due quozienti con l’arcotangente basta sapere che

$$
0\leq\arctan x\leq\frac\pi2\qquad\text{per }x\geq0:
$$

dividendo per $n^2$ (oppure per $n$) e usando i carabinieri, entrambi tendono a $0$. La frazione tende quindi a $\frac{1+0}{1+0}=1$ e il prodotto a $(+\infty)\cdot1=+\infty$.
