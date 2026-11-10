---
type: lecture-note
course: Geometria 1
date: '2026-10-23'
title: Sistemi lineari, nucleo, immagine e rango
source_transcript: _transcripts/Geometria 1/2026-10-22 - Sistemi lineari, nucleo, immagine e rango.md
source_hash: sha256:6821682246f7941b3ece3a2f732de7860eef8090877f415a502bf181e49a696f
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-22T11:59:54.453Z'
original_date: '2026-10-22'
date_adjustment: Shifted forward one day to keep one note per course and date.
vault_path: Notes/Geometria 1/Lectures/2026-10-23 - Sistemi lineari, nucleo, immagine e rango.md
vault_hash: c9d5e1c1e285bdbb209d0d08972633bb2a230aef07ef3576535bc99111875d22
---

## Spazi supplementari

Siano $U$ e $W$ [[Sottospazio vettoriale|sottospazi vettoriali]] di uno [[Spazio vettoriale|spazio vettoriale]] $V$. Si dice che $U$ è un **[[Somma diretta|supplementare]]** di $W$ se

$$
V = U \oplus W,
$$

cioè se valgono entrambe le condizioni:

$$
V = U + W
\qquad\text{e}\qquad
U \cap W = \{0\}.
$$

La somma è quindi diretta: ogni vettore di $V$ si scrive in modo unico come somma di un vettore di $U$ e di un vettore di $W$.

Dalla [[Formula di Grassmann|formula delle dimensioni]] segue che

$$
\dim V = \dim U + \dim W.
$$

In generale il supplementare non è unico.

### Esempi

In $\mathbb{R}^2$, se $W$ è una retta per l’origine, un suo supplementare è una qualunque altra retta $U$ per l’origine, distinta da $W$. Infatti due rette vettoriali distinte hanno intersezione $\{0\}$ e somma tutto $\mathbb{R}^2$:

$$
\mathbb{R}^2 = U \oplus W.
$$

In $\mathbb{R}^3$, se $W$ è un piano per l’origine, un suo supplementare è una retta non contenuta nel piano. In questo caso:

$$
\dim W = 2,\qquad \dim U = 1,
$$

e

$$
\mathbb{R}^3 = U \oplus W.
$$

Anche qui ci sono molti supplementari diversi.

---

## Sistemi lineari e matrici

### Forma generale

Un [[Sistema lineare|sistema lineare]] in $n$ incognite e $m$ equazioni ha la forma

$$
\begin{cases}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n=b_1,\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n=b_2,\\
\vdots\\
a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n=b_m.
\end{cases}
$$

Le incognite compaiono solo al primo grado. Il caso classico di due equazioni in due incognite,

$$
\begin{cases}
ax+by=c,\\
a'x+b'y=c',
\end{cases}
$$

è un caso particolare di quello generale.

Il sistema si studia su un [[Campo|campo]] $\mathbb{K}$, per esempio $\mathbb{R}$ o $\mathbb{C}$.

### Matrice dei coefficienti e matrice completa

La **matrice dei coefficienti** è la [[Matrice|matrice]]

$$
A=(a_{ij})\in M_{m,n}(\mathbb{K}),
$$

formata dai coefficienti delle incognite:

$$
A=
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n}\\
a_{21} & a_{22} & \cdots & a_{2n}\\
\vdots & \vdots & & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}.
$$

Il vettore delle incognite è

