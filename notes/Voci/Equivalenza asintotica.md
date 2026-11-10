---
title: Equivalenza asintotica
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-10-26 - Simboli di Landau, o piccolo e sviluppi dei limiti notevoli
alias:
- asintoticamente equivalente
- asintotico
sintesi: Due funzioni sono asintoticamente equivalenti quando il loro rapporto tende a uno, cioè vanno alla pari vicino al punto considerato.
---

Due funzioni sono **asintoticamente equivalenti** vicino a un punto quando "pareggiano": il loro rapporto tende a $1$. Si scrive $f\sim g$.

## Definizione

Con lo stesso setting dei [[Simboli di Landau|simboli di Landau]], $f(x)\sim g(x)$ per $x\to x_0$ se esiste $\omega$ con

$$
f(x)=g(x)\,\omega(x)\qquad\text{e}\qquad\lim_{x\to x_0}\omega(x)=1.
$$

Se si può dividere per $g$, è equivalente a $\lim_{x\to x_0}\frac{f(x)}{g(x)}=1$. Equivale anche a $f=g+o(g)$.

## Intuizione

È un modo rapido per dire "vicino a $x_0$ la funzione $f$ si comporta come $g$". I limiti notevoli diventano equivalenze: per $x\to0$, $\sin x\sim x$, $\arctan x\sim x$, $\log(1+x)\sim x$, $e^x-1\sim x$.

Attenzione: l'equivalenza va usata con prudenza. Funziona bene con prodotti e quozienti, ma **non** con somme e differenze, perché perde informazione. Per esempio $\sqrt{n^2+7n-4}\sim n$, ma non si può concludere che $\sqrt{n^2+7n-4}-n\sim n-n=0$: il limite vale infatti $\frac72$.

## Esempi

- $x^2+x\sim x^2$ per $x\to+\infty$, perché il rapporto è $1+\frac1x\to1$.
- Per $x\to0$ valgono sia $\cos x\sim1$ sia $\cos x\sim1-\frac{x^2}2$, ma solo la seconda conserva l'informazione utile quando l'$1$ si cancella.
- $\arccos(1-x)\sim\sqrt{2x}$ per $x\to0^+$.

## Vedi anche

- [[Simboli di Landau]]
- [[Parte principale]]
- [[Limiti notevoli]]
- [[Limite di una funzione]]
