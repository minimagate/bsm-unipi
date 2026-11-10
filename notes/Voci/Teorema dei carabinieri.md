---
title: Teorema dei carabinieri
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-06 - Successioni, limiti e teoremi di confronto
alias:
- carabinieri
- teorema del confronto
- teoremi di confronto
sintesi: Se una successione è compresa tra altre due che hanno lo stesso limite, allora ha anch'essa quel limite.
---
Il **teorema dei carabinieri** permette di calcolare un limite "schiacciando" la successione tra due altre, i due carabinieri, che portano il prigioniero con sé.

## Enunciato

Siano $a_n\le b_n\le c_n$ definitivamente e $a_n\to\ell$, $c_n\to\ell$ con $\ell\in\mathbb{R}$. Allora $b_n\to\ell$.

Esiste anche una versione per limiti infiniti (teorema del confronto): se $a_n\le b_n$ definitivamente e $a_n\to+\infty$ allora $b_n\to+\infty$; se $b_n\to-\infty$ allora $a_n\to-\infty$.

## Intuizione

Se due termini si avvicinano a $\ell$ da ambo i lati, quello in mezzo non ha scelta. Attenzione però: da $a_n\le b_n$ e $b_n\to5$ **non** si deduce il limite di $a_n$, e le disuguaglianze strette non passano al limite ($5-\frac3n<5-\frac1n$ ma entrambe tendono a $5$).

## Esempi

- $-\frac1n\le\frac{\sin n}{n}\le\frac1n$ implica $\frac{\sin n}{n}\to0$.
- $1\le\sqrt[n]{2}\le1+\frac1n$ implica $\sqrt[n]{2}\to1$.

## Come si dimostra

Fissato $\varepsilon>0$, da un certo indice in poi $\ell-\varepsilon\le a_n\le b_n\le c_n\le\ell+\varepsilon$, dunque $|b_n-\ell|\le\varepsilon$. I dettagli sono nella sezione [[2026-10-06 - Successioni, limiti e teoremi di confronto#7.2 Teorema dei carabinieri|Teorema dei carabinieri]].

## Vedi anche

- [[Limite di una successione]]
- [[Permanenza del segno]]
- [[Criterio della radice]]
- [[Teoremi algebrici sui limiti]]
