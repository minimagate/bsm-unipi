---
type: lecture-note
course: Geometria 1
date: '2026-09-23'
title: Insiemi, applicazioni e spazi vettoriali
source_transcript: _transcripts/Geometria 1/2026-09-23 - Insiemi, applicazioni e spazi vettoriali.md
source_hash: sha256:b46d37b13beecd9d1c6d4928613205d8b86d908462b5efadb7426c0b3b686b60
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-23T10:33:40.887Z'
vault_path: Notes/Geometria 1/Lectures/2026-09-23 - Insiemi, applicazioni e spazi vettoriali.md
vault_hash: 1fc33cd7b7f71b356ce9700ef44b6084c505a06c44b4d8192107ebd121ea3835
---
> **Corso:** Geometria 1  
> **Data:** 23 settembre 2026

## Indicazioni sul corso e metodo di lavoro

Per il corso ci sono delle note, ricavate da materiali degli anni scorsi, che coprono almeno la prima parte del programma. Non hanno la struttura di un libro, ma sono un buon riferimento da usare insieme agli appunti e agli esercizi.

Ogni due settimane circa verranno assegnati degli esercizi. In genere non saranno corretti sistematicamente: servono soprattutto a stare al passo con gli argomenti e a lavorare in autonomia.

Conviene seguire il corso con continuità. Il linguaggio matematico vuole precisione: cambiare l’ordine delle parole, omettere una condizione o usare un simbolo a caso può cambiare il significato di un’affermazione. Parte della difficoltà iniziale di Geometria 1 viene proprio dal passaggio a un linguaggio più astratto e formale.

Il docente ha insistito sull’importanza di fare gli esercizi di persona. Si possono usare strumenti di intelligenza artificiale per controllare o discutere una soluzione già scritta, ma delegare tutto lo svolgimento impedisce di imparare la tecnica: si impara con lo sforzo e con il lavoro fatto davvero.

---

## 1. Insiemi e operazioni tra insiemi

### 1.1 Notazione per gli insiemi

Un [[Insieme|insieme]] si indica di solito con una lettera maiuscola, ad esempio $A$, mentre i suoi elementi si indicano con lettere minuscole o con altri simboli.

Un modo per descrivere un insieme è l’elencazione dei suoi elementi:

$$
A=\{a,b,c\}.
$$

La notazione

$$
a\in A
$$

significa che $a$ è un elemento di $A$.

La negazione si scrive

$$
a\notin A.
$$

Gli insiemi sono oggetti primitivi: qui non si dà una definizione ulteriore di “insieme”, ci si limita a fissare notazioni e operazioni fondamentali.

### 1.2 Intersezione

Dati due insiemi $X$ e $Y$, la loro [[Operazioni tra insiemi|intersezione]] è l’insieme degli elementi che appartengono a entrambi:

$$
X\cap Y=\{a\mid a\in X \text{ e } a\in Y\}.
$$

Quindi:

$$
a\in X\cap Y
\iff
(a\in X \text{ e } a\in Y).
$$

Graficamente, usando i diagrammi di Venn, $X\cap Y$ è la regione comune ai due insiemi.

### 1.3 Unione

L’[[Operazioni tra insiemi|unione]] di $X$ e $Y$ è l’insieme degli elementi che appartengono ad almeno uno dei due insiemi:

$$
X\cup Y=\{a\mid a\in X \text{ oppure } a\in Y\}.
$$

Pertanto:

$$
a\in X\cup Y
\iff
(a\in X \text{ oppure } a\in Y).
$$

Occhio: “oppure” va inteso in senso inclusivo, cioè un elemento può stare in $X$, in $Y$ o in entrambi.

### 1.4 Prodotto cartesiano

Il [[Prodotto cartesiano|prodotto cartesiano]] di due insiemi $X$ e $Y$ è l’insieme delle coppie ordinate $(x,y)$ in cui il primo elemento sta in $X$ e il secondo sta in $Y$:

$$
X\times Y
=
\{(x,y)\mid x\in X,\ y\in Y\}.
$$

L’ordine degli elementi è essenziale: in generale,

$$
(x,y)\neq (y,x).
$$

