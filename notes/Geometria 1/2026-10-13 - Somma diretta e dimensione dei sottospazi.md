---
type: lecture-note
course: Geometria 1
date: '2026-10-13'
title: Somma diretta e dimensione dei sottospazi
source_transcript: _transcripts/Geometria 1/2026-10-13 - Somma diretta e dimensione dei sottospazi.md
source_hash: sha256:831de69209097cdbd99f6ea75f28bda255cc5fd8afa97be12069403b3771a94f
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-13T12:16:41.875Z'
vault_path: Notes/Geometria 1/Lectures/2026-10-13 - Somma diretta e dimensione dei sottospazi.md
vault_hash: 2c8ebb462d59a08a90ecba0bb62e7d8df63992f70edede6c7c0987afd5a826fc
---
## 1. Dimensione e basi dei sottospazi

Sia $V$ uno [[Spazio vettoriale|spazio vettoriale]] di [[Dimensione di uno spazio vettoriale|dimensione]] finita $n$ e sia $W \subseteq V$ un [[Sottospazio vettoriale|sottospazio vettoriale]].

Un sottospazio è a sua volta uno spazio vettoriale, quindi anche $W$ ha una [[Base di uno spazio vettoriale|base]]. Inoltre ogni base di $W$ è fatta di vettori linearmente indipendenti anche in $V$: una relazione lineare tra vettori di $W$ è anche una relazione lineare in $V$.

Per il teorema di [[Completamento a una base|completamento di una base]], una base di $W$ si può estendere a una base di $V$. Se

$$
\mathcal B_W = \{w_1,\dots,w_k\}
$$

è una base di $W$, esistono vettori $v_{k+1},\dots,v_n$ tali che

$$
\mathcal B_V
=
\{w_1,\dots,w_k,v_{k+1},\dots,v_n\}
$$

è una base di $V$.

Da questo segue immediatamente che

$$
\dim W \leq \dim V.
$$

Infatti una base di $W$ non può avere più elementi di una base di $V$.

### Caso di uguaglianza

Se $\dim W=\dim V=n$, una base di $W$ contiene già $n$ vettori linearmente indipendenti in uno spazio di dimensione $n$: sono quindi una base di $V$.

In particolare, se $\mathcal B_W$ è una base di $W$ e ha lo stesso numero di elementi di una base di $V$, allora

$$
W=\operatorname{span}(\mathcal B_W)=V.
$$

Pertanto:

> Se $W$ è un sottospazio di $V$ e $\dim W=\dim V$, allora $W=V$.

---

## 2. Possibili dimensioni dei sottospazi

Se $\dim V=n$, esistono sottospazi di $V$ di ogni dimensione intera $k$ con

$$
0\leq k\leq n.
$$

Per costruirli si parte da una base di $V$:

$$
\mathcal B=\{v_1,\dots,v_n\}.
$$

Fissato $k\leq n$, si prende lo [[Sottospazio generato|span]] di $k$ vettori della base, ad esempio

$$
W_k=\operatorname{span}\{v_1,\dots,v_k\}.
$$

I vettori $v_1,\dots,v_k$ sono linearmente indipendenti e generano $W_k$, quindi sono una base di $W_k$. Di conseguenza,

$$
\dim W_k=k.
$$

Scegliendo gruppi diversi di $k$ vettori della base si ottengono, in generale, sottospazi diversi della stessa dimensione.

---

## 3. Numero massimo di vettori indipendenti e generatori

Sia $\dim V=n$.

### 3.1. Un insieme linearmente indipendente contiene al più $n$ vettori

Se $v_1,\dots,v_k$ sono linearmente indipendenti in $V$, allora

$$
k\leq n.
$$

Infatti ogni insieme linearmente indipendente si può estendere a una base di $V$, e ogni base di $V$ ha esattamente $n$ vettori: non ce ne possono essere più di $n$ indipendenti.

In particolare:

> Ogni sistema di $n+1$ vettori in uno spazio di dimensione $n$ è linearmente dipendente.

