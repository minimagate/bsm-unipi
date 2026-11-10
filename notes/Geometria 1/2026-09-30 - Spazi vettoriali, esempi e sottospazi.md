---
type: lecture-note
course: Geometria 1
date: '2026-09-30'
title: Spazi vettoriali, esempi e sottospazi
source_transcript: _transcripts/Geometria 1/2026-09-30 - Spazi vettoriali, esempi e sottospazi.md
source_hash: sha256:ee96d8a5fb7e614e3fbbe9f6d2e9d60d2c46086915b110f586dc29623b788533
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-30T06:56:37.331Z'
vault_path: Notes/Geometria 1/Lectures/2026-09-30 - Spazi vettoriali, esempi e sottospazi.md
vault_hash: c970ce67875bed1642644f0cc283b124b40a7b23107f3e70b234edb65ae1c655
---
*Geometria 1 — 30 settembre 2026*

## 1. Idea generale di spazio vettoriale

Uno [[Spazio vettoriale|spazio vettoriale]] è un insieme di oggetti su cui sono definite due operazioni:

1. una **somma di vettori**;
2. un **prodotto esterno** o **moltiplicazione per scalare**.

Gli scalari appartengono a un [[Campo|campo]] $K$. Gli elementi dello spazio vettoriale si chiamano **vettori**, anche quando non sono frecce geometriche.

L’idea è studiare gli oggetti non per la loro natura concreta, ma per le proprietà algebriche che soddisfano. Così insiemi molto diversi — vettori geometrici, tuple di numeri, polinomi, funzioni — hanno la stessa struttura e si trattano con le stesse regole.

Si parla di **spazio vettoriale su $K$** quando le operazioni sull’insieme verificano gli assiomi richiesti rispetto al campo $K$.

---

## 2. I vettori geometrici nel piano

Un primo esempio sono i vettori geometrici del piano.

La somma di due vettori geometrici si definisce con la **regola del parallelogramma**: dati $\mathbf{u}$ e $\mathbf{v}$ applicati allo stesso punto, si costruisce il parallelogramma che ha quei vettori come lati; la diagonale che parte dal punto iniziale è il vettore somma

$$
\mathbf{u}+\mathbf{v}.
$$

Il prodotto esterno consiste nel moltiplicare un vettore per uno scalare $\alpha$, tipicamente un numero reale:

$$
\alpha \mathbf{u}.
$$

Geometricamente:

- se $\alpha>0$, il vettore $\alpha\mathbf{u}$ ha la stessa direzione e lo stesso verso di $\mathbf{u}$;
- la sua lunghezza è $|\alpha|$ volte quella di $\mathbf{u}$;
- se $\alpha<0$, il verso viene invertito;
- se $\alpha=0$, si ottiene il vettore nullo.

Per dimostrare che i vettori geometrici del piano formano uno spazio vettoriale bisognerebbe verificare tutti gli assiomi. Alcune proprietà sono intuitive dalla figura, ma vanno comunque giustificate.

Per esempio, l’associatività della somma

$$
(\mathbf{u}+\mathbf{v})+\mathbf{w}
=
\mathbf{u}+(\mathbf{v}+\mathbf{w})
$$

si può leggere geometricamente osservando che le due costruzioni portano alla stessa diagonale del parallelepipedo, o nel piano alla stessa risultante ottenuta traslando opportunamente i vettori. La verifica rigorosa, però, dipende dalle definizioni adottate.

---

## 3. L’esempio fondamentale $K^n$

Sia $K$ un campo. L’insieme

$$
K^n=\{(x_1,\dots,x_n)\mid x_i\in K\}
$$

è l’insieme delle $n$-[[Spazio K^n|uple ordinate]] di elementi di $K$.

I casi più importanti sono:

$$
\mathbb{R}^n
\qquad\text{e}\qquad
\mathbb{C}^n.
$$

Gli elementi di $K^n$ vengono scritti come

$$
\mathbf{x}=(x_1,\dots,x_n),
\qquad
\mathbf{y}=(y_1,\dots,y_n).
$$

### 3.1 Somma termine a termine

