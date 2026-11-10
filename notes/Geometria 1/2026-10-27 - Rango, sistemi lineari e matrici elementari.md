---
type: lecture-note
course: Geometria 1
date: '2026-10-27'
title: Rango, sistemi lineari e matrici elementari
source_transcript: _transcripts/Geometria 1/2026-10-27 - Rango, sistemi lineari e matrici elementari.md
source_hash: sha256:c76a4339b4a6809d57dcb73e877bab8ab0c979fdfa5f75448332bf7700fd2393
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-27T22:05:19.250Z'
vault_path: Notes/Geometria 1/Lectures/2026-10-27 - Rango, sistemi lineari e matrici elementari.md
vault_hash: edb98a65655214ebab4ab0f1e8ba117d3fe77e19b3519ec15c570ee212a7dbe3
---

## 1. Sistemi lineari e applicazioni lineari associate

Sia $A \in M_{m,n}(\mathbb{K})$ una [[Matrice|matrice]] e consideriamo l’[[Applicazione lineare|applicazione lineare]] associata

$$
f_A:\mathbb{K}^n \longrightarrow \mathbb{K}^m,
\qquad
f_A(x)=Ax.
$$

Se $A$ ha colonne $a_1,\dots,a_n$, allora, per $x=(x_1,\dots,x_n)^T$,

$$
Ax=x_1a_1+\cdots+x_na_n.
$$

Quindi l’immagine di $f_A$ è lo [[Sottospazio generato|spazio generato]] dalle colonne di $A$:

$$
\operatorname{Im}(f_A)
=
\operatorname{span}(a_1,\dots,a_n).
$$

Il [[Rango|rango]] per colonne di $A$ è dunque

$$
\operatorname{rank}(A)
=
\dim\bigl(\operatorname{span}(a_1,\dots,a_n)\bigr)
=
\dim\operatorname{Im}(f_A).
$$

Dal [[Teorema rango-nullità|teorema rango-nullità]],

$$
\dim\ker(f_A)+\dim\operatorname{Im}(f_A)=n,
$$

e quindi

$$
\dim\ker(f_A)=n-\operatorname{rank}(A).
$$

Qui $n$ è il numero di colonne di $A$, cioè la dimensione del dominio.

---

## 2. Sistemi omogenei e non omogenei

### 2.1 Sistema omogeneo

Il sistema lineare omogeneo

$$
Ax=0
$$

ha come soluzioni esattamente il [[Nucleo|nucleo]] dell’applicazione $f_A$:

$$
S_0=\{x\in\mathbb{K}^n:Ax=0\}=\ker(f_A).
$$

In particolare, $S_0$ è un sottospazio vettoriale di $\mathbb{K}^n$ e

$$
\dim S_0
=
\dim\ker(f_A)
=
n-\operatorname{rank}(A).
$$

Se si trova una [[Base di uno spazio vettoriale|base]] di $S_0$, diciamo

$$
v_1,\dots,v_k,
$$

allora ogni soluzione del sistema omogeneo si scrive nella forma

$$
x=t_1v_1+\cdots+t_kv_k,
\qquad
t_1,\dots,t_k\in\mathbb{K},
$$

dove

$$
k=n-\operatorname{rank}(A).
$$

Il metodo di Gauss dà in pratica una base dello spazio delle soluzioni.

### 2.2 Sistema non omogeneo

Consideriamo ora

$$
Ax=b.
$$

L’insieme delle soluzioni può essere vuoto. Se però esiste una soluzione particolare $\xi$, allora è

$$
S=\xi+S_0,
$$

dove

$$
S_0=\ker(f_A)=\{x:Ax=0\}.
$$

Più esplicitamente,

$$
S=\{\xi+v:v\in S_0\}.
$$

Infatti:

- se $x$ è una soluzione di $Ax=b$, allora
  $$
  A(x-\xi)=Ax-A\xi=b-b=0,
  $$
  dunque $x-\xi\in S_0$ e quindi $x=\xi+v$ per un certo $v\in S_0$;
- viceversa, se $v\in S_0$, allora
  $$
  A(\xi+v)=A\xi+Av=b+0=b.
  $$

Se $v_1,\dots,v_k$ è una base dello spazio delle soluzioni del sistema omogeneo associato, la soluzione generale del sistema non omogeneo è

