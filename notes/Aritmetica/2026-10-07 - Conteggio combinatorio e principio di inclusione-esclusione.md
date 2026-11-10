---
type: lecture-note
course: Aritmetica
date: '2026-10-07'
title: Conteggio combinatorio e principio di inclusione-esclusione
source_transcript: _transcripts/Aritmetica/2026-10-06 - Conteggio combinatorio e principio di inclusione-esclusione.md
source_hash: sha256:3b83a8f1346e7eca210322b426b54f5cf7f3990011457579245ae10db83fe4d3
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-06T13:51:39.890Z'
original_date: '2026-10-06'
date_adjustment: Shifted forward one day to keep one note per course and date.
vault_path: Notes/Aritmetica/Lectures/2026-10-07 - Conteggio combinatorio e principio di inclusione-esclusione.md
vault_hash: daa66b1ff7a5d2d42d267cc219dea6e252ca1f3dd73c28ab1d2573f096223e60
---

## 1. Anagrammi con lettere ripetute

### 1.1. Il caso senza ripetizioni

Se una parola ha $n$ lettere tutte distinte, il numero di anagrammi è il numero di modi di ordinare $n$ oggetti distinti:

$$
n!.
$$

Per esempio, con quattro lettere diverse si ottengono

$$
4! = 24
$$

anagrammi.

Il ragionamento è scegliere:

- la lettera da mettere al primo posto: $n$ possibilità;
- la lettera da mettere al secondo posto: $n-1$ possibilità;
- e così via.

Il totale è quindi

$$
n(n-1)(n-2)\cdots 1=n!.
$$

### 1.2. Il problema delle lettere ripetute

Prendiamo la parola `Ana`. Le lettere sono tre, ma le due $A$ sono uguali. Se fossero tutte distinte avremmo

$$
3! = 6
$$

ordinamenti. Ma trattare le due $A$ come distinte produce ripetizioni.

Chiamiamo provvisoriamente le due $A$ con $A_1$ e $A_2$. Per ogni anagramma effettivo, le due copie si possono scambiare in

$$
2!
$$

modi senza cambiare la parola che si vede. Quindi ogni anagramma è contato due volte e il numero corretto è

$$
\frac{3!}{2!}=3.
$$

Gli anagrammi distinti (ignorando maiuscole e minuscole) sono infatti:

- `aan`;
- `ana`;
- `naa`.

Il punto fondamentale: se all’inizio contiamo le lettere ripetute come se fossero distinte, poi dobbiamo dividere per le permutazioni interne delle copie indistinguibili.

### 1.3. Formula generale: coefficiente multinomiale

Supponiamo che una parola abbia lunghezza $n$ e contenga:

- $n_1$ copie di una prima lettera;
- $n_2$ copie di una seconda lettera;
- $\dots$;
- $n_k$ copie di una $k$-esima lettera.

Allora

$$
n_1+n_2+\cdots+n_k=n
$$

e il numero di anagrammi distinti è

$$
\frac{n!}{n_1!n_2!\cdots n_k!}.
$$

Il numeratore $n!$ conta tutti gli ordinamenti distinguendo le singole copie. Il denominatore corregge il sovraconteggio:

- le $n_1$ copie della prima lettera si possono permutare in $n_1!$ modi;
- le $n_2$ copie della seconda lettera in $n_2!$ modi;
- e così via.

Questa quantità si chiama **[[Coefficiente multinomiale|coefficiente multinomiale]]** e si indica spesso con

$$
\binom{n}{n_1,n_2,\ldots,n_k}
=
\frac{n!}{n_1!n_2!\cdots n_k!}.
$$

#### Esempio: `nonno`

La parola `nonno` contiene:

- tre lettere $n$;
- due lettere $o$.

Il numero di anagrammi distinti è quindi

$$
\frac{5!}{3!2!}
=
\frac{120}{6\cdot 2}
=
10.
$$

