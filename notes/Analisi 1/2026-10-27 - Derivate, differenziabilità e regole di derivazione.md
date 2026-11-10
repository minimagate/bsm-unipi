---
type: lecture-note
course: Analisi 1
date: '2026-10-27'
title: Derivate, differenziabilità e regole di derivazione
source_files:
- AM1_26_L025.pdf
- AM1_26_L026.pdf
source_date: '2025-10-22'
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Analisi 1/Lectures/2026-10-27 - Derivate, differenziabilità e regole di derivazione.md
vault_hash: d5167e49bf430eb7e557944b1188ad920f1e115c8acde9891b2c1c9a301e6c2b
---

# Derivate, differenziabilità e regole di derivazione

Questa nota riunisce le due parti **025 e 026** della stessa lezione e prosegue [[2026-10-26 - Simboli di Landau, o piccolo e sviluppi dei limiti notevoli]]. La prima parte definisce la **[[Derivata|derivata]]** come limite del rapporto incrementale e il **differenziale** tramite l'[[Simboli di Landau|o piccolo]], dimostra che le due nozioni coincidono (vedi [[Differenziabilità]]) e calcola le derivate delle funzioni elementari in due modi. La seconda parte ricava le **[[Regole di derivazione|regole di derivazione]]**: teoremi algebrici, funzione composta e funzione inversa.

## 1. Rapporto incrementale e derivata

**Setting.** $D\subseteq\mathbb R$, $f:D\to\mathbb R$, $x_0\in D$. Supporremo sempre che **$x_0$ sia interno a $D$**, cioè

$$
\exists r>0\ \text{t.c.}\ (x_0-r,x_0+r)\subseteq D.
$$

(Per ora basterebbe che $x_0\in D$ sia un [[Punto di accumulazione|punto di accumulazione]] di $D$.)

**Definizione (rapporto incrementale, *difference quotient*).**

$$
\frac{f(x_0+h)-f(x_0)}{h},
$$

definito almeno per ogni $h\in(-r,r)\setminus\{0\}$.

**Geometricamente** è il rapporto tra l'incremento della $y$, $f(x_0+h)-f(x_0)$, e il corrispondente incremento della $x$, $(x_0+h)-x_0=h$. Coincide con il **coefficiente angolare della retta secante** passante per $A=(x_0,f(x_0))$ e $B=(x_0+h,f(x_0+h))$.

**Definizione (derivata).** $f$ è **derivabile in $x_0$** se esiste ed è **reale** il [[Limite di una funzione|limite]]

$$
\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}{h}.
$$

In tal caso il limite si chiama **derivata di $f$ in $x_0$** e si indica, a scelta, con

$$
f'(x_0),\qquad \dot f(x_0),\qquad \frac{df}{dx}(x_0).
$$

**Geometricamente** $f'(x_0)$ è il coefficiente angolare della **retta tangente** al grafico nel punto $(x_0,f(x_0))$, che ha equazione