$$
x=\xi+\sum_{i=1}^k t_iv_i,
\qquad
t_i\in\mathbb{K}.
$$

In sintesi, il sistema omogeneo dà la direzione dello spazio affine delle soluzioni, mentre una soluzione particolare dà il punto da cui traslare.

---

## 3. Criterio di compatibilità: teorema di Rouché-Capelli

Sia $A\in M_{m,n}(\mathbb{K})$ e sia $b\in\mathbb{K}^m$. Consideriamo la matrice completa

$$
\widetilde A=(A\mid b),
$$

ottenuta aggiungendo $b$ come ultima colonna di $A$.

Il sistema

$$
Ax=b
$$

è risolubile se e solo se

$$
\operatorname{rank}(A)=\operatorname{rank}(\widetilde A).
$$

Questa è la forma classica del [[Teorema di Rouché-Capelli|teorema di Rouché-Capelli]].

### Dimostrazione tramite lo spazio generato dalle colonne

Scrivendo $A$ per colonne,

$$
A=(a_1\ \cdots\ a_n),
$$

l’equazione $Ax=b$ equivale a

$$
x_1a_1+\cdots+x_na_n=b.
$$

Quindi $Ax=b$ è risolubile se e solo se $b$ è [[Combinazione lineare|combinazione lineare]] delle colonne di $A$, cioè

$$
b\in\operatorname{span}(a_1,\dots,a_n).
$$

Aggiungendo $b$ alle colonne, si ha sempre

$$
\operatorname{span}(a_1,\dots,a_n)
\subseteq
\operatorname{span}(a_1,\dots,a_n,b).
$$

L’uguaglianza vale se e solo se $b$ sta già nello spazio generato dalle colonne di $A$. È quanto dice il seguente claim.

> **Claim.** Per vettori $v_1,\dots,v_m,v$:
> $$
> v\in\operatorname{span}(v_1,\dots,v_m)
> \iff
> \operatorname{span}(v_1,\dots,v_m,v)=\operatorname{span}(v_1,\dots,v_m).
> $$

*Dimostrazione.* L’inclusione $\operatorname{span}(v_1,\dots,v_m)\subseteq\operatorname{span}(v_1,\dots,v_m,v)$ vale sempre (basta prendere coefficiente $0$ davanti a $v$). Il punto è l’inclusione opposta: vale se e solo se ogni vettore
$$
w=\alpha_1v_1+\cdots+\alpha_mv_m+\alpha v
$$
si può scrivere come combinazione lineare dei soli $v_1,\dots,v_m$.

- Se $v\in\operatorname{span}(v_1,\dots,v_m)$, sostituendo $v=\beta_1v_1+\cdots+\beta_mv_m$ in $w$ si ottiene una combinazione dei soli $v_i$: l’inclusione vale.
- Viceversa, se l’inclusione vale, in particolare $v$ stesso (che sta nello span di sinistra) è combinazione lineare di $v_1,\dots,v_m$, cioè $v\in\operatorname{span}(v_1,\dots,v_m)$ per definizione. $\square$

Applicando il claim con $v_i=a_i$ e $v=b$:

$$
Ax=b
\text{ è risolubile}
\iff
\operatorname{span}(a_1,\dots,a_n)
=
\operatorname{span}(a_1,\dots,a_n,b).
$$

Passando alle dimensioni,

$$
Ax=b
\text{ è risolubile}
\iff
\operatorname{rank}(A)=\operatorname{rank}(\widetilde A).
$$

L’idea è dunque che aggiungere la colonna $b$ non deve aumentare il rango.

> [!example] Esempio
> Per $A=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ e $b=(1,2)^T$ si ha $\operatorname{rank}(A)=1$, mentre $\widetilde A=\begin{pmatrix}1&1&1\\1&1&2\end{pmatrix}$ ha rango $2$. I ranghi sono diversi, quindi $Ax=b$ non ha soluzioni (le due equazioni $x_1+x_2=1$ e $x_1+x_2=2$ sono incompatibili). Con $b=(1,1)^T$ i ranghi sono entrambi $1$ e il sistema è risolubile.

---

## 4. Riduzione di Gauss e matrici a scala

Le [[Operazione elementare di riga|operazioni elementari di riga]] trasformano una matrice in una [[Matrice a scala|matrice a scala]], che ha queste caratteristiche:

