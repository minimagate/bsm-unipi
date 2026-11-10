---
title: Equazione diofantea lineare
type: voce
categoria: metodo
corsi:
- Aritmetica
introdotta_in: 2026-10-06 - Equazioni diofantee lineari e loro soluzioni
alias:
- equazioni diofantee lineari
- equazione diofantea
sintesi: Equazione lineare a coefficienti interi di cui si cercano soluzioni intere, risolvibile se e solo se il massimo comun divisore dei coefficienti divide il termine noto.
---

Un'**equazione diofantea lineare** in due incognite è un'equazione $ax+by=c$ con $a,b,c\in\mathbb{Z}$ di cui si cercano le soluzioni intere $(x,y)\in\mathbb{Z}^2$.

## Enunciato

Sia $d=\gcd(a,b)$. L'equazione $ax+by=c$ ha soluzioni intere se e solo se $d\mid c$. In tal caso, data una soluzione particolare $(x_0,y_0)$, tutte le soluzioni sono

$$x=x_0+\frac bd\,t,\qquad y=y_0-\frac ad\,t,\qquad t\in\mathbb{Z}.$$

## Intuizione

Geometricamente è una retta e le soluzioni sono i suoi punti a coordinate intere: o non ce n'è nessuno (se $d\nmid c$), o ce ne sono infiniti, equispaziati lungo il vettore $\left(\frac bd,-\frac ad\right)$. La struttura è quella "soluzione particolare + soluzione omogenea".

## Esempi

Per $6x+10y=8$: $d=2\mid8$. Da $6\cdot2+10\cdot(-1)=2$ moltiplicando per $4$ si ha $(x_0,y_0)=(8,-4)$, e le soluzioni sono $x=8+5t$, $y=-4-3t$. Invece $6x+10y=7$ non ha soluzioni.

## Come si dimostra

*Esistenza*: Bézout dà $au+bv=d$, quindi $(\gamma u,\gamma v)$ risolve con $c=d\gamma$. *Tutte le soluzioni*: si sottrae e si usa il [[Lemma di Euclide]] dopo aver diviso per $d$. Vedi [[2026-10-06 - Equazioni diofantee lineari e loro soluzioni#8. Determinazione di tutte le soluzioni|la lezione del 6 ottobre]].

## Vedi anche

- [[Identità di Bézout]]
- [[Lemma di Euclide]]
- [[Massimo comun divisore]]
- [[Congruenza lineare]]
