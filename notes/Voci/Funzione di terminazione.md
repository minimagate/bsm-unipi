---
title: Funzione di terminazione
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-26 - Correttezza totale dei cicli, funzioni di terminazione e programmi annotati
alias:
- terminazione
- funzione di terminazione di un ciclo
sintesi: Una funzione sugli stati, a valori naturali, che diminuisce a ogni iterazione e prova che il ciclo termina.
---
Una **funzione di terminazione** (o *bound function*) di un ciclo associa a ogni stato un numero naturale che scende strettamente a ogni iterazione: poiché non esistono successioni infinite strettamente decrescenti di naturali, il ciclo deve fermarsi.

## Definizione

Sia $expt$ (o $t$) l'espressione intera che dà il valore della funzione nello stato. Per `while E do C endw` con invariante $Inv$ servono due condizioni:

$$
Inv\Rightarrow expt\geq0,\qquad
\{Inv\land E\land expt=V\}\ C\ \{expt<V\}
$$

dove $V$ è una variabile di specifica che ricorda il valore di $expt$ prima del giro e che il corpo non modifica. La prima è l'ipotesi di terminazione, la seconda l'ipotesi di progresso.

## Intuizione

Si cerca una grandezza che misura quanto lavoro resta da fare. Entrambe le condizioni servono: una funzione costante è non negativa ma non progredisce; una funzione intera che scende potrebbe andare sotto zero all'infinito; anche una funzione reale positiva può scendere per sempre ($1,\frac12,\frac14,\dots$).

## Esempi

- Per `while x < n do ... x := x + 1 endw` si prende $expt=n-x$.
- Nel MCD per sottrazioni, con `x` e `y` positivi, vale $expt=x+y$: a ogni giro una delle due diminuisce.
- Nell'esempio geometrico dei punti rossi e blu, la lunghezza totale dei segmenti diminuisce per la disuguaglianza triangolare e assume solo un numero finito di valori.

## Come si dimostra

L'argomento è quello della successione degli stati $\sigma_0,\sigma_1,\dots$: i valori $a_i=F(\sigma_i)$ sono naturali e decrescenti. Vedi [[2026-10-26 - Correttezza totale dei cicli, funzioni di terminazione e programmi annotati#2.1 La sequenza degli stati|la lezione del 26 ottobre]].

## Vedi anche

- [[Invariante di ciclo]]
- [[Correttezza totale]]
- [[Comando iterativo]]
- [[Programma annotato]]
