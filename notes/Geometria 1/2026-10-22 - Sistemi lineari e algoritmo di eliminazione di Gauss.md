---
type: lecture-note
course: Geometria 1
date: '2026-10-22'
title: Sistemi lineari e algoritmo di eliminazione di Gauss
source_transcript: _transcripts/Geometria 1/2026-10-22 - Sistemi lineari e algoritmo di eliminazione di
  Gauss.md
source_hash: sha256:eec556b0f85ec39319008d46b208b352ab507cff846b16950c27a5e34f5a109e
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-22T11:59:02.375Z'
vault_path: Notes/Geometria 1/Lectures/2026-10-22 - Sistemi lineari e algoritmo di eliminazione di Gauss.md
vault_hash: f92fc77db785f099c0bc1cfaba9b2a6d4c37c6d6a0a7f2434d0b8322d65b1923
---

## 1. Sistemi lineari e combinazioni lineari delle colonne

Un [[Sistema lineare|sistema lineare]] si può scrivere in forma matriciale così:

$$
A x = b,
$$

dove:

- $A$ è la [[Matrice|matrice]] dei coefficienti;
- $x$ è il vettore delle incognite;
- $b$ è il vettore dei termini noti.

Nel caso di una matrice $2\times 2$,

$$
A=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix},
\qquad
x=
\begin{pmatrix}
x_1\\
x_2
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix},
$$

l’equazione matriciale

$$
Ax=b
$$

corrisponde al sistema

$$
\begin{cases}
a x_1+b x_2=\alpha,\\
c x_1+d x_2=\beta.
\end{cases}
$$

Il [[Prodotto tra matrici|prodotto]] si può riscrivere raccogliendo le incognite:

$$
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\begin{pmatrix}
x_1\\
x_2
\end{pmatrix}
=
x_1
\begin{pmatrix}
a\\
c
\end{pmatrix}
+
x_2
\begin{pmatrix}
b\\
d
\end{pmatrix}.
$$

Quindi $Ax=b$ equivale a

$$
x_1
\begin{pmatrix}
a\\
c
\end{pmatrix}
+
x_2
\begin{pmatrix}
b\\
d
\end{pmatrix}
=
\begin{pmatrix}
\alpha\\
\beta
\end{pmatrix}.
$$

L’equazione ha soluzione se e solo se il vettore dei termini noti è una [[Combinazione lineare|combinazione lineare]] delle colonne di $A$. In altre parole,

$$
Ax=b \text{ è risolubile}
\iff
b\in \operatorname{span}\left\{
\begin{pmatrix}
a\\c
\end{pmatrix},
\begin{pmatrix}
b\\d
\end{pmatrix}
\right\}.
$$

Questa osservazione vale in generale. Siano $A$ e $b$ della forma

$$
A=
\begin{pmatrix}
| & | & & |\\
a_1 & a_2 & \cdots & a_n\\
| & | & & |
\end{pmatrix}
\in M_{m\times n}(\mathbb K),
\qquad
x=
\begin{pmatrix}
x_1\\
\vdots\\
x_n
\end{pmatrix},
\qquad
b\in \mathbb K^m.
$$

Allora

$$
Ax=x_1a_1+x_2a_2+\cdots+x_na_n.
$$

Pertanto

$$
Ax=b
$$

ha almeno una soluzione se e solo se

$$
b\in \operatorname{span}(a_1,\dots,a_n).
$$

Qui sta il legame fondamentale tra sistemi lineari e [[Sottospazio vettoriale|sottospazi vettoriali]]: verificare se un vettore appartiene allo [[Sottospazio generato|span]] di alcuni vettori equivale a risolvere un sistema lineare.

Se $v_1,\dots,v_n$ sono generatori di un sottospazio e si vuole stabilire se un vettore $w$ appartiene a tale sottospazio, si cerca di risolvere

$$
x_1v_1+\cdots+x_nv_n=w.
$$

Le incognite $x_1,\dots,x_n$ sono le [[Coordinate rispetto a una base|coordinate]] di $w$ rispetto ai generatori, se esistono.

---

## 2. Perché introdurre le matrici a scala

Un sistema lineare generico non si risolve a colpo d’occhio. L’idea dell’[[Algoritmo di eliminazione di Gauss|eliminazione di Gauss]] è trasformarlo in un sistema equivalente, cioè con le stesse soluzioni, ma di forma molto più semplice.

