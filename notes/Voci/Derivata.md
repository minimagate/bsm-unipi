---
title: Derivata
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-27 - Derivate, differenziabilità e regole di derivazione
alias:
- derivabile
- derivabilità
- rapporto incrementale
sintesi: La derivata misura la velocità di variazione di una funzione in un punto ed è il coefficiente angolare della retta tangente al grafico.
---

La **derivata** di una funzione in un punto è il limite del rapporto incrementale: misura quanto velocemente cambia $f$ in quel punto, ed è la pendenza della retta tangente al grafico.

## Definizione

Sia $f:D\to\mathbb R$ e $x_0$ interno a $D$. Il **rapporto incrementale** è

$$
\frac{f(x_0+h)-f(x_0)}{h},
$$

cioè il coefficiente angolare della retta secante tra $(x_0,f(x_0))$ e $(x_0+h,f(x_0+h))$. La funzione è **derivabile in $x_0$** se esiste ed è reale il limite

$$
f'(x_0)=\lim_{h\to0}\frac{f(x_0+h)-f(x_0)}{h},
$$

detto derivata di $f$ in $x_0$ (si scrive anche $\dot f(x_0)$ o $\frac{df}{dx}(x_0)$). La retta tangente ha equazione $y=f(x_0)+f'(x_0)(x-x_0)$.

## Intuizione

Si prende la secante e si fa tendere $B$ verso $A$: la secante diventa la tangente. La derivata dice "di quanto sale $y$ per ogni unità di $x$", se zoomiamo abbastanza vicino al punto. È la stessa cosa che dice la [[Differenziabilità|differenziabilità]]: $f(x_0+h)=f(x_0)+f'(x_0)h+o(h)$.

Una funzione derivabile in $x_0$ è anche [[Funzione continua|continua]] in $x_0$.

## Esempi

- $f(x)=x^2$ ha $f'(x_0)=2x_0$, perché $\frac{(x_0+h)^2-x_0^2}{h}=2x_0+h\to2x_0$.
- $(e^x)'=e^x$, $(\sin x)'=\cos x$, $(\log x)'=\frac1x$.
- $|x|$ non è derivabile in $0$: i rapporti incrementali valgono $+1$ a destra e $-1$ a sinistra.

## Come si dimostra

Le derivate delle funzioni elementari si ricavano in due modi (con il limite o con gli sviluppi) nella [[2026-10-27 - Derivate, differenziabilità e regole di derivazione#3. Derivate delle funzioni elementari|lezione del 27 ottobre]]; il fatto che derivabile implica continua è nel paragrafo successivo.

## Vedi anche

- [[Differenziabilità]]
- [[Regole di derivazione]]
- [[Funzione continua]]
- [[Teorema di De L'Hôpital]]