La somma si definisce componente per componente:

$$
\mathbf{x}+\mathbf{y}
=
(x_1+y_1,\dots,x_n+y_n).
$$

Questa è una nuova operazione definita sull’insieme $K^n$:

$$
+ : K^n\times K^n\longrightarrow K^n.
$$

Occhio a distinguere:

- la somma tra vettori, che è l’operazione appena definita su $K^n$;
- la somma tra scalari, che è l’operazione già presente nel campo $K$.

La somma dei vettori è costruita con la somma del campo, ma non è la stessa operazione.

### 3.2 Prodotto esterno

Dato $\alpha\in K$ e $\mathbf{x}\in K^n$, si definisce

$$
\alpha\mathbf{x}
=
(\alpha x_1,\dots,\alpha x_n).
$$

Il risultato è ancora un elemento di $K^n$. Il prodotto esterno è quindi un’applicazione

$$
K\times K^n\longrightarrow K^n.
$$

Anche qui vanno distinti:

- il prodotto di due scalari, come $\alpha\beta$, che è un’operazione nel campo $K$;
- il prodotto esterno $\alpha\mathbf{x}$, che moltiplica uno scalare per un vettore.

---

## 4. Assiomi di spazio vettoriale

Sia $V$ un insieme, sia $K$ un campo e siano definite:

$$
+:V\times V\to V
$$

e

$$
\cdot:K\times V\to V.
$$

L’insieme $V$ è uno spazio vettoriale su $K$ se valgono i seguenti assiomi.

### 4.1 Assiomi relativi alla somma

Per ogni $\mathbf{u},\mathbf{v},\mathbf{w}\in V$:

1. **Chiusura della somma**

   $$
   \mathbf{u}+\mathbf{v}\in V.
   $$

2. **Associatività**

   $$
   (\mathbf{u}+\mathbf{v})+\mathbf{w}
   =
   \mathbf{u}+(\mathbf{v}+\mathbf{w}).
   $$

3. **Commutatività**

   $$
   \mathbf{u}+\mathbf{v}
   =
   \mathbf{v}+\mathbf{u}.
   $$

4. **Esistenza del vettore nullo**

   Esiste un elemento $\mathbf{0}\in V$ tale che

   $$
   \mathbf{u}+\mathbf{0}
   =
   \mathbf{0}+\mathbf{u}
   =
   \mathbf{u}.
   $$

5. **Esistenza dell’opposto**

   Per ogni $\mathbf{u}\in V$ esiste un vettore $-\mathbf{u}\in V$ tale che

   $$
   \mathbf{u}+(-\mathbf{u})
   =
   (-\mathbf{u})+\mathbf{u}
   =
   \mathbf{0}.
   $$

Questi assiomi dicono che $V$, rispetto alla somma, è un **[[Gruppo|gruppo abeliano]]**, cioè un gruppo commutativo.

### 4.2 Assiomi relativi al prodotto esterno

Per ogni $\alpha,\beta\in K$ e $\mathbf{u},\mathbf{v}\in V$ devono valere:

1. **Distributività rispetto alla somma degli scalari**

   $$
   (\alpha+\beta)\mathbf{u}
   =
   \alpha\mathbf{u}+\beta\mathbf{u}.
   $$

2. **Distributività rispetto alla somma dei vettori**

   $$
   \alpha(\mathbf{u}+\mathbf{v})
   =
   \alpha\mathbf{u}+\alpha\mathbf{v}.
   $$

3. **Compatibilità con il prodotto nel campo**

   $$
   (\alpha\beta)\mathbf{u}
   =
   \alpha(\beta\mathbf{u}).
   $$

   Nel membro $\alpha\beta$ si usa il prodotto del campo $K$, mentre negli altri membri si usa il prodotto esterno.

4. **Azione dell’unità del campo**

   Se $1_K$ è l’elemento neutro moltiplicativo di $K$, allora

   $$
   1_K\mathbf{u}=\mathbf{u}.
   $$

Per $\mathbb{R}$ o $\mathbb{C}$, $1_K$ è il numero $1$; in un campo qualsiasi è l’unità di quel campo.

---

