---
type: lecture-note
course: Analisi 1
date: '2026-10-21'
title: Dimostrazioni dei limiti notevoli e applicazioni
source_files:
- AM1_26_L019.pdf
- AM1_26_L020.pdf
source_date: '2025-10-15'
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Analisi 1/Lectures/2026-10-21 - Dimostrazioni dei limiti notevoli e applicazioni.md
vault_hash: 988a44903282197208c6d65aba7409ac47f88d826efc03e29bb503ffb959cbb7
---

# Dimostrazioni dei limiti notevoli e applicazioni

Questa nota riunisce le lezioni **019 e 020** e prosegue [[2026-10-12 - Limiti di funzioni, continuità e limiti notevoli]]. Qui dimostriamo i [[Limiti notevoli|limiti notevoli]] già enunciati e li usiamo per calcolare [[Limite di una funzione|limiti di funzioni]] e di successioni. In tutta la nota $\log$ indica il **logaritmo naturale** e gli angoli sono espressi in **radianti**.

## 1. Il limite fondamentale del seno

**Teorema.**

$$
\lim_{x\to0}\frac{\sin x}{x}=1.
$$

La funzione $\sin x/x$ è **[[Funzione pari e dispari|pari]]**, perché per $x\neq0$

$$
\frac{\sin(-x)}{-x}=\frac{\sin x}{x}.
$$

Basta quindi dimostrare il limite per $x\to0^+$.

### 1.1 La disuguaglianza geometrica

Per $0<x<\pi/2$ vale

$$
\sin x\leq x\leq\tan x.
$$

**Dimostrazione geometrica.** Prendiamo la circonferenza unitaria di centro $O$, il punto $S=(1,0)$ e il punto $P=(\cos x,\sin x)$. Siano $P'$ il simmetrico di $P$ rispetto all'asse orizzontale e $Q$ l'intersezione della semiretta $OP$ con la tangente alla circonferenza in $S$.

- La corda $PP'$ ha lunghezza $2\sin x$; l'arco minore $PP'$ ha lunghezza $2x$. La corda è più corta dell'arco, dunque $\sin x\leq x$.
- Il settore circolare $OSP$ ha area $x/2$, mentre il triangolo $OSQ$ ha area $\tan x/2$. Il settore sta dentro il triangolo, dunque $x\leq\tan x$.

### 1.2 Il confronto che dà il limite

Dividendo per $\sin x>0$ otteniamo

$$
1\leq\frac{x}{\sin x}\leq\frac1{\cos x}
\qquad\text{per }0<x<\frac\pi2.
$$

Per la [[Funzione continua|continuità]] del coseno, $1/\cos x\to1$ quando $x\to0^+$. Il **[[Teorema dei carabinieri|teorema dei carabinieri]]** dà $x/\sin x\to1$ e, passando al reciproco, $\sin x/x\to1$. La parità permette di concludere anche da sinistra.

## 2. Conseguenze trigonometriche

In questa sezione tutti i limiti sono per $x\to0$; le funzioni coinvolte sono quelle [[Funzioni trigonometriche|trigonometriche]] e le loro [[Funzioni trigonometriche inverse|inverse]].

### 2.1 Il limite del coseno

Moltiplichiamo e dividiamo per il coniugato $1+\cos x$:

$$
\begin{aligned}
\frac{1-\cos x}{x^2}
&=\frac{(1-\cos x)(1+\cos x)}{x^2(1+\cos x)}\\
&=\frac{\sin^2x}{x^2}\,\frac1{1+\cos x}
=\left(\frac{\sin x}{x}\right)^2\frac1{1+\cos x}
\longrightarrow\frac12.
\end{aligned}
$$

Quindi

$$
\boxed{\lim_{x\to0}\frac{1-\cos x}{x^2}=\frac12},
\qquad
\lim_{x\to0}\frac{\cos x-1}{x^2}=-\frac12.
$$

### 2.2 Tangente, arcotangente e arcoseno

Per la tangente:

