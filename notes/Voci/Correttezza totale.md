---
title: Correttezza totale
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-20 - Regole di inferenza per le triple di Hoare e invarianti
alias:
- correttezza parziale
- correttezza di un programma
sintesi: Un programma è totalmente corretto se, dalle condizioni iniziali previste, termina davvero e produce lo stato finale richiesto.
---
La **correttezza totale** di un comando rispetto a una precondizione $P$ e a una postcondizione $Q$ significa che l'esecuzione *termina* e lo fa in uno stato che soddisfa $Q$. La **correttezza parziale** richiede meno: il risultato è giusto *se* il programma termina.

## Definizione

Si scrive $\models_{tot}\{P\}\,C\,\{Q\}$ se per ogni $\sigma\models P$ l'esecuzione di $C$ da $\sigma$ termina con successo in $\sigma'\models Q$. Si scrive $\models_{par}\{P\}\,C\,\{Q\}$ se per ogni $\sigma\models P$, *se* l'esecuzione termina, allora termina in uno stato che soddisfa $Q$. Nel proof system la differenza si vede nella funzione $\mathrm{def}$: per la correttezza totale le regole richiedono che le espressioni siano definite, per quella parziale si può ignorarla.

## Intuizione

La correttezza parziale non esclude i cicli infiniti, né un errore a metà esecuzione: dice solo che non si fornisce mai una risposta sbagliata. Per quella totale bisogna in più dimostrare tre cose: ogni espressione è definita, ogni corpo termina, e i cicli fanno un numero finito di iterazioni (con una [[Funzione di terminazione|funzione di terminazione]]).

## Esempi

- `while x>=y do x := x+1 endw` può essere parzialmente corretto rispetto a qualunque postcondizione (se non termina, non c'è niente da smentire), ma non totalmente corretto.
- `y := z div x` dopo `x := 0` non è totalmente corretto, perché divide per zero.

## Vedi anche

- [[Tripla di Hoare]]
- [[Invariante di ciclo]]
- [[Funzione di terminazione]]
- [[Comando iterativo]]
