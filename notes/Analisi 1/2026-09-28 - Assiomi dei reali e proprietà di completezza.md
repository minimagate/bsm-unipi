---
type: lecture-note
course: Analisi 1
date: '2026-09-28'
title: Assiomi dei reali e proprietà di completezza
source_transcript: _transcripts/Analisi 1/2026-09-28 - Assiomi dei reali e proprietà di completezza.md
source_hash: sha256:7f491d3e4a1ae47dcc827230e1efaae0c6685f2af0f7125cdb84895c273cd75c
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-28T12:31:50.721Z'
vault_path: Notes/Analisi 1/Lectures/2026-09-28 - Assiomi dei reali e proprietà di completezza.md
vault_hash: 0d936e7f816249cad6655f4f60c46157936bdbfde9033e8176cc466cc4e503e1
---

# Assiomi dei reali e proprietà di completezza

## 1. Gli insiemi numerici e la nascita dell’analisi

Gli insiemi numerici fondamentali sono

$$
\mathbb{N},\qquad \mathbb{Z},\qquad \mathbb{Q},\qquad \mathbb{R},\qquad \mathbb{C}.
$$

In modo intuitivo:

- $\mathbb{N}$ è l’insieme dei [[Numero naturale|numeri naturali]];
- $\mathbb{Z}$ è l’insieme degli interi, che comprende anche i numeri negativi;
- $\mathbb{Q}$ è l’insieme dei numeri razionali, cioè dei numeri esprimibili come
  $$
  \frac{a}{b},\qquad a,b\in\mathbb{Z},\quad b\neq 0;
  $$
- $\mathbb{R}$ è l’insieme dei numeri reali;
- $\mathbb{C}$ è l’insieme dei numeri complessi, che si scrivono nella forma
  $$
  a+ib,\qquad a,b\in\mathbb{R},
  $$
  dove $i^2=-1$.

Frazioni equivalenti rappresentano lo stesso numero razionale: ad esempio,

$$
\frac{2}{4}=\frac{1}{2}=\frac{3}{6}.
$$

Questa lezione è il punto in cui nasce davvero l’analisi matematica. Finora si possono descrivere molte proprietà algebriche e di ordinamento che valgono già in $\mathbb{Q}$; ciò che distingue veramente $\mathbb{R}$ da $\mathbb{Q}$ è l’**[[Assioma di completezza|assioma di completezza]]**, o assioma di continuità.

I numeri complessi saranno trattati in altri corsi. L’osservazione per cui “la strada più breve tra due affermazioni reali passa spesso per i numeri complessi” è un’indicazione di metodo: molte questioni reali si interpretano o si risolvono più facilmente con strumenti complessi, anche se l’analisi reale studia soprattutto funzioni a valori reali.

---

## 2. Descrizione assiomatica dei numeri reali

Una descrizione assiomatica non costruisce esplicitamente gli oggetti, ma specifica:

1. quali sono gli oggetti;
2. quali operazioni e relazioni sono definite su di essi;
3. quali proprietà devono soddisfare.

Per i [[Numero reale|numeri reali]] si considera una struttura

$$
\left(\mathbb{R},+,\cdot,\leq\right),
$$

costituita da:

- un insieme $\mathbb{R}$;
- un’operazione di addizione;
- un’operazione di moltiplicazione;
- una relazione d’ordine $\leq$.

Le proprietà fondamentali sono organizzate in tre famiglie:

1. **assiomi algebrici**, che rendono $\mathbb{R}$ un [[Campo|campo]];
2. **assiomi di ordinamento**;
3. **assioma di completezza** o di continuità.

Il metodo assiomatico richiede di assumere il minor numero possibile di proprietà indipendenti e di dimostrare tutte le altre come conseguenze. Molte proprietà che usiamo ogni giorno nei calcoli non sono quindi assiomi, ma teoremi.

---

## 3. Gli assiomi algebrici: $\mathbb{R}$ è un campo

Le operazioni di somma e prodotto sono funzioni

$$
+:\mathbb{R}\times\mathbb{R}\longrightarrow\mathbb{R},
$$

e

$$
\cdot:\mathbb{R}\times\mathbb{R}\longrightarrow\mathbb{R}.
$$

La somma associa a ogni coppia $(a,b)$ il numero $a+b$; il prodotto associa alla stessa coppia il numero $ab$.

La notazione usuale $a+b$ o $ab$ è una scrittura abbreviata per indicare l’applicazione di queste funzioni alla coppia $(a,b)$.

