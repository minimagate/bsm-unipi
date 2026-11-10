---
type: lecture-note
course: Aritmetica
date: '2026-10-21'
title: Relazioni di equivalenza e strutture quoziente
source_transcript: _transcripts/Aritmetica/2026-10-22 - Relazioni di equivalenza e strutture quoziente.md
source_hash: sha256:2079632a9956e76f9f7c51f5f66cb232365193288bc3c7869f776df0e419ab32
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-22T11:57:48.864Z'
vault_path: Notes/Aritmetica/Lectures/2026-10-21 - Relazioni di equivalenza e strutture quoziente.md
vault_hash: 45097a28d2815b87ef2a8920e842d2a6e2495d4ab682e35613f4a75d8207c89a
---

# Relazioni di equivalenza e strutture quoziente

## 1. Relazioni di equivalenza

Una relazione $R$ su un [[Insieme|insieme]] $A$ è una proprietà che permette di stabilire, per ogni coppia $(x,y)\in A\times A$, se $x$ è in relazione con $y$. Si scrive

$$
xRy
$$

oppure, più esplicitamente,

$$
x\mathrel{R}y.
$$

Una relazione $R$ su $A$ si dice **[[Relazione di equivalenza|relazione di equivalenza]]** se soddisfa le tre proprietà seguenti:

1. **Riflessività**:
   $$
   \forall x\in A,\qquad xRx.
   $$

2. **Simmetria**:
   $$
   \forall x,y\in A,\qquad xRy\Longrightarrow yRx.
   $$

3. **Transitività**:
   $$
   \forall x,y,z\in A,\qquad
   (xRy\ \text{e}\ yRz)\Longrightarrow xRz.
   $$

La simmetria permette di passare da $xRy$ a $yRx$; la transitività permette di concatenare relazioni già note.

L’idea di fondo è che una relazione di equivalenza consente di considerare "uguali", ai fini della relazione, elementi che nell’insieme iniziale restano distinti.

> [!example] Esempio
> Su $\mathbb Z$ la relazione "$x$ e $y$ hanno lo stesso resto nella divisione per $2$" è di equivalenza (pari con pari, dispari con dispari). Invece la relazione $x\leq y$ è riflessiva e transitiva ma non simmetrica ($1\leq2$ però $2\not\leq1$), quindi non è di equivalenza.

> [!warning]
> Quando si scrive che due elementi sono "uguali" in un quoziente, non si sta dicendo che lo siano nell’insieme di partenza. Si sta dicendo che stanno nella stessa classe di equivalenza e che quindi, nella nuova struttura, vengono identificati.

---

## 2. Classi di equivalenza

Sia $R$ una relazione di equivalenza su un insieme $A$. Fissato $x\in A$, la **[[Classe di equivalenza|classe di equivalenza]] di $x$** rispetto a $R$ è l’insieme

$$
[x]_R=\{y\in A\mid yRx\}.
$$

Spesso, quando la relazione è chiara dal contesto, si scrive semplicemente $[x]$ oppure $\overline{x}$.

La classe $[x]$ raccoglie tutti gli elementi di $A$ equivalenti a $x$. In particolare, poiché $R$ è riflessiva, $x\in[x]$.

Ogni elemento della classe può fare da **rappresentante**. Una stessa classe può quindi avere molti rappresentanti, anche infiniti.

Per esempio, se $x$ e $y$ sono equivalenti, allora

$$
[x]=[y].
$$

Quindi la notazione $[x]$ non individua per forza un solo elemento dell’insieme originario: individua un insieme di elementi equivalenti tra loro.

### 2.1. Classi uguali o disgiunte

Un fatto fondamentale è il seguente.

### Teorema

Sia $R$ una relazione di equivalenza su $A$. Per ogni $x,y\in A$, le classi $[x]$ e $[y]$ sono:

- uguali, se $xRy$;
- disgiunte, se $x\not Ry$.

Equivalentemente,

$$
[x]\cap[y]\neq\varnothing
\quad\Longrightarrow\quad
[x]=[y].
$$

In forma compatta:

$$
[x]=[y]\quad\text{oppure}\quad [x]\cap[y]=\varnothing.
$$

Lo slogan da ricordare:

> **Le classi di equivalenza o coincidono o sono disgiunte.**

### Dimostrazione

Supponiamo che esista un elemento $z$ appartenente a entrambe le classi:

$$
z\in[x]\cap[y].
$$

Allora, per definizione di classe,