Un altro modo di vederlo: se $n+1$ vettori fossero indipendenti, potrebbero essere estesi a una base; ma una base di $V$ ha solo $n$ elementi, impossibile.

### 3.2. Un sistema di generatori contiene almeno $n$ vettori

Se $v_1,\dots,v_k$ generano $V$, allora

$$
k\geq n.
$$

Infatti ogni sistema di generatori contiene una base, e una base di $V$ ha $n$ elementi: un sistema di generatori non può avere meno di $n$ vettori.

Riassumendo:

- un insieme linearmente indipendente in $V$ ha al massimo $n$ elementi;
- un sistema di generatori di $V$ ha almeno $n$ elementi;
- una base di $V$ è contemporaneamente un insieme linearmente indipendente e un sistema di generatori, quindi ha esattamente $n$ elementi.

---

## 4. Somma di due sottospazi

Siano $U,W$ due sottospazi vettoriali di $V$.

La **[[Somma di sottospazi|somma di $U$ e $W$]]** è definita come

$$
U+W
=
\{u+w\mid u\in U,\ w\in W\}.
$$

Quindi $U+W$ è l’insieme di tutti i vettori che si ottengono sommando un vettore di $U$ e uno di $W$.

> [!example] Esempio
> In $\mathbb R^3$ sia $U=\operatorname{span}\{e_1\}$ e $W=\operatorname{span}\{e_2\}$ (due rette). Allora $U+W=\{(a,b,0)\mid a,b\in\mathbb R\}$, il piano $x_3=0$.

### 4.1. $U+W$ è un sottospazio vettoriale

Per dimostrare che $U+W$ è un sottospazio verifichiamo le proprietà fondamentali.

Siano

$$
x=u_1+w_1,\qquad y=u_2+w_2
$$

con $u_1,u_2\in U$ e $w_1,w_2\in W$. Allora

$$
x+y
=
(u_1+w_1)+(u_2+w_2)
=
(u_1+u_2)+(w_1+w_2).
$$

Poiché $U$ e $W$ sono sottospazi,

$$
u_1+u_2\in U,
\qquad
w_1+w_2\in W.
$$

Pertanto $x+y\in U+W$.

Analogamente, per ogni $\lambda\in\mathbb K$,

$$
\lambda x
=
\lambda(u_1+w_1)
=
\lambda u_1+\lambda w_1,
$$

e quindi $\lambda x\in U+W$.

Infine,

$$
0_V=0_U+0_W\in U+W.
$$

Dunque $U+W$ è un sottospazio vettoriale di $V$.

### 4.2. Interpretazione come span

La somma $U+W$ è il più piccolo sottospazio vettoriale che contiene sia $U$ sia $W$.

Infatti:

- $U\subseteq U+W$, perché ogni $u\in U$ si scrive come
  $$
  u=u+0,
  $$
  con $0\in W$;
- $W\subseteq U+W$, perché ogni $w\in W$ si scrive come
  $$
  w=0+w,
  $$
  con $0\in U$.

Se $Z$ è un sottospazio che contiene sia $U$ sia $W$, allora contiene ogni somma $u+w$, perché è chiuso rispetto alla somma. Quindi

$$
U+W\subseteq Z.
$$

Pertanto $U+W$ è il più piccolo sottospazio contenente $U\cup W$, cioè

$$
U+W=\operatorname{span}(U\cup W).
$$

Nota bene: l’unione $U\cup W$, in generale, non è un sottospazio (può non essere chiusa rispetto alla somma), mentre $U+W$ è proprio il sottospazio generato dall’unione.

---

## 5. Somma diretta

Si dice che $U+W$ è una **[[Somma diretta|somma diretta]]** se

$$
U\cap W=\{0\}.
$$

In tal caso si scrive

$$
U\oplus W.
$$

Quindi

$$
U\oplus W
\quad\Longleftrightarrow\quad
U+W\text{ e }U\cap W=\{0\}.
$$

La condizione sull’intersezione dice che l’unico vettore comune ai due sottospazi è il vettore nullo.

