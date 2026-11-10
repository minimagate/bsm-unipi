---
type: lecture-note
course: Analisi 1
date: '2026-10-08'
title: Criteri della radice e del rapporto e gerarchia degli infiniti
source_files:
- AM1_26_L015.pdf
- AM1_26_L016.pdf
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Analisi 1/Lectures/2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti.md
vault_hash: e8e26f5fe8cadb33b07f81062ce3cfd579875294c6ba7c227592de45773937f6
---

# Criteri della radice e del rapporto e gerarchia degli infiniti

Questa nota prosegue [[2026-10-07 - Successioni monotone, numero di Nepero e teoremi algebrici sui limiti]].

## 1. Limiti fondamentali di potenze e radici

### 1.1 La successione $2^n$

Vogliamo dimostrare che

$$
2^n\to+\infty.
$$

Seguendo direttamente la definizione, fissato $M\in\mathbb{R}$ si vorrebbe trovare $n_0$ tale che

$$
2^n\geq M
\qquad\forall n\geq n_0.
$$

Se $M\leq0$, la disuguaglianza è vera per ogni $n$. Se $M>0$ si potrebbe scegliere $n_0\geq\log_2M$, ma il ragionamento sarebbe circolare: per definire rigorosamente il logaritmo bisogna già sapere che la funzione esponenziale può diventare grande quanto si vuole.

Meglio usare la [[Disuguaglianza di Bernoulli|disuguaglianza di Bernoulli]]:

$$
(1+x)^n\geq1+nx
\qquad(x\geq-1).
$$

Con $x=1$ si ottiene

$$
2^n=(1+1)^n\geq1+n.
$$

Poiché $1+n\to+\infty$, il teorema del confronto dà

$$
2^n\to+\infty.
$$

### 1.2 Potenze con base maggiore di $1$

Più in generale, se $a>1$, allora

$$
a^n\to+\infty.
$$

Infatti $a=1+(a-1)$ con $a-1>0$, quindi Bernoulli dà

$$
a^n=(1+a-1)^n\geq1+n(a-1).
$$

Il membro di destra tende a $+\infty$, dunque anche $a^n$ tende a $+\infty$.

---

## 2. Radici $n$-esime

### 2.1 Il limite di $\sqrt[n]{2}$

Vogliamo calcolare

$$
\lim_{n\to+\infty}\sqrt[n]{2}.
$$

Applicando Bernoulli e poi prendendo la radice $n$-esima, per ogni $x\geq0$ si ha

$$
(1+x)^n\geq1+nx
\quad\Longrightarrow\quad
1+x\geq\sqrt[n]{1+nx}.
$$

Scegliendo $x=\frac1n$ otteniamo

$$
1\leq\sqrt[n]{2}\leq1+\frac1n.
$$

I due estremi tendono a $1$; per il [[Teorema dei carabinieri|teorema dei carabinieri]],

$$
\sqrt[n]{2}\to1.
$$

> [!warning] Ragionamento circolare
> Non si può giustificare questo limite scrivendo $\sqrt[n]{2}=2^{1/n}\to2^0=1$, perché la [[Funzione continua|continuità]] della funzione esponenziale non è ancora stata costruita. Questo limite servirà proprio a fondare quella teoria.

### 2.2 Il limite di $\sqrt[n]{a}$ per $a>0$

Per ogni $a>0$ vale

$$
\sqrt[n]{a}\to1.
$$

Se $a\geq1$, si applica Bernoulli con

$$
x=\frac{a-1}{n}\geq0.
$$

Poiché

$$
\left(1+\frac{a-1}{n}\right)^n\geq1+n\frac{a-1}{n}=a,
$$

prendendo la radice $n$-esima si ottiene

$$
1\leq\sqrt[n]{a}\leq1+\frac{a-1}{n}.
$$

Entrambi gli estremi tendono a $1$, quindi $\sqrt[n]{a}\to1$.

Se invece $0<a<1$, si scrive $a=1/b$ con $b>1$. Allora

$$
\sqrt[n]{a}=\frac1{\sqrt[n]{b}}\to\frac11=1.
$$

### 2.3 Tabella dei limiti fondamentali

Per ogni $a>0$:

$$
\sqrt[n]{a}\to1.
$$

Per le potenze:

$$
a^n\to
\begin{cases}
+\infty, & a>1,\\
1, & a=1,\\
0, & 0\leq a<1.
\end{cases}
$$

