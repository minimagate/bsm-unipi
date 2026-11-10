---
type: lecture-note
course: Aritmetica
date: '2026-09-30'
title: Successioni ricorrenti e formule combinatorie
source_transcript: _transcripts/Aritmetica/2026-09-30 - Successioni ricorrenti e formule combinatorie.md
source_hash: sha256:532ba34507db258a4a087cabe38fa06c5b8a88d0b6679626e1e4302ebe381328
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-30T10:52:54.176Z'
vault_path: Notes/Aritmetica/Lectures/2026-09-30 - Successioni ricorrenti e formule combinatorie.md
vault_hash: 7e6c8fc114fa2251889ce86f05bcff2e7296cc8aea6fd3ccb6da03cc32ec82df
---

## 1. Successioni definite per ricorrenza

Una [[Successione|successione]] a valori in un insieme $X$ è una funzione

$$
a:\mathbb{N}\longrightarrow X,
$$

che a ogni numero naturale $n$ associa un elemento $a_n$ di $X$. Di solito si considerano successioni a valori reali o complessi.

Una successione è definita **[[Successione per ricorrenza|per ricorrenza]]** quando i suoi termini si ricavano da alcuni termini iniziali tramite una relazione ricorrente.

L’esempio di partenza è la successione definita da

$$
a_{n+1}=3a_n-2a_{n-1},
$$

con le condizioni iniziali

$$
a_0=0,\qquad a_1=1.
$$

La ricorrenza permette di calcolare tutti i termini, uno dopo l’altro:

- da $a_0$ e $a_1$ si calcola $a_2$;
- da $a_1$ e $a_2$ si calcola $a_3$;
- e così via.

Con condizioni iniziali diverse, per esempio $a_0=5$ e $a_1=7$, la stessa ricorrenza dà un’altra successione.

Ma il nostro obiettivo non è calcolare i termini uno alla volta: vogliamo una **formula esplicita** per $a_n$.

> [!example] Esempio
> Con $a_0=0$ e $a_1=1$: $a_2=3\cdot 1-2\cdot 0=3$, $a_3=3\cdot 3-2\cdot 1=7$, $a_4=3\cdot 7-2\cdot 3=15$. I termini $0,1,3,7,15$ fanno pensare a $2^n-1$: la formula verrà fuori nei paragrafi successivi.

---

## 2. Linearità dell’equazione di ricorrenza

La ricorrenza

$$
a_{n+1}=3a_n-2a_{n-1}
$$

è lineare e omogenea. Significa che, se due successioni la soddisfano, la soddisfa anche ogni loro combinazione lineare.

Siano $(b_n)$ e $(c_n)$ due soluzioni, cioè

$$
b_{n+1}=3b_n-2b_{n-1}
$$

e

$$
c_{n+1}=3c_n-2c_{n-1}.
$$

Per ogni $x,y\in\mathbb{C}$ consideriamo la successione

$$
d_n=xb_n+yc_n.
$$

Allora

$$
\begin{aligned}
d_{n+1}
&=xb_{n+1}+yc_{n+1}\\
&=x(3b_n-2b_{n-1})+y(3c_n-2c_{n-1})\\
&=3(xb_n+yc_n)-2(xb_{n-1}+yc_{n-1})\\
&=3d_n-2d_{n-1}.
\end{aligned}
$$

Quindi $(d_n)$ è ancora una soluzione.

In altre parole, l’insieme delle soluzioni dell’equazione di ricorrenza è uno [[Spazio vettoriale|spazio vettoriale]] sui reali o, più comodamente, sui [[Numero complesso|complessi]]. Usare i complessi è utile perché permette di trattare in modo sistematico le radici del polinomio caratteristico.

Siccome la ricorrenza coinvolge due termini precedenti, ci aspettiamo che lo spazio delle soluzioni abbia dimensione $2$: per individuare una soluzione bastano due valori iniziali, per esempio $a_0$ e $a_1$.

> [!note]
> Il linguaggio degli spazi vettoriali e della dimensione è solo un’interpretazione concettuale. Per risolvere l’esempio basta il calcolo diretto dei paragrafi successivi.

---

## 3. Metodo della soluzione esponenziale

