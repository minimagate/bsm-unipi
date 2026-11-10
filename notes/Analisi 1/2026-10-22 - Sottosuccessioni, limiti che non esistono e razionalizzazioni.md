---
type: lecture-note
course: Analisi 1
date: '2026-10-22'
title: Sottosuccessioni, limiti che non esistono e razionalizzazioni
source_files:
- AM1_26_L021.pdf
- AM1_26_L022.pdf
source_date: '2025-10-20'
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Analisi 1/Lectures/2026-10-22 - Sottosuccessioni, limiti che non esistono e razionalizzazioni.md
vault_hash: cb0dc86fdabfef64ed82ac6109de435385bec10ff17dda72e02b816a794e525f
---

# Sottosuccessioni, limiti che non esistono e razionalizzazioni

Questa nota riunisce le due parti **021 e 022** della stessa lezione e prosegue [[2026-10-21 - Dimostrazioni dei limiti notevoli e applicazioni]]. La prima parte introduce le **[[Sottosuccessione|sottosuccessioni]]** e le usa per dimostrare che un [[Limite di una successione|limite]] **non esiste**, per successioni e per funzioni. La seconda parte è una raccolta di esercizi: **razionalizzazioni** per le forme $+\infty-\infty$, somme con un numero crescente di termini, limiti con un parametro e forme $1^{+\infty}$.

## 1. Sottosuccessioni

L'idea: una **sottosuccessione** si ottiene prendendo solo alcuni termini di una [[Successione|successione]], nell'ordine originale:

$$
\boxed{a_0}\ a_1\ \boxed{a_2}\ \boxed{a_3}\ a_4\ a_5\ a_6\ \boxed{a_7}\ a_8\ \dots
$$

**Definizione.** Sia $(n_k)_{k\in\mathbb N}$ una successione **strettamente crescente** di numeri naturali. La sottosuccessione di $(a_n)$ associata a $(n_k)$ è l'applicazione

$$
k\longmapsto a_{n_k}.
$$

**Esempi.**

| Sottosuccessione | Indici scelti | Termini |
|---|---|---|
| $a_{2k}$ | pari | $a_0,a_2,a_4,a_6,\dots$ |
| $a_{2k+1}$ | dispari | $a_1,a_3,a_5,a_7,\dots$ |
| $a_{k^2}$ | quadrati perfetti | $a_0,a_1,a_4,a_9,\dots$ |

**Definizione più generale.** Si può anche richiedere soltanto che $n_k\to+\infty$, senza che $(n_k)$ sia strettamente monotona.

### 1.1 Le sottosuccessioni ereditano il limite

**Teorema.** Se $a_n\to\ell\in\overline{\mathbb R}$ (la [[Retta reale estesa|retta reale estesa]]), cioè se la successione è di uno dei primi tre tipi (convergente, divergente a $+\infty$ o a $-\infty$), allora **ogni** sua sottosuccessione tende allo stesso $\ell$.

**Idea della dimostrazione.** Qualunque cosa faccia $a_n$ *[[Proprietà definitivamente vera|definitivamente]]* ($a_n\geq M$, $a_n\leq M$, $|a_n-\ell|\leq\varepsilon$), la fa definitivamente anche la sottosuccessione.

Il passaggio si basa su una semplice osservazione. Se $(n_k)$ è strettamente crescente in $\mathbb N$, allora

$$
n_k\geq k\qquad\forall k\in\mathbb N,
$$

per una facile [[Principio di induzione|induzione]]: $n_0\geq0$, e da $n_k\geq k$ segue $n_{k+1}>n_k\geq k$, dunque $n_{k+1}\geq k+1$. Di conseguenza, se $a_n\geq M$ per ogni $n\geq n_0$, allora

$$
a_{n_k}\geq M\qquad\forall k\geq n_0,
$$

perché $k\geq n_0$ implica $n_k\geq k\geq n_0$. Lo stesso vale per $a_n\leq M$ e per $|a_n-\ell|\leq\varepsilon$.

