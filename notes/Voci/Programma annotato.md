---
title: Programma annotato
type: voce
categoria: notazione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-26 - Correttezza totale dei cicli, funzioni di terminazione e programmi annotati
alias:
- programmi annotati
sintesi: Un programma con le asserzioni scritte nei punti chiave, che rende visibili gli obblighi di dimostrazione.
---
Un **programma annotato** è un programma in cui le asserzioni usate nella dimostrazione di correttezza sono scritte esplicitamente tra un comando e l'altro, tra graffe, insieme all'invariante e alla funzione di terminazione dei cicli.

## Definizione

Lo schema di un `while` annotato è:

```text
{P}
CI;
{inv: Inv} {ft: expt}
while E do
    {Inv ∧ E}
    C
endw
{Inv ∧ ¬E}
{Q}
```

Le annotazioni non sono comandi eseguiti. Non sostituiscono la dimostrazione: servono a organizzarla in obblighi precisi, cioè inizializzazione, preservazione dell'invariante, non negatività, diminuzione e implicazione finale.

## Intuizione

È come una dimostrazione scritta in margine al codice: ogni riga dice che cosa si sa in quel punto. Le asserzioni intermedie di una sequenza si ricavano di solito *dal basso verso l'alto*, partendo dalla postcondizione e applicando l'[[Regola dell'assegnamento|assioma dell'assegnamento]] a ritroso.

## Esempi

- Per una sequenza `x := x+1; y := y-1` con postcondizione $x>y$, si annota prima $\{x>y-1\}$ (prima di `y := y-1`) e poi $\{x+1>y-1\}$ (prima di `x := x+1`).
- Nel programma della somma dei primi $n$ interi, si annotano $Inv\equiv s=\sum_{i=0}^{x-1}i\land0\leq x\leq n$ e $expt=n-x$.

## Vedi anche

- [[Invariante di ciclo]]
- [[Funzione di terminazione]]
- [[Tripla di Hoare]]
- [[Regola dell'assegnamento]]