$$
zRx
\qquad\text{e}\qquad
zRy.
$$

Per simmetria, da $zRx$ segue $xRz$. Usando la transitività con $zRy$ si ottiene

$$
xRz
\quad\text{e}\quad
zRy
\quad\Longrightarrow\quad
xRy.
$$

Se $xRy$, i due elementi hanno la stessa classe:

$$
[x]=[y].
$$

La dimostrazione dell’implicazione

$$
xRy\Longrightarrow [x]=[y]
$$

usa riflessività, simmetria e transitività. La classe di $x$ coincide con quella di $y$ perché ogni elemento equivalente a $x$ è equivalente anche a $y$, e viceversa.

---

## 3. L’insieme quoziente

L’insieme di tutte le classi di equivalenza di $R$ si chiama **[[Insieme quoziente|insieme quoziente]]** e si indica con

$$
A/R
$$

oppure

$$
A/{\sim}.
$$

Per definizione,

$$
A/R=\{[x]_R\mid x\in A\}.
$$

Gli elementi di $A/R$ non sono gli elementi originari di $A$, ma le classi di equivalenza.

Passare da $A$ ad $A/R$ è un processo di identificazione: tutti gli elementi della stessa classe vengono "incollati" e trattati come un unico elemento del quoziente.

La funzione naturale

$$
\pi:A\longrightarrow A/R,
\qquad
\pi(x)=[x]
$$

si chiama **proiezione canonica**. Manda ogni elemento nella classe a cui appartiene.

Poiché ogni elemento appartiene a una e una sola classe, le classi di equivalenza formano una partizione di $A$:

- nessuna classe è vuota;
- ogni elemento di $A$ appartiene a una classe;
- due classi diverse sono disgiunte.

---

## 4. Esempio: costruzione dei numeri razionali

I numeri razionali si possono costruire a partire dalle coppie di interi

$$
(a,b)\in\mathbb Z\times(\mathbb Z\setminus\{0\}),
$$

interpretando la coppia $(a,b)$ come la frazione

$$
\frac ab.
$$

Coppie diverse, però, possono rappresentare lo stesso numero razionale. Per esempio,

$$
\frac12=\frac24=\frac36.
$$

Le coppie $(1,2)$, $(2,4)$ e $(3,6)$ sono elementi distinti dell’insieme di partenza, ma vanno identificate perché rappresentano la stessa frazione.

Si definisce quindi la relazione

$$
(a,b)\sim(c,d)
\quad\Longleftrightarrow\quad
ad=bc,
$$

dove $b,d\neq 0$.

La condizione $ad=bc$ è proprio la condizione di uguaglianza tra frazioni:

$$
\frac ab=\frac cd
\quad\Longleftrightarrow\quad
ad=bc.
$$

Il numero razionale rappresentato da $(a,b)$ è dunque la classe di equivalenza

$$
[(a,b)].
$$

In questo modo si può scrivere formalmente

$$
\mathbb Q
=
\bigl(\mathbb Z\times(\mathbb Z\setminus\{0\})\bigr)\big/\sim.
$$

Per esempio,

$$
\left[(1,2)\right]
=
\left[(2,4)\right]
=
\left[(3,6)\right].
$$

Non sono tre frazioni diverse nel quoziente: sono tre rappresentanti della stessa classe.

### Operazioni sui razionali

Per definire le operazioni sui numeri razionali non si lavora direttamente sulle classi: si scelgono dei rappresentanti e si verifica che il risultato non dipenda da quelli scelti.

Per esempio, la somma si definisce ponendo

$$
[(a,b)]+[(c,d)]
=
[(ad+bc,bd)].
$$

Il prodotto si definisce ponendo

$$
[(a,b)]\cdot[(c,d)]
=
[(ac,bd)].
$$

Queste definizioni sono corrette solo dopo aver dimostrato che, sostituendo i rappresentanti con altri delle stesse classi, il risultato resta nella stessa classe.

---

## 5. Congruenza modulo $n$

Sia $n\in\mathbb N$, con $n\geq 1$. La **[[Congruenza modulo n|congruenza modulo $n$]]** è la relazione su $\mathbb Z$ definita da

$$
a\equiv b\pmod n
\quad\Longleftrightarrow\quad
n\mid(a-b).
$$

Equivalentemente,

$$
a\equiv b\pmod n
\quad\Longleftrightarrow\quad
a-b=kn
\quad\text{per qualche }k\in\mathbb Z.
$$