### 3.1 Proprietà della somma

Per ogni $a,b,c\in\mathbb{R}$ valgono:

1. **Associatività**
   $$
   (a+b)+c=a+(b+c).
   $$

2. **Commutatività**
   $$
   a+b=b+a.
   $$

3. **Esistenza dell’elemento neutro additivo**: esiste $0\in\mathbb{R}$ tale che
   $$
   a+0=0+a=a.
   $$

4. **Esistenza dell’inverso additivo**: per ogni $a\in\mathbb{R}$ esiste un elemento, indicato con $-a$, tale che
   $$
   a+(-a)=(-a)+a=0.
   $$

Il numero $-a$ è definito come l’unico numero che, sommato ad $a$, dà $0$. L’unicità dell’inverso additivo è una conseguenza degli assiomi, non una proprietà da aggiungere a parte.

### 3.2 Proprietà del prodotto

Per ogni $a,b,c\in\mathbb{R}$ valgono:

1. **Associatività**
   $$
   (ab)c=a(bc).
   $$

2. **Commutatività**
   $$
   ab=ba.
   $$

3. **Esistenza dell’elemento neutro moltiplicativo**: esiste $1\in\mathbb{R}$ tale che
   $$
   a\cdot 1=1\cdot a=a.
   $$

4. **Esistenza dell’inverso moltiplicativo**: per ogni $a\neq 0$ esiste $a^{-1}$, indicato anche con $\frac{1}{a}$, tale che
   $$
   aa^{-1}=a^{-1}a=1.
   $$

Anche qui l’inverso moltiplicativo è unico, ma l’unicità va dimostrata.

### 3.3 Proprietà distributiva

Somma e prodotto sono legati dalla proprietà distributiva:

$$
a(b+c)=ab+ac.
$$

È l’ultima proprietà fondamentale che collega le due operazioni.

In totale, le proprietà di campo sono:

- quattro proprietà della somma;
- quattro proprietà del prodotto;
- la proprietà distributiva.

### 3.4 Perché si introducono nuovi insiemi numerici?

La catena $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}\subset\mathbb{C}$ si può motivare guardando quali operazioni sono possibili:

- in $\mathbb{N}$ non sempre si può sottrarre: si introducono gli interi $\mathbb{Z}$;
- in $\mathbb{Z}$ non sempre si può dividere: si introducono i razionali $\mathbb{Q}$;
- in $\mathbb{Q}$ non esiste un numero il cui quadrato sia $2$: si introducono i reali $\mathbb{R}$;
- in $\mathbb{R}$ non esiste un numero il cui quadrato sia $-1$: si introducono i complessi $\mathbb{C}$.

Questa descrizione è intuitiva e non è una costruzione formale degli insiemi numerici.

Sottrazione e divisione non sono operazioni primitive in più:

- sottrarre $b$ significa sommare $-b$:
  $$
  a-b=a+(-b);
  $$
- dividere per $b\neq 0$ significa moltiplicare per l’inverso:
  $$
  \frac{a}{b}=a\cdot b^{-1}.
  $$

---

## 4. Gli assiomi di ordinamento

La relazione $\leq$ è un ordinamento totale su $\mathbb{R}$.

### 4.1 Totalità

Per ogni $x,y\in\mathbb{R}$,

$$
x\leq y\quad\text{oppure}\quad y\leq x.
$$

Questa proprietà dice che due numeri reali qualsiasi sono sempre confrontabili.

È una proprietà forte: non ogni relazione d’ordine è totale. Per esempio, con l’inclusione tra sottoinsiemi due sottoinsiemi possono non essere confrontabili, perché nessuno dei due è necessariamente contenuto nell’altro.

### 4.2 Riflessività

Per ogni $x\in\mathbb{R}$,

$$
x\leq x.
$$

Ogni numero è minore o uguale a se stesso.

### 4.3 Antisimmetria

Per ogni $x,y\in\mathbb{R}$,

$$
x\leq y\ \text{e}\ y\leq x
\quad\Longrightarrow\quad
x=y.
$$

Se ciascuno dei due numeri è minore o uguale all’altro, allora coincidono.

### 4.4 Transitività

Per ogni $x,y,z\in\mathbb{R}$,

$$
x\leq y\ \text{e}\ y\leq z
\quad\Longrightarrow\quad
x\leq z.
$$

È la proprietà che usiamo nelle catene di disuguaglianze.

Con la quantificazione completa si scrive

$$
\forall x,y,z\in\mathbb{R},\qquad
\left(x\leq y\land y\leq z\right)\Longrightarrow x\leq z.
$$

