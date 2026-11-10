---
type: lecture-note
course: Aritmetica
date: '2026-10-22'
title: Omomorfismi tra anelli e teorema cinese
source_transcript: _transcripts/Aritmetica/2026-10-22 - Omomorfismi tra anelli e teorema cinese.md
source_hash: sha256:f6ec04ec1918c8efb467be582afb3369fba1dd7dbf2bd461846d3f206a1d6265
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-10-22T11:56:46.052Z'
vault_path: Notes/Aritmetica/Lectures/2026-10-22 - Omomorfismi tra anelli e teorema cinese.md
vault_hash: 5131aca5afd55f6abb731311117c12c5bb3fe5226b93f826c45ccd0352e301fc
---

# Omomorfismi tra anelli e teorema cinese

## Omomorfismi: idea generale

Un [[Omomorfismo|omomorfismo]] è una [[Funzione|funzione]] che conserva le operazioni della struttura algebrica considerata. Non c’entra con la composizione di funzioni: l’idea è che l’immagine di un’operazione coincida con l’operazione delle immagini.

Per esempio, per un omomorfismo di gruppi $f\colon G_1\to G_2$ deve valere, per ogni $x,y\in G_1$,

$$
f(x\ast_{G_1} y)=f(x)\ast_{G_2}f(y).
$$

L’operazione a sinistra si fa nel dominio, quella a destra nel codominio.

Per gli [[Spazio vettoriale|spazi vettoriali]], gli omomorfismi sono proprio le applicazioni lineari, perché conservano la somma e la moltiplicazione per scalare.

> [!example] Esempio
> La riduzione $f\colon\mathbb Z\to\mathbb Z/n\mathbb Z$, $f(a)=[a]_n$, è un omomorfismo di anelli: $f(a+b)=[a+b]_n=[a]_n+[b]_n$ e $f(ab)=[ab]_n=[a]_n[b]_n$. Invece $g\colon\mathbb Z\to\mathbb Z$, $g(a)=a+1$, non conserva la somma ($g(a+b)=a+b+1\neq g(a)+g(b)=a+b+2$).

## Omomorfismi di anelli

Siano $A$ e $B$ due [[Anello|anelli]] commutativi. Un omomorfismo di anelli è una funzione

$$
f\colon A\longrightarrow B
$$

che conserva entrambe le operazioni dell’anello:

$$
f(a_1+a_2)=f(a_1)+f(a_2)
$$

e

$$
f(a_1a_2)=f(a_1)f(a_2)
$$

per ogni $a_1,a_2\in A$.

Se si considera anche la struttura unitaria, si richiede inoltre che l’identità moltiplicativa vada nell’identità moltiplicativa:

$$
f(1_A)=1_B.
$$

Quindi un omomorfismo di anelli conserva:

- la somma;
- il prodotto;
- eventualmente, secondo la convenzione adottata, l’elemento neutro moltiplicativo.

In generale, quando si parla di omomorfismo tra strutture algebriche bisogna specificare sia il dominio sia il codominio: le operazioni devono essere quelle appropriate nei due anelli o gruppi coinvolti.

---

## Il prodotto diretto di anelli

Siano $A$ e $B$ due anelli. Sul [[Prodotto cartesiano|prodotto cartesiano]]

$$
A\times B
$$

si definiscono le operazioni componente per componente:

$$
(a,b)+(a',b')=(a+a',b+b')
$$

e

$$
(a,b)(a',b')=(aa',bb').
$$

Con queste operazioni $A\times B$ è un anello (il [[Prodotto diretto|prodotto diretto]]). Allo stesso modo, se $A$ e $B$ sono gruppi, il prodotto cartesiano diventa un gruppo con l’operazione componente per componente.

Per gli anelli di classi di resto si considera quindi

$$
\mathbb Z/m\mathbb Z\times \mathbb Z/n\mathbb Z,
$$

i cui elementi sono coppie

$$
\left(\overline a^{\,m},\overline b^{\,n}\right),
$$

dove $\overline a^{\,m}$ indica la classe di $a$ modulo $m$ e $\overline b^{\,n}$ la classe di $b$ modulo $n$.

La somma è definita da

