---
type: lecture-note
course: Aritmetica
date: '2026-11-09'
title: Classi laterali e teorema di Lagrange
source_transcript: _transcripts/Aritmetica/2026-11-08 - Classi laterali e teorema di Lagrange.md
source_hash: sha256:c9c5876fe4776d262f6b1259312669943f675b505353d29fb9c8d82e51a4bef6
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-11-08T13:00:05.935Z'
original_date: '2026-11-08'
date_adjustment: Shifted forward one day to keep one note per course and date.
vault_path: Notes/Aritmetica/Lectures/2026-11-09 - Classi laterali e teorema di Lagrange.md
vault_hash: 5a8eddcc7dd155b4dbdd134c78bbb79ca24193f6729d37bc140b7639e8152a21
---

# Classi laterali e teorema di Lagrange

## 1. Generalizzazione delle classi di congruenza

L’obiettivo della lezione è estendere ai gruppi la nozione di [[Classe di congruenza|classe di congruenza]] modulo $n$.

Nel caso additivo di $\mathbb{Z}$, la [[Congruenza modulo n|congruenza modulo $n$]] è descritta dalla condizione

$$
a \equiv b \pmod n
\quad \Longleftrightarrow \quad
a-b \in n\mathbb{Z}.
$$

La differenza $a-b$ corrisponde, nel linguaggio moltiplicativo generale dei gruppi, al prodotto $b^{-1}a$. Per questo, dato un [[Gruppo|gruppo]] $G$ e un [[Sottogruppo|sottogruppo]] $H \leq G$, si considera la relazione

$$
x \sim_H y
\quad \Longleftrightarrow \quad
y^{-1}x \in H.
$$

Questa relazione si chiamerà relazione di equivalenza associata a $H$; le sue classi di equivalenza saranno le **[[Classe laterale|classi laterali]] sinistre** di $H$ in $G$.

> [!warning]
> In un gruppo non abeliano l’ordine dei fattori è essenziale. In generale $y^{-1}x$ e $xy^{-1}$ non coincidono, quindi le classi laterali sinistre e destre vanno trattate separatamente.

---

## 2. La relazione associata a un sottogruppo

Sia $G$ un gruppo e sia $H \leq G$. Definiamo

$$
x \sim_H y
\quad \Longleftrightarrow \quad
y^{-1}x \in H.
$$

Questa è una [[Relazione di equivalenza|relazione di equivalenza]].

### Riflessività

Per ogni $x \in G$,

$$
x^{-1}x=e.
$$

Poiché $e \in H$, segue che $x^{-1}x \in H$, dunque

$$
x \sim_H x.
$$

### Simmetria

Supponiamo che $x \sim_H y$. Allora

$$
y^{-1}x \in H.
$$

Poiché $H$ è un sottogruppo, è chiuso rispetto all’inverso; quindi

$$
(y^{-1}x)^{-1}=x^{-1}y \in H.
$$

Pertanto $y \sim_H x$.

### Transitività

Supponiamo che

$$
x \sim_H y
\qquad\text{e}\qquad
y \sim_H z.
$$

Allora

$$
y^{-1}x \in H,
\qquad
z^{-1}y \in H.
$$

Essendo $H$ chiuso rispetto al prodotto,

$$
(z^{-1}y)(y^{-1}x)
=
z^{-1}(yy^{-1})x
=
z^{-1}x
\in H.
$$

Quindi $x \sim_H z$.

Ne segue che $\sim_H$ è una relazione di equivalenza su $G$.

---

## 3. Classi laterali sinistre

La classe di equivalenza di $x \in G$ è

$$
[x]_H
=
\{y \in G : x \sim_H y\}.
$$

Dalla definizione della relazione,

$$
x \sim_H y
\quad \Longleftrightarrow \quad
y^{-1}x \in H.
$$

La condizione $y^{-1}x \in H$ equivale all’esistenza di un elemento $h \in H$ tale che

$$
y^{-1}x=h.
$$

Moltiplicando a sinistra per $y$ si ottiene

$$
x=yh^{-1}.
$$

Poiché $h$ varia in $H$ esattamente come $h^{-1}$, la classe si può scrivere nella forma

$$
[x]_H=xH=\{xh:h\in H\}.
$$

L’insieme $xH$ si chiama **classe laterale sinistra di $H$ rappresentata da $x$**.

