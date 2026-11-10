---
title: Principio di induzione
type: voce
categoria: metodo
corsi:
- Analisi 1
- Aritmetica
- Geometria 1
introdotta_in: 2026-09-23 - Numeri naturali, induzione e fattorizzazione
alias:
- induzione
- induzione matematica
- induzione debole
sintesi: Per dimostrare che una proprietà vale per tutti i naturali basta verificarla al primo passo e mostrare che passa da ogni numero al successivo.
---

Il **principio di induzione** (o induzione matematica) è il metodo standard per dimostrare che una proprietà $P(n)$ è vera per ogni numero naturale $n\ge n_0$.

## Enunciato

Sia $P(n)$ una proprietà definita per $n\ge n_0$. Se:

1. **passo base**: $P(n_0)$ è vera;
2. **passo induttivo**: per ogni $n\ge n_0$, vale $P(n)\Rightarrow P(n+1)$;

allora $P(n)$ è vera per ogni $n\ge n_0$. L'assunzione $P(n)$ si chiama *ipotesi induttiva*. Nella forma "forte" si può assumere vere tutte le $P(k)$ con $k<n$ (vedi [[Induzione forte]]).

## Intuizione

È l'effetto domino: dimostri che la prima tessera cade (passo base) e che ogni tessera, cadendo, fa cadere la successiva (passo induttivo). Servono *entrambe* le cose: senza passo base la catena non parte, e un passo induttivo che non funziona dal primo livello può dare "dimostrazioni" assurde.

## Esempi

Per dimostrare $1+2+\cdots+n=\frac{n(n+1)}{2}$:

- base: per $n=1$ si ha $1=\frac{1\cdot 2}{2}$;
- passo: se vale per $n$, allora $1+\cdots+n+(n+1)=\frac{n(n+1)}{2}+(n+1)=\frac{(n+1)(n+2)}{2}$.

Un altro esempio: $\sum_{i=0}^{n-1}(2i+1)=n^2$.

## Come si dimostra

L'induzione discende dal [[Principio del minimo]]: se esistesse un controesempio, ce ne sarebbe uno minimo $m_0$; ma $P(m_0-1)$ è vera e il passo induttivo darebbe $P(m_0)$, contraddizione. Vedi [[2026-09-23 - Numeri naturali, induzione e fattorizzazione#5. Principio di induzione matematica|la lezione del 23 settembre]].

## Vedi anche

- [[Induzione forte]]
- [[Principio del minimo]]
- [[Numero naturale]]
- [[Teorema fondamentale dell'aritmetica]]