$$
\left(\overline a^{\,m},\overline b^{\,n}\right)
+
\left(\overline\alpha^{\,m},\overline\beta^{\,n}\right)
=
\left(\overline{a+\alpha}^{\,m},\overline{b+\beta}^{\,n}\right),
$$

mentre il prodotto è

$$
\left(\overline a^{\,m},\overline b^{\,n}\right)
\left(\overline\alpha^{\,m},\overline\beta^{\,n}\right)
=
\left(\overline{a\alpha}^{\,m},\overline{b\beta}^{\,n}\right).
$$

Sono le solite operazioni di $\mathbb Z/m\mathbb Z$ e $\mathbb Z/n\mathbb Z$, applicate separatamente alle due componenti.

> [!example] Esempio
> In $\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z$ si ha $(\overline1^{\,2},\overline2^{\,3})+(\overline1^{\,2},\overline2^{\,3})=(\overline0^{\,2},\overline1^{\,3})$, perché $1+1=2\equiv0\pmod 2$ e $2+2=4\equiv1\pmod 3$.

---

## La mappa naturale

Si considerino due interi positivi $m,n$. È definita la funzione

$$
\varphi\colon \mathbb Z/mn\mathbb Z
\longrightarrow
\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z
$$

ponendo

$$
\varphi\left(\overline x^{\,mn}\right)
=
\left(\overline x^{\,m},\overline x^{\,n}\right).
$$

In altre parole, una classe modulo $mn$ viene mandata nelle due classi che si ottengono riducendo lo stesso intero modulo $m$ e modulo $n$.

È una mappa naturale perché prende un intero $x$ e ne considera contemporaneamente il resto modulo $m$ e il resto modulo $n$.

### Attenzione alla buona definizione

La formula usa un rappresentante $x$ della classe $\overline x^{\,mn}$. Bisogna quindi dimostrare che il risultato non dipende dalla scelta del rappresentante (la [[Buona definizione|buona definizione]]).

Supponiamo che

$$
\overline x^{\,mn}=\overline y^{\,mn}.
$$

Per la caratterizzazione delle congruenze, ciò significa che

$$
mn\mid x-y.
$$

Di conseguenza,

$$
m\mid x-y
\qquad\text{e}\qquad
n\mid x-y.
$$

Pertanto,

$$
\overline x^{\,m}=\overline y^{\,m}
\qquad\text{e}\qquad
\overline x^{\,n}=\overline y^{\,n}.
$$

Quindi

$$
\left(\overline x^{\,m},\overline x^{\,n}\right)
=
\left(\overline y^{\,m},\overline y^{\,n}\right).
$$

La funzione $\varphi$ è dunque ben definita.

> [!warning]
> Anche quando la verifica è semplice, non basta dire che la funzione è "ovviamente" ben definita. La formula è scritta con un rappresentante della classe, quindi l’indipendenza dal rappresentante va dimostrata esplicitamente.

---

## $\varphi$ è un omomorfismo di anelli

Si devono verificare la conservazione della somma e del prodotto.

### Conservazione della somma

Siano $\overline x^{\,mn},\overline y^{\,mn}\in\mathbb Z/mn\mathbb Z$. Allora

$$
\begin{aligned}
\varphi\left(\overline x^{\,mn}+\overline y^{\,mn}\right)
&=
\varphi\left(\overline{x+y}^{\,mn}\right)\\
&=
\left(\overline{x+y}^{\,m},\overline{x+y}^{\,n}\right).
\end{aligned}
$$

D’altra parte,

$$
\begin{aligned}
\varphi\left(\overline x^{\,mn}\right)
+
\varphi\left(\overline y^{\,mn}\right)
&=
\left(\overline x^{\,m},\overline x^{\,n}\right)
+
\left(\overline y^{\,m},\overline y^{\,n}\right)\\
&=
\left(\overline x^{\,m}+\overline y^{\,m},
\overline x^{\,n}+\overline y^{\,n}\right)\\
&=
\left(\overline{x+y}^{\,m},\overline{x+y}^{\,n}\right).
\end{aligned}
$$

Pertanto,

$$
\varphi\left(\overline x^{\,mn}+\overline y^{\,mn}\right)
=
\varphi\left(\overline x^{\,mn}\right)
+
\varphi\left(\overline y^{\,mn}\right).
$$

