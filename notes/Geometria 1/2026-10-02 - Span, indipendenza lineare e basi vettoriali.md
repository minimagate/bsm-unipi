---
type: lecture-note
course: Geometria 1
date: '2026-10-02'
title: Span, indipendenza lineare e basi vettoriali
source_transcript: _transcripts/Geometria 1/2026-10-02 - Span, indipendenza lineare e basi vettoriali.md
source_hash: sha256:f2bb89bdead7999acfdbc3f52475edb66424acfa2848a3efa321570d6d7cafaf
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-02T12:18:40.871Z'
vault_path: Notes/Geometria 1/Lectures/2026-10-02 - Span, indipendenza lineare e basi vettoriali.md
vault_hash: 7fec551ec21bab04c607309f135546d7c34a00035e177fb36409c2f880c768f0
---
## 1. Combinazioni lineari e interpretazione geometrica

Siano $V$ uno [[Spazio vettoriale|spazio vettoriale]] sul campo $\mathbb{K}$ e $v_1,\dots,v_n\in V$. Una **[[Combinazione lineare|combinazione lineare]]** di questi vettori è un vettore della forma

$$
\alpha_1v_1+\alpha_2v_2+\cdots+\alpha_nv_n,
$$

dove $\alpha_1,\dots,\alpha_n\in\mathbb{K}$.

I vettori $v_1,\dots,v_n$ sono fissati; variano i coefficienti $\alpha_1,\dots,\alpha_n$. Al variare dei coefficienti si ottengono tutti i vettori esprimibili con quei vettori.

### Interpretazione geometrica nel piano

Consideriamo due vettori $v_1,v_2$ nel piano.

- Se $v_1$ e $v_2$ sono multipli l’uno dell’altro, tutte le combinazioni lineari
  $$
  \alpha_1v_1+\alpha_2v_2
  $$
  rimangono sulla retta generata da questi vettori.
- Se $v_1$ e $v_2$ non sono multipli l’uno dell’altro, ogni vettore del piano può essere ottenuto come combinazione lineare dei due.

Quindi tutto dipende dalla posizione relativa dei vettori.

### Interpretazione geometrica nello spazio

Consideriamo tre vettori $v_1,v_2,v_3$ nello spazio.

- Se i tre vettori non sono complanari, al variare di $\alpha_1,\alpha_2,\alpha_3$ si possono ottenere tutti i vettori dello spazio.
- Se invece i tre vettori stanno nello stesso piano, tutte le loro combinazioni lineari restano in quel piano: non si può uscirne.

Questi esempi motivano il concetto di spazio generato.

---

## 2. Lo span di un insieme finito di vettori

Lo **span** o **[[Sottospazio generato|sottospazio generato]]** dai vettori $v_1,\dots,v_n$ è l’insieme di tutte le loro combinazioni lineari:

$$
\operatorname{span}(v_1,\dots,v_n)
=
\left\{
\alpha_1v_1+\cdots+\alpha_nv_n
\mid
\alpha_1,\dots,\alpha_n\in\mathbb{K}
\right\}.
$$

In italiano si usa anche la notazione

$$
\operatorname{Span}(v_1,\dots,v_n)
$$

oppure

$$
\langle v_1,\dots,v_n\rangle.
$$

Le due scritture seguenti sono equivalenti:

$$
\operatorname{span}(v_1,\dots,v_n)
=
\left\{
\sum_{i=1}^n\alpha_iv_i
\mid
\alpha_i\in\mathbb{K}
\right\},
$$

e

$$
\operatorname{span}(v_1,\dots,v_n)
=
\left\{
v\in V
\mid
\exists\,\alpha_1,\dots,\alpha_n\in\mathbb{K}
\text{ tali che }
v=\sum_{i=1}^n\alpha_iv_i
\right\}.
$$

La seconda forma sottolinea che un vettore sta nello span se e solo se esistono coefficienti che lo esprimono come combinazione lineare dei vettori dati.

> [!example] Esempio
> In $\mathbb{R}^2$ il vettore $(3,5)$ sta in $\operatorname{span}((1,0),(0,1))$ perché $(3,5)=3(1,0)+5(0,1)$. Invece $(1,2)\notin\operatorname{span}((1,1))$: i multipli di $(1,1)$ hanno le due coordinate uguali.

