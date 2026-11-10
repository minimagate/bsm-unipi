---
title: Invariante di ciclo
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-20 - Regole di inferenza per le triple di Hoare e invarianti
alias:
- invariante
- invarianti
- proprietà invariante
sintesi: Un invariante è una proprietà che vale prima del ciclo e dopo ogni iterazione, e che alla fine, insieme alla guardia falsa, dà il risultato.
---
Un **invariante di ciclo** è un'asserzione $\mathit{Inv}$ che vale prima della prima valutazione della guardia di un `while` e viene ristabilita a ogni iterazione, qualunque sia il numero di giri. È lo strumento per ragionare sui cicli senza sapere quante volte girano.

## Definizione

Per $\mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}$, $\mathit{Inv}$ è un invariante se $\{\mathit{Inv}\land E\}\,C\,\{\mathit{Inv}\}$. Allora, in correttezza parziale,

$$
\frac{\{\mathit{Inv}\land E\}\,C\,\{\mathit{Inv}\}}{\{\mathit{Inv}\}\ \mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\ \{\mathit{Inv}\land\neg E\}}
$$

Per una specifica $\{P\}\,W\,\{R\}$ servono anche $P\Rightarrow\mathit{Inv}$ (vale all'inizio) e $\mathit{Inv}\land\neg E\Rightarrow R$ (all'uscita dà il risultato).

## Intuizione

Si cerca un'unica asserzione che faccia da ponte tra tutte le asserzioni intermedie che si avrebbero per $k=1,2,3,\dots$ iterazioni. Non deve valere dopo ogni singolo comando del corpo, solo a ogni controllo della guardia. Dev'essere significativa: $T$ è invariante di qualunque ciclo ma non dice nulla.

## Esempi

- Per `while x > 0 do x := x - 1 endw` un invariante utile è $x\geq0$: all'uscita, con $\neg(x>0)$, dà $x=0$.
- Nel calcolo del fattoriale con `fatt := 1; x := 1; while x <= n do ...`, l'invariante è $fatt=(x-1)!\land1\leq x\leq n+1$.

## Come si dimostra

La regola segue dal fatto che, se si ripete $\{\mathit{Inv}\land E\}\,C\,\{\mathit{Inv}\}$ un numero qualsiasi di volte, $\mathit{Inv}$ resta vera; vedi [[2026-10-20 - Regole di inferenza per le triple di Hoare e invarianti#9. Il comando iterativo e le proprietà invarianti|la lezione del 20 ottobre]].

## Vedi anche

- [[Comando iterativo]]
- [[Funzione di terminazione]]
- [[Correttezza totale]]
- [[Costruzione di un ciclo]]
- [[Tripla di Hoare]]