L’idea generale per una ricorrenza lineare omogenea è cercare soluzioni della forma

$$
b_n=\lambda^n,
$$

dove $\lambda$ è un numero da determinare.

Sostituendo nella ricorrenza:

$$
\lambda^{n+1}=3\lambda^n-2\lambda^{n-1}.
$$

Se $\lambda\neq 0$, si divide per $\lambda^{n-1}$ e si ottiene

$$
\lambda^2=3\lambda-2,
$$

cioè

$$
\lambda^2-3\lambda+2=0.
$$

Il problema di trovare una successione si riduce così a risolvere una sola equazione di secondo grado.

Fattorizzando:

$$
\lambda^2-3\lambda+2=(\lambda-1)(\lambda-2),
$$

troviamo due radici distinte

$$
\lambda_1=1,\qquad \lambda_2=2.
$$

Di conseguenza, le successioni

$$
1^n=1
\qquad\text{e}\qquad
2^n
$$

sono entrambe soluzioni della ricorrenza.

Per esempio, per $2^n$ si verifica direttamente che

$$
\begin{aligned}
3\cdot 2^n-2\cdot 2^{n-1}
&=3\cdot 2^n-2^n\\
&=2\cdot 2^n\\
&=2^{n+1}.
\end{aligned}
$$

Poiché le due radici sono distinte, tutte le soluzioni della ricorrenza omogenea sono combinazioni lineari delle due soluzioni corrispondenti:

$$
a_n=x2^n+y1^n=x2^n+y,
$$

dove $x,y$ sono costanti.

In generale, per una ricorrenza lineare omogenea del secondo ordine con due radici distinte $\lambda_1,\lambda_2$, la soluzione generale è

$$
a_n=x\lambda_1^n+y\lambda_2^n.
$$

Il caso di radici coincidenti richiede una forma diversa, di solito con un fattore $n$; la lezione non lo sviluppa.

---

## 4. Determinazione delle costanti tramite le condizioni iniziali

Per la successione dell’esempio abbiamo trovato

$$
a_n=x2^n+y.
$$

Imponiamo le condizioni iniziali.

Da $a_0=0$ si ottiene

$$
0=x2^0+y=x+y.
$$

Da $a_1=1$ si ottiene

$$
1=x2^1+y=2x+y.
$$

Il sistema è

$$
\begin{cases}
x+y=0,\\
2x+y=1.
\end{cases}
$$

Dalla prima equazione $y=-x$. Sostituendo nella seconda:

$$
2x-x=1,
$$

da cui

$$
x=1,\qquad y=-1.
$$

La formula esplicita è quindi

$$
\boxed{a_n=2^n-1}.
$$

Verifichiamo direttamente la ricorrenza:

$$
\begin{aligned}
3a_n-2a_{n-1}
&=3(2^n-1)-2(2^{n-1}-1)\\
&=3\cdot 2^n-3-2^n+2\\
&=2^{n+1}-1\\
&=a_{n+1}.
\end{aligned}
$$

E le condizioni iniziali:

$$
a_0=2^0-1=0,
\qquad
a_1=2^1-1=1.
$$

La formula soddisfa sia la ricorrenza sia le condizioni iniziali.

---

## 5. Collegamento con la successione di Fibonacci

Lo stesso procedimento funziona per la [[Successione di Fibonacci|successione di Fibonacci]], definita da

$$
F_{n+1}=F_n+F_{n-1},
$$

con le solite condizioni iniziali

$$
F_0=0,\qquad F_1=1.
$$

Cerchiamo una soluzione del tipo $F_n=\lambda^n$:

$$
\lambda^{n+1}=\lambda^n+\lambda^{n-1}.
$$

Dividendo per $\lambda^{n-1}$:

$$
\lambda^2=\lambda+1,
$$

cioè

$$
\lambda^2-\lambda-1=0.
$$

Le due radici sono

$$
\varphi=\frac{1+\sqrt{5}}{2},
\qquad
\psi=\frac{1-\sqrt{5}}{2}.
$$

La formula di Fibonacci si ottiene come combinazione lineare di $\varphi^n$ e $\psi^n$:

