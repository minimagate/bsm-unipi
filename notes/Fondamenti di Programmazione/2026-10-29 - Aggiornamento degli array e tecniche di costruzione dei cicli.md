---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-10-29'
title: Aggiornamento degli array e tecniche di costruzione dei cicli
source: Lezione_13.pdf (slide 371-405)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-10-29 - Aggiornamento degli array e tecniche di costruzione dei cicli.md
vault_hash: 3424263af179e85796413c0fb99b0b219137c9da890812bc3345344f177102b5
---

# Aggiornamento degli array e tecniche di costruzione dei cicli

La [[2026-10-27 - Verifica di programmi iterativi e introduzione agli array|lezione 12]] ha introdotto gli [[Array|array]] e la semantica della lettura di un elemento. Questa lezione tratta la **modifica di singoli elementi** e sviluppa alcune tecniche per costruire programmi a partire dalle specifiche: scomporre la postcondizione, sostituire una costante con una variabile e rafforzare gli [[Invariante di ciclo|invarianti]] con variabili ausiliarie.

I programmi usano il linguaggio didattico del corso. Attenzione: le funzioni matematiche nelle asserzioni, come $\operatorname{fib}$, non sono per questo operazioni disponibili nei comandi. Gli svolgimenti aggiunti agli esercizi delle slide sono segnalati.

## 1. Aggiornamento selettivo degli array

Gli elementi di un array possono comparire nelle espressioni, per esempio

```text
v[z+1] * y + x
v[2] < w[3]
```

Gli operatori del linguaggio lavorano sui singoli valori, non su intere sequenze: `v + w` non è un'espressione ammessa.

Si estende l'assegnamento con

```text
v[E] := E'
```

dove `v` è un identificatore di array, `E` è un indice intero ed `E'` ha il tipo degli elementi dell'array. Il comando modifica **solo la posizione indicata**: è l'[[Aggiornamento di un array|aggiornamento selettivo]].

### 1.1 Semantica: valutare prima, aggiornare dopo

Nello stato iniziale $\sigma$ si calcolano