Il prodotto cartesiano non è necessariamente un insieme di punti geometrici, anche se lo si può rappresentare graficamente. Quando $X=Y=\mathbb{R}$, l’insieme

$$
\mathbb{R}\times\mathbb{R}
$$

può essere identificato con il piano cartesiano, cioè con $\mathbb{R}^2$:

$$
\mathbb{R}^2=\mathbb{R}\times\mathbb{R}.
$$

Gli elementi di $\mathbb{R}^2$ sono coppie di numeri reali:

$$
(x,y)\in\mathbb{R}^2.
$$

Analogamente,

$$
\mathbb{R}^3
=
\mathbb{R}\times\mathbb{R}\times\mathbb{R}
$$

è l’insieme delle terne $(x,y,z)$ di numeri reali.

Si può definire il prodotto cartesiano in modo iterato. Per esempio:

$$
(\mathbb{R}\times\mathbb{R})\times\mathbb{R}
$$

ha elementi della forma

$$
((x,y),z),
$$

cioè coppie il cui primo elemento è a sua volta una coppia. Formalmente questo insieme non coincide con $\mathbb{R}\times\mathbb{R}\times\mathbb{R}$, i cui elementi sono terne $(x,y,z)$, ma c’è una corrispondenza naturale tra le due descrizioni. La distinzione conta quando si lavora con definizioni precise.

### 1.5 Insiemi numerici

Tra gli insiemi numerici fondamentali si considerano:

- $\mathbb{N}$: insieme dei numeri naturali;
- $\mathbb{Z}$: insieme dei numeri interi;
- $\mathbb{Q}$: insieme dei numeri razionali;
- $\mathbb{R}$: insieme dei numeri reali;
- $\mathbb{C}$: insieme dei numeri complessi.

Attenzione: se lo zero stia o no in $\mathbb{N}$ dipende dalla convenzione. A volte si pone $\mathbb{N}=\{0,1,2,\ldots\}$, altre volte $\mathbb{N}=\{1,2,3,\ldots\}$.

### 1.6 Proprietà distributive tra unione e intersezione

Per tre insiemi $X$, $Y$ e $Z$ valgono le proprietà distributive:

$$
X\cap(Y\cup Z)
=
(X\cap Y)\cup(X\cap Z),
$$

e

$$
X\cup(Y\cap Z)
=
(X\cup Y)\cap(X\cup Z).
$$

Si possono controllare con i diagrammi di Venn, oppure in modo rigoroso con la strategia per dimostrare l’uguaglianza tra insiemi.

---

## 2. Come si dimostra l’uguaglianza tra insiemi

Per dimostrare che due insiemi $A$ e $B$ sono uguali si dimostrano le due [[Sottoinsieme|inclusioni]]:

$$
A\subseteq B
\qquad\text{e}\qquad
B\subseteq A.
$$

Qui $\subseteq$ è l’inclusione non stretta: $A\subseteq B$ vuol dire che ogni elemento di $A$ sta anche in $B$, senza escludere che $A=B$.

Formalmente:

$$
A\subseteq B
\iff
\forall x\,(x\in A\Rightarrow x\in B).
$$

### 2.1 Dimostrazione di un’inclusione

Per dimostrare $A\subseteq B$:

1. si prende un elemento generico $x\in A$;
2. si dimostra che $x\in B$.

Lo schema è quindi:

$$
x\in A
\Longrightarrow
x\in B.
$$

Per dimostrare l’uguaglianza $A=B$, si applica lo stesso procedimento in entrambe le direzioni:

$$
A\subseteq B
\quad\text{e}\quad
B\subseteq A.
$$

### 2.2 Esempio: proprietà distributiva

Consideriamo

$$
X\cap(Y\cup Z)
=
(X\cap Y)\cup(X\cap Z).
$$

Per la prima inclusione, prendiamo un elemento generico $a$ tale che

$$
a\in X\cap(Y\cup Z).
$$

Allora:

$$
a\in X
\quad\text{e}\quad
a\in Y\cup Z.
$$

Dalla seconda condizione segue che:

$$
a\in Y
\quad\text{oppure}\quad
a\in Z.
$$

Se $a\in Y$, allora $a\in X\cap Y$; se $a\in Z$, allora $a\in X\cap Z$. In entrambi i casi:

$$
a\in (X\cap Y)\cup(X\cap Z).
$$

Si ottiene dunque

$$
X\cap(Y\cup Z)
\subseteq
(X\cap Y)\cup(X\cap Z).
$$

Per l’inclusione opposta, si prende un elemento di $(X\cap Y)\cup(X\cap Z)$ e si considera separatamente il caso in cui appartenga a $X\cap Y$ oppure a $X\cap Z$. In entrambi i casi appartiene a $X$ e a $Y\cup Z$, quindi appartiene a $X\cap(Y\cup Z)$.

Questa tecnica tornerà spesso nel resto del corso.

---

## 3. Applicazioni tra insiemi

### 3.1 Definizione intuitiva

Un’[[Funzione|applicazione]], o funzione, da un insieme $X$ a un insieme $Y$ è una regola che associa a ogni elemento di $X$ uno e un solo elemento di $Y$.

Si scrive:

$$
f:X\longrightarrow Y.
$$

In questa notazione:

- $X$ è il **dominio**;
- $Y$ è il **codominio**;
- a ogni $x\in X$ viene associato un unico elemento $f(x)\in Y$.

La proprietà fondamentale è quindi:

$$
\forall x\in X\ \exists!\,y\in Y
\quad\text{tale che}\quad
y=f(x).
$$

Il simbolo $\exists!$ significa “esiste uno e un solo”.

Occhio: non basta dare la legge $x\mapsto f(x)$, bisogna precisare anche dominio e codominio. La stessa espressione può definire applicazioni diverse se cambiano dominio o codominio.

> [!example] Esempio
> La legge $x\mapsto x^2$ definisce due applicazioni diverse: $f:\mathbb{R}\to\mathbb{R}$ e $g:\mathbb{R}\to[0,+\infty)$. La seconda è suriettiva, la prima no (per esempio $-1$ non è mai raggiunto).

### 3.2 Definizione mediante il grafico

L’idea intuitiva di “regola” si formalizza usando il prodotto cartesiano.

Una relazione tra $X$ e $Y$ è un sottoinsieme

$$
\Gamma\subseteq X\times Y.
$$

La relazione $\Gamma$ rappresenta un’applicazione $f:X\to Y$ se per ogni $x\in X$ esiste uno e un solo $y\in Y$ tale che

$$
(x,y)\in\Gamma.
$$

In formula:

$$
\forall x\in X\ \exists!\,y\in Y
\quad\text{tale che}\quad
(x,y)\in\Gamma.
$$

In tal caso si definisce:

$$
f(x)=y,
$$

dove $y$ è l’unico elemento associato a $x$ dalla relazione $\Gamma$.

Quindi il grafico di una funzione è un sottoinsieme di $X\times Y$ che contiene esattamente una coppia con primo elemento $x$ per ogni $x\in X$.

Il disegno del prodotto cartesiano è solo un aiuto intuitivo: la definizione vera è insiemistica.

---

## 4. Iniettività, suriettività e biettività

### 4.1 Applicazioni iniettive

Un’applicazione $f:X\to Y$ è **[[Funzione biettiva|iniettiva]]** se elementi distinti del dominio hanno immagini distinte:

$$
x\neq x'
\Longrightarrow
f(x)\neq f(x').
$$

Una forma equivalente è:

$$
f(x)=f(x')
\Longrightarrow
x=x'.
$$

La negazione dell’iniettività è:

$$
\exists x,x'\in X,\quad x\neq x'
\quad\text{e}\quad
f(x)=f(x').
$$

Quindi $f$ non è iniettiva se esistono due elementi distinti del dominio mandati nello stesso elemento del codominio.

> [!example] Esempio
> $f:\mathbb{R}\to\mathbb{R}$, $f(x)=x^2$ non è iniettiva, perché $f(1)=f(-1)=1$. Invece $g:\mathbb{R}\to\mathbb{R}$, $g(x)=2x+1$ è iniettiva: da $2x+1=2x'+1$ segue $x=x'$.

### 4.2 Applicazioni suriettive

Un’applicazione $f:X\to Y$ è **suriettiva** se ogni elemento del codominio è immagine di almeno un elemento del dominio:

$$
\forall y\in Y\ \exists x\in X
\quad\text{tale che}\quad
f(x)=y.
$$

In altri termini:

$$
f(X)=Y.
$$

La suriettività riguarda il codominio: ogni elemento di $Y$ deve essere davvero raggiunto.

### 4.3 Applicazioni biettive

Un’applicazione è **biettiva** se è contemporaneamente iniettiva e suriettiva.

In tal caso ogni elemento del codominio è immagine di uno e un solo elemento del dominio.

Le applicazioni biettive sono anche dette corrispondenze biunivoche.

---

## 5. Composizione e applicazione identica

Date due applicazioni compatibili (il codominio della prima è il dominio della seconda):

$$
f:X\longrightarrow Y,
\qquad
g:Y\longrightarrow Z.
$$

la loro [[Composizione di funzioni|composizione]] è l’applicazione

$$
g\circ f:X\longrightarrow Z
$$

definita da

$$
(g\circ f)(x)=g(f(x)).
$$

Nella composizione si applica prima $f$ e poi $g$.

La composizione è associativa, quando le applicazioni coinvolte sono compatibili:

$$
h\circ(g\circ f)
=
(h\circ g)\circ f.
$$

### 5.1 Applicazione identica

L’identità di un insieme $X$ è l’applicazione

$$
\operatorname{id}_X:X\longrightarrow X
$$

definita da

$$
\operatorname{id}_X(x)=x
\qquad
\forall x\in X.
$$

Se $f:X\to Y$ è biettiva, allora esiste un’applicazione

$$
g:Y\longrightarrow X
$$

tale che

$$
g\circ f=\operatorname{id}_X
\qquad\text{e}\qquad
f\circ g=\operatorname{id}_Y.
$$

L’applicazione $g$ si chiama **applicazione [[Funzione inversa|inversa]]** di $f$ e si indica con $f^{-1}$.

### 5.2 Costruzione dell’inversa di una biezione

Supponiamo che $f:X\to Y$ sia biettiva. Per definire $g=f^{-1}$ bisogna specificare il valore di $g$ su ogni elemento $y\in Y$.

Poiché $f$ è suriettiva, per ogni $y\in Y$ esiste almeno un $x\in X$ tale che

$$
f(x)=y.
$$

Poiché $f$ è iniettiva, tale $x$ è unico. Si può quindi definire:

$$
g(y)=x,
$$

dove $x$ è l’unico elemento di $X$ tale che

$$
f(x)=y.
$$

Formalmente:

$$
g(y)=
\text{l’unico }x\in X\text{ tale che }f(x)=y.
$$

La suriettività garantisce che tale $x$ esista, l’iniettività che sia unico. Senza entrambe le proprietà non si potrebbe definire così una funzione inversa.

Una volta definita $g$, si verifica che:

$$
g(f(x))=x
\qquad
\forall x\in X,
$$

e

$$
f(g(y))=y
\qquad
\forall y\in Y.
$$

---

## 6. Il piano e i vettori geometrici

Il corso introduce gli spazi vettoriali come generalizzazione di oggetti geometrici e numerici che già conosciamo.

### 6.1 Punti del piano e coordinate

Fissata un’origine $O$ e due direzioni indipendenti, ogni punto $P$ del piano può essere identificato con una coppia di numeri reali $(x,y)$.

Nel riferimento cartesiano usuale si scelgono due versori ortogonali, spesso indicati con $\mathbf{e}_1$ e $\mathbf{e}_2$. Il vettore $\overrightarrow{OP}$ può essere scritto come

$$
\overrightarrow{OP}
=
x\mathbf{e}_1+y\mathbf{e}_2.
$$

I numeri $x$ e $y$ sono le coordinate di $P$, oppure le coordinate del vettore $\overrightarrow{OP}$ rispetto alla base scelta.

### 6.2 Vettori geometrici

Intuitivamente, un vettore geometrico è rappresentato da un segmento orientato. Due segmenti traslati l’uno rispetto all’altro rappresentano lo stesso vettore: contano direzione, verso e lunghezza, non il punto in cui il segmento è disegnato.

La somma di due vettori si costruisce mediante la regola del parallelogramma. Se si sommano i vettori $\mathbf{u}$ e $\mathbf{v}$, la loro somma è la diagonale del parallelogramma costruito sui due vettori:

$$
\mathbf{u}+\mathbf{v}.
$$

La commutatività della somma,

$$
\mathbf{u}+\mathbf{v}
=
\mathbf{v}+\mathbf{u},
$$

è evidente geometricamente perché il parallelogramma costruito non cambia scambiando i due lati.

### 6.3 Riferimenti non ortogonali

Non è necessario scegliere un sistema cartesiano ortogonale. Si possono scegliere due vettori $\mathbf{v}_1$ e $\mathbf{v}_2$ non allineati, anche non unitari e non ortogonali.

Ogni vettore del piano può essere scritto in modo unico nella forma

$$
\overrightarrow{OP}
=
x\mathbf{v}_1+y\mathbf{v}_2.
$$

La coppia $(x,y)$ viene chiamata coordinata del vettore rispetto al riferimento $(\mathbf{v}_1,\mathbf{v}_2)$.

La costruzione geometrica usa il parallelogramma: si scompone $\overrightarrow{OP}$ in una componente parallela a $\mathbf{v}_1$ e una componente parallela a $\mathbf{v}_2$.

Le coordinate dipendono dal riferimento scelto. Se si cambiano i vettori $\mathbf{v}_1$ e $\mathbf{v}_2$, lo stesso vettore può avere coefficienti differenti. L’unicità riguarda quindi le coordinate rispetto a un riferimento fissato.

### 6.4 Coordinate nello spazio

Nello spazio si scelgono tre vettori non complanari $\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3$. Essi costituiscono un riferimento, anche se non sono necessariamente ortogonali o unitari.

Ogni vettore dello spazio si scrive in modo unico come

$$
\mathbf{v}
=
x\mathbf{v}_1+y\mathbf{v}_2+z\mathbf{v}_3.
$$

La terna $(x,y,z)$ è la terna delle coordinate di $\mathbf{v}$ rispetto al riferimento scelto.

Nel caso cartesiano usuale si usano tre versori ortogonali, spesso indicati con $\mathbf{i},\mathbf{j},\mathbf{k}$ oppure con $\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3$.

La costruzione geometrica si può interpretare tramite proiezioni parallele. Per esempio, per determinare la componente lungo $\mathbf{v}_1$, si considera il piano parallelo al piano generato da $\mathbf{v}_2$ e $\mathbf{v}_3$ e passante per il vettore da scomporre. Le costruzioni diventano più complesse rispetto al caso ortogonale, ma il principio è lo stesso.

La proprietà fondamentale richiesta alle coordinate è:

> Ogni vettore deve avere un’unica terna di coordinate rispetto al riferimento fissato.

---

## 7. Somma e prodotto per scalare

Sia $\mathbf{v}$ un vettore scritto rispetto a una base $\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3$ come

$$
\mathbf{v}
=
x\mathbf{v}_1+y\mathbf{v}_2+z\mathbf{v}_3,
$$

e sia $\mathbf{w}$ un altro vettore:

$$
\mathbf{w}
=
x'\mathbf{v}_1+y'\mathbf{v}_2+z'\mathbf{v}_3.
$$

### 7.1 Coordinate della somma

La somma è:

$$
\begin{aligned}
\mathbf{v}+\mathbf{w}
&=
(x\mathbf{v}_1+y\mathbf{v}_2+z\mathbf{v}_3)
+
(x'\mathbf{v}_1+y'\mathbf{v}_2+z'\mathbf{v}_3)\\
&=
(x+x')\mathbf{v}_1
+
(y+y')\mathbf{v}_2
+
(z+z')\mathbf{v}_3.
\end{aligned}
$$

Pertanto le coordinate della somma si ottengono sommando componente per componente:

$$
[\mathbf{v}+\mathbf{w}]
=
(x+x',\,y+y',\,z+z').
$$

Questa proprietà dipende dalle proprietà della somma di vettori, in particolare dalla commutatività e dall’associatività.

### 7.2 Prodotto esterno

Il prodotto di uno scalare per un vettore è un’operazione diversa dalla somma vettoriale: è un’applicazione

$$
\mathbb{R}\times V\longrightarrow V,
$$

che associa a una coppia $(\alpha,\mathbf{v})$ un vettore indicato con

$$
\alpha\mathbf{v}.
$$

Nel caso dei vettori geometrici, $\alpha\mathbf{v}$ ha:

- la stessa direzione di $\mathbf{v}$, se $\alpha\neq 0$;
- verso concorde con quello di $\mathbf{v}$ se $\alpha>0$;
- verso opposto se $\alpha<0$;
- lunghezza moltiplicata per $|\alpha|$.

Il significato concreto dell’operazione dipende dal contesto, ma gli assiomi astratti saranno sempre gli stessi.

Se

$$
\mathbf{v}
=
x\mathbf{v}_1+y\mathbf{v}_2+z\mathbf{v}_3,
$$

allora

$$
\alpha\mathbf{v}
=
(\alpha x)\mathbf{v}_1
+
(\alpha y)\mathbf{v}_2
+
(\alpha z)\mathbf{v}_3.
$$

Quindi le coordinate del prodotto per scalare sono le coordinate del vettore moltiplicate tutte per lo stesso scalare:

$$
[\alpha\mathbf{v}]
=
(\alpha x,\alpha y,\alpha z).
$$

### 7.3 Proprietà del prodotto per scalare

Per scalari $\alpha,\beta\in\mathbb{R}$ e vettori $\mathbf{u},\mathbf{v}\in V$, valgono le proprietà:

#### Distributività rispetto alla somma di vettori

$$
\alpha(\mathbf{u}+\mathbf{v})
=
\alpha\mathbf{u}+\alpha\mathbf{v}.
$$

#### Distributività rispetto alla somma di scalari

$$
(\alpha+\beta)\mathbf{v}
=
\alpha\mathbf{v}+\beta\mathbf{v}.
$$

#### Compatibilità con il prodotto degli scalari

$$
\alpha(\beta\mathbf{v})
=
(\alpha\beta)\mathbf{v}.
$$

#### Azione dell’unità

$$
1\mathbf{v}=\mathbf{v}.
$$

Queste proprietà geometriche di somma e prodotto per scalare sono all’origine degli assiomi degli spazi vettoriali.

---

## 8. Operazioni e campi

### 8.1 Operazioni interne

Un’operazione interna su un insieme $K$ è un’applicazione

$$
K\times K\longrightarrow K.
$$

Essa prende due elementi di $K$ e restituisce ancora un elemento di $K$.

La somma e il prodotto usuali sui numeri reali sono esempi di operazioni interne:

$$
+:\mathbb{R}\times\mathbb{R}\longrightarrow\mathbb{R},
$$

$$
\cdot:\mathbb{R}\times\mathbb{R}\longrightarrow\mathbb{R}.
$$

Il prodotto per scalare, invece, non è un’operazione interna sullo spazio dei vettori: è un’applicazione

$$
K\times V\longrightarrow V,
$$

dove il primo elemento è uno scalare e il secondo è un vettore.

### 8.2 Campi

Un [[Campo|campo]] è un insieme $K$ dotato di due operazioni interne, somma e prodotto, che soddisfano determinati assiomi.

Gli esempi principali sono:

$$
\mathbb{Q},\qquad \mathbb{R},\qquad \mathbb{C}.
$$

Lo scopo della definizione assiomatica è isolare le proprietà essenziali dei numeri, senza dipendere dalla costruzione particolare di interi, razionali o reali.

#### Assiomi della somma

La somma deve soddisfare:

1. **Associatività**
   $$
   (x+y)+z=x+(y+z).
   $$

2. **Commutatività**
   $$
   x+y=y+x.
   $$

3. **Esistenza dell’elemento neutro**
   
   Esiste un elemento $0\in K$ tale che
   $$
   x+0=0+x=x
   \qquad
   \forall x\in K.
   $$

4. **Esistenza dell’opposto**
   
   Per ogni $x\in K$ esiste un elemento $-x\in K$ tale che
   $$
   x+(-x)=(-x)+x=0.
   $$

Di conseguenza $(K,+)$ è un [[Gruppo|gruppo abeliano]], cioè un gruppo commutativo.

#### Assiomi del prodotto

Il prodotto deve soddisfare:

1. **Associatività**
   $$
   (xy)z=x(yz).
   $$

2. **Commutatività**
   $$
   xy=yx.
   $$

3. **Esistenza dell’elemento neutro**
   
   Esiste un elemento $1\in K$ tale che
   $$
   1x=x1=x
   \qquad
   \forall x\in K.
   $$

4. **Esistenza dell’inverso per gli elementi non nulli**
   
   Per ogni $x\in K$ con $x\neq 0$ esiste $x^{-1}\in K$ tale che
   $$
   xx^{-1}=x^{-1}x=1.
   $$

La restrizione $x\neq 0$ serve: lo zero non è invertibile. Gli elementi non nulli di un campo formano un gruppo abeliano rispetto al prodotto.

#### Proprietà distributive

Il prodotto deve essere distributivo rispetto alla somma:

$$
x(y+z)=xy+xz,
$$

e

$$
(x+y)z=xz+yz.
$$

Dato che il prodotto è commutativo le due proprietà sono equivalenti, ma nella formulazione completa si enunciano entrambe.

In sintesi, un campo è un insieme con due operazioni, somma e prodotto, tali che:

- la somma renda l’insieme un gruppo abeliano;
- gli elementi non nulli rendano l’insieme un gruppo abeliano rispetto al prodotto;
- il prodotto sia distributivo rispetto alla somma.

### 8.3 Il campo con due elementi

Esiste un campo con soli due elementi:

$$
\mathbb{F}_2=\{0,1\}.
$$

Le operazioni sono forzate dagli assiomi.

Per la somma:

$$
0+0=0,
\qquad
0+1=1,
\qquad
1+0=1.
$$

Poiché ogni elemento deve avere un opposto e l’opposto di $0$ è $0$, l’opposto di $1$ deve essere $1$ stesso:

$$
1+1=0.
$$

Per il prodotto:

$$
0\cdot 0=0,
\qquad
0\cdot 1=1\cdot 0=0,
\qquad
1\cdot 1=1.
$$

Si può verificare direttamente che queste operazioni soddisfano gli assiomi di campo.

Più in generale, per ogni numero primo $p$ esiste un campo con $p$ elementi, indicato generalmente con $\mathbb{F}_p$.

---

## 9. Spazi vettoriali

### 9.1 Idea generale

Uno [[Spazio vettoriale|spazio vettoriale]] è una generalizzazione astratta dell’insieme dei vettori geometrici del piano o dello spazio.

Si parte da:

- un campo $K$, i cui elementi sono chiamati **scalari**;
- un insieme $V$, i cui elementi sono chiamati **vettori**;
- un’operazione di somma tra vettori;
- un prodotto esterno tra scalari e vettori.

Le operazioni sono:

$$
+:V\times V\longrightarrow V,
$$

e

$$
\cdot:K\times V\longrightarrow V.
$$

Il prodotto esterno viene scritto come

$$
(\alpha,\mathbf{v})\longmapsto \alpha\mathbf{v}.
$$

### 9.2 Assiomi di spazio vettoriale

Un insieme $V$ con queste operazioni è uno spazio vettoriale su $K$ se valgono le proprietà seguenti.

#### Proprietà della somma

Per ogni $\mathbf{u},\mathbf{v},\mathbf{w}\in V$:

1. **Associatività**
   $$
   (\mathbf{u}+\mathbf{v})+\mathbf{w}
   =
   \mathbf{u}+(\mathbf{v}+\mathbf{w}).
   $$

2. **Commutatività**
   $$
   \mathbf{u}+\mathbf{v}
   =
   \mathbf{v}+\mathbf{u}.
   $$

3. **Esistenza del vettore nullo**
   
   Esiste $\mathbf{0}\in V$ tale che
   $$
   \mathbf{v}+\mathbf{0}
   =
   \mathbf{0}+\mathbf{v}
   =
   \mathbf{v}.
   $$

4. **Esistenza dell’opposto**
   
   Per ogni $\mathbf{v}\in V$ esiste $-\mathbf{v}\in V$ tale che
   $$
   \mathbf{v}+(-\mathbf{v})=\mathbf{0}.
   $$

Quindi $(V,+)$ è un gruppo abeliano.

#### Proprietà del prodotto esterno

Per ogni $\alpha,\beta\in K$ e $\mathbf{u},\mathbf{v}\in V$:

5. **Distributività rispetto alla somma di vettori**
   $$
   \alpha(\mathbf{u}+\mathbf{v})
   =
   \alpha\mathbf{u}+\alpha\mathbf{v}.
   $$

6. **Distributività rispetto alla somma di scalari**
   $$
   (\alpha+\beta)\mathbf{v}
   =
   \alpha\mathbf{v}+\beta\mathbf{v}.
   $$

7. **Compatibilità con il prodotto nel campo**
   $$
   (\alpha\beta)\mathbf{v}
   =
   \alpha(\beta\mathbf{v}).
   $$

8. **Azione dell’unità del campo**
   $$
   1\mathbf{v}=\mathbf{v}.
   $$

Questi assiomi formalizzano proprietà che abbiamo già visto per i vettori geometrici.

> [!example] Esempio
> $\mathbb{R}^2$ con somma e prodotto per scalare fatti componente per componente, $(x,y)+(x',y')=(x+x',y+y')$ e $\alpha(x,y)=(\alpha x,\alpha y)$, è uno spazio vettoriale su $\mathbb{R}$: gli otto assiomi si riducono alle proprietà dei numeri reali, applicate a ciascuna coordinata.

---

## 10. Unicità degli elementi neutri e degli inversi

Tra gli esercizi proposti ci sono alcune dimostrazioni fondamentali sugli assiomi di gruppo e di campo.

### 10.1 Unicità dell’elemento neutro per la somma

Supponiamo che $0$ e $0'$ siano entrambi elementi neutri rispetto alla somma. Ciò significa che per ogni $x$:

$$
x+0=x
\qquad\text{e}\qquad
x+0'=x.
$$

In particolare, applicando le proprietà ai due elementi neutri:

$$
0'=0'+0
$$

perché $0$ è neutro, mentre

$$
0'+0=0
$$

perché $0'$ è neutro.

Pertanto:

$$
0'=0'+0=0.
$$

Quindi l’elemento neutro rispetto alla somma è unico.

La struttura è generale: per dimostrare l’unicità di un oggetto caratterizzato da una proprietà, si suppone che ce ne siano due e si mostra che coincidono.

### 10.2 Unicità dell’opposto

Supponiamo che $y$ e $z$ siano entrambi opposti di $x$. Allora:

$$
x+y=0,
\qquad
x+z=0.
$$

Si può dimostrare che $y=z$ usando l’elemento neutro, l’associatività, la commutatività e il fatto che $y$ e $z$ annullano $x$:

$$
\begin{aligned}
y
&=y+0\\
&=y+(x+z)\\
&=(y+x)+z\\
&=(x+y)+z\\
&=0+z\\
&=z.
\end{aligned}
$$

Quindi l’opposto di un elemento è unico.

### 10.3 Unicità dell’inverso moltiplicativo

Analogamente, se $y$ e $z$ sono entrambi inversi di $x\neq 0$, allora:

$$
xy=1,
\qquad
xz=1.
$$

Si dimostra:

$$
\begin{aligned}
y
&=y\cdot 1\\
&=y\cdot(xz)\\
&=(yx)\cdot z\\
&=1\cdot z\\
&=z.
\end{aligned}
$$

Quindi l’inverso moltiplicativo di un elemento non nullo è unico.

---

## 11. Collegamento con gli argomenti successivi

Gli spazi vettoriali sono il primo grande oggetto astratto del corso. Dopo si studieranno soprattutto:

- applicazioni lineari tra spazi vettoriali;
- prodotti scalari;
- interpretazioni geometriche degli spazi vettoriali;
- coordinate e cambiamenti di base;
- applicazioni geometriche, tra cui la classificazione delle coniche.

Le coniche sono curve descritte da equazioni di secondo grado. Uno degli obiettivi geometrici sarà riconoscere, dall’equazione, se una curva è una parabola, un’ellisse, un’iperbole o un’altra conica.

L’idea centrale del corso è passare da esempi concreti — punti, vettori geometrici, coordinate, numeri — a definizioni astratte basate su proprietà e assiomi. L’astrazione non elimina la geometria: anche quando il linguaggio diventa algebrico, conviene tenere a mente gli esempi geometrici che hanno motivato le definizioni.