### 5.1. Esempi geometrici

#### Due rette in $\mathbb R^2$

Siano $U$ e $W$ due rette passanti per l’origine e distinte. La loro intersezione è

$$
U\cap W=\{0\}.
$$

Inoltre, le due rette generano tutto il piano:

$$
U+W=\mathbb R^2.
$$

Quindi

$$
\mathbb R^2=U\oplus W.
$$

#### Un piano e una retta in $\mathbb R^3$

Sia $U$ un piano passante per l’origine e $W$ una retta non contenuta nel piano. Allora

$$
U\cap W=\{0\}
$$

e

$$
U+W=\mathbb R^3.
$$

Pertanto

$$
\mathbb R^3=U\oplus W.
$$

Se invece la retta fosse contenuta nel piano, allora

$$
W\subseteq U,
$$

quindi l’intersezione non sarebbe $\{0\}$ e la somma non sarebbe diretta.

#### Due piani in $\mathbb R^3$

Due piani distinti passanti per l’origine si intersecano in una retta passante per l’origine. Di conseguenza,

$$
\dim(U\cap W)=1
$$

e quindi

$$
U\cap W\neq\{0\}.
$$

Due piani in $\mathbb R^3$ non possono quindi essere in somma diretta.

---

## 6. Caratterizzazione della somma diretta tramite l’unicità

La somma $U+W$ è diretta se e solo se ogni vettore di $U+W$ si scrive in modo unico come somma di un vettore di $U$ e di un vettore di $W$.

In formule:

$$
U\oplus W
\quad\Longleftrightarrow\quad
\forall z\in U+W,\ 
\exists!\,(u,w)\in U\times W
\text{ tali che }z=u+w.
$$

### 6.1. Se l’intersezione è nulla, la decomposizione è unica

Supponiamo che

$$
U\cap W=\{0\}.
$$

Sia $z\in U+W$ e supponiamo che abbia due decomposizioni:

$$
z=u+w=u'+w',
$$

dove $u,u'\in U$ e $w,w'\in W$.

Portando i termini di $U$ da una parte e quelli di $W$ dall’altra si ottiene

$$
u-u'=w'-w.
$$

Il vettore a sinistra sta in $U$, quello a destra in $W$. Chiamandolo $v$, si ha

$$
v\in U\cap W.
$$

Poiché l’intersezione è $\{0\}$,

$$
v=0.
$$

Dunque

$$
u-u'=0,
\qquad
w'-w=0,
$$

e quindi

$$
u=u',
\qquad
w=w'.
$$

La decomposizione è unica.

### 6.2. Se la decomposizione è unica, l’intersezione è nulla

Supponiamo ora che ogni vettore di $U+W$ abbia una decomposizione unica.

Per assurdo, supponiamo che esista un vettore non nullo

$$
v\in U\cap W,
\qquad v\neq 0.
$$

Poiché $v\in U$ e $v\in W$, possiamo scrivere

$$
v=v+0
$$

e anche

$$
v=0+v.
$$

Sono due decomposizioni diverse di $v$ come somma di un vettore di $U$ e uno di $W$, contro l’unicità.

Pertanto necessariamente

$$
U\cap W=\{0\}.
$$

---

## 7. Somma diretta generata da vettori linearmente indipendenti

Sia

$$
\mathcal B=\{v_1,\dots,v_n\}
$$

un insieme linearmente indipendente. Dividiamo $\mathcal B$ in due parti:

$$
\mathcal B_1=\{v_1,\dots,v_h\},
\qquad
\mathcal B_2=\{v_{h+1},\dots,v_n\}.
$$

Definiamo

$$
U=\operatorname{span}(\mathcal B_1),
\qquad
W=\operatorname{span}(\mathcal B_2).
$$

Allora

$$
\operatorname{span}(\mathcal B)=U\oplus W.
$$

### 7.1. La somma è $U+W$

Ogni vettore di $\operatorname{span}(\mathcal B)$ è una combinazione lineare dei vettori di $\mathcal B$:

$$
v
=
\sum_{i=1}^{n}\alpha_i v_i.
$$

