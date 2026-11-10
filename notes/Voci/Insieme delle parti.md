---
title: Insieme delle parti
type: voce
categoria: oggetto
corsi:
- Analisi 1
- Aritmetica
introdotta_in: 2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi
alias:
- insieme potenza
- parti di un insieme
sintesi: L'insieme delle parti di un insieme A è l'insieme di tutti i suoi sottoinsiemi e ha 2 alla n elementi se A ne ha n.
---
L'**insieme delle parti** di un insieme $A$ è l'insieme di tutti i sottoinsiemi di $A$.

## Definizione

$$
\mathcal{P}(A)=\{B : B\subseteq A\}.
$$

Contiene sempre $\varnothing$ e $A$ stesso. Se $A$ ha $n$ elementi, allora $\mathcal{P}(A)$ ha $2^n$ elementi.

## Intuizione

Per costruire un sottoinsieme si decide, per ciascuno degli $n$ elementi, se metterlo o no: $2$ scelte indipendenti per $n$ volte, cioè $2^n$ possibilità.

Attenzione a distinguere elemento e sottoinsieme: se $A=\{3,*,\square\}$ allora $3\in A$ e $\{3\}\in\mathcal{P}(A)$, ma $3\notin\mathcal{P}(A)$.

Si noti che $\mathcal{P}(A)$ è un insieme i cui elementi sono a loro volta insiemi: per questo è facile fare confusione tra $3$, $\{3\}$ e $\{\{3\}\}$, che sono tre oggetti diversi.

## Esempi

- Per $A=\{3,*,\square\}$:
  $\mathcal{P}(A)=\{\varnothing,\{3\},\{*\},\{\square\},\{3,*\},\{3,\square\},\{*,\square\},\{3,*,\square\}\}$, con $2^3=8$ elementi.
- $\mathcal{P}(\varnothing)=\{\varnothing\}$ ha un solo elemento.

## Come si dimostra

Il conteggio $2^n$ è spiegato nella sezione [[2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi#10. Insieme delle parti|Insieme delle parti]] della lezione del 23 settembre.

## Vedi anche

- [[Sottoinsieme]]
- [[Insieme]]
- [[Cardinalità]]
- [[Prodotto cartesiano]]
