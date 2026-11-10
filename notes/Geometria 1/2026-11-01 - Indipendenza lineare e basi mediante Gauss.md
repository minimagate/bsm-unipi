---
type: lecture-note
course: Geometria 1
date: '2026-11-01'
title: Indipendenza lineare e basi mediante Gauss
source_transcript: _transcripts/Geometria 1/2026-11-01 - Indipendenza lineare e basi mediante Gauss.md
source_hash: sha256:cff3070b4affb5feb66e96046568b86db3d438b245edba7b8652159dc1984687
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-11-01T08:08:08.682Z'
vault_path: Notes/Geometria 1/Lectures/2026-11-01 - Indipendenza lineare e basi mediante Gauss.md
vault_hash: 2ef591a11453bc0f424b8f2e05192a3ab495ac9ed096f59ae5e59a9e3b6e5e19
---

## 1. Verifica della struttura di spazio vettoriale e dei sottospazi

Conviene tenere distinte due situazioni.

### Verificare che un insieme sia uno spazio vettoriale

Se si introduce uno [[Spazio vettoriale|spazio vettoriale]] definendo nuove operazioni su un insieme, in linea di principio vanno verificati tutti gli assiomi:

- proprietà associativa e commutativa della somma;
- esistenza del vettore nullo;
- esistenza dell’opposto;
- distributività rispetto alla somma di vettori;
- distributività rispetto alla somma di scalari;
- compatibilità del prodotto per scalare;
- proprietà dell’elemento neutro del campo.

Non basta controllare che le operazioni siano ben definite, cioè che somma e prodotto per scalare restino nell’insieme.

### Verificare che un insieme sia un sottospazio

Se invece $W$ è già contenuto in uno spazio vettoriale noto $V$, non serve ripetere tutti gli assiomi: basta dimostrare che $W$ è un [[Sottospazio vettoriale|sottospazio]], cioè che:

1. $W$ è non vuoto, oppure contiene il vettore nullo;
2. è chiuso rispetto alla somma;
3. è chiuso rispetto al prodotto per scalare.

Equivalentemente, basta verificare che per ogni $u,v\in W$ e per ogni $\lambda,\mu$ si abbia

$$
\lambda u+\mu v\in W.
$$

Tutti gli altri assiomi sono garantiti automaticamente dalla struttura di spazio vettoriale di $V$.

> [!warning]
> Non vanno confusi la verifica degli assiomi per uno spazio vettoriale e il criterio più semplice per riconoscere un sottospazio di uno spazio già noto.

---

## 2. Indipendenza lineare

Siano $v_1,\dots,v_k$ vettori di uno spazio vettoriale $V$.

I vettori $v_1,\dots,v_k$ si dicono **[[Indipendenza lineare|linearmente indipendenti]]** se l’unica [[Combinazione lineare|combinazione lineare]] nulla è quella con tutti i coefficienti nulli:

$$
\lambda_1v_1+\lambda_2v_2+\cdots+\lambda_kv_k=0
\quad\Longrightarrow\quad
\lambda_1=\lambda_2=\cdots=\lambda_k=0.
$$

In caso contrario si dicono **linearmente dipendenti**: esistono coefficienti $\lambda_1,\dots,\lambda_k$, non tutti nulli, tali che

$$
\lambda_1v_1+\cdots+\lambda_kv_k=0.
$$

Se, ad esempio, $\lambda_k\neq 0$, si può ricavare

$$
v_k
=
-\frac{\lambda_1}{\lambda_k}v_1-\cdots
-\frac{\lambda_{k-1}}{\lambda_k}v_{k-1}.
$$

Quindi, in un insieme di vettori dipendenti, almeno un vettore è combinazione lineare degli altri.

### Interpretazione tramite un sistema lineare

Si mettono i vettori come colonne di una [[Matrice|matrice]]:

$$
A=
\begin{bmatrix}
\vert & \vert & & \vert\\
v_1 & v_2 & \cdots & v_k\\
\vert & \vert & & \vert
\end{bmatrix}.
$$

La relazione

$$
\lambda_1v_1+\cdots+\lambda_kv_k=0
$$

è equivalente al sistema omogeneo

