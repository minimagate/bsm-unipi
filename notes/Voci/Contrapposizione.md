---
title: Contrapposizione
type: voce
categoria: metodo
corsi:
- Analisi 1
- Fondamenti di Programmazione
introdotta_in: 2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi
alias:
- controposizione
- dimostrazione per contrapposizione
- dimostrazione per controposizione
sintesi: Un'implicazione equivale alla sua contronominale, quindi per dimostrare che P implica Q si può dimostrare che non Q implica non P.
---
La **contrapposizione** (o controposizione) è la proprietà per cui un'implicazione e la sua contronominale hanno lo stesso valore di verità. Sfruttandola si ottiene un metodo di dimostrazione.

## Enunciato

$$
(P\Rightarrow Q)\;\equiv\;(\neg Q\Rightarrow\neg P).
$$

Per dimostrare $P\Rightarrow Q$ si può quindi supporre $\neg Q$ e dedurre $\neg P$.

## Intuizione

Se "studio ogni giorno $\Rightarrow$ passo l'esame", allora "non passo l'esame $\Rightarrow$ non ho studiato ogni giorno". Attenzione a non confonderla con l'**inversa** $\neg P\Rightarrow\neg Q$, che *non* è equivalente: si può passare l'esame anche senza studiare ogni giorno.

## Esempi

- L'iniettività di una funzione si può scrivere $a_1\ne a_2\Rightarrow f(a_1)\ne f(a_2)$ oppure, per contrapposizione, $f(a_1)=f(a_2)\Rightarrow a_1=a_2$ (forma spesso più comoda).
- "Se $n^2$ è pari, allora $n$ è pari": per contrapposizione, se $n$ è dispari anche $n^2$ è dispari.

## Come si dimostra

Si verifica con le [[Tavola di verità|tavole di verità]], oppure usando $P\Rightarrow Q\equiv\neg P\lor Q$. Il punto è discusso nella sezione [[2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi#5.4 Contraposizione|Contraposizione]] della lezione del 23 settembre.

## Vedi anche

- [[Implicazione]]
- [[Dimostrazione per assurdo]]
- [[Leggi di De Morgan]]
- [[Tavola di verità]]