---

## 3. Lo span è un sottospazio vettoriale

Sia

$$
W=\operatorname{span}(v_1,\dots,v_n).
$$

Dimostriamo che $W$ è un [[Sottospazio vettoriale|sottospazio vettoriale]] di $V$.

### Presenza del vettore nullo

Il vettore nullo appartiene a $W$, perché si ottiene scegliendo tutti i coefficienti uguali a zero:

$$
0v_1+\cdots+0v_n=0.
$$

Quindi

$$
0\in \operatorname{span}(v_1,\dots,v_n).
$$

### Chiusura rispetto alla somma

Siano $u,w\in W$. Per definizione dello span, esistono scalari $\alpha_1,\dots,\alpha_n$ e $\beta_1,\dots,\beta_n$ tali che

$$
u=\alpha_1v_1+\cdots+\alpha_nv_n
$$

e

$$
w=\beta_1v_1+\cdots+\beta_nv_n.
$$

Allora

$$
\begin{aligned}
u+w
&=
(\alpha_1v_1+\cdots+\alpha_nv_n)
+
(\beta_1v_1+\cdots+\beta_nv_n)\\
&=
(\alpha_1+\beta_1)v_1+\cdots+(\alpha_n+\beta_n)v_n.
\end{aligned}
$$

L’ultimo vettore è ancora una combinazione lineare di $v_1,\dots,v_n$, dunque

$$
u+w\in W.
$$

### Chiusura rispetto al prodotto per scalare

Sia $\lambda\in\mathbb{K}$ e sia

$$
u=\alpha_1v_1+\cdots+\alpha_nv_n\in W.
$$

Allora

$$
\begin{aligned}
\lambda u
&=
\lambda(\alpha_1v_1+\cdots+\alpha_nv_n)\\
&=
(\lambda\alpha_1)v_1+\cdots+(\lambda\alpha_n)v_n.
\end{aligned}
$$

Anche $\lambda u$ è quindi una combinazione lineare dei vettori dati:

$$
\lambda u\in W.
$$

Pertanto $\operatorname{span}(v_1,\dots,v_n)$ è un sottospazio vettoriale.

### Osservazione

Nella dimostrazione si usano essenzialmente:

- associatività e commutatività della somma;
- distributività del prodotto scalare rispetto alla somma;
- distributività rispetto alla somma di scalari;
- proprietà del vettore nullo.

---

## 4. Lo span di un insieme arbitrario

La definizione si generalizza a un insieme qualunque $A\subseteq V$, anche infinito.

Si definisce

$$
\operatorname{span}(A)
=
\left\{
\sum_{i=1}^n\alpha_iv_i
\mid
n\in\mathbb{N},\quad
\alpha_i\in\mathbb{K},\
v_i\in A
\right\}.
$$

In modo equivalente:

$$
\operatorname{span}(A)
=
\left\{
v\in V
\mid
\exists n\in\mathbb{N},\
\exists v_1,\dots,v_n\in A,\
\exists \alpha_1,\dots,\alpha_n\in\mathbb{K}:
v=\sum_{i=1}^n\alpha_iv_i
\right\}.
$$

### Importante: le combinazioni sono sempre finite

Anche quando $A$ è infinito, ogni elemento di $\operatorname{span}(A)$ si ottiene usando solo un numero finito di vettori di $A$.

Non si considerano somme infinite o serie del tipo

$$
\sum_{i=1}^{\infty}\alpha_iv_i.
$$

Lo span è fatto solo di combinazioni lineari finite.

In una combinazione può comparire più volte lo stesso vettore: non cambia nulla, si raccolgono i termini sommando i coefficienti. Inoltre, in un sottoinsieme finito di $A$ alcuni vettori possono essere inseriti con coefficiente nullo.

Per esempio, se

$$
v=\alpha_1v_1+\alpha_2v_2,
$$

e si vuole scrivere $v$ come combinazione di $v_1,v_2,v_3,v_4$, basta porre

$$
v=\alpha_1v_1+\alpha_2v_2+0v_3+0v_4.
$$