Riflessività, antisimmetria e transitività caratterizzano una relazione d’ordine; aggiungendo la totalità si ottiene un ordine totale.

---

## 5. Compatibilità tra ordine e operazioni

Gli assiomi di ordinamento interagiscono con quelli algebrici.

### 5.1 Compatibilità con la somma

Per ogni $x,y,z\in\mathbb{R}$,

$$
x\leq y
\quad\Longrightarrow\quad
x+z\leq y+z.
$$

Sommare lo stesso numero a entrambi i membri di una disuguaglianza non ne cambia il verso.

Questo assioma si indica schematicamente con $\mathrm{Ord}_S$.

### 5.2 Compatibilità con il prodotto per numeri non negativi

Se $x\geq 0$ e $y\geq 0$, allora

$$
xy\geq 0.
$$

Questa proprietà si indica con $\mathrm{Ord}_{P}$.

In altre parole, il prodotto di due numeri non negativi è non negativo.

### 5.3 Conseguenza: moltiplicazione per un numero non negativo

Dalle proprietà precedenti si deduce che, se

$$
x\leq y
\quad\text{e}\quad
z\geq 0,
$$

allora

$$
xz\leq yz.
$$

Infatti:

1. da $x\leq y$, sommando $-y$ a entrambi i membri si ottiene
   $$
   x-y\leq 0;
   $$
2. poiché $z\geq 0$ e $y-x\geq 0$, il prodotto di quantità non negative è non negativo;
3. usando la distributività e la compatibilità della somma con l’ordine si ricava
   $$
   xz\leq yz.
   $$

L’idea è che moltiplicare per una quantità non negativa conserva il verso della disuguaglianza.

Se invece $z\leq 0$, moltiplicare per $z$ inverte il verso:

$$
x\leq y,\quad z\leq 0
\quad\Longrightarrow\quad
xz\geq yz.
$$

Anche questa proprietà non è assunta a parte: si dimostra con gli assiomi già introdotti.

---

## 6. Proprietà derivate dagli assiomi

Gli assiomi sono pochi, ma combinandoli si deducono molte proprietà che usiamo continuamente. Alcuni esempi:

$$
0\cdot x=0,
$$

$$
(-1)x=-x,
$$

$$
(-x)(-y)=xy,
$$

$$
-(-x)=x.
$$

Queste identità non sono scritte direttamente negli assiomi e vanno dimostrate.

Anche il fatto che $1>0$ non è assunto esplicitamente negli assiomi di campo e di ordinamento, ma va dedotto. La dimostrazione non è immediata e può essere assegnata come esercizio.

Allo stesso modo, bisogna dimostrare che gli elementi neutri e gli inversi sono unici.

> [!warning]
> Non confondere ciò che è assunto come assioma con ciò che è una conseguenza dimostrabile. Le regole di calcolo usuali sono corrette, ma molte non sono primitive: derivano dagli assiomi.

---

## 7. Differenza tra $\mathbb{Q}$ e $\mathbb{R}$

Tutte le proprietà viste finora valgono anche in $\mathbb{Q}$. In particolare, $\mathbb{Q}$ è un campo ordinato.

Per ora, quindi, nulla distingue davvero $\mathbb{R}$ da $\mathbb{Q}$.

La differenza fondamentale compare con l’assioma di completezza.

---

## 8. Assioma di completezza o di continuità

Siano $A,B\subseteq\mathbb{R}$ due sottoinsiemi non vuoti. Si dice che $A$ sta **a sinistra di $B$** se

$$
\forall a\in A,\ \forall b\in B,\qquad a\leq b.
$$

Geometricamente, tutti gli elementi di $A$ si trovano a sinistra di tutti gli elementi di $B$ sulla retta reale.

L’assioma di completezza afferma che, se $A$ sta a sinistra di $B$, allora esiste almeno un numero reale $c$ che si trova tra i due insiemi:

$$
\exists c\in\mathbb{R}
\quad\text{tale che}\quad
\forall a\in A,\ \forall b\in B,\qquad
a\leq c\leq b.
$$

Il numero $c$ può appartenere ad $A$, a $B$, a entrambi, oppure a nessuno dei due.

L’assioma garantisce l’esistenza di un punto intermedio, non la sua unicità.

### 8.1 Intersezione tra $A$ e $B$

Gli insiemi $A$ e $B$ possono intersecarsi. Se $A$ sta a sinistra di $B$, la loro intersezione può contenere al massimo un punto.

