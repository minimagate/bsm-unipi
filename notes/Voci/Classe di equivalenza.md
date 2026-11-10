---
title: Classe di equivalenza
type: voce
categoria: definizione
corsi:
- Aritmetica
introdotta_in: 2026-10-21 - Relazioni di equivalenza e strutture quoziente
alias:
- classi di equivalenza
sintesi: L'insieme di tutti gli elementi equivalenti a un elemento dato rispetto a una relazione di equivalenza.
---

La **classe di equivalenza** di un elemento è l'insieme di tutti gli elementi che gli sono equivalenti. Due classi o coincidono o sono disgiunte, quindi dividono l'insieme in blocchi senza sovrapposizioni.

## Definizione

Sia $R$ una [[Relazione di equivalenza|relazione di equivalenza]] su $A$ e $x\in A$. La classe di $x$ è

$$
[x]_R=\{y\in A\mid yRx\}.
$$

Si scrive anche $[x]$ o $\overline x$. Ogni elemento della classe è un **rappresentante** della classe. Per la riflessività $x\in[x]$.

**Teorema.** Per ogni $x,y\in A$ vale $[x]=[y]$ oppure $[x]\cap[y]=\varnothing$; inoltre $[x]=[y]\iff xRy$.

## Intuizione

Una classe è un "blocco" di elementi indistinguibili agli occhi della relazione. Scegliere un rappresentante è come scegliere un nome per quel blocco: nomi diversi possono indicare lo stesso blocco.

## Esempi

- Modulo $12$: $[1]_{12}=\{\dots,-11,1,13,25,\dots\}$ e $[5]_{12}=\{\dots,-7,5,17,29,\dots\}$.
- Tra le coppie $(a,b)$ che rappresentano frazioni: $[(1,2)]=[(2,4)]=[(3,6)]$ è il numero razionale $1/2$.

## Come si dimostra

Se $z\in[x]\cap[y]$, per simmetria e transitività si ottiene $xRy$ e quindi $[x]=[y]$; i dettagli sono nella [[2026-10-21 - Relazioni di equivalenza e strutture quoziente#2. Classi di equivalenza|sezione sulle classi]] della lezione del 21 ottobre.

## Vedi anche

- [[Relazione di equivalenza]]
- [[Insieme quoziente]]
- [[Classe di congruenza]]
- [[Classe laterale]]