$$
\frac{\tan x}{x}=\frac{\sin x}{x}\,\frac1{\cos x}\longrightarrow1.
$$

Per l'arcotangente poniamo $y=\arctan x$. Allora $x=\tan y$ e, per continuità, $y\to0$ quando $x\to0$. Di conseguenza

$$
\frac{\arctan x}{x}=\frac{y}{\tan y}\longrightarrow1.
$$

Per l'arcoseno si fa lo stesso: ponendo $y=\arcsin x$, si ha $x=\sin y$ e $y\to0$, perciò

$$
\frac{\arcsin x}{x}=\frac{y}{\sin y}\longrightarrow1.
$$

In conclusione:

$$
\boxed{
\lim_{x\to0}\frac{\tan x}{x}
=\lim_{x\to0}\frac{\arctan x}{x}
=\lim_{x\to0}\frac{\arcsin x}{x}=1
}.
$$

## 3. Dalle successioni alle funzioni: il confronto su intervalli unitari

I limiti di [[Successione|successioni]] aiutano a studiare una funzione per $x\to+\infty$: basta confrontare il suo comportamento su ogni intervallo $[n,n+1)$ con quantità che dipendono solo da $n$.

### 3.1 Lemma sulle funzioni costanti a tratti

Siano $D\subseteq\mathbb R$ con $\sup D=+\infty$, $f:D\to\mathbb R$ e $(a_n)$ una successione. Supponiamo che, per ogni $n$ sufficientemente grande,

$$
f(x)=a_n\qquad\forall x\in D\cap[n,n+1).
$$

Se $a_n\to\ell\in\overline{\mathbb R}$, dove $\overline{\mathbb R}=\mathbb R\cup\{-\infty,+\infty\}$ è la [[Retta reale estesa|retta reale estesa]], allora

$$
\lim_{x\to+\infty}f(x)=\ell.
$$

**Idea della dimostrazione.** Quello che succede ad $a_n$ per $n$ grande succede a $f(x)$ per $x$ grande. Ad esempio, se $\ell\in\mathbb R$, dato $\varepsilon>0$ scegliamo un intero $N$ tale che la formula a tratti valga per $n\geq N$ e $|a_n-\ell|\leq\varepsilon$ per $n\geq N$. Ogni $x\in D$ con $x\geq N$ appartiene a un intervallo $[n,n+1)$ con $n\geq N$, quindi $|f(x)-\ell|\leq\varepsilon$. Per i limiti infiniti si ragiona con le soglie $M$.

### 3.2 Esempio: un'esponenziale prevale su una potenza

Vogliamo calcolare

$$
\lim_{x\to+\infty}\frac{3^x}{x^{27}}.
$$

Per $x\in[n,n+1)$, con $n\geq1$, il numeratore è almeno $3^n$ e il denominatore è al più $(n+1)^{27}$. Pertanto

$$
\frac{3^x}{x^{27}}\geq\frac{3^n}{(n+1)^{27}}.
$$

