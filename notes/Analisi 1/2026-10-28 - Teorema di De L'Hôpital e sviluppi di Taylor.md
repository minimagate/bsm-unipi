---
type: lecture-note
course: Analisi 1
date: '2026-10-28'
title: Teorema di De L'Hôpital e sviluppi di Taylor
source_files:
- AM1_26_L027.pdf
- AM1_26_L028.pdf
source_date: '2025-10-27'
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Analisi 1/Lectures/2026-10-28 - Teorema di De L'Hôpital e sviluppi di Taylor.md
vault_hash: d895cf850eae6a653522fbfd7f933e0d70cfc8a1b35a0cacdff5e9b9f387ca5c
---

# Teorema di De L'Hôpital e sviluppi di Taylor

Questa nota riunisce le due parti **027 e 028** della stessa lezione e prosegue [[2026-10-27 - Derivate, differenziabilità e regole di derivazione]]. La prima parte presenta il **[[Teorema di De L'Hôpital|teorema di De L'Hôpital]]** (enunciato senza dimostrazione, «teorema misterioso»), soprattutto attraverso i modi in cui **non** va usato. La seconda parte introduce i polinomi di **[[Sviluppo di Taylor|Taylor–McLaurin]]** con resto di Peano, ne dimostra l'unicità e ricava gli sviluppi delle funzioni elementari, che generalizzano quelli di [[2026-10-26 - Simboli di Landau, o piccolo e sviluppi dei limiti notevoli]].

## 1. Il teorema di De L'Hôpital

Riguarda limiti del tipo

$$
\lim_{x\to x_0}\frac{f(x)}{g(x)},\qquad x_0\in\overline{\mathbb R}\quad(\text{anche }x_0^+\text{ e }x_0^-).
$$

