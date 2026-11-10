---
type: lecture-note
course: Aritmetica
date: '2026-10-06'
title: Equazioni diofantee lineari e loro soluzioni
source_transcript: _transcripts/Aritmetica/2026-10-06 - Equazioni diofantee lineari e loro soluzioni.md
source_hash: sha256:b5974126edb18c3920a494932d787fdf5293b04d20bdd7fb4d3da6daba336fba
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-06T08:58:01.444Z'
vault_path: Notes/Aritmetica/Lectures/2026-10-06 - Equazioni diofantee lineari e loro soluzioni.md
vault_hash: f0b8abb9aa16696c88e26ed5f3bf0051a0e9f3290bf03a78f1b7d0fbea633860
---

## 1. Forma generale del problema

Un’[[Equazione diofantea lineare|equazione diofantea lineare]] in due incognite è un’equazione del tipo

$$
ax+by=c,
$$

dove $a,b,c\in\mathbb{Z}$ e si cercano **soluzioni intere** $(x,y)\in\mathbb{Z}^2$.

L’obiettivo non è solo trovare una soluzione, quando esiste, ma determinare **tutte** le soluzioni intere.

Il punto fondamentale è questo:

> L’equazione $ax+by=c$ ammette soluzioni intere se e solo se il [[Massimo comun divisore|massimo comune divisore]] di $a$ e $b$ divide $c$.

Indicando con

$$
d=\gcd(a,b),
$$

il criterio di esistenza è quindi

$$
d\mid c.
$$

---

## 2. Il ruolo del massimo comune divisore

Per definizione, $d=\gcd(a,b)$ è un divisore comune di $a$ e $b$, ed è il massimo tra i divisori comuni positivi.

Possiamo scrivere

$$
a=da_1,\qquad b=db_1,
$$

dove $a_1,b_1\in\mathbb{Z}$ e

$$
\gcd(a_1,b_1)=1.
$$

La coppia $(a_1,b_1)$ si ottiene dividendo entrambi i coefficienti per il loro MCD. Questa riduzione è importante perché porta il problema al caso coprimo.

Un fatto fondamentale: ogni combinazione lineare intera di $a$ e $b$ è divisibile per $d$:

$$
d\mid a,\qquad d\mid b
\quad\Longrightarrow\quad
d\mid (ax+by)
$$

per ogni $x,y\in\mathbb{Z}$.

Di conseguenza, se l’equazione

$$
ax+by=c
$$

ha una soluzione intera, allora necessariamente

$$
d\mid c.
$$

Questa è la parte necessaria del criterio.

---

## 3. Dimostrazione della necessità

Supponiamo che esista una soluzione intera $(x,y)$ dell’equazione:

$$
ax+by=c.
$$

Siccome $d=\gcd(a,b)$ divide sia $a$ sia $b$, esistono $a_1,b_1\in\mathbb{Z}$ tali che

$$
a=da_1,\qquad b=db_1.
$$

Sostituendo nell’equazione:

$$
c=ax+by
  =da_1x+db_1y
  =d(a_1x+b_1y).
$$

Il termine tra parentesi è intero, quindi $c$ è un multiplo intero di $d$. Dunque

$$
d\mid c.
$$

Perciò, se $\gcd(a,b)\nmid c$, l’equazione non può avere soluzioni intere.

---

## 4. Identità di Bézout

Per dimostrare la sufficienza serve l’[[Identità di Bézout|identità di Bézout]]:

> Per ogni $a,b\in\mathbb{Z}$, esistono $u,v\in\mathbb{Z}$ tali che
>
> $$
> au+bv=\gcd(a,b).
> $$

Nel caso particolare $\gcd(a,b)=1$ si ottiene

$$
au+bv=1.
$$

I coefficienti $u$ e $v$ si trovano con l’algoritmo di Euclide esteso.

Dall’identità di Bézout seguono due fatti importanti:

1. il MCD è una combinazione lineare intera di $a$ e $b$;
2. ogni multiplo di $\gcd(a,b)$ è anch’esso una combinazione lineare intera di $a$ e $b$.

Infatti, se

$$
au+bv=d,
$$

moltiplicando per un intero $k$:

$$
a(ku)+b(kv)=kd.
$$

---

## 5. Dimostrazione della sufficienza

Supponiamo ora che

$$
d=\gcd(a,b)
$$

divida $c$. Allora esiste $\gamma\in\mathbb{Z}$ tale che

$$
c=d\gamma.
$$

Per l’identità di Bézout esistono $u,v\in\mathbb{Z}$ tali che

$$
au+bv=d.
$$

Moltiplicando entrambi i membri per $\gamma$ si ottiene

$$
a(\gamma u)+b(\gamma v)=d\gamma=c.
$$

