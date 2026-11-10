---
title: Induzione forte
type: voce
categoria: metodo
corsi:
- Aritmetica
introdotta_in: 2026-09-23 - Numeri naturali, induzione e fattorizzazione
alias:
- principio di induzione forte
sintesi: Variante dell'induzione in cui, per dimostrare la proprietà all'n-esimo passo, si possono usare tutti i passi precedenti.
---

L'**induzione forte** (o completa) è una forma del [[Principio di induzione]] in cui l'ipotesi induttiva non si limita a $P(n-1)$ ma comprende tutte le proprietà precedenti.

## Enunciato

Sia $P(n)$ definita per $n\ge n_0$. Se:

1. $P(n_0)$ è vera;
2. per ogni $n>n_0$, dall'ipotesi che $P(n_0),P(n_0+1),\ldots,P(n-1)$ siano tutte vere segue $P(n)$;

allora $P(n)$ è vera per ogni $n\ge n_0$.

## Intuizione

Nell'induzione debole ogni tessera fa cadere la successiva; in quella forte, per far cadere la tessera $n$ puoi contare sul fatto che *tutte* le precedenti siano già cadute. È la scelta naturale quando $P(n)$ dipende da numeri molto più piccoli di $n$ e non dal solo predecessore.

## Esempi

- Ogni $n\ge 2$ è prodotto di numeri primi: se $n$ è composto, $n=ab$ con $2\le a,b\le n-1$, e si usano le fattorizzazioni di $a$ e $b$ (non quella di $n-1$).
- Per $32\,000=32\cdot 1000$ si fattorizzano separatamente $32$ e $1000$.

## Come si dimostra

Debole e forte sono equivalenti: dalla forte alla debole è immediato; dalla debole alla forte si applica l'induzione debole alla proprietà cumulativa $Q(n)$: "$P(k)$ vale per ogni $k\le n$". Vedi [[2026-09-23 - Numeri naturali, induzione e fattorizzazione#8. Induzione forte|la lezione]].

## Vedi anche

- [[Principio di induzione]]
- [[Principio del minimo]]
- [[Teorema fondamentale dell'aritmetica]]
- [[Numero primo]]