**Teorema (De L'Hôpital, «teorema misterioso»).** Supponiamo che

1. **un po' di burocrazia**: $f$ e $g$ siano definite dove serve, le [[Derivata|derivate]] esistano, si possa dividere (vedi il non esempio 3 per cosa vuol dire «dove serve»);
2. il limite sia una **[[Forma indeterminata|forma indeterminata]]** $\frac00$ oppure $\frac{\pm\infty}{\pm\infty}$, cioè
   $$
   \lim_{x\to x_0}f(x)=\lim_{x\to x_0}g(x)=0
   \qquad\text{oppure}\qquad
   \lim_{x\to x_0}f(x)=\lim_{x\to x_0}g(x)=+\infty
   $$
   (gli eventuali segni si portano fuori). Nel caso $\frac\infty\infty$ in realtà **basta che diverga il denominatore**;
3. esista
   $$
   \lim_{x\to x_0}\frac{f'(x)}{g'(x)}=\ell\in\overline{\mathbb R}
   $$
   (cioè siamo in una delle prime tre possibilità: limite finito, $+\infty$, $-\infty$).

Allora

$$
\boxed{\lim_{x\to x_0}\frac{f(x)}{g(x)}=\ell}\qquad\text{(lo stesso }\ell\text{)}.
$$

**Uso operativo.** Devo calcolare $\lim\frac{f}{g}$ e non ci riesco. Controllo che sia del tipo previsto e provo a calcolare $\lim\frac{f'}{g'}$:

1. se questo esiste in $\overline{\mathbb R}$, ho finito;
2. se **non esiste**, il teorema non dice nulla («BOH»);
3. se è ancora indeterminato, posso iterare e calcolare $\lim\frac{f''}{g''}$, e così via (ogni volta ricontrollando le ipotesi).

### 1.1 Tre non esempi

**Non esempio 1: manca la forma indeterminata.**

$$
\lim_{x\to0}\frac{\cos x}{x}\ \overset{?}{=}\ \lim_{x\to0}\frac{-\sin x}{1}=0.\qquad\textbf{No!}
$$

Il numeratore tende a $1$: non è una forma indeterminata. In realtà il limite **non esiste**, perché

$$
\lim_{x\to0^+}\frac{\cos x}x=+\infty,\qquad\lim_{x\to0^-}\frac{\cos x}x=-\infty.
$$

*(Negli appunti la derivata del numeratore è scritta $\sin x$; il segno non cambia la conclusione, che comunque è sbagliata.)*

**Non esempio 2: il limite delle derivate non esiste.**

$$
\lim_{x\to+\infty}\frac{2x+\sin x}{x}\qquad\left[\tfrac{+\infty}{+\infty}\right]
\qquad\leadsto\qquad
\lim_{x\to+\infty}\frac{2+\cos x}{1}\ \text{non esiste}.
$$

Da qui **non** si conclude che il limite di partenza non esiste: se $\lim\frac{f'}{g'}$ non esiste, il teorema tace. In realtà il limite vale $2$, per il [[Teorema dei carabinieri|teorema dei carabinieri]]:

$$
\frac{2x-1}{x}\le\frac{2x+\sin x}{x}\le\frac{2x+1}{x}\qquad(x>0),
$$

e i due estremi tendono a $2$.

**Non esempio 3: la «burocrazia» conta.** Sia $f(x)=\lfloor x\rfloor$ la parte intera, considerata su $(0,+\infty)\setminus\mathbb N$, dove è costante a tratti e quindi derivabile con $f'(x)=0$ in ogni punto in cui è definita. Allora sembrerebbe

$$
\lim_{x\to+\infty}\frac{f(x)}{x}\ \left[\tfrac{+\infty}{+\infty}\right]\ \overset{?}{=}\ \lim_{x\to+\infty}\frac{f'(x)}1=0.
$$

D'altra parte $\frac{x-1}{x}\le\frac{f(x)}{x}\le\frac xx$, quindi per i carabinieri il limite è $1$. **No!** Se faccio il limite per $x\to+\infty$, $f$ e $g$ devono essere definite (e derivabili) almeno in una **semiretta** $(M,+\infty)$; se lo faccio per $x\to0^+$ devono esserlo almeno in $(0,\delta)$ con $\delta>0$; e così via. Qui il dominio è bucato in ogni intero, quindi non contiene nessuna semiretta.

### 1.2 Utilità pratica

Nella pratica De L'Hôpital serve poco (secondo gli appunti, circa il **3%** dei casi): derivando, le funzioni spesso «peggiorano» e si rischia di finire con limiti più complicati di quello iniziale. Quasi sempre c'è una strada alternativa.

**Esempio 1.** $\displaystyle\lim_{x\to+\infty}x\left(\frac\pi2-\arctan x\right)$, forma $+\infty\cdot0$. Riscrivo come quoziente:

$$
\lim_{x\to+\infty}\frac{\frac\pi2-\arctan x}{\frac1x}
\ \overset{[\frac00]\ \text{H}}{=}\
\lim_{x\to+\infty}\frac{-\frac1{1+x^2}}{-\frac1{x^2}}
=\lim_{x\to+\infty}\frac{x^2}{1+x^2}=1.
$$

*Alternativa.* Per ogni $x>0$ vale $\arctan x+\arctan\frac1x=\frac\pi2$, quindi, con $y=\frac1x\to0^+$,

$$
\lim_{x\to+\infty}x\left(\frac\pi2-\arctan x\right)=\lim_{x\to+\infty}\frac{\arctan\frac1x}{\frac1x}=\lim_{y\to0^+}\frac{\arctan y}{y}=1.
$$

**Esempio 2.** $\displaystyle\lim_{x\to0^+}\frac{\arccos(1-x)}{\sqrt x}$, forma $\frac00$ (perché $\arccos1=0$). Con De L'Hôpital, ricordando $(\arccos t)'=-\frac1{\sqrt{1-t^2}}$:

$$
\lim_{x\to0^+}\frac{-\frac{1}{\sqrt{1-(1-x)^2}}\cdot(-1)}{\frac1{2\sqrt x}}
=\lim_{x\to0^+}\frac{2\sqrt x}{\sqrt{2x-x^2}}
=\lim_{x\to0^+}\frac{2}{\sqrt{2-x}}=\sqrt2.
$$

**N.B.** Questo dice che, per $x\to0^+$ (equivalenza asintotica, vedi [[Equivalenza asintotica]]),

$$
\boxed{\arccos(1-x)\sim\sqrt{2x}},\qquad\text{cioè}\qquad\arccos(1-x)=\sqrt{2x}+o(\sqrt x).
$$

*Alternativa.* Pongo $y=\arccos(1-x)$, così $y\to0^+$, $\cos y=1-x$ e $x=1-\cos y$. Il limite diventa

$$
\lim_{y\to0^+}\frac{y}{\sqrt{1-\cos y}}=\lim_{y\to0^+}\sqrt{\frac{y^2}{1-\cos y}}=\sqrt2,
$$

usando il [[Limiti notevoli|limite notevole]] $\frac{1-\cos y}{y^2}\to\frac12$ (e $y>0$ per portare $y$ dentro la radice).

### 1.3 L'esempio

$$
\lim_{x\to0}\frac{e^x-\cos x-\sin x+x^2}{x^2}
$$

Il valore corretto è $\mathbf 2$. Gli appunti lo affrontano in tre modi, di cui i primi due sono sbagliati.

**1° modo: limiti notevoli (sbagliato).** Si aggiunge e toglie $1$ e si raccoglie $x$:

$$
\frac{e^x-1+1-\cos x-\sin x+x^2}{x^2}
=\frac{x\Bigl(\underbrace{\tfrac{e^x-1}{x}}_{\to1}+\underbrace{\tfrac{1-\cos x}{x^2}\,x}_{\to\frac12\cdot0=0}-\underbrace{\tfrac{\sin x}{x}}_{\to1}\Bigr)+x^2}{x^2}
\ \overset{?}{=}\ \frac{x^2}{x^2}\to1.
$$

**No! Non si fanno i limiti metà per volta.** Sostituire la parentesi con il suo limite $0$ mentre il resto della frazione dipende ancora da $x$ butta via esattamente l'informazione che serve: la parentesi tende a $0$, ma conta **quanto velocemente**, perché è moltiplicata per $x$ e divisa per $x^2$.

**2° modo: equivalenza asintotica (sbagliato).** Usando $e^x\sim1+x$, $\cos x\sim1-\frac{x^2}2$, $\sin x\sim x$:

$$
\frac{1+x-1+\frac{x^2}2-x+x^2}{x^2}=\frac{\frac32x^2}{x^2}\ \overset{?}{\to}\ \frac32.\qquad\text{OPS}
$$

**No! Non si usa l'equivalenza asintotica** dentro le somme: $\sim$ si comporta bene con prodotti e quozienti, non con somme e differenze (vedi [[2026-10-26 - Simboli di Landau, o piccolo e sviluppi dei limiti notevoli]]).

**3° modo: De L'Hôpital (corretto).** È del tipo $\frac00$, quindi va bene:

$$
\lim_{x\to0}\frac{e^x+\sin x-\cos x+2x}{2x}
\ \overset{[\frac00]\ \text{H}}{=}\
\lim_{x\to0}\frac{e^x+\cos x+\sin x+2}{2}=\frac42=2.
$$

Gli appunti commentano «DOPPIO OPS»: i primi due modi davano $1$ e $\frac32$, entrambi sbagliati.

**Oss. (dove si rompe il 2° modo).** Se si scrive l'o piccolo invece di $\sim$, ci si accorge del problema:

$$
\frac{e^x-\cos x-\sin x+x^2}{x^2}
=\frac{1+x+o(x)-1+\frac{x^2}2+o(x^2)-x-o(x)+x^2}{x^2}.
$$

Quello che resta contiene $\dfrac{o(x)}{x^2}$, cioè «$\frac{o(x)}{o(x)}$»: non si sa dire nulla («BOH»). Gli sviluppi di $e^x$ e $\sin x$ usati erano troppo poco precisi: servono fino all'ordine $x^2$, e lo si fa nella sezione 4.

**Oss. (ragionamento circolare).** Si può calcolare $\displaystyle\lim_{x\to0}\frac{\sin x}x$ con De L'Hôpital? **No!** Servirebbe sapere che $(\sin x)'=\cos x$, ma per dimostrarlo abbiamo usato proprio quel limite notevole (vedi la sezione sulle derivate elementari in [[2026-10-27 - Derivate, differenziabilità e regole di derivazione]]).

## 2. Il problema di Taylor–McLaurin

**Setting.** $f(x)$ funzione definita in un intorno di $0$, $n$ intero positivo.

**Problema.** Trovare un polinomio $P_n(x)$, di grado $\le n$, tale che

$$
\boxed{f(x)=P_n(x)+o(x^n)\qquad\text{per }x\to0.}
$$

Il termine $o(x^n)$ si chiama **resto di Peano**.

In parole: voglio approssimare $f$ con un polinomio, pagando come errore un $o(x^n)$ (si veda [[Simboli di Landau]]). È inutile considerare gradi $>n$, perché quei termini sarebbero comunque mangiati dall'o piccolo.

**Lemma (unicità).** Se $P_n$ esiste, allora è unico.

*Dimostrazione.* Supponiamo che ce ne siano due:

$$
f(x)=P_n(x)+o(x^n),\qquad f(x)=\widehat P_n(x)+o(x^n).
$$

Facendo la differenza, $P_n(x)-\widehat P_n(x)=o(x^n)$. Supponiamo [[Dimostrazione per assurdo|per assurdo]] che $P_n-\widehat P_n$ non sia il polinomio nullo. Allora ha un termine di grado minimo:

$$
o(x^n)=P_n(x)-\widehat P_n(x)=a_kx^k+\dots\qquad\text{con }a_k\neq0,\ 0\le k\le n.
$$

Divido per $x^k$ e passo al limite per $x\to0$: a destra resta $a_k$ (gli altri termini hanno grado $>k$ e tendono a $0$), a sinistra $\frac{o(x^n)}{x^k}\to0$ perché $k\le n$. Viene $0=a_k$, assurdo. $\square$

## 3. Teorema di Taylor–Peano

**Teorema («misterioso», Taylor–Peano).** Sia $\delta>0$, $f:(-\delta,\delta)\to\mathbb R$, $n\in\mathbb N$. Supponiamo che

1. $f$ sia derivabile almeno $n-1$ volte in $(-\delta,\delta)$;
2. $f$ sia derivabile $n$ volte in $x=0$ (se è derivabile $n$ volte anche altrove, meglio).

Allora $P_n$ esiste ed è dato da

$$
\boxed{P_n(x)=f(0)+f'(0)\,x+\frac{f''(0)}{2!}x^2+\frac{f'''(0)}{3!}x^3+\dots+\frac{f^{(n)}(0)}{n!}x^n=\sum_{k=0}^n\frac{f^{(k)}(0)}{k!}x^k,}
$$

dove $f^{(k)}$ è la derivata $k$-esima di $f$ (con $f^{(0)}=f$).

**Oss. (sufficiente, non necessaria).** Il teorema dà una condizione **sufficiente ma non necessaria**: esistono funzioni che hanno $P_{40}(x)$, anzi lo hanno per ogni $n\in\mathbb N$, ma non hanno nemmeno $f''(0)$.

*(Esempio mio, non negli appunti: $f(x)=e^{-1/x^2}\,D(x)$ per $x\neq0$, $f(0)=0$, con $D$ la funzione di Dirichlet ($1$ sui razionali, $0$ sugli irrazionali). Poiché $|f(x)|\le e^{-1/x^2}=o(x^n)$ per ogni $n$, si ha $P_n\equiv0$ per ogni $n$. Però $f$ non è continua in nessun $x\neq0$, quindi non è derivabile vicino a $0$ e $f''(0)$ non ha senso.)*

**Oss. (casi piccoli).**
- $n=1$: $f(x)=f(0)+f'(0)\,x+o(x)$, cioè la **definizione di differenziale**.
- $n=0$: $f(x)=f(0)+o(1)$, cioè la **continuità** di $f$ in $x=0$.

**Oss.** Ogni $P_{n+1}(x)$ si ottiene da $P_n(x)$ aggiungendo un termine, $\frac{f^{(n+1)}(0)}{(n+1)!}x^{n+1}$.

> [!example] Esempio
> Per $f(x)=\cos x$ si ha $f(0)=1$, $f'(0)=0$, $f''(0)=-1$. Quindi $P_2(x)=1-\frac{x^2}2$, cioè $\cos x=1-\frac{x^2}2+o(x^2)$, lo sviluppo già visto nella lezione sui simboli di Landau.

## 4. Sviluppi di Taylor delle funzioni elementari

Per $x\to0$ (troncando all'ordine voluto e aggiungendo il resto $o(x^n)$):

$$
\begin{aligned}
e^x&=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\frac{x^5}{5!}+\dots\\
\sin x&=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\dots\\
\cos x&=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\dots\\
\log(1+x)&=x-\frac{x^2}2+\frac{x^3}3-\frac{x^4}4+\frac{x^5}5-\dots&&\text{(senza fattoriali)}\\
\arctan x&=x-\frac{x^3}3+\frac{x^5}5-\frac{x^7}7+\dots&&\text{(senza fattoriali)}\\
(1+x)^a&=1+ax+\frac{a(a-1)}{2!}x^2+\frac{a(a-1)(a-2)}{3!}x^3+\dots
\end{aligned}
$$

I coefficienti di $(1+x)^a$ sono una specie di **binomiale con $a$ reale**:

$$
\binom a1=a,\quad\binom a2=\frac{a(a-1)}{2!},\quad\binom a3=\frac{a(a-1)(a-2)}{3!},\quad\dots,\quad\binom ak=\frac{a(a-1)\cdots(a-k+1)}{k!}.
$$

**Oss. (parità).** Se $f$ è **[[Funzione pari e dispari|pari]]**, lo sviluppo ha solo potenze pari; se è **dispari**, solo potenze dispari (si vede in $\sin$, $\cos$, $\arctan$).

*Dimostrazione.* Basta osservare che la derivata di una funzione pari è dispari e viceversa, e che le funzioni dispari valgono $0$ in $0$. Quindi, se $f$ è pari, le derivate di ordine dispari sono dispari e si annullano in $0$; se $f$ è dispari, si annullano in $0$ quelle di ordine pari (compresa $f$ stessa). $\square$

### 4.1 L'esempio, rifatto con Taylor

Con gli sviluppi all'ordine $2$:

$$
e^x=1+x+\frac{x^2}2+o(x^2),\qquad\cos x=1-\frac{x^2}2+o(x^2),\qquad\sin x=x+o(x^2).
$$

Allora

$$
\frac{e^x-\cos x-\sin x+x^2}{x^2}
=\frac{1+x+\frac{x^2}2+o(x^2)-1+\frac{x^2}2-x+x^2}{x^2}
=\frac{2x^2+o(x^2)}{x^2}\longrightarrow2,
$$

in accordo con De L'Hôpital. Rispetto al 2° modo della sezione 1.3, la differenza è che ora tutti i resti sono $o(x^2)$, dello stesso ordine del denominatore. Nota che $\sin x=x+o(x^2)$ è lecito: $\sin$ è dispari, quindi non ha termine in $x^2$ ($P_2=P_1=x$).

### 4.2 Esercizio: quali scritture sono corrette?

| Scrittura | Corretta? | Perché |
|---|---|---|
| $\sin x=x-\frac{x^3}6+o(x^3)$ | sì | Taylor con $n=3$ |
| $\sin x=x-\frac{x^3}6+o(x^4)$ | sì | Taylor con $n=4$ (il termine in $x^4$ è nullo per parità) |
| $\sin x=x-\frac{x^3}6+o(x^5)$ | **no** | manca $\frac{x^5}{120}$ |
| $\sin x=x-\frac{x^3}6+o(x^2)$ | sì, ma **buffa** | l'o piccolo mangia $\frac{x^3}6$ |
| $\sin x=x-257x^3+o(x^2)$ | sì, come sopra | anche $257x^3$ è $o(x^2)$ |

## 5. Verifica degli sviluppi

Si applica la formula di Taylor–Peano: basta calcolare le derivate in $0$.

**$f(x)=e^x$.** $f^{(k)}(x)=e^x$, quindi $f^{(k)}(0)=1$ e il coefficiente di $x^k$ è $\frac1{k!}$.

**$f(x)=\sin x$.**

$$
f^{(0)}=\sin x,\quad f^{(1)}=\cos x,\quad f^{(2)}=-\sin x,\quad f^{(3)}=-\cos x,\quad f^{(4)}=\sin x,
$$

e così via, periodicamente modulo $4$. In $x=0$ si trova $0,1,0,-1,0,\dots$: zero per $k$ pari, $\pm1$ alternati per $k$ dispari.

**$f(x)=\cos x$.** Stessa cosa (in $0$: $1,0,-1,0,\dots$).

**$f(x)=\log(1+x)$.**

$$
f^{(1)}=\frac1{1+x},\quad f^{(2)}=-\frac1{(1+x)^2},\quad f^{(3)}=\frac2{(1+x)^3},\quad f^{(4)}=-\frac6{(1+x)^4}.
$$

Sembra ragionevole che (facile [[Principio di induzione|induzione]])

$$
f^{(k)}(x)=(-1)^{k+1}\frac{(k-1)!}{(1+x)^k}\qquad(k\ge1).
$$

Quindi $f^{(k)}(0)=(-1)^{k+1}(k-1)!$ e il coefficiente di $x^k$ è

$$
\frac1{k!}f^{(k)}(0)=(-1)^{k+1}\frac{(k-1)!}{k!}=(-1)^{k+1}\frac1k,
$$

mentre il termine costante è $\log1=0$. Ecco perché non ci sono fattoriali.

*(Passo induttivo, mio: derivando $(-1)^{k+1}(k-1)!\,(1+x)^{-k}$ si ottiene $(-1)^{k+1}(k-1)!\,(-k)(1+x)^{-k-1}=(-1)^{k+2}\frac{k!}{(1+x)^{k+1}}$.)*

**$f(x)=(1+x)^a$.**

$$
f^{(1)}=a(1+x)^{a-1},\quad f^{(2)}=a(a-1)(1+x)^{a-2},\quad f^{(3)}=a(a-1)(a-2)(1+x)^{a-3},
$$

e così via. In $0$: $f^{(k)}(0)=a(a-1)\cdots(a-k+1)$, e dividendo per $k!$ si ottiene $\binom ak$.

### 5.1 Casi speciali

**$a=-1$:**

$$
\boxed{\frac1{1+x}=1-x+x^2-x^3+x^4-x^5+\dots}
$$

infatti $\binom{-1}1=\frac{-1}{1}=-1$, $\binom{-1}2=\frac{(-1)(-2)}{2!}=1$, $\binom{-1}3=\frac{(-1)(-2)(-3)}{3!}=-1$, e in generale $\binom{-1}k=(-1)^k$.

**Sostituendo $-x$ al posto di $x$:**

$$
\boxed{\frac1{1-x}=1+x+x^2+x^3+x^4+\dots}
$$

**Sostituendo $x^2$ al posto di $x$:**

$$
\frac1{1+x^2}=1-x^2+x^4-x^6+x^8-\dots
$$

Da qui gli appunti indicano la strada per $\arctan$:

1. da questo sviluppo deduco le derivate di $\frac1{1+x^2}$ in $x=0$ (per l'unicità, il coefficiente di $x^k$ è $\frac{1}{k!}$ per la derivata $k$-esima);
2. da quelle deduco le derivate di $\arctan x$ in $x=0$, perché $\arctan'x=\frac1{1+x^2}$;
3. dalle derivate trovo lo sviluppo di $\arctan x$.

*(Completamento mio. Se $\frac1{1+x^2}=\sum_k c_kx^k$, allora $\arctan^{(k+1)}(0)=k!\,c_k$, quindi il coefficiente di $x^{k+1}$ nello sviluppo di $\arctan$ è $\frac{k!\,c_k}{(k+1)!}=\frac{c_k}{k+1}$. Con $c_{2j}=(-1)^j$ e $c_{2j+1}=0$, e $\arctan0=0$, si ottiene $\arctan x=x-\frac{x^3}3+\frac{x^5}5-\dots$. Il passo 1 usa che $\frac1{1+x^2}$ è derivabile infinite volte, così Taylor–Peano si applica e l'unicità identifica i coefficienti con $\frac{f^{(k)}(0)}{k!}$. Restano da giustificare le sostituzioni $x\mapsto-x$ e $x\mapsto x^2$ dentro l'o piccolo, che seguono dalle regole sulle composizioni della nota sui simboli di Landau.)*

## Fonti e precisazioni

- `AM1_26_L027.pdf`: teorema di De L'Hôpital, uso operativo, tre non esempi, utilità pratica, esempi con $\arctan$ e $\arccos$, «l'esempio» risolto in tre modi, ragionamento circolare su $\frac{\sin x}x$.
- `AM1_26_L028.pdf`: problema di Taylor–McLaurin, unicità di $P_n$, teorema di Taylor–Peano, sviluppi delle funzioni elementari, parità, esercizio sulle scritture di $\sin x$, verifica degli sviluppi, casi speciali $\frac1{1\pm x}$ e $\frac1{1+x^2}$.

I due PDF sono le due parti della stessa lezione e riportano entrambi la data **27/10/2025**, conservata nel campo `source_date`.

Precisazioni rispetto agli appunti:
- nel non esempio 1 la derivata di $\cos x$ è scritta $\sin x$ invece di $-\sin x$; l'ho segnalato, la conclusione non cambia;
- il teorema di De L'Hôpital e quello di Taylor–Peano sono enunciati senza dimostrazione («teorema misterioso»);
- le parti segnate «mia» non compaiono nel PDF: l'esempio di funzione con tutti i $P_n$ ma senza $f''(0)$, il passo induttivo per $\log(1+x)$, il completamento dello sviluppo di $\arctan$, il commento sul perché i limiti «metà per volta» sono sbagliati;
- ho aggiunto alcuni passaggi intermedi (la condizione $y>0$ nell'alternativa con $\arccos$, la formula generale $\binom ak$, la tabella dell'esercizio).
