---
type: lecture-note
course: Aritmetica
date: '2026-11-08'
title: Omomorfismi, nuclei e prodotti diretti di gruppi
source_transcript: _transcripts/Aritmetica/2026-11-08 - Omomorfismi, nuclei e prodotti diretti di gruppi.md
source_hash: sha256:30598f18406808a4d74c1e2ca6821bd1f3caf147ba9cb457ff5de118507d34fc
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-11-08T13:01:01.737Z'
vault_path: Notes/Aritmetica/Lectures/2026-11-08 - Omomorfismi, nuclei e prodotti diretti di gruppi.md
vault_hash: 0b01614623c1fc03e2eff6478dbb261489036b1922a17e1c5fa15a40e0a5d6c9
---

# Omomorfismi, nuclei e prodotti diretti di gruppi

## 1. Applicazioni definite su classi di resto

Quando si definisce un’applicazione tra quozienti o tra insiemi di classi di equivalenza, la prima cosa da controllare è la **[[Buona definizione|buona definizione]]**.

Se il dominio è un insieme di classi, un elemento non è rappresentato da un unico oggetto, ma da molti rappresentanti. Perciò una formula del tipo

$$
\overline{a}\longmapsto \overline{a}
$$

ha senso solo se il risultato non dipende dal rappresentante scelto.

### Criterio generale di buona definizione

Supponiamo di voler definire una funzione

$$
f\colon A/{\sim}\longrightarrow B/{\approx},
\qquad
f([a])=[g(a)].
$$

Per dimostrare che $f$ è ben definita bisogna verificare che

$$
[a]=[b]
\quad\Longrightarrow\quad
[g(a)]=[g(b)].
$$

In altre parole, rappresentanti equivalenti nel dominio devono avere immagini equivalenti nel codominio.

---

## 2. Applicazioni tra gruppi quoziente $\mathbb{Z}/n\mathbb{Z}$

Si considera, ad esempio, la funzione formalmente definita da

$$
f\colon \mathbb{Z}/n\mathbb{Z}\longrightarrow \mathbb{Z}/m\mathbb{Z},
\qquad
f(\overline{a}^{\,n})=\overline{a}^{\,m}.
$$

Qui $\overline{a}^{\,n}$ indica la classe di $a$ modulo $n$, mentre $\overline{a}^{\,m}$ indica la classe di $a$ modulo $m$.

La domanda è: quando questa formula definisce davvero una funzione?

Se

$$
\overline{a}^{\,n}=\overline{b}^{\,n},
$$

allora

$$
a\equiv b\pmod n,
$$

cioè $n\mid(a-b)$. Perché le immagini coincidano deve valere anche

$$
a\equiv b\pmod m,
$$

ossia $m\mid(a-b)$.

Questo è garantito per ogni $a,b$ se

$$
m\mid n.
$$

Infatti, se $m\mid n$ e $n\mid(a-b)$, allora anche $m\mid(a-b)$.

Pertanto:

> La formula
>
> $$
> \overline{a}^{\,n}\longmapsto\overline{a}^{\,m}
> $$
>
> definisce una funzione $\mathbb{Z}/n\mathbb{Z}\to\mathbb{Z}/m\mathbb{Z}$ se $m\mid n$.

La condizione è anche necessaria. Infatti, poiché

$$
\overline{0}^{\,n}=\overline{n}^{\,n},
$$

le loro immagini devono essere uguali. Quindi dovrebbe essere

$$
\overline{0}^{\,m}=\overline{n}^{\,m},
$$

cioè $m\mid n$.

### Esempio: una proiezione che non è ben definita

La regola

$$
\mathbb{Z}/4\mathbb{Z}\longrightarrow \mathbb{Z}/3\mathbb{Z},
\qquad
\overline{a}^{\,4}\longmapsto\overline{a}^{\,3}
$$

non è ben definita, perché $3\nmid4$.

Infatti, in $\mathbb{Z}/4\mathbb{Z}$ si ha

$$
\overline{0}^{\,4}=\overline{4}^{\,4}.
$$

Però le immagini sarebbero

$$
\overline{0}^{\,3}
\qquad\text{e}\qquad
\overline{4}^{\,3}=\overline{1}^{\,3},
$$

