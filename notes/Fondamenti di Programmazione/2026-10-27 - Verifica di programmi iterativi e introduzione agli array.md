---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-10-27'
title: Verifica di programmi iterativi e introduzione agli array
source: Lezione_12.pdf (slide 355-370)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-10-27 - Verifica di programmi iterativi e introduzione agli array.md
vault_hash: 5f082254722240cbe461905facfbe31d8aafefc7b60bd95f693e6af6d7177cea
---

# Verifica di programmi iterativi e introduzione agli array

La lezione applica il metodo della [[2026-10-26 - Correttezza totale dei cicli, funzioni di terminazione e programmi annotati|lezione 11]] a tre [[Programma annotato|programmi annotati]]: radice cubica intera, fattoriale e [[Massimo comun divisore|massimo comune divisore]]. Il filo conduttore è scegliere un [[Invariante di ciclo|invariante]] che descriva **che cosa rappresentano le variabili durante il calcolo**, aggiungendo i vincoli necessari alla terminazione. Nella seconda parte il linguaggio viene esteso con gli [[Array|array]] e con il controllo degli indici.

Si usa il linguaggio didattico del corso. I completamenti degli esercizi e le correzioni rispetto alle slide sono segnalati di volta in volta.

## 1. Calcolo della radice cubica intera

Le slide propongono, con $x$ intero non negativo e non modificato:

```text
{x >= 0}
a := 0;
b := 0;
y := 0;
while y <= x do
    y := y + 3 * a + 3 * b + 1;
    a := a + 2 * b + 1;
    b := b + 1
endw
```

### 1.1 Che cosa rappresentano le variabili

Le identità

$$
(b+1)^2=b^2+2b+1,
\qquad
(b+1)^3=b^3+3b^2+3b+1
$$

suggeriscono di mantenere $a=b^2$ e $y=b^3$. Se queste relazioni valgono prima del corpo, i nuovi valori sono

$$
y'=b^3+3b^2+3b+1=(b+1)^3,
\qquad a'=b^2+2b+1=(b+1)^2,
\qquad b'=b+1.
$$

Quindi dopo il corpo valgono ancora $a'=(b')^2$ e $y'=(b')^3$. **L'ordine degli assegnamenti conta**: `y` usa i vecchi valori di `a` e `b`, e `a` usa il vecchio valore di `b`.

Per collegare il calcolo a $x$, le slide scelgono

$$
J\equiv a=b^2\land y=b^3\land(b-1)^3\leq x.
$$

L'ultima congiunzione ricorda che il cubo precedente non supera $x$.

### 1.2 Inizializzazione e invarianza

All'inizio $a=b=y=0$: le prime due uguaglianze valgono e $(b-1)^3=-1\leq x$.

Prima di un'iterazione, $J$ e la guardia danno $b^3=y\leq x$. Dopo l'incremento di $b$, la terza congiunzione richiesta diventa