Separando i primi $h$ vettori dai rimanenti,

$$
v
=
\sum_{i=1}^{h}\alpha_i v_i
+
\sum_{i=h+1}^{n}\alpha_i v_i.
$$

Il primo addendo sta in $U$, il secondo in $W$. Quindi

$$
\operatorname{span}(\mathcal B)\subseteq U+W.
$$

L’inclusione opposta è immediata, perché ogni elemento di $U+W$ è combinazione lineare dei vettori di $\mathcal B$. Pertanto

$$
\operatorname{span}(\mathcal B)=U+W.
$$

### 7.2. L’intersezione è nulla

Sia $v\in U\cap W$. Allora $v$ si scrive sia con i vettori di $\mathcal B_1$ sia con quelli di $\mathcal B_2$:

$$
v=\sum_{i=1}^{h}\alpha_i v_i
=
\sum_{i=h+1}^{n}\alpha_i v_i.
$$

Portando tutto a sinistra,

$$
\sum_{i=1}^{h}\alpha_i v_i
-
\sum_{i=h+1}^{n}\alpha_i v_i
=0.
$$

Questa è una relazione lineare tra i vettori di $\mathcal B$. Poiché $\mathcal B$ è linearmente indipendente, tutti i coefficienti devono essere nulli:

$$
\alpha_i=0
\qquad
\text{per ogni }i.
$$

Quindi $v=0$ e

$$
U\cap W=\{0\}.
$$

Ne segue che

$$
\operatorname{span}(\mathcal B)=U\oplus W.
$$

---

## 8. Dimensione della somma diretta

### Proposizione

Se

$$
U\oplus W
$$

è una somma diretta, allora

$$
\dim(U\oplus W)=\dim U+\dim W.
$$

### Dimostrazione

Siano

$$
\mathcal B_U=\{u_1,\dots,u_r\}
$$

una base di $U$ e

$$
\mathcal B_W=\{w_1,\dots,w_s\}
$$

una base di $W$.

Consideriamo l’unione

$$
\mathcal B=\mathcal B_U\cup\mathcal B_W.
$$

Poiché $U\cap W=\{0\}$, le due basi non hanno vettori in comune; inoltre il vettore nullo non sta in nessuna base, perché un insieme che lo contiene è linearmente dipendente.

#### $\mathcal B$ genera $U\oplus W$

Ogni vettore $z\in U\oplus W$ è della forma

$$
z=u+w
$$

con $u\in U$ e $w\in W$.

Poiché $\mathcal B_U$ è una base di $U$ e $\mathcal B_W$ è una base di $W$,

$$
u=\sum_{i=1}^{r}\alpha_i u_i,
\qquad
w=\sum_{j=1}^{s}\beta_j w_j.
$$

Pertanto

$$
z
=
\sum_{i=1}^{r}\alpha_i u_i
+
\sum_{j=1}^{s}\beta_j w_j,
$$

quindi $z$ è combinazione lineare dei vettori di $\mathcal B$.

#### $\mathcal B$ è linearmente indipendente

Supponiamo che

$$
\sum_{i=1}^{r}\alpha_i u_i
+
\sum_{j=1}^{s}\beta_j w_j
=0.
$$

Portando un gruppo di termini dall’altra parte,

$$
\sum_{i=1}^{r}\alpha_i u_i
=
-\sum_{j=1}^{s}\beta_j w_j.
$$

Il membro sinistro sta in $U$ e il destro in $W$: il vettore comune sta in $U\cap W$, che per ipotesi è $\{0\}$. Quindi entrambi i membri sono nulli:

$$
\sum_{i=1}^{r}\alpha_i u_i=0,
\qquad
\sum_{j=1}^{s}\beta_j w_j=0.
$$

Poiché $\mathcal B_U$ e $\mathcal B_W$ sono basi, sono linearmente indipendenti. Quindi

$$
\alpha_i=0\quad\text{per ogni }i,
\qquad
\beta_j=0\quad\text{per ogni }j.
$$