Nel terzo caso, se $a=0$ la conclusione è immediata. Se $0<a<1$, si pone $a=1/b$ con $b>1$ e si usa

$$
a^n=\frac1{b^n}\to0.
$$

### 2.4 Il limite di $\sqrt[n]{n}$

Un altro limite fondamentale è

$$
\sqrt[n]{n}\to1.
$$

Si usa una versione più precisa della disuguaglianza di Bernoulli, ottenuta tenendo il termine quadratico dello sviluppo binomiale:

$$
(1+x)^n\geq\binom n2x^2
=\frac{n(n-1)}2x^2
\qquad(x\geq0).
$$

Prendendo la radice $n$-esima:

$$
1+x\geq\sqrt[n]{\frac{n(n-1)}2x^2}.
$$

Scegliendo

$$
x=\sqrt{\frac2{n-1}},
$$

il radicando a destra diventa $n$. Pertanto

$$
1\leq\sqrt[n]{n}\leq1+\sqrt{\frac2{n-1}}.
$$

Il membro di destra tende a $1$, dunque

$$
\sqrt[n]{n}\to1.
$$

---

## 3. Criterio della radice

Il **[[Criterio della radice|criterio della radice]]**: sia $(a_n)$ una successione con $a_n\geq0$ definitivamente e supponiamo che

$$
\sqrt[n]{a_n}\to\ell
\qquad
\text{con }\ell\in[0,+\infty)\cup\{+\infty\}.
$$

Allora:

- se $\ell>1$, si ha $a_n\to+\infty$;
- se $\ell<1$, si ha $a_n\to0$;
- se $\ell=1$, il criterio non permette di concludere.

### 3.1 Dimostrazione nel caso $\ell>1$

Tra $1$ e $\ell$ scegliamo

$$
q=\frac{\ell+1}{2}>1.
$$

Poiché $\sqrt[n]{a_n}\to\ell$, definitivamente

$$
\sqrt[n]{a_n}\geq q.
$$

Elevando alla potenza $n$:

$$
a_n\geq q^n.
$$

Dato che $q>1$, si ha $q^n\to+\infty$; per confronto,

$$
a_n\to+\infty.
$$

Se $\ell=+\infty$, lo stesso ragionamento funziona scegliendo un qualunque $q>1$ che venga definitivamente superato da $\sqrt[n]{a_n}$.

### 3.2 Dimostrazione nel caso $\ell<1$

Scegliamo ancora

$$
q=\frac{\ell+1}{2},
$$

che questa volta soddisfa $\ell<q<1$. Definitivamente,

$$
0\leq\sqrt[n]{a_n}\leq q,
$$

e quindi

$$
0\leq a_n\leq q^n.
$$

Poiché $q^n\to0$, il teorema dei carabinieri dà

$$
a_n\to0.
$$

---

## 4. Criterio del rapporto

Il **[[Criterio del rapporto|criterio del rapporto]]**: sia $(a_n)$ una successione con $a_n>0$ definitivamente e supponiamo che

$$
\frac{a_{n+1}}{a_n}\to\ell
\qquad
\text{con }\ell\in[0,+\infty)\cup\{+\infty\}.
$$

Allora:

- se $\ell>1$, si ha $a_n\to+\infty$;
- se $\ell<1$, si ha $a_n\to0$;
- se $\ell=1$, il criterio non permette di concludere.

### 4.1 Dimostrazione nel caso $\ell>1$

Se $\ell$ è finito, poniamo

$$
q=\frac{\ell+1}{2}>1.
$$

Definitivamente, cioè per ogni $n\geq n_0$ con un opportuno $n_0$,

$$
\frac{a_{n+1}}{a_n}\geq q.
$$

Poiché $a_n>0$, questo equivale a

$$
a_{n+1}\geq q\,a_n.
$$

Iterando la disuguaglianza:

$$
a_{n_0+k}\geq q^k a_{n_0}.
$$

Equivalentemente, per ogni $n\geq n_0$,

$$
a_n\geq q^{n-n_0}a_{n_0}
=q^n\bigl(q^{-n_0}a_{n_0}\bigr).
$$

Il fattore tra parentesi è una costante positiva, mentre $q^n\to+\infty$. Quindi $a_n\to+\infty$.

