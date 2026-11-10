---
title: Anello
type: voce
categoria: oggetto
corsi:
- Aritmetica
introdotta_in: 2026-10-21 - Relazioni di equivalenza e strutture quoziente
alias:
- anelli
sintesi: Un insieme con somma e prodotto in cui la somma forma un gruppo abeliano e il prodotto è associativo e distributivo.
---

Un **anello** è un insieme in cui si può sommare, sottrarre e moltiplicare, come in $\mathbb Z$. Non è detto, però, che si possa dividere.

## Definizione

Un anello è un insieme con due operazioni, $+$ e $\cdot$, tali che:

- rispetto alla somma è un [[Gruppo|gruppo]] abeliano;
- il prodotto è associativo;
- il prodotto è distributivo: $a(b+c)=ab+ac$ e $(a+b)c=ac+bc$.

Nel corso si considerano anelli **commutativi con identità**: $ab=ba$ e c'è un elemento $1$ con $1a=a1=a$. Un [[Campo|campo]] è un anello commutativo con identità in cui ogni elemento non nullo ha un inverso moltiplicativo.

## Intuizione

L'anello è il posto naturale dove fare "aritmetica": somme e prodotti che si comportano come ci aspettiamo, ma con la possibilità che certi elementi non siano invertibili. Quando un elemento non è invertibile la divisione non è sempre lecita.

## Esempi

- $\mathbb Z$ è un anello commutativo con identità.
- $\mathbb Z/n\mathbb Z$ è un anello commutativo con identità; è un campo se e solo se $n$ è primo.
- In $\mathbb Z/12\mathbb Z$ si ha $[2]_{12}[6]_{12}=[0]_{12}$ con entrambi i fattori non nulli: un anello può avere divisori dello zero.

## Vedi anche

- [[Gruppo]]
- [[Campo]]
- [[Elementi invertibili modulo n]]
- [[Omomorfismo]]
