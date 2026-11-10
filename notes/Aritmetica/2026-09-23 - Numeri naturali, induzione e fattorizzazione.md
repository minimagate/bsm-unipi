---
type: lecture-note
course: Aritmetica
date: '2026-09-23'
title: Numeri naturali, induzione e fattorizzazione
source_transcript: _transcripts/Aritmetica/2026-09-23 - Numeri naturali, induzione e fattorizzazione.md
source_hash: sha256:bae8eb904bb68ea992cfe5c76090ed12fc96e585ed8cbe50270c1b5e0eead68d
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-23T12:13:44.649Z'
vault_path: Notes/Aritmetica/Lectures/2026-09-23 - Numeri naturali, induzione e fattorizzazione.md
vault_hash: dfe422c27e87a1eeb38a47a19dcdb8608341cf3c6a8d5a28d77e3b64e663c59b
---

## 1. Gli insiemi numerici e le operazioni

### 1.1 Numeri naturali

I [[Numero naturale|numeri naturali]] sono i numeri che usiamo per contare. L’idea è associare agli oggetti di un insieme il numero che dice quanti sono: se ci sono cinque oggetti, il numero $5$ è la [[Cardinalità|cardinalità]] dell’insieme.

C’è anche un altro modo per dire che due insiemi hanno lo stesso numero di elementi: metterli in corrispondenza biunivoca. Se a ogni bambino posso associare esattamente un oggetto, e ogni oggetto finisce a un solo bambino, i due insiemi hanno lo stesso numero di elementi.

In questo corso si adotta la convenzione

$$
\mathbb{N}=\{0,1,2,3,\ldots\}.
$$

Quindi lo zero è un numero naturale.

I naturali sono chiusi rispetto alla somma: se $m,n\in\mathbb{N}$, allora $m+n\in\mathbb{N}$. Non lo sono invece rispetto alla sottrazione. L’equazione

$$
x+3=0
$$

non ha soluzione in $\mathbb{N}$, perché nei naturali $3$ non ha un opposto. Per risolverla servono i numeri interi, dove compare $-3$.

Allo stesso modo, l’equazione

$$
5x+8=0
$$

non ha soluzione naturale, ma si risolve passando prima agli interi e poi, se serve, ai razionali.

### 1.2 Numeri interi, razionali e reali

Gli interi comprendono i naturali e i loro opposti:

$$
\mathbb{Z}=\{\ldots,-2,-1,0,1,2,\ldots\}.
$$

I razionali sono i numeri che si scrivono come rapporto di due interi, con denominatore diverso da zero:

$$
\mathbb{Q}
=
\left\{
\frac{m}{n}
\;\middle|\;
m\in\mathbb{Z},\ n\in\mathbb{Z}\setminus\{0\}
\right\}.
$$

Le frazioni equivalenti si identificano. Per esempio,

$$
\frac{1}{2}=\frac{2}{4}=\frac{3}{6},
$$

perché rappresentano lo stesso razionale. In termini formali, si usa una [[Relazione di equivalenza|relazione di equivalenza]] tra frazioni e si identificano tutte quelle della stessa classe.

Un razionale ha uno sviluppo decimale finito oppure periodico. Per esempio:

$$
\frac{3}{4}=0,75,
\qquad
\frac{1}{3}=0,\overline{3}.
$$

Vale anche il viceversa: ogni sviluppo decimale finito o periodico rappresenta un razionale. Uno sviluppo periodico, per esempio, si trasforma in frazione con la solita tecnica algebrica.

I numeri reali $\mathbb{R}$ comprendono sia i razionali sia gli irrazionali:

$$
\mathbb{Q}\subset\mathbb{R}.
$$

Un reale può avere uno sviluppo decimale infinito non periodico, come

$$
0,101001000100001\ldots,
$$

dove tra due $1$ compaiono blocchi di zeri sempre più lunghi. Lo sviluppo non è periodico, quindi il numero non è razionale.

Un altro esempio fondamentale è $\sqrt{2}$, che non è razionale. La dimostrazione dell’irrazionalità di $\sqrt{2}$ è l’esempio classico di [[Dimostrazione per assurdo|dimostrazione per assurdo]].

Poi ci sono i numeri complessi $\mathbb{C}$, che contengono i reali e permettono, tra le altre cose, di risolvere equazioni come