La forma che vogliamo è quella in cui la matrice dei coefficienti sia **[[Matrice a scala|a scala]]**.

### 2.1 Definizione di matrice a scala

Una matrice è in forma a scala se soddisfa queste condizioni:

1. le righe nulle, se presenti, si trovano in fondo alla matrice;
2. in ogni riga non nulla si considera la prima entrata non nulla;
3. la prima entrata non nulla di ogni riga si trova più a destra rispetto alla prima entrata non nulla della riga precedente;
4. sotto ogni prima entrata non nulla vi sono soltanto zeri.

Le prime entrate non nulle vengono chiamate **pivot**.

Graficamente sono dei gradini: ogni pivot sta più a destra del pivot della riga precedente e sotto ciascun pivot ci sono solo zeri.

Gli elementi a destra del pivot e quelli sopra possono essere qualsiasi: contano la posizione dei pivot e gli zeri sotto di essi.

Per esempio, una matrice del tipo

$$
\begin{pmatrix}
\ast & \ast & \ast & \ast\\
0 & \ast & \ast & \ast\\
0 & 0 & 0 & \ast\\
0 & 0 & 0 & 0
\end{pmatrix},
\qquad
\ast\neq 0 \text{ nei punti che sono pivot},
$$

è a scala.

Al contrario, una matrice non è a scala se la prima entrata non nulla di una riga sta nella stessa colonna di quella della riga precedente. Per esempio, se la seconda e la terza riga hanno entrambe il primo elemento non nullo nella seconda colonna, la matrice non è a scala.

### 2.2 Risoluzione di un sistema a scala

Consideriamo, ad esempio, un sistema a scala del tipo

$$
\begin{cases}
2x_1+x_2-2x_3=2,\\
x_2-2x_3=3.
\end{cases}
$$

La seconda equazione esprime $x_2$ in funzione di $x_3$:

$$
x_2=3+2x_3.
$$

Sostituendo nella prima equazione si ricava $x_1$:

$$
2x_1+(3+2x_3)-2x_3=2,
$$

quindi

$$
2x_1+3=2,
\qquad
x_1=-\frac12.
$$

Qui $x_3$ non è determinata da nessuna equazione: è una variabile libera. Si può assegnare a $x_3$ un valore qualsiasi e da esso ricavare $x_2$ e $x_1$.

In generale si parte dall’ultima equazione non nulla e si risale verso l’alto, usando ogni volta le variabili già trovate.

Se una variabile corrisponde a una colonna con un pivot, è determinata dalle equazioni e si chiama variabile pivot. Se la colonna non contiene alcun pivot, la variabile è libera.

> [!note]
> Che una variabile sia “libera” dipende dalla forma a scala e dalla procedura di risoluzione adottata. In linea di principio si può scegliere un parametro diverso e riscrivere la stessa famiglia di soluzioni in un’altra forma.

### 2.3 Sistemi a scala senza soluzione

Un sistema a scala non ha soluzione se compare una riga della matrice completa del tipo

$$
\begin{pmatrix}
0 & 0 & \cdots & 0 & | & c
\end{pmatrix},
\qquad c\neq 0.
$$

Questa riga corrisponde all’equazione impossibile

$$
0=c.
$$

Per esempio, la matrice completa

$$
\left(
\begin{array}{cc|c}
1 & 2 & 3\\
0 & 1 & 1\\
0 & 0 & 1
\end{array}
\right)
$$

rappresenta il sistema

$$
\begin{cases}
x_1+2x_2=3,\\
x_2=1,\\
0=1.
\end{cases}
$$

Il sistema è incompatibile.

Per un sistema già a scala questo è l’unico caso di incompatibilità: se non compare una riga del tipo $0=c$ con $c\neq 0$, il sistema è risolubile.

---

## 3. La matrice completa

Per applicare Gauss si lavora sulla matrice completa del sistema.

Se $A$ è la matrice dei coefficienti e $b$ il vettore dei termini noti, si scrive

$$
(A\mid b),
$$

dove la sbarretta separa la parte dei coefficienti dalla colonna dei termini noti:

$$
(A\mid b)=
\left(
\begin{array}{cccc|c}
a_{11} & a_{12} & \cdots & a_{1n} & b_1\\
a_{21} & a_{22} & \cdots & a_{2n} & b_2\\
\vdots & \vdots & & \vdots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn} & b_m
\end{array}
\right).
$$