$$
\boxed{y=f(x_0)+f'(x_0)(x-x_0)}.
$$

## 2. Differenziabilità

**Definizione (differenziale).** $f$ è **[[Differenziabilità|differenziabile]] in $x_0$** se esiste un numero reale $\alpha$ tale che

$$
\boxed{f(x_0+h)=f(x_0)+\alpha h+o(h)\quad\text{per }h\to0}.
$$

**Proposizione.** Se $f$ è differenziabile in $x_0$, allora $\alpha$ è unico.

**Dimostrazione.** Supponiamo che ce ne siano due, $\alpha_1$ e $\alpha_2$:

$$
f(x_0+h)=f(x_0)+\alpha_1h+o(h),\qquad f(x_0+h)=f(x_0)+\alpha_2h+o(h).
$$

Sottraendo, e usando che $o(h)-o(h)=o(h)$:

$$
(\alpha_1-\alpha_2)h=o(h)\quad\Longrightarrow\quad \alpha_1-\alpha_2=\underbrace{\frac{o(h)}h}_{\to0}.
$$

A sinistra c'è una costante, quindi $\alpha_1-\alpha_2=0$.

**Teorema.** Nel solito setting, $f$ è derivabile in $x_0$ **se e solo se** è differenziabile in $x_0$. Inoltre $\alpha=f'(x_0)$.

**Dimostrazione.**

*Derivabile $\Rightarrow$ differenziabile.* Ipotesi: esiste $f'(x_0)$ come limite del rapporto incrementale. Tesi: $f(x_0+h)=f(x_0)+f'(x_0)h+o(h)$, il che (con la definizione quasi equivalente di o piccolo) equivale a

$$
\underbrace{\frac{f(x_0+h)-f(x_0)}{h}}_{\to f'(x_0)}-f'(x_0)\longrightarrow f'(x_0)-f'(x_0)=0.
$$

*Differenziabile $\Rightarrow$ derivabile.* Ipotesi: $f(x_0+h)=f(x_0)+\alpha h+o(h)$. Tesi: $f'(x_0)=\alpha$. Usando l'ipotesi,

$$
\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}{h}=\lim_{h\to0}\frac{\alpha h+o(h)}{h}=\lim_{h\to0}\left(\alpha+\frac{o(h)}h\right)=\alpha.
$$

**Uno sguardo avanti.** Da Analisi 2 in poi (più variabili) le due definizioni **non sono più equivalenti**, e per molte cose il differenziale è la nozione migliore.

### 2.1 Interpretazione geometrica

Con $A=(x_0+h,0)$, $B$ alla quota $f(x_0)$, $C$ sulla retta tangente e $D$ sul grafico, tutti sulla verticale $x=x_0+h$:

$$
\underbrace{f(x_0+h)}_{AD}=\underbrace{f(x_0)}_{AB}+\underbrace{\alpha h}_{BC}+\underbrace{o(h)}_{CD}.
$$

Quindi $f(x_0+h)$ è la somma di:

- un **termine costante** $f(x_0)$;
- un **termine lineare in $h$**, $BC$ (se dimezzo $h$, dimezza $BC$);
- un termine che tende a $0$ per $h\to0$, ma **più velocemente** di $h$: lo scarto tra grafico e tangente.

## 3. Derivate delle funzioni elementari

Ogni esempio si può fare in due modi: **1° modo** con il limite del rapporto incrementale, **2° modo** scrivendo $f(x_0+h)$ nella forma $f(x_0)+\alpha h+o(h)$ e leggendo $\alpha$.

**Esempio 1: $f(x)=x^2$, $f'(x_0)=2x_0$.**

- 1° modo: $\displaystyle\lim_{h\to0}\frac{(x_0+h)^2-x_0^2}{h}=\lim_{h\to0}\frac{2x_0h+h^2}{h}=\lim_{h\to0}(2x_0+h)=2x_0$.
- 2° modo: $(x_0+h)^2=\underbrace{x_0^2}_{f(x_0)}+\underbrace{2x_0}_{\alpha}h+\underbrace{h^2}_{o(h)}$.

**Esempio 2: $f(x)=x^3$, $f'(x_0)=3x_0^2$.** Con il 2° modo:

$$
(x_0+h)^3=\underbrace{x_0^3}_{f(x_0)}+\underbrace{3x_0^2}_{\alpha}h+\underbrace{3x_0h^2+h^3}_{o(h)}.
$$

Allo stesso modo (binomio) si fa $f(x)=x^n$ con $n\geq1$ intero: $(x^n)'=nx^{n-1}$.

**Esempio 3: $f(x)=e^x$, $f'(x_0)=e^{x_0}$.**

- 1° modo: $\displaystyle\lim_{h\to0}\frac{e^{x_0+h}-e^{x_0}}{h}=\lim_{h\to0}e^{x_0}\underbrace{\frac{e^h-1}{h}}_{\to1}=e^{x_0}$.
- 2° modo, con lo sviluppo $e^h=1+h+o(h)$ (un [[Limiti notevoli|limite notevole]]): $e^{x_0+h}=e^{x_0}(1+h+o(h))=e^{x_0}+\underbrace{e^{x_0}}_{\alpha}h+o(h)$.

**Esempio 4: $f(x)=\log x$, $f'(x_0)=\dfrac1{x_0}$** (con $x_0>0$). Con il 2° modo, usando $\log(1+t)=t+o(t)$ con $t=\frac h{x_0}$:

$$
\log(x_0+h)=\log\left[x_0\left(1+\frac h{x_0}\right)\right]=\log x_0+\log\left(1+\frac h{x_0}\right)
=\underbrace{\log x_0}_{f(x_0)}+\underbrace{\frac1{x_0}}_{\alpha}h+\underbrace{o\left(\frac h{x_0}\right)}_{o(h)}.
$$

**Esempio 5: $f(x)=\sin x$, $f'(x_0)=\cos x_0$.**

- 1° modo, con la formula di addizione (in alternativa la prostaferesi $\sin\alpha-\sin\beta=\dots$):

$$
\lim_{h\to0}\frac{\sin x_0\cos h+\cos x_0\sin h-\sin x_0}{h}
=\lim_{h\to0}\left\{\cos x_0\underbrace{\frac{\sin h}h}_{\to1}+\sin x_0\underbrace{\frac{\cos h-1}{h^2}}_{\to-\frac12}\underbrace{h}_{\to0}\right\}=\cos x_0.
$$

- 2° modo:

$$
\sin(x_0+h)=\sin x_0\cos h+\cos x_0\sin h=\sin x_0\bigl(1+o(h)\bigr)+\cos x_0\bigl(h+o(h)\bigr)=\sin x_0+\underbrace{\cos x_0}_{\alpha}h+o(h).
$$

> **Morale.** Limiti notevoli, sviluppi e derivate delle funzioni elementari sono **tre facce della stessa medaglia**.

## 4. Derivabile implica continua

**Teorema.** $f$ derivabile in $x_0\Rightarrow f$ [[Funzione continua|continua]] in $x_0$.

**Dimostrazione.** Per $h\neq0$

$$
f(x_0+h)=f(x_0)+\underbrace{\frac{f(x_0+h)-f(x_0)}{h}}_{\to f'(x_0)}\cdot\underbrace{h}_{\to0},
$$

quindi $\lim_{h\to0}f(x_0+h)=f(x_0)$. Con il cambio di variabile $x=x_0+h$ diventa $\lim_{x\to x_0}f(x)=f(x_0)$.

## 5. Strumenti per il calcolo delle derivate

- uso della definizione (solo nei casi estremi);
- tabellina delle derivate delle funzioni elementari (dimostrata con la definizione, §3);
- [[Teoremi algebrici sui limiti|teoremi algebrici]], in versione "per derivate";
- derivata della composizione;
- derivata della funzione inversa.

## 6. Teoremi algebrici

$$
(f\pm g)'=f'\pm g',\qquad (\lambda f)'=\lambda f',\qquad (fg)'=f'g+fg',
$$

$$
\left(\frac1f\right)'=-\frac{f'}{f^2},\qquad \left(\frac fg\right)'=\frac{f'g-fg'}{g^2}.
$$

### 6.1 Somma

**Enunciato.** Solito setting per $f$ e $g$, entrambe derivabili in $x_0$. Allora $s(x)=f(x)+g(x)$ è derivabile in $x_0$ e $s'(x_0)=f'(x_0)+g'(x_0)$.

**1° modo.** Si raggruppano i termini di $f$ e di $g$:

$$
\lim_{h\to0}\frac{s(x_0+h)-s(x_0)}{h}=\lim_{h\to0}\left[\frac{f(x_0+h)-f(x_0)}{h}+\frac{g(x_0+h)-g(x_0)}{h}\right]=f'(x_0)+g'(x_0).
$$

**2° modo.** Sommando gli sviluppi

$$
f(x_0+h)=f(x_0)+f'(x_0)h+o(h),\qquad g(x_0+h)=g(x_0)+g'(x_0)h+o(h)
$$

si ottiene

$$
\underbrace{f(x_0+h)+g(x_0+h)}_{s(x_0+h)}=\underbrace{f(x_0)+g(x_0)}_{s(x_0)}+\underbrace{[f'(x_0)+g'(x_0)]}_{s'(x_0)}h+o(h).
$$

### 6.2 Prodotto

**Enunciato.** Nelle stesse ipotesi, $p(x)=f(x)g(x)$ è derivabile in $x_0$ e

$$
\boxed{p'(x_0)=f'(x_0)g(x_0)+f(x_0)g'(x_0)}.
$$

**1° modo.** Si aggiunge e si toglie un **termine misto** (uno qualunque), qui $f(x_0+h)g(x_0)$:

$$
\begin{aligned}
\frac{p(x_0+h)-p(x_0)}{h}
&=\frac{f(x_0+h)g(x_0+h)-f(x_0+h)g(x_0)+f(x_0+h)g(x_0)-f(x_0)g(x_0)}{h}\\
&=\underbrace{f(x_0+h)}_{\to f(x_0)}\underbrace{\frac{g(x_0+h)-g(x_0)}{h}}_{\to g'(x_0)}+g(x_0)\underbrace{\frac{f(x_0+h)-f(x_0)}{h}}_{\to f'(x_0)}.
\end{aligned}
$$

Nel primo fattore si è usata la **continuità di $f$ in $x_0$** (§4).

**2° modo.** Moltiplicando i due sviluppi:

$$
\underbrace{f(x_0+h)g(x_0+h)}_{p(x_0+h)}=\underbrace{f(x_0)g(x_0)}_{p(x_0)}+\underbrace{\bigl(f(x_0)g'(x_0)+g(x_0)f'(x_0)\bigr)}_{p'(x_0)}h+o(h),
$$

dove nell'$o(h)$ finiscono tutti gli altri 6 termini del prodotto.

### 6.3 Reciproco e quoziente

**Enunciato.** Se $f$ è derivabile in $x_0$ e $f(x_0)\neq0$, allora $q(x)=\dfrac1{f(x)}$ è definita in un intorno di $x_0$, è derivabile in $x_0$ e

$$
q'(x_0)=-\frac{f'(x_0)}{f(x_0)^2}.
$$

**Dimostrazione.** Se $f(x_0)\neq0$, per **[[Permanenza del segno|permanenza del segno]]** (e continuità di $f$) $f(x)\neq0$ almeno in un piccolo intorno di $x_0$, quindi $q$ ha senso. A quel punto

$$
\frac{q(x_0+h)-q(x_0)}{h}=\frac1h\left(\frac1{f(x_0+h)}-\frac1{f(x_0)}\right)
=\underbrace{\frac{f(x_0)-f(x_0+h)}{h}}_{\to-f'(x_0)}\cdot\underbrace{\frac1{f(x_0+h)f(x_0)}}_{\to\frac1{f(x_0)^2}}.
$$

**Corollario (quoziente).**

$$
\left(\frac fg\right)'=\left(f\cdot\frac1g\right)'=f'\cdot\frac1g+f\left(\frac1g\right)'=\frac{f'}g-f\frac{g'}{g^2}=\frac{f'g-fg'}{g^2}.
$$

**Esempio: $(\tan x)'=\dfrac1{\cos^2x}=1+\tan^2x$.**

$$
(\tan x)'=\left(\frac{\sin x}{\cos x}\right)'=\frac{\cos x\cos x-(-\sin x)\sin x}{\cos^2x}=\frac{\cos^2x+\sin^2x}{\cos^2x}.
$$

Dividendo termine a termine si ottiene $1+\tan^2x$; usando $\cos^2x+\sin^2x=1$ si ottiene $\frac1{\cos^2x}$.

**Esempio: $\left(\dfrac1{x^n}\right)'=-\dfrac n{x^{n+1}}$.**

$$
\left(\frac1{x^n}\right)'=-\frac{nx^{n-1}}{(x^n)^2}=-\frac{nx^{n-1}}{x^{2n}}=-\frac n{x^{n+1}}.
$$

## 7. Funzione composta

Ci serve la [[Composizione di funzioni|composizione di funzioni]].

$$
\boxed{[g(f(x))]'=g'(f(x))\cdot f'(x)}
$$

**Enunciato** (saltati un po' di preliminari). Se $f$ è derivabile in $x_0$ e $g$ è derivabile in $f(x_0)$, allora $c(x)=g(f(x))$ è derivabile in $x_0$ e vale la formula sopra.

**Quasi dimostrazione.**

$$
\frac{c(x_0+h)-c(x_0)}{h}
=\frac{g(f(x_0+h))-g(f(x_0))}{f(x_0+h)-f(x_0)}\cdot\underbrace{\frac{f(x_0+h)-f(x_0)}{h}}_{\to f'(x_0)}.
$$

Chiamo $k=f(x_0+h)-f(x_0)$ il denominatore del primo fattore. Si ha $k\to0$ (per la continuità di $f$) e il primo fattore diventa

$$
\frac{g(f(x_0)+k)-g(f(x_0))}{k}\longrightarrow g'(f(x_0)).
$$

**Il problema** è che c'è una potenziale **divisione per $0$**: $k=f(x_0+h)-f(x_0)$ può annullarsi per $h\neq0$ arbitrariamente piccoli. Due vie d'uscita, che si vedranno in futuro:

- estensione del rapporto incrementale;
- lemma della **«sotto-sotto»** *(presumibilmente sulle sotto-sottosuccessioni; negli appunti c'è solo il nome)*.

## 8. Funzione inversa

Sia $g$ la [[Funzione inversa|funzione inversa]] di $f$. Sotto certe ipotesi (non precisate nella lezione)

$$
\boxed{g'(x)=\frac1{f'(g(x))}}.
$$

**Non dimostrazione.** Da $f(g(x))=x$, derivando con la regola della composta:

$$
f'(g(x))\cdot g'(x)=1\quad\leadsto\quad g'(x)=\frac1{f'(g(x))}.
$$

**Osservazione.** Andrebbe bene **SE** sapessi già che $g$ è derivabile: il passaggio la presuppone.

**Esempio 1: $g(x)=\log x$, $f(x)=e^x$.**

$$
g'(x)=\frac1{f'(g(x))}=\frac1{e^{\log x}}=\frac1x.
$$

**Esempio 2: $g(x)=\arctan x$, $f(x)=\tan x$.** Usando $(\tan)'=1+\tan^2$:

$$
g'(x)=\frac1{1+\tan^2(\arctan x)}=\frac1{1+x^2}.
$$

**Esempio 3: $g(x)=\arcsin x$, $f(x)=\sin x$.**

$$
g'(x)=\frac1{\cos(\arcsin x)}=\frac1{\sqrt{1-x^2}},
$$

dove $\cos(\arcsin x)=\sqrt{1-x^2}$ viene dalla [[2026-10-01 - Funzioni trigonometriche e funzioni inverse|lezione sulle funzioni trigonometriche inverse]] (vedi anche [[Funzioni trigonometriche inverse]]). *(Nota mia: vale per $x\in(-1,1)$; in $\pm1$ il denominatore si annulla.)*

## 9. Esempi di calcolo

$$
f(x)=\cos(x^3):\qquad f'(x)=-\sin(x^3)\cdot3x^2;
$$

$$
f(x)=\cos^3x:\qquad f'(x)=3\cos^2x\cdot(-\sin x).
$$

**Potenza con base ed esponente variabili.** Si scrive come esponenziale:

$$
f(x)=(\sin x)^{\cos x}=e^{\cos x\cdot\log(\sin x)},
$$

$$
f'(x)=e^{\cos x\log(\sin x)}\bigl(\cos x\log(\sin x)\bigr)'
=(\sin x)^{\cos x}\left\{-\sin x\log(\sin x)+\cos x\cdot\frac1{\sin x}\cos x\right\}.
$$

*(Nota mia: ha senso dove $\sin x>0$.)*

**Analogamente:**

$$
(a^x)'=\bigl(e^{x\log a}\bigr)'=a^x\log a,\qquad
(x^a)'=\bigl(e^{a\log x}\bigr)'=e^{a\log x}\cdot\frac ax=ax^{a-1}\quad(x>0).
$$

## Fonti e precisazioni

- `AM1_26_L025.pdf`: rapporto incrementale, derivata, differenziale, equivalenza tra le due, derivate delle funzioni elementari, derivabile ⇒ continua.
- `AM1_26_L026.pdf`: teoremi algebrici, funzione composta, funzione inversa, esempi di calcolo.

I due PDF sono le due parti della stessa lezione e riportano entrambi la data **22/10/2025**, conservata nel campo `source_date`.

Precisazioni rispetto agli appunti:
- negli appunti il rapporto incrementale è descritto come «rapporto tra l'incremento della $x$ e il corrispondente incremento della $y$»; la formula è incremento di $y$ diviso incremento di $x$, ed è così che è scritto qui;
- le parti segnate «mia» non compaiono nel PDF (dominio di $\arcsin'$ e di $(\sin x)^{\cos x}$, interpretazione del lemma «sotto-sotto»);
- ho aggiunto alcuni passaggi intermedi (il raggruppamento nel 1° modo della somma, il passaggio $e^{a\log x}\cdot\frac ax$, la continuità usata per $k\to0$ e per la permanenza del segno).