$$
F_n=\frac{\varphi^n-\psi^n}{\sqrt{5}}.
$$

Il punto metodologico: una ricorrenza, che è una famiglia infinita di equazioni, si trasforma in una sola equazione algebrica, il polinomio caratteristico, che sappiamo risolvere.

---

## 6. Coefficienti binomiali e formula del binomio di Newton

### 6.1 Definizione del coefficiente binomiale

Per $0\leq k\leq n$, il [[Coefficiente binomiale|coefficiente binomiale]] è definito da

$$
\binom{n}{k}
=
\frac{n!}{k!(n-k)!}.
$$

Rappresenta il numero di modi di scegliere $k$ elementi da un insieme di $n$ elementi:

$$
\binom{n}{k}
=
\left|\left\{S\subseteq \{1,\dots,n\}: |S|=k\right\}\right|.
$$

In particolare,

$$
\binom{n}{0}=1,
\qquad
\binom{n}{n}=1.
$$

La prima uguaglianza corrisponde all’unico modo di scegliere zero elementi, cioè non scegliere niente; la seconda all’unico modo di sceglierli tutti.

Conviene estendere la convenzione ponendo

$$
\binom{n}{k}=0
\qquad\text{se }k<0\text{ oppure }k>n.
$$

Così le formule diventano più naturali e si possono scrivere somme con gli stessi estremi senza trattare a parte i termini ai bordi.

---

### 6.2 Enunciato del binomio di Newton

Per ogni $n\in\mathbb{N}$ vale la formula del [[Binomio di Newton|binomio di Newton]]

$$
\boxed{
(a+b)^n
=
\sum_{k=0}^{n}
\binom{n}{k}a^k b^{n-k}
}.
$$

I primi casi sono già noti.

Per $n=2$:

$$
(a+b)^2=a^2+2ab+b^2.
$$

Infatti,

$$
\binom{2}{0}=1,\qquad
\binom{2}{1}=2,\qquad
\binom{2}{2}=1.
$$

Per $n=3$:

$$
(a+b)^3=a^3+3a^2b+3ab^2+b^3.
$$

I coefficienti sono la seconda e la terza riga del triangolo di Pascal.

---

### 6.3 Interpretazione combinatoria

Per sviluppare

$$
(a+b)^n
$$

si moltiplicano tra loro $n$ parentesi:

$$
(a+b)(a+b)\cdots(a+b).
$$

Da ogni parentesi si sceglie o il termine $a$, o il termine $b$.

Per ottenere il monomio

$$
a^k b^{n-k},
$$

bisogna scegliere $a$ esattamente $k$ volte e $b$ nelle altre $n-k$ parentesi.

I modi di scegliere quali sono le $k$ parentesi da cui prendere $a$ sono

$$
\binom{n}{k}.
$$

Quindi il coefficiente di $a^k b^{n-k}$ è proprio $\binom{n}{k}$.

Ecco la ragione combinatoria della formula:

$$
(a+b)^n
=
\sum_{k=0}^n
\binom{n}{k}a^k b^{n-k}.
$$

---

### 6.4 Dimostrazione per induzione

La formula si dimostra per induzione su $n$.

#### Caso base

Per $n=0$:

$$
(a+b)^0=1.
$$

D’altra parte,

$$
\sum_{k=0}^{0}\binom{0}{k}a^k b^{0-k}
=
\binom{0}{0}a^0b^0
=
1.
$$

Quindi la formula è vera per $n=0$.

#### Passo induttivo

Supponiamo vera la formula per un certo $n$:

$$
(a+b)^n
=
\sum_{i=0}^{n}
\binom{n}{i}a^i b^{n-i}.
$$

Moltiplichiamo per $a+b$:

$$
\begin{aligned}
(a+b)^{n+1}
&=(a+b)(a+b)^n\\
&=(a+b)\sum_{i=0}^{n}
\binom{n}{i}a^i b^{n-i}.
\end{aligned}
$$

Distribuendo:

$$
(a+b)^{n+1}
=
\sum_{i=0}^{n}
\binom{n}{i}a^{i+1}b^{n-i}
+
\sum_{i=0}^{n}
\binom{n}{i}a^i b^{n-i+1}.
$$