$$
x^2+1=0.
$$

Nei [[Numero complesso|numeri complessi]] si introduce l’unità immaginaria $i$, definita da

$$
i^2=-1.
$$

La lezione, comunque, si concentra soprattutto sui numeri naturali.

---

## 2. Operazioni e proprietà algebriche

Un’operazione binaria su un insieme $X$ è una [[Funzione|funzione]]

$$
\ast\colon X\times X\longrightarrow X.
$$

A una coppia $(a,b)$ di elementi di $X$ si associa un unico elemento $a\ast b\in X$.

Alcuni esempi di operazioni:

- la somma;
- il prodotto;
- la differenza, quando l’insieme è chiuso rispetto alla sottrazione;
- la divisione, quando il denominatore è diverso da zero e il risultato resta nell’insieme;
- l’[[Operazioni tra insiemi|unione]] tra insiemi, vista come operazione sull’[[Insieme delle parti|insieme delle parti]].

Le operazioni possono avere diverse proprietà.

### Commutatività

Un’operazione $\ast$ è commutativa se

$$
a\ast b=b\ast a
\qquad
\forall a,b\in X.
$$

Somma e prodotto di numeri sono commutativi:

$$
a+b=b+a,
\qquad
ab=ba.
$$

Sottrazione e divisione, in generale, no.

### Associatività

Un’operazione $\ast$ è associativa se

$$
(a\ast b)\ast c=a\ast(b\ast c)
\qquad
\forall a,b,c\in X.
$$

Somma e prodotto sono associativi:

$$
(a+b)+c=a+(b+c),
$$

$$
(ab)c=a(bc).
$$

Grazie all’associatività si possono togliere le parentesi quando si sommano o si moltiplicano più numeri.

### Elemento neutro

Un elemento $e\in X$ è neutro per $\ast$ se

$$
a\ast e=e\ast a=a
\qquad
\forall a\in X.
$$

Per la somma il neutro è $0$:

$$
a+0=0+a=a.
$$

Per il prodotto il neutro è $1$:

$$
a\cdot 1=1\cdot a=a.
$$

### Inverso

L’inverso di un elemento dipende dall’operazione.

Per la somma, l’inverso di $a$ è $-a$, perché

$$
a+(-a)=0.
$$

Per il prodotto, l’inverso di un elemento non nullo $a$ è $\frac{1}{a}$, perché

$$
a\cdot\frac{1}{a}=1.
$$

Nei naturali non tutti questi inversi esistono: per esempio $3$ non ha un opposto naturale. Allargare gli insiemi numerici serve anche a questo: rendere possibili nuove operazioni e nuove equazioni.

In generale, più proprietà soddisfano le operazioni, più l’insieme è strutturato. Ma una struttura con troppe proprietà può diventare meno interessante, perché le operazioni si fanno banali. L’obiettivo è studiare le proprietà una per una, per capire che conseguenze hanno sulla struttura.

---

## 3. Definizione assiomatica dei numeri naturali

I naturali si possono introdurre in modo intuitivo, contando, ma in matematica si caratterizzano anche con degli assiomi.

Un assioma è un’affermazione che si assume come punto di partenza della teoria, senza dimostrarla.

### 3.1 Elemento iniziale e successore

Si assume che esista un elemento iniziale, che per convenzione è $0$.

A ogni numero naturale $n$ è associato un successore, indicato con

$$
n+1.
$$

Il successore di $0$ è $1$, quello di $1$ è $2$, e così via:

$$
0,\ 1,\ 2,\ 3,\ldots
$$

Il nome dato all’elemento iniziale è una convenzione: si potrebbe usare un simbolo diverso da $0$, ma $0$ è la scelta usuale e rende naturale la notazione.

La struttura fondamentale dei naturali ha quindi tre ingredienti:

1. un elemento iniziale;
2. un’operazione di passaggio al successore;
3. il principio che permette di ottenere tutti i naturali a partire dall’elemento iniziale.

Tra le proprietà essenziali della costruzione ci sono anche queste:

- $0$ non è il successore di nessun numero naturale;
- numeri naturali distinti hanno successori distinti.

In pratica, ogni numero naturale si ottiene partendo da $0$ e applicando un numero finito di volte l’operazione di successore.

---

## 4. Il principio del minimo

### 4.1 Enunciato