In particolare,

$$
H=eH
$$

è la classe laterale rappresentata dall’identità.

> [!example] Esempio
> In $(\mathbb Z/6\mathbb Z,+)$ prendiamo $H=\{\overline0,\overline3\}$. Le classi laterali (in notazione additiva $x+H$) sono $\{\overline0,\overline3\}$, $\{\overline1,\overline4\}$ e $\{\overline2,\overline5\}$: tre classi di due elementi ciascuna, che partizionano il gruppo. Si ha $\overline1+H=\overline4+H$ perché $\overline4-\overline1=\overline3\in H$.

### Rappresentanti

Un elemento $x \in G$ è un rappresentante della classe laterale $xH$. In realtà tutti gli elementi di $xH$ rappresentano la stessa classe:

$$
xH=yH
\quad\Longleftrightarrow\quad
x\sim_H y.
$$

Quindi non serve passare in rassegna tutti gli elementi della classe: ne basta uno.

### Partizione di $G$

Le classi di equivalenza di una relazione di equivalenza formano una partizione dell’insieme. Pertanto le classi laterali sinistre di $H$:

1. ricoprono tutto $G$;
2. sono a due a due disgiunte oppure coincidono.

Di conseguenza,

$$
G=\bigcup_{x\in R}xH,
$$

dove $R$ è un insieme di rappresentanti distinti delle classi laterali sinistre.

Se due classi laterali hanno un elemento in comune, allora coincidono. Infatti, se

$$
xH\cap yH\neq\varnothing,
$$

esistono $h_1,h_2\in H$ tali che

$$
xh_1=yh_2.
$$

Da questa uguaglianza si ricava che $y^{-1}x\in H$, quindi $xH=yH$.

---

## 4. Cardinalità delle classi laterali

Per ogni $x\in G$, la funzione

$$
\begin{aligned}
f_x:H&\longrightarrow xH\\
h&\longmapsto xh
\end{aligned}
$$

è biiettiva.

- È suriettiva per definizione di $xH$.
- È iniettiva per la legge di cancellazione: se $xh_1=xh_2$, allora
  $$
  h_1=h_2.
  $$

Quindi ogni classe laterale sinistra ha la stessa cardinalità di $H$:

$$
|xH|=|H|.
$$

È il fatto chiave nella dimostrazione del teorema di Lagrange.

> [!warning]
> La legge di cancellazione è essenziale. In un gruppo, da $xh_1=xh_2$ si può cancellare $x$ e concludere $h_1=h_2$. Qui si usa proprio la struttura di gruppo: non è vero in qualunque contesto che si possa semplificare un fattore.

---

## 5. Collegamento con le classi di congruenza modulo $n$

Consideriamo il gruppo additivo $(\mathbb{Z},+)$. Sia

$$
H=n\mathbb{Z}.
$$

La relazione generale diventa

$$
a\sim_H b
\quad\Longleftrightarrow\quad
-b+a=a-b\in n\mathbb{Z}.
$$

Pertanto

$$
a\sim_H b
\quad\Longleftrightarrow\quad
a\equiv b\pmod n.
$$

La classe laterale sinistra di $a$ è

$$
a+n\mathbb{Z}
=
\{a+nk:k\in\mathbb{Z}\},
$$

cioè proprio la classe di congruenza di $a$ modulo $n$.

Nel gruppo additivo $\mathbb{Z}$ non c’è differenza tra classi sinistre e destre, perché l’operazione è commutativa.

---

## 6. Classi laterali destre

Si possono definire anche le **classi laterali destre**. In questo caso si considera la relazione

$$
x\approx_H y
\quad\Longleftrightarrow\quad
xy^{-1}\in H.
$$

La classe di $x$ è

$$
Hx=\{hx:h\in H\}.
$$

Come per le classi sinistre, anche le classi destre formano una partizione di $G$ e hanno tutte la stessa cardinalità di $H$.

In un gruppo abeliano vale sempre

$$
xH=Hx
$$

per ogni $x\in G$. In un gruppo non abeliano, invece, le classi laterali sinistre e destre possono essere diverse.

---

## 7. Il teorema di Lagrange

### Enunciato

Sia $G$ un gruppo finito e sia $H\leq G$. Allora

$$
|H|\mid |G|.
$$

In altre parole, l’ordine di un sottogruppo divide l’ordine del gruppo. È il [[Teorema di Lagrange|teorema di Lagrange]].