### 1.4. Interpretazione tramite partizioni

Il coefficiente multinomiale conta anche i modi di partizionare un insieme di $n$ elementi in $k$ sottoinsiemi distinguibili di cardinalità fissate $n_1,\ldots,n_k$.

Sia $X$ un insieme con $n$ elementi. Il numero di partizioni ordinate

$$
X=X_1\sqcup X_2\sqcup\cdots\sqcup X_k
$$

con

$$
|X_i|=n_i
$$

è

$$
\binom{n}{n_1,n_2,\ldots,n_k}.
$$

La corrispondenza con gli anagrammi è questa:

- gli elementi di $X_i$ corrispondono alle posizioni occupate dalla $i$-esima lettera;
- assegnare a ogni posizione una lettera equivale a dividere l’insieme delle posizioni nei gruppi corrispondenti alle varie lettere.

È una corrispondenza biunivoca: a ogni anagramma si associa una partizione delle posizioni, e a ogni partizione un anagramma.

Con sole due lettere, il coefficiente multinomiale diventa il [[Coefficiente binomiale|coefficiente binomiale]]:

$$
\binom{n}{k}
=
\frac{n!}{k!(n-k)!}.
$$

Con $k$ tipi di lettere si parla, in generale, di coefficiente multinomiale.

---

## 2. Conteggio di funzioni

Siano $X$ e $Y$ insiemi finiti, con

$$
|X|=n,
\qquad
|Y|=m.
$$

### 2.1. Numero totale di funzioni

Per ogni elemento $x\in X$ si può scegliere liberamente la sua immagine in $Y$. Ci sono $m$ possibilità per ciascuno degli $n$ elementi di $X$, quindi il numero totale di [[Funzione|funzioni]] $f:X\to Y$ è

$$
m^n.
$$

Questa formula conta tutte le funzioni, senza chiedere che siano iniettive o suriettive.

### 2.2. Funzioni suriettive e biettive

Una funzione $f:X\to Y$ è **suriettiva** se ogni elemento di $Y$ sta nell’immagine di $f$:

$$
\operatorname{Im}(f)=Y.
$$

Se $|X|=|Y|=n$, una funzione è suriettiva se e solo se è [[Funzione biettiva|biettiva]]. In questo caso il numero di funzioni suriettive, cioè di biezioni, è

$$
n!.
$$

Infatti una biezione è semplicemente un ordinamento degli elementi di $Y$ associati, uno alla volta, agli elementi di $X$.

In generale, se $n<m$ non esistono funzioni suriettive da $X$ a $Y$, perché il dominio non ha abbastanza elementi per coprire tutto il codominio.

---

## 3. Caso particolare: funzioni suriettive da un insieme di cardinalità $n$ a uno di cardinalità $n-1$

Consideriamo una funzione suriettiva

$$
f:X\to Y
$$

con

$$
|X|=n,
\qquad
|Y|=n-1.
$$

Il dominio ha un elemento in più del codominio, quindi almeno due elementi distinti di $X$ hanno la stessa immagine. Per la suriettività, l’unica situazione possibile è questa:

- due elementi distinti $x_1,x_2\in X$ vengono mandati nello stesso elemento $y\in Y$;
- gli altri $n-2$ elementi di $X$ vengono mandati biiettivamente nei restanti $n-2$ elementi di $Y$.

Il conteggio si fa in tre passi.

### Passo 1: scegliere i due elementi che vengono identificati

Si scelgono due elementi distinti di $X$:

$$
\binom{n}{2}.
$$

### Passo 2: scegliere la loro immagine comune

Si sceglie l’elemento di $Y$ su cui vengono mandati entrambi:

$$
n-1
$$

possibilità.

### Passo 3: scegliere la biezione restante

Restano:

- $n-2$ elementi nel dominio;
- $n-2$ elementi nel codominio.

Le funzioni biettive tra questi due insiemi sono

