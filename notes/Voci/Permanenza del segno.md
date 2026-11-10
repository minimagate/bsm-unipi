---
title: Permanenza del segno
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-10-06 - Successioni, limiti e teoremi di confronto
sintesi: Se una successione converge a un limite positivo, allora i suoi termini sono positivi da un certo indice in poi.
---
Il teorema di **permanenza del segno** dice che un limite positivo "forza" i termini a essere positivi, almeno definitivamente.

## Enunciato

Se $a_n\to\ell$ con $\ell>0$, allora $a_n>0$ definitivamente. Più in generale $a_n$ resta definitivamente in ogni intervallo aperto che contiene $\ell$: ad esempio se $a_n\to\sqrt{17}$ allora $4\le a_n\le5$ definitivamente.

## Intuizione

Se i termini sono vicinissimi a un numero positivo, non possono essere negativi. Basta scegliere la tolleranza $\varepsilon$ abbastanza piccola da non toccare lo zero.

## Esempi

- $a_n=\frac{2n+1}{n}\to2>0$, quindi $a_n>0$ definitivamente (qui, per ogni $n$).
- Il viceversa è falso: $a_n=\frac1n>0$ per ogni $n$ ma il limite è $0$, non positivo.

## Come si dimostra

Si usa la definizione di limite con $\varepsilon=\ell/2$: definitivamente $\frac\ell2\le a_n\le\frac{3\ell}2$, e $\frac\ell2>0$. Si veda [[2026-10-06 - Successioni, limiti e teoremi di confronto#6.3 Permanenza del segno|Permanenza del segno]] nella lezione del 6 ottobre.

## Vedi anche

- [[Limite di una successione]]
- [[Proprietà definitivamente vera]]
- [[Teorema dei carabinieri]]
