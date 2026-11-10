---
title: Successione per ricorrenza
type: voce
categoria: metodo
corsi:
- Aritmetica
introdotta_in: 2026-09-30 - Successioni ricorrenti e formule combinatorie
alias:
- successione ricorrente
- equazione di ricorrenza
- ricorrenza
sintesi: Successione i cui termini si ottengono da quelli precedenti tramite una relazione, a partire da alcuni valori iniziali.
---

Una **successione per ricorrenza** è una successione $a:\mathbb{N}\to X$ i cui termini sono determinati da alcuni valori iniziali e da una relazione che lega ogni termine ai precedenti.

## Definizione

Esempio: $a_{n+1}=3a_n-2a_{n-1}$ con $a_0=0$, $a_1=1$. La ricorrenza è *lineare omogenea*: combinazioni lineari di soluzioni sono ancora soluzioni, quindi le soluzioni formano uno spazio vettoriale (di dimensione pari all'ordine, qui $2$).

*Metodo*: si cerca $a_n=\lambda^n$; sostituendo si ottiene l'equazione caratteristica $\lambda^2=3\lambda-2$, con radici $\lambda=1,2$. Se le radici sono distinte, $a_n=x\lambda_1^n+y\lambda_2^n$, e le costanti $x,y$ si fissano con le condizioni iniziali.

## Intuizione

Una ricorrenza è una famiglia infinita di equazioni; il trucco è trasformarla in *una sola* equazione algebrica, il polinomio caratteristico, che sappiamo risolvere. I valori iniziali scelgono poi quale soluzione ottenere.

## Esempi

Da $a_n=x2^n+y$ e $a_0=0,\ a_1=1$ si ricava $x=1,\ y=-1$, cioè

$$a_n=2^n-1.$$

Anche la [[Successione di Fibonacci]] si risolve così, con $\lambda^2-\lambda-1=0$.

## Come si dimostra

Vedi [[2026-09-30 - Successioni ricorrenti e formule combinatorie#3. Metodo della soluzione esponenziale|la lezione del 30 settembre]].

## Vedi anche

- [[Successione di Fibonacci]]
- [[Spazio vettoriale]]
- [[Principio di induzione]]