Ed è anche equivalente alla condizione

$$
a\equiv b\pmod n
\quad\Longleftrightarrow\quad
a= b+kn
\quad\text{per qualche }k\in\mathbb Z.
$$

Si verifica che la congruenza modulo $n$ è una relazione di equivalenza:

- riflessività:
  $$
  a-a=0,
  $$
  e $n\mid 0$;
- simmetria: se $n\mid(a-b)$, allora $n\mid(b-a)$;
- transitività: se $n\mid(a-b)$ e $n\mid(b-c)$, allora
  $$
  a-c=(a-b)+(b-c),
  $$
  quindi $n\mid(a-c)$.

La [[Classe di congruenza|classe di equivalenza di $a$ modulo $n$]] è

$$
[a]_n
=
\{b\in\mathbb Z\mid b\equiv a\pmod n\}.
$$

Esplicitamente,

$$
[a]_n=\{a+kn\mid k\in\mathbb Z\}.
$$

Due numeri della stessa classe differiscono per un multiplo di $n$.

### 5.1. Rappresentanti e resti

Per il teorema della [[Divisione euclidea|divisione euclidea]], ogni intero $a$ si scrive in modo unico come

$$
a=qn+r,
\qquad
0\leq r<n.
$$

Il numero $r$ è il resto della divisione di $a$ per $n$. Da questa scrittura segue

$$
a\equiv r\pmod n.
$$

Perciò ogni classe modulo $n$ ha un unico rappresentante tra

$$
0,1,\dots,n-1.
$$

Le classi modulo $n$ sono quindi esattamente

$$
[0]_n,[1]_n,\dots,[n-1]_n.
$$

Di conseguenza, l’insieme quoziente

$$
\mathbb Z/n\mathbb Z
$$

ha esattamente $n$ elementi:

$$
\mathbb Z/n\mathbb Z
=
\{[0]_n,[1]_n,\dots,[n-1]_n\}.
$$

Occhio a distinguere gli elementi del quoziente dai loro rappresentanti:

- gli elementi di $\mathbb Z$ sono interi;
- gli elementi di $\mathbb Z/n\mathbb Z$ sono classi di equivalenza.

Per esempio, in $\mathbb Z/12\mathbb Z$,

$$
[1]_{12}
=
\{\ldots,-23,-11,1,13,25,\ldots\},
$$

e

$$
[5]_{12}
=
\{\ldots,-19,-7,5,17,29,\ldots\}.
$$

La classe $[1]_{12}$ si può indicare anche con $-11$, $13$, $25$ o qualunque altro intero congruo a $1$ modulo $12$.

---

## 6. Operazioni sulle classi modulo $n$

Si definiscono la somma e il prodotto in $\mathbb Z/n\mathbb Z$ ponendo

$$
[a]_n+[b]_n=[a+b]_n
$$

e

$$
[a]_n\cdot[b]_n=[ab]_n.
$$

Queste formule usano dei rappresentanti. Bisogna quindi dimostrare che le definizioni siano **[[Buona definizione|ben poste]]**, cioè indipendenti dalla scelta dei rappresentanti.

### 6.1. Compatibilità della congruenza con la somma e il prodotto

Se

$$
a\equiv a'\pmod n
\qquad\text{e}\qquad
b\equiv b'\pmod n,
$$

allora

$$
a+b\equiv a'+b'\pmod n
$$

e

$$
ab\equiv a'b'\pmod n.
$$

#### Somma

Dalle ipotesi segue che

