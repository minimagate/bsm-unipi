---
type: lecture-note
course: Analisi 1
date: '2026-10-26'
title: Simboli di Landau, o piccolo e sviluppi dei limiti notevoli
source_files:
- AM1_26_L023.pdf
- AM1_26_L024.pdf
source_date: '2025-10-21'
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Analisi 1/Lectures/2026-10-26 - Simboli di Landau, o piccolo e sviluppi dei limiti notevoli.md
vault_hash: 821832e2ef4691eb6ae96f8a008e7fb11fe8ab05249870891d2fe7ddc5511c15
---

# Simboli di Landau, o piccolo e sviluppi dei limiti notevoli

Questa nota riunisce le due parti **023 e 024** della stessa lezione e prosegue [[2026-10-22 - Sottosuccessioni, limiti che non esistono e razionalizzazioni]]. La prima parte introduce il **linguaggio degli infinitesimi** (o piccolo, O grande, [[Equivalenza asintotica|equivalenza asintotica]]), cioè i **[[Simboli di Landau|simboli di Landau]]**, e ne dimostra le regole di calcolo. La seconda riscrive i [[2026-10-12 - Limiti di funzioni, continuità e limiti notevoli|limiti notevoli]] come **sviluppi** con o piccolo e li usa per calcolare [[Limite di una funzione|limiti]] in modo più meccanico.

## 1. I tre simboli

| Simbolo | Nome | Utilità per i limiti |
|---|---|---|
| $f=o(g)$ | o piccolo | **utilissimo** |
| $f=O(g)$ | O grande | poco utile |
| $f\sim g$ | equivalenza asintotica | **pericolosissima** |

### 1.1 o piccolo

**Setting.** $D\subseteq\mathbb R$, $x_0$ punto in cui ha senso fare i limiti (può essere $\pm\infty$, $5$, $7^-$, $8^+$, …), e $f,g:D\to\mathbb R$ due funzioni.

**Definizione.** Si dice che **$f$ è o piccolo di $g$ per $x\to x_0$**, e si scrive

$$
f(x)=o\bigl(g(x)\bigr)\quad\text{per }x\to x_0,
$$

se esiste una funzione $\omega:D\to\mathbb R$ tale che

$$
\boxed{f(x)=g(x)\,\omega(x)}\qquad\text{e}\qquad\boxed{\lim_{x\to x_0}\omega(x)=0}.
$$

**In breve:** $f$ è $g$ per qualcosa che tende a $0$. Meglio ancora: se $g$ tende a $0$, allora $f$ tende a $0$ «di più», cioè **$f$ batte $g$ nella velocità con cui tende a $0$**.

**Definizione quasi equivalente.** Se si può dividere per $g$ (cioè $g(x)\neq0$ almeno vicino a $x_0$), allora

$$
f(x)=o\bigl(g(x)\bigr)\ \text{per }x\to x_0
\iff
\lim_{x\to x_0}\frac{f(x)}{g(x)}=0.
$$

Basta prendere $\omega=f/g$.

### 1.2 Equivalenza asintotica e O grande

**Equivalenza asintotica.** $f(x)\sim g(x)$ per $x\to x_0$ se vale tutto come sopra ma con

$$
\lim_{x\to x_0}\omega(x)=1.
$$

In breve: $f$ e $g$ «pareggiano». Se si può dividere per $g$, equivale a $f/g\to1$.

**O grande.** $f(x)=O\bigl(g(x)\bigr)$ se vale tutto come sopra ma con $\omega$ **limitata in un intorno di $x_0$**. In breve: $f$ non perde da $g$.

> [!example] Esempio
> Per $x\to+\infty$ si ha $\sin x=O(1)$, perché $\omega(x)=\sin x$ è limitata (anche se non ha limite). Invece $x^2+x\sim x^2$ per $x\to+\infty$, perché $\frac{x^2+x}{x^2}=1+\frac1x\to1$.

### 1.3 Primi esempi

**Esempio 1: $x^3=o(x)$ per $x\to0$.**

- *Con la definizione:* $x^3=x\cdot x^2$, con $f=x^3$, $g=x$, $\omega=x^2\to0$.
- *Con la definizione quasi equivalente:* $\displaystyle\lim_{x\to0}\frac{x^3}{x}=0$.

