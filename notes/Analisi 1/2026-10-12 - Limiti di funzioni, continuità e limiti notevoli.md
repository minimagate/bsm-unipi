---
type: lecture-note
course: Analisi 1
date: '2026-10-12'
title: Limiti di funzioni, continuità e limiti notevoli
source_files:
- AM1_26_L017.pdf
- AM1_26_L018.pdf
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Analisi 1/Lectures/2026-10-12 - Limiti di funzioni, continuità e limiti notevoli.md
vault_hash: e1dcf7c067e6ac4c5c1bab8f8865d9050bcd83990a4a1db1c5ab52db42cca0bf
---

# Limiti di funzioni, continuità e limiti notevoli

Questa nota prosegue [[2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti]]: si passa dai limiti di successioni ai [[Limite di una funzione|limiti di funzioni]].

## 1. Setting

Sia $D\subseteq\mathbb{R}$ non vuoto e $f:D\to\mathbb{R}$. Vogliamo definire

$$
\lim_{x\to+\infty}f(x),\qquad
\lim_{x\to-\infty}f(x),\qquad
\lim_{x\to x_0}f(x),\qquad
\lim_{x\to x_0^+}f(x),\qquad
\lim_{x\to x_0^-}f(x).
$$

Ognuno di questi limiti ha quattro esiti possibili: $\ell\in\mathbb{R}$, $+\infty$, $-\infty$, oppure **N.E.** (non esiste: nessuno dei precedenti).

In tutte le definizioni che seguono, $M$ e $\varepsilon$ sono "la sfida" (interessano $M$ enormi in valore assoluto ed $\varepsilon$ molto vicini a $0$), mentre $k$ o $\delta$ sono "la risposta", che dipende dalla sfida.

---

## 2. Limiti per $x\to+\infty$

**Prerequisito:** $D$ non è limitato superiormente, cioè $\sup D=+\infty$.

- $\displaystyle\lim_{x\to+\infty}f(x)=+\infty$ se
  $$
  \forall M\in\mathbb{R}\ \exists k\in\mathbb{R}\ \text{t.c.}\ f(x)\geq M\quad\forall x\in D\cap[k,+\infty).
  $$
  Più $M$ è alto, più $k$ va spostato a destra.
- $\displaystyle\lim_{x\to+\infty}f(x)=-\infty$ se
  $$
  \forall M\in\mathbb{R}\ \exists k\in\mathbb{R}\ \text{t.c.}\ f(x)\leq M\quad\forall x\in D\cap[k,+\infty).
  $$
- $\displaystyle\lim_{x\to+\infty}f(x)=\ell\in\mathbb{R}$ se
  $$
  \forall\varepsilon>0\ \exists k\in\mathbb{R}\ \text{t.c.}\ |f(x)-\ell|\leq\varepsilon\quad\forall x\in D\cap[k,+\infty).
  $$
  Graficamente: da $k$ in poi il grafico resta nella striscia compresa tra $\ell-\varepsilon$ e $\ell+\varepsilon$.

> [!example] Esempio
> Verifichiamo che $\displaystyle\lim_{x\to+\infty}\frac1x=0$. Dato $\varepsilon>0$ basta prendere $k=\frac1\varepsilon$: per ogni $x\geq k$ si ha $\left|\frac1x-0\right|=\frac1x\leq\frac1k=\varepsilon$. Più $\varepsilon$ è piccolo, più $k$ si sposta a destra.

---

## 3. Limiti per $x\to-\infty$

**Prerequisito:** $\inf D=-\infty$.

Le definizioni sono speculari, con la semiretta $D\cap(-\infty,k]$ al posto di $D\cap[k,+\infty)$:

- $\displaystyle\lim_{x\to-\infty}f(x)=+\infty$ se $\forall M\in\mathbb{R}\ \exists k\in\mathbb{R}$ t.c. $f(x)\geq M$ per ogni $x\in D\cap(-\infty,k]$. Qui, più $M$ è alto, più $k$ va verso sinistra.
- $\displaystyle\lim_{x\to-\infty}f(x)=-\infty$ se $\forall M\in\mathbb{R}\ \exists k\in\mathbb{R}$ t.c. $f(x)\leq M$ per ogni $x\in D\cap(-\infty,k]$.
- $\displaystyle\lim_{x\to-\infty}f(x)=\ell\in\mathbb{R}$ se $\forall\varepsilon>0\ \exists k\in\mathbb{R}$ t.c. $|f(x)-\ell|\leq\varepsilon$ per ogni $x\in D\cap(-\infty,k]$.