Il [[Principio del minimo|principio del minimo]], o principio del buon ordinamento, dice che ogni sottoinsieme non vuoto dei numeri naturali ha un elemento minimo.

Formalmente:

> Se $S\subseteq\mathbb{N}$ e $S\neq\varnothing$, allora esiste $m\in S$ tale che
>
> $$
> m\leq n
> \qquad
> \forall n\in S.
> $$

L’elemento $m$ si chiama minimo di $S$.

Questo principio è tipico dei naturali, ed è uno dei motivi per cui il loro ordine è così comodo nelle dimostrazioni.

### 4.2 Interpretazione intuitiva

Immaginiamo i numeri naturali come punti allineati:

$$
0,\ 1,\ 2,\ 3,\ 4,\ldots
$$

Coloriamo alcuni di questi punti: otteniamo un sottoinsieme non vuoto $S$.

Si può procedere da sinistra verso destra:

- si controlla se $0\in S$;
- se $0\notin S$, si controlla se $1\in S$;
- poi si controlla $2$, poi $3$, e così via.

Siccome $S$ contiene almeno un elemento, prima o poi se ne incontra uno. Il primo che si incontra è per forza il minimo di $S$: tutti quelli prima non stanno in $S$.

Questo funziona perché i naturali hanno un punto di partenza, $0$, e sono ordinati in modo discreto.

> [!example] Esempio
> Sia $S$ l’insieme dei naturali $n$ tali che $n^2>50$. Controllando in ordine, $7^2=49$ non basta, mentre $8^2=64>50$: il minimo di $S$ è quindi $8$.

---

## 5. Principio di induzione matematica

Il [[Principio di induzione|principio di induzione]] serve a dimostrare che una proprietà vale per tutti i numeri naturali, o per tutti quelli da un certo punto in poi.

Sia $P(n)$ una proprietà definita per $n\in\mathbb{N}$.

### 5.1 Forma debole dell’induzione

La forma usuale dice che, se:

1. **passo base**: $P(n_0)$ è vera;
2. **passo induttivo**: per ogni $n\geq n_0$,

   $$
   P(n)\Longrightarrow P(n+1),
   $$

allora

$$
P(n)\text{ è vera per ogni }n\geq n_0.
$$

Il passo induttivo si può scrivere anche così:

$$
\forall n\geq n_0,\quad
\bigl(P(n)\Rightarrow P(n+1)\bigr).
$$

L’ipotesi $P(n)$ si chiama **ipotesi induttiva**; $P(n+1)$ è la tesi del passo induttivo.

#### Schema logico

Il ragionamento è quello delle tessere del domino:

- si fa cadere la prima tessera;
- si dimostra che ogni tessera, cadendo, fa cadere la successiva;
- di conseguenza cadono tutte.

Per i numeri naturali:

- il passo base è la prima tessera;
- il passo induttivo garantisce il passaggio da $n$ a $n+1$.

Occhio: servono entrambe le parti. Non basta dimostrare che, se la proprietà vale a un certo livello, allora vale al successivo: bisogna anche verificare che la catena parta davvero dal valore giusto.

### 5.2 Esempio: somma dei primi numeri naturali

Una formula classica è

$$
1+2+\cdots+n=\frac{n(n+1)}{2}.
$$

Definiamo la proprietà

$$
P(n):\qquad
1+2+\cdots+n=\frac{n(n+1)}{2}.
$$

#### Passo base

Per $n=1$:

$$
1=\frac{1\cdot(1+1)}{2}
=\frac{2}{2}
=1.
$$

Quindi $P(1)$ è vera.

#### Passo induttivo

Supponiamo vera $P(n)$, cioè

$$
1+2+\cdots+n=\frac{n(n+1)}{2}.
$$

Dobbiamo dimostrare $P(n+1)$:

$$
1+2+\cdots+n+(n+1)
=
\frac{(n+1)(n+2)}{2}.
$$

Usando l’ipotesi induttiva:

$$
\begin{aligned}
1+2+\cdots+n+(n+1)
&=
\frac{n(n+1)}{2}+(n+1)\\
&=
\frac{n(n+1)+2(n+1)}{2}\\
&=
\frac{(n+1)(n+2)}{2}.
\end{aligned}
$$

Quindi $P(n+1)$ è vera. Per il principio di induzione, la formula vale per ogni $n\geq 1$.

