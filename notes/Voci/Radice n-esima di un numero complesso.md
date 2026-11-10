---
title: Radice n-esima di un numero complesso
type: voce
categoria: teorema
corsi:
- Geometria 1
introdotta_in: 2026-09-25 - Numeri complessi- operazioni, forma polare e radici
alias:
- radici n-esime
- radici di un numero complesso
sintesi: Ogni numero complesso non nullo ha esattamente n radici n-esime distinte, disposte sui vertici di un poligono regolare.
---

Una **radice $n$-esima** di un numero complesso $w$ è una soluzione dell'equazione $z^n=w$. Se $w\neq 0$ ce ne sono esattamente $n$, tutte distinte.

## Enunciato

Sia $w=R(\cos\theta+i\sin\theta)$ con $R=|w|>0$ e $n\geq 1$. Le soluzioni di $z^n=w$ sono

$$
z_k=\sqrt[n]{R}\left[\cos\left(\frac{\theta+2k\pi}{n}\right)+i\sin\left(\frac{\theta+2k\pi}{n}\right)\right],
\qquad k=0,1,\ldots,n-1.
$$

Se $w=0$ l'unica soluzione è $z=0$.

## Intuizione

Nei reali $\sqrt[n]{R}$ è un solo numero; nei complessi anche l'argomento si divide per $n$, e siccome è definito a meno di $2\pi$ si ottengono $n$ direzioni diverse. Le soluzioni stanno tutte su una circonferenza di raggio $\sqrt[n]{R}$ e sono i vertici di un poligono regolare con $n$ lati.

## Esempi

Le soluzioni di $z^3=-8$ hanno modulo $2$ e argomenti $\frac\pi3,\ \pi,\ \frac{5\pi}3$:

$$
z\in\{-2,\ 1+i\sqrt3,\ 1-i\sqrt3\},
$$

i vertici di un triangolo equilatero inscritto nella circonferenza di raggio $2$. Il caso $w=1$ dà le [[Radice n-esima dell'unità|radici dell'unità]].

## Come si dimostra

Si scrive $z=\rho(\cos\varphi+i\sin\varphi)$ e si impone $z^n=w$ usando la formula delle potenze della [[Forma polare|forma polare]]: i moduli danno $\rho^n=R$, gli argomenti $n\varphi=\theta+2k\pi$. Vedi [[2026-09-25 - Numeri complessi- operazioni, forma polare e radici#17. Radici $n$-esime di un numero complesso|il calcolo completo]].

## Vedi anche

- [[Forma polare]]
- [[Radice n-esima dell'unità]]
- [[Teorema fondamentale dell'algebra]]
- [[Numero complesso]]