Quindi

$$
x_0=\gamma u,\qquad y_0=\gamma v
$$

è una soluzione intera dell’equazione $ax+by=c$.

Abbiamo dimostrato:

## Teorema di esistenza

Siano $a,b,c\in\mathbb{Z}$ e sia $d=\gcd(a,b)$. L’equazione

$$
ax+by=c
$$

ammette almeno una soluzione intera se e solo se

$$
d\mid c.
$$

Quando $d\mid c$, una soluzione particolare si ottiene da una relazione di Bézout per $a$ e $b$.

> [!example] Esempio
> Per $6x+10y=8$ abbiamo $d=\gcd(6,10)=2$, che divide $8$, quindi esistono soluzioni. Una relazione di Bézout è $6\cdot 2+10\cdot(-1)=2$; con $\gamma=4$ otteniamo la soluzione particolare $(x_0,y_0)=(8,-4)$. Invece $6x+10y=7$ non ha soluzioni intere, perché $2\nmid 7$.

---

## 6. Riduzione al caso coprimo

Supponiamo che $d=\gcd(a,b)$ divida $c$. Scriviamo

$$
a=da_1,\qquad b=db_1,\qquad c=dc_1.
$$

L’equazione diventa

$$
da_1x+db_1y=dc_1.
$$

Dividendo per $d$:

$$
a_1x+b_1y=c_1,
$$

dove

$$
\gcd(a_1,b_1)=1.
$$

Questa equazione ridotta è equivalente a quella iniziale: le soluzioni intere sono esattamente le stesse.

La riduzione è utile perché nel caso coprimo si può applicare direttamente il lemma di Euclide, e la struttura delle soluzioni diventa più semplice.

---

## 7. Lemma di Euclide

Per descrivere tutte le soluzioni useremo questo lemma.

> Se $\gcd(r,s)=1$ e $r\mid st$, allora $r\mid t$.

Questo è il [[Lemma di Euclide|lemma di Euclide]]: se $r$ e $s$ sono [[Numeri coprimi|coprimi]] e $r$ divide un prodotto $st$, allora $r$ deve dividere il secondo fattore.

È un passaggio essenziale nella dimostrazione della forma generale delle soluzioni.

---

## 8. Determinazione di tutte le soluzioni

Supponiamo di avere già una soluzione particolare $(x_0,y_0)$ dell’equazione

$$
ax+by=c.
$$

Vogliamo descrivere tutte le altre.

Sia $(x,y)$ un’altra soluzione. Allora

$$
ax+by=c
$$

e

$$
ax_0+by_0=c.
$$

Sottraendo membro a membro:

$$
a(x-x_0)+b(y-y_0)=0.
$$

Usando $a=da_1$ e $b=db_1$, con $\gcd(a_1,b_1)=1$, si ottiene

$$
da_1(x-x_0)+db_1(y-y_0)=0.
$$

Dividendo per $d$:

$$
a_1(x-x_0)+b_1(y-y_0)=0.
$$

Da cui

$$
a_1(x-x_0)=-b_1(y-y_0).
$$

Quindi $a_1$ divide il prodotto $b_1(y-y_0)$. Siccome $\gcd(a_1,b_1)=1$, per il lemma di Euclide:

$$
a_1\mid (y-y_0).
$$

Analogamente,

$$
b_1\mid (x-x_0).
$$

Esiste dunque $t\in\mathbb{Z}$ tale che

$$
x-x_0=b_1t,
$$

e quindi

$$
x=x_0+b_1t.
$$

Sostituendo nell’equazione, si ottiene

$$
y-y_0=-a_1t,
$$

cioè

$$
y=y_0-a_1t.
$$

Ricordando che

$$
a_1=\frac{a}{d},\qquad b_1=\frac{b}{d},
$$

la forma generale di tutte le soluzioni è

$$
\boxed{
\begin{aligned}
x&=x_0+\frac{b}{d}t,\\
y&=y_0-\frac{a}{d}t,
\end{aligned}
\qquad t\in\mathbb{Z}.
}
$$

Qui $(x_0,y_0)$ è una qualunque soluzione particolare.

---

## 9. Verifica della parametrizzazione

Bisogna controllare anche il viceversa: ogni coppia data dalla formula precedente è davvero una soluzione.

Siano

$$
x=x_0+\frac{b}{d}t,
\qquad
y=y_0-\frac{a}{d}t.
$$

Allora

$$
\begin{aligned}
ax+by
&=a\left(x_0+\frac{b}{d}t\right)
+b\left(y_0-\frac{a}{d}t\right)\\
&=ax_0+\frac{ab}{d}t+by_0-\frac{ab}{d}t\\
&=ax_0+by_0\\
&=c.
\end{aligned}
$$