### 5.3 Importanza della scrittura formale

In una dimostrazione per induzione bisogna tenere ben distinti:

- la proprietà $P(n)$;
- l’ipotesi induttiva, cioè l’assunzione che $P(n)$ sia vera;
- la proprietà successiva $P(n+1)$;
- l’indice iniziale $n_0$.

Una scrittura imprecisa può nascondere errori logici. Per esempio, non va bene scrivere una somma con i puntini senza specificare bene quali sono i termini e qual è l’indice finale.

In una somma come

$$
1+2+\cdots+n
$$

i puntini indicano una successione di termini, ma in una dimostrazione più complessa conviene usare una notazione formale, come

$$
\sum_{k=1}^{n} k.
$$

La precisione nella notazione conta ancora di più quando le formule si complicano.

---

## 6. Dimostrazione del principio di induzione mediante il principio del minimo

Principio di induzione e principio del minimo sono equivalenti: ciascuno si può usare per dimostrare l’altro.

### 6.1 Dal principio del minimo all’induzione

Supponiamo di avere una proprietà $P(n)$ definita per ogni $n\geq n_0$ e di assumere:

1. $P(n_0)$ è vera;
2. per ogni $n\geq n_0$,

   $$
   P(n)\Longrightarrow P(n+1).
   $$

Vogliamo dimostrare che $P(n)$ è vera per ogni $n\geq n_0$.

Supponiamo per assurdo che esista almeno un naturale $n\geq n_0$ per cui $P(n)$ è falsa. Consideriamo l’insieme dei controesempi:

$$
S=\{n\in\mathbb{N}: n\geq n_0 \text{ e } P(n)\text{ è falsa}\}.
$$

Per ipotesi, $S\neq\varnothing$. Per il principio del minimo, $S$ ha un minimo, che chiamiamo $m_0$.

Siccome $P(n_0)$ è vera, il minimo controesempio non può essere $n_0$. Dunque

$$
m_0>n_0.
$$

In particolare, $m_0-1\geq n_0$. Per la minimalità di $m_0$, il numero $m_0-1$ non appartiene a $S$, quindi $P(m_0-1)$ è vera.

Dal passo induttivo segue

$$
P(m_0-1)\Longrightarrow P(m_0),
$$

e quindi $P(m_0)$ è vera. Ma questo contraddice il fatto che $m_0\in S$, cioè che $P(m_0)$ sia falsa.

Abbiamo trovato una contraddizione. Quindi $S$ è vuoto e $P(n)$ è vera per ogni $n\geq n_0$.

#### Struttura della dimostrazione

Lo schema è questo:

1. si suppone che la tesi non valga per qualche naturale;
2. si considera l’insieme dei controesempi;
3. si sceglie il più piccolo controesempio;
4. si dimostra che il suo predecessore non è un controesempio;
5. si usa il passo induttivo per dimostrare che nemmeno il minimo controesempio lo è;
6. si ottiene una contraddizione.

### 6.2 Dall’induzione al principio del minimo

Supponiamo di assumere il principio di induzione e prendiamo un insieme non vuoto

$$
S\subseteq\mathbb{N}.
$$

Vogliamo dimostrare che $S$ ha un minimo.

Supponiamo per assurdo che $S$ non abbia minimo. Definiamo la proprietà

$$
P(n):\qquad n\notin S.
$$

Se $0\notin S$, allora $P(0)$ è vera.

Supponiamo ora che $P(n)$ sia vera, cioè $n\notin S$. Se fosse $n+1\in S$, poiché $S$ non ha minimo dovrebbe esistere un elemento di $S$ strettamente minore di $n+1$. Questo elemento sarebbe minore o uguale a $n$, in contrasto con l’ipotesi che nessuno dei numeri precedenti stia in $S$. Quindi anche $n+1\notin S$.

Per induzione, nessun numero naturale appartiene a $S$, cioè

$$
S=\varnothing,
$$

in contraddizione con $S\neq\varnothing$.

Quindi $S$ ha un minimo.

Le due proprietà sono dunque equivalenti:

- principio del minimo;
- principio di induzione.

---

## 7. Errori nell’induzione: il passo base

Il passo base non è una formalità. Va verificato nel punto giusto, cioè nel primo indice da cui si vuole dimostrare la proprietà.

### 7.1 Un esempio fallace