L’unione $\mathcal B$ è quindi una base di $U\oplus W$. Il suo numero di elementi è

$$
r+s=\dim U+\dim W.
$$

Pertanto

$$
\boxed{\dim(U\oplus W)=\dim U+\dim W}.
$$

---

## 9. Formula generale per la dimensione della somma

Se $U$ e $W$ non sono in somma diretta, la dimensione della somma non è semplicemente la somma delle dimensioni. Vale invece la **[[Formula di Grassmann|formula di Grassmann]]**:

$$
\boxed{
\dim(U+W)
=
\dim U+\dim W-\dim(U\cap W)
}.
$$

Il termine $\dim(U\cap W)$ corregge il doppio conteggio dei vettori che stanno in entrambi i sottospazi.

### Esempi

#### Due piani in $\mathbb R^3$

Se $U$ e $W$ sono due piani distinti in $\mathbb R^3$, allora

$$
\dim U=\dim W=2,
\qquad
\dim(U\cap W)=1.
$$

Quindi

$$
\dim(U+W)
=
2+2-1=3.
$$

Poiché $U+W$ è un sottospazio di $\mathbb R^3$ di dimensione $3$,

$$
U+W=\mathbb R^3.
$$

La somma non è diretta, perché l’intersezione ha dimensione $1$.

#### Un piano e una retta trasversale in $\mathbb R^3$

Se $U$ è un piano e $W$ una retta che interseca il piano soltanto nell’origine, allora

$$
\dim U=2,
\qquad
\dim W=1,
\qquad
\dim(U\cap W)=0.
$$

Pertanto

$$
\dim(U+W)=2+1-0=3,
$$

e

$$
\mathbb R^3=U\oplus W.
$$

#### Interpretazione geometrica

La dimensione della somma dipende dalla posizione reciproca dei sottospazi:

- se $U\cap W=\{0\}$, la somma è diretta e le dimensioni si sommano;
- se l’intersezione non è nulla, bisogna sottrarne la dimensione;
- maggiore è l’intersezione, minore è la dimensione della somma.

---

## 10. Dimostrazione della formula generale

Vogliamo dimostrare che

$$
\dim(U+W)
=
\dim U+\dim W-\dim(U\cap W).
$$

Poniamo

$$
\dim U=n,\qquad
\dim W=p,\qquad
\dim(U\cap W)=q.
$$

### 10.1. Base dell’intersezione

Sia

$$
\mathcal B_1=\{v_1,\dots,v_q\}
$$

una base di $U\cap W$.

Poiché $U\cap W\subseteq U$, possiamo estendere $\mathcal B_1$ a una base di $U$:

$$
\mathcal B_U
=
\{v_1,\dots,v_q,u_{q+1},\dots,u_n\}.
$$

Analogamente, poiché $U\cap W\subseteq W$, possiamo estendere $\mathcal B_1$ a una base di $W$:

$$
\mathcal B_W
=
\{v_1,\dots,v_q,w_{q+1},\dots,w_p\}.
$$

Consideriamo ora l’insieme

$$
\mathcal B
=
\{v_1,\dots,v_q,
u_{q+1},\dots,u_n,
w_{q+1},\dots,w_p\}.
$$

I vettori $v_1,\dots,v_q$ compaiono in entrambe le basi, ma si contano una volta sola.

Il numero di vettori di $\mathcal B$ è

$$
q+(n-q)+(p-q)=n+p-q.
$$

### 10.2. $\mathcal B$ genera $U+W$

Sia $z\in U+W$. Allora

$$
z=u+w
$$

con $u\in U$ e $w\in W$.

Poiché $\mathcal B_U$ è una base di $U$, esistono coefficienti tali che

$$
u
=
\sum_{i=1}^{q}\alpha_i v_i
+
\sum_{i=q+1}^{n}\alpha_i u_i.
$$

Analogamente, poiché $\mathcal B_W$ è una base di $W$,

$$
w
=
\sum_{i=1}^{q}\beta_i v_i
+
\sum_{j=q+1}^{p}\beta_j w_j.
$$