### Conservazione del prodotto

Allo stesso modo,

$$
\begin{aligned}
\varphi\left(\overline x^{\,mn}\cdot\overline y^{\,mn}\right)
&=
\varphi\left(\overline{xy}^{\,mn}\right)\\
&=
\left(\overline{xy}^{\,m},\overline{xy}^{\,n}\right),
\end{aligned}
$$

mentre

$$
\begin{aligned}
\varphi\left(\overline x^{\,mn}\right)
\varphi\left(\overline y^{\,mn}\right)
&=
\left(\overline x^{\,m},\overline x^{\,n}\right)
\left(\overline y^{\,m},\overline y^{\,n}\right)\\
&=
\left(\overline{xy}^{\,m},\overline{xy}^{\,n}\right).
\end{aligned}
$$

Quindi

$$
\varphi\left(\overline x^{\,mn}\cdot\overline y^{\,mn}\right)
=
\varphi\left(\overline x^{\,mn}\right)
\varphi\left(\overline y^{\,mn}\right).
$$

La funzione $\varphi$ è dunque un omomorfismo di anelli:

$$
\varphi\colon \mathbb Z/mn\mathbb Z
\longrightarrow
\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z.
$$

---

## Il teorema cinese del resto

### Enunciato

La mappa naturale

$$
\varphi\colon \mathbb Z/mn\mathbb Z
\longrightarrow
\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z,
\qquad
\overline x^{\,mn}\longmapsto
\left(\overline x^{\,m},\overline x^{\,n}\right)
$$

è un [[Isomorfismo|isomorfismo]] di anelli se e solo se $m$ e $n$ sono primi tra loro, cioè

$$
\gcd(m,n)=1.
$$

Equivalentemente, se $\gcd(m,n)=1$, allora per ogni coppia di classi

$$
\left(\overline a^{\,m},\overline b^{\,n}\right)
\in
\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z
$$

esiste un’unica classe $\overline x^{\,mn}$ tale che

$$
x\equiv a\pmod m,
\qquad
x\equiv b\pmod n.
$$

In forma di sistema di congruenze:

$$
\begin{cases}
x\equiv a\pmod m,\\
x\equiv b\pmod n.
\end{cases}
$$

Se $m$ e $n$ sono coprimi, il sistema ha sempre una soluzione, unica modulo $mn$.

---

### Dimostrazione della sufficienza

Supponiamo che

$$
\gcd(m,n)=1.
$$

Vogliamo dimostrare che $\varphi$ è un isomorfismo. Siccome $\varphi$ è già un omomorfismo, basta dimostrare che è biiettiva.

#### Suriettività

Prendiamo un elemento arbitrario del codominio:

$$
\left(\overline a^{\,m},\overline b^{\,n}\right).
$$

Dobbiamo mostrare che esiste una classe $\overline x^{\,mn}$ tale che

$$
\varphi\left(\overline x^{\,mn}\right)
=
\left(\overline a^{\,m},\overline b^{\,n}\right).
$$

Questo equivale a trovare un intero $x$ che soddisfi

$$
\begin{cases}
x\equiv a\pmod m,\\
x\equiv b\pmod n.
\end{cases}
$$

Poiché $\gcd(m,n)=1$, per Bézout esistono $u,v\in\mathbb Z$ tali che

$$
um+vn=1.
$$

Una soluzione esplicita è

$$
x=b um+a vn.
$$

Infatti, modulo $m$ si ha

$$
x=b um+a vn\equiv 0+a\cdot 1\equiv a\pmod m,
$$

perché $um\equiv 0\pmod m$ e $vn\equiv 1\pmod m$.

Analogamente, modulo $n$,

$$
x=b um+a vn\equiv b\cdot 1+0\equiv b\pmod n.
$$

Quindi

$$
\varphi\left(\overline x^{\,mn}\right)
=
\left(\overline a^{\,m},\overline b^{\,n}\right).
$$

La funzione $\varphi$ è suriettiva.

#### Unicità modulo $mn$

Se $x$ e $y$ sono due soluzioni dello stesso sistema, allora

