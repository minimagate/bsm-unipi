---
title: Regole di derivazione
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-27 - Derivate, differenziabilità e regole di derivazione
alias:
- derivata del prodotto
- derivata della funzione composta
- derivata della funzione inversa
sintesi: Formule per calcolare la derivata di somme, prodotti, quozienti, funzioni composte e funzioni inverse a partire dalle derivate delle funzioni elementari.
---

Le **regole di derivazione** permettono di derivare funzioni complicate senza tornare alla definizione di [[Derivata|derivata]].

## Enunciato

Se $f$ e $g$ sono derivabili in $x_0$:

$$
(f\pm g)'=f'\pm g',\qquad (\lambda f)'=\lambda f',\qquad (fg)'=f'g+fg',
$$

$$
\left(\frac1f\right)'=-\frac{f'}{f^2}\ \ (f(x_0)\neq0),\qquad \left(\frac fg\right)'=\frac{f'g-fg'}{g^2}.
$$

Per la composizione, se $f$ è derivabile in $x_0$ e $g$ in $f(x_0)$:

$$
[g(f(x))]'=g'(f(x))\cdot f'(x).
$$

Per la funzione inversa $g$ di $f$ (sotto opportune ipotesi) vale $g'(x)=\dfrac1{f'(g(x))}$.

## Intuizione

Sono il "calcolo con le derivate": ogni regola si legge anche con gli sviluppi $f(x_0+h)=f(x_0)+f'(x_0)h+o(h)$, moltiplicando e sommando i pezzi e tenendo solo il termine lineare. La regola della catena dice che le pendenze si moltiplicano: se $y$ cambia $f'$ volte più veloce di $x$ e $z$ cambia $g'$ volte più veloce di $y$, allora $z$ cambia $g'f'$ volte più veloce di $x$.

## Esempi

- $(\tan x)'=\frac{\cos^2x+\sin^2x}{\cos^2x}=\frac1{\cos^2x}$.
- $\bigl(\cos(x^3)\bigr)'=-\sin(x^3)\cdot3x^2$.
- Da $f=e^x$ e la regola dell'inversa: $(\log x)'=\frac1{e^{\log x}}=\frac1x$; da $f=\tan$: $(\arctan x)'=\frac1{1+x^2}$.

## Come si dimostra

Per somma e prodotto si aggiunge e si toglie un termine misto nel rapporto incrementale; per la composta si moltiplica e si divide per $f(x_0+h)-f(x_0)$ (con la difficoltà che può annullarsi). Dettagli nella [[2026-10-27 - Derivate, differenziabilità e regole di derivazione#6. Teoremi algebrici|lezione del 27 ottobre]].

## Vedi anche

- [[Derivata]]
- [[Composizione di funzioni]]
- [[Funzione inversa]]
- [[Differenziabilità]]
