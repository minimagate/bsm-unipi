---
type: lecture-note
course: Geometria 1
date: '2026-10-07'
title: Coordinate, basi e dimensione degli spazi vettoriali
source_transcript: _transcripts/Geometria 1/2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali.md
source_hash: sha256:6d95338851a56c635b7ee568603a0def38c917a300f8c3ba79d04f8d2a02eedc
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-07T09:20:59.456Z'
vault_path: Notes/Geometria 1/Lectures/2026-10-07 - Coordinate, basi e dimensione degli spazi vettoriali.md
vault_hash: 7121d632aba9915084db5b674176785f59b5eb5745f70f4d9941cb1364fc171c
---
## Coordinate rispetto a una base

Sia $V$ uno [[Spazio vettoriale|spazio vettoriale]] su un campo $K$ e sia $\mathcal{B}$ una [[Base di uno spazio vettoriale|base]] di $V$.

Per definizione di base, ogni vettore $v \in V$ è [[Combinazione lineare|combinazione lineare]] dei vettori di $\mathcal{B}$. Se la base è indicizzata da un insieme $A$, formalmente si scrive

$$
v=\sum_{w\in A}\lambda_w w.
$$

Il coefficiente $\lambda_w \in K$ è la [[Coordinate rispetto a una base|coordinata]] di $v$ lungo il vettore di base $w$.

### Il caso di una base infinita

Quando $\mathcal{B}$ è infinita, la scrittura precedente non è una somma infinita arbitraria: in una combinazione lineare solo un numero finito di coefficienti può essere diverso da zero:

$$
\lambda_w\neq 0
\quad\text{solo per un numero finito di }w\in A.
$$

Quindi ogni vettore è comunque combinazione lineare finita di vettori della base.

I coefficienti $(\lambda_w)_{w\in A}$ formano quindi una famiglia in $K^A$ a supporto finito. Il supporto di una famiglia è

$$
\operatorname{supp}(\lambda)
=
\{w\in A:\lambda_w\neq 0\}.
$$

Con una base infinita, le coordinate di un vettore sono dunque una [[Funzione|funzione]]

$$
\mathcal{B}\longrightarrow K
$$

che è diversa da zero solo su un insieme finito.

> [!warning]
> Non si può identificare $V$ con l’insieme di tutte le funzioni $\mathcal{B}\to K$, perché queste potrebbero avere infiniti valori non nulli: bisogna considerare il sottospazio delle funzioni a supporto finito.

## Coordinate come applicazione

Fissata una base $\mathcal{B}$, a ogni vettore $v\in V$ si associa la funzione

$$
[v]_{\mathcal{B}}:\mathcal{B}\longrightarrow K
$$

definita da

$$
[v]_{\mathcal{B}}(w)=\lambda_w,
$$

dove $\lambda_w$ è il coefficiente di $w$ nello sviluppo di $v$ rispetto alla base $\mathcal{B}$.

La **mappa delle coordinate** è quindi

$$
\Phi_{\mathcal{B}}:V\longrightarrow K^{(\mathcal{B})},
$$

dove $K^{(\mathcal{B})}$ indica l’insieme delle funzioni $\mathcal{B}\to K$ a supporto finito.

Se la base è finita, $K^{(\mathcal{B})}$ coincide con un opportuno spazio $K^n$.

La scelta della base crea quindi una corrispondenza tra:

- i vettori di $V$;
- le loro famiglie di coordinate rispetto a $\mathcal{B}$.

In sostanza, la base permette di descrivere un vettore astratto tramite i coefficienti del suo sviluppo.

---

## Il caso finito: basi ordinate e coordinate in $K^n$

Supponiamo ora che la base sia finita, con $n$ elementi. Per vedere le coordinate come $n$-uple ordinate bisogna scegliere un ordinamento (**base ordinata**):

$$
\mathcal{B}=(v_1,\ldots,v_n).
$$

Una base finita si considera quindi come una lista ordinata di vettori, non solo come un insieme.

Ogni vettore $v\in V$ si scrive in modo unico come

$$
v=x_1v_1+\cdots+x_nv_n.
$$

Il vettore delle coordinate di $v$ rispetto alla base ordinata $\mathcal{B}$ è

$$
[v]_{\mathcal{B}}
=
\begin{pmatrix}
x_1\\
\vdots\\
x_n
\end{pmatrix}
\in K^n.
$$