$$
x\equiv y\pmod m
\qquad\text{e}\qquad
x\equiv y\pmod n.
$$

Quindi

$$
m\mid x-y
\qquad\text{e}\qquad
n\mid x-y.
$$

Poiché $m$ e $n$ sono coprimi, segue che

$$
mn\mid x-y.
$$

Pertanto,

$$
x\equiv y\pmod{mn}.
$$

La soluzione è unica modulo $mn$.

Questo dimostra direttamente l’iniettività. In alternativa, si può usare il fatto che dominio e codominio sono insiemi finiti con lo stesso numero di elementi:

$$
\left|\mathbb Z/mn\mathbb Z\right|=mn
$$

e

$$
\left|\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\right|
=
m\cdot n=mn.
$$

Una funzione tra due insiemi finiti della stessa cardinalità è suriettiva se e solo se è iniettiva. Dunque, dimostrata la suriettività, si ottiene anche la biiettività.

---

### Dimostrazione della necessità

Supponiamo ora che $\varphi$ sia suriettiva. Vogliamo dimostrare che

$$
\gcd(m,n)=1.
$$

Consideriamo nel codominio l’elemento

$$
\left(\overline 0^{\,m},\overline 1^{\,n}\right).
$$

Per la suriettività esiste una classe $\overline x^{\,mn}$ tale che

$$
\varphi\left(\overline x^{\,mn}\right)
=
\left(\overline 0^{\,m},\overline 1^{\,n}\right).
$$

Per la definizione di $\varphi$, questo significa che

$$
\overline x^{\,m}=\overline 0^{\,m}
\qquad\text{e}\qquad
\overline x^{\,n}=\overline 1^{\,n}.
$$

In termini di congruenze:

$$
x\equiv 0\pmod m,
\qquad
x\equiv 1\pmod n.
$$

La prima congruenza implica che $m\mid x$. Se $d$ è un divisore comune di $m$ e $n$, allora $d\mid x$ e, dalla seconda congruenza, $x-1$ è divisibile per $n$, dunque anche per $d$. Ne segue che $d$ divide sia $x$ sia $x-1$, quindi divide la differenza:

$$
x-(x-1)=1.
$$

Pertanto $d=1$. Ogni divisore comune di $m$ e $n$ è uguale a $1$, perciò

$$
\gcd(m,n)=1.
$$

Quindi la suriettività di $\varphi$ implica che $m$ e $n$ siano coprimi.

---

## Esempio: il caso modulo $6$

Poiché

$$
6=2\cdot 3
\qquad\text{e}\qquad
\gcd(2,3)=1,
$$

il teorema cinese fornisce un isomorfismo

$$
\mathbb Z/6\mathbb Z
\cong
\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z.
$$

La mappa è

$$
\varphi\colon \mathbb Z/6\mathbb Z
\longrightarrow
\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z,
\qquad
\overline x^{\,6}
\longmapsto
\left(\overline x^{\,2},\overline x^{\,3}\right).
$$

Gli elementi di $\mathbb Z/6\mathbb Z$ sono

$$
\overline 0^{\,6},
\overline 1^{\,6},
\overline 2^{\,6},
\overline 3^{\,6},
\overline 4^{\,6},
\overline 5^{\,6}.
$$

Le immagini sono:

$$
\begin{array}{c|c}
\text{Classe modulo }6 & \text{Immagine in } \mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z\\
\hline
\overline 0^{\,6} & \left(\overline 0^{\,2},\overline 0^{\,3}\right)\\
\overline 1^{\,6} & \left(\overline 1^{\,2},\overline 1^{\,3}\right)\\
\overline 2^{\,6} & \left(\overline 0^{\,2},\overline 2^{\,3}\right)\\
\overline 3^{\,6} & \left(\overline 1^{\,2},\overline 0^{\,3}\right)\\
\overline 4^{\,6} & \left(\overline 0^{\,2},\overline 1^{\,3}\right)\\
\overline 5^{\,6} & \left(\overline 1^{\,2},\overline 2^{\,3}\right)
\end{array}
$$

Per esempio,

$$
\overline 4^{\,6}
\longmapsto
\left(\overline 4^{\,2},\overline 4^{\,3}\right)
=
\left(\overline 0^{\,2},\overline 1^{\,3}\right).
$$

