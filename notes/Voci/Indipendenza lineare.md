---
title: Indipendenza lineare
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-02 - Span, indipendenza lineare e basi vettoriali
alias:
- linearmente indipendente
- linearmente dipendente
- dipendenza lineare
- vettori indipendenti
sintesi: Dei vettori sono linearmente indipendenti se l'unica combinazione lineare che dà il vettore nullo è quella con tutti i coefficienti nulli.
---

Dei vettori sono **linearmente indipendenti** se nessuno di loro è combinazione lineare degli altri; in modo equivalente, se l'unica relazione lineare che li annulla è quella banale. Altrimenti sono **linearmente dipendenti**.

## Definizione

I vettori $v_1,\dots,v_n$ sono linearmente indipendenti se

$$
\alpha_1v_1+\cdots+\alpha_nv_n=0
\quad\Longrightarrow\quad
\alpha_1=\cdots=\alpha_n=0.
$$

Sono dipendenti se esistono scalari non tutti nulli con $\alpha_1v_1+\cdots+\alpha_nv_n=0$. Equivalentemente, i vettori sono dipendenti se e solo se uno di essi è [[Combinazione lineare|combinazione lineare]] degli altri.

## Intuizione

Indipendenza significa assenza di ridondanze: ogni vettore aggiunge una direzione nuova. Ha anche una conseguenza concreta: la rappresentazione di un vettore come combinazione degli $v_i$ è **unica**, quindi i coefficienti sono ben definiti (le [[Coordinate rispetto a una base|coordinate]]). Se una famiglia è dipendente lo è ogni famiglia più grande che la contiene.

## Esempi

- Un solo vettore $v$ è indipendente se e solo se $v\neq 0$.
- Due vettori sono dipendenti se e solo se sono multipli l'uno dell'altro.
- In $\mathbb{R}^3$, $(1,0,0),(0,1,0),(1,1,0)$ sono dipendenti perché la somma dei primi due è il terzo.
- $(-1,1,0),(-2,1,1)$ sono indipendenti.

## Come si dimostra

Per l'unicità dello sviluppo si sottraggono due rappresentazioni dello stesso vettore e si usa l'indipendenza: vedi [[2026-10-02 - Span, indipendenza lineare e basi vettoriali#9. Indipendenza lineare e unicità dello sviluppo|indipendenza e unicità dello sviluppo]].

## Vedi anche

- [[Combinazione lineare]]
- [[Base di uno spazio vettoriale]]
- [[Sottospazio generato]]