La mappa delle coordinate è dunque

$$
\Phi_{\mathcal{B}}:V\longrightarrow K^n,
\qquad
v\longmapsto [v]_{\mathcal{B}}.
$$

La scrittura

$$
v=x_1v_1+\cdots+x_nv_n
$$

e la scrittura

$$
[v]_{\mathcal{B}}=(x_1,\ldots,x_n)
$$

descrivono lo stesso vettore in due modi: la prima usa i vettori della base, la seconda i coefficienti.

### L’importanza dell’ordinamento

Se si cambia l’ordine dei vettori della base, cambiano in generale le coordinate.

Per esempio, in $\mathbb{R}^2$ si possono considerare le due basi ordinate

$$
\mathcal{B}=(e_1,e_2)
\qquad\text{e}\qquad
\mathcal{B}'=(e_2,e_1).
$$

Se

$$
v=xe_1+ye_2,
$$

allora

$$
[v]_{\mathcal{B}}
=
\begin{pmatrix}
x\\
y
\end{pmatrix},
\qquad
[v]_{\mathcal{B}'}
=
\begin{pmatrix}
y\\
x
\end{pmatrix}.
$$

Il vettore geometrico è lo stesso; cambiano le coordinate perché è cambiato l’ordine dei vettori di riferimento.

Per questo, lavorando con le coordinate, si prende sempre una base ordinata.

---

## La mappa delle coordinate è un isomorfismo

La mappa

$$
\Phi_{\mathcal{B}}:V\longrightarrow K^n
$$

è una biiezione lineare, quindi è un [[Isomorfismo|isomorfismo]] di spazi vettoriali.

### Linearità

Siano

$$
v=x_1v_1+\cdots+x_nv_n,
\qquad
w=y_1v_1+\cdots+y_nv_n.
$$

Allora

$$
v+w
=
(x_1+y_1)v_1+\cdots+(x_n+y_n)v_n.
$$

Pertanto

$$
[v+w]_{\mathcal{B}}
=
\begin{pmatrix}
x_1+y_1\\
\vdots\\
x_n+y_n
\end{pmatrix}
=
\begin{pmatrix}
x_1\\
\vdots\\
x_n
\end{pmatrix}
+
\begin{pmatrix}
y_1\\
\vdots\\
y_n
\end{pmatrix}.
$$

Quindi

$$
\Phi_{\mathcal{B}}(v+w)
=
\Phi_{\mathcal{B}}(v)+\Phi_{\mathcal{B}}(w).
$$

Analogamente, per ogni $\alpha\in K$,

$$
\alpha v
=
(\alpha x_1)v_1+\cdots+(\alpha x_n)v_n,
$$

e dunque

$$
[\alpha v]_{\mathcal{B}}
=
\alpha [v]_{\mathcal{B}}.
$$

Le coordinate rispettano quindi somma e moltiplicazione per scalare.

### Iniettività

Supponiamo che due vettori $v,w\in V$ abbiano le stesse coordinate:

$$
[v]_{\mathcal{B}}=[w]_{\mathcal{B}}.
$$

Cioè hanno gli stessi coefficienti nello sviluppo rispetto alla base. Quindi

$$
v=x_1v_1+\cdots+x_nv_n
\quad\text{e}\quad
w=x_1v_1+\cdots+x_nv_n.
$$

Ne segue che $v=w$. Pertanto $\Phi_{\mathcal{B}}$ è iniettiva.

### Suriettività

Sia

$$
(x_1,\ldots,x_n)\in K^n.
$$

Consideriamo il vettore

$$
v=x_1v_1+\cdots+x_nv_n\in V.
$$

Per costruzione,

$$
[v]_{\mathcal{B}}=(x_1,\ldots,x_n).
$$

Ogni elemento di $K^n$ è quindi immagine di un vettore di $V$, perciò $\Phi_{\mathcal{B}}$ è suriettiva.

### Conclusione

La mappa delle coordinate è un isomorfismo:

$$
V\cong K^n.
$$

Quindi ogni spazio vettoriale finitamente dimensionale è, una volta scelta una base, essenzialmente uno spazio di vettori-colonna di scalari.

---

## Matrici come spazio vettoriale

### Definizione dello spazio delle matrici

Sia $K$ un campo. Si indica con

$$
M_{m,n}(K)
$$

l’insieme delle [[Matrice|matrici]] con $m$ righe e $n$ colonne a coefficienti in $K$:

$$
A=
\begin{pmatrix}
a_{11} & \cdots & a_{1n}\\
\vdots & \ddots & \vdots\\
a_{m1} & \cdots & a_{mn}
\end{pmatrix}.
$$

L’indice $i$ indica la riga e l’indice $j$ la colonna; quindi $a_{ij}$ è l’elemento nella posizione $(i,j)$.

Scrivendo semplicemente $M_n(K)$ si intende lo spazio delle matrici quadrate $n\times n$:

$$
M_n(K)=M_{n,n}(K).
$$

Per esempio, $M_2(K)$ è lo spazio delle matrici $2\times 2$.

### Operazioni

La somma è definita solo tra matrici dello stesso tipo, cioè con lo stesso numero di righe e di colonne:

$$
(A+B)_{ij}=a_{ij}+b_{ij}.
$$

La moltiplicazione per uno scalare $\lambda\in K$ si fa elemento per elemento:

$$
(\lambda A)_{ij}=\lambda a_{ij}.
$$

Con queste operazioni, $M_{m,n}(K)$ è uno spazio vettoriale su $K$.

Le operazioni sono analoghe a quelle di $K^n$; cambia solo che gli elementi sono disposti in una tabella con due indici invece che in una lista.

---

## La base canonica di $M_{m,n}(K)$

Per ogni coppia di indici

$$
1\leq i\leq m,
\qquad
1\leq j\leq n,
$$

si definisce la matrice $E_{ij}$ (non confonderla con le matrici elementari di riga che vedremo con Gauss) come la matrice che ha:

- un $1$ nella posizione $(i,j)$;
- tutti gli altri elementi uguali a $0$.

Ad esempio, in $M_{2}(K)$:

$$
E_{11}=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
E_{12}=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
$$

$$
E_{21}=
\begin{pmatrix}
0&0\\
1&0
\end{pmatrix},
\qquad
E_{22}=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
$$

L’insieme

$$
\mathcal{E}
=
\{E_{ij}:1\leq i\leq m,\ 1\leq j\leq n\}
$$

è la base canonica di $M_{m,n}(K)$.

### Generazione

Sia

$$
A=(a_{ij})\in M_{m,n}(K).
$$

Allora

$$
A=\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}E_{ij}.
$$

