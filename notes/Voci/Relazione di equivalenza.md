---
title: Relazione di equivalenza
type: voce
categoria: definizione
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-10-21 - Relazioni di equivalenza e strutture quoziente
alias:
- relazioni di equivalenza
- equivalenza
sintesi: Una relazione riflessiva, simmetrica e transitiva, che permette di considerare uguali elementi diversi di un insieme.
---

Una **relazione di equivalenza** su un insieme è un modo di dire quando due elementi sono "la stessa cosa" per uno scopo preciso, anche se come elementi dell'insieme restano distinti.

## Definizione

Sia $R$ una relazione su un [[Insieme|insieme]] $A$. Si dice **relazione di equivalenza** se per ogni $x,y,z\in A$ valgono:

1. **riflessività**: $xRx$;
2. **simmetria**: $xRy\Rightarrow yRx$;
3. **transitività**: $(xRy\ \text{e}\ yRz)\Rightarrow xRz$.

## Intuizione

Pensa a "avere lo stesso resto nella divisione per $2$": pari con pari, dispari con dispari. La relazione raggruppa gli elementi in blocchi, le [[Classe di equivalenza|classi di equivalenza]], che non si sovrappongono e ricoprono tutto $A$. Considerare "uguali" gli elementi dello stesso blocco è l'idea alla base dell'[[Insieme quoziente|insieme quoziente]].

## Esempi

- La [[Congruenza modulo n|congruenza modulo $n$]] su $\mathbb Z$: $a\equiv b\pmod n$ se $n\mid a-b$.
- Su $\mathbb Z\times(\mathbb Z\setminus\{0\})$ la relazione $(a,b)\sim(c,d)\iff ad=bc$ identifica le frazioni che rappresentano lo stesso numero razionale.
- La relazione $x\leq y$ su $\mathbb Z$ **non** è di equivalenza: è riflessiva e transitiva, ma non simmetrica.

## Come si dimostra

Per verificare che una relazione è di equivalenza si controllano le tre proprietà una per una; per la congruenza modulo $n$ la verifica è nella sezione [[2026-10-21 - Relazioni di equivalenza e strutture quoziente#5. Congruenza modulo $n$|sulla congruenza modulo n]] della lezione del 21 ottobre.

## Vedi anche

- [[Classe di equivalenza]]
- [[Insieme quoziente]]
- [[Congruenza modulo n]]
- [[Buona definizione]]
