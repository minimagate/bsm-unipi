---
title: Combinazione lineare
type: voce
categoria: definizione
corsi:
- Geometria 1
introdotta_in: 2026-10-02 - Span, indipendenza lineare e basi vettoriali
alias:
- combinazioni lineari
sintesi: Una combinazione lineare di alcuni vettori è una somma di multipli di quei vettori.
---

Una **combinazione lineare** dei vettori $v_1,\dots,v_n$ di uno [[Spazio vettoriale|spazio vettoriale]] è un vettore della forma data dalla somma dei $v_i$ moltiplicati per scalari.

## Definizione

Siano $v_1,\dots,v_n\in V$ e $\alpha_1,\dots,\alpha_n\in K$. Il vettore

$$
\alpha_1v_1+\alpha_2v_2+\cdots+\alpha_nv_n
$$

è una combinazione lineare di $v_1,\dots,v_n$. I vettori sono fissati, variano i coefficienti. Le combinazioni sono sempre **finite**, anche quando si parte da un insieme infinito.

## Intuizione

È il modo di "costruire" nuovi vettori da vettori dati. Nel piano, due vettori non paralleli permettono di raggiungere ogni punto; due vettori paralleli restano su una retta. Nello spazio, tre vettori non complanari raggiungono tutto, tre complanari restano nel loro piano. L'insieme di tutte le combinazioni è il [[Sottospazio generato]].

## Esempi

- In $\mathbb{R}^2$: $(3,5)=3(1,0)+5(0,1)$.
- In $\mathbb{R}[x]$: $2+3x-x^2=2\cdot1+3\cdot x+(-1)\cdot x^2$.
- Il vettore nullo è sempre combinazione lineare, con tutti i coefficienti nulli (la combinazione banale).

## Come si dimostra

Per mostrare che un vettore è combinazione di altri si risolve un sistema nei coefficienti. La chiusura del sottospazio generato rispetto alle combinazioni è mostrata in [[2026-10-02 - Span, indipendenza lineare e basi vettoriali#3. Lo span è un sottospazio vettoriale|lo span è un sottospazio]].

## Vedi anche

- [[Sottospazio generato]]
- [[Indipendenza lineare]]
- [[Sottospazio vettoriale]]
