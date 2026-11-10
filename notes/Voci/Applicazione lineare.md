---
title: Applicazione lineare
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-23 - Sistemi lineari, nucleo, immagine e rango
alias:
- applicazioni lineari
- trasformazione lineare
- mappa lineare
sintesi: Funzione tra spazi vettoriali che rispetta la somma di vettori e il prodotto per uno scalare.
---

Un'**applicazione lineare** è una funzione tra due spazi vettoriali che rispetta le loro operazioni: somma di vettori e prodotto per uno scalare. Sono le "mappe giuste" tra spazi vettoriali.

## Definizione

Siano $V$ e $V'$ spazi vettoriali sullo stesso campo $\mathbb K$. Una funzione $F:V\to V'$ è lineare se

1. $F(v+v')=F(v)+F(v')$ per ogni $v,v'\in V$;
2. $F(\alpha v)=\alpha F(v)$ per ogni $\alpha\in\mathbb K$ e $v\in V$.

Equivalentemente $F(\alpha_1v_1+\cdots+\alpha_rv_r)=\alpha_1F(v_1)+\cdots+\alpha_rF(v_r)$. In particolare $F(0)=0$.

## Intuizione

Una mappa lineare conserva le combinazioni lineari, quindi è determinata dai valori sui vettori di una base: assegnati arbitrariamente i valori sulla base, esiste una e una sola applicazione lineare che li ha. Per questo ogni applicazione lineare tra spazi di dimensione finita si descrive con una matrice.

## Esempi

Per ogni matrice $A\in M_{m,n}(\mathbb K)$ la funzione $F_A:\mathbb K^n\to\mathbb K^m$, $F_A(x)=Ax$, è lineare, per la distributività del prodotto tra matrici.

La funzione $F(x,y)=(x+y,2y)$ da $\mathbb R^2$ in $\mathbb R^2$ è lineare, mentre $G(x)=x+1$ da $\mathbb R$ in $\mathbb R$ non lo è perché $G(0)\neq 0$.

## Come si dimostra

Per mostrare che $F_A$ è lineare basta usare le proprietà del prodotto: $A(x+y)=Ax+Ay$ e $A(\alpha x)=\alpha(Ax)$. Si veda [[2026-10-23 - Sistemi lineari, nucleo, immagine e rango#Interpretazione come applicazione lineare|la lezione del 23 ottobre]].

## Vedi anche

- [[Nucleo]]
- [[Matrice associata a un'applicazione lineare]]
- [[Teorema rango-nullità]]
- [[Isomorfismo]]