Per questo le diverse definizioni dello span, solo in apparenza differenti, individuano lo stesso insieme.

---

## 5. Proprietà fondamentali dello span

### Lo span contiene l’insieme di partenza

Per ogni $A\subseteq V$ vale

$$
A\subseteq \operatorname{span}(A).
$$

Infatti, se $v\in A$, allora

$$
v=1\cdot v,
$$

che è una combinazione lineare finita di vettori di $A$.

Nel caso finito:

$$
v_i
=
0v_1+\cdots+0v_{i-1}+1v_i+0v_{i+1}+\cdots+0v_n.
$$

Quindi ogni vettore $v_i$ appartiene a $\operatorname{span}(v_1,\dots,v_n)$.

### Se $W$ è un sottospazio che contiene $A$, allora contiene lo span di $A$

Se $W\leq V$ e

$$
A\subseteq W,
$$

allora

$$
\operatorname{span}(A)\subseteq W.
$$

Infatti $W$ è chiuso rispetto a somma e prodotto per scalare, quindi ogni combinazione lineare finita di elementi di $A$ sta ancora in $W$.

### Lo span come più piccolo sottospazio contenente $A$

Lo span di $A$ è il più piccolo sottospazio vettoriale di $V$ che contiene $A$.

Formalmente:

$$
\operatorname{span}(A)
=
\bigcap_{\substack{W\leq V\\ A\subseteq W}}W.
$$

Questa uguaglianza esprime due fatti:

1. $\operatorname{span}(A)$ è un sottospazio che contiene $A$;
2. ogni sottospazio che contiene $A$ contiene anche $\operatorname{span}(A)$.

La seconda proprietà è quella che garantisce la minimalità dello span.

### Span dello span

Poiché $\operatorname{span}(A)$ è già un sottospazio, ripetere lo span non aggiunge nulla:

$$
\operatorname{span}(\operatorname{span}(A))
=
\operatorname{span}(A).
$$

Infatti, una combinazione lineare di combinazioni lineari di elementi di $A$ è ancora una combinazione lineare finita di elementi di $A$.

---

## 6. Insiemi di generatori

Un sottoinsieme $A\subseteq V$ si dice un **insieme di generatori** (o sistema di generatori) di $V$ se

$$
\operatorname{span}(A)=V.
$$

In altre parole, $A$ genera $V$ se ogni vettore di $V$ è combinazione lineare di un numero finito di elementi di $A$.

Se $A=\{v_1,\dots,v_n\}$, la condizione diventa:

$$
\forall v\in V,\ \exists \alpha_1,\dots,\alpha_n\in\mathbb{K}
\quad
v=\alpha_1v_1+\cdots+\alpha_nv_n.
$$

### Interpretazione

Un sistema di generatori permette di esprimere ogni vettore dello spazio usando vettori fissati.

Per esempio, due vettori non multipli generano il piano, mentre due vettori multipli generano soltanto una retta.

Analogamente, in $\mathbb{R}^3$, tre vettori non complanari generano tutto lo spazio, mentre tre vettori complanari generano al più il piano che li contiene.

---

## 7. Esempio: lo spazio dei polinomi

Un esempio importante è lo spazio dei [[Polinomio|polinomi]] $\mathbb{K}[x]$.

I monomi

$$
1,\ x,\ x^2,\ x^3,\dots
$$

generano $\mathbb{K}[x]$, perché ogni polinomio è una combinazione lineare finita di monomi:

$$
p(x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n.
$$

I coefficienti $a_i$ possono essere nulli, ma in ogni polinomio compaiono comunque solo un numero finito di potenze di $x$.

Pertanto

$$
\mathbb{K}[x]
=
\operatorname{span}(1,x,x^2,x^3,\dots).
$$

Questo è un esempio di spazio vettoriale che possiede un insieme di generatori infinito.

### Sottospazi generati da famiglie particolari di monomi

Se si considera, ad esempio, l’insieme dei monomi di grado pari,

$$
\{1,x^2,x^4,x^6,\dots\},
$$

il suo span è l’insieme dei polinomi formati soltanto da potenze pari:

$$
a_0+a_1x^2+a_2x^4+\cdots+a_nx^{2n}.
$$

Analogamente, lo span dei monomi di grado dispari è costituito dai polinomi della forma

$$
a_0x+a_1x^3+a_2x^5+\cdots+a_nx^{2n+1}.
$$

Il punto è sempre lo stesso: ogni elemento dello span è una combinazione lineare **finita** dei monomi considerati.

---

## 8. Indipendenza lineare

Il secondo requisito per avere coordinate uniche riguarda l’unicità delle combinazioni lineari.

Siano $v_1,\dots,v_n\in V$. I vettori sono **[[Indipendenza lineare|linearmente indipendenti]]** se l’unica combinazione lineare che dà il vettore nullo è quella banale:

$$
\alpha_1v_1+\cdots+\alpha_nv_n=0
\quad\Longrightarrow\quad
\alpha_1=\cdots=\alpha_n=0.
$$

Equivalentemente, i vettori sono linearmente dipendenti se esistono scalari $\alpha_1,\dots,\alpha_n$, non tutti nulli, tali che

$$
\alpha_1v_1+\cdots+\alpha_nv_n=0.
$$

La combinazione con tutti i coefficienti nulli esiste sempre:

$$
0v_1+\cdots+0v_n=0.
$$

Questa è la **soluzione banale**. L’indipendenza lineare richiede che non ce ne siano altre.

Si può quindi scrivere:

- indipendenza lineare:
  $$
  \alpha_1v_1+\cdots+\alpha_nv_n=0
  \Longrightarrow
  \alpha_1=\cdots=\alpha_n=0;
  $$
- dipendenza lineare:
  $$
  \exists\,(\alpha_1,\dots,\alpha_n)\neq(0,\dots,0)
  \quad\text{tale che}\quad
  \alpha_1v_1+\cdots+\alpha_nv_n=0.
  $$

> [!example] Esempio
> In $\mathbb{R}^3$ i vettori $(1,0,0),(0,1,0),(1,1,0)$ sono dipendenti: $1\cdot(1,0,0)+1\cdot(0,1,0)-1\cdot(1,1,0)=0$. I primi due, da soli, sono indipendenti.

---

## 9. Indipendenza lineare e unicità dello sviluppo

L’indipendenza lineare equivale all’unicità della rappresentazione dei vettori come combinazioni lineari.

### Dall’indipendenza all’unicità

Supponiamo che $v_1,\dots,v_n$ siano linearmente indipendenti e che un vettore $v$ abbia due rappresentazioni:

$$
v=\alpha_1v_1+\cdots+\alpha_nv_n
$$

e

$$
v=\beta_1v_1+\cdots+\beta_nv_n.
$$

Sottraendo la seconda uguaglianza dalla prima:

$$
(\alpha_1v_1+\cdots+\alpha_nv_n)
-
(\beta_1v_1+\cdots+\beta_nv_n)=0.
$$

Usando l’opposto di un vettore e la distributività:

$$
(\alpha_1-\beta_1)v_1+\cdots+(\alpha_n-\beta_n)v_n=0.
$$

Per l’indipendenza lineare, tutti i coefficienti devono essere nulli:

$$
\alpha_i-\beta_i=0
\qquad\text{per ogni }i.
$$

Dunque

$$
\alpha_i=\beta_i
\qquad\text{per ogni }i.
$$

La rappresentazione è quindi unica.

### Dall’unicità all’indipendenza

Supponiamo ora che ogni vettore abbia una rappresentazione unica, e consideriamo il vettore nullo. Ha sempre la rappresentazione banale:

$$
0=0v_1+\cdots+0v_n.
$$

Se esistesse una combinazione non banale

$$
0=\alpha_1v_1+\cdots+\alpha_nv_n,
$$

avremmo due rappresentazioni diverse del vettore nullo, in contraddizione con l’unicità.

Quindi l’unica rappresentazione del vettore nullo è quella banale e i vettori sono linearmente indipendenti.

---

## 10. Casi semplici di indipendenza lineare

### Un solo vettore

Consideriamo un solo vettore $v$.

Esso è linearmente indipendente se

$$
\alpha v=0
\quad\Longrightarrow\quad
\alpha=0.
$$

- Se $v=0$, allora
  $$
  1\cdot v=1\cdot 0=0,
  $$
  e il coefficiente $1$ non è nullo. Quindi il vettore nullo è linearmente dipendente.
- Se $v\neq 0$ e $\alpha v=0$, allora $\alpha=0$. Infatti, se $\alpha\neq 0$, si può moltiplicare per $\alpha^{-1}$:
  $$
  \alpha^{-1}(\alpha v)=\alpha^{-1}0,
  $$
  da cui
  $$
  v=0,
  $$
  in contraddizione con l’ipotesi.

Pertanto:

$$
\{v\}\text{ è linearmente indipendente}
\Longleftrightarrow
v\neq 0.
$$

### Due vettori

Consideriamo $v_1,v_2$. Se sono linearmente dipendenti, esistono $\alpha_1,\alpha_2$, non entrambi nulli, tali che

$$
\alpha_1v_1+\alpha_2v_2=0.
$$

Almeno uno dei coefficienti è diverso da zero.

Se $\alpha_2\neq 0$, si può isolare $v_2$:

$$
\alpha_2v_2=-\alpha_1v_1,
$$

e moltiplicando per $\alpha_2^{-1}$ si ottiene

$$
v_2=-\alpha_2^{-1}\alpha_1v_1.
$$

Quindi $v_2$ è un multiplo di $v_1$.

Analogamente, se $\alpha_1\neq 0$, si ricava che $v_1$ è un multiplo di $v_2$.

Ne segue il criterio geometrico:

> Due vettori sono linearmente dipendenti se e solo se sono multipli l’uno dell’altro.

Nel piano, due vettori non nulli sono quindi linearmente indipendenti se e solo se non sono paralleli.

---

## 11. Un vettore appartenente allo span degli altri

Per una famiglia di vettori $v_1,\dots,v_n$, la dipendenza lineare equivale al fatto che almeno uno dei vettori sia combinazione lineare degli altri.

### Se la famiglia è dipendente, allora un vettore dipende dagli altri

Supponiamo che esista una relazione non banale

$$
\alpha_1v_1+\cdots+\alpha_nv_n=0.
$$

Poiché la relazione è non banale, esiste almeno un indice $i$ tale che $\alpha_i\neq 0$. Isolando il termine $\alpha_iv_i$:

$$
\alpha_iv_i
=
-\sum_{j\neq i}\alpha_jv_j.
$$

Moltiplicando per $\alpha_i^{-1}$:

$$
v_i
=
-\sum_{j\neq i}\alpha_i^{-1}\alpha_jv_j.
$$

Quindi $v_i$ è combinazione lineare degli altri vettori.

### Se un vettore è combinazione degli altri, la famiglia è dipendente

Supponiamo invece che

$$
v_i=\sum_{j\neq i}\beta_jv_j.
$$

Portando tutto al primo membro:

$$
-\sum_{j\neq i}\beta_jv_j+v_i=0.
$$

Questa è una combinazione lineare nulla in cui il coefficiente di $v_i$ è $1$, quindi non tutti i coefficienti sono nulli. La famiglia è dunque linearmente dipendente.

Si è quindi dimostrato:

$$
\{v_1,\dots,v_n\}
\text{ è linearmente dipendente}
$$

se e solo se

$$
\text{uno dei vettori è combinazione lineare degli altri}.
$$

---

## 12. Basi vettoriali

Una **[[Base di uno spazio vettoriale|base]]** di uno spazio vettoriale $V$ è un insieme $B\subseteq V$ che soddisfa contemporaneamente due condizioni:

1. $B$ genera $V$;
2. $B$ è linearmente indipendente.

In formule:

$$
B\text{ è una base di }V
\Longleftrightarrow
\begin{cases}
\operatorname{span}(B)=V,\\
B\text{ è linearmente indipendente}.
\end{cases}
$$

Le due condizioni hanno ruoli distinti:

- la proprietà di generazione garantisce che ogni vettore possa essere espresso tramite gli elementi della base;
- l’indipendenza lineare garantisce che tale espressione sia unica.

In sintesi, una base è un sistema di riferimento con abbastanza vettori per generare tutto lo spazio, ma nessuno di troppo.

> [!example] Esempio
> In $\mathbb{R}^2$ i vettori $(1,1)$ e $(1,-1)$ sono una base: non sono multipli l’uno dell’altro (indipendenti) e generano il piano, perché $(x,y)=\frac{x+y}{2}(1,1)+\frac{x-y}{2}(1,-1)$.

---

## 13. Coordinate rispetto a una base

Sia

$$
B=(v_1,\dots,v_n)
$$

una base di $V$. Per ogni $v\in V$, poiché $B$ genera $V$, esistono scalari $\alpha_1,\dots,\alpha_n$ tali che

$$
v=\alpha_1v_1+\cdots+\alpha_nv_n.
$$

Poiché $B$ è linearmente indipendente, questi coefficienti sono unici.

I coefficienti $\alpha_1,\dots,\alpha_n$ si chiamano le **coordinate di $v$ rispetto alla base $B$**.

Si raccolgono nel vettore colonna

$$
[v]_B
=
\begin{pmatrix}
\alpha_1\\
\vdots\\
\alpha_n
\end{pmatrix}.
$$

La notazione ricorda che le [[Coordinate rispetto a una base|coordinate]] dipendono dalla base scelta: lo stesso vettore ha coordinate diverse rispetto a basi diverse.

In particolare, la corrispondenza

$$
v\longmapsto [v]_B
$$

è biunivoca tra $V$ e $\mathbb{K}^n$ quando $B$ è una base formata da $n$ vettori.

---

## 14. La base canonica di $\mathbb{K}^n$

In $\mathbb{K}^n$ si considera la [[Base di uno spazio vettoriale|base canonica]]

$$
E=(e_1,\dots,e_n),
$$

dove

$$
e_1=
\begin{pmatrix}
1\\
0\\
\vdots\\
0
\end{pmatrix},
\quad
e_2=
\begin{pmatrix}
0\\
1\\
\vdots\\
0
\end{pmatrix},
\quad
\dots,
\quad
e_n=
\begin{pmatrix}
0\\
\vdots\\
0\\
1
\end{pmatrix}.
$$

Ogni vettore

$$
x=
\begin{pmatrix}
x_1\\
\vdots\\
x_n
\end{pmatrix}
$$

si scrive immediatamente come

$$
x=x_1e_1+\cdots+x_ne_n.
$$

Quindi i vettori $e_1,\dots,e_n$ generano $\mathbb{K}^n$.

Per dimostrare l’indipendenza lineare, supponiamo che

$$
\alpha_1e_1+\cdots+\alpha_ne_n=0.
$$

Il membro sinistro è

$$
\begin{pmatrix}
\alpha_1\\
\vdots\\
\alpha_n
\end{pmatrix},
$$

perciò deve essere uguale al vettore nullo. Ne segue:

$$
\alpha_1=\cdots=\alpha_n=0.
$$

La base canonica è quindi una base di $\mathbb{K}^n$.

Nel caso di $\mathbb{R}^2$:

$$
e_1=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
e_2=
\begin{pmatrix}
0\\
1
\end{pmatrix},
$$

e ogni vettore

$$
x=
\begin{pmatrix}
x_1\\
x_2
\end{pmatrix}
$$

si scrive come

$$
x=x_1e_1+x_2e_2.
$$

Le coordinate rispetto alla base canonica coincidono quindi con le entrate del vettore colonna.

> [!warning]
> Le coordinate non appartengono al vettore in modo assoluto: sono coordinate **rispetto a una base**. Cambiando base, cambiano in generale i coefficienti della rappresentazione.

---

## 15. Esempio di una base non canonica in $\mathbb{R}^2$

Sia

$$
B=(v_1,v_2)
$$

una coppia di vettori non paralleli. Essi formano una base di $\mathbb{R}^2$ perché:

- generano tutto il piano;
- sono linearmente indipendenti.

Ogni vettore $x\in\mathbb{R}^2$ si scrive in modo unico come

$$
x=\alpha_1v_1+\alpha_2v_2.
$$

Le coordinate di $x$ rispetto a $B$ sono

$$
[x]_B=
\begin{pmatrix}
\alpha_1\\
\alpha_2
\end{pmatrix}.
$$

Queste coordinate non coincidono in generale con le coordinate cartesiane di $x$ rispetto alla base canonica: dipendono dai vettori scelti come riferimento.

---

## 16. La base dei monomi in $\mathbb{K}[x]$

Nello spazio dei polinomi $\mathbb{K}[x]$, la famiglia

$$
(1,x,x^2,x^3,\dots)
$$

è una base.

### Generazione

Ogni polinomio $p(x)\in\mathbb{K}[x]$ è una combinazione lineare finita dei monomi:

$$
p(x)=a_0+a_1x+\cdots+a_nx^n.
$$

Quindi i monomi generano $\mathbb{K}[x]$.

### Indipendenza lineare

Supponiamo che una combinazione lineare finita dei monomi sia il polinomio nullo:

$$
a_0+a_1x+\cdots+a_nx^n=0.
$$

Un polinomio è nullo se e solo se tutti i suoi coefficienti sono nulli. Pertanto:

$$
a_0=a_1=\cdots=a_n=0.
$$

La famiglia dei monomi è linearmente indipendente.

Di conseguenza, $(1,x,x^2,\dots)$ è una base infinita di $\mathbb{K}[x]$.

### Perché non esiste una base finita costituita da generatori di $\mathbb{K}[x]$

Supponiamo di scegliere un insieme finito di polinomi $p_1,\dots,p_m$. Sia

$$
d=\max\{\deg p_1,\dots,\deg p_m\}.
$$

Ogni combinazione lineare dei polinomi $p_1,\dots,p_m$ ha grado al più $d$:

$$
\deg(\alpha_1p_1+\cdots+\alpha_mp_m)\leq d,
$$

salvo il caso del polinomio nullo.

Di conseguenza, tali polinomi non possono generare un polinomio di grado maggiore di $d$, per esempio $x^{d+1}$. Quindi nessun insieme finito di polinomi può generare tutto $\mathbb{K}[x]$.

Questo mostra concretamente che $\mathbb{K}[x]$ è uno spazio vettoriale infinito-dimensionale.

---

## 17. Relazione tra generazione, indipendenza e basi

Riassumiamo le nozioni introdotte.

- Un insieme $A$ **genera** $V$ se ogni vettore di $V$ è combinazione lineare di elementi di $A$.
- Un insieme $A$ è **linearmente indipendente** se la combinazione lineare nulla è soltanto quella banale.
- Una **base** è un insieme che genera $V$ ed è linearmente indipendente.

La generazione garantisce l’esistenza dello sviluppo:

$$
\forall v\in V,\quad v=\sum_i\alpha_iv_i.
$$

L’indipendenza garantisce l’unicità dei coefficienti:

$$
v=\sum_i\alpha_iv_i=\sum_i\beta_iv_i
\quad\Longrightarrow\quad
\alpha_i=\beta_i\ \text{per ogni }i.
$$

Quindi la base permette di associare a ogni vettore un’unica lista di coordinate.

---

## 18. Osservazioni sui sottoinsiemi e sulla dipendenza

Se un insieme di vettori è linearmente dipendente, ogni insieme più grande che lo contiene è anch’esso linearmente dipendente: la stessa relazione non banale continua a valere aggiungendo coefficienti nulli ai nuovi vettori.

Viceversa, se un insieme più grande è linearmente indipendente, ogni suo sottoinsieme è linearmente indipendente. Infatti, una relazione non banale tra i vettori del sottoinsieme sarebbe anche una relazione non banale tra tutti i vettori dell’insieme più grande.

Sono proprietà comode per riconoscere in fretta dipendenza e indipendenza in una famiglia di vettori.

---

## 19. Idea geometrica complessiva

Le definizioni formalizzano fatti geometrici già visibili in dimensione due e tre:

- un vettore non nullo genera una retta;
- due vettori non paralleli generano un piano;
- tre vettori non complanari generano lo spazio;
- aggiungere un vettore già appartenente allo span degli altri non amplia lo spazio generato;
- una base è un sistema di riferimento senza ridondanze;
- le coordinate descrivono quanto occorre di ciascun vettore della base per ottenere il vettore dato.

Le combinazioni lineari permettono di trattare allo stesso modo spazi geometrici, spazi di vettori numerici e spazi più astratti, come quello dei polinomi.