che sono diverse in $\mathbb{Z}/3\mathbb{Z}$. La stessa classe del dominio avrebbe quindi due immagini diverse.

### Esempio: la proiezione canonica

La funzione

$$
\pi\colon\mathbb{Z}\longrightarrow\mathbb{Z}/n\mathbb{Z},
\qquad
\pi(a)=\overline{a}^{\,n}
$$

è sempre ben definita, perché qui gli elementi del dominio sono interi e non classi già rappresentate in modo non unico.

Inoltre $\pi$ è un omomorfismo di gruppi rispetto all’addizione:

$$
\pi(a+b)=\overline{a+b}
=\overline{a}+\overline{b}
=\pi(a)+\pi(b).
$$

---

## 3. Omomorfismi di gruppi

Siano $(G,\cdot)$ e $(H,*)$ [[Gruppo|gruppi]]. Un’applicazione

$$
f\colon G\longrightarrow H
$$

si dice **[[Omomorfismo|omomorfismo di gruppi]]** se preserva l’operazione:

$$
f(x\cdot y)=f(x)*f(y)
\qquad
\forall x,y\in G.
$$

Quando non c’è rischio di confusione, si scrive semplicemente

$$
f(xy)=f(x)f(y).
$$

L’operazione non è necessariamente la somma: nei gruppi additivi si scriverebbe

$$
f(x+y)=f(x)+f(y),
$$

ma nel contesto generale dei gruppi si usa la notazione moltiplicativa.

Un omomorfismo può essere:

- **iniettivo**, se elementi distinti hanno immagini distinte;
- **suriettivo**, se ogni elemento del codominio è immagine di qualche elemento del dominio;
- **biettivo**, se è contemporaneamente iniettivo e suriettivo (vedi [[Funzione biettiva|funzione biettiva]]);
- un **[[Isomorfismo|isomorfismo]]**, se è un omomorfismo biettivo.

Se esiste un isomorfismo $G\to H$, si dice che $G$ e $H$ sono isomorfi e si scrive

$$
G\cong H.
$$

L’isomorfismo non identifica letteralmente gli elementi dei due gruppi: identifica il loro comportamento algebrico. Proprietà come l’abelianità, la struttura dei sottogruppi e gli ordini degli elementi vengono preservate.

---

### 4. Proprietà fondamentali degli omomorfismi

#### 4.1 L’identità viene mandata nell’identità

Sia $e_G$ l’identità di $G$ ed $e_H$ l’identità di $H$. Allora

$$
f(e_G)=e_H.
$$

Infatti:

$$
f(e_G)
=f(e_Ge_G)
=f(e_G)f(e_G).
$$

Moltiplicando a sinistra per l’inverso di $f(e_G)$, oppure usando la legge di cancellazione nei gruppi, si ottiene

$$
e_H=f(e_G).
$$

La cancellazione è lecita perché ogni gruppo ha gli inversi. Per esempio, da $ab=ac$ si moltiplica a sinistra per $a^{-1}$ e si ottiene $b=c$.

> Attenzione: $\mathbb{Z}/n\mathbb{Z}$ è un gruppo rispetto all’addizione, non rispetto alla moltiplicazione in generale. La moltiplicazione modulo $n$ dà un gruppo solo restringendosi agli elementi invertibili, oppure in casi particolari.

#### 4.2 L’inverso dell’immagine è l’immagine dell’inverso

Per ogni $x\in G$ vale

$$
f(x^{-1})=f(x)^{-1}.
$$

Dimostrazione:

$$
f(x)f(x^{-1})
=f(xx^{-1})
=f(e_G)
=e_H.
$$

Analogamente,

$$
f(x^{-1})f(x)=e_H.
$$

Dunque $f(x^{-1})$ è l’inverso di $f(x)$, cioè

$$
f(x^{-1})=f(x)^{-1}.
$$

Più in generale, per ogni $n\in\mathbb{Z}$,

$$
f(x^n)=f(x)^n.
$$

Per $n>0$ segue dalla proprietà di omomorfismo; per $n<0$ si usa la proprietà sugli inversi.

---

## 5. Immagini e controimmagini