La matrice completa ha lo stesso numero di righe di $A$ e una colonna aggiuntiva.

È importante distinguere:

- i pivot nelle colonne delle incognite;
- un eventuale pivot nella colonna dei termini noti.

Un pivot nella colonna dei termini noti corrisponde precisamente a una riga del tipo

$$
0=c,\qquad c\neq 0,
$$

e quindi segnala che il sistema non ha soluzioni.

---

## 4. Operazioni elementari di riga

Le [[Operazione elementare di riga|operazioni elementari di riga]] sono le trasformazioni che portano a un sistema equivalente. Sono tre:

1. scambiare due righe;
2. moltiplicare una riga per uno scalare $\lambda\neq 0$;
3. sostituire una riga con essa sommata a un multiplo di un’altra riga.

### 4.1 Scambio di due righe

Scambiare due righe cambia solo l’ordine delle equazioni, non le soluzioni.

Per esempio, il sistema

$$
\begin{cases}
x+y=1,\\
2x-y=3
\end{cases}
$$

ha le stesse soluzioni del sistema con le due equazioni invertite.

### 4.2 Moltiplicazione di una riga per uno scalare non nullo

Moltiplicare un’equazione per $\lambda\neq 0$ non ne cambia le soluzioni, perché si può sempre dividere di nuovo per $\lambda$.

Per esempio,

$$
2x_1-2x_3=2
$$

è equivalente a

$$
x_1-x_3=1,
$$

ottenuta moltiplicando la riga per $\frac12$.

Occhio: $\lambda\neq 0$ è necessario, perché moltiplicando per zero l’equazione diventa $0=0$ e si perde informazione.

### 4.3 Sommare a una riga un multiplo di un’altra

Si può sostituire una riga $R_j$ con

$$
R_j+\lambda R_k,
\qquad j\neq k.
$$

A livello di equazioni, si sostituisce un’equazione con la somma di essa e di un multiplo di un’altra.

Questa operazione non cambia le soluzioni: se un vettore soddisfa entrambe le equazioni originarie, soddisfa anche la loro combinazione lineare. Inoltre è invertibile, perché la riga precedente si recupera facendo

$$
R_j\longleftarrow R_j-\lambda R_k.
$$

> [!example] Esempio
> Nella matrice completa $\left(\begin{array}{cc|c}1&2&3\\2&5&7\end{array}\right)$ la mossa $R_2\leftarrow R_2-2R_1$ dà $\left(\begin{array}{cc|c}1&2&3\\0&1&1\end{array}\right)$. Il sistema ottenuto è a scala e ha le stesse soluzioni di quello di partenza: $x_2=1$, $x_1=1$.

Le tre operazioni si dicono operazioni elementari **di riga** perché si applicano alle righe della matrice. Si potrebbero definire operazioni analoghe sulle colonne, ma hanno effetti diversi e non si usano per risolvere i sistemi.

---

## 5. Invarianza dell’insieme delle soluzioni

Le operazioni elementari di riga applicate alla matrice completa $(A\mid b)$ producono sistemi con lo stesso insieme di soluzioni.

Il motivo è che:

- scambiare due equazioni non modifica il loro contenuto;
- moltiplicare un’equazione per uno scalare non nullo produce un’equazione equivalente;
- sommare a un’equazione un multiplo di un’altra preserva la verità del sistema e l’operazione è invertibile.

Quindi Gauss cambia l’aspetto del sistema, ma non le sue soluzioni.

---

## 6. Effetto sulle righe e sulle colonne

Occhio a distinguere l’effetto delle operazioni di riga sullo span delle righe e su quello delle colonne.

### 6.1 Lo span delle righe non cambia

Le operazioni elementari di riga non cambiano il sottospazio generato dalle righe della matrice.

Lo scambio di due righe cambia solo l’ordine dei generatori.

La moltiplicazione di una riga per $\lambda\neq 0$ non cambia lo span, perché il vettore originario si può recuperare moltiplicando per $\lambda^{-1}$.

Resta da verificare la terza operazione. Supponiamo di sostituire la riga $a_j$ con

$$
a_j'=a_j+\lambda a_k,
\qquad k\neq j.
$$

Indichiamo con $S$ lo span delle righe originarie e con $S'$ lo span delle righe dopo la trasformazione.