Sommando,

$$
z
=
\sum_{i=1}^{q}(\alpha_i+\beta_i)v_i
+
\sum_{i=q+1}^{n}\alpha_i u_i
+
\sum_{j=q+1}^{p}\beta_j w_j.
$$

Quindi $z$ è combinazione lineare dei vettori di $\mathcal B$, e dunque $\mathcal B$ genera $U+W$.

### 10.3. $\mathcal B$ è linearmente indipendente

Supponiamo che una combinazione lineare dei vettori di $\mathcal B$ sia nulla:

$$
\sum_{i=1}^{q}\gamma_i v_i
+
\sum_{i=q+1}^{n}\alpha_i u_i
+
\sum_{j=q+1}^{p}\beta_j w_j
=0.
$$

Separiamo i termini appartenenti alle due basi:

$$
\sum_{i=1}^{q}\gamma_i v_i
+
\sum_{i=q+1}^{n}\alpha_i u_i
=
-\sum_{j=q+1}^{p}\beta_j w_j.
$$

Il membro sinistro sta in $U$, il destro in $W$: il vettore comune sta quindi in $U\cap W$.

Essendo $\{v_1,\dots,v_q\}$ una base di $U\cap W$, il vettore comune si scrive in modo unico come combinazione lineare di $v_1,\dots,v_q$.

Ma il membro destro è scritto con i vettori

$$
w_{q+1},\dots,w_p.
$$

L’unicità delle coordinate nella base di $W$ implica allora che

$$
\beta_j=0
\qquad
\text{per ogni }j=q+1,\dots,p.
$$

Di conseguenza,

$$
\sum_{i=1}^{q}\gamma_i v_i
+
\sum_{i=q+1}^{n}\alpha_i u_i
=0.
$$

Poiché

$$
\{v_1,\dots,v_q,u_{q+1},\dots,u_n\}
$$

è una base di $U$, tutti i coefficienti sono nulli:

$$
\gamma_i=0
\quad\text{per ogni }i,
\qquad
\alpha_i=0
\quad\text{per ogni }i.
$$

Pertanto tutti i coefficienti della combinazione iniziale sono nulli e $\mathcal B$ è linearmente indipendente.

Quindi $\mathcal B$ è una base di $U+W$. Ne segue che

$$
\dim(U+W)=|\mathcal B|=n+p-q,
$$

cioè

$$
\boxed{
\dim(U+W)
=
\dim U+\dim W-\dim(U\cap W)
}.
$$

---

## 11. Decomposizione di matrici in parte simmetrica e antisimmetrica

Consideriamo lo spazio vettoriale delle [[Matrice|matrici]] quadrate a coefficienti reali.

### 11.1. Matrici simmetriche

Una matrice quadrata $A=(a_{ij})$ è **[[Matrice trasposta|simmetrica]]** se

$$
a_{ij}=a_{ji}
\qquad
\text{per ogni }i,j.
$$

Equivalentemente,

$$
A^T=A.
$$

Geometricamente, gli elementi simmetrici rispetto alla diagonale principale sono uguali.

Per esempio, una matrice $2\times 2$ simmetrica ha la forma

$$
A=
\begin{pmatrix}
a & b\\
b & d
\end{pmatrix}.
$$

L’insieme delle matrici simmetriche è un sottospazio vettoriale: la somma di due matrici simmetriche è simmetrica e il prodotto di una matrice simmetrica per uno scalare è ancora simmetrico.

### 11.2. Matrici antisimmetriche

Una matrice quadrata $A=(a_{ij})$ è **antisimmetrica** se

$$
a_{ij}=-a_{ji}
\qquad
\text{per ogni }i,j.
$$

Equivalentemente,

$$
A^T=-A.
$$

Nel caso reale, sulla diagonale principale vale

$$
a_{ii}=-a_{ii},
$$

da cui

$$
2a_{ii}=0
$$

e quindi

$$
a_{ii}=0.
$$

Pertanto una matrice antisimmetrica reale ha diagonale nulla.