### 1.2 Successioni senza limite

Se $(a_n)$ **non ha limite** (tipo 4), le sue sottosuccessioni possono avere limite oppure no.

**Esempio classico.** Per $a_n=(-1)^n$:

- $a_{2k}=1\to1$ e $a_{2k+1}=-1\to-1$;
- $a_{k^2}$ non ha limite, perché $k^2$ ha la stessa parità di $k$ e quindi i termini alternano ancora $1$ e $-1$;
- $a_{k!}\to1$, perché $k!$ è pari per $k\geq2$.

## 2. Come dimostrare che una successione non ha limite

> **Criterio.** Per dimostrare che $(a_n)$ non ha limite basta trovare **due sottosuccessioni con limiti diversi**.

In realtà la condizione è anche necessaria (è un «se e solo se»), ma a noi serve solo la direzione sufficiente.

**Dimostrazione.** Se [[Dimostrazione per assurdo|per assurdo]] $a_n\to\ell\in\overline{\mathbb R}$, per il teorema precedente tutte le sottosuccessioni avrebbero lo stesso limite $\ell$.

**Perché è comodo.** Negare direttamente la definizione è una fatica. Che $(a_n)$ abbia limite reale significa

$$
\exists\ell\in\mathbb R\ \forall\varepsilon>0\ \exists n_0\in\mathbb N\ \forall n\geq n_0\quad |\ell-a_n|\leq\varepsilon.
$$

La negazione è

$$
\forall\ell\in\mathbb R\ \exists\varepsilon>0\ \underbrace{\forall n_0\in\mathbb N\ \exists n\geq n_0}_{\text{frequentemente}}\quad |\ell-a_n|>\varepsilon,
$$

e per dire che il limite non esiste bisognerebbe anche escludere a parte i limiti $\pm\infty$. Trovare due sottosuccessioni è molto più rapido.

### Esempio 1: $n^3+(-1)^n n^5$ non ha limite

Sui pari e sui dispari:

$$
a_{2k}=(2k)^3+(2k)^5\longrightarrow+\infty,
\qquad
a_{2k+1}=(2k+1)^3-(2k+1)^5\longrightarrow-\infty.
$$

Per entrambi i limiti basta raccogliere la potenza dominante $k^5$.

### Esempio 2: $n^5+(-1)^n n^3\to+\infty$

Qui il termine oscillante è **dominato** e il limite esiste:

$$
n^5+(-1)^n n^3=\underbrace{n^5}_{\to+\infty}\Bigl(1+\underbrace{\frac{(-1)^n}{n^2}}_{\to0}\Bigr)\longrightarrow+\infty,
$$

dove il secondo fattore tende a $1$ per il [[Teorema dei carabinieri|teorema dei carabinieri]]:

$$
-\frac1{n^2}\leq\frac{(-1)^n}{n^2}\leq\frac1{n^2}.
$$

### Esempio 3: $\sin\left(\frac\pi7 n\right)$ non ha limite

**Brutta copia: come si scelgono gli indici.** Si cercano gli $n$ su cui il seno assume valori facili.

- $\sin=0$: $\frac\pi7 n=2k\pi$, cioè $n=14k$.
- $\sin=1$: $\frac\pi7 n=\frac\pi2+2k\pi$, cioè $2n=14k+7$. Impossibile, perché il primo membro è pari e il secondo dispari.
- $\sin=\sin\frac\pi7$: $\frac\pi7 n=\frac\pi7+2k\pi$, cioè $n=1+14k$.

**Bella copia.**

$$
a_{14k}=\sin\Bigl(\frac\pi7\cdot14k\Bigr)=\sin(2k\pi)=0\longrightarrow0,
$$

$$
a_{14k+1}=\sin\Bigl(\frac\pi7+2k\pi\Bigr)=\sin\frac\pi7\longrightarrow\sin\frac\pi7\neq0.
$$

## 3. Come dimostrare che un limite di funzione non esiste

Passiamo ora ai [[Limite di una funzione|limiti di funzioni]].