Infatti $a_{ij}E_{ij}$ contribuisce solo alla posizione $(i,j)$, dove mette il valore $a_{ij}$; sommando tutti i contributi si ricostruisce esattamente $A$.

Quindi le matrici elementari generano $M_{m,n}(K)$.

### Indipendenza lineare

Supponiamo che

$$
\sum_{i=1}^{m}\sum_{j=1}^{n}\lambda_{ij}E_{ij}=0.
$$

Nella posizione $(i,j)$ l’unica matrice della somma che contribuisce è $E_{ij}$. Ne segue che

$$
\lambda_{ij}=0
\qquad
\text{per ogni }i,j.
$$

Pertanto le matrici elementari sono linearmente indipendenti.

Di conseguenza, $\mathcal{E}$ è una base di $M_{m,n}(K)$.

### Dimensione

Una matrice con $m$ righe e $n$ colonne ha $mn$ posizioni. Quindi

$$
\dim_K M_{m,n}(K)=mn.
$$

In particolare,

$$
\dim_K M_n(K)=n^2.
$$

Per esempio,

$$
\dim_K M_2(K)=4.
$$

Le quattro coordinate di una matrice $2\times 2$ sono infatti i suoi quattro elementi:

$$
\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix}.
$$

> [!note]
> La base canonica delle matrici è comoda perché le coordinate si leggono direttamente: il coefficiente di $E_{ij}$ nello sviluppo di $A$ è l’elemento $a_{ij}$.

---

## Verifica dell’indipendenza: attenzione al campo

Negli esercizi sulle matrici si arriva spesso a sistemi di equazioni sui coefficienti. Ricordate che le conclusioni dipendono dal campo degli scalari.

Per esempio, da

$$
2\lambda=0
$$

si può dedurre $\lambda=0$ solo se $2$ è invertibile nel campo $K$.

