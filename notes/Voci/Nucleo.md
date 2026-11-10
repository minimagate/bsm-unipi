---
title: Nucleo
type: voce
categoria: definizione
corsi:
- Aritmetica
- Geometria 1
introdotta_in: 2026-10-23 - Sistemi lineari, nucleo, immagine e rango
alias:
- ker
- nucleo di un omomorfismo
- nucleo di un'applicazione lineare
sintesi: Insieme dei vettori che un'applicazione lineare manda nel vettore nullo.
---

Il **nucleo** di un'applicazione lineare è l'insieme dei vettori che vengono mandati nel vettore nullo. Misura quanto l'applicazione "schiaccia" lo spazio di partenza. Nel corso di Aritmetica la stessa idea si applica agli omomorfismi di gruppi e di anelli.

## Definizione

Se $F:V\to V'$ è lineare,

$$
\ker(F)=\{v\in V\mid F(v)=0\}.
$$

Per l'applicazione $F_A(x)=Ax$ associata a una matrice, $\ker(F_A)=\{x\in\mathbb K^n\mid Ax=0\}$ è l'insieme delle soluzioni del sistema omogeneo $Ax=0$.

## Intuizione

Il nucleo è sempre un sottospazio vettoriale di $V$. Dice quanta informazione l'applicazione perde: $F$ è iniettiva se e solo se $\ker(F)=\{0\}$. La sua dimensione si ricava dal teorema rango-nullità: $\dim\ker(F)=\dim V-\dim\operatorname{Im}(F)$.

## Esempi

Per $A=\begin{pmatrix}1&2\\2&4\end{pmatrix}$ il sistema $Ax=0$ si riduce a $x_1+2x_2=0$, quindi $\ker(F_A)=\operatorname{span}\{(-2,1)\}$.

Per $F(X)=AX-XA$ sulle matrici $2\times2$, il nucleo è formato dalle matrici che commutano con $A$.

## Come si dimostra

Che $\ker(F)$ sia un sottospazio segue da: $F(u+v)=F(u)+F(v)=0$, $F(\alpha u)=\alpha F(u)=0$ e $F(0)=0$. La verifica, e l'equivalenza tra iniettività e nucleo banale, sono [[2026-10-23 - Sistemi lineari, nucleo, immagine e rango#Immagine e nucleo di un’applicazione lineare|nella lezione del 23 ottobre]].

## Vedi anche

- [[Applicazione lineare]]
- [[Teorema rango-nullità]]
- [[Sistema lineare]]
- [[Sottospazio vettoriale]]