$$
n\mid(a-a')
\qquad\text{e}\qquad
n\mid(b-b').
$$

Allora

$$
(a+b)-(a'+b')
=
(a-a')+(b-b'),
$$

che è divisibile per $n$. Quindi

$$
a+b\equiv a'+b'\pmod n.
$$

#### Prodotto

Si può scrivere

$$
ab-a'b'
=
ab-a'b+a'b-a'b'
=
(a-a')b+a'(b-b').
$$

Entrambi i termini a destra sono divisibili per $n$, quindi lo è anche la loro somma. Dunque

$$
ab\equiv a'b'\pmod n.
$$

Perciò le operazioni sono ben definite:

$$
[a]_n=[a']_n,\quad [b]_n=[b']_n
\Longrightarrow
[a+b]_n=[a'+b']_n
$$

e

$$
[a b]_n=[a'b']_n.
$$

> [!warning]
> Non basta scrivere una formula per la somma o per il prodotto delle classi. Prima bisogna verificare che il risultato non dipenda dal rappresentante scelto.

È la stessa questione che si incontra nella costruzione dei numeri razionali: la definizione deve dipendere dalla classe, non dalla particolare coppia o dal particolare intero scelto come rappresentante.

> [!example] Esempio
> In $\mathbb Z/6\mathbb Z$ si ha $[4]_6+[5]_6=[9]_6=[3]_6$ e $[4]_6\cdot[5]_6=[20]_6=[2]_6$. Se al posto di $4$ e $5$ usiamo i rappresentanti $-2$ e $11$, otteniamo $[-2+11]_6=[9]_6$ e $[-22]_6=[2]_6$: stesse classi, come deve essere.

---

## 7. Proprietà di $\mathbb Z/n\mathbb Z$

Una volta dimostrato che le operazioni sono ben definite, le loro proprietà si trasferiscono da $\mathbb Z$ al quoziente.

Per esempio, l’associatività della somma segue da quella degli interi:

$$
\begin{aligned}
\bigl([a]_n+[b]_n\bigr)+[c]_n
&=[a+b]_n+[c]_n\\
&=[(a+b)+c]_n\\
&=[a+(b+c)]_n\\
&=[a]_n+[b+c]_n\\
&=[a]_n+\bigl([b]_n+[c]_n\bigr).
\end{aligned}
$$

L’elemento neutro rispetto alla somma è

$$
[0]_n,
$$

perché

$$
[a]_n+[0]_n=[a+0]_n=[a]_n.
$$

L’opposto di $[a]_n$ è $[-a]_n$, infatti

$$
[a]_n+[-a]_n=[0]_n.
$$

Quindi $(\mathbb Z/n\mathbb Z,+)$ è un gruppo abeliano.

Anche il prodotto è associativo e commutativo:

$$
([a]_n[b]_n)[c]_n
=
[(ab)c]_n
=
[a(bc)]_n
=
[a]_n([b]_n[c]_n),
$$

e

$$
[a]_n[b]_n=[ab]_n=[ba]_n=[b]_n[a]_n.
$$

L’elemento neutro rispetto al prodotto è

$$
[1]_n,
$$

poiché

$$
[a]_n[1]_n=[a]_n.
$$

Inoltre il prodotto è distributivo rispetto alla somma:

$$
[a]_n\bigl([b]_n+[c]_n\bigr)
=
[a]_n[b+c]_n
=
[a(b+c)]_n
$$

e

$$
[a(b+c)]_n=[ab+ac]_n
=[ab]_n+[ac]_n.
$$

Ne segue che $\mathbb Z/n\mathbb Z$ è un anello commutativo con identità.

---

## 8. Strutture algebriche e operazioni

Una **operazione binaria** su un insieme $G$ è una [[Funzione|funzione]]

$$
\star:G\times G\longrightarrow G.
$$

La condizione fondamentale è la chiusura: dati $x,y\in G$, il risultato $x\star y$ deve appartenere ancora a $G$.

Le proprietà principali di un’operazione sono:

### Associatività

$$
\forall x,y,z\in G,\qquad
(x\star y)\star z=x\star(y\star z).
$$

### Commutatività

$$
\forall x,y\in G,\qquad
x\star y=y\star x.
$$

Associatività e commutatività sono proprietà diverse: un’operazione può essere associativa senza essere commutativa.

### Elemento neutro

Un elemento $e\in G$ è elemento neutro per $\star$ se

$$
\forall x\in G,\qquad
x\star e=e\star x=x.
$$

L’elemento neutro deve funzionare sia a destra sia a sinistra.

### Elemento inverso

Dato $x\in G$, un elemento $y\in G$ si dice inverso di $x$ se

$$
x\star y=y\star x=e.
$$

Con una notazione generica si scrive spesso

$$
y=x^{-1}.
$$

Se l’operazione è la somma, l’inverso di $x$ si indica invece con $-x$.

---

## 9. Gruppi

Un insieme $G$ dotato di un’operazione $\star$ è un **[[Gruppo|gruppo]]** se:

1. $\star$ è un’operazione interna su $G$;
2. $\star$ è associativa;
3. esiste un elemento neutro $e\in G$;
4. ogni elemento di $G$ possiede un inverso.

Se inoltre l’operazione è commutativa, il gruppo si dice **abeliano**.

Esempi:

- $(\mathbb Z,+)$ è un gruppo abeliano;
- $(\mathbb Z/n\mathbb Z,+)$ è un gruppo abeliano;
- $(\mathbb Z,\cdot)$ non è un gruppo, perché la maggior parte degli interi non ha un inverso moltiplicativo in $\mathbb Z$.

Per esempio, $2$ non ha un inverso in $\mathbb Z$ rispetto al prodotto: non esiste $x\in\mathbb Z$ tale che $2x=1$.

La struttura di gruppo permette di dimostrare proprietà astratte una volta per tutte e poi applicarle a molti esempi diversi. È uno dei motivi per cui in matematica si studiano strutture definite da proprietà generali: una dimostrazione astratta vale per ogni insieme e ogni operazione che soddisfino le stesse ipotesi.

---

## 10. Anelli e campi

Un **[[Anello|anello]]** è un insieme dotato di due operazioni, generalmente indicate con $+$ e $\cdot$, tali che:

- rispetto alla somma si ottiene un gruppo abeliano;
- il prodotto è associativo;
- il prodotto è distributivo rispetto alla somma:
  $$
  a(b+c)=ab+ac,
  $$
  $$
  (a+b)c=ac+bc.
  $$

Nel corso si considerano in particolare anelli commutativi con identità, cioè anelli in cui:

$$
ab=ba
$$

per ogni $a,b$, e in cui esiste un elemento $1$ tale che

$$
1a=a1=a.
$$

Esempi:

- $\mathbb Z$ è un anello commutativo con identità;
- $\mathbb Z/n\mathbb Z$ è un anello commutativo con identità;
- gli [[Spazio vettoriale|spazi vettoriali]] sono strutture più ricche, perché oltre alle operazioni interne coinvolgono anche la moltiplicazione per scalari.

Un **[[Campo|campo]]** è un anello commutativo con identità in cui ogni elemento non nullo è invertibile rispetto al prodotto. Quindi, se $K$ è un campo, per ogni $a\in K$ con $a\neq 0$ esiste $a^{-1}\in K$ tale che

$$
aa^{-1}=a^{-1}a=1.
$$

In generale un anello non è un campo, perché può contenere elementi non nulli privi di inverso moltiplicativo.

---

## 11. Elementi invertibili in $\mathbb Z/n\mathbb Z$

Un elemento $[a]_n\in\mathbb Z/n\mathbb Z$ è [[Elementi invertibili modulo n|invertibile]] se esiste una classe $[x]_n$ tale che

$$
[a]_n[x]_n=[1]_n.
$$

Per la definizione del prodotto nel quoziente, questa condizione equivale a

$$
[ax]_n=[1]_n,
$$

cioè

$$
ax\equiv 1\pmod n.
$$

Quindi $[a]_n$ è invertibile se e solo se la congruenza

$$
ax\equiv 1\pmod n
$$

ammette una soluzione intera $x$.

Un risultato fondamentale sulle [[Congruenza lineare|congruenze lineari]] dice che

$$
ax\equiv b\pmod n
$$

è risolvibile se e solo se

$$
\gcd(a,n)\mid b.
$$

Per l’invertibilità $b=1$, perciò:

### Teorema

La classe $[a]_n$ è invertibile in $\mathbb Z/n\mathbb Z$ se e solo se

$$
\gcd(a,n)=1.
$$

#### Dimostrazione: necessità

Supponiamo che $[a]_n$ sia invertibile. Allora esiste $x\in\mathbb Z$ tale che

$$
ax\equiv 1\pmod n.
$$

Quindi esiste $k\in\mathbb Z$ tale che

$$
ax-1=kn,
$$

ossia

$$
ax-kn=1.
$$

Ogni divisore comune di $a$ e $n$ divide il membro sinistro e quindi divide $1$. Dunque

$$
\gcd(a,n)=1.
$$

#### Dimostrazione: sufficienza

Se

$$
\gcd(a,n)=1,
$$

per l’[[Identità di Bézout|identità di Bézout]] esistono $x,k\in\mathbb Z$ tali che

$$
ax+nk=1.
$$

Da questa uguaglianza segue

$$
ax\equiv 1\pmod n,
$$

quindi

$$
[a]_n[x]_n=[1]_n.
$$

Pertanto $[a]_n$ è invertibile.

L’invertibilità dipende dalla classe e non dal rappresentante scelto. Infatti, se

$$
[a]_n=[a']_n,
$$

allora

$$
a\equiv a'\pmod n
$$

e vale

$$
\gcd(a,n)=\gcd(a',n).
$$

Quindi due rappresentanti della stessa classe sono o entrambi invertibili o entrambi non invertibili.

---

## 12. Esempio: invertibili modulo $12$

Consideriamo $\mathbb Z/12\mathbb Z$. Le classi sono

$$
[0]_{12},[1]_{12},[2]_{12},\ldots,[11]_{12}.
$$

Una classe $[a]_{12}$ è invertibile se e solo se

$$
\gcd(a,12)=1.
$$

Calcolando i massimi comuni divisori:

- $\gcd(0,12)=12$;
- $\gcd(1,12)=1$;
- $\gcd(2,12)=2$;
- $\gcd(3,12)=3$;
- $\gcd(4,12)=4$;
- $\gcd(5,12)=1$;
- $\gcd(6,12)=6$;
- $\gcd(7,12)=1$;
- $\gcd(8,12)=4$;
- $\gcd(9,12)=3$;
- $\gcd(10,12)=2$;
- $\gcd(11,12)=1$.

Le classi invertibili sono dunque

$$
[1]_{12},\ [5]_{12},\ [7]_{12},\ [11]_{12}.
$$

I loro inversi si trovano risolvendo le congruenze corrispondenti:

$$
1\cdot 1\equiv 1\pmod{12},
$$

quindi

$$
[1]_{12}^{-1}=[1]_{12};
$$

$$
5\cdot 5=25\equiv 1\pmod{12},
$$

quindi

$$
[5]_{12}^{-1}=[5]_{12};
$$

$$
7\cdot 7=49\equiv 1\pmod{12},
$$

quindi

$$
[7]_{12}^{-1}=[7]_{12};
$$

$$
11\cdot 11=121\equiv 1\pmod{12},
$$

quindi

$$
[11]_{12}^{-1}=[11]_{12}.
$$

Le classi $[2]_{12}$, $[3]_{12}$, $[4]_{12}$, $[6]_{12}$, $[8]_{12}$, $[9]_{12}$ e $[10]_{12}$ non sono invertibili perché hanno con $12$ un massimo comune divisore maggiore di $1$.

In particolare, $\mathbb Z/12\mathbb Z$ non è un campo: contiene elementi non nulli, come $[2]_{12}$, che non sono invertibili.

---

## 13. Il caso del modulo primo

Se $p$ è un [[Numero primo|numero primo]], ogni intero $a$ con $1\leq a\leq p-1$ è coprimo con $p$. Di conseguenza, in $\mathbb Z/p\mathbb Z$ ogni classe non nulla è invertibile.

Pertanto

$$
\mathbb Z/p\mathbb Z
$$

è un campo quando $p$ è primo.

Per un modulo composto, invece, possono esistere classi non nulle non invertibili. Per esempio, modulo $12$, la classe $[2]_{12}$ è non nulla ma non invertibile.

La differenza è legata alla presenza di divisori dello zero negli anelli $\mathbb Z/n\mathbb Z$ quando $n$ non è primo. Per esempio,

$$
[2]_{12}[6]_{12}=[12]_{12}=[0]_{12},
$$

anche se né $[2]_{12}$ né $[6]_{12}$ è la classe nulla.

---

## 14. Strategia generale per definire operazioni su un quoziente

Quando si ha un insieme quoziente $A/{\sim}$ e si vuole definire un’operazione sulle classi, la procedura corretta è:

1. scegliere rappresentanti delle classi;
2. applicare l’operazione nell’insieme di partenza;
3. passare alla classe del risultato;
4. dimostrare che il risultato non dipende dai rappresentanti scelti.

Nel caso di $\mathbb Z/n\mathbb Z$:

$$
[a]_n+[b]_n=[a+b]_n,
$$

$$
[a]_n[b]_n=[ab]_n.
$$

La parte non automatica è la buona definizione. Bisogna dimostrare che, se

$$
[a]_n=[a']_n
\qquad\text{e}\qquad
[b]_n=[b']_n,
$$

allora

$$
[a+b]_n=[a'+b']_n
$$

e

$$
[ab]_n=[a'b']_n.
$$

Solo dopo questa verifica si possono trasferire al quoziente le proprietà algebriche delle operazioni.

Lo stesso principio vale per la costruzione dei numeri razionali: addizione e moltiplicazione tra frazioni devono essere indipendenti dalla particolare rappresentazione scelta per ciascun numero razionale. Le proprietà delle frazioni non si possono semplicemente dare per scontate: nella costruzione formale vanno dimostrate attraverso la relazione di equivalenza.
