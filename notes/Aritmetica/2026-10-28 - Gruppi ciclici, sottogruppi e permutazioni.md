---
type: lecture-note
course: Aritmetica
date: '2026-10-28'
title: Gruppi ciclici, sottogruppi e permutazioni
source_transcript: _transcripts/Aritmetica/2026-10-27 - Gruppi ciclici, sottogruppi e permutazioni.md
source_hash: sha256:2d6d16bb550fe475b5f6f3a400e6d7eb63ffbbb40dfa56308aaaf5eed9d8e925
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-27T22:04:32.898Z'
original_date: '2026-10-27'
date_adjustment: Shifted forward one day to keep one note per course and date.
vault_path: Notes/Aritmetica/Lectures/2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni.md
vault_hash: 75268074c9366ee6e3bd214ccc7dc5bb36084dad7ba019e26b342913527af977
---

# Gruppi ciclici, sottogruppi e permutazioni

## 1. Esempi di gruppi

Un **[[Gruppo|gruppo]]** è un insieme $G$ dotato di un’operazione, indicata generalmente con $\cdot$, tale che:

1. l’operazione è interna:
   $$
   \forall x,y\in G,\qquad x\cdot y\in G;
   $$

2. l’operazione è associativa:
   $$
   \forall x,y,z\in G,\qquad (x\cdot y)\cdot z=x\cdot(y\cdot z);
   $$

3. esiste un elemento neutro $e\in G$:
   $$
   \forall x\in G,\qquad e\cdot x=x\cdot e=x;
   $$

4. ogni elemento è invertibile:
   $$
   \forall x\in G,\ \exists x^{-1}\in G
   \quad\text{tale che}\quad
   x\cdot x^{-1}=x^{-1}\cdot x=e.
   $$

L’operazione non deve essere per forza commutativa. Se inoltre
$$
x\cdot y=y\cdot x
\qquad\forall x,y\in G,
$$
il gruppo si dice **abeliano** o **commutativo**.

### 1.1 Notazione moltiplicativa e additiva

In notazione moltiplicativa si scrivono:

- l’operazione come $xy$ oppure $x\cdot y$;
- l’elemento neutro come $e$ oppure $1$;
- l’inverso di $x$ come $x^{-1}$;
- le potenze $x^n$.

In notazione additiva si scrivono:

- l’operazione come $x+y$;
- l’elemento neutro come $0$;
- l’opposto di $x$ come $-x$;
- i multipli interi $nx$.

La scelta della notazione dipende dall’operazione considerata e non cambia la struttura astratta di gruppo.

### 1.2 Esempi fondamentali

- $(\mathbb{Z},+)$ è un gruppo abeliano, con elemento neutro $0$ e opposto di $n$ dato da $-n$.
- $(\mathbb{Z}/m\mathbb{Z},+)$ è un gruppo abeliano finito, con $m$ elementi.
- $(\mathbb{C},+)$ è un gruppo abeliano.
- $\mathbb{C}^{\times}=\mathbb{C}\setminus\{0\}$, con il prodotto, è un gruppo abeliano. Lo zero si esclude perché non è invertibile rispetto alla moltiplicazione.
- Più in generale, se $K$ è un [[Campo|campo]], il gruppo moltiplicativo di $K$ è
  $$
  K^\times=K\setminus\{0\}.
  $$
- L’insieme degli elementi invertibili di un anello $R$ rispetto al prodotto si indica spesso con $R^\times$ oppure $R^*$.
- Gli spazi vettoriali, se si guarda solo alla loro struttura additiva e si dimentica il prodotto per scalare, sono gruppi abeliani rispetto alla somma.

Nel caso degli interi modulo $m$, l’insieme degli [[Elementi invertibili modulo n|elementi invertibili]] rispetto al prodotto è
$$
(\mathbb{Z}/m\mathbb{Z})^\times
=
\left\{\overline{a}\in\mathbb{Z}/m\mathbb{Z}:
\gcd(a,m)=1\right\}.
$$

L’operazione è il prodotto modulo $m$. Per esempio, $\overline{a}$ è invertibile modulo $m$ se e solo se esiste $\overline{b}$ tale che
$$
\overline{a}\,\overline{b}=\overline{1}.
$$

### 1.3 Proprietà elementari dei gruppi