$$
(n-2)!
$$

in numero.

Complessivamente:

$$
\binom{n}{2}(n-1)(n-2)!.
$$

Semplificando,

$$
\binom{n}{2}(n-1)(n-2)!
=
\frac{n(n-1)}{2}(n-1)(n-2)!
=
\frac{n!(n-1)}{2}.
$$

Questa strategia è relativamente semplice perché la differenza tra le cardinalità è solo $1$. Se invece $|Y|=n-2$, le possibilità si complicano: si può avere

- un gruppo di tre elementi del dominio mandati nello stesso elemento del codominio;
- oppure due coppie di elementi del dominio mandate in due elementi distinti del codominio.

Per differenze maggiori il numero di configurazioni cresce in fretta. Meglio, allora, un metodo generale.

---

## 4. Principio di inclusione-esclusione

### 4.1. Formula per due insiemi

Per due sottoinsiemi $A,B$ di un insieme universo,

$$
|A\cup B|
=
|A|+|B|-|A\cap B|.
$$

Si sottrae $|A\cap B|$ perché gli elementi dell’intersezione sono stati contati due volte.

> [!example] Esempio
> Tra i numeri da $1$ a $100$, quanti sono divisibili per $2$ o per $3$? Sono $50$ i multipli di $2$, $33$ i multipli di $3$ e $16$ i multipli di $6$ (cioè di entrambi), quindi $50+33-16=67$.

### 4.2. Formula generale

Per $m$ insiemi $A_1,\ldots,A_m$, il [[Principio di inclusione-esclusione|principio di inclusione-esclusione]] dice che

$$
\left|\bigcup_{i=1}^{m}A_i\right|
=
\sum_{i}|A_i|
-
\sum_{i<j}|A_i\cap A_j|
+
\sum_{i<j<k}|A_i\cap A_j\cap A_k|
-\cdots
+(-1)^{m+1}|A_1\cap\cdots\cap A_m|.
$$

I segni si alternano:

- si sommano le cardinalità dei singoli insiemi;
- si sottraggono le intersezioni a due a due;
- si sommano le intersezioni a tre a tre;
- si continua alternando.

La formula è utile soprattutto quando tutte le intersezioni dello stesso ordine hanno la stessa cardinalità.

---

## 5. Conteggio delle funzioni suriettive tramite inclusione-esclusione

Siano

$$
|X|=n,
\qquad
|Y|=m.
$$

Vogliamo contare le funzioni suriettive $f:X\to Y$.

### 5.1. Funzioni non suriettive

Una funzione non è suriettiva se almeno un elemento di $Y$ non sta nella sua immagine.

Per ogni $i\in Y$ definiamo

$$
F_i
=
\{f:X\to Y:\ i\notin\operatorname{Im}(f)\}.
$$

Quindi $F_i$ è l’insieme delle funzioni che evitano l’elemento $i$ del codominio.

L’insieme delle funzioni non suriettive è

$$
F_1\cup F_2\cup\cdots\cup F_m.
$$

Infatti una funzione non suriettiva omette almeno un elemento del codominio, quindi sta in almeno uno degli insiemi $F_i$.

In generale gli insiemi $F_i$ non sono disgiunti: una funzione può evitare più elementi di $Y$ contemporaneamente.

### 5.2. Cardinalità delle intersezioni

Per un singolo insieme $F_i$, l’immagine può contenere solo gli altri $m-1$ elementi di $Y$. Quindi

$$
|F_i|=(m-1)^n.
$$

Per un’intersezione di due insiemi, per esempio $F_1\cap F_2$, la funzione deve evitare due elementi del codominio. Per ogni elemento del dominio restano quindi $m-2$ valori possibili:

$$
|F_1\cap F_2|=(m-2)^n.
$$

Più in generale, fissati $k$ elementi distinti di $Y$ da evitare,

$$
|F_{i_1}\cap\cdots\cap F_{i_k}|
=
(m-k)^n.
$$

