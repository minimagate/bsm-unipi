---
title: Costruzione di un ciclo
type: voce
categoria: metodo
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-29 - Aggiornamento degli array e tecniche di costruzione dei cicli
alias:
- costruzione di cicli
- tecniche di costruzione dei cicli
sintesi: Progettare un ciclo partendo dalla postcondizione, scegliendo invariante e guardia in modo che insieme implichino il risultato.
---
La **costruzione di un ciclo** è l'insieme delle tecniche per ricavare un `while` corretto dalla specifica, invece di scrivere il programma e poi verificarlo.

## Definizione

Data $\{pre\}\ C\ \{post\}$, si cerca una scomposizione $P\land G\Rightarrow post$ in cui $P$ sarà l'invariante e $G\equiv\neg E$ la negazione della guardia. Si progettano poi l'inizializzazione $CI$ (che rende vero $P$) e il corpo (che lo conserva facendo progredire una [[Funzione di terminazione|funzione di terminazione]]). Restano da controllare definitezza, invarianza e terminazione.

## Intuizione

È una strategia, non una ricetta. Le tecniche principali viste a lezione sono:

- **scomporre la postcondizione** in un invariante e una guardia, introducendo una variabile per un quantificatore esistenziale (il resto nella divisione);
- **sostituire una costante con una variabile**: al posto di $n$ nella somma $\sum_{i=0}^{n-1}a[i]$ si usa $x$, e il ciclo porta $x$ fino a $n$;
- **rafforzare l'invariante con una variabile ausiliaria**, quando un valore non è calcolabile direttamente;
- **conservare una quantità** del problema, come il MCD nell'algoritmo per sottrazioni.

## Esempi

- Fibonacci: l'invariante $x=\operatorname{fib}(i)$ non basta, perché `fib(i-1)` non è un'espressione del linguaggio. Si aggiunge `y` con $y=\operatorname{fib}(i-1)$ e il corpo `temp := x; x := x + y; y := temp; i := i + 1`.
- Somma di un array: invariante $s=\sum_{i=0}^{x-1}a[i]\land0\leq x\leq n$, guardia $x\neq n$.

## Vedi anche

- [[Invariante di ciclo]]
- [[Comando iterativo]]
- [[Successione di Fibonacci]]
- [[Array]]
