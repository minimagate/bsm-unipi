---
title: Dimostrazione per assurdo
type: voce
categoria: metodo
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine
alias:
- per assurdo
- assurdo
sintesi: Per dimostrare una tesi si assume la sua negazione e si deriva una contraddizione.
---

La **dimostrazione per assurdo** dimostra una tesi mostrando che negarla porta a una contraddizione.

## Enunciato

Corrisponde a due equivalenze del [[Calcolo proposizionale|calcolo proposizionale]]:

$$
P\equiv(\neg P\Rightarrow\mathrm F),
\qquad
(Q\Rightarrow R)\equiv((Q\land\neg R)\Rightarrow\mathrm F).
$$

Per dimostrare $P$ si assume $\neg P$ e si deriva $\mathrm F$. Per dimostrare che da $Q$ segue $R$ si assumono insieme $Q$ e $\neg R$ e si deriva una contraddizione.

## Intuizione

"Supponiamo per assurdo che la tesi sia falsa..." e si arriva a qualcosa di impossibile: allora la tesi non poteva essere falsa. Rispetto alla [[Contrapposizione|contrapposizione]], che dimostra $\neg Q\Rightarrow\neg P$ al posto di $P\Rightarrow Q$, qui la contraddizione può essere con qualunque cosa nota.

## Esempi

Per dimostrare per assurdo $(P\lor Q\Rightarrow R)\Rightarrow(P\Rightarrow R)$ si nega tutta la formula:

$$
\begin{aligned}
&(P\lor Q\Rightarrow R)\land\neg(P\Rightarrow R)\\
&\equiv(\neg(P\lor Q)\lor R)\land P\land\neg R
\Rightarrow\neg(P\lor Q)\land P\\
&\equiv\neg P\land\neg Q\land P\equiv\mathrm F.
\end{aligned}
$$

## Vedi anche

- [[Contrapposizione]]
- [[Dimostrazione per casi]]
- [[Implicazione]]
- [[Tautologia]]