Questo è vero, ad esempio, in $\mathbb{R}$ e in $\mathbb{C}$. In un campo di caratteristica $2$, invece,

$$
2=0,
$$

quindi l’equazione $2\lambda=0$ è vera per ogni $\lambda$ e non permette di concludere che $\lambda=0$.

> [!warning]
> Non si può “dividere per $2$” senza verificare che $2$ sia non nullo e invertibile nel campo considerato. In generale, risolvendo relazioni lineari bisogna tener conto della caratteristica del campo.

---

## Basi: due caratterizzazioni fondamentali

Una base è un insieme di vettori che è contemporaneamente:

1. linearmente indipendente;
2. generatore dello spazio.

Esistono però altre due caratterizzazioni molto importanti.

### Base come insieme linearmente indipendente massimale

Un insieme $B\subseteq V$ è linearmente indipendente massimale se:

- $B$ è linearmente indipendente;
- ogni insieme che contiene propriamente $B$ è linearmente dipendente.

“Massimale” si riferisce all’inclusione tra insiemi: non si può aggiungere a $B$ un vettore mantenendo l’indipendenza lineare.

#### Dimostrazione: un insieme linearmente indipendente massimale genera

Supponiamo che $B$ sia linearmente indipendente massimale. Vogliamo dimostrare che $B$ genera $V$.

Supponiamo per assurdo che esista un vettore

$$
v\in V
\qquad\text{tale che}\qquad
v\notin \operatorname{span}(B).
$$

Allora l’insieme

$$
B'=B\cup\{v\}
$$

contiene propriamente $B$. Poiché $B$ è massimale linearmente indipendente, $B'$ deve essere linearmente dipendente.

Quindi esistono scalari, non tutti nulli, tali che

$$
\sum_{i=1}^{r}\alpha_i b_i+\beta v=0,
\qquad
b_i\in B.
$$

Il coefficiente $\beta$ deve essere diverso da zero. Infatti, se $\beta=0$, si avrebbe una relazione lineare non banale tra elementi di $B$, in contraddizione con l’indipendenza di $B$.

Poiché $\beta\neq 0$, si può ricavare

$$
v
=
-\frac{1}{\beta}
\sum_{i=1}^{r}\alpha_i b_i.
$$

Questo implica

$$
v\in\operatorname{span}(B),
$$

in contraddizione con la scelta di $v$.

Pertanto non esiste alcun vettore fuori da $\operatorname{span}(B)$ e quindi

$$
\operatorname{span}(B)=V.
$$

Essendo già linearmente indipendente, $B$ è una base.

### Base come insieme minimale di generatori

Un insieme $B\subseteq V$ è un insieme minimale di generatori se:

- $B$ genera $V$;
- nessun suo sottoinsieme proprio genera $V$.

“Minimale” si riferisce all’inclusione tra insiemi: non si può togliere un vettore da $B$ continuando a generare tutto lo spazio.

#### Dimostrazione: un insieme minimale di generatori è indipendente

Supponiamo che $B$ sia un insieme minimale di generatori. Vogliamo dimostrare che $B$ è linearmente indipendente.

Supponiamo per assurdo che $B$ sia linearmente dipendente. Allora esiste una relazione lineare non banale

$$
\alpha_1b_1+\cdots+\alpha_rb_r=0,
$$

con almeno un coefficiente non nullo. Supponiamo, per esempio, che $\alpha_1\neq 0$. Allora

$$
b_1
=
-\frac{1}{\alpha_1}
\left(
\alpha_2b_2+\cdots+\alpha_rb_r
\right).
$$

Quindi $b_1$ appartiene allo span degli altri vettori:

$$
b_1\in\operatorname{span}(B\setminus\{b_1\}).
$$

Ogni vettore generato da $B$ si può quindi riscrivere usando solo gli elementi di $B\setminus\{b_1\}$. Ne segue che

$$
\operatorname{span}(B\setminus\{b_1\})=\operatorname{span}(B)=V.
$$

Ma questo contraddice la minimalità di $B$.

Pertanto $B$ è linearmente indipendente. Essendo anche un insieme di generatori, è una base.

### Equivalenza

Per ogni insieme $B\subseteq V$ sono equivalenti:

1. $B$ è una base di $V$;
2. $B$ è linearmente indipendente massimale;
3. $B$ è un insieme minimale di generatori.