Le due somme non hanno ancora i monomi scritti con gli stessi indici. Nella prima si pone

$$
j=i+1,
$$

nella seconda si pone

$$
j=i.
$$

Nella prima somma $i$ va da $0$ a $n$, quindi $j$ va da $1$ a $n+1$:

$$
\sum_{i=0}^{n}
\binom{n}{i}a^{i+1}b^{n-i}
=
\sum_{j=1}^{n+1}
\binom{n}{j-1}a^j b^{n+1-j}.
$$

Nella seconda somma:

$$
\sum_{i=0}^{n}
\binom{n}{i}a^i b^{n-i+1}
=
\sum_{j=0}^{n}
\binom{n}{j}a^j b^{n+1-j}.
$$

Quindi

$$
\begin{aligned}
(a+b)^{n+1}
&=
\sum_{j=1}^{n+1}
\binom{n}{j-1}a^j b^{n+1-j}
+
\sum_{j=0}^{n}
\binom{n}{j}a^j b^{n+1-j}.
\end{aligned}
$$

Grazie alla convenzione $\binom{n}{k}=0$ fuori dall’intervallo $0\leq k\leq n$, entrambe le somme si possono estendere da $j=0$ a $j=n+1$:

$$
(a+b)^{n+1}
=
\sum_{j=0}^{n+1}
\left[
\binom{n}{j-1}+\binom{n}{j}
\right]
a^j b^{n+1-j}.
$$

Ora si usa l’identità di Pascal:

$$
\binom{n}{j-1}+\binom{n}{j}
=
\binom{n+1}{j}.
$$

Quindi

$$
(a+b)^{n+1}
=
\sum_{j=0}^{n+1}
\binom{n+1}{j}a^j b^{n+1-j}.
$$

Il passo induttivo è concluso, e con lui la dimostrazione.

#### Dimostrazione dell’identità di Pascal

L’identità

$$
\binom{n}{j-1}+\binom{n}{j}
=
\binom{n+1}{j}
$$

si verifica algebricamente:

$$
\begin{aligned}
\binom{n}{j-1}+\binom{n}{j}
&=
\frac{n!}{(j-1)!(n-j+1)!}
+
\frac{n!}{j!(n-j)!}\\
&=
\frac{n!j}{j!(n-j+1)!}
+
\frac{n!(n-j+1)}{j!(n-j+1)!}\\
&=
\frac{n!(n+1)}{j!(n-j+1)!}\\
&=
\frac{(n+1)!}{j!((n+1)-j)!}\\
&=
\binom{n+1}{j}.
\end{aligned}
$$

L’identità ha anche un’interpretazione combinatoria: per scegliere $j$ elementi da un insieme di $n+1$ elementi, si può distinguere se un elemento fissato sta o no nel sottoinsieme scelto.

---

### 6.5 Attenzione agli indici nelle somme

Quando si cambiano gli indici di sommatoria, ricordiamo che l’indice è una variabile locale: il suo nome non ha significato fuori dalla somma.

Per esempio, nelle due somme

$$
\sum_{i=0}^{n}\binom{n}{i}a^{i+1}b^{n-i}
\qquad\text{e}\qquad
\sum_{i=0}^{n}\binom{n}{i}a^i b^{n-i+1}
$$

la variabile $i$ è indipendente nelle due somme. Si può rinominare l’indice in una delle due, purché si modifichino coerentemente tutti i termini e gli estremi.

Se il cambio di indice non è chiaro, conviene controllare un caso piccolo, per esempio $n=2$, scrivendo esplicitamente tutti i termini.

---

## 7. Numero dei sottoinsiemi di un insieme finito

Sia $X$ un insieme finito con $n$ elementi. L’insieme delle parti $\mathcal{P}(X)$ è l’insieme di tutti i sottoinsiemi di $X$.

La cardinalità di $\mathcal{P}(X)$ è

$$
\boxed{|\mathcal{P}(X)|=2^n}.
$$

### 7.1 Dimostrazione tramite coefficienti binomiali

Un sottoinsieme di $X$ può avere cardinalità $k$, con $0\leq k\leq n$.