- le righe nulle, se presenti, sono in fondo;
- in ogni riga non nulla, il primo elemento non nullo sta più a destra di quello della riga precedente;
- sotto ogni elemento pivot ci sono zeri.

Una generica matrice a scala può avere la forma

$$
S=
\begin{pmatrix}
* & * & * & * & \cdots & *\\
0 & * & * & * & \cdots & *\\
0 & 0 & * & * & \cdots & *\\
\vdots & & & \ddots & & \vdots\\
0 & \cdots & 0 & 0 & \cdots & 0
\end{pmatrix}.
$$

Se $S$ ha $k$ righe non nulle, allora ha $k$ pivot non nulli.

Le operazioni elementari di riga non cambiano le soluzioni del sistema associato. Perciò, se la matrice completa $\widetilde A$ viene ridotta a una matrice a scala $\widetilde S$, il sistema originale e quello ridotto hanno le stesse soluzioni.

In particolare, per il sistema omogeneo,

$$
Ax=0
\iff
Sx=0,
$$

dove $S$ è una forma a scala ottenuta da $A$ con operazioni elementari di riga.

Così si può risolvere il sistema iniziale sostituendolo con uno a forma triangolare, in cui le incognite si determinano procedendo dal basso verso l’alto.

---

## 5. Vettori a scala e indipendenza lineare

Le colonne pivot di una matrice a scala sono vettori a scala: la posizione dell’ultimo elemento non nullo di ciascun vettore si sposta progressivamente verso destra.

Un insieme di vettori a scala non nulli è [[Indipendenza lineare|linearmente indipendente]].

### Dimostrazione

Siano $v_1,\dots,v_k$ vettori a scala e supponiamo che

$$
x_1v_1+\cdots+x_kv_k=0.
$$

Guardiamo la componente corrispondente all’ultimo elemento non nullo di $v_k$. Per la struttura a scala:

- $v_k$ ha componente non nulla in quella posizione;
- i vettori precedenti hanno componente nulla in quella posizione.

L’equazione corrispondente diventa quindi

$$
x_kp_k=0,
$$

dove $p_k\neq 0$ è il pivot di $v_k$. Ne segue

$$
x_k=0.
$$

Si procede poi a ritroso: considerando la componente del pivot di $v_{k-1}$ e usando $x_k=0$, si ottiene

$$
x_{k-1}=0.
$$

Continuando così si ricava

$$
x_k=x_{k-1}=\cdots=x_1=0.
$$

Pertanto $v_1,\dots,v_k$ sono linearmente indipendenti.

---

## 6. Rango di una matrice a scala

Sia $S$ una matrice a scala con $k$ righe non nulle.

Le colonne pivot di $S$ sono $k$ vettori a scala e quindi sono linearmente indipendenti. Inoltre, ogni colonna di $S$ appartiene al sottospazio

$$
\operatorname{span}(e_1,\dots,e_k),
$$

dove $e_1,\dots,e_k$ sono i primi vettori della base canonica dello spazio delle righe della matrice.

Infatti tutte le colonne di $S$ hanno componenti nulle dalla componente $k+1$ in poi. Il sottospazio

$$
\operatorname{span}(e_1,\dots,e_k)
$$

ha dimensione $k$. Le $k$ colonne pivot sono linearmente indipendenti e stanno in questo spazio di dimensione $k$, quindi formano una base dello spazio generato da tutte le colonne di $S$.

Di conseguenza,

$$
\operatorname{rank}(S)=k,
$$

cioè il rango di una matrice a scala è uguale a:

- al numero dei pivot;
- al numero delle righe non nulle;
- alla dimensione dello spazio generato dalle colonne.

---

## 7. Invarianza del rango per riduzione di Gauss

Se $S$ è ottenuta da $A$ con operazioni elementari di riga, allora $A$ e $S$ hanno lo stesso spazio delle soluzioni del sistema omogeneo associato:

$$
\{x:Ax=0\}
=
\{x:Sx=0\}.
$$

Applicando la formula rango-nullità,

$$
n-\operatorname{rank}(A)
=
n-\operatorname{rank}(S).
$$

Pertanto

$$
\operatorname{rank}(A)=\operatorname{rank}(S).
$$

Questo è un modo rapido per dimostrare che la riduzione di [[Algoritmo di eliminazione di Gauss|Gauss]] non cambia il rango.