Se

$$
c\in A\cap B,
$$

allora $c$ è necessariamente il punto di separazione tra i due insiemi. In generale, però, possono esserci molti punti reali compresi tra tutti gli elementi di $A$ e tutti gli elementi di $B$.

Esempi intuitivi:

- $A=(-\infty,1]$ e $B=[1,+\infty)$: il solo punto comune è $1$;
- $A=(-\infty,3]$ e $B=[3,+\infty)$: il solo punto comune è $3$;
- se tra $A$ e $B$ rimane un intervallo non vuoto, allora esistono molti possibili punti $c$.

L’esistenza del numero $3$ non è un assioma a parte: il numero $3$ si costruisce a partire da $1$ come

$$
3=1+1+1.
$$

### 8.2 Perché l’assioma non vale in $\mathbb{Q}$?

Consideriamo

$$
A=\left\{x\in\mathbb{Q}:x\geq 0,\ x^2\leq 2\right\},
$$

e

$$
B=\left\{x\in\mathbb{Q}:x\geq 0,\ x^2\geq 2\right\}.
$$

Ogni elemento di $A$ è minore o uguale a ogni elemento di $B$, quindi $A$ sta a sinistra di $B$.

L’ordinamento è intuitivo perché gli elementi sono non negativi: per numeri non negativi, al crescere del numero cresce anche il quadrato.

Se esistesse un numero razionale $c$ compreso tra $A$ e $B$, dovrebbe valere

$$
c^2=2.
$$

Infatti:

- se $c^2<2$, allora $c$ apparterrebbe ancora ad $A$ e non separerebbe correttamente i due insiemi;
- se $c^2>2$, allora $c$ apparterrebbe a $B$ e, di nuovo, non sarebbe il punto di separazione.

Ma non esiste alcun $c\in\mathbb{Q}$ tale che $c^2=2$. Se infatti

$$
c=\frac{p}{q}
$$

con $p,q\in\mathbb{Z}$ e frazione ridotta ai minimi termini, da

$$
\frac{p^2}{q^2}=2
$$

si ottiene

$$
p^2=2q^2.
$$

Questo implica che $p$ è pari; ponendo $p=2k$ si ricava che anche $q$ è pari, contraddicendo il fatto che la frazione fosse ridotta ai minimi termini.

Quindi in $\mathbb{Q}$ non esiste il punto intermedio richiesto dall’assioma di completezza.

In $\mathbb{R}$, invece, l’assioma garantisce l’esistenza di un numero $c$ tale che

$$
c^2=2.
$$

Questo numero sarà indicato con $\sqrt{2}$.

La completezza è dunque ciò che permette di colmare i “buchi” di $\mathbb{Q}$.

---

## 9. Esistenza e unicità dei numeri reali

In linea di principio gli assiomi potrebbero essere incompatibili: assumere troppe proprietà può portare a una struttura che non esiste.

Il teorema fondamentale, chiamato scherzosamente **teorema misterioso**, afferma che:

> Esiste una struttura $\left(\mathbb{R},+,\cdot,\leq\right)$ che soddisfa gli assiomi di campo ordinato e l’assioma di completezza, ed essa è unica a meno di isomorfismo.

L’esistenza significa che c’è davvero un insieme $\mathbb{R}$ con due operazioni e un ordinamento che soddisfano tutti gli assiomi.

L’unicità non significa che esista un solo insieme possibile chiamato $\mathbb{R}$. Significa che due strutture qualunque che soddisfano gli stessi assiomi sono indistinguibili dal punto di vista matematico.

Più precisamente, se

$$
(\mathbb{R},+,\cdot,\leq)
$$

e