I sottoinsiemi con esattamente $k$ elementi sono

$$
\binom{n}{k}.
$$

Sottoinsiemi di cardinalità diversa non si sovrappongono, quindi

$$
|\mathcal{P}(X)|
=
\sum_{k=0}^{n}\binom{n}{k}.
$$

Applichiamo il binomio di Newton con $a=b=1$:

$$
(1+1)^n
=
\sum_{k=0}^{n}
\binom{n}{k}1^k1^{n-k}.
$$

Ogni monomio vale $1$, quindi:

$$
2^n
=
\sum_{k=0}^{n}\binom{n}{k}.
$$

Dunque

$$
|\mathcal{P}(X)|=2^n.
$$

Questa formula equivale al fatto che ogni elemento di $X$ può essere scelto oppure no: per ciascuno degli $n$ elementi ci sono due possibilità indipendenti.

---

### 7.2 Sottoinsiemi di cardinalità pari e dispari

Sia $X$ un insieme con $n$ elementi. Confrontiamo il numero di sottoinsiemi di cardinalità pari e quello di cardinalità dispari.

Il numero totale è

$$
\sum_{\substack{k=0\\ k\text{ pari}}}^{n}\binom{n}{k}
+
\sum_{\substack{k=0\\ k\text{ dispari}}}^{n}\binom{n}{k}
=
2^n.
$$

Per confrontare le due quantità si usa il binomio di Newton con $a=1$ e $b=-1$:

$$
(1-1)^n
=
\sum_{k=0}^{n}\binom{n}{k}(-1)^k.
$$

Per $n>0$ il membro sinistro è zero:

$$
0=
\sum_{k\text{ pari}}\binom{n}{k}
-
\sum_{k\text{ dispari}}\binom{n}{k}.
$$

Quindi

$$
\sum_{k\text{ pari}}\binom{n}{k}
=
\sum_{k\text{ dispari}}\binom{n}{k}.
$$

Unendo questa uguaglianza alla somma totale $2^n$, ciascuna delle due quantità vale

$$
2^{n-1}.
$$

Dunque, se $n>0$, metà dei sottoinsiemi ha cardinalità pari e metà dispari:

$$
\boxed{
\#\{\text{sottoinsiemi pari}\}
=
\#\{\text{sottoinsiemi dispari}\}
=
2^{n-1}
}.
$$

Un’altra dimostrazione costruisce una corrispondenza tra sottoinsiemi pari e dispari: fissato $x\in X$, si associa a ogni sottoinsieme $A$ il sottoinsieme

$$
A\triangle\{x\},
$$

dove $\triangle$ indica la differenza simmetrica. L’operazione inserisce $x$ se non appartiene ad $A$ e lo toglie se appartiene ad $A$, cambiando così la parità della cardinalità.

---

## 8. Funzioni caratteristiche

Sia $X$ un insieme e sia $A\subseteq X$. La **[[Funzione caratteristica|funzione caratteristica]]** di $A$ è la funzione

$$
\mathbf{1}_A:X\longrightarrow\{0,1\}
$$

definita da

$$
\mathbf{1}_A(x)=
\begin{cases}
1,&x\in A,\\
0,&x\notin A.
\end{cases}
$$

La funzione caratteristica traduce una proprietà insiemistica in una funzione numerica.

Se $X$ è finito, la cardinalità di $A$ si ottiene sommando la funzione caratteristica su tutti gli elementi di $X$:

$$
|A|
=
\sum_{x\in X}\mathbf{1}_A(x).
$$

Infatti ogni elemento di $A$ contribuisce con $1$, mentre ogni elemento fuori da $A$ contribuisce con $0$.

---

### 8.1 Intersezioni

Per due sottoinsiemi $A,B\subseteq X$ vale

$$
\mathbf{1}_{A\cap B}(x)
=
\mathbf{1}_A(x)\mathbf{1}_B(x).
$$

Infatti:

- se $x\in A\cap B$, entrambi i fattori valgono $1$, quindi il prodotto vale $1$;
- se $x$ non appartiene a uno dei due insiemi, almeno un fattore vale $0$, quindi il prodotto vale $0$.

Di conseguenza,