Poiché il rango di $S$ è il numero dei suoi pivot, per calcolare il rango di una matrice basta contare i pivot della sua forma a scala.

---

## 8. Rango per righe e rango per colonne

Il rango è stato definito come dimensione dello spazio generato dalle colonne:

$$
\operatorname{rank}_{\mathrm{col}}(A)
=
\dim\operatorname{span}(\text{colonne di }A).
$$

Si può però definire anche il rango per righe:

$$
\operatorname{rank}_{\mathrm{rig}}(A)
=
\dim\operatorname{span}(\text{righe di }A).
$$

Righe e colonne di solito stanno in spazi diversi. Se $A$ è una matrice $m\times n$:

- le colonne appartengono a $\mathbb{K}^m$;
- le righe appartengono a $\mathbb{K}^n$.

Ciononostante, i due numeri coincidono:

$$
\boxed{
\operatorname{rank}_{\mathrm{rig}}(A)
=
\operatorname{rank}_{\mathrm{col}}(A)
}.
$$

### Dimostrazione per una matrice a scala

Sia $S$ una matrice a scala con $k$ pivot.

Abbiamo già dimostrato che il rango per colonne è $k$, perché le colonne pivot formano una base dello spazio delle colonne.

D’altra parte, le $k$ righe non nulle di $S$ sono anch’esse vettori a scala, quindi linearmente indipendenti. Essendo esattamente $k$, anche il rango per righe è $k$:

$$
\operatorname{rank}_{\mathrm{rig}}(S)
=
\operatorname{rank}_{\mathrm{col}}(S)
=
k.
$$

Le operazioni elementari di riga lasciano invariato lo spazio generato dalle righe: ogni nuova riga è combinazione lineare delle righe precedenti e, poiché ogni operazione è invertibile, vale anche l’inclusione opposta. Quindi

$$
\operatorname{span}(\text{righe di }A)
=
\operatorname{span}(\text{righe di }S).
$$

Ne segue

$$
\operatorname{rank}_{\mathrm{rig}}(A)
=
\operatorname{rank}_{\mathrm{rig}}(S)
=
\operatorname{rank}_{\mathrm{col}}(S)
=
\operatorname{rank}_{\mathrm{col}}(A).
$$

### Conseguenze

Per una matrice $A\in M_{m,n}(\mathbb{K})$,

$$
\operatorname{rank}(A)\leq m,
\qquad
\operatorname{rank}(A)\leq n,
$$

e quindi

$$
\boxed{
\operatorname{rank}(A)\leq \min\{m,n\}.
}
$$

Inoltre,

$$
\boxed{
\operatorname{rank}(A)=\operatorname{rank}(A^T).
}
$$

Infatti le righe di $A$ sono le colonne della [[Matrice trasposta|trasposta]] $A^T$, quindi il rango per righe di $A$ coincide con il rango per colonne di $A^T$.

---

## 9. Matrici elementari e operazioni di riga

Le operazioni elementari di riga si possono interpretare come moltiplicazioni a sinistra per opportune matrici quadrate invertibili, dette [[Matrice elementare|matrici elementari]].

Sia $A\in M_{m,n}(\mathbb{K})$. Se $P\in M_m(\mathbb{K})$, allora $PA$ (un [[Prodotto tra matrici|prodotto tra matrici]]) è ancora una matrice $m\times n$.

### 9.1 Selezione di una riga mediante i vettori canonici

Sia $e_i^T$ il vettore canonico riga con $1$ in posizione $i$ e zeri altrove. Allora

$$
e_i^TA
$$

è la $i$-esima riga di $A$.

Infatti, se $A=(a_{ij})$, il prodotto ha componenti

$$
e_i^TA
=
(a_{i1},\dots,a_{in}).
$$

Questa osservazione serve a costruire matrici che modificano le righe di $A$ in modo controllato.

---

### 9.2 Scambio di due righe

Per scambiare le righe $i$ e $j$ di $A$ si usa la matrice di permutazione $P_{ij}$, ottenuta dalla matrice identità scambiando le righe $i$ e $j$.

Per esempio, per scambiare le prime due righe:

$$
P_{12}
=
\begin{pmatrix}
0&1&0&\cdots&0\\
1&0&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&\cdots&1
\end{pmatrix}.
$$

Allora

$$
P_{12}A
$$