Se $\ell=+\infty$, si sceglie invece un qualunque $q>1$: il rapporto supera definitivamente $q$ e la stessa iterazione conclude la dimostrazione.

### 4.2 Dimostrazione nel caso $\ell<1$

Poniamo

$$
q=\frac{\ell+1}{2},
$$

così che $0<q<1$. Definitivamente,

$$
\frac{a_{n+1}}{a_n}\leq q,
$$

e, iterando come prima,

$$
0\leq a_n\leq q^{n-n_0}a_{n_0}.
$$

Poiché il membro di destra tende a $0$, segue che

$$
a_n\to0.
$$

### 4.3 Forme più deboli ma spesso sufficienti

Per applicare i due criteri non è sempre necessario conoscere il limite.

- Se esiste $q>1$ tale che $\sqrt[n]{a_n}\geq q$ definitivamente, allora $a_n\to+\infty$.
- Se esiste $q\in(0,1)$ tale che $\sqrt[n]{a_n}\leq q$ definitivamente, allora $a_n\to0$.
- Se esiste $q>1$ tale che $\frac{a_{n+1}}{a_n}\geq q$ definitivamente, allora $a_n\to+\infty$.
- Se esiste $q\in(0,1)$ tale che $\frac{a_{n+1}}{a_n}\leq q$ definitivamente, allora $a_n\to0$.

---

## 5. Dal rapporto alla radice

Sia $(a_n)$ una successione con $a_n>0$ definitivamente. Se

$$
\frac{a_{n+1}}{a_n}\to\ell
\qquad
\text{con }\ell\in[0,+\infty)\cup\{+\infty\},
$$

allora

$$
\sqrt[n]{a_n}\to\ell.
$$

Questo risultato rende il criterio del rapporto particolarmente utile: quando il rapporto tra termini consecutivi è semplice, permette di calcolare il limite della radice $n$-esima.

### 5.1 Dimostrazione per $0<\ell<+\infty$

Fissiamo $\varepsilon>0$ abbastanza piccolo da avere $\ell-\frac\varepsilon2>0$. Definitivamente,

$$
\ell-\frac\varepsilon2
\leq
\frac{a_{n+1}}{a_n}
\leq
\ell+\frac\varepsilon2.
$$

Esiste quindi $n_0$ tale che, iterando le due disuguaglianze, per ogni $n\geq n_0$:

$$
\left(\ell-\frac\varepsilon2\right)^{n-n_0}a_{n_0}
\leq a_n\leq
\left(\ell+\frac\varepsilon2\right)^{n-n_0}a_{n_0}.
$$

Prendendo la radice $n$-esima:

$$
\left(\ell-\frac\varepsilon2\right)
\sqrt[n]{\left(\ell-\frac\varepsilon2\right)^{-n_0}a_{n_0}}
\leq\sqrt[n]{a_n}
\leq
\left(\ell+\frac\varepsilon2\right)
\sqrt[n]{\left(\ell+\frac\varepsilon2\right)^{-n_0}a_{n_0}}.
$$

Le quantità dentro le due radici sono costanti positive; le loro radici $n$-esime tendono quindi a $1$. Il membro di sinistra tende a $\ell-\frac\varepsilon2$, quello di destra a $\ell+\frac\varepsilon2$. Definitivamente si ottiene

$$
\ell-\varepsilon\leq\sqrt[n]{a_n}\leq\ell+\varepsilon,
$$

che dimostra la tesi.

I casi $\ell=0$ e $\ell=+\infty$ si trattano con stime unilaterali dello stesso tipo.

### 5.2 Il caso $\ell=1$ e il mancato viceversa

Il teorema rapporto $\Rightarrow$ radice vale anche per $\ell=1$, anche se in quel caso il criterio del rapporto non dice se $(a_n)$ tenda a $0$, a $+\infty$ o a un valore finito.

Il viceversa è falso: la radice può avere limite anche quando il rapporto non converge. Per esempio, per

$$
a_n=1,2,1,2,1,2,\ldots
$$

i rapporti sono alternativamente

$$
2,\frac12,2,\frac12,\ldots
$$

e quindi non hanno limite. Tuttavia

$$
1\leq\sqrt[n]{a_n}\leq\sqrt[n]{2},
$$

perciò $\sqrt[n]{a_n}\to1$.

---

## 6. Gerarchia degli infiniti: esempi con il rapporto