$$
|A\cap B|
=
\sum_{x\in X}\mathbf{1}_A(x)\mathbf{1}_B(x).
$$

Più in generale:

$$
\mathbf{1}_{A_1\cap\cdots\cap A_k}(x)
=
\prod_{i=1}^{k}\mathbf{1}_{A_i}(x).
$$

---

### 8.2 Unioni

Per l’unione di due insiemi vale

$$
\mathbf{1}_{A\cup B}
=
\mathbf{1}_A+\mathbf{1}_B-\mathbf{1}_{A\cap B}.
$$

Verifica punto per punto:

- se $x$ appartiene solo ad $A$, il membro destro vale $1+0-0=1$;
- se $x$ appartiene solo a $B$, vale $0+1-0=1$;
- se $x$ appartiene a entrambi, vale $1+1-1=1$;
- se non appartiene a nessuno, vale $0$.

Sommando su $x\in X$ si ottiene la formula di inclusione-esclusione per due insiemi:

$$
\boxed{
|A\cup B|
=
|A|+|B|-|A\cap B|
}.
$$

Si sottrae $|A\cap B|$ perché gli elementi comuni erano stati contati due volte.

---

## 9. Principio di inclusione-esclusione

### 9.1 Formula generale

Siano $A_1,\dots,A_n$ sottoinsiemi di un insieme finito. Secondo il [[Principio di inclusione-esclusione|principio di inclusione-esclusione]], la cardinalità della loro unione è

$$
\boxed{
\left|\bigcup_{i=1}^{n}A_i\right|
=
\sum_{i=1}^{n}|A_i|
-
\sum_{1\leq i<j\leq n}|A_i\cap A_j|
+
\sum_{1\leq i<j<k\leq n}|A_i\cap A_j\cap A_k|
-\cdots
+(-1)^{n+1}
\left|A_1\cap\cdots\cap A_n\right|
}.
$$

In forma compatta:

$$
\left|\bigcup_{i=1}^{n}A_i\right|
=
\sum_{\varnothing\neq I\subseteq\{1,\dots,n\}}
(-1)^{|I|+1}
\left|\bigcap_{i\in I}A_i\right|.
$$

Qui $I$ varia tra tutti i sottoinsiemi non vuoti dell’insieme degli indici $\{1,\dots,n\}$.

Il segno dipende dalla cardinalità di $I$:

- intersezioni di un solo insieme: segno positivo;
- intersezioni a due a due: segno negativo;
- intersezioni a tre a tre: segno positivo;
- intersezioni a quattro a quattro: segno negativo;
- e così via.

La struttura è quindi alternata:

$$
+,-,+,-,\dots
$$

---

### 9.2 Perché compaiono i segni alternati

Consideriamo un elemento $x$ che appartiene esattamente a $m$ degli insiemi $A_1,\dots,A_n$.

Vogliamo contare quante volte $x$ contribuisce alla somma di inclusione-esclusione.

- Nella somma delle cardinalità singole, $x$ è contato $\binom{m}{1}=m$ volte.
- Nella somma delle intersezioni doppie, $x$ è contato $\binom{m}{2}$ volte con segno negativo.
- Nella somma delle intersezioni triple, $x$ è contato $\binom{m}{3}$ volte con segno positivo.
- In generale, nelle intersezioni di $k$ insiemi, $x$ è contato $\binom{m}{k}$ volte con segno $(-1)^{k+1}$.

Il contributo totale di $x$ è quindi

$$
\binom{m}{1}
-\binom{m}{2}
+\binom{m}{3}
-\cdots
+(-1)^{m+1}\binom{m}{m}.
$$

Per il binomio di Newton:

$$
(1-1)^m
=
\sum_{k=0}^{m}\binom{m}{k}(-1)^k
=
0.
$$

Separando il termine per $k=0$, che vale $1$, si ottiene

$$
\sum_{k=1}^{m}\binom{m}{k}(-1)^k=-1.
$$

Moltiplicando per $-1$:

$$
\sum_{k=1}^{m}(-1)^{k+1}\binom{m}{k}=1.
$$

Quindi ogni elemento dell’unione è contato esattamente una volta, qualunque sia il numero $m$ di insiemi a cui appartiene.