$$
A
\begin{bmatrix}
\lambda_1\\
\lambda_2\\
\vdots\\
\lambda_k
\end{bmatrix}
=
\begin{bmatrix}
0\\
0\\
\vdots\\
0
\end{bmatrix}.
$$

Pertanto:

- i vettori sono linearmente indipendenti se il sistema ha soltanto la soluzione nulla;
- i vettori sono linearmente dipendenti se il sistema ammette soluzioni non nulle.

Riducendo $A$ a scala con l’[[Algoritmo di eliminazione di Gauss|eliminazione di Gauss]], il sistema omogeneo ha solo la soluzione nulla se e solo se ogni incognita corrisponde a una colonna pivotale. Di conseguenza:

> $v_1,\dots,v_k$ sono linearmente indipendenti se e solo se nella matrice formata da questi vettori come colonne c’è un pivot in ogni colonna.

Se i pivot sono meno delle colonne, ci sono variabili libere e quindi soluzioni non nulle del sistema omogeneo: i vettori sono dipendenti.

---

## 3. Esempio di verifica dell’indipendenza

Per verificare se una famiglia di vettori è linearmente indipendente si procede così:

1. si costruisce la matrice avente i vettori come colonne;
2. si applicano operazioni elementari sulle righe;
3. si osservano le colonne pivotali della matrice a scala.

Se tutte le colonne sono pivotali, i vettori iniziali sono linearmente indipendenti. Se invece una o più colonne non sono pivotali, la famiglia è linearmente dipendente.

A lezione sono stati fatti esempi numerici con famiglie di tre vettori. In un primo caso la riduzione dava tre pivot, e i tre vettori risultavano linearmente indipendenti. In un secondo caso dava solo due pivot, e i tre vettori erano linearmente dipendenti.

Il numero di pivot coincide con il [[Rango|rango]] della matrice e indica il numero massimo di vettori linearmente indipendenti nella famiglia.

---

## 4. Individuare un sottoinsieme linearmente indipendente

Supponiamo di avere una famiglia di vettori

$$
v_1,\dots,v_k
$$

che non è linearmente indipendente. La riduzione di Gauss non solo stabilisce che la famiglia è dipendente, ma permette anche di estrarne una sottofamiglia linearmente indipendente.

Si costruisce la matrice

$$
A=
\begin{bmatrix}
\vert & \vert & & \vert\\
v_1 & v_2 & \cdots & v_k\\
\vert & \vert & & \vert
\end{bmatrix}
$$

e la si riduce a scala. Si guardano poi le **colonne pivotali**, ricordando di riferirle alle colonne della matrice iniziale.

Se i pivot si trovano, per esempio, nelle colonne $1$, $2$ e $5$, allora i vettori

$$
v_1,\ v_2,\ v_5
$$

sono linearmente indipendenti.

In generale, i vettori iniziali corrispondenti alle colonne pivotali formano una [[Base di uno spazio vettoriale|base]] dello spazio generato da tutti i vettori:

$$
\{v_j:\text{ la colonna }j\text{ è pivotale}\}
$$

è una base di

$$
\operatorname{span}(v_1,\dots,v_k).
$$

### Perché è possibile eliminare le colonne non pivotali?

Le operazioni elementari sulle righe non cambiano l’insieme delle soluzioni del sistema omogeneo

$$
Ax=0.
$$

Quindi permettono di capire correttamente quali colonne sono indipendenti. Però le operazioni di riga modificano i vettori-colonna e, in generale, anche lo spazio da essi generato.

Per questo le colonne pivotali usate per costruire la base devono essere quelle della **matrice iniziale**, non quelle della matrice ridotta.

> [!warning]
> Le operazioni di riga preservano le soluzioni dei sistemi lineari, ma in generale non preservano lo [[Sottospazio generato|span]] delle colonne.  
> Di conseguenza, per estrarre una base dallo span delle colonne si scelgono le colonne pivotali della matrice iniziale.

### Perché si possono eliminare colonne prima o durante la riduzione?

Se si considera solo un sottoinsieme delle colonne iniziali, le stesse operazioni di Gauss si possono applicare alla matrice più piccola: le operazioni di riga agiscono su ogni colonna allo stesso modo.

Per esempio, se si vuole verificare se $v_1$ e $v_2$ sono indipendenti, si può:

- cancellare la terza colonna dalla matrice iniziale;
- proseguire la riduzione sulle due colonne rimaste;
- osservare se entrambe diventano colonne pivotali.