Sia $f\colon G\to H$ un omomorfismo e sia $K\leq G$ un [[Sottogruppo|sottogruppo]]. L’[[Immagine e controimmagine|immagine]] di $K$ è

$$
f(K)=\{f(x)\mid x\in K\}.
$$

### Proposizione

L’immagine di un sottogruppo tramite un omomorfismo è un sottogruppo del codominio:

$$
K\leq G
\quad\Longrightarrow\quad
f(K)\leq H.
$$

#### Dimostrazione

Per il criterio di sottogruppo, bisogna mostrare che $f(K)$ è non vuoto, chiuso rispetto al prodotto e rispetto agli inversi.

Poiché $K$ è un sottogruppo, contiene $e_G$. Quindi

$$
f(e_G)=e_H\in f(K),
$$

perciò $f(K)$ è non vuoto.

Siano $u,v\in f(K)$. Per definizione di immagine, esistono $x,y\in K$ tali che

$$
u=f(x),
\qquad
v=f(y).
$$

Allora

$$
uv=f(x)f(y)=f(xy).
$$

Poiché $K$ è un sottogruppo, $xy\in K$; dunque

$$
uv=f(xy)\in f(K).
$$

Infine, se $u=f(x)\in f(K)$, allora

$$
u^{-1}=f(x)^{-1}=f(x^{-1}).
$$

Poiché $x^{-1}\in K$, si ha $u^{-1}\in f(K)$.

Pertanto $f(K)$ è un sottogruppo di $H$.

---

### Controimmagine di un sottogruppo

Se $K\leq H$, la controimmagine di $K$ è

$$
f^{-1}(K)
=
\{x\in G\mid f(x)\in K\}.
$$

Anche la controimmagine di un sottogruppo tramite un omomorfismo è un sottogruppo:

$$
K\leq H
\quad\Longrightarrow\quad
f^{-1}(K)\leq G.
$$

Infatti, se $x,y\in f^{-1}(K)$, allora $f(x),f(y)\in K$, quindi

$$
f(xy^{-1})
=f(x)f(y)^{-1}\in K.
$$

Ne segue che $xy^{-1}\in f^{-1}(K)$.

---

## 6. Il nucleo di un omomorfismo

### Definizione

Il **[[Nucleo|nucleo]]** di un omomorfismo $f\colon G\to H$ è la controimmagine dell’identità di $H$:

$$
\ker(f)=f^{-1}(\{e_H\})
=
\{x\in G\mid f(x)=e_H\}.
$$

Gli elementi del nucleo sono quindi esattamente quelli che vengono mandati nell’identità.

Poiché $\{e_H\}$ è un sottogruppo di $H$, per la proprietà delle controimmagini si ha subito:

$$
\ker(f)\leq G.
$$

#### Esempio: il nucleo della proiezione canonica

Per

$$
\pi\colon\mathbb{Z}\longrightarrow\mathbb{Z}/n\mathbb{Z},
\qquad
\pi(a)=\overline{a}^{\,n},
$$

il nucleo è

$$
\ker(\pi)
=
\{a\in\mathbb{Z}\mid \overline{a}^{\,n}=\overline{0}^{\,n}\}.
$$

La condizione equivale a

$$
a\equiv0\pmod n,
$$

cioè $n\mid a$. Pertanto

$$
\ker(\pi)=n\mathbb{Z}.
$$

Si vede così che il nucleo non è per forza formato solo dall’identità del dominio: per la proiezione $\mathbb{Z}\to\mathbb{Z}/n\mathbb{Z}$ è il sottogruppo infinito $n\mathbb{Z}$.

---

### 7. Criterio di iniettività

### Teorema

Sia $f\colon G\to H$ un omomorfismo. Allora

$$
f \text{ è iniettivo}
\quad\Longleftrightarrow\quad
\ker(f)=\{e_G\}.
$$

#### Dimostrazione: direzione facile

Supponiamo che $f$ sia iniettivo. Se $x\in\ker(f)$, allora

$$
f(x)=e_H.
$$

Ma, poiché $f(e_G)=e_H$, si ha

$$
f(x)=f(e_G).
$$

L’iniettività implica

$$
x=e_G.
$$

Quindi

$$
\ker(f)=\{e_G\}.
$$