si ottiene da $A$ scambiando la prima e la seconda riga.

In generale,

$$
P_{ij}A
$$

è la matrice ottenuta da $A$ scambiando le righe $i$ e $j$.

Riga per riga, usando l’osservazione precedente, la $k$-esima riga di $P_{ij}$ è
$$
(P_{ij})_k=
\begin{cases}
e_k^T & \text{se } k\neq i,j,\\
e_j^T & \text{se } k=i,\\
e_i^T & \text{se } k=j,
\end{cases}
$$
quindi la riga $i$ di $P_{ij}A$ è $e_j^TA$ (la riga $j$ di $A$), e viceversa.

Queste matrici sono invertibili: fare due volte lo stesso scambio riporta alla matrice iniziale,

$$
P_{ij}^2=I_m.
$$

Pertanto

$$
P_{ij}^{-1}=P_{ij}.
$$

---

### 9.3 Moltiplicazione di una riga per uno scalare non nullo

Per moltiplicare la riga $i$ per $\lambda\neq 0$, si usa la matrice diagonale

$$
D_i(\lambda)
=
\operatorname{diag}(1,\dots,1,\lambda,1,\dots,1),
$$

dove $\lambda$ occupa la posizione $i$-esima.

Si ha

$$
D_i(\lambda)A,
$$

che lascia invariate tutte le righe tranne la $i$, moltiplicata per $\lambda$.

La matrice è invertibile perché $\lambda\neq 0$ e

$$
D_i(\lambda)^{-1}
=
D_i(\lambda^{-1}).
$$

Infatti il prodotto di due matrici diagonali si calcola moltiplicando gli elementi corrispondenti della diagonale:

$$
\operatorname{diag}(d_1,\dots,d_m)
\operatorname{diag}(e_1,\dots,e_m)
=
\operatorname{diag}(d_1e_1,\dots,d_me_m).
$$

Una matrice diagonale è invertibile se e solo se tutti gli elementi della diagonale principale sono non nulli.

---

### 9.4 Somma di un multiplo di una riga a un’altra

Per sostituire la riga $i$ con

$$
R_i+\lambda R_j,
\qquad i\neq j,
$$

si considera la matrice

$$
E_{ij}(\lambda)=I_m+\lambda E_{ij},
$$

dove $E_{ij}$ è la matrice canonica avente un unico elemento non nullo, uguale a $1$, nella posizione $(i,j)$.

La matrice $E_{ij}(\lambda)$ coincide con l’identità, tranne per l’elemento $\lambda$ nella posizione $(i,j)$. Moltiplicando a sinistra

$$
E_{ij}(\lambda)A,
$$

si ottiene:

- la riga $i$ trasformata in $R_i+\lambda R_j$;
- tutte le altre righe invariate.

Questa matrice è invertibile e

$$
E_{ij}(\lambda)^{-1}=E_{ij}(-\lambda).
$$

Infatti, applicando prima l’operazione con $\lambda$ e poi quella con $-\lambda$, la modifica si annulla:

$$
R_i
\longmapsto
R_i+\lambda R_j
\longmapsto
R_i+\lambda R_j-\lambda R_j
=
R_i.
$$

> [!example] Esempio
> Con $m=2$ e $E_{21}(-2)=\begin{pmatrix}1&0\\-2&1\end{pmatrix}$ si ha $E_{21}(-2)\begin{pmatrix}1&2\\2&5\end{pmatrix}=\begin{pmatrix}1&2\\0&1\end{pmatrix}$: la seconda riga è diventata $R_2-2R_1$. L’inversa è $E_{21}(2)$.

---

## 10. Matrici invertibili e gruppo lineare generale

Le [[Matrice invertibile|matrici quadrate invertibili]] di ordine $m$ formano, rispetto al prodotto riga per colonna, un [[Gruppo|gruppo]], il gruppo lineare generale

$$
GL_m(\mathbb{K}).
$$

Una matrice $P\in M_m(\mathbb{K})$ è invertibile se esiste $Q\in M_m(\mathbb{K})$ tale che

$$
PQ=QP=I_m.
$$

Il prodotto di due matrici invertibili è invertibile. Se $P$ e $Q$ sono invertibili, allora

$$
(PQ)^{-1}=Q^{-1}P^{-1}.
$$

Infatti,

