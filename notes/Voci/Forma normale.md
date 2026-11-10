---
title: Forma normale
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine
alias:
- forme normali
- forma normale congiuntiva
- forma normale disgiuntiva
sintesi: Forma standard di una formula proposizionale come congiunzione di disgiunzioni (FNC) oppure come disgiunzione di congiunzioni (FND) di letterali.
---

Una **forma normale** è una forma standard in cui si porta una formula proposizionale per confrontarla con altre o per applicare metodi automatici di dimostrazione.

## Definizione

- Una **forma normale congiuntiva** (FNC) è una congiunzione di disgiunzioni di variabili proposizionali, eventualmente negate:
  $(P_1\lor P_2\lor\cdots)\land(Q_1\lor Q_2\lor\cdots)\land\cdots$
- Una **forma normale disgiuntiva** (FND) è una disgiunzione di congiunzioni di variabili proposizionali, eventualmente negate:
  $(P_1\land P_2\land\cdots)\lor(Q_1\land Q_2\land\cdots)\lor\cdots$

Si ottengono eliminando $\Rightarrow$ ed $\equiv$, spingendo le negazioni verso le variabili con le [[Leggi di De Morgan|leggi di De Morgan]] e applicando le leggi distributive.

## Intuizione

Due formule scritte in modo molto diverso possono avere la stessa forma normale, e allora sono [[Equivalenza logica|equivalenti]]. Il prezzo da pagare è che le distributività possono far crescere molto la formula. Le clausole della FNC sono proprio gli oggetti su cui lavora il [[Principio di risoluzione|principio di risoluzione]].

## Esempi

$$
\neg((P\Rightarrow Q)\land(R\Rightarrow P))
\equiv\neg(\neg P\lor Q)\lor\neg(\neg R\lor P)
\equiv(P\land\neg Q)\lor(R\land\neg P),
$$

che è una FND. Portando in FND anche $\neg(\neg Q\Rightarrow\neg P)\lor\neg(R\Rightarrow P)$ si trova $(\neg Q\land P)\lor(R\land\neg P)$, uguale a meno di commutatività: le due formule di partenza sono equivalenti.

## Vedi anche

- [[Principio di risoluzione]]
- [[Equivalenza logica]]
- [[Leggi di De Morgan]]
- [[Completezza funzionale]]
