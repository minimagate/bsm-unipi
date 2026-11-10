---
title: Coefficiente multinomiale
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-07 - Conteggio combinatorio e principio di inclusione-esclusione
alias:
- coefficienti multinomiali
- anagrammi
sintesi: Il coefficiente multinomiale conta i modi di ordinare oggetti con ripetizioni, cioè gli anagrammi di una parola con lettere ripetute.
---

Il **coefficiente multinomiale** generalizza il [[Coefficiente binomiale|binomiale]] e conta gli anagrammi di una parola con lettere ripetute.

## Definizione

Se una parola ha lunghezza $n$ e contiene $n_1$ copie di una lettera, $n_2$ di un'altra, ..., $n_k$ della $k$-esima (con $n_1+\cdots+n_k=n$), il numero di anagrammi distinti è

$$\binom{n}{n_1,\ldots,n_k}=\frac{n!}{n_1!\,n_2!\cdots n_k!}.$$

Conta anche le partizioni ordinate di un insieme di $n$ elementi in sottoinsiemi di cardinalità $n_1,\ldots,n_k$.

## Intuizione

Se tutte le lettere fossero distinte avresti $n!$ ordinamenti; ma scambiare tra loro le copie uguali non cambia la parola, quindi ogni anagramma è contato $n_i!$ volte per ciascuna lettera ripetuta, e bisogna dividere.

## Esempi

- `nonno`: $\frac{5!}{3!\,2!}=10$ anagrammi.
- `ana` (a, n, a): $\frac{3!}{2!}=3$.
- Con $k=2$ si ricade nel coefficiente binomiale.

## Come si dimostra

Vedi [[2026-10-07 - Conteggio combinatorio e principio di inclusione-esclusione#1.3. Formula generale: coefficiente multinomiale|la lezione del 7 ottobre]].

## Vedi anche

- [[Coefficiente binomiale]]
- [[Stelle e sbarre]]
- [[Double counting]]
- [[Cardinalità]]
