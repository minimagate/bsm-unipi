---
title: Completamento a una base
type: voce
categoria: metodo
corsi:
- Geometria 1
introdotta_in: 2026-11-01 - Indipendenza lineare e basi mediante Gauss
alias:
- estrazione di una base
- completamento di una base
sintesi: Procedura per estrarre una base da un insieme di generatori oppure per aggiungere vettori a un insieme indipendente fino a ottenere una base.
---

Il **completamento a una base** è il procedimento che, a partire da vettori linearmente indipendenti, ne aggiunge altri fino a ottenere una base dello spazio. Il procedimento duale, l'**estrazione**, ricava una base da un insieme di generatori.

## Definizione

*Estrazione.* Se $v_1,\dots,v_k$ generano $W\subseteq\mathbb K^n$, si mettono come colonne di una matrice, si riduce con Gauss e si prendono i vettori della matrice **iniziale** corrispondenti alle colonne pivotali: sono una base di $W$.

*Completamento.* Se $v_1,\dots,v_k\in\mathbb K^n$ sono linearmente indipendenti, si considera la matrice con colonne $v_1,\dots,v_k,e_1,\dots,e_n$ (con $e_i$ la base canonica) e si estrae una base: contiene tutti i $v_i$ più alcuni $e_i$.

## Intuizione

I vettori iniziali e quelli canonici insieme generano certamente $\mathbb K^n$; l'algoritmo elimina quelli ridondanti. I primi $k$ sono già indipendenti, quindi sono pivotali e restano. Occhio: si usano le colonne della matrice di partenza, non quelle ridotte, perché le operazioni di riga cambiano lo span delle colonne.

## Esempi

Estrazione: $v_1=(1,0)$, $v_2=(2,0)$, $v_3=(0,1)$ hanno pivot nelle colonne $1$ e $3$, quindi $\{v_1,v_3\}$ è una base dello span.

Completamento: in $\mathbb R^3$ per completare $v=(1,1,0)$ si riduce la matrice con colonne $v,e_1,e_2,e_3$; i pivot sono nelle colonne $1,2,4$, quindi $\{v,e_1,e_3\}$ è una base.

## Come si dimostra

La giustificazione è nel ragionamento sul sistema omogeneo $Ax=0$, che non cambia con le operazioni di riga: si veda [[2026-11-01 - Indipendenza lineare e basi mediante Gauss#7. Completamento di una famiglia linearmente indipendente a una base|la lezione del 1 novembre]].

## Vedi anche

- [[Base di uno spazio vettoriale]]
- [[Indipendenza lineare]]
- [[Algoritmo di eliminazione di Gauss]]
- [[Lemma di scambio]]