### 3.1 Limite per eccesso e per difetto

Le solite varianti (come per le successioni):

$$
\lim_{x\to-\infty}f(x)=\ell^+
\iff
\forall\varepsilon>0\ \exists k\in\mathbb{R}\ \forall x\in D\cap(-\infty,k]\quad \ell<f(x)\leq\ell+\varepsilon,
$$

$$
\lim_{x\to-\infty}f(x)=\ell^-
\iff
\forall\varepsilon>0\ \exists k\in\mathbb{R}\ \forall x\in D\cap(-\infty,k)\quad \ell-\varepsilon\leq f(x)<\ell.
$$

> [!note] Cosa è obbligatorio e cosa no
> Nelle note alcuni dettagli sono marcati come **obbligatori** e altri come **trattabili** (cioè intercambiabili senza cambiare il significato):
> - obbligatori: $\varepsilon>0$ stretto e la disuguaglianza stretta $\ell<f(x)$ (risp. $f(x)<\ell$), che è proprio ciò che distingue $\ell^+$ da $\ell$;
> - trattabili: intervallo chiuso o aperto in $k$, e $\leq$ oppure $<$ dal lato di $\ell\pm\varepsilon$.

---

## 4. Limiti per $x\to x_0$

### 4.1 Punto di accumulazione

**Prerequisito su $D$:** $x_0$ è un **[[Punto di accumulazione|punto di accumulazione]]** di $D$, cioè

$$
\forall\delta>0\qquad \bigl(D\cap[x_0-\delta,x_0+\delta]\bigr)\setminus\{x_0\}\neq\emptyset.
$$

In parole: in ogni intervallo centrato in $x_0$ c'è almeno un punto di $D$ diverso da $x_0$ stesso.

> [!warning] Attenzione
> La condizione **non** è "$x_0\in D$" e **non** è "$x_0$ appartiene alla chiusura di $D$". Un punto di accumulazione può non stare in $D$; viceversa un punto isolato di $D$ sta in $D$ ma non è di accumulazione.

### 4.2 Definizioni

Indichiamo con $I_\delta=\bigl(D\cap[x_0-\delta,x_0+\delta]\bigr)\setminus\{x_0\}$ l'intorno bucato di $x_0$ in $D$.

- $\displaystyle\lim_{x\to x_0}f(x)=+\infty$ se $\forall M\in\mathbb{R}\ \exists\delta>0$ t.c. $f(x)\geq M$ per ogni $x\in I_\delta$.
- $\displaystyle\lim_{x\to x_0}f(x)=-\infty$ se $\forall M\in\mathbb{R}\ \exists\delta>0$ t.c. $f(x)\leq M$ per ogni $x\in I_\delta$.
- $\displaystyle\lim_{x\to x_0}f(x)=\ell\in\mathbb{R}$ se
  $$
  \forall\varepsilon>0\ \exists\delta>0\ \text{t.c.}\ |f(x)-\ell|\leq\varepsilon\quad\forall x\in I_\delta.
  $$

Gli $\varepsilon$ interessanti sono quelli vicini a $0$: più $\varepsilon$ diventa piccolo, più $\delta$ diventa piccolo.

> [!tip] Quanto vale $f(x_0)$?
> Non importa affatto: $x_0$ è escluso dall'intorno. Il limite è una *previsione* di quello che dovrebbe succedere in $x_0$ sulla base di quello che succede lì vicino. (E $f(x_0)$ potrebbe anche non esistere, se $x_0\notin D$.)