**Fatto generale.** Per $x\to0$ (ricordando il [[Limite di una funzione|limite]] di una potenza):

$$
x^a=o(x^b)\iff a>b,
$$

perché $x^a=x^b\cdot x^{a-b}$ e $\omega=x^{a-b}\to0$ se e solo se $a>b$. Quindi **vicino a $0$ vince la potenza più alta**. *(Nota mia: per esponenti non interi si intende $x\to0^+$.)*

**Osservazione.** $\dfrac1{x^2}=o\left(\dfrac1{x^3}\right)$ per $x\to0$, anche se nessuna delle due tende a $0$: il rapporto è $x\to0$. L'o piccolo confronta velocità, non richiede infinitesimi.

**Esempio 2: $\sin(x^2)\arctan x=o(x^2)$ per $x\to0$.** Con la definizione quasi equivalente:

$$
\lim_{x\to0}\frac{\sin(x^2)\arctan x}{x^2}
=\lim_{x\to0}\underbrace{\frac{\sin(x^2)}{x^2}}_{\to1}\cdot\underbrace{\arctan x}_{\to0}=0,
\qquad
\omega(x)=\frac{\sin(x^2)}{x^2}\arctan x.
$$

## 2. Proprietà dell'o piccolo

Setting come sopra, tutto per $x\to x_0$. Supponiamo $f_1(x)=o(g(x))$ e $f_2(x)=o(g(x))$, cioè $f_1=g\,\omega_1$ e $f_2=g\,\omega_2$ con $\omega_1,\omega_2\to0$.

**Somma/differenza: $f_1\pm f_2=o(g)$.**

$$
f_1\pm f_2=g\,\underbrace{[\omega_1\pm\omega_2]}_{\omega_3\to0}.
$$

**Multiplo: $\lambda f_1=o(g)$.**

$$
\lambda f_1=\lambda g\,\omega_1=g\cdot\underbrace{\lambda\omega_1}_{\omega_3\to0}.
$$

Volendo è vero anche che $\lambda f_1=o(\lambda g)$.

**Prodotto: $f_1f_2=o(g^2)$.**

$$
f_1f_2=g\,\omega_1\cdot g\,\omega_2=g^2\cdot\underbrace{\omega_1\omega_2}_{\omega_3\to0\cdot0=0}.
$$

**Quoziente: nulla di furbo.**

$$
\frac{f_1}{f_2}=\frac{g\,\omega_1}{g\,\omega_2}=\frac{\omega_1}{\omega_2}\qquad\left[\tfrac00\Rightarrow\text{boh}\right].
$$

In breve: $f_1$ batte $g$, $f_2$ batte $g$, ma non si sa nulla su come finisce tra $f_1$ e $f_2$.

**Transitività.** Se $f=o(g)$ e $g=o(h)$, allora $f=o(h)$:

$$
f=g\,\omega_1,\quad g=h\,\omega_2\quad\Longrightarrow\quad f=h\cdot\underbrace{\omega_2\,\omega_1}_{\omega_3\to0\cdot0}.
$$

> **Riassunto.**
> $$
> o(g)\pm o(g)=o(g),\qquad \lambda\,o(g)=o(g),\qquad o(g)\cdot o(g)=o(g^2),
> $$
> $$
> \frac{o(g)}{o(g)}=\text{nulla di furbo},\qquad o\bigl(o(g)\bigr)=o(g).
> $$

### 2.1 Esempio: quale o piccolo è più forte

Tutto per $x\to0$:

| Affermazione | Vera? | Perché |
|---|---|---|
| $\sin(2x)\arctan x=o(x)$ | sì | dividendo per $x$ il limite è $0$ |
| $\sin(2x)\arctan^2x=o(x)$ | sì | dividendo per $x$ il limite è $0$ |
| $\sin(2x)\arctan^2x=o(x^2)$ | sì | dividendo per $x^2$ il limite è $0$ |
| $\sin(2x)\arctan^2x=o(x^3)$ | **no** | dividendo per $x^3$ il limite è $2$ |

