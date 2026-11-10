---
title: Comando iterativo
type: voce
categoria: oggetto
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-19 - Espressioni, comandi e triple di Hoare
alias:
- while
- ciclo while
- iterazione
sintesi: Il comando che ripete un corpo finché la guardia è vera, e quindi anche l'unico che può non terminare.
---
Il **comando iterativo** `while E do C endw` ripete il comando `C` (il *corpo*) finché l'espressione booleana `E` (la *guardia*) resta vera. È il costrutto con cui il linguaggio didattico del corso esprime i cicli.

## Definizione

Sintassi: `while E do C endw`, con `E` espressione booleana e `C` comando. La semantica, data dalla funzione $\mathcal C$ sugli stati, è ricorsiva:

$$
\mathcal C(\mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw},\sigma)=
\begin{cases}
\sigma&\text{se }\mathcal E(E,\sigma)=\mathbf f\\
\mathcal C(\mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw},\mathcal C(C,\sigma))&\text{se }\mathcal E(E,\sigma)=\mathbf t
\end{cases}
$$

Se la guardia è falsa si resta nello stato corrente; altrimenti si esegue il corpo e si riparte dal nuovo stato.

## Intuizione

Eseguire un `while` equivale a eseguire una sequenza $C_1;C_2;C_3;\dots$ di copie del corpo, che si ferma al primo stato in cui la guardia è falsa. La sequenza può essere vuota (guardia falsa subito) oppure infinita (la guardia resta vera per sempre). Per questo $\mathcal C$ è una funzione parziale, e per questo servono strumenti per dimostrare che un ciclo si ferma.

## Esempi

- `while x>=y do x := x - 1 endw` termina sempre: `x` scende di $1$ a ogni giro mentre `y` resta fissa.
- `while x>=y do x := x + 1 endw` non termina se all'inizio `x >= y`, perché la guardia resta vera.
- L'elevamento a potenza: `risultato := 1; while esponente > 0 do risultato := risultato * base; esponente := esponente - 1 endw` calcola $A^B$ con $B\geq0$.

## Vedi anche

- [[Invariante di ciclo]]
- [[Funzione di terminazione]]
- [[Costruzione di un ciclo]]
- [[Ciclo for]]
- [[Tripla di Hoare]]