Nelle note «$x\to$ CANE» indica un punto di arrivo generico: $+\infty$, $-\infty$, $x_0$, $x_0^+$ oppure $x_0^-$.

> **Criterio.** Per dimostrare che $\displaystyle\lim_{x\to\text{CANE}}f(x)$ non esiste basta trovare due successioni
> $$a_n\to\text{CANE},\qquad b_n\to\text{CANE}$$
> tali che
> $$f(a_n)\to\ell_1\in\overline{\mathbb R},\qquad f(b_n)\to\ell_2\in\overline{\mathbb R},\qquad \ell_1\neq\ell_2.$$

Anche questa è una condizione sufficiente, ma in realtà è un «se e solo se».

**Dimostrazione.** Se per assurdo $\lim_{x\to\text{CANE}}f(x)=\ell\in\overline{\mathbb R}$, allora $f(a_n)$ e $f(b_n)$ tenderebbero entrambe a $\ell$. È il [[2026-10-21 - Dimostrazioni dei limiti notevoli e applicazioni#5.1 Lemma di passaggio al limite lungo una successione|criterio funzioni → successioni]], applicato con $x=a_n$ e con $x=b_n$.

**Promemoria (dalle ipotesi del criterio).** Le successioni devono stare nel dominio di $f$ e, se il punto è finito, essere diverse da $x_0$; per $x_0^+$ o $x_0^-$ devono avvicinarsi dal lato giusto.

### Esempio 1: $\displaystyle\lim_{x\to+\infty}\sin x$ non esiste

$$
a_n=2\pi n\to+\infty,\qquad \sin(a_n)=0\to0;
$$

$$
b_n=\frac\pi2+2\pi n\to+\infty,\qquad \sin(b_n)=1\to1.
$$

### Esempio 2: $\displaystyle\lim_{x\to0^+}\cos\frac1{x^2}$ non esiste

**Brutta copia.**

- Posso avere $\cos=1$? Serve $\frac1{x^2}=2k\pi$, cioè $x=\frac1{\sqrt{2k\pi}}\to0^+$.
- Posso avere $\cos=0$? Serve $\frac1{x^2}=2k\pi+\frac\pi2$, cioè $x=\frac1{\sqrt{2k\pi+\pi/2}}\to0^+$.

**Bella copia.** Per $n\geq1$ consideriamo

$$
a_n=\frac1{\sqrt{2n\pi}}\to0^+,
\qquad
\cos\frac1{a_n^2}=\cos(2\pi n)=1\to1;
$$

$$
b_n=\frac1{\sqrt{2n\pi+\pi/2}}\to0^+,
\qquad
\cos\frac1{b_n^2}=\cos\Bigl(2\pi n+\frac\pi2\Bigr)=0\to0.
$$

### Esempio 3: $\displaystyle\lim_{x\to+\infty}x(2+\sin x)=+\infty$

Qui il limite esiste. Poiché $2+\sin x\geq1$, per $x>0$ si ha

$$
x(2+\sin x)\geq x\longrightarrow+\infty,
$$

e si conclude per confronto.

### Esempio 4: $\displaystyle\lim_{x\to+\infty}x(1+\sin x)$ non esiste

Ora il fattore $1+\sin x$ si annulla infinite volte. Con $f(x)=x(1+\sin x)$:

$$
a_n=\pi n\to+\infty,\qquad f(a_n)=\pi n\to+\infty;
$$

$$
b_n=\frac{3\pi}2+2n\pi\to+\infty,\qquad f(b_n)=0\to0.
$$

Se il limite fosse stato per $x\to-\infty$, si sarebbero usate

$$
a_n=-\pi n\to-\infty,\qquad b_n=\frac{3\pi}2-2n\pi\to-\infty.
$$

### Esempio 5: $\bigl(2+\cos\bigl(\frac\pi{22}n\bigr)\bigr)^n$ non ha limite

Si tratta di una successione. Sui multipli di $44$ il coseno vale $1$:

$$
a_{44k}=\bigl(2+\cos(2k\pi)\bigr)^{44k}=3^{44k}\longrightarrow+\infty.
$$

Vorrei invece $\cos=-1$: $\frac\pi{22}n=\pi+2k\pi$, cioè $n=22+44k$. Allora

$$
a_{44k+22}=\bigl(2+\cos(\pi+2k\pi)\bigr)^{44k+22}=1^{44k+22}=1\longrightarrow1.
$$

### Esempio 6: $\displaystyle\lim_{x\to+\infty}\sin x\cdot\sin\frac1x=0$

$$
\underbrace{-\sin\frac1x}_{\to0}\leq\sin x\cdot\sin\frac1x\leq\underbrace{\sin\frac1x}_{\to0}.
$$

Si è usato che $\sin\frac1x>0$ quando $x$ è abbastanza grande (basta $x>1/\pi$, così che $0<1/x<\pi$). Si conclude con i carabinieri.

> [!example] Esempio
> Il criterio funziona anche per $x\to x_0$: per $\displaystyle\lim_{x\to0}\sin\frac1x$ prendiamo $a_n=\frac1{2\pi n}$ e $b_n=\frac1{\frac\pi2+2\pi n}$, entrambe tendenti a $0$. Si ha $\sin\frac1{a_n}=\sin(2\pi n)=0$ e $\sin\frac1{b_n}=1$: due limiti diversi, quindi il limite non esiste.

## 4. Razionalizzazioni: forme $+\infty-\infty$ con radici

Sono [[Forma indeterminata|forme indeterminate]]: non si possono risolvere con i soli [[Teoremi algebrici sui limiti|teoremi algebrici]], serve un'idea in più.

### Esempio 1: $\displaystyle\lim_{n\to+\infty}\sqrt{n+7}-\sqrt{n+4}=0$

**Trucco: razionalizzare.** Si moltiplica e si divide per la somma delle due radici:

$$
\sqrt{n+7}-\sqrt{n+4}=\frac{(n+7)-(n+4)}{\sqrt{n+7}+\sqrt{n+4}}=\frac3{\sqrt{n+7}+\sqrt{n+4}}\longrightarrow\frac3{+\infty}=0.
$$

L'identità usata è

$$
\boxed{\sqrt A-\sqrt B=(\sqrt A-\sqrt B)\frac{\sqrt A+\sqrt B}{\sqrt A+\sqrt B}=\frac{A-B}{\sqrt A+\sqrt B}}.
$$

> **Errore da non fare.** «$\sqrt{n+7}-\sqrt{n+4}\sim\sqrt n-\sqrt n=0$». Qui il risultato sarebbe giusto per caso; l'esempio successivo mostra che il ragionamento è sbagliato.

### Esempio 2: $\displaystyle\lim_{n\to+\infty}\sqrt{n^2+7n+4}-n=\frac72$

> **Errore da non fare.** «$\dots=\sqrt{n^2}-n=n-n=0$». Darebbe $0$, mentre il limite è $7/2$.

Si moltiplica e si divide per $\sqrt{\cdots}+n$:

$$
\frac{(n^2+7n+4)-n^2}{\sqrt{n^2+7n+4}+n}
=\frac{7+\frac4n}{\sqrt{1+\frac7n+\frac4{n^2}}+1}
\longrightarrow\frac72,
$$

dove nel secondo passaggio si è diviso numeratore e denominatore per $n$.

### Esempio 3: $\displaystyle\lim_{n\to+\infty}\sqrt[3]{n^3+7n^2+4}-n=\frac73$

**Come si razionalizzano le radici cubiche?** Si usa il prodotto notevole

$$
a^3-b^3=(a-b)(a^2+ab+b^2)
$$

con $a=\sqrt[3]A$ e $b=\sqrt[3]B$:

$$
A-B=\bigl(\sqrt[3]A-\sqrt[3]B\bigr)\underbrace{\bigl(\sqrt[3]{A^2}+\sqrt[3]{AB}+\sqrt[3]{B^2}\bigr)}_{\text{fattore per cui moltiplicare e dividere}}.
$$

Con $A=n^3+7n^2+4$ e $B=n^3$ (quindi $\sqrt[3]B=n$):

$$
\sqrt[3]{n^3+7n^2+4}-n
=\frac{(n^3+7n^2+4)-n^3}{\sqrt[3]{(n^3+7n^2+4)^2}+\sqrt[3]{n^3(n^3+7n^2+4)}+n^2}.
$$

Raccogliendo $n^2$ sopra e sotto, il numeratore diventa $7+4/n^2\to7$ e ciascuno dei tre addendi del denominatore tende a $1$. Il limite è $\dfrac73$.

### Esempio 4: $\displaystyle\lim_{n\to+\infty}\sqrt{n+5}-\sqrt[3]{2n+7}=+\infty$

Qui non serve razionalizzare: si **raccoglie $\sqrt n$, che comanda**.

$$
\begin{aligned}
\sqrt{n+5}-\sqrt[3]{2n+7}
&=\sqrt n\left\{\sqrt{1+\frac5n}-\frac1{\sqrt n}\sqrt[3]{2n+7}\right\}\\
&=\sqrt n\left\{\sqrt{1+\frac5n}-\frac{\sqrt[3]n}{\sqrt n}\sqrt[3]{2+\frac7n}\right\}\\
&=\underbrace{\sqrt n}_{\to+\infty}\Bigl\{\underbrace{\sqrt{1+\frac5n}}_{\to1}-\underbrace{\frac1{\sqrt[6]n}}_{\to0}\underbrace{\sqrt[3]{2+\frac7n}}_{\to\sqrt[3]2}\Bigr\}\longrightarrow+\infty.
\end{aligned}
$$

## 5. Somme con un numero crescente di termini

Nei tre esempi seguenti il numero di addendi, $n+1$, cresce con $n$. La strategia comune è stimare la somma con

$$
(\text{termine più piccolo})\cdot(\text{numero dei termini})\leq a_n\leq(\text{termine più grande})\cdot(\text{numero dei termini}).
$$

### Esempio 5: $\displaystyle a_n=\sum_{k=n}^{2n}\frac1{k^2}\to0$

I primi termini sono

$$
a_1=1+\frac14,\qquad a_2=\frac14+\frac19+\frac1{16},\qquad a_3=\frac19+\frac1{16}+\frac1{25}+\frac1{36},\ \dots
$$

> **Errore da non fare.** Pensare che il risultato segua dal fatto che tutti i termini tendono a $0$. Il numero dei termini cresce: l'esempio 6 mostra che una somma di termini infinitesimi può divergere.

**Dimostrazione.** Il termine più grande è $1/n^2$ e i termini sono $n+1$:

$$
0\leq a_n\leq\frac1{n^2}(n+1).
$$

Il membro destro tende a $0$, quello sinistro è $0$: si conclude con i carabinieri.

### Esempio 6: $\displaystyle a_n=\sum_{k=n}^{2n}\frac1{\sqrt k}\to+\infty$

Per esempio $a_3=\frac1{\sqrt3}+\frac1{\sqrt4}+\frac1{\sqrt5}+\frac1{\sqrt6}$. Ora il termine più piccolo è $1/\sqrt{2n}$:

$$
a_n\geq\frac1{\sqrt{2n}}(n+1).
$$

Il membro destro tende a $+\infty$, quindi per confronto anche $a_n\to+\infty$.

### Esempio 7: $\displaystyle a_n=\sum_{k=n}^{2n}\frac1k$ tende a un limite $\ell\in(0,+\infty)$

La stessa stima dà

$$
\frac1{2n}(n+1)\leq a_n\leq\frac1n(n+1).
$$

I due estremi tendono a $\frac12$ e a $1$, quindi $\ell$, **se esiste**, sta in $\left[\frac12,1\right]$. Il confronto da solo non basta però a mostrare che il limite esiste.

**Perché $\ell$ esiste?** Si spera nella monotonia. Passando da $a_n$ ad $a_{n+1}$ si perde il termine $\frac1n$ e si aggiungono $\frac1{2n+1}$ e $\frac1{2n+2}$:

$$
a_{n+1}-a_n=\frac1{2n+2}+\frac1{2n+1}-\frac1n\leq\frac1{2n}+\frac1{2n}-\frac1n=0.
$$

La successione è decrescente e limitata dal basso (da $\frac12$), quindi per il teorema sulle [[Successione monotona|successioni monotone]] ha limite.

**Osservazione.** Si vedrà più avanti che $\ell=\log2$.

## 6. Limiti con un parametro

### Esempio 8: un rapporto di polinomi

$$
\lim_{n\to+\infty}\frac{n^3+n^a+5}{n^5+n^3+1}=
\begin{cases}
+\infty&\text{se }a>5,\\
1&\text{se }a=5,\\
0&\text{se }a<5.
\end{cases}
$$

**Come si dimostra.** Si raccoglie $n^5$ sopra e sotto. Il denominatore diviso per $n^5$ tende a $1$; il numeratore diviso per $n^5$ è $n^{-2}+n^{a-5}+5n^{-5}$, che tende a $+\infty$, $1$ o $0$ a seconda che $a-5$ sia positivo, nullo o negativo.

### Esempio 9: $\left(1+\frac1n\right)^{n^a}$

$$
\lim_{n\to+\infty}\left(1+\frac1n\right)^{n^a}=
\begin{cases}
+\infty&\text{se }a>1,\\
e&\text{se }a=1,\\
1&\text{se }a<1.
\end{cases}
$$

Si scrive la potenza (ricorda il [[Numero di Nepero|numero di Nepero]]) come $e^{n^a\log(1+\frac1n)}$ e si calcola il limite dell'esponente:

$$
n^a\log\left(1+\frac1n\right)
=\frac{n^a}n\cdot\frac{\log\left(1+\frac1n\right)}{\frac1n}
=n^{a-1}\underbrace{\frac{\log\left(1+\frac1n\right)}{\frac1n}}_{\to1}.
$$

Il riquadro tende a $1$ per il [[Limiti notevoli|limite notevole]] del logaritmo con $x=\frac1n\to0$. Il comportamento dipende quindi facilmente da $n^{a-1}$, che tende a $+\infty$, $1$ o $0$; l'esponenziale tende di conseguenza a $+\infty$, $e$ o $1$.

## 7. Altri esercizi sui limiti di funzioni

### Esempio 10: $\displaystyle\lim_{x\to-\infty}\sqrt{x^2+7x+2}+x$ $\quad[+\infty-\infty]$

> **Errore da non fare (TERRIBILE!).** «$\sqrt{\cdots}+x=x+x\to-\infty$». L'uguaglianza $\sqrt{x^2}=x$ vale solo per $x\geq0$; in generale $\sqrt{x^2}=|x|$, e qui $x\to-\infty$.

Si pone $y=-x$, così $y\to+\infty$, e il limite diventa

$$
\lim_{y\to+\infty}\sqrt{y^2-7y+2}-y=-\frac72,
$$

che si calcola razionalizzando come nell'esempio 2:

$$
\frac{-7y+2}{\sqrt{y^2-7y+2}+y}=\frac{-7+\frac2y}{\sqrt{1-\frac7y+\frac2{y^2}}+1}\longrightarrow-\frac72.
$$

### Esempio 11: $\displaystyle\lim_{x\to\frac{3\pi}2}\frac{\cos x}{2x-3\pi}$ $\quad[0/0]$

Si riporta il limite in $0$ ponendo $y=x-\frac{3\pi}2$, in modo che $y\to0$. Da $x=y+\frac{3\pi}2$ si ha $2x-3\pi=2y$, e per la formula di addizione

$$
\cos\left(\frac{3\pi}2+y\right)=\cos\frac{3\pi}2\cos y-\sin\frac{3\pi}2\sin y=\sin y.
$$

Quindi

$$
\lim_{y\to0}\frac{\cos\left(\frac{3\pi}2+y\right)}{2y}=\lim_{y\to0}\frac{\sin y}{2y}=\boxed{\frac12}.
$$

> **Attenzione: segno corretto rispetto agli appunti.** Nel PDF compare $\cos\left(\frac{3\pi}2+y\right)=-\sin y$ e il risultato $-\frac12$. Il segno corretto è $+$: per $x$ appena a destra di $\frac{3\pi}2$ numeratore e denominatore sono entrambi positivi, quindi il limite non può essere negativo.

### Esempio 12: $\displaystyle\lim_{x\to0^+}\sqrt[x]{\frac{a^x+b^x}2}$ con $a,b>0$ $\quad[1^{+\infty}]$

Si scrive

$$
\left(\frac{a^x+b^x}2\right)^{1/x}=e^{\frac1x\log\left(\frac{a^x+b^x}2\right)}
$$

e si calcola il limite dell'esponente. Ponendo $t=\frac{a^x+b^x}2-1\to0$:

$$
\frac1x\log\left(1+\frac{a^x+b^x}2-1\right)
=\underbrace{\frac{\log(1+t)}{t}}_{\to1}\cdot\frac1x\left(\frac{a^x+b^x}2-1\right).
$$

**Calcolo a parte («in un angolo»):**

$$
\frac1x\left(\frac{a^x+b^x}2-1\right)=\frac1x\cdot\frac{a^x+b^x-2}2
=\frac{a^x-1}{2x}+\frac{b^x-1}{2x}
\longrightarrow\frac12\log a+\frac12\log b=\log\sqrt{ab}.
$$

L'esponente tende a $\log\sqrt{ab}$ e quindi il limite originale è

$$
\boxed{\lim_{x\to0^+}\sqrt[x]{\frac{a^x+b^x}2}=\sqrt{ab}}.
$$

*Nota (mia):* il fattore $\log(1+t)/t$ richiede $t\neq0$. Se $a=b=1$ si ha $t\equiv0$, ma allora l'espressione vale identicamente $1=\sqrt{ab}$ e il risultato resta vero.

### Esempio 13: $\displaystyle\lim_{x\to+\infty}\sqrt[x]{\frac{a^x+b^x}2}=\max\{a,b\}$

Indicazione degli appunti: **chi comanda si raccoglie!**

*Svolgimento (mio).* Supponiamo $a\geq b$ (l'altro caso è simmetrico). Raccogliendo $a^x$:

$$
\left(\frac{a^x+b^x}2\right)^{1/x}=a\left(\frac{1+(b/a)^x}2\right)^{1/x}.
$$

Poiché $0<b/a\leq1$, la base dell'ultima potenza sta in $\left[\frac12,1\right]$. Dunque

$$
\left(\frac12\right)^{1/x}\leq\left(\frac{1+(b/a)^x}2\right)^{1/x}\leq1,
$$

e $(1/2)^{1/x}\to(1/2)^0=1$. Per i carabinieri il fattore tende a $1$ e il limite è $a=\max\{a,b\}$.

## Fonti e precisazioni

- `AM1_26_L021.pdf`: sottosuccessioni e criteri di non esistenza del limite per successioni e funzioni.
- `AM1_26_L022.pdf`: razionalizzazioni, somme con un numero crescente di termini, limiti con parametro e forme $1^{+\infty}$.

I due PDF sono le due parti della stessa lezione e riportano entrambi la data **20/10/2025**, conservata nel campo `source_date`.

Correzione rispetto agli appunti: nell'esempio 11 della lezione 022 il risultato corretto è $+\frac12$, non $-\frac12$. Le parti segnate «mia» o «mio» (gli svolgimenti dell'esempio 13 e il caso limite dell'esempio 12) non compaiono nel PDF. Ho aggiunto anche alcuni passaggi intermedi, come l'induzione per $n_k\geq k$ e la razionalizzazione esplicita nell'esempio 10.