#### Dimostrazione: direzione inversa

Supponiamo ora che

$$
\ker(f)=\{e_G\}.
$$

Vogliamo dimostrare che $f$ è iniettivo. Siano $x,y\in G$ tali che

$$
f(x)=f(y).
$$

Moltiplicando a destra per $f(y)^{-1}$ si ottiene

$$
f(x)f(y)^{-1}=e_H.
$$

Usando la proprietà degli inversi,

$$
f(x)f(y)^{-1}
=
f(x)f(y^{-1})
=
f(xy^{-1}).
$$

Quindi

$$
f(xy^{-1})=e_H,
$$

ossia

$$
xy^{-1}\in\ker(f).
$$

Per ipotesi il nucleo è banale, dunque

$$
xy^{-1}=e_G.
$$

Moltiplicando a destra per $y$ si conclude che

$$
x=y.
$$

Pertanto $f$ è iniettivo.

> [!example] Esempio
> L’omomorfismo $f\colon\mathbb Z/6\mathbb Z\to\mathbb Z/3\mathbb Z$, $\overline a^{\,6}\mapsto\overline a^{\,3}$ (ben definito perché $3\mid6$) ha nucleo $\{\overline0^{\,6},\overline3^{\,6}\}$, che non è banale: infatti $f$ non è iniettivo, perché $\overline0^{\,6}$ e $\overline3^{\,6}$ vanno entrambi in $\overline0^{\,3}$.

---

## 8. Ordine degli elementi e omomorfismi

Ricordiamo che l’[[Ordine di un elemento|ordine]] di un elemento $x\in G$ è il minimo intero positivo $n$ tale che

$$
x^n=e_G,
$$

se tale intero esiste. Se non esiste, si dice che $x$ ha ordine infinito.

### Proposizione

Se $f\colon G\to H$ è un omomorfismo e $x\in G$ ha ordine finito, allora

$$
\operatorname{ord}(f(x))
\mid
\operatorname{ord}(x).
$$

#### Dimostrazione

Sia

$$
\operatorname{ord}(x)=n.
$$

Allora $x^n=e_G$. Applicando $f$:

$$
f(x)^n
=
f(x^n)
=
f(e_G)
=
e_H.
$$

Per definizione di ordine, l’ordine di $f(x)$ divide ogni esponente positivo che manda $f(x)$ nell’identità. In particolare,

$$
\operatorname{ord}(f(x))\mid n.
$$

Quindi

$$
\operatorname{ord}(f(x))
\mid
\operatorname{ord}(x).
$$

L’ordine può dunque diminuire, ma non aumentare.

#### Caso degli omomorfismi iniettivi

Se $f$ è iniettivo, gli ordini vengono conservati:

$$
\operatorname{ord}(f(x))
=
\operatorname{ord}(x).
$$

Infatti, se $x^n=e_G$ allora $f(x)^n=e_H$, quindi l’ordine dell’immagine divide quello di $x$. Viceversa, se $f(x)^m=e_H$, allora

$$
f(x^m)=e_H=f(e_G).
$$

Per l’iniettività,

$$
x^m=e_G.
$$

I due ordini coincidono.

#### Avvertenza

Gli elementi del nucleo non devono per forza avere ordine infinito o un ordine particolare. L’unica cosa che li caratterizza è

$$
f(x)=e_H.
$$

Per esempio, nella proiezione canonica

$$
\pi\colon\mathbb{Z}\to\mathbb{Z}/n\mathbb{Z},
$$

tutti gli elementi di $n\mathbb{Z}$ stanno nel nucleo, e in $\mathbb{Z}$ hanno ordine infinito, mentre la loro immagine ha ordine $1$.

---

## 9. Gruppi ciclici

Un gruppo $G$ si dice **[[Gruppo ciclico|ciclico]]** se esiste un elemento $g\in G$ tale che

$$
G=\langle g\rangle
=
\{g^k\mid k\in\mathbb{Z}\}.
$$

L’elemento $g$ è detto generatore di $G$.

A seconda dell’ordine di $g$, si distinguono due casi.

### 9.1 Gruppo ciclico infinito

Se $g$ ha ordine infinito, tutte le potenze