$$
(b'-1)^3=b^3\leq x,
$$

quindi anch'essa è preservata.

La stessa verifica si può organizzare all'indietro con l'[[Regola dell'assegnamento|assioma dell'assegnamento]]. Partendo da $J$ dopo il corpo si ottengono, nell'ordine inverso:

$$
\begin{aligned}
R_2&\equiv a=(b+1)^2\land y=(b+1)^3\land b^3\leq x,
&&\text{prima di }b:=b+1;\\
R_1&\equiv a+2b+1=(b+1)^2\land y=(b+1)^3\land b^3\leq x,
&&\text{prima di }a:=a+2b+1;\\
R_0&\equiv a+2b+1=(b+1)^2\\
&\quad\land y+3a+3b+1=(b+1)^3\land b^3\leq x,
&&\text{prima di }y:=y+3a+3b+1.
\end{aligned}
$$

Resta $J\land y\leq x\Rightarrow R_0$, che segue dalle due identità algebriche. Le espressioni del corpo sono tutte definite.

### 1.3 Il risultato effettivo e il refuso delle slide

All'uscita valgono $J$ e $y>x$, quindi

$$
(b-1)^3\leq x<b^3.
$$

Poiché il cubo è strettamente crescente, si ottiene

$$
\boxed{b-1=\left\lfloor\sqrt[3]{x}\right\rfloor}.
$$

**Correzione rispetto alle slide 355-356:** il codice riportato calcola in `b` la parte intera della radice cubica **più uno**. La postcondizione stampata $b=\lfloor\sqrt[3]{x}\rfloor$ è errata. Per esempio, con $x=0$ il corpo viene eseguito una volta e lascia $b=1$; con $x=8$ lascia $b=3$.

Se si vuole il risultato richiesto direttamente in `b`, basta aggiungere, dopo `endw`, l'assegnamento

```text
b := b - 1
```

Questa è una correzione aggiunta al programma delle slide. L'invariante descritto sopra riguarda il ciclo prima dell'assegnamento finale.

### 1.4 Terminazione: svolgimento aggiunto

Le slide lasciano per esercizio la [[Funzione di terminazione|funzione di terminazione]]. Possiamo rafforzare l'invariante in

$$
Inv\equiv J\land b\geq0\land x\geq0
$$

e scegliere

$$
expt=x+1-(b-1)^3.
$$

È un intero e da $(b-1)^3\leq x$ segue $expt\geq1$. Dopo un'iterazione $b'=b+1$, mentre $x$ non cambia, perciò

$$
expt'=x+1-b^3,
\qquad
expt-expt'=b^3-(b-1)^3=3b(b-1)+1>0
$$

per ogni intero $b\geq0$. L'invariante rafforzato si inizializza e si conserva; la guardia è sempre definita. Il ciclo termina.

La potenza cubica nella funzione di terminazione è solo una scrittura abbreviata: con gli operatori del linguaggio, $(b-1)^3$ diventa `(b-1)*(b-1)*(b-1)`.

## 2. Calcolo del fattoriale

La specifica è

$$
\{n\geq0\}\ C\ \{fatt=n!\},
$$

con $n$ intero non modificato. Il programma è

```text
fatt := 1;
x := 1;
while x <= n do
    fatt := fatt * x;
    x := x + 1
endw
```

All'inizio di ogni iterazione `fatt` contiene il prodotto degli interi già attraversati, cioè $(x-1)!$. Un invariante adatto è

$$
Inv\equiv fatt=(x-1)!\land1\leq x\leq n+1.
$$

*Correzioni rispetto alla slide 359:* il limite inferiore $1$ rende sempre definito $(x-1)!$. Inoltre scegliamo **$expt=n+1-x$**: $n-x$ varrebbe $-1$ nello stato finale $x=n+1$ e non rispetterebbe la regola del corso $Inv\Rightarrow expt\geq0$.

### 2.1 Verifica: svolgimento aggiunto

**Inizializzazione.** $x=1$ e $fatt=1=0!$; da $n\geq0$ segue $1\leq n+1$.

**Invarianza.** Se $fatt=(x-1)!$ e $x\leq n$, dopo la moltiplicazione si ha $fatt'=x!$. Dopo l'incremento $x'=x+1$, dunque

$$
fatt'=(x'-1)!.
$$

Inoltre $1\leq x'\leq n+1$.

**Terminazione.** Da $x\leq n+1$ segue $n+1-x\geq0$. Ogni iterazione diminuisce questa quantità di $1$.

**Uscita.** La guardia falsa dà $x>n$; insieme a $x\leq n+1$ e al fatto che $x$ è intero si ottiene $x=n+1$. Pertanto $fatt=(x-1)!=n!$.

Per $n=0$ non si entra nel ciclo e si ottiene correttamente $0!=1$.

## 3. Massimo comune divisore mediante sottrazioni

La specifica è

$$
\{a>0\land b>0\}\ C\ \{x=\operatorname{mcd}(a,b)\},
$$

con $a,b$ interi positivi non modificati dal programma. Si usano le proprietà

$$
\begin{aligned}
\operatorname{mcd}(x,x)&=x &&x>0;\\
\operatorname{mcd}(x,y)&=\operatorname{mcd}(x-y,y) &&x>y>0;\\
\operatorname{mcd}(x,y)&=\operatorname{mcd}(x,y-x) &&y>x>0.
\end{aligned}
$$