## 5. Verifica degli assiomi in $K^n$

Le proprietà di $K^n$ si dimostrano direttamente da quelle degli elementi di $K$.

### 5.1 Associatività della somma

Siano

$$
\mathbf{x}=(x_1,\dots,x_n),\quad
\mathbf{y}=(y_1,\dots,y_n),\quad
\mathbf{z}=(z_1,\dots,z_n).
$$

Per definizione,

$$
\mathbf{x}+\mathbf{y}
=
(x_1+y_1,\dots,x_n+y_n).
$$

Pertanto,

$$
(\mathbf{x}+\mathbf{y})+\mathbf{z}
=
\bigl((x_1+y_1)+z_1,\dots,(x_n+y_n)+z_n\bigr).
$$

Usando l’associatività della somma in $K$,

$$
(x_i+y_i)+z_i
=
x_i+(y_i+z_i)
\qquad
\text{per ogni }i.
$$

Quindi

$$
(\mathbf{x}+\mathbf{y})+\mathbf{z}
=
\bigl(x_1+(y_1+z_1),\dots,x_n+(y_n+z_n)\bigr)
=
\mathbf{x}+(\mathbf{y}+\mathbf{z}).
$$

Ogni passaggio va giustificato: prima si applica la definizione di somma tra $n$-uple, poi l’associatività della somma nel campo $K$.

Le altre proprietà additive si verificano analogamente, componente per componente.

### 5.2 Vettore nullo

Il vettore nullo di $K^n$ è

$$
\mathbf{0}=(0,\dots,0).
$$

Infatti,

$$
\mathbf{x}+\mathbf{0}
=
(x_1+0,\dots,x_n+0)
=
(x_1,\dots,x_n)
=
\mathbf{x}.
$$

Nel caso dei vettori geometrici, il vettore nullo ha lunghezza $0$ e non possiede una direzione definita.

### 5.3 Opposto

Se

$$
\mathbf{x}=(x_1,\dots,x_n),
$$

il suo opposto è

$$
-\mathbf{x}=(-x_1,\dots,-x_n),
$$

dove $-x_i$ indica l’opposto di $x_i$ nel campo $K$.

Infatti,

$$
\mathbf{x}+(-\mathbf{x})
=
(x_1-x_1,\dots,x_n-x_n)
=
(0,\dots,0).
$$

Quando $K=\mathbb{R}$, $-x_i$ è il normale opposto reale; in un campo arbitrario significa semplicemente l’opposto rispetto alla somma del campo.

### 5.4 Distributività

Per esempio, siano $\alpha,\beta\in K$ e $\mathbf{x}=(x_1,\dots,x_n)$. Allora

$$
(\alpha+\beta)\mathbf{x}
=
\bigl((\alpha+\beta)x_1,\dots,(\alpha+\beta)x_n\bigr).
$$

Usando la distributività nel campo $K$,

$$
(\alpha+\beta)x_i
=
\alpha x_i+\beta x_i.
$$

Quindi

$$
(\alpha+\beta)\mathbf{x}
=
(\alpha x_1+\beta x_1,\dots,\alpha x_n+\beta x_n)
=
\alpha\mathbf{x}+\beta\mathbf{x}.
$$

La distributività rispetto alla somma di vettori si verifica allo stesso modo:

$$
\alpha(\mathbf{x}+\mathbf{y})
=
\alpha(x_1+y_1,\dots,x_n+y_n)
$$

$$
=
\bigl(\alpha(x_1+y_1),\dots,\alpha(x_n+y_n)\bigr)
$$

$$
=
(\alpha x_1+\alpha y_1,\dots,\alpha x_n+\alpha y_n)
=
\alpha\mathbf{x}+\alpha\mathbf{y}.
$$

---

## 6. Proprietà derivate dagli assiomi

Alcune proprietà che si usano spesso non sono assiomi a sé, ma si dimostrano dagli assiomi dello spazio vettoriale.

### 6.1 Il prodotto per lo scalare nullo

Per ogni $\mathbf{v}\in V$ vale

$$
0_K\mathbf{v}=\mathbf{0}.
$$