La terza è **più forte** della seconda, cioè la implica (per transitività, perché $x^2=o(x)$): battere $x^2$ è più difficile che battere $x$.

### 2.2 Composizioni

Per $x\to0$, supponiamo $f(x)=o(x^a)$ con $a>0$, cioè $f(x)=x^a\,\omega(x)$ con $\omega\to0$.

**$f(x^3)=o(x^{3a})$.**

$$
f(x^3)=x^{3a}\cdot\underbrace{\omega(x^3)}_{\omega_1(x)\to0},
$$

dove $\omega(x^3)\to0$ per cambio di variabile $y=x^3$.

**$[f(x)]^3=o(x^{3a})$.**

$$
[f(x)]^3=[x^a\omega(x)]^3=x^{3a}\cdot\underbrace{\omega(x)^3}_{\omega_1\to0}.
$$

**$f(\arctan x)=o(x^a)$.**

$$
f(\arctan x)=(\arctan x)^a\,\omega(\arctan x)
=x^a\cdot\underbrace{\frac{(\arctan x)^a}{x^a}\cdot\omega(\arctan x)}_{\omega_1(x)\to1\cdot0}.
$$

**$\arctan\bigl(f(x)\bigr)=o(x^a)$.**

$$
\arctan\bigl(f(x)\bigr)=x^a\cdot\underbrace{\frac{\arctan(f(x))}{x^a}}_{\omega_1(x)},
\qquad
\omega_1(x)=\underbrace{\frac{\arctan(f(x))}{f(x)}}_{\to1}\cdot\underbrace{\frac{f(x)}{x^a}}_{\to0}\to1\cdot0=0.
$$

Il primo fattore tende a $1$ perché $f(x)\to0$ (essendo $a>0$); il secondo è proprio l'$\omega$ di $f$.

**Osservazione.** L'ultima dimostrazione funziona se si può dividere per $f$ (cioè $f(x)\neq0$ vicino a $0$). *(Nota mia: nei punti dove $f(x)=0$ si ha anche $\arctan(f(x))=0$, quindi il risultato resta vero ponendo il primo fattore uguale a $1$ lì.)*

## 3. Sviluppi: i limiti notevoli con o piccolo

Sempre per $x\to0$ (sono i [[Limiti notevoli|limiti notevoli]] riscritti):

$$
\begin{aligned}
\sin x&=x+o(x) & e^x&=1+x+o(x)\\
\arctan x&=x+o(x) & \log(1+x)&=x+o(x)\\
\cos x&=1+o(x) & \tan x&=x+o(x)\\
\cos x&=1-\frac{x^2}2+o(x^2) & \arcsin x&=x+o(x)
\end{aligned}
$$

$$
\boxed{(1+x)^a=1+ax+o(x)\qquad a\in\mathbb R}
$$

Ciascuno è una riscrittura del limite notevole corrispondente tramite la definizione quasi equivalente. Alcuni casi:

**$\sin x=x+o(x)$**, cioè $\sin x-x=o(x)$:

$$
\lim_{x\to0}\frac{\sin x-x}{x}=\lim_{x\to0}\left(\frac{\sin x}x-1\right)=1-1=0.
$$

**$\cos x=1+o(x)$**, cioè $\cos x-1=o(x)$:

$$
\lim_{x\to0}\frac{\cos x-1}{x}=\lim_{x\to0}\underbrace{\frac{\cos x-1}{x^2}}_{\to-\frac12}\cdot\underbrace{x}_{\to0}=0.
$$

**$\cos x=1-\frac{x^2}2+o(x^2)$**, cioè $\cos x-1+\frac{x^2}2=o(x^2)$:

$$
\lim_{x\to0}\left(\underbrace{\frac{\cos x-1}{x^2}}_{\to-\frac12}+\frac12\right)=-\frac12+\frac12=0.
$$

Il secondo sviluppo del coseno è più preciso del primo: dice anche **come** $\cos x$ si stacca da $1$.

**$(1+x)^a=1+ax+o(x)$** (include $a$ frazionario o negativo). Bisogna dimostrare che $\displaystyle\lim_{x\to0}\frac{(1+x)^a-1-ax}{x}=0$:

