---
title: Congruenza modulo n
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari
alias:
- congruenza
- congruenze
- congruenze modulo n
- aritmetica modulare
sintesi: Due interi sono congrui modulo n se la loro differenza è divisibile per n, cioè se hanno lo stesso resto nella divisione per n.
---

Due interi $a,b$ sono **congrui modulo $n$** (con $n>0$) se differiscono per un multiplo di $n$. È la base dell'aritmetica modulare.

## Definizione

$$a\equiv b\pmod n\iff n\mid(a-b)\iff a=b+kn\ \text{per qualche }k\in\mathbb{Z}.$$

Equivale ad avere lo stesso resto nella [[Divisione euclidea]] per $n$. È una [[Relazione di equivalenza]] su $\mathbb{Z}$ e rispetta somma, differenza e prodotto: da $a\equiv b$ e $c\equiv d$ segue $a+c\equiv b+d$ e $ac\equiv bd$. Attenzione alla cancellazione: da $ac\equiv bc$ si deduce solo $a\equiv b\pmod{n/\gcd(c,n)}$.

## Intuizione

È come guardare l'orologio: contano solo i resti, e il quadrante ha $n$ ore. Puoi sostituire un numero con un altro congruo in qualsiasi espressione fatta di somme e prodotti: ottimo per ridurre numeri grandi.

## Esempi

- $17\equiv2\pmod5$ perché $5\mid15$.
- $85\cdot38\equiv1\cdot3=3\pmod7$.
- Criterio del $3$: $10\equiv1\pmod3$, quindi un numero è congruo alla somma delle sue cifre.

## Come si dimostra

Vedi [[2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari#3. Congruenze modulo $n$|la lezione dell'8 ottobre]].

## Vedi anche

- [[Classe di congruenza]]
- [[Congruenza lineare]]
- [[Inverso modulo n]]
- [[Teorema cinese del resto]]
- [[Relazione di equivalenza]]
