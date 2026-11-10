---
title: Funzione periodica
type: voce
categoria: definizione
corsi:
- Analisi 1
introdotta_in: 2026-09-30 - Simmetrie, monotonia e grafici delle funzioni elementari
alias:
- funzioni periodiche
- periodo
sintesi: Una funzione è periodica se esiste un numero positivo T per cui il valore non cambia traslando l'argomento di T.
---
Una funzione **periodica** è una funzione il cui grafico si ripete identico a intervalli regolari.

## Definizione

$f\colon\mathbb{R}\to\mathbb{R}$ è periodica se esiste $T>0$ tale che

$$
f(x+T)=f(x)\qquad\forall x\in\mathbb{R}.
$$

Un tale $T$ è un **periodo**. Se $T$ è un periodo lo sono anche $2T,3T,\dots$; se c'è un periodo positivo più piccolo di tutti, si chiama **periodo minimo**.

## Intuizione

Conoscendo il grafico su un intervallo di lunghezza $T$, lo si ricostruisce per ripetizione. Per mostrare che una funzione è periodica basta esibire un periodo; mostrare che *non* lo è è in genere più delicato.

Attenzione: la somma di due funzioni periodiche con periodi diversi può non essere periodica. Se invece la funzione interna di una composizione è periodica, la composizione è periodica con lo stesso periodo.

## Esempi

- $\sin$ e $\cos$ hanno periodo minimo $2\pi$; $\tan$ ha periodo minimo $\pi$.
- $\sin^3 x$ è periodica di periodo $2\pi$.
- $\sin(x^2)$ non è periodica: i suoi zeri non sono equidistanziati.

## Vedi anche

- [[Funzioni trigonometriche]]
- [[Funzione pari e dispari]]
- [[Composizione di funzioni]]
- [[Funzione monotona]]
