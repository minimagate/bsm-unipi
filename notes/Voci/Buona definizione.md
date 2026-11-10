---
title: Buona definizione
type: voce
categoria: metodo
corsi:
- Aritmetica
introdotta_in: 2026-10-22 - Omomorfismi tra anelli e teorema cinese
alias:
- ben definita
- ben definito
- buona posizione
sintesi: Verifica che una funzione definita tramite rappresentanti di classi non dipenda dal rappresentante scelto.
---

La **buona definizione** (o buona posizione) è la verifica che una regola scritta usando dei rappresentanti definisca davvero una funzione: il risultato deve dipendere solo dalla classe, non dal rappresentante scelto.

## Enunciato

Sia $f\colon A/{\sim}\to B/{\approx}$ definita da $f([a])=[g(a)]$. Per dimostrare che $f$ è ben definita bisogna verificare che

$$
[a]=[b]\quad\Longrightarrow\quad[g(a)]=[g(b)].
$$

## Intuizione

Una classe ha molti nomi (i rappresentanti). Se la formula cambia risposta cambiando nome, la formula non descrive una funzione sulla classe. Per esempio, "il numeratore" non è una funzione ben definita sui numeri razionali: $1/2$ e $2/4$ sono lo stesso numero ma hanno numeratori diversi.

## Esempi

- Somma e prodotto in $\mathbb Z/n\mathbb Z$: $[a]_n+[b]_n=[a+b]_n$ è ben posta perché, se $a\equiv a'$ e $b\equiv b'$ allora $a+b\equiv a'+b'$.
- $\mathbb Z/n\mathbb Z\to\mathbb Z/m\mathbb Z$, $[a]_n\mapsto[a]_m$ è ben definita se e solo se $m\mid n$. Per $\mathbb Z/4\mathbb Z\to\mathbb Z/3\mathbb Z$ non lo è: $[0]_4=[4]_4$ ma $[0]_3\neq[4]_3=[1]_3$.

## Come si dimostra

Di solito basta prendere due rappresentanti della stessa classe e mostrare che le immagini coincidono. Un caso tipico è la mappa $\varphi\colon\mathbb Z/mn\mathbb Z\to\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z$, trattato nella sezione [[2026-10-22 - Omomorfismi tra anelli e teorema cinese#Attenzione alla buona definizione|sulla buona definizione]].

## Vedi anche

- [[Insieme quoziente]]
- [[Classe di equivalenza]]
- [[Omomorfismo]]
- [[Congruenza modulo n]]