La **[[Gerarchia degli infiniti|gerarchia degli infiniti]]** dice in che ordine crescono le successioni più comuni: prima le potenze, poi gli esponenziali, poi i fattoriali, poi $n^n$. Vediamo come si dimostra con il criterio del rapporto.

### 6.1 L’esponenziale domina ogni potenza

Consideriamo

$$
a_n=\frac{3^n}{n^{78}}.
$$

Il rapporto tra termini consecutivi è

$$
\frac{a_{n+1}}{a_n}
=\frac{3^{n+1}}{(n+1)^{78}}\frac{n^{78}}{3^n}
=3\left(\frac{n}{n+1}\right)^{78}
\to3>1.
$$

Per il criterio del rapporto,

$$
\frac{3^n}{n^{78}}\to+\infty.
$$

L’esponente $78$ non ha un ruolo speciale: lo stesso metodo mostra che un esponenziale di base maggiore di $1$ domina ogni potenza fissata di $n$.

### 6.2 Il fattoriale domina l’esponenziale

Sia

$$
a_n=\frac{n!}{3^n}.
$$

Allora

$$
\frac{a_{n+1}}{a_n}
=\frac{(n+1)!}{3^{n+1}}\frac{3^n}{n!}
=\frac{n+1}{3}
\to+\infty.
$$

Quindi

$$
\frac{n!}{3^n}\to+\infty.
$$

### 6.3 La successione $\frac{n^n}{n!}$

Poniamo

$$
a_n=\frac{n^n}{n!}.
$$

Si ha

$$
\begin{aligned}
\frac{a_{n+1}}{a_n}
&=\frac{(n+1)^{n+1}}{(n+1)!}\frac{n!}{n^n}\\
&=\frac{(n+1)^n}{n^n}
=\left(1+\frac1n\right)^n
\to e>1.
\end{aligned}
$$

Pertanto

$$
\frac{n^n}{n!}\to+\infty.
$$

### 6.4 Il limite di $\frac{\sqrt[n]{n!}}{n}$

Osserviamo che

$$
\frac{\sqrt[n]{n!}}{n}
=\sqrt[n]{\frac{n!}{n^n}}.
$$

Ponendo $a_n=\frac{n!}{n^n}$, il rapporto vale

$$
\frac{a_{n+1}}{a_n}
=\frac{(n+1)!}{(n+1)^{n+1}}\frac{n^n}{n!}
=\left(\frac{n}{n+1}\right)^n
=\frac1{\left(1+\frac1n\right)^n}
\to\frac1e.
$$

Per il teorema rapporto $\Rightarrow$ radice,

$$
\frac{\sqrt[n]{n!}}{n}\to\frac1e.
$$

---

## 7. Altri esempi

### 7.1 La successione $\frac{3^{n^2}}{n^n}$

Poniamo

$$
a_n=\frac{3^{n^2}}{n^n}.
$$

La radice $n$-esima è

$$
\sqrt[n]{a_n}=\frac{3^n}{n}.
$$

L’esponenziale domina la potenza $n$, quindi $\frac{3^n}{n}\to+\infty$. Per il criterio della radice,

$$
\frac{3^{n^2}}{n^n}\to+\infty.
$$

### 7.2 La successione $\frac{(2n)!}{n^n}$

Sia

$$
a_n=\frac{(2n)!}{n^n}.
$$

Il rapporto tra termini consecutivi è

$$
\begin{aligned}
\frac{a_{n+1}}{a_n}
&=\frac{(2n+2)!}{(n+1)^{n+1}}\frac{n^n}{(2n)!}\\
&=(2n+2)(2n+1)\frac{n^n}{(n+1)^{n+1}}\\
&=2(2n+1)\left(\frac{n}{n+1}\right)^n\\
&=\frac{2(2n+1)}{\left(1+\frac1n\right)^n}
\to+\infty.
\end{aligned}
$$

Per il criterio del rapporto,

$$
\frac{(2n)!}{n^n}\to+\infty.
$$

Un’altra dimostrazione parte dalla stima

$$
(2n)!\geq n^n\,n!,
$$

perché

$$
(2n)!=n!\,(n+1)(n+2)\cdots(2n)
$$

e ciascuno degli ultimi $n$ fattori è almeno $n$. Da questa stima segue

$$
\frac{(2n)!}{n^n}\geq n!\to+\infty.
$$