Ogni riga nuova appartiene a $S$, perché $a_j'$ è combinazione lineare di $a_j$ e $a_k$. Quindi

$$
S'\subseteq S.
$$

Viceversa,

$$
a_j=a_j'-\lambda a_k,
$$

e tutte le righe originarie sono combinazioni lineari delle righe nuove. Quindi

$$
S\subseteq S'.
$$

Pertanto

$$
S=S'.
$$

Di conseguenza, le operazioni elementari di riga preservano il **rango di riga** (vedi [[Rango|rango]]).

### 6.2 Lo span delle colonne può cambiare

Le operazioni di riga, invece, possono cambiare lo span delle colonne.

Nota bene: se le colonne di una matrice generano un certo sottospazio e si applicano operazioni di riga, le nuove colonne possono generare un sottospazio diverso.

Le operazioni di colonna hanno il comportamento duale:

- preservano lo span delle colonne;
- in generale possono modificare lo span delle righe.

Quindi, quando si usa Gauss per studiare lo span delle colonne, bisogna ricordare che le operazioni di riga modificano i vettori-colonna. Servono comunque a individuare le colonne pivot della matrice originale, ma lo span delle colonne della matrice ridotta non va scambiato per quello delle colonne iniziali senza ulteriori argomentazioni.

---

## 7. Algoritmo di eliminazione di Gauss

L’obiettivo dell’algoritmo è trasformare una matrice qualsiasi in una matrice a scala usando solo operazioni elementari di riga.

### 7.1 Struttura ricorsiva dell’algoritmo

Si considera la prima colonna della matrice corrente.

#### Caso 1: la colonna è tutta nulla

Se la prima colonna è tutta di zeri, la si ignora e si riapplica l’algoritmo alla sottomatrice formata dalle colonne successive. Se anche la successiva è nulla, si continua allo stesso modo: in generale si cerca la prima colonna non nulla.

#### Caso 2: la prima colonna non è nulla

Se la prima colonna contiene un elemento non nullo, si sceglie una riga $j$ con

$$
a_{j1}\neq 0.
$$

Se serve, si scambia la riga $j$ con la prima, così da avere un elemento non nullo in posizione iniziale.

Volendo, si normalizza il pivot moltiplicando la prima riga per $1/a_{11}$, ottenendo un pivot uguale a $1$.

Poi, per ogni riga sotto la prima, si elimina l’elemento della prima colonna con l’operazione

$$
R_i\longleftarrow R_i-\frac{a_{i1}}{a_{11}}R_1.
$$

Infatti, nella prima componente della nuova riga si ottiene

$$
a_{i1}-\frac{a_{i1}}{a_{11}}a_{11}=0.
$$

In questo modo il primo pivot è seguito da zeri in tutte le righe sottostanti.

A questo punto la prima riga e la prima colonna sono a posto: non si cancellano, semplicemente non si toccano più. Si guarda il rettangolo che resta sotto e a destra del primo pivot e si ripete lo stesso procedimento.

L’algoritmo procede dunque ricorsivamente su matrici sempre più piccole:

1. trovare la prima colonna non nulla della sottomatrice;
2. portare un elemento non nullo nella prima posizione disponibile;
3. usarlo come pivot;
4. annullare tutti gli elementi sottostanti nella stessa colonna;
5. passare alla sottomatrice situata sotto e a destra del pivot.

Alla fine si ottiene una matrice a scala.

### 7.2 Osservazione sugli indici

Quando si lavora con una sottomatrice, gli indici possono riferirsi alla sottomatrice corrente e non alla matrice completa.

Per esempio, nel blocco sotto il primo pivot la prima riga e la prima colonna si indicano ancora con $a_{11}$ e $a_{21}$, anche se nella matrice originale corrispondono ad altre righe e colonne.

Bisogna quindi distinguere sempre:

- gli indici relativi alla matrice completa;
- gli indici relativi alla sottomatrice su cui l’algoritmo sta operando.

### 7.3 Esempio di eliminazione

Si parte da una matrice completa qualsiasi. Se nella prima posizione c’è uno zero ma più in basso nella prima colonna c’è un elemento non nullo, si scambia la prima riga con una riga opportuna.

Dopo lo scambio, si usa il pivot della prima colonna per annullare tutto ciò che sta sotto. Per esempio, se il pivot è $a_{11}\neq 0$ e nella riga $j$ compare $a_{j1}\neq 0$, si esegue

