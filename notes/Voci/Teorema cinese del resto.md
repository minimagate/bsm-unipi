---
title: Teorema cinese del resto
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari
alias:
- CRT
- teorema cinese
- sistemi di congruenze
sintesi: Un sistema di congruenze con moduli coprimi ha sempre soluzione, unica modulo il prodotto dei moduli.
---

Il **teorema cinese del resto** (CRT) descrive quando un sistema di congruenze ha soluzione e quante ne ha.

## Enunciato

Se $m_1,m_2$ sono [[Numeri coprimi|coprimi]], il sistema

$$\begin{cases}x\equiv a_1\pmod{m_1},\\x\equiv a_2\pmod{m_2}\end{cases}$$

ha sempre soluzione, unica modulo $m_1m_2$. Se i moduli non sono coprimi, il sistema ha soluzione se e solo se $\gcd(m_1,m_2)\mid a_2-a_1$, e allora la soluzione è unica modulo $\operatorname{mcm}(m_1,m_2)$.

## Intuizione

Sapere il resto modulo $3$ e il resto modulo $5$ equivale a sapere il resto modulo $15$: due informazioni "indipendenti" si fondono in una. Si risolve scrivendo $x=a_1+km_1$ e sostituendo nella seconda.

## Esempi

$x\equiv2\pmod3$ e $x\equiv3\pmod5$: da $x=2+3k$ si ha $3k\equiv1\pmod5$, quindi $k\equiv2$ e $x\equiv8\pmod{15}$.

## Come si dimostra

La riduzione a una [[Congruenza lineare]] nell'incognita $k$ e la condizione di compatibilità sono in [[2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari#11. Sistemi di congruenze|la lezione dell'8 ottobre]].

## Vedi anche

- [[Congruenza lineare]]
- [[Numeri coprimi]]
- [[Minimo comune multiplo]]
- [[Classe di congruenza]]
