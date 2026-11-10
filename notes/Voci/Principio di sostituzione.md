---
title: Principio di sostituzione
type: voce
categoria: teorema
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza
alias:
- sostituzione per l'equivalenza
- sostituzione per l'implicazione
sintesi: Sostituendo in una formula una sottoformula con una equivalente si ottiene una formula equivalente; con una implicata, il verso dipende dalla polarità.
---

Il **principio di sostituzione** è la regola che giustifica ogni passaggio di una dimostrazione per trasformazioni successive: se due sottoformule sono equivalenti, una può prendere il posto dell'altra.

## Enunciato

**Per l'equivalenza.** Se $P\equiv Q$, allora per ogni formula $R$ vale $R\equiv R[Q/P]$, dove $R[Q/P]$ è $R$ con $P$ sostituita da $Q$:

$$
\frac{P\equiv Q}{R\equiv R[Q/P]}.
$$

**Per l'implicazione.** Se $P\Rightarrow Q$ e l'occorrenza sostituita di $P$ è **positiva** in $R$, allora $R\Rightarrow R[Q/P]$; se è **negativa**, allora $R\Leftarrow R[Q/P]$.

Un'occorrenza è negativa quando è preceduta da un numero dispari di negazioni o di antecedenti di implicazione, positiva altrimenti.

## Intuizione

È l'analogo logico del "sostituire uguali con uguali" dell'algebra. Per l'implicazione bisogna stare attenti, come con le disuguaglianze: sostituire in posizione negativa inverte il verso, un po' come moltiplicare per $-1$.

## Esempi

- Da $\neg\neg P\equiv P$ segue $(\neg\neg P\land Q)\equiv(P\land Q)$.
- Da $P\land Q\Rightarrow P$ non si può passare da «$\mathit{studia}\land\mathit{frequenta}\Rightarrow\mathit{supera}$» a «$\mathit{studia}\Rightarrow\mathit{supera}$»: la prima occorrenza è nell'antecedente, quindi negativa, e il verso si inverte.
- In $P\Rightarrow(\neg R\Rightarrow Q)$ la $P$ è negativa, mentre $R$ e $Q$ sono positive.

## Vedi anche

- [[Equivalenza logica]]
- [[Implicazione]]
- [[Tautologia]]
- [[Regola di inferenza]]
