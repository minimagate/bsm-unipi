---
title: Assioma di completezza
type: voce
categoria: teorema
corsi:
- Analisi 1
introdotta_in: 2026-09-28 - Assiomi dei reali e proprietà di completezza
alias:
- completezza
- completezza dei reali
- assioma di continuità
sintesi: Se un insieme di reali sta tutto a sinistra di un altro, esiste un numero reale compreso tra i due; è la proprietà che distingue i reali dai razionali.
---
L'**assioma di completezza** (o di continuità) è la proprietà che distingue $\mathbb{R}$ da $\mathbb{Q}$ ed è alla base della teoria dei limiti.

## Enunciato

Siano $A,B\subseteq\mathbb{R}$ non vuoti con $A$ a sinistra di $B$, cioè $a\le b$ per ogni $a\in A$ e $b\in B$. Allora

$$
\exists c\in\mathbb{R}\ \text{tale che}\ \forall a\in A,\ \forall b\in B:\quad a\le c\le b.
$$

Il numero $c$ garantisce l'esistenza di un punto di separazione, non la sua unicità.

## Intuizione

La retta reale non ha buchi. In $\mathbb{Q}$ l'assioma fallisce: per $A=\{x\in\mathbb{Q}: x\ge0,\ x^2\le2\}$ e $B=\{x\in\mathbb{Q}: x\ge0,\ x^2\ge2\}$ il punto di separazione dovrebbe avere quadrato $2$, ma non esiste nessun razionale con questa proprietà.

## Esempi

- Da questo assioma discende l'esistenza di $\sqrt2$.
- Ne discende l'esistenza dell'[[Estremo superiore|estremo superiore]] di ogni insieme non vuoto e limitato superiormente.
- Ne discende che $\mathbb{N}$ non è limitato superiormente.

## Come si dimostra

È un assioma: non si dimostra. Le conseguenze sono nella lezione [[2026-09-28 - Assiomi dei reali e proprietà di completezza#8. Assioma di completezza o di continuità|Assioma di completezza o di continuità]].

## Vedi anche

- [[Numero reale]]
- [[Estremo superiore]]
- [[Maggiorante]]
- [[Campo]]