Il numero

$$
[G:H]
$$

delle classi laterali sinistre di $H$ in $G$ si chiama **[[Indice di un sottogruppo|indice]] di $H$ in $G$**. Per un gruppo finito vale

$$
[G:H]=\frac{|G|}{|H|}.
$$

Lo slogan del teorema è:

> **L’ordine del sottogruppo divide l’ordine del gruppo.**

### Dimostrazione

Sia $R$ un insieme di rappresentanti distinti delle classi laterali sinistre. Poiché le classi laterali formano una partizione,

$$
G=\bigsqcup_{x\in R}xH,
$$

dove il simbolo $\bigsqcup$ indica unione disgiunta.

Passando alle cardinalità,

$$
|G|
=
\sum_{x\in R}|xH|.
$$

Ogni classe laterale ha la stessa cardinalità di $H$, quindi

$$
|G|
=
\sum_{x\in R}|H|
=
|R|\cdot |H|.
$$

Poiché $|R|=[G:H]$,

$$
|G|=[G:H]\cdot |H|.
$$

Pertanto $|H|$ divide $|G|$.

---

## 8. Conseguenze del teorema di Lagrange

### 8.1 Ordine di un elemento

Sia $x\in G$. Il sottogruppo generato da $x$ è

$$
\langle x\rangle=\{x^k:k\in\mathbb{Z}\}.
$$

Per definizione, l’[[Ordine di un elemento|ordine]] di $x$ è

$$
\operatorname{ord}(x)=|\langle x\rangle|.
$$

Applicando il teorema di Lagrange al sottogruppo $\langle x\rangle$ si ottiene

$$
\operatorname{ord}(x)\mid |G|.
$$

Quindi, in un gruppo finito, l’ordine di ogni elemento divide l’ordine del gruppo.

L’unico elemento di ordine $1$ è l’identità, perché

$$
\operatorname{ord}(x)=1
\quad\Longleftrightarrow\quad
\langle x\rangle=\{e\}
\quad\Longleftrightarrow\quad
x=e.
$$

### 8.2 Ogni elemento elevato all’ordine del gruppo

Se $G$ è finito e $x\in G$, allora

$$
\operatorname{ord}(x)\mid |G|.
$$

Per definizione di ordine di un elemento,

$$
x^{\operatorname{ord}(x)}=e.
$$

Segue quindi che

$$
x^{|G|}=e
\qquad\text{per ogni }x\in G.
$$

È una forma generale del teorema di Fermat.

### 8.3 Gruppi di ordine primo

Sia $G$ un gruppo tale che

$$
|G|=p,
$$

dove $p$ è primo.

Preso un elemento $x\neq e$, il suo ordine è un divisore di $p$. I soli divisori di $p$ sono $1$ e $p$. Poiché $x\neq e$, l’ordine di $x$ non può essere $1$, dunque

$$
\operatorname{ord}(x)=p.
$$

Pertanto

$$
|\langle x\rangle|=p=|G|,
$$

e quindi

$$
\langle x\rangle=G.
$$

Si conclude che ogni gruppo di ordine primo è ciclico.

---

## 9. Teorema di Fermat ed Eulero

Consideriamo il gruppo moltiplicativo delle classi invertibili modulo $m$:

$$
(\mathbb{Z}/m\mathbb{Z})^\times.
$$

È formato dalle classi $[a]$ tali che $\gcd(a,m)=1$, cioè dalle classi che hanno un inverso moltiplicativo modulo $m$.

La sua cardinalità è la funzione di Eulero:

$$
\left|(\mathbb{Z}/m\mathbb{Z})^\times\right|=\varphi(m).
$$

Applicando il teorema di Lagrange, per ogni classe invertibile $[a]$ si ha

$$
\operatorname{ord}([a])\mid \varphi(m),
$$

e quindi

$$
[a]^{\varphi(m)}=[1].
$$

Equivalentemente,

$$
a^{\varphi(m)}\equiv 1\pmod m
\qquad
\text{se }\gcd(a,m)=1.
$$

Questo è il **teorema di Eulero**.

Se $m=p$ è primo, allora

$$
\varphi(p)=p-1,
$$

e si ottiene il **[[Piccolo teorema di Fermat|piccolo teorema di Fermat]]**:

