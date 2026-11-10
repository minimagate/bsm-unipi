---
title: Teorema di Rouché-Capelli
type: voce
categoria: teorema
corsi:
- Geometria 1
introdotta_in: 2026-10-27 - Rango, sistemi lineari e matrici elementari
alias:
- Rouché-Capelli
sintesi: Un sistema lineare ha soluzione se e solo se la matrice dei coefficienti e la matrice completa hanno lo stesso rango.
---

Il **teorema di Rouché-Capelli** dà un criterio di compatibilità per i sistemi lineari: il sistema $Ax=b$ è risolubile se e solo se aggiungere la colonna $b$ non aumenta il rango.

## Enunciato

Sia $A\in M_{m,n}(\mathbb K)$, $b\in\mathbb K^m$ e $\widetilde A=(A\mid b)$ la matrice completa. Allora

$$
Ax=b\text{ è risolubile}\iff\operatorname{rank}(A)=\operatorname{rank}(\widetilde A).
$$

Se il sistema è risolubile e il rango comune è $r$, le soluzioni dipendono da $n-r$ parametri liberi (un'unica soluzione se $r=n$).

## Intuizione

$Ax=b$ è risolubile quando $b$ sta nello span delle colonne di $A$. Se $b$ è già nello span, aggiungerlo come colonna non cambia lo span e quindi nemmeno il rango; se invece non c'è, il rango sale di uno. Con Gauss il caso "rango che sale" è una riga del tipo $0=c$ con $c\neq 0$.

## Esempi

Per $A=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ e $b=(1,2)^T$ si ha $\operatorname{rank}(A)=1$ e $\operatorname{rank}(\widetilde A)=2$: nessuna soluzione. Con $b=(1,1)^T$ i ranghi sono entrambi $1$ e il sistema è risolubile, con $2-1=1$ parametro libero.

## Come si dimostra

$Ax=b$ è risolubile se e solo se $b\in\operatorname{span}(a_1,\dots,a_n)$; questo equivale a $\operatorname{span}(a_1,\dots,a_n,b)=\operatorname{span}(a_1,\dots,a_n)$, quindi alla stessa dimensione. I dettagli sono [[2026-10-27 - Rango, sistemi lineari e matrici elementari#Dimostrazione tramite lo spazio generato dalle colonne|nella lezione del 27 ottobre]].

## Vedi anche

- [[Sistema lineare]]
- [[Rango]]
- [[Algoritmo di eliminazione di Gauss]]
- [[Sottospazio generato]]