Le tre descrizioni sottolineano aspetti diversi della stessa situazione:

- la base non contiene relazioni lineari non banali;
- non si può aggiungere alcun vettore senza perdere l’indipendenza;
- non si può eliminare alcun vettore senza perdere la proprietà di generare.

---

## Esistenza di una base nel caso finitamente generato

Supponiamo che $V$ sia generato da un insieme finito

$$
A=\{v_1,\ldots,v_m\}.
$$

Se $A$ è già linearmente indipendente, allora è una base.

Se invece $A$ è linearmente dipendente, c’è almeno un vettore che si può eliminare senza cambiare lo spazio generato. Lo si elimina; se il nuovo insieme è ancora dipendente, si ripete.

Poiché l’insieme iniziale è finito, il procedimento termina. Si ottiene un insieme che:

- genera ancora $V$;
- è linearmente indipendente.

Questo insieme è una base di $V$.

In particolare, ogni spazio vettoriale finitamente generato ammette una base finita.

---

## Lemma di scambio

Il risultato centrale per confrontare basi è il [[Lemma di scambio|lemma di scambio]], detto anche lemma di Steinitz.

### Forma elementare

Siano

$$
\{u_1,\ldots,u_r\}
$$

un insieme linearmente indipendente e $v\in V$ un vettore che appartiene allo span di questi vettori. Supponiamo che

$$
v=\alpha_1u_1+\cdots+\alpha_ru_r
$$

e che, per esempio, $\alpha_1\neq 0$.

Allora si può sostituire $u_1$ con $v$:

$$
\{v,u_2,\ldots,u_r\}.
$$

Il nuovo insieme:

1. è linearmente indipendente;
2. genera lo stesso sottospazio del vecchio insieme.

> [!example] Esempio
> In $\mathbb{R}^2$ prendiamo $\{u_1,u_2\}=\{(1,0),(0,1)\}$ e $v=(2,3)=2u_1+3u_2$, con $\alpha_1=2\neq 0$. Sostituendo $u_1$ con $v$ si ottiene $\{(2,3),(0,1)\}$, che è ancora indipendente e genera ancora $\mathbb{R}^2$.

#### Dimostrazione della generazione

Dalla relazione

$$
v=\alpha_1u_1+\cdots+\alpha_ru_r
$$

si ricava, poiché $\alpha_1\neq 0$,

$$
u_1
=
\frac{1}{\alpha_1}
\left(
v-\alpha_2u_2-\cdots-\alpha_ru_r
\right).
$$

Quindi $u_1$ appartiene allo span di $\{v,u_2,\ldots,u_r\}$. Gli altri vettori sono già presenti nel nuovo insieme. Pertanto

$$
\operatorname{span}(u_1,\ldots,u_r)
\subseteq
\operatorname{span}(v,u_2,\ldots,u_r).
$$

L’inclusione opposta segue dal fatto che $v$ è combinazione lineare dei vecchi vettori. Quindi gli span coincidono.

#### Dimostrazione dell’indipendenza

Supponiamo che

$$
\beta v+\beta_2u_2+\cdots+\beta_ru_r=0.
$$

Sostituendo l’espressione di $v$ si ottiene

$$
\beta
(\alpha_1u_1+\cdots+\alpha_ru_r)
+\beta_2u_2+\cdots+\beta_ru_r=0.
$$

Raccogliendo i coefficienti:

$$
(\beta\alpha_1)u_1
+
(\beta\alpha_2+\beta_2)u_2
+\cdots+
(\beta\alpha_r+\beta_r)u_r
=0.
$$

Poiché $\{u_1,\ldots,u_r\}$ è linearmente indipendente, tutti i coefficienti devono essere nulli. In particolare,

$$
\beta\alpha_1=0.
$$

Essendo $\alpha_1\neq 0$, segue $\beta=0$. Di conseguenza anche tutti gli altri coefficienti sono nulli:

$$
\beta_2=\cdots=\beta_r=0.
$$

Il nuovo insieme è quindi linearmente indipendente.

---

## Lemma di scambio nella forma per basi

Sia

$$
\mathcal{B}=(u_1,\ldots,u_n)
$$

una base di $V$ e sia

$$
\mathcal{C}=(w_1,\ldots,w_m)
$$

un insieme linearmente indipendente.