Gli elementi da evitare si possono scegliere in

$$
\binom{m}{k}
$$

modi.

### 5.3. Formula generale

Il numero totale di funzioni da $X$ a $Y$ è $m^n$. Togliendo le funzioni non suriettive con l’inclusione-esclusione si ottiene:

$$
\#\{\text{funzioni suriettive }X\to Y\}
=
\sum_{k=0}^{m}
(-1)^k\binom{m}{k}(m-k)^n.
$$

Scritta per esteso:

$$
m^n
-
\binom{m}{1}(m-1)^n
+
\binom{m}{2}(m-2)^n
-\cdots
+
(-1)^m\binom{m}{m}0^n.
$$

Per $n>0$ l’ultimo termine è nullo perché

$$
0^n=0.
$$

Quindi la somma spesso si può fermare a $k=m-1$.

La formula vale anche quando $m>n$: il risultato è $0$, come deve essere, perché non può esserci una suriezione da un insieme più piccolo a uno più grande.

### 5.4. Perché le intersezioni dello stesso ordine hanno la stessa cardinalità

Non importa quali siano i $k$ elementi del codominio esclusi: se ne escludiamo $k$, restano sempre $m-k$ valori possibili. Perciò tutte le intersezioni di $k$ insiemi $F_i$ hanno cardinalità

$$
(m-k)^n.
$$

Questo permette di raggruppare tutte le intersezioni dello stesso ordine in un unico termine:

$$
\binom{m}{k}(m-k)^n.
$$

Il coefficiente binomiale conta la scelta dei $k$ elementi da escludere; il fattore $(m-k)^n$ conta le funzioni che evitano quegli elementi.

### 5.5. Verifica nel caso $m=n$

Se $|X|=|Y|=n$, le funzioni suriettive sono le biezioni e devono essere $n!$. La formula di inclusione-esclusione diventa

$$
\sum_{k=0}^{n}
(-1)^k\binom{n}{k}(n-k)^n=n!.
$$

L’identità coincide con il conteggio diretto delle permutazioni, ma l’uguaglianza non è evidente guardando solo la formula. È un esempio di identità combinatoria che si può dimostrare contando lo stesso oggetto in due modi diversi.

---

## 6. Double counting e identità combinatorie

Una tecnica generale della combinatoria è contare lo stesso insieme, o la stessa famiglia di oggetti, in due modi diversi.

Se un insieme di oggetti viene contato:

- con il metodo A, ottenendo la formula $P$;
- con il metodo B, ottenendo la formula $Q$;

allora necessariamente

$$
P=Q.
$$

Questo approccio si chiama **double counting**, cioè conteggio doppio.

Il vantaggio è che certe identità algebriche, difficili da dimostrare direttamente, diventano naturali se si riconosce l’oggetto combinatorio che entrambe le espressioni contano.

Un principio metodologico importante:

> Quando compare una sommatoria con coefficienti binomiali, conviene cercare un’interpretazione combinatoria dei suoi termini prima di manipolarla algebricamente.

---

## 7. Conteggio di coppie di sottoinsiemi con intersezione fissata

Sia $U$ un insieme con

$$
|U|=100.
$$

Vogliamo contare le coppie ordinate di sottoinsiemi $(A,B)$ tali che

$$
|A\cap B|=30.
$$

### 7.1. Prima scelta: fissare l’intersezione

Scegliamo prima l’insieme

$$
I=A\cap B
$$

di cardinalità $30$.

Ci sono

$$
\binom{100}{30}
$$

possibilità.

Fissato $I$, gli altri $70$ elementi di $U\setminus I$ non possono appartenere contemporaneamente ad $A$ e a $B$, altrimenti starebbero nell’intersezione.

Per ciascuno di questi elementi ci sono esattamente tre possibilità:

1. sta in $A$ ma non in $B$;
2. sta in $B$ ma non in $A$;
3. non sta né in $A$ né in $B$.