$$
\ldots,g^{-2},g^{-1},e,g,g^2,\ldots
$$

sono distinte. La funzione

$$
\varphi\colon\mathbb{Z}\longrightarrow G,
\qquad
\varphi(k)=g^k
$$

è un isomorfismo.

È un omomorfismo perché

$$
\varphi(k+\ell)
=
g^{k+\ell}
=
g^kg^\ell
=
\varphi(k)\varphi(\ell).
$$

È suriettivo perché $g$ genera $G$. È iniettivo perché, se $g^k=g^\ell$, allora

$$
g^{k-\ell}=e,
$$

e l’ordine infinito di $g$ implica $k-\ell=0$, cioè $k=\ell$.

Quindi ogni gruppo ciclico infinito è isomorfo a $(\mathbb{Z},+)$:

$$
G\cong\mathbb{Z}.
$$

### 9.2 Gruppo ciclico finito

Se $g$ ha ordine $n$, allora

$$
g^n=e_G
$$

e le potenze si ripetono con periodo $n$:

$$
g^{k+n}=g^k
\qquad
\forall k\in\mathbb{Z}.
$$

In questo caso si definisce

$$
\varphi\colon\mathbb{Z}/n\mathbb{Z}\longrightarrow G,
\qquad
\varphi(\overline{k})=g^k.
$$

#### Buona definizione

Se

$$
\overline{k}=\overline{\ell}\pmod n,
$$

allora $n\mid(k-\ell)$, dunque $k-\ell=qn$ per qualche $q\in\mathbb{Z}$. Pertanto

$$
g^k
=
g^{\ell+qn}
=
g^\ell(g^n)^q
=
g^\ell.
$$

Quindi $\varphi$ è ben definita.

#### Omomorfismo

Si ha

$$
\varphi(\overline{k}+\overline{\ell})
=
\varphi(\overline{k+\ell})
=
g^{k+\ell}
=
g^kg^\ell
=
\varphi(\overline{k})\varphi(\overline{\ell}).
$$

#### Suriettività

Ogni elemento di $G$ è una potenza di $g$, quindi è immagine di una classe $\overline{k}$.

#### Iniettività

Se

$$
\varphi(\overline{k})=e_G,
$$

allora

$$
g^k=e_G.
$$

Poiché $g$ ha ordine $n$, segue che $n\mid k$, e quindi

$$
\overline{k}=\overline{0}.
$$

Il nucleo è dunque banale e $\varphi$ è iniettiva.

Pertanto ogni gruppo ciclico finito di ordine $n$ è isomorfo a $\mathbb{Z}/n\mathbb{Z}$:

$$
G\cong\mathbb{Z}/n\mathbb{Z}.
$$

> A meno di isomorfismo, i gruppi ciclici sono quindi soltanto:
>
> - $\mathbb{Z}$, nel caso infinito;
> - $\mathbb{Z}/n\mathbb{Z}$, nel caso finito di ordine $n$.

È un risultato importante perché permette di studiare tutti i gruppi ciclici dello stesso ordine attraverso un modello standard.

---

### 10. Omomorfismi determinati dall’immagine di un generatore

Sia $G=\langle g\rangle$ un gruppo ciclico e sia $f\colon G\to H$ un omomorfismo. Per ogni $k\in\mathbb{Z}$,

$$
f(g^k)=f(g)^k.
$$

Quindi l’omomorfismo è completamente determinato dal valore $f(g)$.

#### Caso finito

Se $g$ ha ordine $n$, deve valere

$$
g^n=e_G.
$$

Applicando $f$ si ottiene

$$
f(g)^n=e_H.
$$

Quindi l’elemento $f(g)$ deve avere ordine che divide $n$.

In particolare, per definire un omomorfismo

$$
\mathbb{Z}/n\mathbb{Z}\longrightarrow H
$$

basta scegliere un elemento $h\in H$ tale che

$$
h^n=e_H,
$$

e porre

$$
\overline{k}\longmapsto h^k.
$$

La condizione $h^n=e_H$ è proprio quella che garantisce la buona definizione rispetto alle classi modulo $n$.

---

## 11. Esempio: gruppi ciclici di radici dell’unità