> [!example] Esempio
> Sia $f(x)=\frac{x^2-1}{x-1}$ con $D=\mathbb{R}\setminus\{1\}$. In $x_0=1$ la funzione non è definita, ma $1$ è di accumulazione per $D$ e per $x\neq1$ si ha $f(x)=x+1$. Quindi $\displaystyle\lim_{x\to1}f(x)=2$, anche se $f(1)$ non esiste.

### 4.3 Varianti: limiti destri/sinistri e per eccesso/difetto

Si combinano le idee precedenti. Alcuni esempi:

- $\displaystyle\lim_{x\to7^+}f(x)=-\infty$:
  $$
  \forall M\in\mathbb{R}\ \exists\delta>0\ \forall x\in D\cap(7,7+\delta]\quad f(x)\leq M.
  $$
  (Nelle note l'intervallo è scritto come $(x_0,x_0+\delta]$, con $x_0=7$.)
- $\displaystyle\lim_{x\to-\infty}f(x)=7^+$:
  $$
  \forall\varepsilon>0\ \exists k\in\mathbb{R}\ \forall x\in D\cap(-\infty,k]\quad 7<f(x)\leq7+\varepsilon.
  $$
- $\displaystyle\lim_{x\to8^-}f(x)=10^+$:
  $$
  \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D\cap[8-\delta,8)\quad 10<f(x)\leq10+\varepsilon.
  $$

Il limite destro usa solo i punti a destra di $x_0$ (intervallo $(x_0,x_0+\delta]$), il sinistro solo quelli a sinistra ($[x_0-\delta,x_0)$).

---

## 5. Continuità

**Definizione.** Solito setting $D\subseteq\mathbb{R}$, $f:D\to\mathbb{R}$, e supponiamo ora $x_0\in D$.

- Se
  $$
  \lim_{x\to x_0}f(x)=f(x_0),
  $$
  allora $f$ si dice **[[Funzione continua|continua]] in $x_0$**.
- $f$ si dice **continua in $D$** se è continua in ogni punto di $D$.

> [!note] Nota burocratica
> Se $x_0$ è **isolato** in $D$, cioè $\exists\delta>0$ con $D\cap[x_0-\delta,x_0+\delta]=\{x_0\}$, il limite non ha senso; per convenzione $f$ è continua in $x_0$ gratis.

Esplicitando la definizione di limite (con $x_0\in D$ si può includere anche $x_0$, perché lì $|f(x)-f(x_0)|=0$): $f$ è continua in $x_0$ se

$$
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D\cap[x_0-\delta,x_0+\delta]\quad |f(x)-f(x_0)|\leq\varepsilon.
$$

---

## 6. Strumenti base per il calcolo dei limiti di funzioni

- **Teoremi di confronto** (a due e a tre, i "[[Teorema dei carabinieri|carabinieri]]"): esattamente come per le successioni.
- **[[Teoremi algebrici sui limiti|Teoremi algebrici]]**: esattamente come per le successioni.
- **Funzioni continue**: se $f$ è continua in $x_0$, allora $\lim_{x\to x_0}f(x)=f(x_0)$.
- **Limiti notevoli** (§8).
- **Cambi di variabile** (§7.3).

### 6.1 Il "metateorema misterioso"

> Tutte le funzioni ottenute a partire da quelle elementari mediante operazioni algebriche e/o composizioni sono continue nei punti in cui non hanno problemi burocratici (denominatori che si annullano, logaritmi di quantità $\leq0$, …).

Per dimostrarlo davvero bisognerebbe provare:

1. che le funzioni elementari sono continue (dimostrazione diversa a seconda della funzione);
2. i teoremi algebrici;
3. che la composizione di funzioni continue è continua.

Seguono due esempi di questi passi.

---

## 7. Due dimostrazioni di continuità

### 7.1 Esempio 1: $2^x$ è continua su tutto $\mathbb{R}$

Per ogni $x_0\in\mathbb{R}$ va dimostrato che $\lim_{x\to x_0}2^x=2^{x_0}$. Si scrive

$$
|2^x-2^{x_0}|=2^{x_0}\,|2^{x-x_0}-1|,
$$

e il secondo fattore deve essere piccolo quando $x-x_0$ è piccolo.

**Caso $x>x_0$.** Dato $\varepsilon>0$ cerchiamo $\delta>0$ tale che

$$
2^{x-x_0}-1<\frac{\varepsilon}{2^{x_0}}\qquad\forall x\in[x_0,x_0+\delta].
$$

Ponendo $h=x-x_0$, vogliamo $\delta$ tale che

$$
2^h-1<\frac{\varepsilon}{2^{x_0}}\qquad\forall h\in[0,\delta].
$$

Dalle successioni sappiamo che $\sqrt[n]{2}\to1$ (vedi [[2026-10-08 - Criteri della radice e del rapporto e gerarchia degli infiniti|lezione precedente]], §2.1), quindi

$$
\exists n_0\in\mathbb{N}\ \text{t.c.}\ 2^{1/n}-1<\frac{\varepsilon}{2^{x_0}}\qquad\forall n\geq n_0.
$$

Scegliendo $\delta=\frac1{n_0}$, per la [[Funzione monotona|monotonia]] di $2^x$:

$$
2^h-1\leq2^{1/n_0}-1<\frac{\varepsilon}{2^{x_0}}\qquad\forall h\in\left[0,\tfrac1{n_0}\right].
$$

**Caso $x<x_0$.** Si pone $x-x_0=-h$ e si procede in maniera analoga.

> [!note] Perché non è circolare
> Qui si usa il limite $\sqrt[n]{2}\to1$, dimostrato con [[Disuguaglianza di Bernoulli|Bernoulli]] *senza* usare la continuità dell'esponenziale: è proprio il motivo per cui la lezione precedente insisteva nel non scrivere $2^{1/n}\to2^0$.

### 7.2 Esempio 2: continuità della composizione (caso semplice)

**Ipotesi:** $f:\mathbb{R}\to\mathbb{R}$ continua in $x_0$; $g:\mathbb{R}\to\mathbb{R}$ continua in $f(x_0)$.
**Tesi:** $g(f(x))$ è continua in $x_0$.

*Idea:* quando $x$ è vicino a $x_0$, $f(x)$ è vicino a $f(x_0)$; ma allora $g(f(x))$ è vicino a $g(f(x_0))$.

*Dimostrazione.* Bisogna provare che

$$
\forall\varepsilon>0\ \exists\delta>0\ \forall x\in[x_0-\delta,x_0+\delta]\quad |g(f(x))-g(f(x_0))|\leq\varepsilon.
$$

1. Sia dato $\varepsilon>0$.
2. Per la continuità di $g$ in $f(x_0)$ esiste $\delta_1>0$ tale che
   $$
   |g(y)-g(f(x_0))|\leq\varepsilon\qquad\forall y\in[f(x_0)-\delta_1,f(x_0)+\delta_1].
   $$
3. Uso la continuità di $f$ in $x_0$ con $\delta_1$ al posto di $\varepsilon$: ottengo $\delta_2>0$ tale che
   $$
   |f(x)-f(x_0)|\leq\delta_1\qquad\forall x\in[x_0-\delta_2,x_0+\delta_2].
   $$
4. $\delta_2$ è il $\delta$ cercato. Infatti per ogni $x\in[x_0-\delta_2,x_0+\delta_2]$ si ha $f(x)\in[f(x_0)-\delta_1,f(x_0)+\delta_1]$, e quindi, applicando il punto 2 con $y=f(x)$,
   $$
   |g(f(x))-g(f(x_0))|\leq\varepsilon.\qquad\blacksquare
   $$

### 7.3 Interpretazione operativa: il cambio di variabile

Per calcolare $\lim_{x\to x_0}g(f(x))$:

- pongo $y=f(x)$; quando $x\to x_0$ si ha $y\to f(x_0)$;
- il limite diventa
  $$
  \lim_{y\to f(x_0)}g(y)=g(f(x_0)).
  $$

Lo stesso schema ("pongo $y=\dots$ e osservo che $y\to\dots$") è quello usato negli esempi sui limiti notevoli.

---

## 8. Limiti notevoli

I **[[Limiti notevoli|limiti notevoli]]** sono organizzati "per generazioni":

**Padri**

$$
\lim_{x\to0}\frac{\sin x}{x}=1,
\qquad
\lim_{x\to+\infty}\left(1+\frac1x\right)^x=e.
$$

**Figli**

$$
\lim_{x\to0}\frac{1-\cos x}{x^2}=\frac12,
\qquad
\lim_{x\to0}\frac{e^x-1}{x}=1,
\qquad
\lim_{x\to0}\frac{\log(1+x)}{x}=1.
$$

**Nipoti**

$$
\lim_{x\to0}\frac{\arctan x}{x}=\lim_{x\to0}\frac{\tan x}{x}=\lim_{x\to0}\frac{\arcsin x}{x}=1,
$$

$$
\lim_{x\to0}\frac{a^x-1}{x}=\log a\qquad\forall a>0\quad(\log\text{ in base }e).
$$

**Limite dimenticato**

$$
\lim_{x\to0^+}x\log x=0.
$$

> [!note] Osservazione
> Sono tutti [[Forma indeterminata|forme]] del tipo $\frac00$, tranne quello che dà $e$ (forma $1^\infty$) e il limite dimenticato (forma $0\cdot\infty$).

---

## 9. Esempi

La tecnica ricorrente è moltiplicare e dividere per la quantità giusta, in modo da far comparire limiti notevoli, e poi usare un cambio di variabile.

### 9.1 $\displaystyle\lim_{x\to0}\frac{e^{3x}-1}{\sin x}$ (forma $\frac00$)

$$
\frac{e^{3x}-1}{\sin x}
=\underbrace{\frac{e^{3x}-1}{3x}}_{\to1}\cdot3\cdot\underbrace{\frac{x}{\sin x}}_{\to1}
\to3.
$$

Per il primo fattore pongo $y=3x$ e osservo che $y\to0$, ottenendo $\frac{e^y-1}{y}\to1$.

### 9.2 $\displaystyle\lim_{x\to0}\frac{\arctan(x^2)}{\sin^2x}$ (forma $\frac00$)

$$
\frac{\arctan(x^2)}{\sin^2x}
=\underbrace{\frac{\arctan(x^2)}{x^2}}_{\to1}\cdot\underbrace{\left(\frac{x}{\sin x}\right)^2}_{\to1^2}
\to1,
$$

ponendo $y=x^2$ nel primo fattore.

### 9.3 $\displaystyle\lim_{x\to0}\frac{\log(1+\tan x)}{\sin x}$

$$
\frac{\log(1+\tan x)}{\sin x}
=\underbrace{\frac{\log(1+\tan x)}{\tan x}}_{\to1}\cdot\underbrace{\frac{\tan x}{x}}_{\to1}\cdot\underbrace{\frac{x}{\sin x}}_{\to1}
\to1,
$$

ponendo $y=\tan x$ nel primo fattore.

### 9.4 $\displaystyle\lim_{x\to0}\frac{\sin(\cos x)}{\cos x}$

Non è una forma indeterminata: è una funzione continua tranquilla in $0$, quindi il limite vale $\frac{\sin1}{1}=\sin1$.

In alternativa: pongo $y=\cos x$, con $y\to1$ per $x\to0$; il limite diventa
$$
\lim_{y\to1}\frac{\sin y}{y}=\frac{\sin1}{1}=\sin1.
$$

### 9.5 $\displaystyle\lim_{x\to0}\frac{\log(\cos x)}{x^2}$ (forma $\frac{\log1}{0}=\frac00$)

$$
\frac{\log(\cos x)}{x^2}
=\underbrace{\frac{\log\bigl(1+(\cos x-1)\bigr)}{\cos x-1}}_{\to1}\cdot\underbrace{\frac{\cos x-1}{x^2}}_{\to-\frac12}
\to-\frac12.
$$

Per il primo fattore pongo $y=\cos x-1$, con $y\to0$, e il limite diventa $\lim_{y\to0}\frac{\log(1+y)}{y}=1$.

> [!note] Dettaglio aggiunto
> Per poter dividere per $\cos x-1$ serve $\cos x\neq1$, che vale per $0<|x|<2\pi$: quindi in un intorno bucato di $0$ la scrittura è lecita.
