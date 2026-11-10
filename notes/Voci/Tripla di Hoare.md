---
title: Tripla di Hoare
type: voce
categoria: notazione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-19 - Espressioni, comandi e triple di Hoare
alias:
- triple di Hoare
- Hoare
- semantica assiomatica
sintesi: Una tripla scrive che, partendo da stati che soddisfano una precondizione, l'esecuzione di un comando termina in stati che soddisfano una postcondizione.
---
Una **tripla di Hoare** $\{Q\}\ C\ \{R\}$ è la notazione con cui la semantica assiomatica descrive il comportamento di un comando: se si parte da uno stato che soddisfa $Q$, l'esecuzione di $C$ finisce in uno stato che soddisfa $R$.

## Definizione

In $\{Q\}\ C\ \{R\}$, $C$ è un comando e $Q$, $R$ sono *asserzioni*, cioè formule della logica del primo ordine sulle variabili dello stato. $Q$ è la precondizione, $R$ la postcondizione. La tripla è **soddisfatta** se per ogni stato $\sigma\models Q$ l'esecuzione di $C$ da $\sigma$ termina con successo in uno stato $\sigma'\models R$. Con questa lettura si parla di correttezza totale.

## Intuizione

La stessa tripla si può usare in tre modi. Dati $Q$ e $C$ si cerca $R$: si *descrive* che cosa fa il comando. Dati $Q$ e $R$ si cerca $C$: si *scrive un programma* che realizza una specifica. Dati tutti e tre si *dimostra* che il programma è corretto, ed è l'uso principale nel corso, con un proof system di assiomi e regole di inferenza.

## Esempi

- $\{x>1\}\ \mathtt{x:=x+1}\ \{x>2\}$ è soddisfatta: se $x>1$ prima, dopo l'incremento $x>2$.
- Con $Q=(x>0)$ e $R=(y=2\cdot x)$, il comando `y := x * 2` soddisfa la tripla, ma la soddisfa anche `y := 10; x := 5`: la specifica è troppo debole perché non fissa il valore iniziale di $x$.

## Vedi anche

- [[Precondizione e postcondizione]]
- [[Correttezza totale]]
- [[Regola dell'assegnamento]]
- [[Programma annotato]]
- [[Regola di inferenza]]
