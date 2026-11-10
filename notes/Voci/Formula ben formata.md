---
title: Formula ben formata
type: voce
categoria: definizione
corsi:
- Fondamenti di Programmazione
introdotta_in: 2026-10-08 - Sintassi e semantica della logica del primo ordine
alias:
- formule ben formate
- fbf
- termine
- termini
sintesi: Espressione costruita secondo le regole sintattiche della logica del primo ordine a partire da termini, predicati, connettivi e quantificatori.
---

Una **formula ben formata** (fbf) è una frase del linguaggio della [[Logica del primo ordine|logica del primo ordine]] costruita rispettando le regole della sintassi. Per costruirle servono prima i **termini**.

## Definizione

L'alfabeto contiene variabili $\mathcal V$, costanti $\mathcal C$, simboli di funzione $\mathcal F$ e di predicato $\mathcal P$ (ciascuno con la sua arietà), $\mathrm T$, $\mathrm F$, i [[Connettivo logico|connettivi]] e i quantificatori $\forall,\exists$.

I **termini** denotano individui e sono definiti induttivamente: ogni costante e ogni variabile è un termine; se $g\in\mathcal F$ ha arietà $n$ e $t_1,\dots,t_n$ sono termini, lo è anche $g(t_1,\dots,t_n)$.

Le **formule** sono:

- $\mathrm T$ e $\mathrm F$;
- le formule atomiche $p(t_1,\dots,t_n)$ con $p\in\mathcal P$;
- $(P)$, $\neg P$, $P\land Q$, $P\lor Q$, $P\Rightarrow Q$, $P\equiv Q$ se $P$ e $Q$ sono formule;
- $(\forall x.P)$ e $(\exists x.P)$ se $P$ è una formula e $x$ una variabile.

## Intuizione

Un termine denota un **individuo** (come $x+1$), una formula denota un **valore di verità** (come $\operatorname{dispari}(x+1)$). I predicati trasformano termini in formule, le funzioni trasformano termini in termini.

## Esempi

- Termini: $a$, $x$, $g(a)$, $h(x,g(a))$; con $+$ e $*$ anche $x+(1*z)$.
- Formula atomica: $\operatorname{pari}(2)$, oppure $x\le g(y)$.
- Formula: $(\forall x.\operatorname{pari}(x)\Rightarrow\operatorname{dispari}(x+1))$.

## Vedi anche

- [[Variabile libera e legata]]
- [[Quantificatore]]
- [[Interpretazione]]
- [[Logica del primo ordine]]