Non sempre serve rifare i calcoli da capo: spesso si può riutilizzare la riduzione già fatta, continuando sulla matrice ottenuta.

---

## 5. Base dello span di una famiglia di vettori

Una famiglia di vettori è una base di uno spazio se soddisfa entrambe le condizioni:

1. è linearmente indipendente;
2. genera lo spazio.

Se $v_1,\dots,v_k$ sono i vettori di partenza, Gauss permette di estrarre una base di

$$
\operatorname{span}(v_1,\dots,v_k).
$$

I vettori corrispondenti alle colonne pivotali della matrice iniziale:

- sono linearmente indipendenti;
- generano lo stesso spazio generato da tutti i vettori iniziali.

Quindi, se la matrice ha rango $r$, si ottengono esattamente $r$ vettori che formano una base dello span.

Ad esempio, se tre vettori hanno soltanto due colonne pivotali, allora:

- i tre vettori complessivamente sono dipendenti;
- i due vettori corrispondenti alle colonne pivotali sono indipendenti;
- quei due vettori formano una base dello spazio generato dai tre vettori.

Il terzo vettore è combinazione lineare dei primi due, ma per trovare la base non serve scrivere la combinazione esplicita.

---

## 6. Estrazione di una base da un insieme di generatori

Supponiamo che $v_1,\dots,v_k$ siano generatori di un sottospazio $W$:

$$
W=\operatorname{span}(v_1,\dots,v_k).
$$

Per estrarre una base di $W$:

1. si costruisce la matrice con i vettori come colonne;
2. si applica l’algoritmo di Gauss;
3. si individuano le colonne pivotali;
4. si prendono, nella matrice iniziale, i vettori corrispondenti alle colonne pivotali.

Il risultato è una base di $W$.

Questa procedura è un’**estrazione**: si parte da un insieme di generatori e si elimina la ridondanza, senza introdurre nuovi vettori.

> [!example] Esempio
> In $\mathbb{R}^2$ siano $v_1=(1,0)$, $v_2=(2,0)$, $v_3=(0,1)$. La matrice con queste colonne è già a scala e ha pivot nelle colonne $1$ e $3$. Una base di $\operatorname{span}(v_1,v_2,v_3)=\mathbb{R}^2$ è quindi $\{v_1,v_3\}$ (e infatti $v_2=2v_1$ è ridondante).

---

## 7. Completamento di una famiglia linearmente indipendente a una base

La procedura precedente estrae una base da una famiglia che già genera. La situazione opposta è il **[[Completamento a una base|completamento]]**.

Supponiamo di avere $k$ vettori linearmente indipendenti in $\mathbb{K}^n$:

$$
v_1,\dots,v_k,
\qquad k\leq n.
$$

Non sono necessariamente una base di $\mathbb{K}^n$: per esserlo devono anche generare lo spazio, e una base di $\mathbb{K}^n$ contiene $n$ vettori.

L’obiettivo è aggiungere vettori fino a ottenere una base di $\mathbb{K}^n$.

### Metodo mediante la base canonica

Si possono aggiungere ai vettori iniziali alcuni vettori della base canonica:

$$
e_1,\dots,e_n.
$$

Si considera la matrice

$$
A=
\begin{bmatrix}
\vert & \vert & & \vert & \vert & & \vert\\
v_1 & \cdots & v_k & e_1 & \cdots & e_n\\
\vert & \vert & & \vert & \vert & & \vert
\end{bmatrix}.
$$

Poiché $v_1,\dots,v_k$ sono linearmente indipendenti, le prime $k$ colonne sono già indipendenti e nella riduzione a scala producono necessariamente $k$ pivot, uno per ciascuna delle prime $k$ colonne.

Continuando la riduzione, alcune delle colonne aggiunte diventano a loro volta pivotali. Si prendono allora:

- tutti i vettori iniziali $v_1,\dots,v_k$;
- i vettori aggiunti corrispondenti alle ulteriori colonne pivotali.

L’insieme così ottenuto è una base di $\mathbb{K}^n$.

### Perché il procedimento funziona?

La base canonica genera già tutto $\mathbb{K}^n$, quindi i vettori iniziali insieme a quelli canonici sono certamente un insieme di generatori di $\mathbb{K}^n$.