$$
\frac{(1+x)^a-1}{x}-a
=\frac{e^{a\log(1+x)}-1}{x}-a
=\underbrace{\frac{e^{a\log(1+x)}-1}{a\log(1+x)}}_{\to1}\cdot a\underbrace{\frac{\log(1+x)}{x}}_{\to1}-a
\longrightarrow a-a=0,
$$

dove il primo fattore tende a $1$ con $y=a\log(1+x)\to0$. *(Nota mia: il passaggio divide per $a$, quindi vale per $a\neq0$; per $a=0$ l'enunciato è banale.)*

**Successioni.** L'o piccolo si usa anche per le [[Successione|successioni]], ovviamente per $n\to+\infty$: $a_n=o(b_n)$ se e solo se $a_n=b_n\,\omega_n$ con $\omega_n\to0$.

### 3.1 Gli stessi limiti come equivalenze

Per $x\to0$:

$$
\sin x\sim x,\quad \arctan x\sim x,\quad \tan x\sim x,\quad \arcsin x\sim x,\quad \log(1+x)\sim x,
$$

$$
e^x\sim1+x,\quad \cos x\sim1-\frac{x^2}2,\quad \cos x\sim1,\quad (1+x)^a\sim1+ax.
$$

Le ultime righe mostrano perché $\sim$ è pericolosa (la [[Equivalenza asintotica|equivalenza asintotica]] perde informazione): $\cos x\sim1$ e $\cos x\sim1-\frac{x^2}2$ sono entrambe vere, ma solo la seconda contiene l'informazione che serve quando l'$1$ si cancella. L'o piccolo invece tiene traccia esplicitamente di quanto si sta trascurando.

## 4. Esercizi

### Esercizio 1: $\displaystyle\lim_{x\to0}\frac{\sin(2x)+e^{3x}-\cos x}{\arctan x+\tan^2x}=5$

**All'antica.** Divido sopra e sotto per $x$ e sopra aggiungo e tolgo $1$:

$$
\frac{\overbrace{\dfrac{\sin(2x)}{x}}^{\to2}+\overbrace{\dfrac{e^{3x}-1}{x}}^{\to3}+\overbrace{\dfrac{1-\cos x}{x^2}}^{\to\frac12}\cdot\overbrace{x}^{\to0}}
{\underbrace{\dfrac{\arctan x}{x}}_{\to1}+\underbrace{\dfrac{\tan^2x}{x^2}}_{\to1}\cdot\underbrace{x}_{\to0}}
\longrightarrow\frac{2+3+\frac12\cdot0}{1+1\cdot0}=5.
$$

**Oggi: sviluppo tutto.**

$$
\begin{aligned}
\sin(2x)&=2x+o(2x)=2x+o(x), & \cos x&=1+o(x),\\
e^{3x}&=1+3x+o(x), & \arctan x&=x+o(x),\\
\tan x&=x+o(x), & \tan^2x&=o(x).
\end{aligned}
$$

Sostituisco, usando tante volte che $o(x)+o(x)=o(x)$:

$$
\frac{2x+1+3x-1+o(x)}{x+o(x)}=\frac{5x+o(x)}{x+o(x)}
=\frac{5+\overbrace{\dfrac{o(x)}x}^{\to0}}{1+\underbrace{\dfrac{o(x)}x}_{\to0}}\longrightarrow5.
$$

> **Morale.** Le funzioni strane sono **polinomi + spazzatura**, e la spazzatura è raccolta dall'o piccolo.

### Esercizio 2: $\displaystyle\lim_{x\to0}\frac{e^{\arctan(2x)}-\sqrt[3]{1+x}}{\sin(5x)+\log(1-x)}=\frac5{12}$

**Modalità rapida (con $\sim$, come negli appunti).**

- Denominatore: $\sin(5x)\sim5x$, $\log(1-x)\sim-x$, quindi denominatore $\sim4x$.
- $e^{\arctan(2x)}\sim e^{2x}\sim1+2x$.
- $\sqrt[3]{1+x}=(1+x)^{1/3}\sim1+\frac13x$.

$$
\text{Frazione}\sim\frac{1+2x-1-\frac13x}{5x-x}\sim\frac{\frac53x}{4x}\sim\frac5{12}.
$$

*Versione con o piccolo (mia), che giustifica i passaggi.* Da $\arctan(2x)=2x+o(x)$ e $e^y=1+y+o(y)$:

$$
e^{\arctan(2x)}=1+2x+o(x),\qquad \sqrt[3]{1+x}=1+\frac x3+o(x),
$$

$$
\sin(5x)+\log(1-x)=5x+o(x)-x+o(x)=4x+o(x).
$$

Quindi

$$
\frac{\frac53x+o(x)}{4x+o(x)}=\frac{\frac53+\frac{o(x)}x}{4+\frac{o(x)}x}\longrightarrow\frac{5/3}4=\frac5{12}.
$$

Sommare e sottrarre equivalenze asintotiche non è lecito in generale (vedi l'esercizio 3); qui il risultato è giusto perché le parti principali non si cancellano del tutto.

### Esercizio 3: $\displaystyle\lim_{n\to+\infty}\sqrt{n^2+7n-4}-n=\frac72$

È lo stesso tipo dell'esempio 2 (sezione 4) di [[2026-10-22 - Sottosuccessioni, limiti che non esistono e razionalizzazioni]], risolto lì razionalizzando e ora con gli sviluppi.

> **Troppo rozzo.** «$\sqrt{n^2+7n-4}-n\sim n-n=0$». Sbagliato.

**Occhio:** è vero che $\sqrt{n^2+7n-4}\sim n$ (diviso per $n$ tende a $1$), ma non si possono sottrarre le equivalenze.

Raccolgo $n^2$ dentro la radice:

$$
n\left(1+\frac7n-\frac4{n^2}\right)^{1/2}-n
=\underbrace{n}_{+\infty}\underbrace{\left\{\left(1+\frac7n-\underbrace{\frac4{n^2}}_{o(1/n)}\right)^{1/2}-1\right\}}_{0}.
$$

Usando $(1+x)^{1/2}=1+\frac12x+o(x)$ con $x=\frac7n+o\left(\frac1n\right)$:

$$
=n\left\{\left(1+\frac7n+o\left(\frac1n\right)\right)^{1/2}-1\right\}
=n\left\{1+\frac12\cdot\frac7n+o\left(\frac1n\right)-1\right\}
=\frac72+o(1)\longrightarrow\frac72.
$$

**Osservazione: $n\cdot o\left(\frac1n\right)=o(1)$**, e $o(1)$ è sinonimo di «roba che tende a $0$»:

$$
n\cdot o\left(\frac1n\right)=n\cdot\frac1n\cdot\omega_n=\omega_n\to0.
$$

**Osservazione: le «seconde linee».** Le parti principali $n$ si sono semplificate, e in quel caso entrano in gioco i termini successivi dello sviluppo. Infatti

$$
\sqrt{n^2+7n-4}=n+o(n)
$$

è vera, ma non basta:

$$
\sqrt{n^2+7n-4}-n=\cancel n+o(n)-\cancel n=o(n)=\underbrace{n}_{\to+\infty}\cdot\underbrace{\omega_n}_{\to0}=\text{boh}.
$$

Tenendo conto delle seconde linee si ottiene invece lo sviluppo che serve:

$$
\boxed{\sqrt{n^2+7n-4}=n+\frac72+o(1)}.
$$

## Fonti e precisazioni

- `AM1_26_L023.pdf`: simboli di Landau, definizioni, proprietà dell'o piccolo, composizioni.
- `AM1_26_L024.pdf`: sviluppi dei limiti notevoli, equivalenze asintotiche, esercizi 1–3.

I due PDF sono le due parti della stessa lezione e riportano entrambi la data **21/10/2025**, conservata nel campo `source_date`.

Le parti segnate «mia» non compaiono nel PDF: la versione con o piccolo dell'esercizio 2, le precisazioni su $x\to0^+$, sul caso $a=0$ e sul caso $f(x)=0$ nelle composizioni. Negli appunti, nell'elenco delle equivalenze compare $(1+x)^a=1+ax$; qui è scritto $(1+x)^a\sim1+ax$, che è evidentemente l'intenzione.