```text
x := a;
y := b;
while x != y do
    if x > y
        then x := x - y
        else y := y - x
    fi
endw
```

### 3.1 Come ricavare l'invariante dalla postcondizione

Se all'uscita $x=y$, allora $\operatorname{mcd}(x,y)=x$. Basta dunque conservare il valore del MCD durante tutto il ciclo:

$$
Inv\equiv x>0\land y>0\land
\operatorname{mcd}(x,y)=\operatorname{mcd}(a,b).
$$

Le congiunzioni $x>0$ e $y>0$ servono sia alle proprietà usate sia alla prova di terminazione.

### 3.2 Verifica: svolgimento aggiunto

L'inizializzazione rende vera l'uguaglianza dei MCD e assicura la positività.

Nel corpo si distinguono due casi:

- Se $x>y$, il nuovo valore $x-y$ è positivo e $\operatorname{mcd}(x-y,y)=\operatorname{mcd}(x,y)$.
- Se il ramo `else` viene eseguito, da $x\neq y$ e $\neg(x>y)$ segue $x<y$. Quindi $y-x>0$ e $\operatorname{mcd}(x,y-x)=\operatorname{mcd}(x,y)$.

La funzione di terminazione è

$$
expt=x+y.
$$

È positiva sotto $Inv$. Nel primo ramo il nuovo valore è $(x-y)+y=x<x+y$; nel secondo è $x+(y-x)=y<x+y$. Quindi il ciclo termina.

All'uscita $x=y>0$, perciò

$$
\operatorname{mcd}(a,b)=\operatorname{mcd}(x,y)
=\operatorname{mcd}(x,x)=x.
$$

### 3.3 La tecnica generale mostrata dall'esempio

Una strategia utile è conservare una quantità del problema:

$$
F(x_1,\ldots,x_m)=F(a_1,\ldots,a_m),
$$

dove gli $a_i$ sono i dati iniziali non modificati e gli $x_i$ sono variabili di lavoro. Si inizializza con $x_i:=a_i$ e si sceglie una guardia la cui falsità renda semplice estrarre il risultato. Nel MCD, la quantità conservata è $\operatorname{mcd}$ e la condizione finale è $x=y$.

La sola uguaglianza può richiedere un rafforzamento con vincoli di dominio o di segno, come $x>0\land y>0$.

## 4. Ricavare un assegnamento dalla proprietà da conservare

Si cerca $E$ tale che

```text
{x*y + p*q = n}
x := x - p;
q := E
{x*y + p*q = n}
```

L'aggiornamento di `x` toglie $py$ alla quantità $xy+pq$. Per compensare dobbiamo aumentare $q$ di $y$:

$$
\boxed{E=q+y}.
$$

Infatti, indicando con $x,q$ i valori iniziali,

$$
(x-p)y+p(q+y)=xy-py+pq+py=xy+pq=n.
$$

La stessa soluzione si verifica all'indietro con (ass) e (seq):

```text
{(x-p)*y + p*(q+y) = n}
x := x - p;
{x*y + p*(q+y) = n}
q := q + y
{x*y + p*q = n}
```

La prima asserzione equivale alla precondizione. Non ci sono divisioni né accessi ad array, quindi tutte le espressioni sono definite. Se $p=0$ la conservazione non pone vincoli sul valore assegnato a `q`, purché l'espressione sia definita; $q+y$ funziona senza problemi anche in quel caso.

*Precisazione aggiunta sulla sostituzione:* per un'espressione incognita $E$ che contenesse `x`, risalendo anche attraverso `x := x-p` bisognerebbe sostituire $x-p$ dentro $E$. La soluzione $q+y$ non contiene `x`, quindi questo problema non si presenta.

## 5. Array come sequenze omogenee

Un [[Array|**array**]] rappresenta una sequenza finita di valori tutti dello stesso tipo. Astrattamente è una funzione

$$
v:[a,b)\to A,
$$

dove $[a,b)$ indica gli indici naturali $i$ tali che $a\leq i<b$, e $A$ è $\mathbb Z$ oppure $\mathrm{Bool}$. Il dominio si indica con $\operatorname{dom}(v)$.

