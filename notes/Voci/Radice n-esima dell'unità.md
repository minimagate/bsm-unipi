---
title: Radice n-esima dell'unità
type: voce
categoria: oggetto
corsi:
- Aritmetica
- Geometria 1
introdotta_in: 2026-10-01 - Fattorizzazione dei polinomi e radici complesse
alias:
- radici dell'unità
- radici n-esime dell'unità
sintesi: Le radici n-esime dell'unità sono le n soluzioni complesse dell'equazione z alla n uguale a 1 e formano un poligono regolare inscritto nella circonferenza unitaria.
---

Le **radici $n$-esime dell'unità** sono le soluzioni complesse dell'equazione $z^n=1$. Sono esattamente $n$ e stanno sulla circonferenza unitaria.

## Definizione

$$
z_k=e^{2\pi i k/n}=\cos\frac{2\pi k}{n}+i\sin\frac{2\pi k}{n},
\qquad k=0,1,\dots,n-1.
$$

Si ottengono scrivendo $z=re^{i\theta}$ e $1=e^{2\pi ik}$: i moduli danno $r=1$, gli argomenti $n\theta=2\pi k$. È il caso $w=1$ delle [[Radice n-esima di un numero complesso|radici n-esime di un numero complesso]].

## Intuizione

Sono i vertici di un poligono regolare con $n$ lati inscritto nella circonferenza unitaria, con un vertice in $1$. Se si moltiplica per $z_1$ si ruota di $\frac{2\pi}{n}$, e da lì si genera il poligono.

## Esempi

Per $z^6=1$ le sei radici sono

$$
1,\quad \tfrac12+i\tfrac{\sqrt3}{2},\quad -\tfrac12+i\tfrac{\sqrt3}{2},\quad -1,\quad -\tfrac12-i\tfrac{\sqrt3}{2},\quad \tfrac12-i\tfrac{\sqrt3}{2},
$$

i vertici di un esagono regolare. Poiché $z^6-1$ ha coefficienti reali, le radici non reali sono a coppie coniugate, e infatti

$$
z^6-1=(z-1)(z+1)(z^2+z+1)(z^2-z+1).
$$

## Come si dimostra

Si confrontano moduli e argomenti come sopra: vedi [[2026-10-01 - Fattorizzazione dei polinomi e radici complesse#16. Radici $n$-esime dell’unità|il calcolo nella lezione del 1 ottobre]].

## Vedi anche

- [[Forma polare]]
- [[Radice n-esima di un numero complesso]]
- [[Numero complesso]]
- [[Radice di un polinomio]]