Prendiamo l’affermazione scherzosa:

> In ogni insieme di $n$ studenti, tutti gli studenti hanno gli occhi dello stesso colore.

Il tentativo di dimostrazione va così:

- per $n=1$ l’affermazione è vera;
- supponiamo che sia vera per un insieme di $n$ studenti;
- prendiamo $n+1$ studenti;
- consideriamo i primi $n$ e gli ultimi $n$;
- per ipotesi induttiva, in ciascuno dei due gruppi gli studenti hanno occhi dello stesso colore;
- i due gruppi dovrebbero avere un elemento in comune, e questo permetterebbe di concludere che tutti gli $n+1$ studenti hanno gli occhi dello stesso colore.

Il problema è nel passaggio da $n=1$ a $n=2$. Con due studenti:

- il primo gruppo, formato dai primi $n=1$ studenti, contiene il primo studente;
- il secondo gruppo, formato dagli ultimi $n=1$ studenti, contiene il secondo;
- i due gruppi non hanno elementi in comune.

Manca proprio l’elemento che dovrebbe collegare i due gruppi.

Quindi il passo induttivo non è valido a partire da $n=1$. L’argomento potrebbe funzionare da $n=2$ in poi, perché per $n\geq 2$ i due gruppi di $n$ elementi ricavati da un insieme di $n+1$ elementi hanno almeno un elemento in comune. Ma allora bisognerebbe verificare che la proprietà sia vera per $n=2$, e questo non succede.

L’esempio ci ricorda che bisogna sempre:

1. controllare il valore iniziale;
2. verificare che il passo induttivo funzioni proprio a partire da quel valore;
3. non confondere una proprietà vera per $n=1$ con una proprietà vera per tutti i naturali.

---

## 8. Induzione forte

### 8.1 Enunciato

La forma forte dell’induzione, detta anche induzione completa, è la seguente.

Sia $P(n)$ una proprietà definita per ogni $n\geq n_0$. Se:

1. $P(n_0)$ è vera;
2. per ogni $n>n_0$, assumendo vere tutte le proprietà precedenti

   $$
   P(n_0),P(n_0+1),\ldots,P(n-1),
   $$

   si riesce a dimostrare $P(n)$;

allora $P(n)$ è vera per ogni $n\geq n_0$.

Formalmente:

$$
\left[
P(n_0)
\ \land\
\forall n>n_0,\,
\left(
\bigwedge_{k=n_0}^{n-1}P(k)
\Longrightarrow P(n)
\right)
\right]
\Longrightarrow
\forall n\geq n_0,\ P(n).
$$

La differenza con l’[[Induzione forte|induzione forte]] rispetto a quella debole è che, per dimostrare $P(n)$, si possono usare tutte le proprietà precedenti, non solo $P(n-1)$.

### 8.2 Interpretazione con le tessere del domino

Nell’induzione debole ogni tessera fa cadere direttamente la successiva.

Nell’induzione forte, per far cadere la tessera $n$ si può contare sul fatto che siano già cadute tutte le precedenti:

$$
n_0,n_0+1,\ldots,n-1.
$$

L’induzione forte è utile quando il problema per $n$ dipende da numeri molto più piccoli di $n$, e non solo dal predecessore $n-1$.

### 8.3 Equivalenza tra induzione debole e forte

Le due forme sono equivalenti: ogni proprietà dimostrabile con una si dimostra anche con l’altra.

L’induzione forte implica quella debole in modo immediato: se per dimostrare $P(n+1)$ si possono usare tutte le proprietà precedenti, in particolare si può usare $P(n)$.

Per dimostrare l’induzione forte usando quella debole, si introduce una nuova proprietà:

$$
Q(n):\qquad
P(k)\text{ è vera per ogni }k\text{ con }n_0\leq k\leq n.
$$

La proprietà $Q(n)$ dice quindi che tutte le proprietà fino al livello $n$ sono vere.

Si procede per induzione debole su $Q(n)$.

#### Passo base

Per $n=n_0$,

$$
Q(n_0)
$$

coincide con $P(n_0)$, che è vera per ipotesi.

#### Passo induttivo

Supponiamo vera $Q(n)$. Significa che

$$
P(n_0),P(n_0+1),\ldots,P(n)
$$