$$
(PQ)(Q^{-1}P^{-1})
=
P(QQ^{-1})P^{-1}
=
P I_m P^{-1}
=
I_m.
$$

Analogamente,

$$
(Q^{-1}P^{-1})(PQ)=I_m.
$$

Il gruppo $GL_m(\mathbb{K})$ non è commutativo per $m\geq 2$:

$$
PQ\neq QP
$$

per matrici generiche $P$ e $Q$, perché il prodotto di matrici non è commutativo. L’identità, però, commuta con ogni matrice.

Per $m=1$ le matrici sono semplicemente gli scalari di $\mathbb{K}$ e quelle invertibili sono gli elementi non nulli:

$$
GL_1(\mathbb{K})=\mathbb{K}^{\times}
=
\mathbb{K}\setminus\{0\}.
$$

In questo caso il gruppo è commutativo.

---

## 11. Riduzione di Gauss come prodotto di matrici elementari

Ogni operazione elementare di riga si ottiene moltiplicando a sinistra per una matrice elementare.

Se da $A$ si arriva a $S$ con una successione di operazioni elementari di riga, allora esistono matrici elementari $E_1,\dots,E_r$ tali che

$$
S=E_r\cdots E_2E_1A.
$$

Ponendo

$$
P=E_r\cdots E_2E_1,
$$

si ha

$$
S=PA.
$$

Poiché ogni matrice elementare è invertibile, anche $P$ è invertibile.

Inoltre l’inversa di ogni matrice elementare è ancora elementare:

- l’inversa di uno scambio di righe è lo stesso scambio;
- l’inversa della moltiplicazione di una riga per $\lambda\neq 0$ è la moltiplicazione per $\lambda^{-1}$;
- l’inversa dell’operazione $R_i\mapsto R_i+\lambda R_j$ è $R_i\mapsto R_i-\lambda R_j$.

---

## 12. Ogni matrice invertibile è prodotto di matrici elementari

Sia $P\in M_m(\mathbb{K})$ invertibile. Allora

$$
\operatorname{rank}(P)=m.
$$

> **Esercizio** (lasciato a lezione: «trovare e capire sulle dispense»). $P\in GL_m(\mathbb{K})\Rightarrow\operatorname{rank}(P)=m$.

*Dimostrazione.* Consideriamo $f_P:\mathbb{K}^m\to\mathbb{K}^m$, $f_P(x)=Px$. Se $Px=0$, moltiplicando a sinistra per $P^{-1}$:
$$
x=P^{-1}Px=P^{-1}0=0.
$$
Quindi $\ker(f_P)=\{0\}$ e, per rango-nullità,
$$
\operatorname{rank}(P)=m-\dim\ker(f_P)=m.
$$
In alternativa: per ogni $y\in\mathbb{K}^m$ si ha $y=P(P^{-1}y)$, quindi $f_P$ è suriettiva, $\operatorname{Im}(f_P)=\mathbb{K}^m$ e $\operatorname{rank}(P)=\dim\operatorname{Im}(f_P)=m$. $\square$

Riducendo $P$ a scala si ottiene una matrice con $m$ pivot, quindi senza righe nulle. Proseguendo fino alla forma completamente ridotta si arriva alla matrice identità:

$$
E_r\cdots E_1P=I_m
$$

per opportune matrici elementari $E_1,\dots,E_r$.

Da questa relazione segue

$$
P=E_1^{-1}\cdots E_r^{-1}.
$$

Poiché le inverse delle matrici elementari sono ancora matrici elementari, $P$ è prodotto di matrici elementari.

Quindi:

$$
\boxed{
\text{Ogni matrice invertibile è prodotto di matrici elementari.}
}
$$

In altre parole, le matrici elementari generano il gruppo $GL_m(\mathbb{K})$ rispetto al prodotto di matrici. Attenzione: è una generazione di gruppo, non di spazio vettoriale.

---

## 13. Equivalenza a sinistra

Siano $A,B\in M_{m,n}(\mathbb{K})$. Si dice che $A$ è equivalente a sinistra a $B$ se esiste una matrice invertibile $P\in GL_m(\mathbb{K})$ tale che

$$
B=PA.
$$

Si scrive, ad esempio,

$$
A\sim_{\mathrm{s}}B.
$$

Questa è una [[Relazione di equivalenza|relazione di equivalenza]].

### Riflessività

Prendendo $P=I_m$,