$$
a^{p-1}\equiv 1\pmod p
\qquad
\text{se }p\nmid a.
$$

> [!example] Esempio
> Per $m=9$ si ha $\varphi(9)=6$, e per $a=2$ (coprimo con $9$) il teorema di Eulero dà $2^6=64\equiv1\pmod 9$ (infatti $64=63+1$). Per $p=7$ e $a=3$ il piccolo teorema di Fermat dà $3^6=729\equiv1\pmod7$.

---

## 10. Esempio: il gruppo $S_3$

Il [[Gruppo delle permutazioni|gruppo $S_3$]] delle permutazioni di $\{1,2,3\}$ ha cardinalità

$$
|S_3|=6.
$$

Gli elementi di $S_3$ sono:

- l’identità;
- le tre trasposizioni, di ordine $2$;
- i due cicli di lunghezza $3$, di ordine $3$.

Il gruppo $S_3$ non è abeliano. Inoltre non è ciclico: se lo fosse, essendo di ordine $6$, dovrebbe contenere un elemento di ordine $6$. Ma in $S_3$ gli elementi hanno solo ordine $1$, $2$ oppure $3$.

È coerente con il teorema di Lagrange: gli ordini degli elementi devono dividere $6$.

### Un sottogruppo di ordine $2$

Sia, ad esempio,

$$
H=\{e,\tau\},
$$

dove $\tau$ è una trasposizione. Allora

$$
|H|=2
\qquad\text{e}\qquad
[S_3:H]=\frac{6}{2}=3.
$$

Quindi esistono esattamente tre classi laterali sinistre e tre classi laterali destre.

Le classi laterali sinistre sono del tipo

$$
H,\qquad \sigma H,\qquad \sigma^2H,
$$

dove $\sigma$ è un elemento scelto fuori da $H$ e le classi si ottengono scegliendo ogni volta un rappresentante che non appartenga alle classi già trovate.

Analogamente, le classi laterali destre sono del tipo

$$
H,\qquad H\sigma,\qquad H\sigma^2.
$$

Poiché $S_3$ non è abeliano, può succedere che

$$
\sigma H\neq H\sigma.
$$

Però sia le classi sinistre sia quelle destre sono partizioni di $S_3$ in tre sottoinsiemi di due elementi.

> [!example] Esempio
> Sia $H=\{e,(1\ 2)\}$ e $\sigma=(1\ 2\ 3)$. Componendo da destra a sinistra, $\sigma(1\ 2)=(1\ 3)$ e $(1\ 2)\sigma=(2\ 3)$. Quindi $\sigma H=\{(1\ 2\ 3),(1\ 3)\}$ mentre $H\sigma=\{(1\ 2\ 3),(2\ 3)\}$: le classi sinistra e destra di $\sigma$ sono diverse.

---

## 11. Quando coincidono le classi sinistre e destre?

Per un sottogruppo $H\leq G$, le seguenti condizioni sono equivalenti:

1. per ogni $g\in G$,
   $$
   gH=Hg;
   $$
2. per ogni $g\in G$,
   $$
   gHg^{-1}=H;
   $$
3. per ogni $g\in G$,
   $$
   gHg^{-1}\subseteq H;
   $$
   perché l’inclusione si può applicare anche a $g^{-1}$ per ottenere quella opposta;
4. ogni classe laterale sinistra di $H$ è anche una classe laterale destra, e viceversa.

Quando queste condizioni valgono, $H$ si dice **[[Sottogruppo normale|sottogruppo normale]]** di $G$, e si scrive

$$
H\trianglelefteq G.
$$

La definizione principale è quindi

$$
H\trianglelefteq G
\quad\Longleftrightarrow\quad
gHg^{-1}=H
\quad\text{per ogni }g\in G.
$$

Equivalentemente,

$$
H\trianglelefteq G
\quad\Longleftrightarrow\quad
gH=Hg
\quad\text{per ogni }g\in G.
$$

> [!warning]
> L’uguaglianza $gH=Hg$ è un’uguaglianza tra insiemi. Non vuol dire che ogni $g\in G$ commuti con ogni elemento $h\in H$.

---

## 12. Verifica della normalità tramite inclusioni

Per dimostrare che

$$
gHg^{-1}=H,
$$

spesso basta dimostrare una sola inclusione, ad esempio

$$
gHg^{-1}\subseteq H.
$$