Il fatto che tutti i resti modulo $2$ e modulo $3$ si combinino in modo unico è esattamente la biiettività della mappa.

### Interpretazione tramite i resti

Un intero della forma $6k$ ha resto $0$ sia modulo $2$ sia modulo $3$.

Un intero della forma $6k+1$ ha resto $1$ sia modulo $2$ sia modulo $3$.

Un intero della forma $6k+2$ ha resto $0$ modulo $2$ e resto $2$ modulo $3$.

Un intero della forma $6k+3$ ha resto $1$ modulo $2$ e resto $0$ modulo $3$.

Un intero della forma $6k+4$ ha resto $0$ modulo $2$ e resto $1$ modulo $3$.

Un intero della forma $6k+5$ ha resto $1$ modulo $2$ e resto $2$ modulo $3$.

Queste sei possibilità sono tutte le coppie possibili di resti modulo $2$ e modulo $3$.

---

## Perché la coprimalità è essenziale

Se $m$ e $n$ non sono coprimi, non tutte le coppie di classi possono essere realizzate.

Per esempio, consideriamo il sistema

$$
\begin{cases}
x\equiv 0\pmod 2,\\
x\equiv 1\pmod 4.
\end{cases}
$$

La prima congruenza richiede che $x$ sia pari, la seconda richiede che $x$ sia dispari. Il sistema è impossibile.

Di conseguenza la mappa

$$
\mathbb Z/8\mathbb Z
\longrightarrow
\mathbb Z/2\mathbb Z\times\mathbb Z/4\mathbb Z
$$

non è suriettiva, perché la coppia

$$
\left(\overline 0^{\,2},\overline 1^{\,4}\right)
$$

non sta nell’immagine.

La coprimalità non è quindi un dettaglio tecnico: è proprio ciò che garantisce che le condizioni modulo $m$ e modulo $n$ siano compatibili per ogni scelta dei resti.

---

## Passaggio dai gruppi additivi ai gruppi moltiplicativi

Per ogni $m$ si considera il gruppo moltiplicativo delle classi invertibili modulo $m$:

$$
\left(\mathbb Z/m\mathbb Z\right)^\times.
$$

È formato dalle classi $\overline x^{\,m}$ tali che $x$ sia coprimo con $m$:

$$
\left(\mathbb Z/m\mathbb Z\right)^\times
=
\left\{
\overline x^{\,m}\in\mathbb Z/m\mathbb Z
:
\gcd(x,m)=1
\right\}.
$$

L’operazione è il prodotto delle classi:

$$
\overline x^{\,m}\cdot\overline y^{\,m}
=
\overline{xy}^{\,m}.
$$

L’elemento neutro è $\overline 1^{\,m}$.

La mappa $\varphi$ induce, quando $\gcd(m,n)=1$, una mappa tra i gruppi moltiplicativi:

$$
\varphi^\times\colon
\left(\mathbb Z/mn\mathbb Z\right)^\times
\longrightarrow
\left(\mathbb Z/m\mathbb Z\right)^\times
\times
\left(\mathbb Z/n\mathbb Z\right)^\times
$$

definita da

$$
\varphi^\times\left(\overline x^{\,mn}\right)
=
\left(\overline x^{\,m},\overline x^{\,n}\right).
$$

È la restrizione di $\varphi$ al sottoinsieme degli elementi invertibili, con codominio ristretto al prodotto dei gruppi di elementi invertibili.

### La mappa è ben definita sul gruppo moltiplicativo

Se $\overline x^{\,mn}$ è invertibile, allora

$$
\gcd(x,mn)=1.
$$

In particolare $x$ è coprimo sia con $m$ sia con $n$:

$$
\gcd(x,m)=1,
\qquad
\gcd(x,n)=1.
$$

Quindi le classi $\overline x^{\,m}$ e $\overline x^{\,n}$ sono invertibili, e l’immagine sta davvero nel codominio scelto.

La restrizione conserva il prodotto perché $\varphi$ lo conserva già su tutto l’anello:

$$
\begin{aligned}
\varphi^\times\left(\overline x^{\,mn}\overline y^{\,mn}\right)
&=
\varphi^\times\left(\overline{xy}^{\,mn}\right)\\
&=
\left(\overline{xy}^{\,m},\overline{xy}^{\,n}\right)\\
&=
\left(\overline x^{\,m},\overline x^{\,n}\right)
\left(\overline y^{\,m},\overline y^{\,n}\right).
\end{aligned}
$$

Quindi $\varphi^\times$ è un omomorfismo di gruppi.

---

## Teorema cinese per gli elementi invertibili

Se $\gcd(m,n)=1$, la restrizione induce un isomorfismo di gruppi

$$
\left(\mathbb Z/mn\mathbb Z\right)^\times
\cong
\left(\mathbb Z/m\mathbb Z\right)^\times
\times
\left(\mathbb Z/n\mathbb Z\right)^\times.
$$

Per dimostrare la suriettività, prendiamo

$$
\left(\overline a^{\,m},\overline b^{\,n}\right)
\in
\left(\mathbb Z/m\mathbb Z\right)^\times
\times
\left(\mathbb Z/n\mathbb Z\right)^\times.
$$

Quindi

$$
\gcd(a,m)=1
\qquad\text{e}\qquad
\gcd(b,n)=1.
$$

Per il teorema cinese esiste un intero $x$ tale che

$$
x\equiv a\pmod m,
\qquad
x\equiv b\pmod n.
$$

Da queste congruenze segue

$$
\gcd(x,m)=1
\qquad\text{e}\qquad
\gcd(x,n)=1.
$$

Poiché $m$ e $n$ sono coprimi, si ottiene

$$
\gcd(x,mn)=1.
$$

Pertanto $\overline x^{\,mn}$ è invertibile e

$$
\varphi^\times\left(\overline x^{\,mn}\right)
=
\left(\overline a^{\,m},\overline b^{\,n}\right).
$$

La mappa è quindi suriettiva. Anche l’iniettività segue dal teorema cinese, oppure dal fatto che è la restrizione di un isomorfismo di anelli.

### Esempio nel caso modulo $6$

Gli elementi invertibili modulo $6$ sono

$$
\left(\mathbb Z/6\mathbb Z\right)^\times
=
\left\{\overline 1^{\,6},\overline 5^{\,6}\right\}.
$$

Infatti $1$ e $5$ sono gli unici resti tra $0$ e $5$ coprimi con $6$.

D’altra parte,

$$
\left(\mathbb Z/2\mathbb Z\right)^\times
=
\left\{\overline 1^{\,2}\right\}
$$

e

$$
\left(\mathbb Z/3\mathbb Z\right)^\times
=
\left\{\overline 1^{\,3},\overline 2^{\,3}\right\}.
$$

Il prodotto ha quindi gli elementi

$$
\left(\overline 1^{\,2},\overline 1^{\,3}\right),
\qquad
\left(\overline 1^{\,2},\overline 2^{\,3}\right).
$$

La restrizione della mappa è

$$
\overline 1^{\,6}
\longmapsto
\left(\overline 1^{\,2},\overline 1^{\,3}\right)
$$

e

$$
\overline 5^{\,6}
\longmapsto
\left(\overline 1^{\,2},\overline 2^{\,3}\right).
$$

Quindi

$$
\left(\mathbb Z/6\mathbb Z\right)^\times
\cong
\left(\mathbb Z/2\mathbb Z\right)^\times
\times
\left(\mathbb Z/3\mathbb Z\right)^\times.
$$

---

## Isomorfismo e nomi degli elementi

Un isomorfismo non richiede che gli elementi dei due oggetti abbiano lo stesso nome o siano letteralmente gli stessi. Richiede che esista una corrispondenza biiettiva che conservi le operazioni.

Per esempio, gli elementi di $\mathbb Z/6\mathbb Z$ sono classi modulo $6$, mentre gli elementi di

$$
\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z
$$

sono coppie di classi. Gli oggetti sono costruiti in modo diverso e i loro elementi hanno un altro aspetto, ma come anelli sono isomorfi quando $2$ e $3$ sono coprimi.

Cambiare i nomi degli elementi non cambia la struttura: contano le operazioni e il modo in cui gli elementi interagiscono tramite esse.
