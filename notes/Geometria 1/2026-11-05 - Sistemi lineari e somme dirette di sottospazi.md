---
type: lecture-note
course: Geometria 1
date: '2026-11-05'
title: Sistemi lineari e somme dirette di sottospazi
source_transcript: _transcripts/Geometria 1/2026-11-04 - Sistemi lineari e somme dirette di sottospazi.md
source_hash: sha256:ac4b8c8aacd19b6e540afb35eeeab7f351d4b048906b8da1606c3f8b553f8806
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-11-04T13:37:33.673Z'
original_date: '2026-11-04'
date_adjustment: Shifted forward one day to keep one note per course and date.
vault_path: Notes/Geometria 1/Lectures/2026-11-05 - Sistemi lineari e somme dirette di sottospazi.md
vault_hash: a21a8da824475f21cfde513f39c44f79c7aa4c14577c6cc6c898447c85e61881
---

## 1. Molteplicità di una radice e derivata di un polinomio

In questa sezione si lavora su $\mathbb R$ o $\mathbb C$, o più in generale su un [[Campo|campo]] di caratteristica zero. In caratteristica positiva il risultato richiede che la caratteristica non divida $m$: per esempio, in caratteristica $p$ si ha $(x^p)'=0$. Per $m=1$, «molteplicità $0$» significa che il punto non è una radice della derivata.

Sia $P(x)$ un [[Polinomio|polinomio]] e sia $x_0$ una sua [[Radice di un polinomio|radice di molteplicità]] $m\geq 1$. Per definizione, esiste un polinomio $Q(x)$ tale che

$$
P(x)=(x-x_0)^mQ(x),
$$

con

$$
Q(x_0)\neq 0.
$$

Occhio: $Q(x_0)\neq 0$ è essenziale. Se fosse $Q(x_0)=0$, si potrebbe estrarre un altro fattore $(x-x_0)$ e la molteplicità sarebbe maggiore di $m$.

### Derivazione

Derivando il prodotto si ottiene

$$
P'(x)
=
m(x-x_0)^{m-1}Q(x)
+
(x-x_0)^mQ'(x).
$$

Si raccoglie il fattore comune $(x-x_0)^{m-1}$:

$$
P'(x)
=
(x-x_0)^{m-1}
\left[
mQ(x)+(x-x_0)Q'(x)
\right].
$$

Pertanto $x_0$ è certamente una radice di $P'(x)$ di molteplicità almeno $m-1$.

Per la molteplicità esatta, si valuta in $x_0$ il polinomio tra parentesi:

$$
mQ(x_0)+(x_0-x_0)Q'(x_0)
=
mQ(x_0).
$$

Poiché $m\neq 0$ e $Q(x_0)\neq 0$, si ha

$$
mQ(x_0)\neq 0.
$$

Quindi il fattore tra parentesi non è divisibile per $(x-x_0)$ e la molteplicità di $x_0$ come radice di $P'(x)$ è esattamente $m-1$.

### Risultato

Se $x_0$ è radice di $P$ di molteplicità $m$, allora $x_0$ è radice di $P'$ di molteplicità $m-1$:

$$
\operatorname{mult}_{P'}(x_0)
=
\operatorname{mult}_{P}(x_0)-1.
$$

Esempi:

- radice semplice di $P$ ($m=1$): non è radice di $P'$;
- radice doppia di $P$ ($m=2$): è radice semplice di $P'$;
- radice tripla di $P$ ($m=3$): è radice doppia di $P'$.

Questa relazione copre tutti i valori possibili della molteplicità $m\geq 1$.

> [!warning]
> Vale l’implicazione
>
> $$
> x_0\text{ radice di }P\text{ di molteplicità }m
> \Longrightarrow
> x_0\text{ radice di }P'\text{ di molteplicità }m-1.
> $$
>
> In generale non vale il contrario: da $x_0$ radice di $P'$ non segue che sia radice di $P$.

---

## 2. Trasposta del prodotto di matrici

Siano $A$ e $B$ due [[Matrice|matrici]] per cui il [[Prodotto tra matrici|prodotto]] $AB$ è definito. Se

$$
A=(a_{ij}),\qquad B=(b_{jk}),
$$

allora l’elemento $(i,k)$ della matrice $AB$ è

$$
(AB)_{ik}
=
\sum_j a_{ij}b_{jk}.
$$

La [[Matrice trasposta|trasposta]] di $AB$ ha quindi elemento $(k,i)$ uguale a

$$
\bigl((AB)^T\bigr)_{ki}
=
(AB)_{ik}
=
\sum_j a_{ij}b_{jk}.
$$

D’altra parte,

$$
(B^TA^T)_{ki}
=
\sum_j (B^T)_{kj}(A^T)_{ji}
=
\sum_j b_{jk}a_{ij}.
$$

Poiché gli elementi sono scalari e quindi commutano,

$$
\sum_j b_{jk}a_{ij}
=
\sum_j a_{ij}b_{jk}.
$$

Ne segue la proprietà fondamentale:

$$
\boxed{(AB)^T=B^TA^T.}
$$

Nota bene: l’ordine dei fattori si inverte, e in generale $(AB)^T=A^TB^T$ è falso.

---

## 3. Risoluzione dei sistemi lineari con il metodo di Gauss

### 3.1. Matrice completa e forma a scala

Un [[Sistema lineare|sistema lineare]] si rappresenta con la sua matrice completa, cioè la matrice dei coefficienti affiancata dalla colonna dei termini noti.

Le [[Operazione elementare di riga|operazioni elementari sulle righe]] sono:

1. scambiare due righe;
2. moltiplicare una riga per uno scalare non nullo;
3. sommare a una riga un multiplo di un’altra riga.

Queste operazioni non modificano le soluzioni del sistema.

L’obiettivo del [[Algoritmo di eliminazione di Gauss|metodo di Gauss]] è portare la matrice in [[Matrice a scala|forma a scala]], per ricavare le incognite dall’ultima riga procedendo a ritroso.

#### Scelta del pivot

Per iniziare l’eliminazione conviene scegliere come prima riga una il cui primo coefficiente sia non nullo: se in prima posizione c’è uno zero, si scambiano le righe. Spesso conviene anche scegliere come pivot un coefficiente uguale a $1$ o $-1$, così si evitano le divisioni e i calcoli restano semplici.

> [!warning]
> Dividere per un’espressione con un parametro richiede una distinzione di casi: se si divide per $c-1$, per esempio, bisogna separare $c\neq 1$ da $c=1$.
>
> Quando possibile, meglio usare operazioni del tipo
>
> $$
> R_i\longleftarrow R_i+\lambda R_j
> $$
>
> invece di dividere per quantità che potrebbero annullarsi.

---

### 3.2. Interpretazione delle righe finali

Dopo la riduzione possono comparire tre situazioni.

#### Sistema incompatibile

Se compare una riga del tipo

$$
\begin{bmatrix}
0&0&\cdots&0&\mid&\alpha
\end{bmatrix},
\qquad \alpha\neq 0,
$$

questa riga rappresenta l’equazione impossibile

$$
0=\alpha.
$$

Il sistema non ha soluzioni.

In termini di [[Rango|rango]]:

$$
\operatorname{rank}(A)
<
\operatorname{rank}(A\mid b).
$$

#### Sistema compatibile determinato

Se il sistema è compatibile e ogni incognita corrisponde a una colonna pivot, allora esiste un’unica soluzione.

Se il numero delle incognite è $n$, la condizione è

$$
\operatorname{rank}(A)=\operatorname{rank}(A\mid b)=n.
$$

#### Sistema compatibile indeterminato

Se il sistema è compatibile e alcune colonne non sono pivot, le corrispondenti incognite sono parametri liberi: le soluzioni dipendono da tanti parametri quante sono le variabili libere,

$$
\text{numero di parametri liberi}
=
n-\operatorname{rank}(A).
$$

In questo caso le soluzioni sono infinite se il campo è infinito; su un campo finito con $q$ elementi sono $q^{n-\operatorname{rank}(A)}$.

---

## 4. Soluzione particolare e soluzione dell’omogenea

Consideriamo un sistema lineare non omogeneo

$$
A x=b.
$$

Se il sistema è compatibile, si può scegliere una soluzione particolare $x_p$ tale che

$$
Ax_p=b.
$$

Si considera poi il sistema omogeneo associato

$$
Ax=0.
$$

L’insieme delle soluzioni dell’omogenea è il [[Nucleo|nucleo]] di $A$:

$$
\ker A=\{x\mid Ax=0\}.
$$

Se $x$ è una soluzione qualunque del sistema non omogeneo, allora

$$
A(x-x_p)=Ax-Ax_p=b-b=0.
$$

Quindi $x-x_p\in\ker A$, cioè esiste $u\in\ker A$ tale che

$$
x=x_p+u.
$$

Viceversa, se $u\in\ker A$, allora

$$
A(x_p+u)=Ax_p+Au=b+0=b.
$$

Pertanto le soluzioni del sistema non omogeneo sono

$$
\boxed{x_p+\ker A.}
$$

Se $\{q_1,\dots,q_k\}$ è una [[Base di uno spazio vettoriale|base]] dello spazio delle soluzioni dell’omogenea, la soluzione generale si scrive

$$
\boxed{
x=x_p+\lambda_1q_1+\cdots+\lambda_kq_k,
\qquad
\lambda_1,\dots,\lambda_k\in\mathbb{R}.
}
$$

Geometricamente, l’insieme delle soluzioni è un traslato del sottospazio $\ker A$.

### Costruzione della soluzione particolare

Una soluzione particolare si ottiene ponendo tutti i parametri liberi uguali a zero. Non è l’unica scelta possibile: qualunque valore dei parametri dà una soluzione particolare.

Per esempio, se la soluzione generale è

$$
x=
\begin{pmatrix}
1\\
0\\
3\\
0\\
0
\end{pmatrix}
+
\lambda_1q_1+\lambda_2q_2,
$$

allora ponendo $\lambda_1=\lambda_2=0$ si ottiene la soluzione particolare

$$
x_p=
\begin{pmatrix}
1\\
0\\
3\\
0\\
0
\end{pmatrix}.
$$

I vettori $q_1,q_2$ sono invece generatori dello spazio delle soluzioni dell’omogenea; se sono linearmente indipendenti, ne formano una base.

> [!note]
> Per risolvere il sistema non omogeneo non serve rifare tutto da zero:
>
> 1. si trova una soluzione particolare;
> 2. si risolve il sistema omogeneo associato;
> 3. si sommano la soluzione particolare e tutte le soluzioni dell’omogenea.

---

## 5. Sistemi dipendenti da un parametro

Quando i coefficienti dipendono da un parametro, la forma a scala può cambiare per certi valori del parametro, quindi vanno studiati separatamente i casi in cui un pivot si annulla. Un procedimento corretto è:

1. scrivere la matrice completa;
2. eseguire operazioni di riga valide senza dividere per espressioni eventualmente nulle;
3. portare la matrice il più possibile in forma a scala;
4. individuare i coefficienti che possono annullarsi;
5. distinguere i casi corrispondenti;
6. confrontare il rango della matrice incompleta con quello della matrice completa.

### Rango e compatibilità

Per il sistema

$$
Ax=b
$$

vale il [[Teorema di Rouché-Capelli|teorema di Rouché–Capelli]]:

- il sistema è compatibile se e solo se
  $$
  \operatorname{rank}(A)=\operatorname{rank}(A\mid b);
  $$
- se il rango comune è uguale al numero $n$ delle incognite, la soluzione è unica;
- se il rango comune $r$ è minore di $n$, ci sono $n-r$ parametri liberi: infinite soluzioni su un campo infinito, oppure $q^{n-r}$ su un campo con $q$ elementi;
- se
  $$
  \operatorname{rank}(A)<\operatorname{rank}(A\mid b),
  $$
  il sistema è incompatibile.

Nel caso parametrico, un valore speciale del parametro può far annullare un pivot della matrice incompleta. Se allo stesso tempo nella matrice completa compare un elemento non nullo nella colonna dei termini noti, si ottiene una riga del tipo

$$
0=1
$$

o, più in generale,

$$
0=\alpha,\qquad \alpha\neq 0,
$$

e il sistema non ha soluzioni.

Se invece il pivot si annulla sia nei coefficienti sia nel termine noto, aumentano le variabili libere e può comparire una famiglia infinita di soluzioni.

#### Attenzione alle operazioni con parametri

Una trasformazione come

$$
R_i\longleftarrow R_i+\lambda(c)R_j
$$

è lecita per ogni valore del parametro, perché non richiede che alcun coefficiente sia non nullo.

Al contrario, la trasformazione

$$
R_i\longleftarrow \frac{1}{c-1}R_i
$$

è lecita solo se $c\neq 1$. Per usarla bisogna dividere il procedimento in due casi:

- caso $c\neq 1$;
- caso $c=1$.

Per evitare errori e casi superflui, conviene tenere i prodotti e usare somme di multipli di righe finché possibile.

---

## 6. Verifica delle soluzioni

Una volta ottenuta una soluzione, conviene sostituirla nel sistema iniziale. Così si scoprono:

- errori di calcolo;
- errori logici;
- errori nella trascrizione della matrice;
- parametri assegnati in modo scorretto;
- segni sbagliati durante l’eliminazione.

La verifica non è facoltativa: fa parte della risoluzione dell’esercizio. Se il sistema è semplice, di solito si controllano subito tutte le equazioni sostituendo il vettore trovato.

In particolare, dopo aver risolto un sistema ridotto non basta fidarsi dei passaggi formali: bisogna controllare che il vettore soddisfi davvero le equazioni originarie.

---

## 7. Metodo di studio degli esercizi

Per esercizi di questo tipo conviene procedere per gradi:

1. ripassare la tecnica generale, per esempio l’eliminazione di Gauss;
2. svolgere un esercizio semplice subito dopo aver studiato la tecnica;
3. controllare esplicitamente il risultato;
4. passare a esercizi con parametri o con condizioni aggiuntive;
5. confrontare i diversi casi e capire quale strumento è stato necessario in ciascuno.

L’obiettivo non è memorizzare una sequenza di operazioni, ma riconoscere la struttura del problema: scelta dei pivot, variabili libere, compatibilità, spazio delle soluzioni e verifica finale.

---

## 8. Basi di sottospazi definiti da equazioni

Consideriamo un [[Sottospazio vettoriale|sottospazio]] $W\subseteq\mathbb{R}^5$ definito da un’equazione lineare omogenea, per esempio

$$
x_1+2x_2+3x_3+4x_4+5x_5=0.
$$

Con una sola equazione in cinque incognite ci sono quattro parametri liberi. Si possono scegliere, ad esempio, $x_2,x_3,x_4,x_5$ come parametri e ricavare $x_1$:

$$
x_1=-2x_2-3x_3-4x_4-5x_5.
$$

Quindi un vettore generico di $W$ è

$$
\begin{pmatrix}
x_1\\x_2\\x_3\\x_4\\x_5
\end{pmatrix}
=
x_2
\begin{pmatrix}
-2\\1\\0\\0\\0
\end{pmatrix}
+
x_3
\begin{pmatrix}
-3\\0\\1\\0\\0
\end{pmatrix}
+
x_4
\begin{pmatrix}
-4\\0\\0\\1\\0
\end{pmatrix}
+
x_5
\begin{pmatrix}
-5\\0\\0\\0\\1
\end{pmatrix}.
$$

Una base di $W$ è quindi

$$
\left\{
\begin{pmatrix}
-2\\1\\0\\0\\0
\end{pmatrix},
\begin{pmatrix}
-3\\0\\1\\0\\0
\end{pmatrix},
\begin{pmatrix}
-4\\0\\0\\1\\0
\end{pmatrix},
\begin{pmatrix}
-5\\0\\0\\0\\1
\end{pmatrix}
\right\}.
$$

La dimensione è

$$
\dim W=4.
$$

### Perché non si può usare direttamente la base canonica di $\mathbb{R}^5$

La base canonica di $\mathbb{R}^5$ è una base dello spazio ambiente, ma in generale non è una base di $W$.

Per esempio,

$$
e_1=
\begin{pmatrix}
1\\0\\0\\0\\0
\end{pmatrix}
$$

non appartiene a $W$, perché sostituendolo nell’equazione si ottiene

$$
1+2\cdot 0+3\cdot 0+4\cdot 0+5\cdot 0=1\neq 0.
$$

I vettori di una base di un sottospazio devono appartenere al sottospazio.

La base canonica dello spazio dei parametri liberi si può però usare per costruire una base di $W$: si pone un parametro libero uguale a $1$ alla volta, gli altri uguali a $0$, e si ricava la coordinata dipendente dall’equazione.

---

## 9. Somma diretta di due sottospazi

Siano $U,V$ sottospazi di uno spazio vettoriale $W$. La [[Somma di sottospazi|somma]] $U+V$ è l’insieme dei vettori della forma

$$
u+v,
\qquad u\in U,\ v\in V.
$$

Si dice che la somma è [[Somma diretta|diretta]], e si scrive

$$
U\oplus V,
$$

se ogni vettore di $U+V$ si scrive in modo unico come somma di un vettore di $U$ e di un vettore di $V$.

La caratterizzazione fondamentale è

$$
\boxed{
U+V\text{ è somma diretta}
\Longleftrightarrow
U\cap V=\{0\}.
}
$$

Infatti, se

$$
u_1+v_1=u_2+v_2,
$$

allora

$$
u_1-u_2=v_2-v_1.
$$

Il vettore comune sta sia in $U$ sia in $V$, dunque in $U\cap V$. Se l’[[Operazioni tra insiemi|intersezione]] è $\{0\}$, si ha

$$
u_1-u_2=0,\qquad v_2-v_1=0,
$$

e quindi

$$
u_1=u_2,\qquad v_1=v_2.
$$

La rappresentazione è unica.

> [!example] Esempio
> In $\mathbb{R}^2$ siano $U$ l’asse $x$ e $V$ l’asse $y$. Si intersecano solo nell’origine, quindi la somma è diretta e ogni $(a,b)$ si scrive in modo unico come $(a,0)+(0,b)$. Invece le rette $U=\operatorname{span}\{(1,0)\}$ e $V'=\operatorname{span}\{(1,0)\}$ coincidono: la somma non è diretta e, per esempio, $(1,0)=(1,0)+0=0+(1,0)$.

### Basi e dimensione

Se $\mathcal{B}_U$ è una base di $U$ e $\mathcal{B}_V$ è una base di $V$, quando la somma è diretta l’unione delle due basi è una base di $U\oplus V$:

$$
\mathcal{B}_{U\oplus V}
=
\mathcal{B}_U\cup\mathcal{B}_V.
$$

Di conseguenza,

$$
\boxed{
\dim(U\oplus V)
=
\dim U+\dim V.
}
$$

Più in generale, senza l’ipotesi di somma diretta vale la [[Formula di Grassmann|formula di Grassmann]]:

$$
\dim(U+V)
=
\dim U+\dim V-\dim(U\cap V).
$$

Quindi la somma delle dimensioni vale senza termine correttivo solo quando l’intersezione è banale.

---

## 10. Somma diretta di tre o più sottospazi

Siano $U,V,Z$ sottospazi di uno spazio vettoriale. La scrittura

$$
U\oplus V\oplus Z
$$

significa che ogni vettore della somma si scrive in modo unico nella forma

$$
w=u+v+z,
\qquad
u\in U,\ v\in V,\ z\in Z.
$$

Attenzione: la condizione non equivale semplicemente a

$$
U\cap V\cap Z=\{0\},
$$

che da sola è troppo debole. Ma non basta nemmeno richiedere che tutte le intersezioni a due a due siano banali,

$$
U\cap V=\{0\},\qquad
U\cap Z=\{0\},\qquad
V\cap Z=\{0\},
$$

per garantire che $U+V+Z$ sia una somma diretta.

### Esempio nel piano

Nel piano $\mathbb{R}^2$ si possono prendere tre rette distinte per l’origine: ognuna ha dimensione $1$ e due rette distinte hanno intersezione $\{0\}$. Tuttavia le tre rette non possono essere in somma diretta, perché

$$
\dim R_1+\dim R_2+\dim R_3=1+1+1=3,
$$

mentre lo spazio ambiente ha dimensione $2$.

Se lo fossero, la somma avrebbe dimensione $3$, impossibile in $\mathbb{R}^2$.

---

### 10.1. Caratterizzazione tramite somme progressive

La condizione corretta si esprime imponendo che ciascun sottospazio abbia intersezione banale con la somma dei precedenti. Per esempio,

$$
U\oplus V\oplus Z
$$

si interpreta come

$$
(U\oplus V)\oplus Z,
$$

cioè devono valere entrambe le condizioni:

$$
U\cap V=\{0\}
$$

e

$$
(U+V)\cap Z=\{0\}.
$$

Equivalentemente, raggruppando in altro modo,

$$
U\oplus(V\oplus Z),
$$

ottenendo

$$
V\cap Z=\{0\}
$$

e

$$
U\cap(V+Z)=\{0\}.
$$

Le due formulazioni sono equivalenti perché la somma diretta è associativa. Per tre sottospazi si può quindi usare la condizione

$$
U\cap V=\{0\}
\quad\text{e}\quad
(U+V)\cap Z=\{0\}.
$$

oppure, in forma più simmetrica e generale,

$$
\boxed{
V_i\cap\sum_{j\neq i}V_j=\{0\}
\qquad
\text{per ogni }i.
}
$$

cioè ogni sottospazio deve avere intersezione banale con la somma di tutti gli altri.

---

### 10.2. Unicità della decomposizione

La somma

$$
U\oplus V\oplus Z
$$

è diretta se e solo se ogni vettore $w$ della somma ammette un’unica rappresentazione

$$
w=u+v+z.
$$

Se esistessero due rappresentazioni,

$$
w=u_1+v_1+z_1
=
u_2+v_2+z_2,
$$

si avrebbe

$$
(u_1-u_2)+(v_1-v_2)+(z_1-z_2)=0.
$$

La somma è diretta esattamente quando l’unica relazione lineare di questo tipo è quella banale:

$$
u_1-u_2=0,\qquad
v_1-v_2=0,\qquad
z_1-z_2=0.
$$

Quindi la somma diretta si può esprimere in due modi equivalenti:

1. tramite condizioni sulle intersezioni;
2. tramite unicità della scrittura dei vettori come somme di componenti appartenenti ai diversi sottospazi.

---

### 10.3. Basi e dimensione nel caso di più sottospazi

Se

$$
W=U\oplus V\oplus Z
$$

e $\mathcal{B}_U,\mathcal{B}_V,\mathcal{B}_Z$ sono basi dei tre sottospazi, allora

$$
\mathcal{B}_U\cup\mathcal{B}_V\cup\mathcal{B}_Z
$$

è una base di $W$.

Di conseguenza,

$$
\boxed{
\dim W
=
\dim U+\dim V+\dim Z.
}
$$

Si ottiene applicando due volte il risultato per due sottospazi:

$$
\dim\bigl((U\oplus V)\oplus Z\bigr)
=
\dim(U\oplus V)+\dim Z
=
\dim U+\dim V+\dim Z.
$$

Più in generale, se

$$
W=V_1\oplus\cdots\oplus V_k,
$$

allora la base di $W$ si ottiene riunendo le basi dei singoli sottospazi e

$$
\dim W
=
\sum_{i=1}^k\dim V_i.
$$

---

## 11. Costruzione di sottospazi in somma diretta

Per costruire tre sottospazi di $W$ in somma diretta, la strategia naturale è partire da una base di $W$ e dividerne i vettori in gruppi disgiunti.

Se una base di $W$ è

$$
\mathcal{B}=\{b_1,\dots,b_n\},
$$

si possono definire, ad esempio,

$$
U=\operatorname{span}(b_1,\dots,b_r),
$$

$$
V=\operatorname{span}(b_{r+1},\dots,b_s),
$$

$$
Z=\operatorname{span}(b_{s+1},\dots,b_n).
$$

Poiché tutti i vettori appartengono a una stessa base, sono linearmente indipendenti. Di conseguenza i sottospazi così ottenuti sono in somma diretta e

$$
W=U\oplus V\oplus Z.
$$

È il ragionamento inverso rispetto a quello per costruire una base della somma diretta: unendo basi dei singoli sottospazi si ottiene una base dello spazio totale; viceversa, da una base dello spazio totale si possono distribuire i vettori tra i sottospazi.

---

## 12. Intersezione tra un sottospazio generato e uno definito da equazioni

Un sottospazio si può descrivere in due modi:

- tramite [[Sottospazio generato|generatori]]:
  $$
  W=\operatorname{span}(v_1,\dots,v_k);
  $$
- tramite equazioni lineari:
  $$
  Z=\{x\mid \text{alcune condizioni lineari sono soddisfatte}\}.
  $$

Per trovare $W\cap Z$ si parte da un vettore generico di $W$:

$$
w=\alpha_1v_1+\cdots+\alpha_kv_k.
$$

Poi si impongono su $w$ le equazioni che definiscono $Z$.

Si ottiene un sistema lineare nelle variabili $\alpha_1,\dots,\alpha_k$, le cui soluzioni danno le [[Combinazione lineare|combinazioni lineari]] dei generatori di $W$ che stanno anche in $Z$.

### Descrizione tramite applicazione lineare

Supponiamo che $Z$ sia il nucleo di un’[[Applicazione lineare|applicazione lineare]] $F$:

$$
Z=\ker F.
$$

Allora

$$
W\cap Z
=
W\cap\ker F
=
\ker(F|_W),
$$

dove $F|_W$ è la restrizione di $F$ a $W$.

Per studiare questa restrizione basta conoscere l’immagine dei vettori di una base di $W$. Se

$$
w=\alpha_1v_1+\cdots+\alpha_kv_k,
$$

per linearità si ha

$$
F(w)
=
\alpha_1F(v_1)+\cdots+\alpha_kF(v_k).
$$

La condizione $w\in\ker F$ diventa quindi

$$
\alpha_1F(v_1)+\cdots+\alpha_kF(v_k)=0.
$$

Si risolve il sistema nelle coordinate $\alpha_i$ e si sostituiscono le soluzioni nell’espressione di $w$.

---

### Esempio di applicazione

Supponiamo che $W$ sia generato da tre vettori $v_1,v_2,v_3$ e che una condizione lineare definisca il sottospazio $Z$ tramite una forma lineare $f$:

$$
Z=\ker f.
$$

Supponiamo inoltre che

$$
f(v_1)=2,\qquad
f(v_2)=1,\qquad
f(v_3)=-1.
$$

Un vettore generico di $W$ è

$$
w=\alpha_1v_1+\alpha_2v_2+\alpha_3v_3.
$$

La condizione $w\in Z$ equivale a

$$
f(w)=0.
$$

Per linearità:

$$
f(w)
=
\alpha_1f(v_1)+\alpha_2f(v_2)+\alpha_3f(v_3)
=
2\alpha_1+\alpha_2-\alpha_3.
$$

Quindi bisogna risolvere

$$
2\alpha_1+\alpha_2-\alpha_3=0.
$$

Si tratta di un sistema omogeneo con una sola equazione e tre incognite, quindi ci sono due parametri liberi. Risolvendo, ad esempio rispetto ad $\alpha_1$:

$$
\alpha_1
=
-\frac{1}{2}\alpha_2+\frac{1}{2}\alpha_3.
$$

Ponendo alternativamente

$$
(\alpha_2,\alpha_3)=(1,0)
$$

e

$$
(\alpha_2,\alpha_3)=(0,1),
$$

si ottengono due soluzioni linearmente indipendenti nello spazio dei coefficienti. Sostituendole nella combinazione

$$
\alpha_1v_1+\alpha_2v_2+\alpha_3v_3,
$$

si ottengono due vettori che formano una base di $W\cap Z$, purché siano linearmente indipendenti.

Il punto è che non si cercano direttamente i vettori dell’intersezione: si cercano prima le combinazioni lineari dei generatori di $W$ che soddisfano le equazioni di $Z$.

---

## 13. Completamento di una base

Se si hanno alcuni vettori linearmente indipendenti e li si vuole [[Completamento a una base|completare a una base]] dello spazio ambiente, si possono aggiungere vettori della base canonica verificando l’indipendenza.

Procedura generale:

1. si dispongono i vettori come colonne di una matrice;
2. si applica l’eliminazione di Gauss;
3. si individuano le colonne pivot;
4. si aggiungono vettori della base canonica finché il rango raggiunge la dimensione dello spazio.

Per esempio, in $\mathbb{R}^4$ si possono iniziare ad aggiungere

$$
e_1=
\begin{pmatrix}
1\\0\\0\\0
\end{pmatrix},
\quad
e_2=
\begin{pmatrix}
0\\1\\0\\0
\end{pmatrix},
\quad
e_3=
\begin{pmatrix}
0\\0\\1\\0
\end{pmatrix},
\quad
e_4=
\begin{pmatrix}
0\\0\\0\\1
\end{pmatrix}.
$$

Non serve però aggiungerli tutti alla cieca: se i vettori iniziali sono già indipendenti, si provano i vettori canonici uno alla volta e si tengono solo quelli che aumentano il rango.

Quattro vettori linearmente indipendenti in $\mathbb{R}^4$ formano automaticamente una base.

Anche qui Gauss è il metodo generale e sicuro: guardando la posizione degli zeri a volte si capisce subito quali vettori aggiungere, ma il controllo tramite il rango resta il procedimento affidabile.
