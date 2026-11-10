---
title: Principio di inclusione-esclusione
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-09-30 - Successioni ricorrenti e formule combinatorie
alias:
- inclusione-esclusione
sintesi: La cardinalità di un'unione di insiemi si ottiene sommando e sottraendo alternativamente le cardinalità delle intersezioni.
---

Il **principio di inclusione-esclusione** permette di contare gli elementi di un'unione di insiemi che si sovrappongono, correggendo via via i conteggi doppi.

## Enunciato

Per due insiemi: $|A\cup B|=|A|+|B|-|A\cap B|$. In generale, per $A_1,\ldots,A_n$ finiti,

$$\left|\bigcup_{i=1}^nA_i\right|=\sum_{\varnothing\ne I\subseteq\{1,\ldots,n\}}(-1)^{|I|+1}\left|\bigcap_{i\in I}A_i\right|.$$

I segni sono $+,-,+,-,\ldots$ per intersezioni di $1,2,3,4,\ldots$ insiemi.

## Intuizione

Sommando le cardinalità conti due volte ciò che sta in due insiemi; sottrai le intersezioni a due a due, ma così gli elementi in tre insiemi sono stati tolti troppo, e li riaggiungi... Il meccanismo corregge a catena il sovraconteggio dei termini precedenti.

## Esempi

- Numeri da $1$ a $100$ divisibili per $2$ o per $3$: $50+33-16=67$.
- Funzioni suriettive $X\to Y$ con $|X|=n$, $|Y|=m$: $\sum_{k=0}^{m}(-1)^k\binom{m}{k}(m-k)^n$ (lezione del 7 ottobre).

## Come si dimostra

Un elemento che sta in esattamente $m$ insiemi contribuisce $\sum_{k=1}^{m}(-1)^{k+1}\binom{m}{k}=1$, per il [[Binomio di Newton]] con $(1-1)^m=0$. Vedi [[2026-09-30 - Successioni ricorrenti e formule combinatorie#9.2 Perché compaiono i segni alternati|la lezione del 30 settembre]].

## Vedi anche

- [[Binomio di Newton]]
- [[Funzione caratteristica]]
- [[Coefficiente binomiale]]
- [[Double counting]]