Quindi i $70$ elementi si possono assegnare in

$$
3^{70}
$$

modi.

Il numero totale di coppie è dunque

$$
\boxed{
\binom{100}{30}3^{70}
}.
$$

Questa strategia funziona meglio che scegliere prima $A$ e $B$ a caso e poi imporre il vincolo sulla loro intersezione.

### 7.2. Interpretazione come partizione

Fissato $I=A\cap B$, l’insieme $U$ si divide in quattro regioni:

- $A\cap B=I$;
- $A\setminus B$;
- $B\setminus A$;
- $U\setminus(A\cup B)$.

Gli elementi di $I$ hanno già la loro destinazione: stanno sia in $A$ sia in $B$. Gli altri $70$ si possono collocare nelle tre regioni rimanenti, da cui il fattore $3^{70}$.

---

## 8. Tassellazioni di una griglia $2\times n$

Consideriamo una griglia rettangolare $2\times n$ da ricoprire interamente con tessere $2\times 1$.

Le tessere possono essere disposte:

- verticalmente, occupando una colonna intera;
- orizzontalmente, in coppia, occupando due caselle sovrapposte nella stessa zona.

Indichiamo con $T_n$ il numero di tassellazioni della griglia $2\times n$.

### 8.1. Casi iniziali

Per $n=1$ c’è una sola tassellazione, con una tessera verticale:

$$
T_1=1.
$$

Per $n=2$ ce ne sono due:

- due tessere verticali;
- due tessere orizzontali.

Quindi

$$
T_2=2.
$$

È utile anche porre

$$
T_0=1,
$$

pensando alla tassellazione vuota dell’insieme vuoto.

### 8.2. Relazione di ricorrenza

Guardiamo la prima parte della tassellazione.

#### Primo caso: prima tessera verticale

Se la tassellazione inizia con una tessera verticale, resta da tassellare una griglia $2\times(n-1)$. Le possibilità sono

$$
T_{n-1}.
$$

#### Secondo caso: prime due tessere orizzontali

Se la prima colonna non è coperta da una tessera verticale, le prime due caselle della riga superiore e le prime due della riga inferiore devono essere coperte da due tessere orizzontali. Resta una griglia $2\times(n-2)$, che si tassella in

$$
T_{n-2}
$$

modi.

I due casi sono disgiunti ed esauriscono tutte le possibilità. Quindi:

$$
\boxed{
T_n=T_{n-1}+T_{n-2}
}
$$

con condizioni iniziali

$$
T_0=1,\qquad T_1=1.
$$

È la [[Successione di Fibonacci|successione di Fibonacci]] traslata di un indice. Se $F_0=0$, $F_1=1$, allora

$$
T_n=F_{n+1}.
$$

Per esempio:

$$
T_1=1,\quad T_2=2,\quad T_3=3,\quad T_4=5,\quad T_5=8.
$$

La [[Successione per ricorrenza|ricorrenza]] dipende dalla struttura del problema, mentre i valori iniziali determinano quale successione si ottiene. La stessa legge

$$
a_n=a_{n-1}+a_{n-2}
$$

con condizioni iniziali diverse darebbe una successione diversa.

### 8.3. Secondo metodo: classificare per numero di tessere orizzontali

Ogni tassellazione si può classificare in base al numero $k$ di coppie di tessere orizzontali.

Ogni coppia di tessere orizzontali occupa una lunghezza $2$, mentre ogni tessera verticale occupa una colonna, cioè una lunghezza $1$.

Se ci sono $k$ coppie orizzontali, occupano $2k$ colonne. Le colonne rimanenti sono occupate da tessere verticali, e sono

$$
n-2k.
$$

In totale ci sono

$$
k+(n-2k)=n-k
$$

blocchi:

- $k$ blocchi del tipo “coppia orizzontale”;
- $n-2k$ blocchi del tipo “tessera verticale”.

