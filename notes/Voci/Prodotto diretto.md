---
title: Prodotto diretto
type: voce
categoria: oggetto
corsi:
- Aritmetica
introdotta_in: 2026-10-22 - Omomorfismi tra anelli e teorema cinese
alias:
- prodotto diretto di gruppi
- prodotto diretto di anelli
sintesi: Il prodotto cartesiano di due gruppi o anelli con le operazioni definite componente per componente.
---

Il **prodotto diretto** di due strutture algebriche è il loro [[Prodotto cartesiano|prodotto cartesiano]] con le operazioni fatte componente per componente: sulla prima coordinata si calcola come nel primo, sulla seconda come nel secondo.

## Definizione

Se $G_1$ e $G_2$ sono [[Gruppo|gruppi]], su $G_1\times G_2$ si pone

$$
(x_1,y_1)(x_2,y_2)=(x_1x_2,\,y_1y_2).
$$

L'identità è $(e_{G_1},e_{G_2})$ e l'inverso di $(x,y)$ è $(x^{-1},y^{-1})$. Per gli [[Anello|anelli]] si definiscono allo stesso modo somma e prodotto: $(a,b)+(a',b')=(a+a',b+b')$ e $(a,b)(a',b')=(aa',bb')$. Se i gruppi sono finiti, $|G_1\times G_2|=|G_1|\,|G_2|$.

## Intuizione

È il modo più semplice per costruire un oggetto grande a partire da due piccoli, senza alcuna interazione tra le due componenti. L'ordine di una coppia è il minimo comune multiplo degli ordini delle componenti: $\operatorname{ord}(x,y)=\operatorname{mcm}(\operatorname{ord}(x),\operatorname{ord}(y))$.

## Esempi

- In $\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z$ si ha $(\overline1,\overline2)+(\overline1,\overline2)=(\overline0,\overline1)$.
- $\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\cong\mathbb Z/mn\mathbb Z$ se e solo se $\gcd(m,n)=1$: è il contenuto del [[Teorema cinese del resto|teorema cinese del resto]] nella versione con omomorfismi.

## Come si dimostra

Le verifiche sono nella sezione [[2026-10-22 - Omomorfismi tra anelli e teorema cinese#Il prodotto diretto di anelli|sul prodotto diretto di anelli]] della lezione del 22 ottobre.

## Vedi anche

- [[Omomorfismo]]
- [[Isomorfismo]]
- [[Teorema cinese del resto]]
- [[Ordine di un elemento]]
