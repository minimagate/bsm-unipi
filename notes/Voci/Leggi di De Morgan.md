---
title: Leggi di De Morgan
type: voce
categoria: teorema
corsi:
- Analisi 1
- Fondamenti di Programmazione
introdotta_in: 2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi
alias:
- De Morgan
- legge di De Morgan
sintesi: La negazione di una congiunzione è la disgiunzione delle negazioni e viceversa, e analogamente i quantificatori si scambiano quando si nega.
---
Le **leggi di De Morgan** dicono come si nega un "e" e un "oppure": la negazione scambia i connettivi (e i quantificatori) e nega i pezzi.

## Enunciato

Per ogni coppia di proposizioni $P$, $Q$:

$$
\neg(P\land Q)\equiv\neg P\lor\neg Q,\qquad
\neg(P\lor Q)\equiv\neg P\land\neg Q.
$$

La versione per i [[Quantificatore|quantificatori]] è:

$$
\neg\forall x\,P(x)\equiv\exists x\,\neg P(x),\qquad
\neg\exists x\,P(x)\equiv\forall x\,\neg P(x).
$$

## Intuizione

"Non è vero che $P$ e $Q$ sono entrambe vere" vuol dire che almeno una è falsa. "Non è vero che almeno una è vera" vuol dire che sono entrambe false. Lo stesso vale per i quantificatori: "non tutti" significa "qualcuno no", e "nessuno" significa "tutti no".

## Esempi

- $\neg(x\ge 0\land x\le 1)$ equivale a $x<0\lor x>1$.
- La negazione di "tutte le pecore sono nere" è "esiste almeno una pecora non nera" (e non "nessuna pecora è nera").

## Come si dimostra

Per le proposizioni basta confrontare le [[Tavola di verità|tavole di verità]] dei due membri. Il caso dei quantificatori è discusso nella lezione: [[2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi#3.4 Leggi di De Morgan per le proposizioni|leggi di De Morgan per le proposizioni]] e [[2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi#4. Negazione dei quantificatori|negazione dei quantificatori]].

## Vedi anche

- [[Quantificatore]]
- [[Connettivo logico]]
- [[Tavola di verità]]
- [[Contrapposizione]]