I termini con $t$ si cancellano. Quindi ogni valore intero di $t$ dà una soluzione.

La parametrizzazione descrive dunque esattamente tutte le soluzioni intere.

---

## 10. Forma geometrica

L’equazione

$$
ax+by=c
$$

rappresenta una retta nel piano cartesiano. Le soluzioni diofantee sono i punti della retta con entrambe le coordinate intere.

Se $(x_0,y_0)$ è una soluzione particolare, tutte le altre si ottengono traslando questo punto lungo il vettore

$$
\left(\frac{b}{d},-\frac{a}{d}\right).
$$

Infatti:

$$
(x,y)
=
(x_0,y_0)
+t\left(\frac{b}{d},-\frac{a}{d}\right),
\qquad t\in\mathbb{Z}.
$$

Il vettore di traslazione è parallelo alla retta, perché

$$
a\frac{b}{d}+b\left(-\frac{a}{d}\right)=0.
$$

La condizione $t\in\mathbb{Z}$ seleziona proprio i punti a coordinate intere sulla retta.

Quindi:

- se $d\nmid c$, la retta non contiene punti del reticolo $\mathbb{Z}^2$;
- se $d\mid c$, contiene infiniti punti del reticolo;
- trovata una soluzione particolare, tutte le altre si ottengono con traslazioni intere lungo il vettore indicato.

---

## 11. Algoritmo pratico per risolvere un’equazione

Per risolvere concretamente

$$
ax+by=c,
$$

si procede così.

### Passo 1: calcolare il massimo comune divisore

Calcolare

$$
d=\gcd(a,b).
$$

### Passo 2: verificare la condizione di esistenza

Controllare se

$$
d\mid c.
$$

- Se $d\nmid c$, non esistono soluzioni intere.
- Se $d\mid c$, si prosegue.

### Passo 3: trovare i coefficienti di Bézout

Con l’algoritmo di Euclide esteso, trovare $u,v\in\mathbb{Z}$ tali che

$$
au+bv=d.
$$

### Passo 4: ottenere una soluzione particolare

Scrivere

$$
c=d\gamma
$$

e moltiplicare l’identità di Bézout per $\gamma$:

$$
a(\gamma u)+b(\gamma v)=c.
$$

Una soluzione particolare è quindi

$$
(x_0,y_0)=(\gamma u,\gamma v).
$$

### Passo 5: scrivere tutte le soluzioni

Usare la formula

$$
\boxed{
\begin{aligned}
x&=x_0+\frac{b}{d}t,\\
y&=y_0-\frac{a}{d}t,
\end{aligned}
\qquad t\in\mathbb{Z}.
}
$$

---

## 12. Soluzioni diverse e parametrizzazioni diverse

Una stessa famiglia di soluzioni si può scrivere in modi che sembrano diversi.

Per esempio, cambiando il parametro da $t$ a $t+1$, oppure da $t$ a $t+k$ con $k\in\mathbb{Z}$, si ottiene una scrittura diversa ma la stessa collezione di punti, purché il cambio di parametro sia compatibile con la parametrizzazione.

Che due formule abbiano un aspetto diverso non vuol dire che descrivano soluzioni diverse: bisogna verificare se generano lo stesso insieme di coppie $(x,y)$.

Non serve nemmeno che le coordinate di una soluzione siano entrambe non nulle: sono ammesse anche soluzioni come

$$
x=0
\qquad\text{o}\qquad
y=0,
$$

quando soddisfano l’equazione.

---

## 13. Osservazioni metodologiche

Il passaggio più importante è distinguere bene tra:

1. **esistenza** di almeno una soluzione, data dalla condizione
   $$
   \gcd(a,b)\mid c;
   $$

2. **costruzione** di una soluzione particolare, ottenuta con Bézout;

3. **determinazione di tutte le soluzioni**, ottenuta studiando la differenza tra due soluzioni.

Date due soluzioni $(x,y)$ e $(x_0,y_0)$, la loro differenza soddisfa l’equazione omogenea

$$
a(x-x_0)+b(y-y_0)=0.
$$

Per questo la soluzione generale dell’equazione non omogenea è formata da:

- una soluzione particolare dell’equazione originale;
- più la soluzione generale dell’equazione omogenea $ax+by=0$.

La soluzione omogenea è

$$
(x,y)=t\left(\frac{b}{d},-\frac{a}{d}\right),
\qquad t\in\mathbb{Z}.
$$

Di conseguenza,

$$
\text{soluzione generale}
=
\text{soluzione particolare}
+
\text{soluzione omogenea}.
$$

Questa struttura è analoga a quella di altri problemi algebrici: si trova una soluzione particolare e poi si aggiungono tutte le soluzioni del problema omogeneo associato.