Dimostrazione:

$$
0_K\mathbf{v}
=
(0_K+0_K)\mathbf{v}
=
0_K\mathbf{v}+0_K\mathbf{v}.
$$

Sommiamo a entrambi i membri l’opposto di $0_K\mathbf{v}$:

$$
\mathbf{0}=0_K\mathbf{v}.
$$

Quindi

$$
0_K\mathbf{v}=\mathbf{0}.
$$

### 6.2 Il prodotto di uno scalare per il vettore nullo

Per ogni $\alpha\in K$ vale

$$
\alpha\mathbf{0}=\mathbf{0}.
$$

Infatti,

$$
\alpha\mathbf{0}
=
\alpha(\mathbf{0}+\mathbf{0})
=
\alpha\mathbf{0}+\alpha\mathbf{0}.
$$

Sottraendo $\alpha\mathbf{0}$ da entrambi i membri si ottiene

$$
\alpha\mathbf{0}=\mathbf{0}.
$$

### 6.3 Opposto di un vettore

Il vettore $(-1_K)\mathbf{v}$ è l’opposto di $\mathbf{v}$:

$$
\mathbf{v}+(-1_K)\mathbf{v}
=
1_K\mathbf{v}+(-1_K)\mathbf{v}
=
(1_K-1_K)\mathbf{v}
=
0_K\mathbf{v}
=
\mathbf{0}.
$$

Pertanto,

$$
-\mathbf{v}=(-1_K)\mathbf{v}.
$$

---

## 7. Polinomi a coefficienti in un campo

Sia $K$ un campo. L’insieme $K[x]$ dei [[Polinomio|polinomi]] nella variabile formale $x$ a coefficienti in $K$ è fatto di espressioni del tipo

