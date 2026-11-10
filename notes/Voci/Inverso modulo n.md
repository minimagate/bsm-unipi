---
title: Inverso modulo n
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari
alias:
- inverso moltiplicativo
- inverso modulare
sintesi: L'inverso di a modulo n è una classe che moltiplicata per a dà uno; esiste se e solo se a e n sono coprimi.
---

L'**inverso di $a$ modulo $n$** è un intero $a^{-1}$ tale che $aa^{-1}\equiv1\pmod n$.

## Definizione

$a$ ha un inverso modulo $n$ se e solo se $\gcd(a,n)=1$. Se l'[[Identità di Bézout]] dà $ua+vn=1$, allora $ua\equiv1\pmod n$ e quindi $a^{-1}\equiv u\pmod n$. L'inverso permette di risolvere $ax\equiv b$ come $x\equiv a^{-1}b$ e di cancellare fattori coprimi con $n$.

## Intuizione

È la "divisione" nell'aritmetica modulare: non puoi dividere per $a$, ma puoi moltiplicare per $a^{-1}$. Si trova con l'algoritmo di Euclide esteso.

In pratica: per trovare $a^{-1}$ modulo $n$ si esegue l'algoritmo di Euclide su $a$ e $n$ e si risale all'indietro fino a ottenere $ua+vn=1$; il coefficiente $u$, ridotto modulo $n$, è l'inverso cercato.

## Esempi

Modulo $7$: $3\cdot5=15\equiv1$, quindi $3^{-1}\equiv5$. Modulo $6$ il numero $2$ non ha inverso, perché $\gcd(2,6)=2$.

## Come si dimostra

Vedi [[2026-10-08 - Fattorizzazione unica, congruenze e sistemi modulari#10. Calcolo dell’inverso modulo $n$|la lezione dell'8 ottobre]].

## Vedi anche

- [[Congruenza lineare]]
- [[Identità di Bézout]]
- [[Numeri coprimi]]
- [[Congruenza modulo n]]