### 7.3 Radice $n$-esima di un coefficiente binomiale

Consideriamo

$$
a_n=\binom{3n}{n}=\frac{(3n)!}{(2n)!\,n!}.
$$

Il rapporto è

$$
\begin{aligned}
\frac{a_{n+1}}{a_n}
&=\frac{(3n+3)!}{(2n+2)!(n+1)!}\frac{(2n)!n!}{(3n)!}\\
&=\frac{(3n+3)(3n+2)(3n+1)}{(2n+2)(2n+1)(n+1)}\\
&\to\frac{27}{4}.
\end{aligned}
$$

Per il teorema rapporto $\Rightarrow$ radice,

$$
\sqrt[n]{\binom{3n}{n}}\to\frac{27}{4}.
$$

### 7.4 Confronto tra $\sqrt[n]{n}$ e $\sqrt[n]{n!}$

Applicando direttamente il teorema rapporto $\Rightarrow$ radice:

- se $a_n=n$, allora $\frac{a_{n+1}}{a_n}=\frac{n+1}{n}\to1$, quindi
  $$
  \sqrt[n]{n}\to1;
  $$
- se $a_n=n!$, allora $\frac{a_{n+1}}{a_n}=n+1\to+\infty$, quindi
  $$
  \sqrt[n]{n!}\to+\infty.
  $$

---

## 8. Radici $n$-esime di polinomi e somme

### 8.1 Radice $n$-esima di un polinomio

In generale, la radice $n$-esima di una quantità polinomiale positiva tende a $1$. Consideriamo per esempio

$$
\sqrt[n]{n^4+3n^3-7n+25}.
$$

Raccogliendo $n^4$:

$$
\sqrt[n]{n^4+3n^3-7n+25}
=\sqrt[n]{n^4}\,
\sqrt[n]{1+\frac3n-\frac7{n^3}+\frac{25}{n^4}}.
$$

Il primo fattore soddisfa

$$
\sqrt[n]{n^4}=\left(\sqrt[n]{n}\right)^4\to1.
$$

Il secondo radicando tende a $1$, quindi è definitivamente compreso, per esempio, tra $\frac12$ e $27$. Di conseguenza

$$
\sqrt[n]{\frac12}
\leq
\sqrt[n]{1+\frac3n-\frac7{n^3}+\frac{25}{n^4}}
\leq
\sqrt[n]{27}.
$$

I due estremi tendono a $1$, dunque anche il secondo fattore tende a $1$. Pertanto

$$
\sqrt[n]{n^4+3n^3-7n+25}\to1.
$$

### 8.2 Un’esponenziale dentro la radice

Calcoliamo

$$
\sqrt[n]{7^n-n^7+n^5\cos(n!)}.
$$

Raccogliendo $7^n$ dentro la radice:

$$
\sqrt[n]{7^n-n^7+n^5\cos(n!)}
=7\sqrt[n]{1-\frac{n^7}{7^n}+\frac{n^5\cos(n!)}{7^n}}.
$$

Poiché l’esponenziale $7^n$ domina ogni potenza di $n$,

$$
\frac{n^7}{7^n}\to0,
\qquad
\left|\frac{n^5\cos(n!)}{7^n}\right|
\leq\frac{n^5}{7^n}\to0.
$$

Il radicando tra parentesi tende quindi a $1$ ed è positivo definitivamente. Come nell’esempio precedente, la sua radice $n$-esima tende a $1$. Ne segue

$$
\sqrt[n]{7^n-n^7+n^5\cos(n!)}\to7.
$$

---

## 9. Schema operativo

Quando compare una successione positiva difficile da trattare direttamente, conviene procedere in questo ordine:

1. provare a calcolare $\sqrt[n]{a_n}$;
2. se la radice è ancora complicata, provare il rapporto $\frac{a_{n+1}}{a_n}$;
3. se il rapporto ha limite, usare il teorema rapporto $\Rightarrow$ radice;
4. confrontare il limite ottenuto con $1$ per applicare il criterio della radice o del rapporto.

Il valore $1$ è la soglia decisiva:

- un limite strettamente maggiore di $1$ produce crescita verso $+\infty$;
- un limite strettamente minore di $1$ produce convergenza a $0$;
- il valore $1$ è un caso di equilibrio e, da solo, non determina il comportamento della successione.