$$
p(x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n,
\qquad
a_i\in K.
$$

Qui i polinomi sono **espressioni formali**, non necessariamente funzioni: la variabile $x$ è solo un simbolo.

Il grado di un polinomio non nullo è il massimo esponente $k$ per cui il coefficiente di $x^k$ è diverso da zero:

$$
\deg p
=
\max\{k\mid a_k\neq 0\}.
$$

Per esempio,

$$
p(x)=3x^5-2x^2+1
$$

ha grado $5$.

### 7.1 Somma di polinomi

La somma si definisce sommando i coefficienti delle stesse potenze di $x$:

$$
\left(\sum_{i=0}^n a_i x^i\right)
+
\left(\sum_{i=0}^n b_i x^i\right)
=
\sum_{i=0}^n (a_i+b_i)x^i.
$$

I termini dello stesso grado si raccolgono. Se il coefficiente di una potenza diventa zero, quel termine scompare.

Per esempio, se

$$
p(x)=3x^5+2x^3+\cdots
$$

e

$$
q(x)=-3x^5+5x^3+\cdots,
$$

il termine di grado $5$ si cancella nella somma:

$$
3x^5+(-3x^5)=0.
$$

Di conseguenza il grado della somma può diminuire. In generale,

$$
\deg(p+q)\leq \max\{\deg p,\deg q\}.
$$

L’uguaglianza non vale sempre, perché i termini di grado massimo possono cancellarsi.

### 7.2 Prodotto esterno sui polinomi

Dato $\alpha\in K$ e

$$
p(x)=a_0+a_1x+\cdots+a_nx^n,
$$

si definisce

$$
\alpha p(x)
=
\alpha a_0+\alpha a_1x+\cdots+\alpha a_nx^n.
$$

Lo scalare moltiplica tutti i coefficienti del polinomio.

Con queste operazioni $K[x]$ è uno spazio vettoriale su $K$: la verifica degli assiomi si riduce alle proprietà delle operazioni in $K$.

Il polinomio nullo è

$$
0(x)=0+0x+0x^2+\cdots,
$$

cioè il polinomio avente tutti i coefficienti uguali a zero.

### 7.3 Polinomi di grado esattamente $n$

L’insieme dei polinomi di grado esattamente uguale a $n$ non è, in generale, uno spazio vettoriale.

Il problema è la chiusura rispetto alla somma: due polinomi di grado $n$ possono avere coefficienti dominanti opposti, e allora la somma ha grado minore di $n$. Inoltre il polinomio nullo non ha grado esattamente $n$, quindi non sta nell’insieme.

### 7.4 Polinomi di grado al più $n$

Si considera allora

$$
K_n[x]
=
\{p(x)\in K[x]\mid \deg p\leq n\},
$$

dove si include anche il polinomio nullo.

Equivalentemente,

$$
K_n[x]
=
\left\{
a_0+a_1x+\cdots+a_nx^n
\mid
a_i\in K
\right\}.
$$

Questo insieme è uno spazio vettoriale su $K$:

- la somma di due polinomi di grado al più $n$ ha ancora grado al più $n$;
- il prodotto per uno scalare non aumenta il grado;
- il polinomio nullo appartiene all’insieme;
- le altre proprietà sono ereditate da $K[x]$.

In particolare, $K_n[x]$ è un sottospazio vettoriale di $K[x]$.

---

## 8. Spazio vettoriale delle funzioni

Un altro esempio importante è l’insieme delle funzioni a valori reali. Sia $X$ un insieme e consideriamo

$$
\mathcal{F}(X,\mathbb{R})
=
\{f\mid f:X\to\mathbb{R}\}.
$$

Gli elementi dello spazio sono funzioni, trattate come vettori.

### 8.1 Somma di funzioni

Date $f,g\in\mathcal{F}(X,\mathbb{R})$, la somma si definisce punto per punto:

$$
(f+g)(x)=f(x)+g(x)
\qquad
\text{per ogni }x\in X.
$$

Il membro destro è una somma di numeri reali.

### 8.2 Prodotto per scalare

Dato $\alpha\in\mathbb{R}$ e $f\in\mathcal{F}(X,\mathbb{R})$, si definisce

$$
(\alpha f)(x)=\alpha f(x)
\qquad
\text{per ogni }x\in X.
$$

Anche in questo caso il membro destro è il prodotto di due numeri reali.

Le proprietà seguono da quelle dei valori reali. Per esempio,

$$
((f+g)+h)(x)
=
(f(x)+g(x))+h(x)
$$

e, per l’associatività della somma in $\mathbb{R}$,

$$
(f(x)+g(x))+h(x)
=
f(x)+(g(x)+h(x))
=
(f+(g+h))(x).
$$

Poiché le due funzioni assumono lo stesso valore per ogni $x$, sono uguali:

$$
(f+g)+h=f+(g+h).
$$

Il vettore nullo è la funzione nulla

$$
0(x)=0
\qquad
\text{per ogni }x\in X,
$$

e l’opposto di $f$ è la funzione $-f$ definita da

$$
(-f)(x)=-f(x).
$$

Pertanto $\mathcal{F}(X,\mathbb{R})$ è uno spazio vettoriale su $\mathbb{R}$.

---

## 9. Sottospazi vettoriali

### 9.1 Definizione

Sia $V$ uno spazio vettoriale su $K$. Un [[Sottoinsieme|sottoinsieme]] $W\subseteq V$ si dice **[[Sottospazio vettoriale|sottospazio vettoriale]]** di $V$ se, con le stesse operazioni di $V$, $W$ è a sua volta uno spazio vettoriale su $K$.

Somma e prodotto esterno in $W$ sono quindi le restrizioni di quelle di $V$:

- se $\mathbf{u},\mathbf{v}\in W$, la somma in $W$ è la stessa somma calcolata in $V$;
- se $\alpha\in K$ e $\mathbf{u}\in W$, il prodotto $\alpha\mathbf{u}$ è quello già definito in $V$.

Non si introducono operazioni nuove.

### 9.2 Criterio di sottospazio

Un sottoinsieme $W\subseteq V$ è un sottospazio vettoriale se e solo se:

1. $W\neq\varnothing$;
2. per ogni $\mathbf{u},\mathbf{v}\in W$,

   $$
   \mathbf{u}+\mathbf{v}\in W;
   $$

3. per ogni $\alpha\in K$ e $\mathbf{u}\in W$,

   $$
   \alpha\mathbf{u}\in W.
   $$

Spesso si usa la versione equivalente:

- $\mathbf{0}\in W$;
- $W$ è chiuso rispetto alla somma;
- $W$ è chiuso rispetto al prodotto per scalare.

Un criterio ancora più compatto è la chiusura rispetto alle [[Combinazione lineare|combinazioni lineari]]:

$$
\forall \mathbf{u},\mathbf{v}\in W,\ \forall \alpha,\beta\in K,
\qquad
\alpha\mathbf{u}+\beta\mathbf{v}\in W.
$$

Infatti questa proprietà implica sia la chiusura rispetto alla somma (con $\alpha=\beta=1$), sia quella rispetto al prodotto per scalare (con uno dei coefficienti uguale a zero).

> [!example] Esempio
> $W=\{(x,y)\in\mathbb{R}^2\mid x+y=0\}$ è un sottospazio di $\mathbb{R}^2$: contiene $(0,0)$; se $(x,y)$ e $(x',y')$ stanno in $W$, allora $(x+x')+(y+y')=0$; e $\alpha x+\alpha y=\alpha(x+y)=0$. Invece $\{(x,y)\mid x+y=1\}$ non lo è, perché non contiene $(0,0)$.

### 9.3 Perché il vettore nullo è necessario

Se $W$ è un sottospazio e contiene un vettore $\mathbf{v}$, allora deve contenere anche

$$
0_K\mathbf{v}=\mathbf{0}.
$$

Quindi ogni sottospazio non vuoto contiene necessariamente il vettore nullo.

Ecco perché un insieme che non contiene $\mathbf{0}$ non può essere un sottospazio vettoriale.

---

## 10. Esempi geometrici di sottospazi

### 10.1 Una retta passante per l’origine

In $\mathbb{R}^2$, l’insieme

$$
W=\{t\mathbf{v}\mid t\in\mathbb{R}\},
$$

dove $\mathbf{v}\neq\mathbf{0}$, è la retta passante per l’origine avente direzione $\mathbf{v}$.

Se $s\mathbf{v}$ e $t\mathbf{v}$ appartengono a $W$, allora

$$
s\mathbf{v}+t\mathbf{v}
=
(s+t)\mathbf{v}\in W.
$$

Inoltre, per ogni $\alpha\in\mathbb{R}$,

$$
\alpha(s\mathbf{v})
=
(\alpha s)\mathbf{v}\in W.
$$

Quindi $W$ è un sottospazio vettoriale.

### 10.2 Una retta non passante per l’origine

Una retta che non passa per l’origine non può essere un sottospazio vettoriale.

Il motivo più immediato è che non contiene il vettore nullo. Lo si vede anche graficamente: sommando due vettori di una retta non passante per l’origine, la regola del parallelogramma può dare un vettore fuori dalla retta.

Inoltre, moltiplicando un vettore della retta per lo scalare $0$, si ottiene $\mathbf{0}$, che è fuori dalla retta.

### 10.3 Sottospazi di $\mathbb{R}^2$

Gli unici sottospazi vettoriali di $\mathbb{R}^2$ sono:

1. il sottospazio banale

   $$
   \{\mathbf{0}\};
   $$

2. le rette passanti per l’origine;

3. tutto $\mathbb{R}^2$.

L’idea della dimostrazione: un sottospazio contiene sempre $\mathbf{0}$. Se contiene un solo vettore non nullo $\mathbf{v}$ e non contiene vettori indipendenti da $\mathbf{v}$, allora contiene esattamente tutti i multipli di $\mathbf{v}$, cioè una retta per l’origine. Se invece contiene un altro vettore non appartenente a quella retta, allora contiene tutte le combinazioni lineari dei due vettori; in $\mathbb{R}^2$ queste combinazioni generano tutto il piano.

### 10.4 Sottospazi di $\mathbb{R}^3$

In $\mathbb{R}^3$ compaiono più possibilità:

1. $\{\mathbf{0}\}$;
2. le rette passanti per l’origine;
3. i piani passanti per l’origine;
4. tutto $\mathbb{R}^3$.

Se un sottospazio contiene un vettore non nullo, contiene tutta la retta generata da quel vettore. Se contiene un secondo vettore fuori dalla prima retta, contiene il piano generato dai due vettori:

$$
W=\{\alpha\mathbf{u}+\beta\mathbf{v}\mid \alpha,\beta\in\mathbb{R}\}.
$$

Se contiene poi un terzo vettore fuori da quel piano, contiene tutte le combinazioni lineari di tre vettori indipendenti e quindi coincide con $\mathbb{R}^3$.

---

## 11. Intersezione di sottospazi

Se $W_1$ e $W_2$ sono sottospazi vettoriali di $V$, allora anche la loro [[Operazioni tra insiemi|intersezione]]

$$
W_1\cap W_2
$$

è un sottospazio vettoriale.

Infatti:

- se $\mathbf{u},\mathbf{v}\in W_1\cap W_2$, allora $\mathbf{u},\mathbf{v}$ appartengono sia a $W_1$ sia a $W_2$;
- poiché entrambi sono sottospazi,

  $$
  \mathbf{u}+\mathbf{v}\in W_1
  \qquad\text{e}\qquad
  \mathbf{u}+\mathbf{v}\in W_2;
  $$

  quindi

  $$
  \mathbf{u}+\mathbf{v}\in W_1\cap W_2;
  $$

- analogamente, per ogni $\alpha\in K$,

  $$
  \alpha\mathbf{u}\in W_1
  \qquad\text{e}\qquad
  \alpha\mathbf{u}\in W_2,
  $$

  dunque

  $$
  \alpha\mathbf{u}\in W_1\cap W_2.
  $$

L’intersezione contiene sempre il vettore nullo, perché ogni sottospazio lo contiene.

Lo stesso ragionamento vale per l’intersezione di un numero qualunque di sottospazi.

---

## 12. Unione di sottospazi

L’unione di due sottospazi, in generale, non è un sottospazio.

Siano $W_1,W_2\subseteq V$ due sottospazi. Se uno dei due è contenuto nell’altro, per esempio

$$
W_1\subseteq W_2,
$$

allora

$$
W_1\cup W_2=W_2,
$$

quindi l’unione è un sottospazio.

Se invece nessuno dei due è contenuto nell’altro, l’unione non è un sottospazio. Infatti si possono scegliere

$$
\mathbf{u}\in W_1\setminus W_2,
\qquad
\mathbf{v}\in W_2\setminus W_1.
$$

I vettori $\mathbf{u}$ e $\mathbf{v}$ appartengono all’unione, ma in generale la loro somma

$$
\mathbf{u}+\mathbf{v}
$$

non appartiene né a $W_1$ né a $W_2$. Di conseguenza,

$$
\mathbf{u}+\mathbf{v}\notin W_1\cup W_2,
$$

e l’unione non è chiusa rispetto alla somma.

In $\mathbb{R}^2$, per esempio, l’unione di due rette distinte per l’origine non è un sottospazio: prendendo un vettore non nullo su ciascuna retta, la loro somma sta in una terza direzione, quindi in nessuna delle due rette.

La proposizione fondamentale è dunque:

> L’unione di due sottospazi vettoriali è un sottospazio se e solo se uno dei due sottospazi è contenuto nell’altro.

---

## 13. Strategia pratica per verificare un sottospazio

Per stabilire che un insieme $W$ è un sottospazio di $V$ basta:

1. verificare che $W$ non sia vuoto, oppure direttamente che $\mathbf{0}\in W$;
2. prendere due elementi generici $\mathbf{u},\mathbf{v}\in W$ e dimostrare che

   $$
   \mathbf{u}+\mathbf{v}\in W;
   $$

3. prendere $\alpha\in K$ e $\mathbf{u}\in W$ e dimostrare che

   $$
   \alpha\mathbf{u}\in W.
   $$

Non serve ripetere tutti gli assiomi: associatività, commutatività e distributività valgono già nello spazio ambiente $V$ e vengono ereditate da $W$, purché le operazioni restino interne a $W$.

In pratica, il punto è controllare che le operazioni **non facciano uscire dall’insieme**.
