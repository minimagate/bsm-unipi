---
title: Forma polare
type: voce
categoria: notazione
corsi:
- Geometria 1
introdotta_in: 2026-09-25 - Numeri complessi- operazioni, forma polare e radici
alias:
- forma trigonometrica
- coordinate polari
- argomento di un numero complesso
sintesi: La forma polare descrive un numero complesso con il suo modulo e il suo argomento, cioè l'angolo rispetto all'asse reale positivo.
---

La **forma polare** (o trigonometrica) di un [[Numero complesso|numero complesso]] non nullo lo scrive tramite la distanza dall'origine e l'angolo rispetto all'asse reale positivo.

## Definizione

Se $z=a+ib\neq 0$, sia $\rho=|z|=\sqrt{a^2+b^2}$ e sia $\theta$ l'**argomento** di $z$, misurato in senso antiorario a partire dalla semiretta reale positiva. Allora $a=\rho\cos\theta$, $b=\rho\sin\theta$ e

$$
z=\rho(\cos\theta+i\sin\theta).
$$

L'argomento è definito a meno di multipli di $2\pi$: $\arg(z)=\theta+2k\pi$, con $k\in\mathbb{Z}$. Per $z=0$ non è definito.

## Intuizione

Le coordinate cartesiane sono comode per la somma, quelle polari per il prodotto: se $w=\lambda(\cos\varphi+i\sin\varphi)$ allora

$$
zw=\rho\lambda\bigl[\cos(\theta+\varphi)+i\sin(\theta+\varphi)\bigr],
$$

cioè i [[Modulo di un numero complesso|moduli]] si moltiplicano e gli argomenti si sommano. Il prodotto diventa una rotazione combinata con una dilatazione.

## Esempi

- $-1=\cos\pi+i\sin\pi$.
- $i=\cos\frac\pi2+i\sin\frac\pi2$.
- Formula di De Moivre: $z^n=\rho^n[\cos(n\theta)+i\sin(n\theta)]$.

Attenzione al quadrante: per ricavare $\theta$ non basta $\arctan(b/a)$: punti in quadranti diversi hanno lo stesso rapporto $b/a$, quindi bisogna correggere con $\pi$ a seconda del segno di $a$ (vedi [[Funzioni trigonometriche inverse]]).

## Come si dimostra

La formula del prodotto segue dalle formule di addizione di seno e coseno: vedi [[2026-09-25 - Numeri complessi- operazioni, forma polare e radici#15. Prodotto in forma polare|il prodotto in forma polare]].

## Vedi anche

- [[Modulo di un numero complesso]]
- [[Radice n-esima di un numero complesso]]
- [[Funzioni trigonometriche]]