sono tutte vere. Per l’ipotesi dell’induzione forte, da queste segue $P(n+1)$. Quindi sono vere tutte le proprietà fino a $n+1$, cioè $Q(n+1)$.

Per induzione debole, $Q(n)$ è vera per ogni $n\geq n_0$, e dunque lo è anche ogni $P(n)$.

La tecnica, in breve, è sostituire la proprietà originaria con una proprietà cumulativa che contiene tutta l’informazione necessaria fino al livello considerato.

---

## 9. Teorema fondamentale dell’aritmetica

### 9.1 Numeri primi e numeri composti

Un numero naturale $p\geq 2$ è detto **[[Numero primo|primo]]** se i suoi soli [[Divisibilità|divisori]] naturali sono $1$ e $p$.

Un numero naturale $n\geq 2$ che non è primo è detto **composto**. In questo caso si scrive come prodotto di due naturali strettamente compresi tra $1$ e $n$:

$$
n=ab,
\qquad
1<a<n,
\qquad
1<b<n.
$$

Il numero $1$ non è primo: la condizione $n\geq 2$ nella definizione di numero primo è essenziale.

### 9.2 Enunciato

Il [[Teorema fondamentale dell'aritmetica|teorema fondamentale dell’aritmetica]] dice che ogni numero naturale $n\geq 2$ si scrive come prodotto di numeri primi.

Inoltre, questa fattorizzazione è unica a meno dell’ordine dei fattori.

Formalmente, per ogni $n\geq 2$ esistono numeri primi $p_1,\ldots,p_r$ tali che

$$
n=p_1p_2\cdots p_r,
$$

e se anche

$$
n=q_1q_2\cdots q_s
$$

è una fattorizzazione in numeri primi, allora $r=s$ e i fattori $q_i$ coincidono con i $p_i$ a meno di un riordinamento.

Per esempio,

$$
10=2\cdot 5=5\cdot 2.
$$

Queste due scritture non sono due fattorizzazioni diverse: cambia solo l’ordine dei fattori.

Con le potenze si può scrivere, per esempio,

$$
100=2^2\cdot 5^2.
$$

L’unicità va quindi intesa a meno dell’ordine, o, equivalentemente, come unicità degli esponenti dei vari fattori primi.

In questa lezione si dimostra per prima la parte di **esistenza** della fattorizzazione; l’unicità richiede un argomento in più.

---

## 10. Dimostrazione dell’esistenza della fattorizzazione mediante induzione forte

Definiamo la proprietà

$$
P(n):\qquad
n\text{ è prodotto di numeri primi}.
$$

Vogliamo dimostrare che $P(n)$ è vera per ogni $n\geq 2$.

### 10.1 Passo base

Per $n=2$, il numero $2$ è primo. È quindi già una fattorizzazione in primi, con un solo fattore:

$$
2=2.
$$

Dunque $P(2)$ è vera.

### 10.2 Passo induttivo

Supponiamo $n>2$ e che tutte le proprietà precedenti siano vere:

$$
P(2),P(3),\ldots,P(n-1).
$$

Dobbiamo dimostrare $P(n)$. Ci sono due casi.

#### Caso 1: $n$ è primo

Se $n$ è primo, è già una fattorizzazione in primi. Quindi $P(n)$ è vera.

#### Caso 2: $n$ è composto

Se $n$ non è primo, esistono $a,b\in\mathbb{N}$ tali che

$$
n=ab,
$$

con

$$
1<a<n,
\qquad
1<b<n.
$$

In particolare,

$$
2\leq a\leq n-1,
\qquad
2\leq b\leq n-1.
$$

Per ipotesi induttiva, sia $a$ sia $b$ sono fattorizzabili in primi. Esistono quindi primi $p_1,\ldots,p_r$ e $q_1,\ldots,q_s$ tali che

$$
a=p_1\cdots p_r,
\qquad
b=q_1\cdots q_s.
$$

Moltiplicando le due fattorizzazioni:

$$
n=ab
=
(p_1\cdots p_r)(q_1\cdots q_s).
$$

Il membro di destra è un prodotto di primi. Quindi anche $n$ è fattorizzabile in primi.

Abbiamo dimostrato $P(n)$ in entrambi i casi. Per induzione forte, ogni numero naturale $n\geq 2$ è prodotto di numeri primi.

---

## 11. Perché è naturale usare l’induzione forte

La dimostrazione precedente non usa la fattorizzazione di $n-1$. Se $n$ è composto, infatti, si scrive

$$
n=ab
$$

e si usano le fattorizzazioni dei due fattori $a$ e $b$, che possono essere molto più piccoli di $n$ e non c’entrano niente con $n-1$.

Per esempio, per fattorizzare $32\,000$ si può scrivere

$$
32\,000=32\cdot 1000
$$

e fattorizzare separatamente $32$ e $1000$. L’informazione che serve riguarda numeri più piccoli, ma non solo il predecessore.

Sapere che $n-1$ è fattorizzabile non basta per dire qualcosa sulla fattorizzazione di $n$, perché in generale il predecessore di un numero non divide il numero successivo.

Per questo l’induzione forte è la forma più naturale per il teorema di fattorizzazione.

### 11.1 Dimostrazione con induzione debole

Poiché induzione debole e forte sono equivalenti, il teorema si può dimostrare anche con quella debole, ma bisogna cambiare proprietà.

Invece di considerare solo

$$
P(n):\qquad n\text{ è fattorizzabile},
$$

si definisce

$$
Q(n):\qquad
\text{ogni }k\text{ con }2\leq k\leq n
\text{ è fattorizzabile in numeri primi}.
$$

#### Passo base

Per $n=2$, $Q(2)$ equivale alla fattorizzazione di $2$, che è vera.

#### Passo induttivo

Supponiamo vera $Q(n)$. Allora tutti i numeri

$$
2,3,\ldots,n
$$

sono fattorizzabili.

Per dimostrare $Q(n+1)$ resta solo da dimostrare che $n+1$ è fattorizzabile:

- se $n+1$ è primo, non c’è niente da fare;
- se $n+1$ è composto, si scrive

  $$
  n+1=ab
  $$

  con $2\leq a,b\leq n$, e quindi $a$ e $b$ sono fattorizzabili per ipotesi induttiva.

Il prodotto delle due fattorizzazioni dà una fattorizzazione di $n+1$.

La proprietà cumulativa $Q(n)$ contiene esattamente tutte le informazioni che, nella dimostrazione con induzione forte, si assumono contemporaneamente.

---

## 12. Osservazioni metodologiche

### 12.1 Scelta dell’indice iniziale

Il valore iniziale $n_0$ va scelto in modo coerente con:

- il dominio di definizione della proprietà;
- il punto da cui la proprietà può essere vera;
- il funzionamento del passo induttivo.

Non tutte le formule o proprietà sono definite per ogni naturale. Per esempio:

$$
\sqrt{n-5}
$$

è definita nei reali solo quando

$$
n\geq 5.
$$

Allo stesso modo, l’espressione

$$
\frac{5n+3}{n-2}
$$

non è definita per $n=2$.

Se una proprietà è definita per tutti i naturali ma diventa vera solo da un certo punto in poi, si può applicare l’induzione a partire da quell’indice. Per esempio, se la proprietà vale per ogni $n\geq 7$, si sceglie

$$
n_0=7.
$$

Non serve che il dominio della formula inizi esattamente da $n_0$: basta che la proprietà sia definita nel punto iniziale e in tutti i punti successivi che si considerano.

### 12.2 Il passo base e il passo induttivo hanno ruoli distinti

Il passo base mostra che la proprietà parte davvero.

Il passo induttivo mostra che la proprietà si conserva passando da un livello al successivo, oppure che si ottiene usando i livelli precedenti.

Trascurare il passo base può produrre dimostrazioni convincenti all’apparenza ma sbagliate. L’esempio degli studenti con gli occhi dello stesso colore mostra che un passaggio induttivo plausibile può cadere proprio al primo livello.

### 12.3 Scelta della forma di induzione

Conviene scegliere la forma più adatta al problema:

- **induzione debole**: quando $P(n+1)$ dipende in modo naturale da $P(n)$;
- **induzione forte**: quando $P(n)$ dipende da più valori precedenti o da fattori molto più piccoli;
- **induzione debole con proprietà cumulativa**: quando si vuole trasformare un argomento di induzione forte in una dimostrazione che usa solo il predecessore.

Nel teorema fondamentale dell’aritmetica l’induzione forte rende la dimostrazione immediata, perché un numero composto si spezza in fattori più piccoli, non necessariamente consecutivi.
