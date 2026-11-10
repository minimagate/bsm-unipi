---
title: Completezza funzionale
type: voce
categoria: teorema
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine
alias:
- connettivo NAND
- NAND
sintesi: Un insieme di connettivi è funzionalmente completo se con esso si esprimono tutti gli altri; ad esempio bastano la congiunzione e la negazione, oppure il solo NAND.
---

Un insieme di connettivi è **funzionalmente completo** se permette di esprimere tutti gli altri connettivi. Significa che non servono tutti i connettivi: ne bastano pochi.

## Enunciato

L'insieme $\{\land,\neg\}$ è funzionalmente completo, perché:

$$
P\Rightarrow Q\equiv\neg(P\land\neg Q),
\qquad
P\lor Q\equiv\neg(\neg P\land\neg Q),
$$

$$
(P\equiv Q)\equiv\neg(P\land\neg Q)\land\neg(Q\land\neg P).
$$

Lo sono anche $\{\lor,\neg\}$ e $\{\Rightarrow,\neg\}$. Il **NAND**, definito da $P\uparrow Q\equiv\neg(P\land Q)$, da solo è funzionalmente completo.

## Intuizione

Per i circuiti questo è importante: con un solo tipo di porta, il NAND, si può costruire qualunque funzione booleana. In logica si tengono comunque $\Rightarrow$ ed $\equiv$ per leggibilità e perché rappresentano direttamente le tecniche di dimostrazione.

## Esempi

Con il solo NAND: $\neg P\equiv P\uparrow P$ e $P\land Q\equiv(P\uparrow Q)\uparrow(P\uparrow Q)$.

| $P$ | $Q$ | $P\uparrow Q$ |
|---|---|---|
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf t$ | $\mathsf f$ |

## Come si dimostra

Ogni connettivo mancante si riscrive con le leggi di eliminazione e di De Morgan, come sopra: vedi [[2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine#4. Completezza funzionale dei connettivi|nella lezione del 23 settembre]].

## Vedi anche

- [[Connettivo logico]]
- [[Leggi di De Morgan]]
- [[Equivalenza logica]]
- [[Forma normale]]