Infatti, sostituendo $g$ con $g^{-1}$ si ottiene

$$
g^{-1}Hg\subseteq H.
$$

Moltiplicando opportunamente a sinistra per $g$ e a destra per $g^{-1}$ si ricava l’inclusione opposta

$$
H\subseteq gHg^{-1}.
$$

Quindi le due inclusioni danno l’uguaglianza.

Per verificare un’inclusione tra insiemi si procede elemento per elemento: si prende un elemento arbitrario dell’insieme a sinistra e si dimostra che sta nell’insieme a destra.

---

## 13. Sottogruppi normali in gruppi abeliani

Se $G$ è abeliano, allora per ogni $g\in G$ e $h\in H$ vale

$$
gh=hg.
$$

Di conseguenza,

$$
gH=Hg
$$

per ogni sottogruppo $H\leq G$. Pertanto:

> **Ogni sottogruppo di un gruppo abeliano è normale.**

Nel caso abeliano, quindi, non c’è differenza tra classi laterali sinistre e destre.

---

## 14. Il centro di un gruppo è normale

Il [[Centro di un gruppo|centro]] di $G$ è

$$
Z(G)=\{x\in G: xg=gx\text{ per ogni }g\in G\}.
$$

Gli elementi del centro commutano con tutti gli elementi del gruppo.

Per dimostrare che $Z(G)$ è normale, si prende $x\in Z(G)$ e $g\in G$. Poiché $x$ commuta con $g$,

$$
gx=xg.
$$

Moltiplicando a destra per $g^{-1}$ si ottiene

$$
gxg^{-1}=x.
$$

Poiché $x\in Z(G)$, segue che

$$
gxg^{-1}\in Z(G).
$$

Quindi

$$
gZ(G)g^{-1}\subseteq Z(G).
$$

Applicando lo stesso ragionamento a $g^{-1}$ si ottiene l’inclusione opposta, dunque

$$
gZ(G)g^{-1}=Z(G).
$$

Pertanto

$$
Z(G)\trianglelefteq G.
$$

---

## 15. Il nucleo di un omomorfismo è normale

Sia

$$
f:G\longrightarrow G'
$$

un [[Omomorfismo|omomorfismo]] di gruppi. Il [[Nucleo|nucleo]] è

$$
\ker(f)=\{x\in G:f(x)=e_{G'}\}.
$$

Il nucleo è già noto essere un sottogruppo di $G$. Per dimostrarne la normalità si prende $k\in\ker(f)$ e $g\in G$. Allora

$$
f(gkg^{-1})
=
f(g)f(k)f(g^{-1}).
$$

Poiché $k\in\ker(f)$,

$$
f(k)=e_{G'}.
$$

Quindi

$$
f(gkg^{-1})
=
f(g)e_{G'}f(g)^{-1}
=
e_{G'}.
$$

Pertanto

$$
gkg^{-1}\in\ker(f),
$$

e si conclude che

$$
g\ker(f)g^{-1}=\ker(f).
$$

Dunque

$$
\ker(f)\trianglelefteq G.
$$

---

## 16. Indice di un sottogruppo

Il numero delle classi laterali sinistre di $H$ in $G$ si chiama **indice** di $H$ in $G$ e si indica con

$$
[G:H].
$$

Se $G$ è finito, il teorema di Lagrange dà

$$
[G:H]=\frac{|G|}{|H|}.
$$

L’indice può anche essere infinito se $G$ è infinito.

Per esempio, nel caso di $S_3$ e di un sottogruppo $H$ di ordine $2$,

$$
[S_3:H]=\frac{6}{2}=3.
$$

Le classi laterali sono quindi tre, ciascuna con due elementi.

---

## 17. Procedura pratica per trovare le classi laterali

Per determinare le classi laterali di $H$ in $G$:

1. si prende la classe laterale dell’identità:
   $$
   H=eH;
   $$
2. si sceglie un elemento $x\notin H$ e si costruisce $xH$;
3. si sceglie un elemento che non appartenga alle classi già trovate;
4. si costruisce la nuova classe laterale;
5. si continua finché tutti gli elementi di $G$ sono stati inclusi.

Non bisogna costruire una nuova classe usando un elemento che sta già in una classe precedente, perché si otterrebbe la stessa classe.

Le classi ottenute sono sempre disgiunte oppure uguali e costituiscono una partizione di $G$.