$$
A=I_mA,
$$

quindi

$$
A\sim_{\mathrm{s}}A.
$$

### Simmetria

Se

$$
B=PA
$$

con $P$ invertibile, allora

$$
A=P^{-1}B.
$$

Pertanto

$$
B\sim_{\mathrm{s}}A.
$$

### Transitività

Se

$$
B=PA
\qquad\text{e}\qquad
C=QB,
$$

con $P,Q$ invertibili, allora

$$
C=Q(PA)=(QP)A.
$$

Il prodotto $QP$ è invertibile, con

$$
(QP)^{-1}=P^{-1}Q^{-1}.
$$

Dunque

$$
A\sim_{\mathrm{s}}C.
$$

### Interpretazione mediante operazioni elementari

Poiché ogni matrice invertibile è prodotto di matrici elementari,

$$
B=PA
$$

se e solo se $B$ si ottiene da $A$ mediante una successione di operazioni elementari di riga.

Quindi:

$$
\boxed{
A\sim_{\mathrm{s}}B
\iff
B\text{ si ottiene da }A\text{ mediante operazioni elementari di riga}.
}
$$

Le classi di equivalenza a sinistra sono dunque le classi di matrici ottenibili l’una dall’altra con operazioni elementari sulle righe.

---

## 14. Forma completamente ridotta a scala

Una volta ottenuta una matrice a scala, si può proseguire con la riduzione.

### Primo passaggio: normalizzazione dei pivot

Ogni pivot non nullo può essere trasformato in $1$ dividendo la riga corrispondente per il pivot.

### Secondo passaggio: annullamento sopra i pivot

Dopo aver reso i pivot uguali a $1$, con operazioni elementari si annullano anche gli elementi sopra i pivot, non solo quelli sotto.

Si ottiene così una matrice [[Forma ridotta a scala|completamente ridotta a scala]], caratterizzata da:

- ogni pivot è uguale a $1$;
- nella colonna di ciascun pivot, tutti gli altri elementi sono nulli;
- le posizioni dei pivot avanzano verso destra;
- le righe nulle, se presenti, sono in fondo.

Questa forma è utile perché permette di leggere subito:

- del rango;
- delle variabili pivot e delle variabili libere;
- della soluzione di un sistema lineare;
- di una base dello spazio delle soluzioni.

La forma completamente ridotta a scala è una forma canonica per l’equivalenza a sinistra: ogni classe di equivalenza a sinistra contiene un’unica matrice completamente ridotta a scala.

> [!example] Esempio
> Da $\begin{pmatrix}2&4\\0&3\end{pmatrix}$, già a scala, si normalizzano i pivot ($R_1\leftarrow\tfrac12R_1$, $R_2\leftarrow\tfrac13R_2$) ottenendo $\begin{pmatrix}1&2\\0&1\end{pmatrix}$, poi con $R_1\leftarrow R_1-2R_2$ si arriva a $\begin{pmatrix}1&0\\0&1\end{pmatrix}=I_2$.

---

## 15. Equivalenza a destra

Si può definire una nozione analoga agendo sulle colonne.

Siano $A,B\in M_{m,n}(\mathbb{K})$. Si dice che $A$ è equivalente a destra a $B$ se esiste una matrice invertibile $Q\in GL_n(\mathbb{K})$ tale che

$$
B=AQ.
$$

In questo caso si scrive, ad esempio,

$$
A\sim_{\mathrm{d}}B.
$$

Moltiplicare a destra per una matrice elementare equivale a eseguire un’operazione elementare sulle colonne:

- scambio di due colonne;
- moltiplicazione di una colonna per uno scalare non nullo;
- somma di un multiplo di una colonna a un’altra.

Quindi

$$
\boxed{
A\sim_{\mathrm{d}}B
\iff
B\text{ si ottiene da }A\text{ mediante operazioni elementari di colonna}.
}
$$

Che sia una relazione di equivalenza si dimostra come a sinistra:

- riflessività usando $I_n$;
- simmetria usando $Q^{-1}$;
- transitività usando il prodotto di matrici invertibili.

La differenza è tutta nel lato della moltiplicazione:

- $B=PA$: operazioni sulle righe;
- $B=AQ$: operazioni sulle colonne.

Le forme canoniche per l’equivalenza a destra si ottengono quindi agendo sulle colonne invece che sulle righe.
