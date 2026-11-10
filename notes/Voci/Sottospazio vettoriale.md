---
title: Sottospazio vettoriale
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-09-30 - Spazi vettoriali, esempi e sottospazi
alias:
- sottospazi
- sottospazio
- sottospazi vettoriali
- criterio di sottospazio
sintesi: Un sottospazio vettoriale è un sottoinsieme non vuoto di uno spazio vettoriale chiuso rispetto a somma e prodotto per scalare.
---

Un **sottospazio vettoriale** di uno [[Spazio vettoriale|spazio vettoriale]] $V$ è un sottoinsieme $W\subseteq V$ che, con le stesse operazioni di $V$, è a sua volta uno spazio vettoriale.

## Definizione (criterio di sottospazio)

$W\subseteq V$ è un sottospazio se e solo se:

1. $W\neq\varnothing$ (equivalentemente $\mathbf 0\in W$);
2. $\mathbf u,\mathbf v\in W\Rightarrow \mathbf u+\mathbf v\in W$;
3. $\alpha\in K,\ \mathbf u\in W\Rightarrow \alpha\mathbf u\in W$.

In modo compatto: $\alpha\mathbf u+\beta\mathbf v\in W$ per ogni $\mathbf u,\mathbf v\in W$ e $\alpha,\beta\in K$ (chiusura per [[Combinazione lineare|combinazioni lineari]]).

## Intuizione

Basta controllare che le operazioni non facciano uscire dall'insieme: gli altri assiomi sono già validi in $V$. Ogni sottospazio contiene lo zero (si ottiene come $0\cdot\mathbf v$), quindi una retta che non passa per l'origine non è mai un sottospazio.

## Esempi

- I sottospazi di $\mathbb{R}^2$ sono solo $\{\mathbf 0\}$, le rette per l'origine e tutto $\mathbb{R}^2$.
- In $\mathbb{R}^3$: $\{\mathbf 0\}$, le rette e i piani per l'origine, tutto $\mathbb{R}^3$.
- L'insieme delle soluzioni di un [[Sistema lineare|sistema lineare omogeneo]] è un sottospazio; $\{x_1+x_2=1\}$ non lo è.
- L'intersezione di due sottospazi è un sottospazio; l'unione in generale no.

## Come si dimostra

Si verificano le tre condizioni del criterio; vedi [[2026-09-30 - Spazi vettoriali, esempi e sottospazi#9.2 Criterio di sottospazio|il criterio di sottospazio]] e la [[2026-09-30 - Spazi vettoriali, esempi e sottospazi#13. Strategia pratica per verificare un sottospazio|strategia pratica]].

## Vedi anche

- [[Sottospazio generato]]
- [[Somma di sottospazi]]
- [[Base di uno spazio vettoriale]]