Per costruire una tassellazione basta scegliere quali $k$ degli $n-k$ blocchi sono coppie orizzontali. Le possibilità sono

$$
\binom{n-k}{k}.
$$

Il massimo valore di $k$ è

$$
\left\lfloor\frac n2\right\rfloor,
$$

perché in una griglia di lunghezza $n$ non si possono mettere più di $\lfloor n/2\rfloor$ coppie orizzontali.

Si ottiene la formula esplicita

$$
\boxed{
T_n=
\sum_{k=0}^{\lfloor n/2\rfloor}
\binom{n-k}{k}
}.
$$

Questa somma dà lo stesso numero della ricorrenza di Fibonacci:

$$
\sum_{k=0}^{\lfloor n/2\rfloor}
\binom{n-k}{k}
=
F_{n+1}.
$$

È un esempio di double counting:

- il primo metodo conta le tassellazioni in base alla prima tessera e porta alla ricorrenza;
- il secondo le conta in base al numero di coppie orizzontali e porta alla somma binomiale.

---

## 9. Esempio di conteggio basato sulla parità

Consideriamo l’insieme dei numeri

$$
\{1,2,\ldots,100\},
$$

formato da:

- $50$ numeri pari;
- $50$ numeri dispari.

Vogliamo scegliere un sottoinsieme di cardinalità $96$ con somma pari.

Una somma di interi è pari se e solo se il numero degli addendi dispari è pari. I numeri pari non cambiano la parità della somma: la decidono i dispari.

Se scegliamo $j$ numeri dispari, dobbiamo scegliere anche $96-j$ numeri pari. Il valore $j$ deve essere pari e rispettare i limiti dati dal numero di elementi disponibili.

I valori pari possibili sono:

$$
j=46,\ 48,\ 50.
$$

Il numero di sottoinsiemi cercato è quindi

$$
\binom{50}{46}\binom{50}{50}
+
\binom{50}{48}\binom{50}{48}
+
\binom{50}{50}\binom{50}{46}.
$$

Equivalentemente, usando il numero di pari scelti:

$$
\boxed{
\binom{50}{50}\binom{50}{46}
+
\binom{50}{48}\binom{50}{48}
+
\binom{50}{46}\binom{50}{50}
}.
$$

La regola generale:

> La somma di un insieme di interi è pari se e solo se il sottoinsieme degli elementi dispari scelti ha cardinalità pari.

Se invece scegliamo $47$ numeri dispari, la somma è dispari, perché il numero di addendi dispari è dispari.

---

## 10. Osservazioni metodologiche

Gli esercizi della lezione mostrano alcune strategie fondamentali di conteggio:

1. **Contare direttamente le scelte successive**, come per le permutazioni.
2. **Correggere le ripetizioni**, dividendo per le permutazioni delle copie indistinguibili.
3. **Scomporre in casi disgiunti**, come nella ricorrenza delle tassellazioni.
4. **Contare il complementare**, quando il problema diretto è complicato ma il totale è semplice.
5. **Applicare il principio di inclusione-esclusione** quando gli insiemi da unire si sovrappongono.
6. **Fissare prima una struttura importante**, come l’intersezione $A\cap B$, per semplificare il conteggio successivo.
7. **Contare lo stesso oggetto in due modi**, ottenendo identità combinatorie.
8. **Interpretare le somme binomiali**, invece di trattarle solo come espressioni algebriche.

Davanti a un problema di conteggio conviene sempre chiedersi:

- Qual è l’insieme degli oggetti da contare?
- Le scelte sono indipendenti?
- Sto contando ogni oggetto una sola volta?
- Alcuni oggetti sono contati più volte?
- È più semplice contare il complementare?
- Posso dividere gli oggetti in casi disgiunti?
- C’è una struttura naturale da fissare per prima?
- La stessa famiglia si può descrivere in un secondo modo?