Si applica allora l’algoritmo di estrazione visto prima. I primi $k$ vettori sono già indipendenti, quindi corrispondono a colonne pivotali e restano nella base estratta; si aggiungono solo i vettori canonici necessari per portare il numero di pivot a $n$.

Il risultato è una base che contiene la famiglia iniziale:

$$
\{v_1,\dots,v_k\}
\subseteq
\mathcal{B}.
$$

> [!note]
> Il completamento non produce una base qualsiasi: costruisce una base che contiene i vettori linearmente indipendenti dati in partenza.

> [!example] Esempio
> In $\mathbb{R}^3$ completiamo $\{v\}$ con $v=(1,1,0)$. Nella matrice con colonne $v,e_1,e_2,e_3$, dopo $R_2\leftarrow R_2-R_1$ i pivot sono nelle colonne $1$, $2$ e $4$ (la colonna di $e_2$ non è pivotale, infatti $e_2=v-e_1$). Una base che contiene $v$ è quindi $\{v,e_1,e_3\}$.

---

## 8. Esempio concettuale di completamento

Se si parte da una famiglia linearmente indipendente

$$
v_1,\dots,v_k\in\mathbb{K}^n,
$$

si può formare la matrice con colonne

$$
v_1,\dots,v_k,e_1,\dots,e_n.
$$

Dopo la riduzione a scala:

- le prime $k$ colonne devono essere pivotali;
- tra le colonne della base canonica si individuano quelle che forniscono i pivot mancanti;
- si mantengono i vettori corrispondenti alle colonne pivotali della matrice iniziale.

In questo modo si ottengono esattamente $n$ vettori linearmente indipendenti, quindi una base di $\mathbb{K}^n$.

Il punto è che non si cerca una base “a caso”: si completa in modo sistematico l’insieme già indipendente.

---

## 9. Intersezione di sottospazi descritti da equazioni

Per determinare l’[[Operazioni tra insiemi|intersezione]] di due sottospazi conviene usare le loro descrizioni tramite equazioni.

Supponiamo che

$$
U=\{x\in\mathbb{K}^n:A x=0\},
\qquad
W=\{x\in\mathbb{K}^n:B x=0\}.
$$

Un vettore sta nell’intersezione $U\cap W$ se e solo se soddisfa contemporaneamente entrambe le famiglie di equazioni:

$$
x\in U\cap W
\quad\Longleftrightarrow\quad
\begin{cases}
Ax=0,\\
Bx=0.
\end{cases}
$$

Si ottiene quindi un unico sistema mettendo insieme tutte le equazioni:

$$
\begin{bmatrix}
A\\
B
\end{bmatrix}x=0.
$$

La procedura è:

1. si scrivono le equazioni che descrivono il primo sottospazio;
2. si scrivono le equazioni che descrivono il secondo sottospazio;
3. si uniscono le due famiglie di equazioni in un unico sistema;
4. si riduce il sistema con Gauss;
5. si determina l’insieme delle soluzioni;
6. se necessario, si estrae una base dello spazio delle soluzioni.

Se i sottospazi sono invece dati con generatori, bisogna prima passare a una descrizione tramite equazioni.

---

## 10. Somma di sottospazi

Per la [[Somma di sottospazi|somma di sottospazi]] è di solito più comoda la descrizione tramite generatori.

Se

$$
U=\operatorname{span}(u_1,\dots,u_r),
\qquad
W=\operatorname{span}(w_1,\dots,w_s),
$$

allora

$$
U+W
=
\operatorname{span}(u_1,\dots,u_r,w_1,\dots,w_s).
$$

Quindi si procede così:

1. si raccolgono tutti i generatori di $U$ e di $W$;
2. si costruisce la matrice che li ha come colonne;
3. si applica l’algoritmo di Gauss;
4. si prendono, dalla matrice iniziale, le colonne pivotali;
5. i vettori corrispondenti costituiscono una base di $U+W$.

Se i sottospazi sono dati tramite equazioni, si trova prima una base di ciascuno risolvendo i rispettivi sistemi, e poi si applica la procedura precedente.

In sintesi:

- per l’intersezione è naturale unire le equazioni;
- per la somma è naturale unire i generatori;
- in entrambi i casi, Gauss permette infine di ottenere una base.