Per esempio, una matrice antisimmetrica $2\times 2$ ha la forma

$$
A=
\begin{pmatrix}
0 & b\\
-b & 0
\end{pmatrix}.
$$

Anche l’insieme delle matrici antisimmetriche è un sottospazio vettoriale.

> Occhio alla caratteristica del campo: da $a_{ii}=-a_{ii}$ si ricava $a_{ii}=0$ solo se $2$ è invertibile nel campo (vero sui reali e sui complessi).

### 11.3. L’intersezione è nulla

Nel caso reale, una matrice simmetrica e antisimmetrica insieme soddisfa

$$
a_{ij}=a_{ji}
$$

e

$$
a_{ij}=-a_{ji}.
$$

Quindi

$$
a_{ij}=-a_{ij},
$$

da cui

$$
2a_{ij}=0
$$

e quindi

$$
a_{ij}=0
\qquad
\text{per ogni }i,j.
$$

La matrice è dunque la matrice nulla. Pertanto

$$
\mathcal S\cap\mathcal A=\{0\},
$$

dove $\mathcal S$ è il sottospazio delle matrici simmetriche e $\mathcal A$ quello delle matrici antisimmetriche.

### 11.4. Trasposta di una matrice

Se $M=(a_{ij})$ è una matrice $m\times n$, la sua **trasposta** $M^T$ è la matrice $n\times m$ definita da

$$
(M^T)_{ij}=a_{ji}.
$$

In pratica si scambiano righe e colonne.

Per esempio,

$$
M=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\quad\Longrightarrow\quad
M^T=
\begin{pmatrix}
a & c\\
b & d
\end{pmatrix}.
$$

Per le matrici quadrate valgono le caratterizzazioni:

$$
M\text{ simmetrica}
\quad\Longleftrightarrow\quad
M=M^T,
$$

e

$$
M\text{ antisimmetrica}
\quad\Longleftrightarrow\quad
M=-M^T.
$$

### 11.5. Decomposizione canonica

Per ogni matrice quadrata reale $M$,

$$
M
=
\frac{1}{2}(M+M^T)
+
\frac{1}{2}(M-M^T).
$$

La prima matrice,

$$
\frac{1}{2}(M+M^T),
$$

è simmetrica, perché

$$
\left(\frac{1}{2}(M+M^T)\right)^T
=
\frac{1}{2}(M^T+M)
=
\frac{1}{2}(M+M^T).
$$

La seconda matrice,

$$
\frac{1}{2}(M-M^T),
$$

è antisimmetrica, perché

$$
\left(\frac{1}{2}(M-M^T)\right)^T
=
\frac{1}{2}(M^T-M)
=
-\frac{1}{2}(M-M^T).
$$

Quindi ogni matrice si scrive come somma di una matrice simmetrica e di una matrice antisimmetrica:

$$
M=S+A,
$$

con

$$
S=\frac{1}{2}(M+M^T),
\qquad
A=\frac{1}{2}(M-M^T).
$$

Poiché l’intersezione tra i due sottospazi è $\{0\}$, la decomposizione è una somma diretta:

$$
\boxed{
\mathcal M_n(\mathbb R)
=
\mathcal S_n\oplus\mathcal A_n
}.
$$

L’unicità della decomposizione segue dalla caratterizzazione generale della somma diretta.

---

## 12. Osservazioni metodologiche sugli esercizi

Negli esercizi in cui si cerca una base non basta trovare dei vettori: bisogna dimostrare entrambe le proprietà:

1. i vettori generano il sottospazio;
2. i vettori sono linearmente indipendenti.

Solo dopo aver verificato entrambe si può concludere che l’insieme è una base.

In particolare, costruendo una base di un sottospazio bisogna spiegare perché ogni vettore del sottospazio è combinazione dei vettori scelti e perché una combinazione lineare nulla ha tutti i coefficienti nulli.

Infine, attenzione ai connettivi logici: usare “e” e “oppure” in modo ambiguo rende difficile capire quali siano le ipotesi e quali le conclusioni.
