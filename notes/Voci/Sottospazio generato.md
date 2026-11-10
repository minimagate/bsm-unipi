---
title: Sottospazio generato
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-02 - Span, indipendenza lineare e basi vettoriali
alias:
- span
- generatori
- sistema di generatori
- insieme di generatori
- spazio generato
sintesi: Il sottospazio generato da alcuni vettori è l'insieme di tutte le loro combinazioni lineari.
---

Il **sottospazio generato** (o **span**) da un insieme di vettori è l'insieme di tutte le loro [[Combinazione lineare|combinazioni lineari]]. È il più piccolo [[Sottospazio vettoriale|sottospazio]] che li contiene.

## Definizione

$$
\operatorname{span}(v_1,\dots,v_n)=\{\alpha_1v_1+\cdots+\alpha_nv_n\mid \alpha_i\in\mathbb{K}\}.
$$

Per un insieme qualunque $A\subseteq V$, anche infinito, $\operatorname{span}(A)$ è l'insieme delle combinazioni lineari *finite* di elementi di $A$. Si scrive anche $\langle v_1,\dots,v_n\rangle$. Se $\operatorname{span}(A)=V$, si dice che $A$ è un insieme (o sistema) di **generatori** di $V$.

## Intuizione

Lo span di un vettore non nullo è una retta per l'origine, di due vettori non paralleli un piano, di tre non complanari lo spazio. Aggiungere un vettore che sta già nello span non amplia nulla. Formalmente $A\subseteq\operatorname{span}(A)$, $\operatorname{span}(\operatorname{span}(A))=\operatorname{span}(A)$ e

$$
\operatorname{span}(A)=\bigcap_{\substack{W\leq V\\ A\subseteq W}}W.
$$

## Esempi

- $\operatorname{span}\{(1,2,0),(0,3,1)\}=\{(x_1,x_2,x_3)\mid 2x_1-x_2+3x_3=0\}$.
- In $\mathbb{K}[x]$, i monomi $1,x,x^2,\dots$ generano tutto lo spazio.
- I monomi di grado pari generano i polinomi con sole potenze pari.

## Come si dimostra

Lo span contiene $\mathbf 0$ (coefficienti nulli), somme e multipli di combinazioni sono ancora combinazioni: vedi [[2026-10-02 - Span, indipendenza lineare e basi vettoriali#3. Lo span è un sottospazio vettoriale|lo span è un sottospazio vettoriale]].

## Vedi anche

- [[Combinazione lineare]]
- [[Indipendenza lineare]]
- [[Base di uno spazio vettoriale]]
- [[Somma di sottospazi]]