Gli elementi che non stanno nell’unione non compaiono in nessuna intersezione e contribuiscono zero.

Questo dimostra la formula di inclusione-esclusione.

---

### 9.3 Dimostrazione tramite funzioni caratteristiche

La stessa dimostrazione si può formulare con le funzioni caratteristiche.

Per ogni $x\in X$, la funzione caratteristica dell’unione soddisfa

$$
\mathbf{1}_{\bigcup_{i=1}^{n}A_i}(x)
=
\sum_{\varnothing\neq I\subseteq\{1,\dots,n\}}
(-1)^{|I|+1}
\mathbf{1}_{\bigcap_{i\in I}A_i}(x).
$$

Supponiamo che $x$ appartenga esattamente a $m$ degli insiemi. Allora:

- $\mathbf{1}_{\bigcup_i A_i}(x)=1$;
- il membro destro vale

$$
\sum_{k=1}^{m}
(-1)^{k+1}\binom{m}{k}
=1.
$$

Se invece $x$ non appartiene a nessun $A_i$, tutti i termini sono nulli e il membro destro vale $0$.

Sommando su tutti gli elementi di $X$:

$$
\sum_{x\in X}
\mathbf{1}_{\bigcup_i A_i}(x)
=
\sum_{\varnothing\neq I\subseteq\{1,\dots,n\}}
(-1)^{|I|+1}
\sum_{x\in X}
\mathbf{1}_{\bigcap_{i\in I}A_i}(x).
$$

Usando

$$
\sum_{x\in X}\mathbf{1}_B(x)=|B|,
$$

si ricava

$$
\left|\bigcup_{i=1}^{n}A_i\right|
=
\sum_{\varnothing\neq I\subseteq\{1,\dots,n\}}
(-1)^{|I|+1}
\left|\bigcap_{i\in I}A_i\right|.
$$

---

### 9.4 Complementari e unioni

Per un sottoinsieme $A\subseteq X$, il complementare è

$$
A^c=X\setminus A.
$$

La sua funzione caratteristica è

$$
\mathbf{1}_{A^c}(x)=1-\mathbf{1}_A(x).
$$

Il complementare di un’unione è l’intersezione dei complementari:

$$
\left(\bigcup_{i=1}^{n}A_i\right)^c
=
\bigcap_{i=1}^{n}A_i^c.
$$

È una delle [[Leggi di De Morgan|leggi di De Morgan]]. In termini di funzioni caratteristiche:

$$
\mathbf{1}_{(\cup_i A_i)^c}
=
1-\mathbf{1}_{\cup_i A_i}.
$$

Passare ai complementari è comodo perché l’intersezione si esprime facilmente come prodotto di funzioni caratteristiche:

$$
\mathbf{1}_{A_1\cap\cdots\cap A_n}
=
\mathbf{1}_{A_1}\cdots\mathbf{1}_{A_n}.
$$

Si può quindi ricostruire la funzione caratteristica dell’unione partendo dal complementare e sviluppando il prodotto. Il risultato è ancora la formula di inclusione-esclusione, con i segni alternati.

La funzione caratteristica trasforma così operazioni insiemistiche, spesso scomode da gestire direttamente, in operazioni algebriche su funzioni: somme, prodotti e complementi.

---

### 9.5 Esempio con tre insiemi

Per tre sottoinsiemi $A,B,C$:

$$
\begin{aligned}
|A\cup B\cup C|
={}&|A|+|B|+|C|\\
&-|A\cap B|-|A\cap C|-|B\cap C|\\
&+|A\cap B\cap C|.
\end{aligned}
$$

Il termine $|A\cap B\cap C|$ si aggiunge alla fine perché:

1. gli elementi nell’intersezione tripla sono contati tre volte nella prima riga;
2. vengono sottratti tre volte nella seconda riga;
3. quindi, fin lì, il loro contributo è $3-3=0$;
4. aggiungendo una volta l’intersezione tripla, il contributo finale diventa $1$.

Questo mostra il meccanismo generale della formula: le intersezioni di ordine successivo correggono il sovraconteggio dei termini precedenti.