La successione a destra tende a $+\infty$ per la [[2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti|gerarchia degli infiniti]] (l'esponenziale batte la potenza). Per il lemma, la corrispondente funzione costante a tratti tende a $+\infty$; per confronto,

$$
\boxed{\lim_{x\to+\infty}\frac{3^x}{x^{27}}=+\infty}.
$$

## 4. Dal numero di Nepero ai limiti di esponenziale e logaritmo

Il punto di partenza è il [[Numero di Nepero|numero di Nepero]], già visto come [[Limite di una successione|limite di successione]] in [[2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti]]:

$$
\left(1+\frac1n\right)^n\longrightarrow e.
$$

### 4.1 Estensione alla variabile reale: $x\to+\infty$

Per $x\in[n,n+1)$, con $n\geq1$, confrontiamo sia le basi sia gli esponenti. Poiché le basi sono maggiori di $1$,

$$
\left(1+\frac1{n+1}\right)^n
\leq\left(1+\frac1x\right)^x
\leq\left(1+\frac1n\right)^{n+1}.
$$

Le due successioni esterne tendono a $e$. Infatti

$$
\left(1+\frac1n\right)^{n+1}
=\underbrace{\left(1+\frac1n\right)^n}_{\to e}
\underbrace{\left(1+\frac1n\right)}_{\to1},
$$

mentre

$$
\left(1+\frac1{n+1}\right)^n
=\underbrace{\left(1+\frac1{n+1}\right)^{n+1}}_{\to e}
\underbrace{\left(1+\frac1{n+1}\right)^{-1}}_{\to1}.
$$

Usando il lemma precedente per le funzioni costanti su $[n,n+1)$ e poi i carabinieri si conclude:

$$
\boxed{\lim_{x\to+\infty}\left(1+\frac1x\right)^x=e}.
$$

### 4.2 Lo stesso limite per $x\to-\infty$

Poniamo $y=-x$, così $y\to+\infty$. Per $y>1$:

$$
\begin{aligned}
\left(1+\frac1x\right)^x
&=\left(1-\frac1y\right)^{-y}
=\left(\frac y{y-1}\right)^y\\
&=\left(1+\frac1{y-1}\right)^{y-1}
\left(1+\frac1{y-1}\right)
\longrightarrow e\cdot1=e.
\end{aligned}
$$

Il primo fattore si riconduce al limite appena dimostrato ponendo $z=y-1\to+\infty$. Quindi anche

$$
\lim_{x\to-\infty}\left(1+\frac1x\right)^x=e.
$$

### 4.3 Il limite $(1+y)^{1/y}$ per $y\to0$

Con il cambio di variabile $y=1/x$, $x\to+\infty$ corrisponde a $y\to0^+$ e $x\to-\infty$ a $y\to0^-$. I due limiti precedenti danno

$$
\boxed{\lim_{y\to0}(1+y)^{1/y}=e}.
$$

La base è positiva per $y>-1$, dunque la potenza è definita in un intorno bucato di $0$.

### 4.4 Il limite del logaritmo

Poiché il logaritmo è continuo in $e$, lo possiamo applicare al limite precedente:

$$
\log\bigl((1+y)^{1/y}\bigr)
=\frac{\log(1+y)}{y}\longrightarrow\log e=1.
$$

Rinominando la variabile:

$$
\boxed{\lim_{x\to0}\frac{\log(1+x)}x=1}.
$$

### 4.5 Il limite dell'esponenziale

Poniamo $y=\log(1+x)$, da cui $x=e^y-1$. Quando $x\to0$, anche $y\to0$, e il limite del logaritmo diventa

$$
\frac{y}{e^y-1}\longrightarrow1.
$$

Passando al reciproco si ottiene

$$
\boxed{\lim_{x\to0}\frac{e^x-1}x=1}.
$$

Per una base generica $a>0$, con $a\neq1$, scriviamo $a^x=e^{x\log a}$:

$$
\frac{a^x-1}x
=\frac{e^{x\log a}-1}{x\log a}\,\log a
\longrightarrow\log a.
$$

Il cambio di variabile è $y=x\log a\to0$. Se $a=1$, il rapporto è identicamente nullo per $x\neq0$, quindi il risultato vale ancora:

$$
\boxed{\lim_{x\to0}\frac{a^x-1}x=\log a\qquad\forall a>0}.
$$

### 4.6 Il «limite dimenticato»: $x\log x$

Per $x\to0^+$ il prodotto $x\log x$ presenta la [[Forma indeterminata|forma indeterminata]] $0\cdot(-\infty)$.

Poniamo prima $y=\log x$, dunque $x=e^y$ e $y\to-\infty$, poi $z=-y\to+\infty$:

$$
x\log x=e^y y=-ze^{-z}=-\frac z{e^z}\longrightarrow0,
$$

perché l'esponenziale prevale sulla potenza (è la [[Gerarchia degli infiniti|gerarchia degli infiniti]]). Quindi

$$
\boxed{\lim_{x\to0^+}x\log x=0}.
$$

Vale anche la generalizzazione

$$
\boxed{\lim_{x\to0^+}x^a|\log x|^b=0\qquad\forall a>0,\ b>0}.
$$

**Stesso cambio di variabile, in esplicito.** Ponendo $z=-\log x\to+\infty$, il prodotto diventa $z^b/e^{az}$, che tende a zero per la stessa gerarchia.

## 5. Dalle funzioni alle successioni

### 5.1 Lemma di passaggio al limite lungo una successione

Siano $f:D\to\mathbb R$ e $(a_n)$ una successione. Supponiamo che:

1. [[Proprietà definitivamente vera|definitivamente]] $a_n\in D$ e, se $x_0\in\mathbb R$, $a_n\neq x_0$;
2. $a_n\to x_0\in\overline{\mathbb R}$;
3. $\displaystyle\lim_{x\to x_0}f(x)=\ell\in\overline{\mathbb R}$.

Allora

$$
\boxed{f(a_n)\longrightarrow\ell}.
$$

**Dimostrazione nel caso $x_0,\ell\in\mathbb R$.** Dato $\varepsilon>0$, per il limite di $f$ esiste $\delta>0$ tale che

$$
x\in D,\quad0<|x-x_0|\leq\delta
\quad\Longrightarrow\quad |f(x)-\ell|\leq\varepsilon.
$$

Poiché $a_n\to x_0$, definitivamente $|a_n-x_0|\leq\delta$. L'ipotesi sul dominio garantisce anche che $a_n\in D$ e $a_n\neq x_0$. Possiamo quindi applicare la stima con $x=a_n$, ottenendo definitivamente $|f(a_n)-\ell|\leq\varepsilon$.

L'esclusione di $x_0$ serve perché il limite di una funzione **non impone alcun valore a $f(x_0)$**. Per usare un limite destro o sinistro occorre inoltre che $a_n$ si avvicini dal lato corrispondente.

### 5.2 Primo esempio

Ponendo $x=1/n\to0$:

$$
n\sin\frac1n
=\frac{\sin(1/n)}{1/n}\longrightarrow1.
$$

Il limite notevole di funzione si applica lungo la successione $1/n$.

> [!example] Esempio
> Con lo stesso lemma: $\displaystyle n\,\arctan\frac1n=\frac{\arctan(1/n)}{1/n}\to1$, perché $x=1/n\to0$ e $\frac{\arctan x}{x}\to1$.

## 6. Esercizi sui limiti di successioni

### 6.1 $n^2\bigl(\cos(2/n)-1\bigr)$

Facciamo comparire il quadrato dell'argomento del coseno:

$$
n^2\left(\cos\frac2n-1\right)
=4\,\frac{\cos(2/n)-1}{(2/n)^2}
\longrightarrow4\left(-\frac12\right)=-2.
$$

### 6.2 $n\,[\log(n+33)-\log(n+7)]$

La differenza dei logaritmi si trasforma nel logaritmo di un rapporto:

$$
\begin{aligned}
n[\log(n+33)-\log(n+7)]
&=n\log\frac{n+33}{n+7}\\
&=n\log\left(1+\frac{26}{n+7}\right)\\
&=\underbrace{\frac{\log\left(1+\frac{26}{n+7}\right)}{\frac{26}{n+7}}}_{\to1}
\underbrace{\frac{26n}{n+7}}_{\to26}
\longrightarrow26.
\end{aligned}
$$

Il limite notevole si applica con $x=26/(n+7)\to0$.

### 6.3 $n(\sqrt[n]{20}-1)$

Scriviamo la radice come potenza e poniamo $x=1/n$:

$$
n(\sqrt[n]{20}-1)
=\frac{20^{1/n}-1}{1/n}\longrightarrow\log20.
$$

### 6.4 $n(\sqrt[n]{7}-\sqrt[n]{5})$

Aggiungiamo e sottraiamo $1$ per ottenere due limiti del tipo precedente:

$$
\begin{aligned}
n(\sqrt[n]{7}-\sqrt[n]{5})
&=n(\sqrt[n]{7}-1)-n(\sqrt[n]{5}-1)\\
&\longrightarrow\log7-\log5=\log\frac75.
\end{aligned}
$$

### 6.5 $\dfrac n{\log n}(\sqrt[n]{n}-1)$

Quando una potenza ha sia la base sia l'esponente variabili, è utile la riscrittura

$$
A^B=e^{B\log A}\qquad(A>0).
$$

In questo caso

$$
\sqrt[n]{n}=n^{1/n}=e^{\frac{\log n}{n}},
$$

perciò, per $n>1$,

$$
\frac n{\log n}(\sqrt[n]{n}-1)
=\frac{e^{\frac{\log n}{n}}-1}{\frac{\log n}{n}}
\longrightarrow1.
$$

Qui il piccolo argomento è $x_n=(\log n)/n\to0$, sempre per la gerarchia degli infiniti.

## 7. Esercizi sui limiti di funzioni

### 7.1 Una somma di termini al numeratore e al denominatore

Calcoliamo

$$
\lim_{x\to0}
\frac{\sin(2x+x^2)+e^x-\cos x}
{\arctan(3x)+\arcsin(x^2)}.
$$

È una forma $0/0$. Al numeratore scriviamo $e^x-\cos x=(e^x-1)+(1-\cos x)$, poi dividiamo numeratore e denominatore per $x$:

$$
\frac{
\dfrac{\sin(2x+x^2)}x+\dfrac{e^x-1}x+\dfrac{1-\cos x}x
}{
\dfrac{\arctan(3x)}x+\dfrac{\arcsin(x^2)}x
}.
$$

Studiamo separatamente i cinque termini:

$$
\frac{\sin(2x+x^2)}x
=\frac{\sin(2x+x^2)}{2x+x^2}(2+x)\longrightarrow2,
$$

$$
\frac{e^x-1}x\longrightarrow1,
\qquad
\frac{1-\cos x}x=\frac{1-\cos x}{x^2}\,x\longrightarrow0,
$$

$$
\frac{\arctan(3x)}x=3\,\frac{\arctan(3x)}{3x}\longrightarrow3,
\qquad
\frac{\arcsin(x^2)}x=\frac{\arcsin(x^2)}{x^2}\,x\longrightarrow0.
$$

Il denominatore dopo la divisione per $x$ tende a $3\neq0$, quindi è non nullo vicino a $0$. Il limite cercato è

$$
\boxed{\frac{2+1+0}{3+0}=1}.
$$

### 7.2 Una forma $1^{+\infty}$

Calcoliamo

$$
\lim_{x\to0}(\cos x)^{1/\sin^2x}.
$$

Vicino a $0$ il coseno è positivo e, in un intorno bucato sufficientemente piccolo, $\sin x\neq0$. Possiamo scrivere

$$
(\cos x)^{1/\sin^2x}
=\exp\left(\frac{\log(\cos x)}{\sin^2x}\right).
$$

Calcoliamo prima il limite dell'esponente:

$$
\frac{\log(\cos x)}{\sin^2x}
=\underbrace{\frac{\log\bigl(1+(\cos x-1)\bigr)}{\cos x-1}}_{\to1}
\underbrace{\frac{\cos x-1}{x^2}}_{\to-1/2}
\underbrace{\frac{x^2}{\sin^2x}}_{\to1}
\longrightarrow-\frac12.
$$

Per la continuità dell'esponenziale:

$$
\boxed{\lim_{x\to0}(\cos x)^{1/\sin^2x}=e^{-1/2}=\frac1{\sqrt e}}.
$$

### 7.3 Potenze del coseno: distinguere argomento ed esponente

Calcoliamo

$$
\lim_{x\to0}\frac{1-\cos^2(x^3)}{1-\cos^3(x^2)}.
$$

Qui $\cos^2(x^3)=[\cos(x^3)]^2$, mentre $\cos^3(x^2)=[\cos(x^2)]^3$.

Usiamo le scomposizioni $1-A^2=(1-A)(1+A)$ e $1-B^3=(1-B)(1+B+B^2)$:

$$
\frac{1-\cos^2(x^3)}{1-\cos^3(x^2)}
=\frac{1-\cos(x^3)}{1-\cos(x^2)}
\frac{1+\cos(x^3)}{1+\cos(x^2)+\cos^2(x^2)}.
$$

Il secondo fattore tende a $2/3$. Per il primo facciamo comparire i quadrati degli argomenti:

$$
\frac{1-\cos(x^3)}{1-\cos(x^2)}
=\underbrace{\frac{1-\cos(x^3)}{x^6}}_{\to1/2}
\underbrace{\frac{x^4}{1-\cos(x^2)}}_{\to2}
\underbrace{x^2}_{\to0}
\longrightarrow0.
$$

Pertanto

$$
\boxed{\lim_{x\to0}\frac{1-\cos^2(x^3)}{1-\cos^3(x^2)}=0}.
$$

### 7.4 Lo stesso rapporto moltiplicato per un fattore oscillante

Consideriamo

$$
\lim_{x\to0}
\frac{1-\cos^2(x^3)}{1-\cos^3(x^2)}\cos\left(\frac1{x^2}\right).
$$

Il coseno oscillante non ha limite, ma è limitato in valore assoluto da $1$. Se indichiamo con $R(x)$ il rapporto dell'esercizio precedente, abbiamo

$$
0\leq\left|R(x)\cos\left(\frac1{x^2}\right)\right|
\leq|R(x)|\longrightarrow0.
$$

Per confronto il valore assoluto tende a zero e quindi anche l'espressione originaria tende a zero.

Il **trucco del [[Valore assoluto|valore assoluto]]** è

$$
f(x)\to0\iff|f(x)|\to0,
\qquad
a_n\to0\iff|a_n|\to0.
$$

### 7.5 Un limite notevole non si può applicare fuori dalle sue ipotesi

Calcoliamo

$$
\lim_{x\to+\infty}\frac{\log(1+3^x)}x.
$$

La riscrittura

$$
\frac{\log(1+3^x)}x
=\frac{\log(1+3^x)}{3^x}\,\frac{3^x}x
$$

è algebricamente corretta, ma **non** consente di applicare $\log(1+y)/y\to1$: qui $y=3^x\to+\infty$, mentre il limite notevole richiede $y\to0$.

Il modo giusto è raccogliere $3^x$ nell'argomento del logaritmo:

$$
\begin{aligned}
\frac{\log(1+3^x)}x
&=\frac{\log\left(3^x(1+3^{-x})\right)}x\\
&=\frac{x\log3+\log(1+3^{-x})}x\\
&=\log3+\frac1x\log(1+3^{-x}).
\end{aligned}
$$

Poiché $3^{-x}\to0$, abbiamo $\log(1+3^{-x})\to0$; inoltre $1/x\to0$. L'ultimo prodotto tende a zero, dunque

$$
\boxed{\lim_{x\to+\infty}\frac{\log(1+3^x)}x=\log3}.
$$

## Fonti e precisazioni

- Lezione 019 (`AM1_26_L019.pdf`, in Downloads): dimostrazioni dei limiti notevoli, confronto su intervalli unitari e limite $x\log x$.
- Lezione 020 (`AM1_26_L020.pdf`, in Downloads): passaggio dai limiti di funzioni a quelli di successioni ed esercizi svolti.

Entrambi i PDF riportano la data **15/10/2025**, conservata nel campo `source_date`.

Sono corretti due refusi locali della lezione 020: a p. 3 il rapporto $(1-\cos x)/x^2$ tende a $+1/2$; a p. 5, per $x\to+\infty$, $1/x$ tende a $0$. I risultati finali dei due esercizi restano quelli indicati negli appunti. Nella dimostrazione con base $a$ è stato inoltre esplicitato il caso $a=1$, per evitare la divisione per $\log a=0$.