$$
(\mathbb{R}',\oplus,\otimes,\preceq)
$$

sono due strutture che soddisfano gli assiomi dei reali, allora esiste una funzione [[Funzione biettiva|biiettiva]]

$$
\varphi:\mathbb{R}\longrightarrow\mathbb{R}'
$$

che preserva tutte le operazioni e l’ordinamento:

$$
\varphi(a+b)=\varphi(a)\oplus\varphi(b),
$$

$$
\varphi(ab)=\varphi(a)\otimes\varphi(b),
$$

e

$$
a\leq b
\quad\Longleftrightarrow\quad
\varphi(a)\preceq\varphi(b).
$$

La funzione $\varphi$ è un **[[Isomorfismo|isomorfismo]]**: una traduzione tra le due strutture che conserva tutta la struttura matematica.

Se si sommano due numeri nella prima struttura e poi si applica $\varphi$, si ottiene lo stesso risultato che si avrebbe traducendo prima i due numeri nella seconda struttura e sommandoli lì.

L’assioma di completezza è essenziale per l’unicità. Esistono molti campi ordinati, ma diventano unici, a meno di isomorfismo, quando si impone anche la completezza.

---

## 10. Naturali contenuti nei reali

Gli assiomi garantiscono l’esistenza di $0$ e $1$:

- $0$ è l’elemento neutro della somma;
- $1$ è l’elemento neutro del prodotto;
- inoltre $0\neq 1$.

A partire da questi si costruiscono i naturali:

$$
2=1+1,
$$

$$
3=1+1+1,
$$

e in generale

$$
n=\underbrace{1+\cdots+1}_{n\text{ volte}}.
$$

Questo definisce un’applicazione da $\mathbb{N}$ a $\mathbb{R}$.

Non è però immediato che i numeri naturali così costruiti siano tutti distinti. In alcuni campi, infatti, sommando ripetutamente $1$ si può tornare a $0$. Ad esempio, negli interi modulo $7$ vale

$$
7=0.
$$

Per dimostrare che in $\mathbb{R}$ i naturali sono distinti e che l’applicazione $\mathbb{N}\to\mathbb{R}$ è iniettiva, serve usare in modo sostanziale l’ordinamento e, in particolare, la completezza.

---

## 11. Maggioranti, minoranti, massimo e minimo

Sia $A\subseteq\mathbb{R}$ un insieme non vuoto.

### 11.1 Maggiorante

Un numero $M\in\mathbb{R}$ è un **[[Maggiorante|maggiorante]]** di $A$ se

$$
\forall a\in A,\qquad a\leq M.
$$

In questo caso $M$ è maggiore o uguale a tutti gli elementi di $A$.

L’insieme dei maggioranti di $A$ si può indicare con

$$
\operatorname{Mag}(A)
=
\left\{M\in\mathbb{R}:\forall a\in A,\ a\leq M\right\}.
$$

Un insieme può avere molti maggioranti. Se $M$ è un maggiorante, in genere lo è anche ogni numero $M'\geq M$.

I maggioranti non sono quindi necessariamente unici e non devono necessariamente appartenere ad $A$.

### 11.2 Minorante

Un numero $m\in\mathbb{R}$ è un **minorante** di $A$ se

$$
\forall a\in A,\qquad m\leq a.
$$

Un minorante è una barriera dal basso: è minore o uguale a tutti gli elementi di $A$.

Anche i minoranti possono essere numerosi e non devono appartenere ad $A$.

### 11.3 Massimo

Un numero $M\in\mathbb{R}$ è il **[[Massimo e minimo|massimo]]** di $A$ se:

1. $M\in A$;
2. $M$ è un maggiorante di $A$.

Formalmente,

$$
M=\max A
$$

se e solo se

$$
M\in A
\quad\text{e}\quad
\forall a\in A,\ a\leq M.
$$

Un maggiorante che appartiene all’insieme è dunque il massimo.

### 11.4 Minimo

Un numero $m\in\mathbb{R}$ è il **minimo** di $A$ se:

1. $m\in A$;
2. $m$ è un minorante di $A$.

Formalmente,

$$
m=\min A
$$

se e solo se

$$
m\in A
\quad\text{e}\quad
\forall a\in A,\ m\leq a.
$$

### 11.5 Unicità di massimo e minimo

Se il massimo esiste, è unico.

Supponiamo che $M_1$ e $M_2$ siano entrambi massimi di $A$. Poiché $M_1$ è massimo,

$$
M_2\leq M_1.
$$

Poiché anche $M_2$ è massimo,

$$
M_1\leq M_2.
$$

Per l’antisimmetria dell’ordine,

$$
M_1=M_2.
$$

Lo stesso ragionamento vale per il minimo.

> [!warning]
> Massimo e minimo non sono obbligati a esistere.

Esempi:

- $A=\mathbb{R}$ non ha maggioranti e quindi non ha massimo;
- $A=(0,1)$ ha maggioranti, ma non ha massimo, perché $1$ è un maggiorante ma non appartiene all’insieme;
- analogamente, $(0,1)$ non ha minimo.

---

## 12. Insiemi limitati

### 12.1 Limitatezza superiore

Un insieme $A\subseteq\mathbb{R}$ è **limitato superiormente** se ha almeno un maggiorante:

$$
\exists M\in\mathbb{R}\ \text{tale che}\ 
\forall a\in A,\ a\leq M.
$$

Non serve che esista un massimo: basta una barriera dall’alto.

### 12.2 Limitatezza inferiore

Un insieme $A$ è **limitato inferiormente** se ha almeno un minorante:

$$
\exists m\in\mathbb{R}\ \text{tale che}\ 
\forall a\in A,\ m\leq a.
$$

### 12.3 Insieme limitato

Un insieme si dice semplicemente **limitato** se è limitato sia superiormente sia inferiormente.

Una formulazione equivalente è:

$$
A\text{ è limitato}
\quad\Longleftrightarrow\quad
\exists L\in\mathbb{R}\ \text{tale che}\ 
\forall a\in A,\ |a|\leq L.
$$

Infatti la condizione

$$
|a|\leq L
$$

equivale a

$$
-L\leq a\leq L.
$$

Le due barriere si possono rendere simmetriche scegliendo $L$ abbastanza grande.

---

## 13. Estremo superiore ed estremo inferiore

Sia $A\subseteq\mathbb{R}$ non vuoto.

### 13.1 Estremo superiore

Se $A$ non è limitato superiormente, per convenzione si pone

$$
\sup A=+\infty.
$$

Se invece $A$ è limitato superiormente, l’insieme dei suoi maggioranti è non vuoto:

$$
\operatorname{Mag}(A)\neq\varnothing.
$$

In questo caso si definisce

$$
\sup A=\min\operatorname{Mag}(A).
$$

L’**[[Estremo superiore|estremo superiore]]** è quindi il più piccolo dei maggioranti.

Che questo minimo esista non è automatico dalla definizione: deriva dall’assioma di completezza.

### 13.2 Estremo inferiore

Se $A$ non è limitato inferiormente, si pone

$$
\inf A=-\infty.
$$

Se invece $A$ è limitato inferiormente, l’insieme dei minoranti è non vuoto e si definisce

$$
\inf A=\max\operatorname{Min}(A),
$$

dove $\operatorname{Min}(A)$ indica l’insieme dei minoranti di $A$.

L’estremo inferiore è quindi il più grande dei minoranti.

Anche l’esistenza di questo massimo deriva dall’assioma di completezza.

### 13.3 Relazione con massimo e minimo

Se il massimo esiste, coincide con il supremo:

$$
\max A=\sup A.
$$

Se il minimo esiste, coincide con l’infimo:

$$
\min A=\inf A.
$$

Quando massimo e minimo non esistono, supremo e infimo possono comunque esistere.

Esempio:

$$
A=(0,1).
$$

I maggioranti sono tutti i numeri $M\geq 1$, quindi

$$
\sup A=1.
$$

I minoranti sono tutti i numeri $m\leq 0$, quindi

$$
\inf A=0.
$$

Però $1\notin A$ e $0\notin A$, dunque $A$ non ha né massimo né minimo.

In questo senso supremo e infimo sono i numeri che “vorrebbero essere” massimo e minimo, ma non appartengono all’insieme.

---

## 14. Dimostrazione dell’esistenza del supremo

Consideriamo il caso non banale: $A$ è non vuoto e limitato superiormente.

Sia

$$
B=\operatorname{Mag}(A)
$$

l’insieme di tutti i maggioranti di $A$.

Per definizione, per ogni $a\in A$ e ogni $b\in B$ vale

$$
a\leq b.
$$

Quindi $A$ sta a sinistra di $B$.

Per l’assioma di completezza esiste un numero $c\in\mathbb{R}$ tale che

$$
\forall a\in A,\ \forall b\in B,\qquad a\leq c\leq b.
$$

Dalla prima disuguaglianza,

$$
\forall a\in A,\qquad a\leq c,
$$

si deduce che $c$ è un maggiorante di $A$. Pertanto

$$
c\in B.
$$

Dalla seconda disuguaglianza,

$$
\forall b\in B,\qquad c\leq b,
$$

si deduce che $c$ è minore o uguale a ogni maggiorante di $A$. Quindi $c$ è il minimo dell’insieme dei maggioranti:

$$
c=\min B.
$$

Per definizione,

$$
c=\sup A.
$$

Dunque ogni insieme non vuoto e limitato superiormente ha un estremo superiore.

La dimostrazione per l’infimo è analoga, scambiando:

- maggioranti con minoranti;
- minimo con massimo;
- sinistra con destra.

Questa dimostrazione mostra il legame diretto tra completezza e supremi: il supremo non è una proprietà puramente algebrica, ma una conseguenza dell’assioma di continuità.

---

## 15. Caratterizzazione del supremo

La definizione di $\sup A$ si può riscrivere con i quantificatori, in una forma basata su una proprietà di approssimazione.

### 15.1 Caso $\sup A=+\infty$

Per un insieme non vuoto $A\subseteq\mathbb{R}$,

$$
\sup A=+\infty
$$

se e solo se

$$
\forall M\in\mathbb{R},\ \exists a\in A
\quad\text{tale che}\quad
a>M.
$$

Equivalentemente si può scrivere $a\geq M$, a seconda della convenzione; la forma con $a>M$ dice chiaramente che l’insieme contiene elementi arbitrariamente grandi.

#### Dimostrazione tramite negazione

Dire che $A$ non è limitato superiormente significa negare

$$
\exists M\in\mathbb{R}\ \text{tale che}\ \forall a\in A,\ a\leq M.
$$

Negando i quantificatori si ottiene

$$
\forall M\in\mathbb{R},\ \exists a\in A
\quad\text{tale che}\quad
a>M.
$$

L’ordine dei quantificatori è essenziale:

1. si sceglie prima un $M$ qualunque;
2. dopo aver visto $M$, l’insieme $A$ deve fornire un elemento $a$ più grande di $M$.

Non sarebbe equivalente chiedere un unico $a$ che superi tutti gli $M$.

Geometricamente: per ogni barriera reale $M$, l’insieme riesce a produrre un elemento oltre quella barriera.

### 15.2 Caso $\sup A=L\in\mathbb{R}$

Per $A\neq\varnothing$, vale

$$
\sup A=L
$$

se e solo se valgono entrambe le condizioni:

1. $L$ è un maggiorante di $A$:
   $$
   \forall a\in A,\qquad a\leq L;
   $$

2. ogni intervallo immediatamente a sinistra di $L$ contiene almeno un elemento di $A$:
   $$
   \forall \varepsilon>0,\ \exists a\in A
   \quad\text{tale che}\quad
   L-\varepsilon<a.
   $$

La seconda condizione si può esprimere anche come

$$
\forall \varepsilon>0,\ \exists a\in A
\quad\text{tale che}\quad
L-\varepsilon<a\leq L.
$$

La prima condizione dice che $A$ sta tutto a sinistra di $L$. La seconda dice che $L$ non si può abbassare nemmeno di una quantità arbitrariamente piccola.

Se per qualche $\varepsilon>0$ non esistesse alcun elemento di $A$ maggiore di $L-\varepsilon$, allora tutti gli elementi di $A$ soddisferebbero

$$
a\leq L-\varepsilon.
$$

In tal caso $L-\varepsilon$ sarebbe un maggiorante di $A$, più piccolo di $L$, contraddicendo il fatto che $L$ è il minimo dei maggioranti.

Qui compare per la prima volta in modo strutturale il parametro $\varepsilon$, che sarà centrale nella definizione di limite.

> [!example] Esempio
> Per $A=(0,1)$ si ha $\sup A=1$. Verifichiamo la seconda condizione: dato $\varepsilon>0$ (diciamo $\varepsilon<1$), il numero $a=1-\frac{\varepsilon}{2}$ appartiene ad $A$ e vale $1-\varepsilon<a\leq 1$. Quindi non c’è modo di abbassare $1$ restando un maggiorante.

---

## 16. Caratterizzazione dell’infimo

In modo analogo:

$$
\inf A=-\infty
$$

se e solo se

$$
\forall M\in\mathbb{R},\ \exists a\in A
\quad\text{tale che}\quad
a<M.
$$

Se invece $\inf A=l\in\mathbb{R}$, allora:

1. $l$ è un minorante:
   $$
   \forall a\in A,\qquad l\leq a;
   $$

2. ogni intervallo immediatamente a destra di $l$ contiene almeno un elemento di $A$:
   $$
   \forall\varepsilon>0,\ \exists a\in A
   \quad\text{tale che}\quad
   a<l+\varepsilon.
   $$

Equivalentemente,

$$
\forall\varepsilon>0,\ \exists a\in A
\quad\text{tale che}\quad
l\leq a<l+\varepsilon.
$$

Se non esistesse un elemento di $A$ minore di $l+\varepsilon$, allora $l+\varepsilon$ non descriverebbe correttamente l’azione dell’estremo inferiore; l’idea è simmetrica a quella del supremo.

---

## 17. Il ruolo dell’insieme vuoto

Molte definizioni vengono date assumendo

$$
A\neq\varnothing.
$$

Questa ipotesi evita casi patologici o poco utili.

Formalmente, ogni numero reale è un maggiorante dell’insieme vuoto, perché la proposizione

$$
\forall a\in\varnothing,\qquad a\leq M
$$

è vera per ogni $M$: non esistono elementi dell’insieme vuoto che possano violarla.

Analogamente, ogni numero reale è un minorante dell’insieme vuoto.

Se si provasse a definire supremo e infimo del vuoto con le stesse formule, si otterrebbero convenzioni problematiche:

- l’insieme dei maggioranti sarebbe tutto $\mathbb{R}$;
- l’insieme dei minoranti sarebbe tutto $\mathbb{R}$;
- non esisterebbe il minimo di $\mathbb{R}$ né il massimo di $\mathbb{R}$;
- con le convenzioni estese si arriverebbe alla situazione paradossale
  $$
  \inf\varnothing=+\infty,
  \qquad
  \sup\varnothing=-\infty.
  $$

Per questo, nei contesti del corso, $\sup A$ e $\inf A$ si considerano per insiemi non vuoti.

La stessa attenzione al vuoto serve nella teoria degli insiemi. Ad esempio:

- esiste un’unica funzione dall’insieme vuoto all’insieme vuoto;
- esiste un’unica funzione dall’insieme vuoto a un insieme qualunque;
- il numero di funzioni da un insieme con due elementi a un insieme con cinque elementi è
  $$
  5^2=25.
  $$

Le formule generali vanno formulate in modo da restare coerenti anche quando compare l’insieme vuoto.

---

## 18. Esempio: il supremo di $\mathbb{N}$

Consideriamo $\mathbb{N}$ come sottoinsieme di $\mathbb{R}$. L’affermazione

$$
\sup\mathbb{N}=+\infty
$$

equivale a dire che $\mathbb{N}$ non è limitato superiormente:

$$
\forall L\in\mathbb{R},\ \exists n\in\mathbb{N}
\quad\text{tale che}\quad
n>L.
$$

In altre parole, per ogni numero reale esiste un numero naturale che lo supera.

Si dimostra per assurdo. Supponiamo che $\mathbb{N}$ sia limitato superiormente e poniamo

$$
\sup\mathbb{N}=L\in\mathbb{R}.
$$

Usando la caratterizzazione del supremo, scegliamo $\varepsilon=\frac12$. Esiste allora $n\in\mathbb{N}$ tale che

$$
L-\frac12<n\leq L.
$$

Poiché $n+1\in\mathbb{N}$, possiamo sommare $1$ alla disuguaglianza:

$$
L-\frac12+1<n+1.
$$

Poiché

$$
L-\frac12+1=L+\frac12>L,
$$

segue che

$$
n+1>L.
$$

Ma $n+1$ è un numero naturale, quindi abbiamo trovato un elemento di $\mathbb{N}$ maggiore di $L$, contraddicendo il fatto che $L$ fosse un maggiorante.

Pertanto $\mathbb{N}$ non ha maggioranti e

$$
\sup\mathbb{N}=+\infty.
$$

La dimostrazione usa proprietà elementari come

$$
-\frac12+1=\frac12
$$

e

$$
\frac12>0,
$$

che vanno anch’esse giustificate a partire dagli assiomi se si vuole una fondazione completamente formale.

Nota bene: il risultato non segue dai soli assiomi di campo ordinato. Esistono campi ordinati in cui l’insieme ottenuto sommando ripetutamente $1$ resta limitato superiormente. La non limitatezza di $\mathbb{N}$ è una conseguenza della completezza dei reali.

---

## 19. Significato concettuale della completezza

L’assioma di completezza:

- distingue $\mathbb{R}$ da $\mathbb{Q}$;
- garantisce l’esistenza di punti di separazione tra insiemi ordinati;
- garantisce l’esistenza del supremo per ogni insieme non vuoto e limitato superiormente;
- garantisce l’esistenza dell’infimo per ogni insieme non vuoto e limitato inferiormente;
- permette di trattare numeri come $\sqrt{2}$;
- è alla base della teoria dei limiti.

In particolare, il supremo è una versione precisa dell’idea di “punto più a destra possibile”, anche quando questo punto non appartiene all’insieme. La caratterizzazione con $\varepsilon$ formalizza il fatto che ogni punto strettamente più piccolo del supremo non può essere un maggiorante.

Questa struttura di approssimazione da destra e da sinistra sarà la base concettuale delle definizioni di limite che vedremo più avanti.