$$
j=\mathcal E(E,\sigma),\qquad d=\mathcal E(E',\sigma).
$$

Entrambi devono essere definiti e $j\in\operatorname{dom}(v)$. Si costruisce poi la sequenza $w=\sigma(v)[d/j]$, cioè

$$
w(i)=
\begin{cases}
d&\text{se }i=j,\\
\sigma(v)(i)&\text{se }i\neq j.
\end{cases}
$$

Il nuovo stato associa a `v` questa sequenza:

$$
\mathcal C(v[E]:=E',\sigma)
=\sigma\bigl[\sigma(v)[\mathcal E(E',\sigma)/\mathcal E(E,\sigma)]/v\bigr].
$$

Nella formula ci sono due aggiornamenti distinti: quello **interno** modifica un elemento della sequenza, quello **esterno** aggiorna il valore dell'identificatore `v` nello stato. Indice e valore a destra vengono valutati entrambi nello stato precedente all'assegnamento.

### 1.2 Assioma e regola di verifica

Scriviamo $w=v[E'/E]$ per la sequenza ottenuta aggiornando `v` all'indice `E` con il valore `E'`. L'assioma è

$$
\{\mathrm{def}(E)\land\mathrm{def}(E')\land
E\in\operatorname{dom}(v)\land P[w/v]\}\
v[E]:=E'\ \{P\}.
$$

Rafforzando la precondizione si ottiene la regola

$$
\frac{R\Rightarrow\mathrm{def}(E)\land\mathrm{def}(E')\land
E\in\operatorname{dom}(v)\land P[w/v]}
{\{R\}\ v[E]:=E'\ \{P\}}
\quad w=v[E'/E].
$$

La sostituzione riguarda **l'intera sequenza** nell'asserzione: per ogni indice $i$, il nuovo elemento è $E'$ se $i=E$, ed è il vecchio $v[i]$ altrimenti. È questa distinzione che permette di verificare postcondizioni [[Quantificatore|quantificate]] su più posizioni.

## 2. Esempio: estendere un prefisso di somme

Sia `a : array [0,n) of int`. Vogliamo verificare

$$
\left\{1\leq k<n\land
\forall i\in[0,k).\ a[i]=\sum_{j=0}^{i}j\right\}
$$

```text
a[k] := a[k-1] + k
```

$$
\left\{\forall i\in[0,k].\ a[i]=\sum_{j=0}^{i}j\right\}.
$$

L'array contiene già le somme nelle posizioni prima di `k`; il comando calcola la successiva.

**Definitezza.** Da $1\leq k<n$ segue che sia $k$ sia $k-1$ appartengono a $[0,n)$: sono leciti la scrittura e l'accesso a destra.

**Postcondizione.** Sia $w=a[(a[k-1]+k)/k]$ la sequenza aggiornata. Dividiamo gli indici in due casi:

- Se $0\leq i<k$, l'aggiornamento non tocca $i$, quindi $w[i]=a[i]=\sum_{j=0}^{i}j$.
- Se $i=k$, allora
  $$
  w[k]=a[k-1]+k
  =\left(\sum_{j=0}^{k-1}j\right)+k
  =\sum_{j=0}^{k}j.
  $$

Questo è lo schema tipico delle prove sugli array: si verificano separatamente **la posizione modificata e quelle che restano invariate**.

## 3. Incrementare tutti gli elementi di un array

Sia `a : array [0,n) of int` e sia $V$ una variabile di specifica che rappresenta la sequenza iniziale, con lo stesso dominio. La specifica è

$$
\{n\geq0\land\forall k\in[0,n).\ a[k]=V[k]\}\ C\
\{\forall k\in[0,n).\ a[k]=V[k]+1\}.
$$

Il programma proposto è

```text
x := 0;
while x < n do
    a[x] := a[x] + 1;
    x := x + 1
endw
```

L'invariante divide l'array in una parte già elaborata e una ancora da elaborare:

$$
\begin{aligned}
Inv\equiv{}&0\leq x\leq n\\
&\land\forall k\in[0,x).\ a[k]=V[k]+1\\
&\land\forall k\in[x,n).\ a[k]=V[k].
\end{aligned}
$$

La seconda parte è importante: quando leggiamo `a[x]` dobbiamo sapere che contiene ancora il valore iniziale $V[x]$.

### 3.1 Verifica: svolgimento aggiunto

**Inizializzazione.** Con $x=0$, il prefisso elaborato è vuoto e la proprietà sulla parte restante coincide con la precondizione.

**Invarianza.** Sotto $Inv\land x<n$ si ha $x\in[0,n)$, quindi l'accesso e la scrittura sono definiti. Dopo l'aggiornamento:

$$
\forall k\in[0,x+1).\ a[k]=V[k]+1,
\qquad
\forall k\in[x+1,n).\ a[k]=V[k].
$$

Infatti le posizioni $k<x$ non cambiano, la posizione $x$ diventa $V[x]+1$ e le posizioni $k>x$ restano uguali a $V[k]$. Dopo `x := x+1` si ritrova $Inv$.

**Terminazione.** $expt=n-x$ è non negativa sotto l'invariante e diminuisce di $1$ a ogni iterazione; l'aggiornamento dell'array non modifica `x`.

**Uscita.** Da $x\leq n$ e $\neg(x<n)$ segue $x=n$: l'intero array appartiene al prefisso elaborato. Se $n=0$, la specifica è soddisfatta senza eseguire il corpo.

## 4. Costruire un ciclo dalla postcondizione

Data una specifica $\{pre\}\ C\ \{post\}$, l'idea per [[Costruzione di un ciclo|costruire un ciclo]] è cercare una scomposizione

$$
P\land G\Rightarrow post
$$

in cui $P$ possa essere mantenuta come invariante e $G$ possa essere ottenuta negando una guardia esprimibile nel linguaggio:

$$
G\equiv\neg E.
$$

Si costruiscono allora l'inizializzazione e il corpo:

```text
{pre}
CI;
{inv: P} {ft: expt}
while E do
    C
endw
{P ∧ G}
{post}
```

Restano sempre da verificare la definitezza, l'invarianza e la terminazione. Nota bene: è una strategia di progettazione, non una ricetta che risolve da sola ogni problema.

### 4.1 Esempio: ricavare il quoziente introducendo il resto

La postcondizione $q=x\ \mathtt{div}\ y$, sotto $x\geq0$ e $y>0$, equivale a

$$
\exists r.\ x=qy+r\land0\leq r<y.
$$

Introduciamo una variabile di programma `r` che faccia da testimone dell'esistenziale e separiamo

$$
\underbrace{x=qy+r\land r\geq0}_{Inv}
\land\underbrace{r<y}_{G}.
$$

La guardia è quindi $E\equiv r\geq y$. L'inizializzazione è `q := 0; r := x`, il corpo è `q := q+1; r := r-y` e la funzione di terminazione è $r$.

La dimostrazione completa è nella [[2026-10-26 - Correttezza totale dei cicli, funzioni di terminazione e programmi annotati#6. Divisione intera mediante sottrazioni|lezione 11]]. Per la correttezza totale si conserva anche $y>0$, necessario alla diminuzione del resto.

## 5. Rimpiazzare una costante con una variabile: somma di un array

Con `a : array [0,n) of int`, $n$ non modificato e $n\geq0$, si vuole

$$
s=\sum_{i=0}^{n-1}a[i].
$$

Rimpiazziamo nella postcondizione la costante $n$ con una variabile `x`:

$$
s=\sum_{i=0}^{x-1}a[i].
$$

Questa proprietà, insieme a $x=n$, implica il risultato, e la guardia candidata è $x\neq n$. Per garantire indici validi e una funzione di terminazione naturale rafforziamo l'invariante:

$$
Inv\equiv s=\sum_{i=0}^{x-1}a[i]\land0\leq x\leq n,
\qquad expt=n-x.
$$

```text
{n >= 0}
x := 0;
s := 0;
while x != n do
    s := s + a[x];
    x := x + 1
endw
```

**Inizializzazione.** Con $x=0$ la somma è vuota e vale $0$.

**Invarianza e definitezza.** Da $0\leq x\leq n$ e $x\neq n$ segue $0\leq x<n$. L'accesso `a[x]` è quindi definito. Dopo l'aggiunta,

$$
s'=\sum_{i=0}^{x-1}a[i]+a[x]=\sum_{i=0}^{x}a[i].
$$

Dopo l'incremento $x'=x+1$, questa è la somma fino a $x'-1$ e vale ancora $0\leq x'\leq n$.

**Terminazione e uscita.** $n-x$ è non negativa e diminuisce di $1$. All'uscita $x=n$ e si ottiene la somma richiesta. L'array non viene modificato; per $n=0$ il risultato è $0$.

Il rafforzamento $0\leq x\leq n$ serve a tre cose: controllare gli indici, limitare il contatore e rendere non negativa la funzione di terminazione.

## 6. Rafforzare l'invariante con una variabile ausiliaria: Fibonacci

La [[Successione di Fibonacci|successione di Fibonacci]] è definita da

$$
\operatorname{fib}(0)=0,\qquad\operatorname{fib}(1)=1,
\qquad
\operatorname{fib}(j)=\operatorname{fib}(j-1)+\operatorname{fib}(j-2)
\quad(j\geq2).
$$

La specifica è

$$
\{k\geq1\}\ C\ \{x=\operatorname{fib}(k)\},
$$

con $k$ intero non modificato. Una prima idea è mantenere

$$
x=\operatorname{fib}(i)\land1\leq i\leq k,
\qquad E\equiv i\neq k,
\qquad expt=k-i.
$$

Per avanzare da $i$ a $i+1$ dovremmo calcolare

$$
\operatorname{fib}(i+1)=x+\operatorname{fib}(i-1).
$$

Ma `fib(i-1)` **non è un'espressione del linguaggio**. Introduciamo quindi una variabile `y` che ne conservi il valore:

$$
Inv\equiv x=\operatorname{fib}(i)
\land y=\operatorname{fib}(i-1)
\land1\leq i\leq k.
$$

### 6.1 Conservare i vecchi valori durante gli assegnamenti

L'aggiornamento desiderato è, in termini dei vecchi valori,

$$
x'=x+y,\qquad y'=x.
$$

La sequenza `x := x+y; y := x` non va bene, perché il secondo comando leggerebbe il nuovo valore di `x`. Bisogna salvare il vecchio valore:

```text
temp := x;
x := x + y;
y := temp
```

Dopo questa sequenza $x=\operatorname{fib}(i+1)$ e $y=\operatorname{fib}(i)$; incrementando `i` si ripristina l'invariante.

### 6.2 Programma e verifica

```text
{k >= 1}
x := 1;
i := 1;
y := 0;
while i != k do
    temp := x;
    x := x + y;
    y := temp;
    i := i + 1
endw
{x = fib(k)}
```

*Completamento della prova lasciata per esercizio.* L'inizializzazione usa $\operatorname{fib}(1)=1$ e $\operatorname{fib}(0)=0$. Se $i<k$, il corpo produce la coppia successiva e porta `i` a $i+1\leq k$. $expt=k-i$ è non negativa e diminuisce di $1$; tutte le espressioni del corpo sono definite. All'uscita $i=k$, quindi $x=\operatorname{fib}(k)$.

Per $k=1$ il ciclo non viene eseguito. Il caso $k=0$ è escluso dalla specifica proposta.

## 7. Bandiera a due colori: partizionare un array

Sia `a : array [0,n) of int`. Vogliamo permutarne gli elementi in modo che prima ci siano tutti i valori **negativi**, poi quelli **positivi o nulli**.

Sia $A$ la sequenza iniziale, rappresentata da una variabile di specifica. $\operatorname{perm}(a,A)$ significa che le due sequenze hanno gli stessi elementi con le stesse molteplicità, eventualmente in ordine diverso.

La specifica è

$$
\{n\geq0\land a=A\}\ C\
\left\{
\begin{aligned}
&\operatorname{perm}(a,A)\land0\leq x\leq n\\
&\land\forall i\in[0,x).\ a[i]<0\\
&\land\forall i\in[x,n).\ a[i]\geq0
\end{aligned}
\right\}.
$$

### 7.1 Due confini e tre porzioni

Usiamo due confini `x` e `y`, con invariante

$$
\begin{aligned}
Inv\equiv{}&\operatorname{perm}(a,A)\land0\leq x\leq y\leq n\\
&\land\forall i\in[0,x).\ a[i]<0\\
&\land\forall i\in[y,n).\ a[i]\geq0.
\end{aligned}
$$

| Intervallo | Che cosa sappiamo |
|---|---|
| $[0,x)$ | Tutti gli elementi sono negativi |
| $[x,y)$ | Gli elementi sono ancora da classificare |
| $[y,n)$ | Tutti gli elementi sono non negativi |

La guardia è $x\neq y$ e la funzione di terminazione è $y-x$, la lunghezza della parte ancora da esaminare. L'inizializzazione `x := 0; y := n` rende vuote entrambe le porzioni già classificate.

### 7.2 Costruzione del corpo

Sotto $Inv\land x\neq y$ si ha $x<y$, quindi sia $x$ sia $y-1$ sono indici validi.

- Se $a[x]<0$, basta incrementare `x`: l'elemento entra nel prefisso negativo.
- Se $a[x]\geq0$, va portato nella parte destra. Si scambia `a[x]` con `a[y-1]` e si decrementa `y`.

Nel secondo caso `x` **non avanza**: il valore arrivato da destra deve ancora essere classificato. Una semplice copia `a[y-1] := a[x]` perderebbe il vecchio elemento di destra, mentre lo scambio conserva $\operatorname{perm}(a,A)$.

### 7.3 Programma completo

```text
{n >= 0 ∧ a = A}
x := 0;
y := n;
while x != y do
    if a[x] < 0
        then x := x + 1
        else temp := a[y-1];
             a[y-1] := a[x];
             a[x] := temp;
             y := y - 1
    fi
endw
```

In entrambi i rami l'invariante è preservata e $y-x$ diminuisce di $1$, restando non negativa. Lo scambio è corretto anche quando $x=y-1$: in quel caso scambia una posizione con sé stessa. All'uscita $x=y$ e la porzione sconosciuta è vuota.

*Correzioni rispetto alle slide:* nella slide 395 i segni dei due casi sono invertiti; i casi coerenti con l'invariante e con il codice della slide 396 sono $a[x]<0$ e $a[x]\geq0$. Nella slide 397 l'ultimo quantificatore deve riferirsi ad $a[i]$, non ad $a[y]$, e il confine finale soddisfa $x\in[0,n]$, non $[0,n)$. Il valore $x=n$ è possibile se tutti gli elementi sono negativi; $n=0$ deve essere ammesso.

## 8. Esercizio svolto: bandiera a tre colori

La slide 398 chiede di estendere la partizione a tre categorie: negativi, zeri e positivi. **Il seguente svolgimento è aggiunto alle slide.**

### 8.1 Specifica e invariante

Vogliamo ottenere, per due confini finali $x,z$,

$$
\begin{aligned}
&\operatorname{perm}(a,A)\land0\leq x\leq z\leq n\\
&\land\forall i\in[0,x).\ a[i]<0\\
&\land\forall i\in[x,z).\ a[i]=0\\
&\land\forall i\in[z,n).\ a[i]>0.
\end{aligned}
$$

Durante il calcolo introduciamo un terzo confine `y` e conserviamo

$$
\begin{aligned}
Inv\equiv{}&\operatorname{perm}(a,A)\land0\leq x\leq z\leq y\leq n\\
&\land\forall i\in[0,x).\ a[i]<0\\
&\land\forall i\in[x,z).\ a[i]=0\\
&\land\forall i\in[y,n).\ a[i]>0.
\end{aligned}
$$

La parte sconosciuta è $[z,y)$. Usiamo guardia $z\neq y$, funzione di terminazione $y-z$ e inizializzazione $x=z=0$, $y=n$.

### 8.2 Corpo e verifica

```text
{n >= 0 ∧ a = A}
x := 0;
z := 0;
y := n;
while z != y do
    if a[z] < 0
        then temp := a[x];
             a[x] := a[z];
             a[z] := temp;
             x := x + 1;
             z := z + 1
        else if a[z] = 0
                 then z := z + 1
                 else y := y - 1;
                      temp := a[y];
                      a[y] := a[z];
                      a[z] := temp
             fi
    fi
endw
```

Se `a[z]` è negativo, lo scambio lo porta all'inizio della zona degli zeri. Quando $x<z$, il vecchio `a[x]` è zero e può passare nella posizione `z`; quando $x=z$, lo scambio lascia quella posizione invariata. Incrementando entrambi i confini si ripristinano le zone.

Se `a[z]` è zero, basta allargare la zona degli zeri. Se è positivo, si restringe da destra la zona sconosciuta e si porta il positivo nella posizione appena aggiunta al suffisso. In questo caso `z` resta fermo per riesaminare il valore scambiato da destra.

Sotto la guardia $z<y$, tutti gli indici letti o scritti sono validi: nel ramo positivo il nuovo `y` è il vecchio $y-1\geq z$. Ogni ramo conserva gli elementi tramite scambi e diminuisce $y-z$ di $1$. All'uscita $z=y$, quindi la zona sconosciuta è vuota e vale la postcondizione.

## 9. Una successione definita dimezzando l'indice

Le ultime slide considerano la successione

$$
f(j)=
\begin{cases}
0&j=0,\\
1&j=1,\\
f(j/2)&j\geq2\land j\text{ pari},\\
f((j-1)/2)+f((j+1)/2)&j\geq2\land j\text{ dispari}.
\end{cases}
$$

La specifica è $\{n\geq0\}\ C\ \{h=f(n)\}$, con $n$ intero non modificato.

Far crescere un indice da $0$ a $n$, come per Fibonacci, porterebbe a conservare valori a indici dimezzati, e le slide osservano che così l'invariante diventa difficile da preservare. Conviene invece seguire la struttura della ricorrenza e **far diminuire l'indice**.

### 9.1 Conservare una combinazione di due valori consecutivi

Nell'esempio delle slide,

$$
\begin{aligned}
f(19)&=f(9)+f(10)\\
&=f(4)+2f(5)\\
&=3f(2)+2f(3)\\
&=5f(1)+2f(2)\\
&=7.
\end{aligned}
$$

Le espressioni intermedie combinano due termini consecutivi con coefficienti che cambiano, e questo suggerisce

$$
Inv\equiv0\leq x\leq n\land
f(n)=k\,f(x)+h\,f(x+1).
$$

Qui $k$ è una variabile di lavoro, distinta dal parametro $k$ dell'esempio di Fibonacci.

L'inizializzazione

```text
x := n;
k := 1;
h := 0
```

stabilisce l'invariante. La guardia è $x\neq0$. All'uscita,

$$
f(n)=k f(0)+h f(1)=h,
$$

quindi il risultato è già nella variabile richiesta.

### 9.2 Derivare gli aggiornamenti per parità

Poniamo $q=x\ \mathtt{div}\ 2$.

**Caso pari.** Sotto la guardia, $x=2q\geq2$, quindi

$$
\begin{aligned}
k f(x)+h f(x+1)
&=k f(q)+h\bigl(f(q)+f(q+1)\bigr)\\
&=(k+h)f(q)+h f(q+1).
\end{aligned}
$$

Manteniamo l'invariante con `k := h+k`, lasciando `h` invariata, e poi `x := x div 2`.

**Caso dispari — svolgimento aggiunto dell'esercizio.** Se $x=2q+1$,

$$
\begin{aligned}
k f(x)+h f(x+1)
&=k\bigl(f(q)+f(q+1)\bigr)+h f(q+1)\\
&=k f(q)+(k+h)f(q+1).
\end{aligned}
$$

Quindi lasciamo `k` invariata, eseguiamo `h := h+k` e poi dimezziamo `x`. L'identità usata vale anche per $x=1$: in quel caso $q=0$ e $f(1)=f(0)+f(1)$ per i valori iniziali.

### 9.3 Programma completo e terminazione

```text
{n >= 0}
x := n;
k := 1;
h := 0;
while x != 0 do
    if x mod 2 = 0
        then k := h + k
        else h := h + k
    fi;
    x := x div 2
endw
{h = f(n)}
```

Scegliamo come [[Funzione di terminazione|funzione di terminazione]] $expt=x$. L'invariante garantisce $x\geq0$ e la guardia implica $x>0$, perciò

$$
0\leq x\ \mathtt{div}\ 2<x.
$$

La funzione di terminazione diminuisce strettamente; le divisioni e il modulo hanno divisore costante $2\neq0$, quindi sono definiti. Per $n=0$ il ciclo non viene eseguito e si ottiene $h=0=f(0)$.

Qui $f$ compare soltanto nella specifica e nell'invariante: il programma usa somme, divisione intera e modulo per calcolarne il valore.

## Fonte e precisazioni

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 13, 29 ottobre 2026, slide 371-405, file originale `/Users/michelangelogubinelli/Downloads/Lezione_13.pdf`.
- La prova dell'incremento dell'array, il completamento della verifica di Fibonacci, la soluzione della bandiera a tre colori e la derivazione del caso dispari dell'ultima successione sono svolgimenti aggiunti degli esercizi proposti.
- I refusi che cambiano il significato dell'esempio della bandiera a due colori sono segnalati nella sezione dedicata. Il codice è normalizzato alla sintassi del corso: assegnamenti separati da `;`, inizializzazioni sequenziali e `y := temp` nell'esempio di Fibonacci.
