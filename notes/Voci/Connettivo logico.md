---
title: Connettivo logico
type: voce
categoria: definizione
corsi:
- Analisi 1
- Fondamenti di Programmazione
introdotta_in: 2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza
alias:
- connettivi logici
- connettivi
- connettivo
sintesi: Operatore che combina proposizioni in una proposizione più complessa, il cui valore di verità dipende da quello delle componenti.
---

Un **connettivo logico** è un operatore che costruisce una nuova proposizione a partire da proposizioni già note, in modo che il suo valore di verità dipenda solo dai valori delle componenti.

## Definizione

I connettivi del [[Calcolo proposizionale|calcolo proposizionale]] sono: negazione $\neg$, congiunzione $\land$, disgiunzione $\lor$ (inclusiva), [[Implicazione|implicazione]] $\Rightarrow$ ed equivalenza $\equiv$. Ognuno è interpretato da una funzione booleana descritta da una [[Tavola di verità|tavola di verità]]:

| $P$ | $Q$ | $\neg P$ | $P\land Q$ | $P\lor Q$ | $P\Rightarrow Q$ | $P\equiv Q$ |
|---|---|---|---|---|---|---|
| $\mathsf t$ | $\mathsf t$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf f$ | $\mathsf f$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf f$ |
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |

## Intuizione

Sono per le proposizioni quello che $+$ e $\cdot$ sono per i numeri: operatori con cui costruire espressioni più grandi. Il connettivo che sta più "in alto" nella formula, cioè quello che non è argomento di nessun altro, è il **connettivo principale** e decide il valore finale.

## Esempi

- $\neg P$ è vera quando $P$ è falsa.
- $P\land Q$ è vera solo se sono vere entrambe; $P\lor Q$ è vera se lo è almeno una.
- La disgiunzione è **inclusiva**: «carne o pesce» in senso esclusivo richiederebbe un altro connettivo.

## Vedi anche

- [[Tavola di verità]]
- [[Implicazione]]
- [[Completezza funzionale]]
- [[Calcolo proposizionale]]