Il lemma di scambio permette di sostituire a poco a poco alcuni vettori della base $\mathcal{B}$ con vettori di $\mathcal{C}$, mantenendo sempre una base.

Si procede così:

1. si scrive $w_1$ come combinazione lineare dei vettori di $\mathcal{B}$;
2. poiché $w_1\neq 0$, almeno un coefficiente è non nullo;
3. si scambia $w_1$ con il vettore della base corrispondente a quel coefficiente;
4. si ottiene una nuova base;
5. si considera $w_2$ e si ripete il procedimento;
6. si continua finché è possibile.

Dopo ogni scambio:

- il nuovo insieme genera ancora $V$;
- il nuovo insieme rimane linearmente indipendente;
- un vettore di $\mathcal{C}$ entra nella base al posto di un vettore della base originale.

Non si possono sostituire più di $n$ vettori, perché la base iniziale ha solo $n$ elementi. Di conseguenza,

$$
m\leq n.
$$

È una delle conseguenze fondamentali del lemma di scambio:

> Un insieme linearmente indipendente in uno spazio generato da $n$ vettori contiene al massimo $n$ elementi.

In particolare, se anche $\mathcal{C}$ è una base, il risultato si applica nelle due direzioni e dà

$$
m\leq n
\qquad\text{e}\qquad
n\leq m.
$$

Pertanto

$$
m=n.
$$

Quindi tutte le basi di uno spazio vettoriale finito hanno lo stesso numero di elementi.

---

## Dimensione

Sia $V$ uno spazio vettoriale finitamente dimensionale. La **[[Dimensione di uno spazio vettoriale|dimensione]]** di $V$ è il numero di elementi di una sua base:

$$
\dim_K(V)=n
$$

se e solo se ogni base di $V$ contiene $n$ vettori.

Che questo numero non dipenda dalla base scelta è garantito dal lemma di scambio.

La dimensione è quindi il numero di parametri indipendenti che servono per descrivere un vettore di $V$.

Se $\dim_K(V)=n$, allora, scelta una base ordinata,

$$
V\cong K^n.
$$

Le coordinate di un vettore sono proprio questi $n$ parametri.

### Esempi

#### Spazio delle colonne

$$
\dim_K(K^n)=n.
$$

La base canonica è

$$
e_1=
\begin{pmatrix}
1\\0\\\vdots\\0
\end{pmatrix},
\quad
\ldots,
\quad
e_n=
\begin{pmatrix}
0\\\vdots\\0\\1
\end{pmatrix}.
$$

#### Matrici rettangolari

Per lo spazio delle matrici $m\times n$,

$$
\dim_K(M_{m,n}(K))=mn.
$$

#### Matrici quadrate

Per lo spazio delle matrici quadrate $n\times n$,

$$
\dim_K(M_n(K))=n^2.
$$

Ad esempio,

$$
\dim_K(M_2(K))=4.
$$

---

## Confronto tra basi nel caso infinito

Nel caso finito, dire che due basi hanno lo stesso numero di elementi significa che hanno la stessa cardinalità.

Nel caso infinito è più delicato: non si confrontano numeri naturali, ma si chiede l’esistenza di una biiezione tra gli insiemi delle due basi.

La formulazione generale è:

> Due basi dello stesso spazio vettoriale sono equipotenti, cioè tra esse esiste una biiezione.

Nel corso si è sviluppato soprattutto il caso finito, con il lemma di scambio. Il caso generale richiede strumenti ulteriori, tipicamente un principio di scelta o risultati equivalenti sull’esistenza e il confronto delle basi infinite.

---

## Schema concettuale

Per uno spazio vettoriale finitamente dimensionale $V$:

$$
\boxed{
\text{base}
\Longleftrightarrow
\text{insieme linearmente indipendente massimale}
\Longleftrightarrow
\text{insieme minimale di generatori}
}
$$

Se una base ha $n$ elementi, allora:

- ogni vettore di $V$ è descritto da $n$ coordinate;
- $V$ è isomorfo a $K^n$;
- ogni insieme linearmente indipendente ha al massimo $n$ elementi;
- ogni insieme di generatori ha almeno $n$ elementi;
- ogni altra base ha esattamente $n$ elementi;
- $\dim_K(V)=n$.

È il lemma di scambio a collegare queste proprietà e a garantire che il numero di elementi di una base non dipende dalla base.