$$
R_j\longleftarrow R_j-\frac{a_{j1}}{a_{11}}R_1.
$$

Ripetendo l’operazione per tutte le righe sotto la prima, la prima colonna assume la forma

$$
\begin{pmatrix}
a_{11}\\
0\\
\vdots\\
0
\end{pmatrix}.
$$

Poi si lavora sulla sottomatrice rimanente. Il risultato è una matrice a scala, da cui il sistema si risolve con la sostituzione all’indietro.

---

## 8. Teorema sulla risoluzione dei sistemi a scala

Sia

$$
Ax=b
$$

un sistema lineare con $n$ incognite. Si consideri la matrice completa $(A\mid b)$ e si supponga che sia in forma a scala.

Indichiamo con:

- $\operatorname{rank}_{\mathrm{righe}}(A)$ il rango di riga della matrice dei coefficienti;
- $\operatorname{rank}_{\mathrm{righe}}(A\mid b)$ il rango di riga della matrice completa;
- $k$ il numero di pivot nelle colonne delle incognite.

Allora:

### 8.1 Criterio di esistenza

Il sistema è risolubile se e solo se

$$
\operatorname{rank}_{\mathrm{righe}}(A)
=
\operatorname{rank}_{\mathrm{righe}}(A\mid b).
$$

Infatti, il rango della matrice completa è maggiore di quello della matrice dei coefficienti esattamente quando compare un pivot nella colonna dei termini noti, cioè una riga

$$
0=c,\qquad c\neq 0,
$$

che rende il sistema incompatibile.

### 8.2 Caso di soluzione unica

Se il sistema è compatibile e

$$
\operatorname{rank}_{\mathrm{righe}}(A)=n,
$$

dove $n$ è il numero delle incognite, allora ci sono $n$ pivot per $n$ incognite: nessuna variabile libera, quindi un’unica soluzione.

In questo caso:

$$
\operatorname{rank}_{\mathrm{righe}}(A)
=
\operatorname{rank}_{\mathrm{righe}}(A\mid b)
=
n.
$$

### 8.3 Caso di infinite soluzioni

Se il sistema è compatibile e

$$
\operatorname{rank}_{\mathrm{righe}}(A)
=
\operatorname{rank}_{\mathrm{righe}}(A\mid b)
=
k<n,
$$

allora ci sono $k$ pivot e $n-k$ variabili libere.

Le soluzioni dipendono quindi da $n-k$ parametri.

Se il [[Campo|campo]] $\mathbb K$ è infinito, il sistema ha infinite soluzioni. Se $\mathbb K$ è finito, le soluzioni sono

$$
|\mathbb K|^{\,n-k}.
$$

---

## 9. Esempio con variabili libere

Consideriamo il sistema

$$
\begin{cases}
x_1+x_2-x_3+2x_4=2,\\
x_3+x_4=-1.
\end{cases}
$$

La matrice completa è

$$
\left(
\begin{array}{cccc|c}
1 & 1 & -1 & 2 & 2\\
0 & 0 & 1 & 1 & -1
\end{array}
\right).
$$

I pivot sono nella prima e nella terza colonna, cioè $x_1$ e $x_3$. Le colonne senza pivot sono la seconda e la quarta, cioè $x_2$ e $x_4$: queste sono le variabili libere.

Ponendo

$$
x_2=s,
\qquad
x_4=t,
$$

la seconda equazione dà

$$
x_3+t=-1,
$$

da cui

$$
x_3=-1-t.
$$

Sostituendo nella prima equazione:

$$
x_1+s-(-1-t)+2t=2,
$$

quindi

$$
x_1=1-s-3t.
$$

L’insieme delle soluzioni è dunque

$$
\begin{pmatrix}
x_1\\
x_2\\
x_3\\
x_4
\end{pmatrix}
=
\begin{pmatrix}
1-s-3t\\
s\\
-1-t\\
t
\end{pmatrix}.
$$

Raccogliendo i parametri:

$$
\begin{pmatrix}
x_1\\
x_2\\
x_3\\
x_4
\end{pmatrix}
=
\begin{pmatrix}
1\\
0\\
-1\\
0
\end{pmatrix}
+
s
\begin{pmatrix}
-1\\
1\\
0\\
0
\end{pmatrix}
+
t
\begin{pmatrix}
-3\\
0\\
-1\\
1
\end{pmatrix}.
$$

