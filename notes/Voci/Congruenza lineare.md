---
title: Congruenza lineare
type: voce
categoria: metodo
corsi:
- Aritmetica
introdotta_in: 2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari
alias:
- congruenze lineari
sintesi: Congruenza della forma a x congruo b modulo n, risolvibile se e solo se il massimo comun divisore di a e n divide b.
---

Una **congruenza lineare** è una congruenza $ax\equiv b\pmod n$ nell'incognita $x$.

## Enunciato

Sia $d=\gcd(a,n)$. La congruenza $ax\equiv b\pmod n$ ha soluzione se e solo se $d\mid b$. In tal caso, se $x_0$ è una soluzione, le soluzioni sono $x\equiv x_0\pmod{n/d}$, cioè $d$ classi distinte modulo $n$. Se $\gcd(a,n)=1$ c'è una sola classe: $x\equiv a^{-1}b\pmod n$.

## Intuizione

Equivale all'[[Equazione diofantea lineare|equazione diofantea]] $ax+ny=b$ (con $y=-k$), quindi si risolve con l'[[Identità di Bézout]]. Il criterio del MCD permette di dire se esistono soluzioni prima di cercarle.

## Esempi

- $4x\equiv6\pmod{10}$: $d=2\mid6$, soluzioni $x\equiv4$ e $x\equiv9\pmod{10}$.
- $14x\equiv15\pmod{21}$ è impossibile, perché $\gcd(14,21)=7\nmid15$.

## Come si dimostra

*Necessità*: $d$ divide $ax-kn=b$. *Sufficienza*: si divide per $d$, si usa Bézout su $a_1,n_1$ coprimi e si moltiplica per $b_1$. Vedi [[2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari#9. Congruenze lineari|la lezione dell'8 ottobre]].

## Vedi anche

- [[Congruenza modulo n]]
- [[Inverso modulo n]]
- [[Equazione diofantea lineare]]
- [[Teorema cinese del resto]]