> **Proposizione.** Sia $(G,\cdot)$ un gruppo. Allora:
>
> 1. l’elemento neutro è unico;
> 2. l’inverso di ogni $g\in G$ è unico;
> 3. $(g^{-1})^{-1}=g$ per ogni $g\in G$;
> 4. $(gh)^{-1}=h^{-1}g^{-1}$ per ogni $g,h\in G$;
> 5. (cancellazione) $ab=ac\ \Rightarrow\ b=c$, e analogamente $ba=ca\ \Rightarrow\ b=c$.

#### Dimostrazione

1. Se $e,e'$ sono entrambi elementi neutri, allora
   $$
   e=e\cdot e'=e'.
   $$
   (La prima uguaglianza usa che $e'$ è neutro, la seconda che lo è $e$.)

2. Siano $x,y$ due inversi di $g$. Allora
   $$
   x=x\cdot e=x(gy)=(xg)y=e\cdot y=y.
   $$

3. Da $g^{-1}g=gg^{-1}=e$ si legge che $g$ è un inverso di $g^{-1}$. Per l’unicità dell’inverso (punto 2), $(g^{-1})^{-1}=g$.

4. Si verifica che $h^{-1}g^{-1}$ è un inverso di $gh$:
   $$
   (gh)(h^{-1}g^{-1})=g(hh^{-1})g^{-1}=g\,e\,g^{-1}=gg^{-1}=e,
   $$
   e allo stesso modo $(h^{-1}g^{-1})(gh)=e$. Per l’unicità, $(gh)^{-1}=h^{-1}g^{-1}$.

5. Moltiplicando $ab=ac$ a sinistra per $a^{-1}$:
   $$
   a^{-1}ab=a^{-1}ac\ \Rightarrow\ b=c.
   $$

> [!warning]
> L’ordine nel punto 4 si inverte: in un gruppo non abeliano, in generale $(gh)^{-1}\neq g^{-1}h^{-1}$.

## 2. Le radici $n$-esime dell’unità

Sia $n\geq 1$. L’insieme delle [[Radice n-esima dell'unità|radici $n$-esime dell’unità]] è
$$
\mu_n=\{z\in\mathbb{C}:z^n=1\}.
$$

(Negli appunti questo gruppo è indicato con $C_n=\{z\in\mathbb{C}^*:z^n=1\}$.)

Poiché $0^n\neq 1$, lo zero non appartiene a $\mu_n$. L’insieme $\mu_n$ è un gruppo rispetto alla moltiplicazione complessa.

La verifica delle proprietà è la seguente:

- se $z,w\in\mu_n$, allora
  $$
  (zw)^n=z^nw^n=1,
  $$
  quindi $zw\in\mu_n$;
- l’elemento neutro è $1$, che soddisfa $1^n=1$;
- se $z^n=1$, allora
  $$
  z^{-1}=z^{n-1},
  $$
  perché
  $$
  z\cdot z^{n-1}=z^n=1;
  $$
- l’associatività è quella della moltiplicazione complessa.

Le radici $n$-esime dell’unità sono
$$
\mu_n=
\left\{
e^{2\pi i k/n}:k=0,1,\dots,n-1
\right\}.
$$

Sono quindi $n$ elementi disposti regolarmente sulla circonferenza unitaria nel piano complesso. Se $\zeta=e^{2\pi i/n}$, allora
$$
\mu_n=\{1,\zeta,\zeta^2,\dots,\zeta^{n-1}\}.
$$

In particolare $\mu_n$ è un gruppo ciclico generato da $\zeta$:
$$
\mu_n=\langle \zeta\rangle.
$$

## 3. Sottogruppi

### 3.1 Definizione

Sia $G$ un gruppo. Un [[Sottoinsieme|sottoinsieme]] $H\subseteq G$ si dice **[[Sottogruppo|sottogruppo]]** di $G$ se, considerando su $H$ la stessa operazione di $G$, l’insieme $H$ è a sua volta un gruppo.

Si scrive
$$
H\leq G.
$$

Non basta che $H$ sia un sottoinsieme di $G$: bisogna verificare che l’operazione e le strutture necessarie siano compatibili.

### 3.2 Criterio del sottogruppo

Un criterio pratico molto importante è il seguente.

> **Criterio del sottogruppo.**  
> Sia $G$ un gruppo e sia $H\subseteq G$. Se:
> 
> 1. $H\neq\varnothing$;
> 2. per ogni $x,y\in H$ vale
>    $$
>    xy^{-1}\in H,
>    $$
> 
> allora $H$ è un sottogruppo di $G$.

La condizione $xy^{-1}\in H$ permette di verificare in un colpo solo la chiusura rispetto al prodotto e rispetto agli inversi.

> [!example] Esempio
> Sia $n\in\mathbb Z$ e $H=n\mathbb Z\subseteq(\mathbb Z,+)$. In notazione additiva la condizione è $x-y\in H$. $H$ non è vuoto ($0\in H$) e se $x=na$, $y=nb$ allora $x-y=n(a-b)\in n\mathbb Z$. Quindi $n\mathbb Z\leq\mathbb Z$.

#### Dimostrazione

Poiché $H\neq\varnothing$, esiste $a\in H$.

Ponendo $x=y=a$ nella condizione, si ottiene
$$
aa^{-1}=e\in H.
$$

Quindi l’elemento neutro di $G$ appartiene a $H$.

Ora, preso $x\in H$, poiché $e\in H$, la condizione applicata a $e$ e $x$ dà
$$
ex^{-1}=x^{-1}\in H.
$$

Infine, se $x,y\in H$, abbiamo già direttamente
$$
xy^{-1}\in H.
$$
Poiché $y^{-1}\in H$, possiamo sostituire $y^{-1}$ al secondo elemento e ottenere
$$
x(y^{-1})^{-1}=xy\in H.
$$

Pertanto $H$ è chiuso rispetto al prodotto e agli inversi. L’associatività è ereditata da $G$, e l’elemento neutro è lo stesso $e$ di $G$. Dunque $H$ è un gruppo.

### 3.3 Perché l’elemento neutro e gli inversi sono quelli di $G$

Se $H\leq G$, l’operazione su $H$ è la restrizione dell’operazione di $G$. Non si introducono nuove operazioni.

L’elemento neutro di $H$ deve quindi coincidere con quello di $G$. Infatti, se $e_H$ fosse l’identità di $H$, allora per ogni $h\in H$ si avrebbe
$$
e_Hh=h.
$$
Ma anche $eh=h$. Per l’unicità dell’elemento neutro, segue che
$$
e_H=e.
$$

Allo stesso modo, l’inverso di un elemento è unico. Se $x\in H$ e $y,z\in H$ sono entrambi inversi di $x$, allora
$$
y=y e=y(xz)=(yx)z=ez=z.
$$

Quindi l’inverso di $x$ calcolato in $H$ coincide con l’inverso calcolato in $G$.

> [!warning]
> Per verificare che un insieme è un sottogruppo non serve ricontrollare l’associatività, se l’operazione è già quella di un gruppo ambiente: viene ereditata automaticamente. Bisogna invece verificare che l’insieme non sia vuoto e che contenga i prodotti e gli inversi necessari.

**Esempi banali.** Per ogni gruppo $G$, sia $G$ stesso sia $\{e\}$ sono sottogruppi di $G$.

### 3.4 Intersezione e unione di sottogruppi

> **Proposizione.** Siano $H,K\leq G$. Allora:
>
> - $H\cap K\leq G$;
> - $H\cup K\leq G\iff H\subseteq K$ oppure $K\subseteq H$.

#### Dimostrazione

*Intersezione.* $e\in H$ ed $e\in K$, quindi $e\in H\cap K\neq\varnothing$. Se $x,y\in H\cap K$, allora $xy^{-1}\in H$ (perché $H\leq G$) e $xy^{-1}\in K$ (perché $K\leq G$), dunque $xy^{-1}\in H\cap K$. Per il criterio del sottogruppo, $H\cap K\leq G$.

*Unione, $(\Leftarrow)$.* Se $H\subseteq K$, allora $H\cup K=K$, che è un sottogruppo; analogamente se $K\subseteq H$.

*Unione, $(\Rightarrow)$.* Supponiamo per assurdo che $H\cup K\leq G$ ma che nessuno dei due sia contenuto nell’altro. Esistono allora
$$
h\in H\setminus K,
\qquad
k\in K\setminus H.
$$
Poiché $H\cup K$ è chiuso rispetto al prodotto, $hk\in H\cup K$.

- Se $hk\in H$, allora $k=h^{-1}(hk)\in H$: assurdo.
- Se $hk\in K$, allora $h=(hk)k^{-1}\in K$: assurdo.

Quindi $H\subseteq K$ oppure $K\subseteq H$.

> [!note]
> La dimostrazione negli appunti è rimasta in bianco; quella sopra è l’argomento standard.

### 3.5 Esercizio: sottogruppi $d\mathbb{Z}$ di $\mathbb{Z}$

Sia $d\in\mathbb{Z}$. Allora
$$
\langle d\rangle=\{dn\}_{n\in\mathbb{Z}}=d\mathbb{Z}\leq\mathbb{Z}.
$$

**(a)** $d\mathbb{Z}\subseteq m\mathbb{Z}\iff m\mid d$.

- $(\Rightarrow)$ $d=d\cdot 1\in d\mathbb{Z}\subseteq m\mathbb{Z}$, quindi $d=mq$ per qualche $q$, cioè $m\mid d$.
- $(\Leftarrow)$ Se $d=mq$, ogni elemento $dn=m(qn)$ sta in $m\mathbb{Z}$.

Occhio al verso: il sottogruppo *più piccolo* corrisponde al numero *multiplo*. Per esempio $6\mathbb{Z}\subseteq 2\mathbb{Z}$ perché $2\mid 6$.

**(b)** $d\mathbb{Z}\cap m\mathbb{Z}=k\mathbb{Z}$: trovare $k$.

*Soluzione (non svolta a lezione):* $k=\operatorname{mcm}(d,m)$. Infatti
$$
x\in d\mathbb{Z}\cap m\mathbb{Z}
\iff d\mid x\ \text{e}\ m\mid x
\iff \operatorname{mcm}(d,m)\mid x
\iff x\in\operatorname{mcm}(d,m)\,\mathbb{Z},
$$
dove il passaggio centrale usa che ogni multiplo comune di $d$ e $m$ è multiplo del loro [[Minimo comune multiplo|minimo comune multiplo]]. Ad esempio $4\mathbb{Z}\cap 6\mathbb{Z}=12\mathbb{Z}$.

## 4. Gruppi ciclici

### 4.1 Potenze di un elemento

Sia $G$ un gruppo e sia $g\in G$. Le potenze intere di $g$ sono definite da
$$
g^0=e,
$$
$$
g^n=\underbrace{g\cdot g\cdots g}_{n\text{ volte}}
\qquad(n>0),
$$
e
$$
g^{-n}=(g^{-1})^n
\qquad(n>0).
$$

Le potenze soddisfano le usuali regole:
$$
g^r g^s=g^{r+s}
\qquad\forall r,s\in\mathbb{Z}.
$$

Se il gruppo è scritto in notazione additiva, alle potenze corrispondono i multipli interi:
$$
ng=\underbrace{g+\cdots+g}_{n\text{ volte}}
$$
per $n>0$, con $0g=0$ e $(-n)g=-(ng)$.

Per esempio, in $(\mathbb{Z},+)$, l’insieme generato da $5$ è
$$
\langle 5\rangle
=
\{m\cdot 5:m\in\mathbb{Z}\}
=
\{\dots,-10,-5,0,5,10,\dots\}.
$$

### 4.2 Sottogruppo generato da un elemento

Il sottogruppo generato da $g\in G$ è
$$
\langle g\rangle
=
\{g^n:n\in\mathbb{Z}\}.
$$

In notazione additiva:
$$
\langle g\rangle
=
\{ng:n\in\mathbb{Z}\}.
$$

L’insieme $\langle g\rangle$ è un sottogruppo di $G$. Infatti:

- non è vuoto, perché
  $$
  g^0=e\in\langle g\rangle;
  $$
- se $g^r,g^s\in\langle g\rangle$, allora
  $$
  g^r(g^s)^{-1}=g^r g^{-s}=g^{r-s}\in\langle g\rangle.
  $$

Quindi il criterio del sottogruppo garantisce che $\langle g\rangle\leq G$. Si chiama **sottogruppo generato da $g$**.

Inoltre $\langle g\rangle$ è sempre **abeliano**, anche se $G$ non lo è:
$$
g^ng^m=g^{n+m}=g^{m+n}=g^mg^n.
$$

**Esempio.** In $(\mathbb{Z}/12\mathbb{Z},+)$:
$$
\langle\overline{3}\rangle=\{n\cdot\overline{3}\}_{n\in\mathbb{Z}}=\{\overline{0},\overline{3},\overline{6},\overline{9}\},
$$
perché $4\cdot\overline{3}=\overline{12}=\overline{0}$ e da lì i multipli si ripetono. Quindi $\overline{3}$ ha ordine $4$.

Il gruppo $G$ si dice **[[Gruppo ciclico|ciclico]]** se esiste un elemento $g\in G$ tale che
$$
G=\langle g\rangle.
$$

In tal caso $g$ si chiama **generatore** di $G$.

Un gruppo ciclico si può scrivere in notazione moltiplicativa come
$$
G=\{\dots,g^{-2},g^{-1},e,g,g^2,\dots\}.
$$

In notazione additiva:
$$
G=\{\dots,-2g,-g,0,g,2g,\dots\}.
$$

### 4.3 Gruppi ciclici finiti e infiniti

Un gruppo ciclico può essere finito oppure infinito.

Se le potenze di $g$ non si ripetono mai, allora $\langle g\rangle$ è infinito. Se invece esiste $m>0$ tale che
$$
g^m=e,
$$
le potenze cominciano a ripetersi:
$$
g^{m+k}=g^k
\qquad\forall k\in\mathbb{Z}.
$$

In questo caso
$$
\langle g\rangle=\{e,g,g^2,\dots,g^{m-1}\}
$$
ed è quindi finito.

L’**[[Ordine di un elemento|ordine]]** di $g$, indicato con $\operatorname{ord}(g)$, è il minimo intero positivo $m$ tale che
$$
g^m=e,
$$
se tale intero esiste. Se non esiste alcun intero positivo con questa proprietà, si dice che $g$ ha ordine infinito. In formule:
$$
\operatorname{ord}(g)=\min\{k>0: g^k=e\},
\qquad
\operatorname{ord}(g)=+\infty\ \text{se tale }k\text{ non esiste}.
$$

> **Osservazione.** Se $\operatorname{ord}(g)=+\infty$, tutte le potenze di $g$ sono distinte, e quindi $\langle g\rangle$ è infinito.
>
> *Dimostrazione.* Se fosse $g^n=g^m$ con $n>m$, moltiplicando per $g^{-m}$ si avrebbe
> $$
> g^{n-m}=e,\qquad n-m>0,
> $$
> contro l’ipotesi che non esista alcun $k>0$ con $g^k=e$. Assurdo.

Se $g$ ha ordine $m$, allora
$$
\langle g\rangle=\{e,g,g^2,\dots,g^{m-1}\}
$$
e
$$
|\langle g\rangle|=m.
$$

Per esempio, il generatore $\zeta=e^{2\pi i/n}$ delle radici $n$-esime dell’unità ha ordine $n$:
$$
\zeta^n=1,
$$
mentre nessuna potenza positiva $\zeta^k$ con $0<k<n$ è uguale a $1$.

### 4.4 Dipendenza dal parametro

La descrizione
$$
\langle g\rangle=\{g^n:n\in\mathbb{Z}\}
$$
usa un parametro intero $n$, ma valori diversi del parametro possono dare lo stesso elemento. In un gruppo finito di ordine $m$ vale infatti
$$
g^{n+m}=g^n.
$$

Per esempio, se $g$ ha ordine $3$, allora
$$
g^0=g^3=g^6=\cdots,
$$
$$
g^1=g^4=g^7=\cdots,
$$
$$
g^2=g^5=g^8=\cdots.
$$

Il parametro $n$ va quindi considerato modulo $m$.

## 5. Il centro di un gruppo

Il **[[Centro di un gruppo|centro]]** di un gruppo $G$ è l’insieme
$$
Z(G)=\{z\in G:zg=gz\ \text{per ogni }g\in G\}.
$$

Gli elementi del centro sono quelli che commutano con tutti gli elementi del gruppo.

Il centro è un sottogruppo di $G$. Per verificarlo:

- $e\in Z(G)$, perché $eg=ge=g$ per ogni $g\in G$;
- se $x,y\in Z(G)$ e $g\in G$, allora
  $$
  (xy)g=x(yg)=x(gy)=(xg)y=(gx)y=g(xy),
  $$
  quindi $xy\in Z(G)$;
- se $x\in Z(G)$, allora per ogni $g\in G$:
  $$
  xg=gx.
  $$
  Moltiplicando opportunamente per $x^{-1}$, si ottiene
  $$
  x^{-1}g=gx^{-1},
  $$
  quindi $x^{-1}\in Z(G)$.

Pertanto
$$
Z(G)\leq G.
$$

Un gruppo abeliano è caratterizzato dalla condizione
$$
Z(G)=G.
$$

Infatti, se $G$ è abeliano, ogni elemento commuta con ogni altro elemento. Viceversa, se ogni elemento appartiene al centro, ogni coppia di elementi commuta.

> [!example] Esempio
> Nel gruppo abeliano $(\mathbb Z/12\mathbb Z,+)$ il centro è tutto il gruppo, perché ogni coppia commuta. In $S_3$ (vedi §6) il centro è invece solo $\{\operatorname{id}\}$: per esempio $(1\ 2\ 3)$ non commuta con $(1\ 2)$, come si calcola nel §6.8.

## 6. Gruppo delle permutazioni

### 6.1 Definizione

Sia $X$ un insieme. Una **[[Gruppo delle permutazioni|permutazione]]** di $X$ è una [[Funzione biettiva|funzione biiettiva]]
$$
\sigma:X\to X.
$$

L’insieme di tutte le permutazioni di $X$ forma un gruppo rispetto alla [[Composizione di funzioni|composizione di funzioni]]. Questo gruppo si indica con
$$
\operatorname{Sym}(X).
$$

Se $X=\{1,2,\dots,n\}$, si usa la notazione
$$
S_n=\operatorname{Sym}(\{1,2,\dots,n\}).
$$

Gli elementi di $S_n$ sono tutte le biiezioni dell’insieme $\{1,\dots,n\}$ in sé.

### 6.2 Struttura di gruppo

L’operazione è la composizione:
$$
\sigma\tau=\sigma\circ\tau.
$$

Per definizione,
$$
(\sigma\tau)(x)=\sigma(\tau(x)).
$$

La composizione si applica quindi da destra verso sinistra: prima si applica $\tau$, poi $\sigma$.

Le proprietà di gruppo sono:

- **chiusura:** la composizione di due biiezioni è ancora una biiezione;
- **associatività:**
  $$
  (\sigma\tau)\rho=\sigma(\tau\rho);
  $$
- **elemento neutro:** la funzione identità
  $$
  \operatorname{id}(x)=x
  \qquad\forall x\in X;
  $$
- **inversi:** ogni permutazione $\sigma$ è biiettiva, quindi ha una [[Funzione inversa|funzione inversa]] $\sigma^{-1}$, con
  $$
  \sigma\sigma^{-1}
  =
  \sigma^{-1}\sigma
  =
  \operatorname{id}.
  $$

L’associatività non richiede un calcolo specifico sulle permutazioni: viene da quella della composizione di funzioni.

Il gruppo $S_n$ è in generale non abeliano per $n\geq 3$. In generale,
$$
\sigma\tau\neq\tau\sigma.
$$

### 6.3 Notazione a due righe

Una permutazione di $\{1,\dots,n\}$ si può scrivere come
$$
\sigma=
\begin{pmatrix}
1&2&\cdots&n\\
\sigma(1)&\sigma(2)&\cdots&\sigma(n)
\end{pmatrix}.
$$

La prima riga elenca gli elementi di partenza, la seconda le rispettive immagini.

Per esempio,
$$
\sigma=
\begin{pmatrix}
1&2&3\\
2&3&1
\end{pmatrix}
$$
significa
$$
\sigma(1)=2,\qquad
\sigma(2)=3,\qquad
\sigma(3)=1.
$$

La stessa permutazione si può scrivere in notazione ciclica come
$$
\sigma=(1\ 2\ 3).
$$

### 6.4 Notazione ciclica

Un ciclo
$$
(a_1\ a_2\ \dots\ a_k)
$$
indica la permutazione definita da
$$
a_1\mapsto a_2,\quad
a_2\mapsto a_3,\quad
\dots,\quad
a_{k-1}\mapsto a_k,\quad
a_k\mapsto a_1,
$$
mentre tutti gli elementi non presenti nel ciclo restano fissi.

Per esempio,
$$
(1\ 3\ 2)
$$
indica
$$
1\mapsto 3,\qquad 3\mapsto 2,\qquad 2\mapsto 1.
$$

Un ciclo di lunghezza $1$ è un punto fisso. Per questo i punti fissi si omettono di solito dalla notazione ciclica.

La stessa permutazione si può rappresentare iniziando il ciclo da un punto diverso:
$$
(1\ 3\ 2)=(3\ 2\ 1)=(2\ 1\ 3).
$$

L’ordine ciclico invece non si può cambiare a piacere:
$$
(1\ 3\ 2)\neq(1\ 2\ 3).
$$

Questi due cicli sono uno l’inverso dell’altro:
$$
(1\ 3\ 2)^{-1}=(2\ 3\ 1)=(1\ 2\ 3).
$$

In generale,
$$
(a_1\ a_2\ \dots\ a_k)^{-1}
=
(a_k\ a_{k-1}\ \dots\ a_2\ a_1).
$$

### 6.5 Composizione di permutazioni

Per calcolare $\sigma\tau$ si applica prima $\tau$ e poi $\sigma$:
$$
(\sigma\tau)(x)=\sigma(\tau(x)).
$$

Per esempio, se
$$
\sigma=(1\ 2\ 3),
\qquad
\tau=(1\ 3\ 2),
$$
si calcolano le immagini dei singoli elementi seguendo l’ordine corretto.

Attenzione a non confondere la composizione con l’ordine in cui sono scritti i simboli: la convenzione usuale è che la permutazione a destra viene applicata per prima.

> [!example] Esempio
> Con $\sigma=(1\ 2\ 3)$ e $\tau=(1\ 3\ 2)$: $1\overset{\tau}{\mapsto}3\overset{\sigma}{\mapsto}1$, $2\overset{\tau}{\mapsto}1\overset{\sigma}{\mapsto}2$, $3\overset{\tau}{\mapsto}2\overset{\sigma}{\mapsto}3$. Quindi $\sigma\tau=\operatorname{id}$, coerentemente con il fatto che i due cicli sono uno l’inverso dell’altro.

> [!warning]
> Il gruppo delle permutazioni non è commutativo. Anche quando $\sigma$ e $\tau$ sono costruite sugli stessi elementi, può succedere che
> $$
> \sigma\tau\neq\tau\sigma.
> $$
> Ogni prodotto va quindi calcolato esplicitamente, applicando prima la permutazione a destra.

### 6.6 Cicli disgiunti

Due cicli si dicono **disgiunti** se non hanno elementi in comune.

Cicli disgiunti commutano. Se $\sigma$ e $\tau$ sono disgiunti, allora
$$
\sigma\tau=\tau\sigma.
$$

Il motivo è che ciascun ciclo agisce su elementi diversi: applicare prima uno o prima l’altro dà lo stesso risultato.

Ogni permutazione si può scrivere come prodotto di cicli disgiunti. Questa decomposizione è essenzialmente unica, a meno dell’ordine dei cicli e della scelta del punto di partenza all’interno di ciascun ciclo.

Se
$$
\sigma=(a_1\ \dots\ a_r)(b_1\ \dots\ b_s)
$$
con i due cicli disgiunti, allora
$$
\sigma^m
=
(a_1\ \dots\ a_r)^m
(b_1\ \dots\ b_s)^m.
$$

L’ordine di un prodotto di cicli disgiunti è il minimo comune multiplo delle lunghezze dei cicli:
$$
\operatorname{ord}(\sigma)
=
\operatorname{mcm}(r,s)
$$
nel caso di due cicli di lunghezze $r$ e $s$.

Più in generale, se
$$
\sigma=\sigma_1\cdots\sigma_t
$$
è la decomposizione in cicli disgiunti e $\sigma_i$ ha lunghezza $r_i$, allora
$$
\operatorname{ord}(\sigma)
=
\operatorname{mcm}(r_1,\dots,r_t).
$$

### 6.7 Cardinalità di $S_n$

Per costruire una permutazione di $\{1,\dots,n\}$:

- l’immagine di $1$ si può scegliere in $n$ modi;
- l’immagine di $2$ nei rimanenti $n-1$ modi;
- l’immagine di $3$ nei rimanenti $n-2$ modi;
- e così via.

Pertanto
$$
|S_n|=n!.
$$

In particolare:
$$
|S_1|=1,\qquad
|S_2|=2,\qquad
|S_3|=6.
$$

Per $n=3$, le permutazioni sono:
$$
\operatorname{id},\quad
(1\ 2),\quad
(1\ 3),\quad
(2\ 3),\quad
(1\ 2\ 3),\quad
(1\ 3\ 2).
$$

Il gruppo $S_3$ è il primo esempio significativo di gruppo non abeliano.

### 6.8 $S(X)$ non è abeliano se $|X|\geq 3$

Negli appunti il gruppo delle permutazioni è indicato con
$$
S(X)=\{f:X\to X\mid f\text{ biiettiva}\}.
$$

> **Proposizione.** Se $|X|\geq 3$, allora $S(X)$ non è abeliano.

Basta trovare due permutazioni che non commutano. Si scelgono tre elementi distinti di $X$, chiamati $1,2,3$, e si considerano permutazioni che fissano tutti gli altri elementi:
$$
\tau_1=(2\ 3),\qquad
\tau_2=(1\ 3),\qquad
\tau_3=(1\ 2),\qquad
\sigma=(1\ 2\ 3).
$$
In notazione a due righe, $\sigma:1\mapsto 2,\ 2\mapsto 3,\ 3\mapsto 1$.

Calcolo di $\sigma\tau_3$ (prima $\tau_3$, poi $\sigma$):
$$
1\overset{\tau_3}{\mapsto}2\overset{\sigma}{\mapsto}3,\qquad
2\overset{\tau_3}{\mapsto}1\overset{\sigma}{\mapsto}2,\qquad
3\overset{\tau_3}{\mapsto}3\overset{\sigma}{\mapsto}1,
$$
quindi $\sigma\tau_3=(1\ 3)=\tau_2$.

Calcolo di $\tau_3\sigma$ (prima $\sigma$, poi $\tau_3$):
$$
1\mapsto 2\mapsto 1,\qquad
2\mapsto 3\mapsto 3,\qquad
3\mapsto 1\mapsto 2,
$$
quindi $\tau_3\sigma=(2\ 3)=\tau_1$.

Poiché $\tau_2\neq\tau_1$, si ha $\sigma\tau_3\neq\tau_3\sigma$: il gruppo non è abeliano. $\blacksquare$

Valgono inoltre
$$
\tau_1^2=\tau_2^2=\tau_3^2=\operatorname{id},
\qquad
\sigma^3=\operatorname{id}.
$$

Ponendo $\tau=\tau_3=(1\ 2)$, tutto $S_3$ si scrive con $\sigma$ e $\tau$:
$$
S_3=\{\operatorname{id},\ \sigma,\ \sigma^2,\ \tau,\ \sigma\tau,\ \tau\sigma\},
$$
con $\sigma^2=(1\ 3\ 2)$, $\sigma\tau=(1\ 3)$, $\tau\sigma=(2\ 3)$. Sono sei elementi distinti, in accordo con $|S_3|=3!=6$.

> [!note]
> Se $|X|\leq 2$, invece, $S(X)$ ha al più $2$ elementi ed è abeliano: l’ipotesi $|X|\geq 3$ è necessaria.

## 7. Collegamento tra gruppi ciclici e permutazioni

Anche un gruppo di permutazioni può contenere sottogruppi ciclici. Se $\sigma\in S_n$, allora
$$
\langle\sigma\rangle
=
\{\sigma^k:k\in\mathbb{Z}\}
$$
è il sottogruppo ciclico generato da $\sigma$.

Se $\sigma$ ha ordine $m$, allora
$$
\langle\sigma\rangle
=
\{\operatorname{id},\sigma,\sigma^2,\dots,\sigma^{m-1}\}.
$$

Per esempio, se
$$
\sigma=(1\ 2\ 3),
$$
allora
$$
\sigma^2=(1\ 3\ 2),
\qquad
\sigma^3=\operatorname{id}.
$$

Di conseguenza,
$$
\langle\sigma\rangle
=
\{\operatorname{id},(1\ 2\ 3),(1\ 3\ 2)\},
$$
che è un sottogruppo ciclico di $S_3$ di ordine $3$.

Le potenze di una permutazione sono quindi un esempio concreto della costruzione generale $\langle g\rangle$.

## 8. Osservazioni metodologiche sulle dimostrazioni

Nelle verifiche di proprietà di gruppo conviene distinguere ciò che va dimostrato da ciò che è già noto per il gruppo ambiente.

Se $H$ è un sottoinsieme di un gruppo $G$ e si vuole provare che $H\leq G$:

1. si può mostrare direttamente che $H$ contiene l’identità, è chiuso rispetto al prodotto e contiene gli inversi;
2. oppure si può usare il criterio più compatto:
   $$
   H\neq\varnothing
   \quad\text{e}\quad
   xy^{-1}\in H
   \quad\forall x,y\in H.
   $$

Per dimostrare un’identità in un gruppo si possono usare le cancellazioni a sinistra e a destra. Se, ad esempio,
$$
ax=ay,
$$
moltiplicando a sinistra per $a^{-1}$ si ottiene
$$
x=y.
$$

Allo stesso modo, da
$$
xa=ya
$$
si ricava $x=y$ moltiplicando a destra per $a^{-1}$.

Bisogna però evitare ragionamenti circolari: quando si dimostra l’esistenza o l’unicità di un inverso, non si può assumere come già dimostrata la proprietà che si sta cercando di ottenere. Si usano solo le proprietà di gruppo già disponibili: associatività, identità e cancellazioni.