Nel gruppo moltiplicativo dei numeri complessi non nulli, l’insieme delle [[Radice n-esima dell'unità|radici $n$-esime dell’unità]] è

$$
C_n
=
\{z\in\mathbb{C}\mid z^n=1\}.
$$

Questo insieme ha esattamente $n$ elementi e forma un gruppo rispetto alla moltiplicazione.

Se $\zeta$ è una radice $n$-esima primitiva dell’unità, allora

$$
C_n=\langle \zeta\rangle
=
\{1,\zeta,\zeta^2,\ldots,\zeta^{n-1}\}.
$$

La funzione

$$
\varphi\colon\mathbb{Z}/n\mathbb{Z}\longrightarrow C_n,
\qquad
\varphi(\overline{k})=\zeta^k
$$

è un isomorfismo.

Perciò $C_n$ e $\mathbb{Z}/n\mathbb{Z}$ sono gruppi diversi come insiemi e come operazioni concrete, ma hanno la stessa struttura algebrica:

$$
C_n\cong\mathbb{Z}/n\mathbb{Z}.
$$

---

### 12. Esempio: omomorfismi da $\mathbb{Z}/4\mathbb{Z}$ a $\mathbb{Z}/3\mathbb{Z}$

Un omomorfismo

$$
f\colon\mathbb{Z}/4\mathbb{Z}\longrightarrow\mathbb{Z}/3\mathbb{Z}
$$

è determinato dall’immagine di $\overline{1}^{\,4}$, perché $\overline{1}^{\,4}$ genera $\mathbb{Z}/4\mathbb{Z}$.

L’elemento $\overline{1}^{\,4}$ ha ordine $4$. Di conseguenza $f(\overline{1}^{\,4})$ deve avere ordine divisore di $4$.

Nel gruppo $\mathbb{Z}/3\mathbb{Z}$ gli ordini possibili sono:

- l’ordine $1$ per $\overline{0}^{\,3}$;
- l’ordine $3$ per $\overline{1}^{\,3}$ e $\overline{2}^{\,3}$.

L’unico ordine che divide $4$ è $1$. Dunque necessariamente

$$
f(\overline{1}^{\,4})=\overline{0}^{\,3}.
$$

Ne segue che l’unico omomorfismo è quello banale:

$$
f(\overline{k}^{\,4})=\overline{0}^{\,3}
\qquad
\forall k.
$$

Lo si vede anche così: l’immagine di un elemento di ordine $4$ dovrebbe avere ordine divisore di $4$, ma in $\mathbb{Z}/3\mathbb{Z}$ non esistono elementi di ordine $2$ o $4$.

---

## 13. Prodotti diretti di gruppi

Siano $G_1$ e $G_2$ due gruppi. Il loro **[[Prodotto diretto|prodotto diretto]]** è il [[Prodotto cartesiano|prodotto cartesiano]]

$$
G_1\times G_2
=
\{(x,y)\mid x\in G_1,\ y\in G_2\},
$$

dotato dell’operazione definita componente per componente:

$$
(x_1,y_1)(x_2,y_2)
=
(x_1x_2,y_1y_2).
$$

Le operazioni usate nelle due componenti sono quelle dei gruppi $G_1$ e $G_2$, che non devono per forza essere la stessa operazione concreta.

#### Verifica della struttura di gruppo

- L’identità è
  $$
  (e_{G_1},e_{G_2}).
  $$

- L’inverso di $(x,y)$ è
  $$
  (x,y)^{-1}
  =
  (x^{-1},y^{-1}).
  $$

- L’associatività segue componente per componente:
  $$
  \bigl((x_1,y_1)(x_2,y_2)\bigr)(x_3,y_3)
  =
  (x_1x_2x_3,y_1y_2y_3)
  $$
  e
  $$
  (x_1,y_1)\bigl((x_2,y_2)(x_3,y_3)\bigr)
  =
  (x_1x_2x_3,y_1y_2y_3).
  $$

Se $G_1$ e $G_2$ sono finiti, allora

$$
|G_1\times G_2|
=
|G_1|\,|G_2|.
$$

Per esempio, se $|G_1|=2$ e $|G_2|=6$, allora

$$
|G_1\times G_2|=12.
$$

---

### 14. Centro del prodotto diretto

Il [[Centro di un gruppo|centro]] di un gruppo $G$ è

$$
Z(G)=\{z\in G\mid zg=gz\ \forall g\in G\}.
$$

Nel prodotto diretto vale

$$
Z(G_1\times G_2)
=
Z(G_1)\times Z(G_2).
$$

Infatti, $(z_1,z_2)$ commuta con ogni $(x_1,x_2)$ se e solo se

$$
(z_1,z_2)(x_1,x_2)
=
(x_1,x_2)(z_1,z_2),
$$

cioè se e solo se

$$
z_1x_1=x_1z_1
\qquad\text{e}\qquad
z_2x_2=x_2z_2
$$

per ogni $x_1\in G_1$ e $x_2\in G_2$. Questo equivale a

$$
z_1\in Z(G_1),
\qquad
z_2\in Z(G_2).
$$

---

## 15. Ordine di un elemento in un prodotto diretto

Siano $x\in G_1$ e $y\in G_2$. Consideriamo l’elemento $(x,y)\in G_1\times G_2$.

Per ogni $n\in\mathbb{N}$,

$$
(x,y)^n=(x^n,y^n).
$$

Siano

$$
\operatorname{ord}(x)=m,
\qquad
\operatorname{ord}(y)=n.
$$

Cerchiamo il minimo intero positivo $d$ tale che

$$
(x,y)^d=(e_{G_1},e_{G_2}).
$$

Questa uguaglianza equivale a

$$
x^d=e_{G_1}
\qquad\text{e}\qquad
y^d=e_{G_2}.
$$

Quindi $d$ deve essere contemporaneamente un multiplo di $m$ e di $n$. Il minimo possibile è il [[Minimo comune multiplo|minimo comune multiplo]].

### Teorema

Se $x$ e $y$ hanno ordine finito, allora

$$
\operatorname{ord}(x,y)
=
\operatorname{mcm}\bigl(\operatorname{ord}(x),\operatorname{ord}(y)\bigr).
$$

#### Dimostrazione

Poniamo

$$
m=\operatorname{ord}(x),
\qquad
n=\operatorname{ord}(y),
\qquad
d=\operatorname{mcm}(m,n).
$$

Poiché $m\mid d$ e $n\mid d$, si ha

$$
x^d=e_{G_1},
\qquad
y^d=e_{G_2}.
$$

Pertanto

$$
(x,y)^d=(e_{G_1},e_{G_2}).
$$

Dunque l’ordine di $(x,y)$ divide $d$.

Viceversa, se

$$
(x,y)^k=(e_{G_1},e_{G_2}),
$$

allora

$$
x^k=e_{G_1},
\qquad
y^k=e_{G_2}.
$$

Da ciò segue che

$$
m\mid k,
\qquad
n\mid k.
$$

Quindi $k$ è un multiplo comune di $m$ e $n$, e pertanto

$$
\operatorname{mcm}(m,n)\mid k.
$$

Il minimo esponente positivo che annulla $(x,y)$ è quindi proprio

$$
\operatorname{mcm}(m,n).
$$

#### Esempio

Se $x$ ha ordine $2$ e $y$ ha ordine $3$, allora

$$
\operatorname{ord}(x,y)
=
\operatorname{mcm}(2,3)
=
6.
$$

Se invece $x$ ha ordine $2$ e $y$ ha ordine $2$, allora

$$
\operatorname{ord}(x,y)=2.
$$

In particolare, l’ordine di una coppia in generale non è il prodotto degli ordini delle componenti: è il loro minimo comune multiplo.

---

## 16. Collegamento tra prodotti e gruppi ciclici

Il prodotto diretto di due gruppi ciclici non è sempre ciclico.

Se

$$
G_1=\langle x\rangle,
\qquad
G_2=\langle y\rangle,
$$

con

$$
\operatorname{ord}(x)=m,
\qquad
\operatorname{ord}(y)=n,
$$

allora l’elemento $(x,y)$ ha ordine

$$
\operatorname{mcm}(m,n).
$$

Il prodotto $G_1\times G_2$ ha cardinalità $mn$. Per essere ciclico dovrebbe contenere un elemento di ordine $mn$. Ma l’ordine di ogni elemento è al più $\operatorname{mcm}(m,n)$ nel caso dei generatori delle due componenti; in particolare, quando $m$ e $n$ non sono coprimi,

$$
\operatorname{mcm}(m,n)<mn,
$$

e il prodotto non può essere ciclico.

Nel caso di gruppi ciclici finiti vale il criterio noto:

$$
\mathbb{Z}/m\mathbb{Z}\times\mathbb{Z}/n\mathbb{Z}
\cong
\mathbb{Z}/mn\mathbb{Z}
\quad\Longleftrightarrow\quad
\gcd(m,n)=1.
$$

Il motivo è che, se $m$ e $n$ sono coprimi,

$$
\operatorname{mcm}(m,n)=mn,
$$

quindi la coppia formata da due generatori ha ordine pari alla cardinalità dell’intero prodotto.

> [!example] Esempio
> $\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z\cong\mathbb Z/6\mathbb Z$: la coppia $(\overline1,\overline1)$ ha ordine $\operatorname{mcm}(2,3)=6$, quindi genera tutto il gruppo di $6$ elementi. Invece $\mathbb Z/2\mathbb Z\times\mathbb Z/2\mathbb Z$ non è ciclico: ha $4$ elementi ma ogni elemento ha ordine al più $\operatorname{mcm}(2,2)=2$.

---

## 17. Esempi con gruppi ciclici finiti e ordini degli elementi

In un gruppo ciclico di ordine $n$, isomorfo a $\mathbb{Z}/n\mathbb{Z}$, l’ordine della classe $\overline{k}$ è

$$
\operatorname{ord}(\overline{k})
=
\frac{n}{\gcd(n,k)}.
$$

In particolare, gli elementi di ordine $d$, dove $d\mid n$, sono quelli della forma

$$
\overline{\frac{n}{d}r},
$$

con $r$ coprimo con $d$.

Il sottogruppo di ordine $d$ è unico e coincide con

$$
\left\langle \overline{\frac{n}{d}}\right\rangle.
$$

Così si individuano gli elementi di un certo ordine senza controllarli uno per uno.

#### Esempio in $\mathbb{Z}/100\mathbb{Z}$

Il sottogruppo di ordine $25$ è generato da

$$
\overline{4}^{\,100},
$$

perché

$$
\frac{100}{25}=4.
$$

È

$$
\left\langle \overline{4}^{\,100}\right\rangle
=
\{
\overline{0}^{\,100},
\overline{4}^{\,100},
\overline{8}^{\,100},
\ldots,
\overline{96}^{\,100}
\}.
$$

Ha $25$ elementi.

Gli elementi di ordine esattamente $25$ sono le potenze del generatore corrispondenti agli esponenti coprimi con $25$:

$$
\overline{4k}^{\,100},
\qquad
\gcd(k,25)=1.
$$

Il loro numero è

$$
\varphi(25)=20,
$$

dove $\varphi$ è la funzione di Eulero.

Gli elementi di ordine $5$ appartengono invece all’unico sottogruppo di ordine $5$, generato da

$$
\overline{20}^{\,100}.
$$

---

## 18. Osservazioni conclusive sui nuclei e sugli isomorfismi

Gli omomorfismi permettono di trasferire molte proprietà strutturali:

- l’identità viene mandata nell’identità;
- gli inversi vengono mandati negli inversi;
- le potenze vengono preservate;
- l’immagine di un sottogruppo è un sottogruppo;
- la controimmagine di un sottogruppo è un sottogruppo;
- il nucleo è un sottogruppo del dominio;
- l’ordine dell’immagine divide l’ordine dell’elemento di partenza;
- gli omomorfismi iniettivi conservano gli ordini;
- un omomorfismo è iniettivo se e solo se il suo nucleo è banale.

Nel caso dei gruppi ciclici, un omomorfismo è determinato dall’immagine di un generatore. Questo permette di costruire e classificare facilmente gli omomorfismi tra gruppi ciclici.

Infine, il prodotto diretto costruisce nuovi gruppi a partire da gruppi già noti. L’identità, l’inverso e le operazioni sono definiti componente per componente, mentre l’ordine di una coppia è il minimo comune multiplo degli ordini delle sue componenti.