Le due variabili libere corrispondono ai due parametri $s$ e $t$.

---

## 10. Gauss e appartenenza a uno span

Siano $v_1,\dots,v_k\in \mathbb K^m$ e sia

$$
A=
\begin{pmatrix}
| & & |\\
v_1 & \cdots & v_k\\
| & & |
\end{pmatrix}.
$$

Per stabilire se un vettore $w\in\mathbb K^m$ sta nello span di $v_1,\dots,v_k$, si considera il sistema

$$
Ax=w.
$$

Si applica l’algoritmo di Gauss alla matrice completa

$$
(A\mid w).
$$

Dopo le operazioni di riga si ottiene una matrice a scala

$$
(S\mid w').
$$

Il vettore $w$ sta nello span delle colonne di $A$ se e solo se il sistema è compatibile, cioè se non compare una riga del tipo

$$
0=c,\qquad c\neq 0.
$$

Equivalentemente, nelle righe in cui i coefficienti sono nulli deve essere nullo anche il termine noto corrispondente.

### Esempio

Consideriamo i vettori

$$
v_1=
\begin{pmatrix}
1\\
-1\\
0
\end{pmatrix},
\qquad
v_2=
\begin{pmatrix}
0\\
1\\
-1
\end{pmatrix},
$$

e un vettore generico

$$
w=
\begin{pmatrix}
x\\
y\\
z
\end{pmatrix}.
$$

Per verificare se $w\in\operatorname{span}(v_1,v_2)$, si considera

$$
\left(
\begin{array}{cc|c}
1 & 0 & x\\
-1 & 1 & y\\
0 & -1 & z
\end{array}
\right).
$$

Le prime due colonne sono i generatori, l’ultima è il vettore $w$.

Applicando operazioni di riga si può ottenere una forma a scala del tipo

$$
\left(
\begin{array}{cc|c}
1 & 0 & x\\
0 & 1 & x+y\\
0 & 0 & x+y+z
\end{array}
\right).
$$

Per evitare una contraddizione deve essere

$$
x+y+z=0.
$$

Pertanto

$$
w\in\operatorname{span}(v_1,v_2)
\iff
x+y+z=0.
$$

L’equazione

$$
x+y+z=0
$$

è quindi un’equazione cartesiana del sottospazio generato da $v_1$ e $v_2$.

In pratica abbiamo passato da una descrizione con generatori a una con equazioni.

---

## 11. Trovare una base di un sottospazio definito da equazioni

Supponiamo che un sottospazio $W\subseteq \mathbb K^n$ sia l’insieme delle soluzioni di un sistema lineare omogeneo:

$$
W=\{x\in\mathbb K^n: Ax=0\}.
$$

Per trovare una [[Base di uno spazio vettoriale|base]] di $W$:

1. si porta la matrice $A$ in forma a scala;
2. si individuano le variabili pivot e le variabili libere;
3. si assegnano parametri alle variabili libere;
4. si esprimono le variabili pivot in funzione dei parametri;
5. si raccoglie ciascun parametro.

I vettori che moltiplicano i parametri generano $W$ e sono anche linearmente indipendenti, perché ogni parametro corrisponde a una variabile libera distinta; dunque formano una base.

### Esempio

Consideriamo il sottospazio definito da

$$
\begin{cases}
x_1+2x_2=0,\\
x_3-x_4=0.
\end{cases}
$$

La matrice dei coefficienti è già a scala:

$$
\begin{pmatrix}
1 & 2 & 0 & 0\\
0 & 0 & 1 & -1
\end{pmatrix}.
$$

I pivot sono nella prima e nella terza colonna. Le variabili libere sono quindi $x_2$ e $x_4$.

Poniamo

$$
x_2=t,
\qquad
x_4=u.
$$

Le equazioni diventano

$$
x_1=-2t,
\qquad
x_3=u.
$$

Quindi ogni vettore di $W$ ha la forma

$$
\begin{pmatrix}
x_1\\
x_2\\
x_3\\
x_4
\end{pmatrix}
=
\begin{pmatrix}
-2t\\
t\\
u\\
u
\end{pmatrix}
=
t
\begin{pmatrix}
-2\\
1\\
0\\
0
\end{pmatrix}
+
u
\begin{pmatrix}
0\\
0\\
1\\
1
\end{pmatrix}.
$$

Ne segue che

$$
W=
\operatorname{span}
\left\{
\begin{pmatrix}
-2\\
1\\
0\\
0
\end{pmatrix},
\begin{pmatrix}
0\\
0\\
1\\
1
\end{pmatrix}
\right\}.
$$

I due vettori costituiscono una base di $W$.

In questo esempio il numero di vettori della base è il numero di variabili libere.

---

## 12. Indipendenza lineare e rango

Gauss serve anche a verificare se una famiglia di vettori è [[Indipendenza lineare|linearmente indipendente]].

Siano $v_1,\dots,v_k\in\mathbb K^n$. La famiglia è linearmente indipendente se l’equazione

$$
\lambda_1v_1+\cdots+\lambda_kv_k=0
$$

ha come unica soluzione

$$
\lambda_1=\cdots=\lambda_k=0.
$$

Costruendo la matrice che ha i vettori come colonne,

$$
A=
\begin{pmatrix}
| & & |\\
v_1 & \cdots & v_k\\
| & & |
\end{pmatrix},
$$

la condizione diventa

$$
A\lambda=0.
$$

Quindi si applica Gauss ad $A$ e si controlla se tutte le variabili sono pivot. Se ogni colonna contiene un pivot, il sistema omogeneo ha solo la soluzione nulla e i vettori sono linearmente indipendenti.

Se invece compare almeno una variabile libera, esiste una combinazione lineare non banale che dà il vettore nullo, e la famiglia è linearmente dipendente.

> [!example] Esempio
> I vettori $v_1=(1,0,1)$, $v_2=(0,1,1)$, $v_3=(1,1,2)$ in $\mathbb R^3$ sono le colonne di una matrice che con $R_3\leftarrow R_3-R_1$ e poi $R_3\leftarrow R_3-R_2$ diventa $\begin{pmatrix}1&0&1\\0&1&1\\0&0&0\end{pmatrix}$. La terza colonna non ha pivot, quindi c’è una variabile libera e i vettori sono dipendenti: infatti $v_3=v_1+v_2$.

Gauss permette quindi di:

- verificare l’indipendenza lineare;
- estrarre da un insieme di generatori una sottofamiglia linearmente indipendente;
- costruire una base eliminando i vettori ridondanti;
- calcolare il rango.

---

## 13. Intersezione e somma di sottospazi

Gauss serve anche a lavorare con sottospazi descritti in modi diversi.

### 13.1 Intersezione

Se due sottospazi sono descritti mediante equazioni,

$$
W_1=\{x: A_1x=0\},
\qquad
W_2=\{x: A_2x=0\},
$$

allora la loro [[Operazioni tra insiemi|intersezione]] si ottiene imponendo contemporaneamente tutte le equazioni:

$$
W_1\cap W_2
=
\{x:
A_1x=0
\text{ e }
A_2x=0\}.
$$

Basta quindi mettere insieme le equazioni di $W_1$ e quelle di $W_2$:

$$
\begin{pmatrix}
A_1\\
A_2
\end{pmatrix}x=0.
$$

Risolvendo questo sistema con Gauss si ottiene una parametrizzazione dell’intersezione e quindi una base di $W_1\cap W_2$.

Se invece i sottospazi sono dati con generatori, si può prima trasformare ciascuna descrizione in equazioni, oppure impostare direttamente le condizioni di appartenenza a entrambi.

### 13.2 Somma

Se $W_1$ e $W_2$ sono dati tramite generatori,

$$
W_1=\operatorname{span}(v_1,\dots,v_r),
\qquad
W_2=\operatorname{span}(w_1,\dots,w_s),
$$

allora la [[Somma di sottospazi|somma]] è

$$
W_1+W_2
=
\operatorname{span}(v_1,\dots,v_r,w_1,\dots,w_s).
$$

L’unione dei due insiemi di generatori genera la somma, anche se può non essere linearmente indipendente.

Per trovare una base di $W_1+W_2$ si costruisce la matrice con tutte queste colonne e si usa Gauss per eliminare i vettori ridondanti, ottenendo una famiglia indipendente che genera lo stesso sottospazio.

In sintesi:

- per l’intersezione si mettono insieme le equazioni;
- per la somma si mettono insieme i generatori;
- in entrambi i casi Gauss permette poi di passare a una base.