Il numero di elementi è $b-a$: l'estremo destro $b$ **non è un indice valido**. Se $a=b$, l'array è vuoto.

Nel linguaggio si scrive

```text
v : array [a,b) of int
w : array [a,b) of bool
```

Per esempio, `v : array [0,4) of int` ha indici $0,1,2,3$.

### 5.1 Accesso agli elementi: sintassi

Se `v` è un identificatore di array ed `E` un'espressione di tipo intero, allora

```text
v[E]
```

è un'espressione che denota l'elemento all'indice ottenuto valutando `E`. Esempi: `voto[4]`, `temperatura[x+1]`, `v[v[0]+v[1]]`.

L'ultimo esempio è lecito perché un valore letto dall'array, se intero, può servire a calcolare un altro indice. Resta però da verificare che gli indici siano validi.

### 5.2 Estensione dello stato e della semantica

Prima lo [[Stato|stato]] associava a un identificatore un intero o un booleano. Ora, se `v` identifica un array, $\sigma(v)$ è una **funzione sugli indici**:

$$
\sigma(v):\operatorname{dom}(v)\to A.
$$

Per esempio,

$$
\sigma(v)=\{0\mapsto2,\ 1\mapsto1,\ 2\mapsto10,\ 3\mapsto6\}.
$$

La semantica dell'accesso è

$$
\mathcal E(v[E],\sigma)
=\sigma(v)\bigl(\mathcal E(E,\sigma)\bigr),
$$

purché $\mathcal E(E,\sigma)$ sia definito e appartenga a $\operatorname{dom}(v)$.

### 5.3 Esempio di accesso annidato

Con l'array di prima,

$$
\begin{aligned}
\mathcal E(v[v[0]+v[1]],\sigma)
&=\sigma(v)\bigl(\sigma(v)(0)+\sigma(v)(1)\bigr)\\
&=\sigma(v)(2+1)\\
&=\sigma(v)(3)\\
&=6.
\end{aligned}
$$

Gli indici $0$, $1$ e l'indice calcolato $3$ appartengono tutti al dominio. Occhio: non basta controllare gli accessi interni, anche il risultato usato come indice esterno deve essere valido.

## 6. Estensione di $\mathrm{def}$ agli array

Si aggiunge la clausola

$$
\boxed{\mathrm{def}(v[E])
=\mathrm{def}(E)\land E\in\operatorname{dom}(v)}.
$$

Ci sono ora due possibili cause di indefinitezza nelle espressioni staticamente corrette:

| Espressione | Condizione di definitezza |
|---|---|
| $E\ \mathtt{div}\ E'$ oppure $E\ \mathtt{mod}\ E'$ | $\mathrm{def}(E)\land\mathrm{def}(E')\land E'\neq0$ |
| $v[E]$ | $\mathrm{def}(E)\land E\in\operatorname{dom}(v)$ |

Per un array di dominio $[0,n)$, per esempio,

$$
\mathrm{def}(v[x+1])\equiv0\leq x+1<n.
$$

*Esplicitazione aggiunta dell'esempio annidato:* prima di semplificare grazie allo stato concreto,

$$
\mathrm{def}(v[v[0]+v[1]])
\equiv 0\in\operatorname{dom}(v)
\land1\in\operatorname{dom}(v)
\land v[0]+v[1]\in\operatorname{dom}(v).
$$

Nella prossima lezione questa estensione servirà per verificare anche gli assegnamenti a singoli elementi, come `v[k] := E`.

## Fonte e collegamenti

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 12, 27 ottobre 2026, slide 355-370, file originale `/Users/michelangelogubinelli/Downloads/Lezione_12.pdf`.
- Le correzioni alla radice cubica e al fattoriale sono motivate nelle rispettive sezioni; non sono risultati dichiarati dalle slide. La funzione di terminazione della radice cubica e le verifiche complete degli esercizi sono svolgimenti aggiunti.
- Seguito: [[2026-10-29 - Aggiornamento degli array e tecniche di costruzione dei cicli]].