$$
x=
\begin{pmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{pmatrix}
\in \mathbb{K}^n,
$$

mentre il vettore dei termini noti è

$$
b=
\begin{pmatrix}
b_1\\
b_2\\
\vdots\\
b_m
\end{pmatrix}
\in \mathbb{K}^m.
$$

Il sistema si scrive in forma compatta come

$$
Ax=b.
$$

La **matrice completa** si ottiene affiancando ad $A$ la colonna dei termini noti:

$$
\widetilde A=
\left(
\begin{array}{c|c}
A & b
\end{array}
\right).
$$

La scrittura matriciale raccoglie in un’unica espressione tutte le equazioni.

---

## Prodotto tra matrici e prodotto matrice-vettore

### Condizione di compatibilità

Se

$$
A\in M_{m,n}(\mathbb{K}),
\qquad
B\in M_{n,p}(\mathbb{K}),
$$

allora il [[Prodotto tra matrici|prodotto]] $AB$ è definito e appartiene a $M_{m,p}(\mathbb{K})$.

La condizione fondamentale è che le colonne della prima matrice siano tante quante le righe della seconda:

$$
\underbrace{m\times n}_{A}
\cdot
\underbrace{n\times p}_{B}
=
\underbrace{m\times p}_{AB}.
$$

L’elemento $(i,j)$ della matrice prodotto è

$$
(AB)_{ij}
=
\sum_{k=1}^{n}a_{ik}b_{kj}.
$$

Si ottiene moltiplicando la riga $i$-esima di $A$ per la colonna $j$-esima di $B$ e sommando i prodotti corrispondenti.

Il prodotto tra matrici, quando è definito, è associativo e distributivo:

$$
(AB)C=A(BC),
$$

e

$$
A(B+C)=AB+AC,
\qquad
(A+B)C=AC+BC.
$$

Occhio: in generale non è commutativo, anche quando entrambi i prodotti sono definiti:

$$
AB\neq BA.
$$

### Prodotto matrice-vettore

Nei sistemi lineari la seconda matrice è di solito una sola colonna, cioè un vettore. Se

$$
A\in M_{m,n}(\mathbb{K}),
\qquad
x\in\mathbb{K}^n,
$$

allora

$$
Ax\in\mathbb{K}^m.
$$

In coordinate:

$$
Ax=
\begin{pmatrix}
\displaystyle\sum_{j=1}^n a_{1j}x_j\\
\displaystyle\sum_{j=1}^n a_{2j}x_j\\
\vdots\\
\displaystyle\sum_{j=1}^n a_{mj}x_j
\end{pmatrix}.
$$

La componente $i$-esima di $Ax$ è

$$
(Ax)_i=\sum_{j=1}^n a_{ij}x_j.
$$

---

## Interpretazione come applicazione lineare

A ogni matrice

$$
A\in M_{m,n}(\mathbb{K})
$$

è associata una [[Funzione|applicazione]]

$$
F_A:\mathbb{K}^n\longrightarrow\mathbb{K}^m,
\qquad
F_A(x)=Ax.
$$

Questa applicazione è lineare.

### Definizione di applicazione lineare

Siano $V$ e $V'$ spazi vettoriali sullo stesso campo $\mathbb{K}$. Un’applicazione

$$
F:V\longrightarrow V'
$$

si dice **[[Applicazione lineare|lineare]]** se:

1. preserva la somma:

   $$
   F(v+v')=F(v)+F(v')
   \qquad
   \forall v,v'\in V;
   $$

2. preserva il prodotto per scalare:

   $$
   F(\alpha v)=\alpha F(v)
   \qquad
   \forall \alpha\in\mathbb{K},\ \forall v\in V.
   $$

Nota bene: la somma a sinistra è quella dello spazio di partenza, quella a destra è quella dello spazio di arrivo. Si usa lo stesso simbolo, ma sono due somme diverse.

Equivalentemente, un’applicazione lineare preserva tutte le [[Combinazione lineare|combinazioni lineari]]:

$$
F\left(\alpha_1v_1+\cdots+\alpha_rv_r\right)
=
\alpha_1F(v_1)+\cdots+\alpha_rF(v_r).
$$

Si dimostra applicando più volte le due condizioni della definizione.

### Linearità della moltiplicazione per una matrice

Per $x,y\in\mathbb{K}^n$ vale

$$
A(x+y)=Ax+Ay
$$

per la distributività del prodotto tra matrici.

Inoltre, per ogni $\alpha\in\mathbb{K}$,

$$
A(\alpha x)=\alpha(Ax).
$$

Dunque $F_A(x)=Ax$ è un’applicazione lineare.

---

## Il prodotto matrice-vettore come combinazione delle colonne

Siano $A_1,\dots,A_n\in\mathbb{K}^m$ le colonne della matrice $A$. Allora

$$
A=
\begin{pmatrix}
\vert & \vert & & \vert\\
A_1&A_2&\cdots&A_n\\
\vert & \vert & & \vert
\end{pmatrix}.
$$

Se

$$
x=
\begin{pmatrix}
x_1\\
\vdots\\
x_n
\end{pmatrix},
$$

allora

$$
Ax=x_1A_1+x_2A_2+\cdots+x_nA_n.
$$

Quindi $Ax$ è una combinazione lineare delle colonne di $A$, con coefficienti dati dalle componenti di $x$.

#### Caso $2\times 2$

Se

$$
A=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\qquad
x=
\begin{pmatrix}
x_1\\
x_2
\end{pmatrix},
$$

allora

$$
Ax=
\begin{pmatrix}
ax_1+bx_2\\
cx_1+dx_2
\end{pmatrix}.
$$

Se le colonne di $A$ sono

$$
A_1=
\begin{pmatrix}
a\\
c
\end{pmatrix},
\qquad
A_2=
\begin{pmatrix}
b\\
d
\end{pmatrix},
$$

si può riscrivere:

$$
Ax=x_1A_1+x_2A_2.
$$

Questa interpretazione è fondamentale per capire l’immagine dell’applicazione lineare associata ad $A$ e il rango della matrice.

---

## Interpretazioni geometriche delle soluzioni

Consideriamo, per esempio, un sistema in due incognite:

$$
\begin{cases}
ax_1+bx_2=c,\\
cx_1+dx_2=e.
\end{cases}
$$

### Interpretazione come intersezione di luoghi geometrici

Ogni equazione lineare in due incognite rappresenta, se non è degenere, una retta del piano. Le soluzioni del sistema sono i punti che stanno su entrambe le rette, cioè:

$$
\text{insieme delle soluzioni}
=
\text{intersezione delle rette associate alle equazioni}.
$$

A seconda della posizione delle rette, si possono avere:

- nessuna soluzione, se le rette sono parallele e distinte;
- una sola soluzione, se le rette si intersecano in un punto;
- infinite soluzioni, se le due equazioni descrivono la stessa retta.

### Interpretazione come combinazione delle colonne

La forma

$$
Ax=b
$$

e l’identità

$$
Ax=x_1A_1+\cdots+x_nA_n
$$

mostrano che risolvere il sistema vuol dire trovare coefficienti $x_1,\dots,x_n$ tali che

$$
x_1A_1+\cdots+x_nA_n=b.
$$

In altre parole, si cercano le combinazioni lineari delle colonne di $A$ che producono il vettore $b$.

Questa seconda lettura è utile perché collega direttamente i sistemi lineari a:

- immagine di un’applicazione lineare;
- [[Sottospazio generato|spazio generato]] dalle colonne;
- rango della matrice.

---

## Immagine e nucleo di un’applicazione lineare

Sia

$$
F:V\longrightarrow V'
$$

un’applicazione, anche non lineare.

### Immagine

L’**[[Immagine e controimmagine|immagine]]** di $F$ è l’insieme dei vettori dello spazio di arrivo che si ottengono applicando $F$ a qualche vettore dello spazio di partenza:

$$
\operatorname{Im}(F)
=
\{w\in V'\mid \exists v\in V:\ F(v)=w\}.
$$

Equivalentemente,

$$
\operatorname{Im}(F)=\{F(v)\mid v\in V\}.
$$

Un vettore $w\in V'$ sta nell’immagine se e solo se esiste almeno un $v\in V$ tale che

$$
F(v)=w.
$$

Nel caso dell’applicazione associata a una matrice,

$$
F_A:\mathbb{K}^n\longrightarrow\mathbb{K}^m,
\qquad
F_A(x)=Ax,
$$

si ha

$$
b\in\operatorname{Im}(F_A)
\iff
\exists x\in\mathbb{K}^n:\ Ax=b.
$$

Quindi il sistema $Ax=b$ è risolubile se e solo se

$$
b\in\operatorname{Im}(F_A).
$$

### Nucleo

Se $F$ è lineare, il **[[Nucleo|nucleo]]** di $F$ è l’insieme dei vettori dello spazio di partenza mandati nel vettore nullo dello spazio di arrivo:

$$
\ker(F)
=
\{v\in V\mid F(v)=0\}.
$$

Nel caso della matrice $A$:

$$
\ker(F_A)
=
\{x\in\mathbb{K}^n\mid Ax=0\}.
$$

Quindi il nucleo di $F_A$ coincide con le soluzioni del sistema omogeneo associato:

$$
Ax=0.
$$

---

## Nucleo e immagine sono sottospazi vettoriali

### Il nucleo

Sia $F:V\to V'$ lineare. Si dimostra che $\ker(F)$ è un sottospazio vettoriale di $V$.

#### Chiusura rispetto alla somma

Siano $u,v\in\ker(F)$. Allora

$$
F(u)=0,
\qquad
F(v)=0.
$$

Per linearità:

$$
F(u+v)=F(u)+F(v)=0+0=0.
$$

Pertanto

$$
u+v\in\ker(F).
$$

#### Chiusura rispetto al prodotto per scalare

Sia $\alpha\in\mathbb{K}$ e sia $u\in\ker(F)$. Allora

$$
F(u)=0.
$$

Per linearità:

$$
F(\alpha u)=\alpha F(u)=\alpha\cdot 0=0.
$$

Quindi

$$
\alpha u\in\ker(F).
$$

#### Presenza del vettore nullo

Resta da verificare che $0\in\ker(F)$, cioè che

$$
F(0)=0.
$$

Questo segue dalla linearità. Infatti:

$$
F(0)=F(0+0)=F(0)+F(0).
$$

Sottraendo $F(0)$ da entrambi i membri si ottiene

$$
F(0)=0.
$$

Dunque $\ker(F)$ contiene il vettore nullo ed è chiuso rispetto a somma e prodotto per scalare: è un sottospazio vettoriale.

In particolare, l’insieme delle soluzioni del sistema omogeneo

$$
Ax=0
$$

è sempre un sottospazio vettoriale di $\mathbb{K}^n$.

### L’immagine

Sia $F:V\to V'$ lineare. Anche $\operatorname{Im}(F)$ è un sottospazio vettoriale di $V'$.

#### Chiusura rispetto alla somma

Siano $w,w'\in\operatorname{Im}(F)$. Per definizione, esistono $u,u'\in V$ tali che

$$
F(u)=w,
\qquad
F(u')=w'.
$$

Allora, per linearità,

$$
w+w'
=
F(u)+F(u')
=
F(u+u').
$$

Quindi $w+w'$ appartiene ancora all’immagine:

$$
w+w'\in\operatorname{Im}(F).
$$

#### Chiusura rispetto al prodotto per scalare

Sia $\alpha\in\mathbb{K}$ e sia $w\in\operatorname{Im}(F)$. Esiste $u\in V$ tale che

$$
F(u)=w.
$$

Allora

$$
\alpha w
=
\alpha F(u)
=
F(\alpha u).
$$

Pertanto $\alpha w\in\operatorname{Im}(F)$.

Inoltre $0\in\operatorname{Im}(F)$ perché

$$
F(0)=0.
$$

Dunque $\operatorname{Im}(F)$ è un sottospazio vettoriale dello spazio di arrivo.

---

## Esempio di nucleo e immagine

Si consideri un’applicazione lineare

$$
F:\mathbb{R}^3\longrightarrow\mathbb{R}^3
$$

definita da una matrice $A$. Il nucleo si calcola risolvendo il sistema omogeneo

$$
Ax=0.
$$

Le soluzioni ottenute formano il sottospazio

$$
\ker(F)\subseteq\mathbb{R}^3.
$$

L’immagine è invece costituita da tutti i vettori ottenibili nella forma

$$
Ax,
\qquad x\in\mathbb{R}^3.
$$

Poiché $Ax$ è una combinazione lineare delle colonne di $A$, si ha:

$$
\operatorname{Im}(F)
=
\operatorname{span}\{A_1,A_2,A_3\}.
$$

Nel transcript l’esempio numerico della matrice è risultato non completamente leggibile; il punto concettuale è che il nucleo si calcola risolvendo $Ax=0$, mentre l’immagine coincide con lo spazio generato dalle colonne della matrice.

> [!example] Esempio
> Sia $A=\begin{pmatrix}1&2\\2&4\end{pmatrix}$ e $F_A:\mathbb{R}^2\to\mathbb{R}^2$. Il sistema $Ax=0$ si riduce a $x_1+2x_2=0$, quindi $\ker(F_A)=\operatorname{span}\{(-2,1)\}$. Le colonne sono $(1,2)$ e $(2,4)=2(1,2)$, quindi $\operatorname{Im}(F_A)=\operatorname{span}\{(1,2)\}$. Entrambi hanno dimensione $1$ e $1+1=2=\dim\mathbb{R}^2$.

---

## Iniettività e nucleo

### Proposizione

Sia

$$
F:V\longrightarrow V'
$$

un’applicazione lineare. Allora (vedi [[Funzione biettiva|iniettività]]):

$$
F\text{ è iniettiva}
\iff
\ker(F)=\{0\}.
$$

### Dimostrazione

#### Se $F$ è iniettiva, allora $\ker(F)=\{0\}$

Sappiamo che

$$
F(0)=0.
$$

Se $F$ è iniettiva e $v\in\ker(F)$, allora

$$
F(v)=0=F(0).
$$

Per l’iniettività segue

$$
v=0.
$$

Quindi l’unico vettore del nucleo è il vettore nullo:

$$
\ker(F)=\{0\}.
$$

#### Se $\ker(F)=\{0\}$, allora $F$ è iniettiva

Supponiamo che

$$
F(v)=F(v').
$$

Sottraendo i due membri e usando la linearità:

$$
F(v)-F(v')=0,
$$

quindi

$$
F(v-v')=0.
$$

Pertanto

$$
v-v'\in\ker(F).
$$

Per ipotesi $\ker(F)=\{0\}$, dunque

$$
v-v'=0,
$$

e quindi

$$
v=v'.
$$

Questo dimostra che $F$ è iniettiva.

---

## Sistemi omogenei e sistemi non omogenei

Consideriamo il sistema

$$
Ax=b.
$$

Indichiamo con $S$ l’insieme delle soluzioni:

$$
S=\{x\in\mathbb{K}^n\mid Ax=b\}.
$$

### Sistema omogeneo

Nel caso $b=0$ si ottiene il sistema omogeneo:

$$
Ax=0.
$$

Il suo insieme di soluzioni è

$$
S_0=\{x\in\mathbb{K}^n\mid Ax=0\}
=\ker(F_A).
$$

Poiché il nucleo è un sottospazio vettoriale, $S_0$ è un sottospazio di $\mathbb{K}^n$.

Il sistema omogeneo è sempre compatibile, perché $x=0$ è certamente una soluzione:

$$
A0=0.
$$

Il problema è quindi trovare tutte le soluzioni e, in particolare, una [[Base di uno spazio vettoriale|base]] del sottospazio $S_0$.

### Sistema non omogeneo

Se $b\neq 0$, il sistema può essere compatibile o incompatibile. È compatibile se e solo se

$$
b\in\operatorname{Im}(F_A).
$$

Infatti:

$$
b\in\operatorname{Im}(F_A)
\iff
\exists x\in\mathbb{K}^n:\ F_A(x)=b
\iff
\exists x\in\mathbb{K}^n:\ Ax=b.
$$

---

## Struttura dell’insieme delle soluzioni

Supponiamo che il sistema non omogeneo

$$
Ax=b
$$

abbia almeno una soluzione particolare $\xi$, cioè

$$
A\xi=b.
$$

Allora tutte le soluzioni si ottengono aggiungendo a $\xi$ una soluzione del sistema omogeneo.

### Prima inclusione

Sia $x_0\in S_0$, quindi

$$
Ax_0=0.
$$

Allora

$$
A(\xi+x_0)
=
A\xi+Ax_0
=
b+0
=
b.
$$

Pertanto $\xi+x_0$ è una soluzione del sistema non omogeneo.

Quindi

$$
\xi+S_0\subseteq S.
$$

### Inclusione reciproca

Sia $x\in S$ un’altra soluzione. Allora

$$
Ax=b
\qquad\text{e}\qquad
A\xi=b.
$$

Sottraendo le due uguaglianze:

$$
Ax-A\xi=0.
$$

Per linearità:

$$
A(x-\xi)=0.
$$

Dunque

$$
x-\xi\in S_0,
$$

e quindi esiste $x_0\in S_0$ tale che

$$
x=\xi+x_0.
$$

Ne segue che

$$
S\subseteq \xi+S_0.
$$

Pertanto:

$$
\boxed{S=\xi+S_0}.
$$

In forma esplicita:

$$
\boxed{
\{x\in\mathbb{K}^n\mid Ax=b\}
=
\xi+\ker(F_A)
}.
$$

Le soluzioni di un sistema compatibile formano quindi un **traslato** del sottospazio delle soluzioni del sistema omogeneo.

> [!example] Esempio
> Il sistema $x_1+x_2=2$ in $\mathbb{R}^2$ ha soluzione particolare $\xi=(2,0)$, mentre il sistema omogeneo $x_1+x_2=0$ ha $S_0=\operatorname{span}\{(1,-1)\}$. Quindi $S=\{(2,0)+t(1,-1)\}$: la retta $x_1+x_2=2$, parallela a $S_0$ ma non passante per l’origine.

### Interpretazione geometrica

Se $S_0$ è una retta vettoriale passante per l’origine, allora $S=\xi+S_0$ è una retta parallela a $S_0$, ma generalmente non passante per l’origine.

Più in generale, i traslati di sottospazi vettoriali si chiamano **sottospazi affini**; il concetto verrà ripreso più avanti nel corso.

Una conseguenza importante è:

- se il sistema omogeneo ha solo la soluzione nulla, allora il sistema non omogeneo, quando compatibile, ha un’unica soluzione;
- se il sistema omogeneo ha infinite soluzioni, allora ogni sistema non omogeneo compatibile ha infinite soluzioni, organizzate come un traslato di $S_0$.

La risoluzione pratica del sistema richiede quindi due operazioni:

1. trovare una soluzione particolare di $Ax=b$, di solito con l’[[Algoritmo di eliminazione di Gauss|algoritmo di Gauss]];
2. trovare una base dello spazio delle soluzioni di $Ax=0$.

---

## Rango di una matrice

Il **[[Rango|rango]]** della matrice $A$ è la [[Dimensione di uno spazio vettoriale|dimensione]] dello spazio generato dalle sue colonne:

$$
\operatorname{rank}(A)
=
\dim\operatorname{span}\{A_1,\dots,A_n\}.
$$

Poiché

$$
Ax=x_1A_1+\cdots+x_nA_n,
$$

l’immagine dell’applicazione lineare $F_A$ è esattamente lo spazio generato dalle colonne di $A$:

$$
\operatorname{Im}(F_A)
=
\operatorname{span}\{A_1,\dots,A_n\}.
$$

Di conseguenza:

$$
\boxed{
\operatorname{rank}(A)
=
\dim\operatorname{Im}(F_A)
}.
$$

Non è solo un’uguaglianza tra dimensioni: i due spazi sono proprio lo stesso sottospazio di $\mathbb{K}^m$.

Il rango si può quindi leggere in due modi equivalenti:

1. come dimensione dello spazio delle colonne;
2. come dimensione dell’immagine dell’applicazione $x\mapsto Ax$.

---

## Teorema della dimensione: formula rango-nucleo

### Enunciato

Sia

$$
F:V\longrightarrow V'
$$

un’applicazione lineare, con $V$ di dimensione finita. Allora:

$$
\boxed{
\dim V
=
\dim\ker(F)
+
\dim\operatorname{Im}(F)
}.
$$

Questa relazione si chiama **formula delle dimensioni**, o **[[Teorema rango-nullità|teorema rango-nucleo]]**.

La dimensione dello spazio di partenza si spezza quindi in due contributi:

- la dimensione del nucleo;
- la dimensione dell’immagine.

### Dimostrazione

Sia

$$
\{v_1,\dots,v_k\}
$$

una base di $\ker(F)$.

Poiché questo insieme è linearmente indipendente in $V$, lo si può [[Completamento a una base|estendere a una base]] di $V$:

$$
\mathcal{B}
=
\{v_1,\dots,v_k,v_{k+1},\dots,v_n\}.
$$

Pertanto

$$
\dim V=n.
$$

I primi $k$ vettori vengono mandati nel vettore nullo:

$$
F(v_1)=\cdots=F(v_k)=0.
$$

Consideriamo i vettori del codominio

$$
w_{k+1}=F(v_{k+1}),\quad\dots,\quad w_n=F(v_n).
$$

Dimostriamo che

$$
\{w_{k+1},\dots,w_n\}
$$

è una base di $\operatorname{Im}(F)$.

#### Generazione dell’immagine

Sia $w\in\operatorname{Im}(F)$. Per definizione di immagine, esiste $v\in V$ tale che

$$
F(v)=w.
$$

Poiché $\mathcal{B}$ è una base di $V$, esistono scalari $\alpha_1,\dots,\alpha_n$ tali che

$$
v=\alpha_1v_1+\cdots+\alpha_kv_k
+\alpha_{k+1}v_{k+1}+\cdots+\alpha_nv_n.
$$

Applicando $F$ e usando la linearità:

$$
\begin{aligned}
w=F(v)
&=
\alpha_1F(v_1)+\cdots+\alpha_kF(v_k)\\
&\quad+\alpha_{k+1}F(v_{k+1})+\cdots+\alpha_nF(v_n).
\end{aligned}
$$

I primi $k$ termini sono nulli perché $v_1,\dots,v_k\in\ker(F)$. Quindi:

$$
w
=
\alpha_{k+1}w_{k+1}
+\cdots+
\alpha_nw_n.
$$

Pertanto i vettori $w_{k+1},\dots,w_n$ generano $\operatorname{Im}(F)$.

#### Indipendenza lineare

Supponiamo che

$$
\alpha_{k+1}w_{k+1}
+\cdots+
\alpha_nw_n=0.
$$

Sostituendo $w_i=F(v_i)$:

$$
\alpha_{k+1}F(v_{k+1})
+\cdots+
\alpha_nF(v_n)=0.
$$

Per linearità:

$$
F\left(
\alpha_{k+1}v_{k+1}
+\cdots+
\alpha_nv_n
\right)=0.
$$

Quindi il vettore

$$
u=
\alpha_{k+1}v_{k+1}
+\cdots+
\alpha_nv_n
$$

appartiene al nucleo di $F$. Essendo $\{v_1,\dots,v_k\}$ una base del nucleo, esistono scalari $\beta_1,\dots,\beta_k$ tali che

$$
u=\beta_1v_1+\cdots+\beta_kv_k.
$$

Pertanto:

$$
\beta_1v_1+\cdots+\beta_kv_k
-\alpha_{k+1}v_{k+1}
-\cdots-
\alpha_nv_n=0.
$$

Questa è una relazione lineare tra i vettori della base $\mathcal{B}$ di $V$. Poiché $\mathcal{B}$ è [[Indipendenza lineare|linearmente indipendente]], tutti i coefficienti sono nulli. In particolare:

$$
\alpha_{k+1}=\cdots=\alpha_n=0.
$$

Quindi $\{w_{k+1},\dots,w_n\}$ è linearmente indipendente.

Abbiamo quindi dimostrato che è una base dell’immagine. Ha $n-k$ elementi, dunque:

$$
\dim\operatorname{Im}(F)=n-k.
$$

Poiché

$$
k=\dim\ker(F),
\qquad
n=\dim V,
$$

si ottiene:

$$
\dim\ker(F)+\dim\operatorname{Im}(F)
=
k+(n-k)
=
n
=
\dim V.
$$

---

## Conseguenza per i sistemi omogenei

Sia

$$
A\in M_{m,n}(\mathbb{K})
$$

e sia $F_A:\mathbb{K}^n\to\mathbb{K}^m$ l’applicazione $F_A(x)=Ax$.

Il sistema omogeneo ha insieme di soluzioni

$$
S_0=\{x\in\mathbb{K}^n\mid Ax=0\}
=\ker(F_A).
$$

Applicando la formula rango-nucleo:

$$
\dim\ker(F_A)
+
\dim\operatorname{Im}(F_A)
=
\dim\mathbb{K}^n=n.
$$

Poiché

$$
\dim\operatorname{Im}(F_A)=\operatorname{rank}(A),
$$

si ottiene:

$$
\boxed{
\dim S_0
=
n-\operatorname{rank}(A)
}.
$$

Questa formula dà il numero di parametri da cui dipendono le soluzioni del sistema omogeneo.

In particolare:

- se $\operatorname{rank}(A)=n$, allora

  $$
  \dim S_0=0,
  $$

  quindi

  $$
  S_0=\{0\};
  $$

- se $\operatorname{rank}(A)<n$, allora

  $$
  \dim S_0>0,
  $$

  quindi il sistema omogeneo ha soluzioni non nulle. Se il campo $K$ è infinito, le soluzioni sono infinite; se $K$ ha $q$ elementi, le soluzioni sono esattamente $q^{n-\operatorname{rank}(A)}$.

Il rango si calcola in pratica con la riduzione di Gauss: nella forma a scala coincide con il numero di righe non nulle. Useremo questo metodo sia per il rango sia per le soluzioni dei sistemi lineari.
