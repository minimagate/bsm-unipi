---
title: Gruppo delle permutazioni
type: voce
categoria: oggetto
corsi:
- Aritmetica
introdotta_in: 2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni
alias:
- permutazione
- permutazioni
- gruppo simmetrico
- notazione ciclica
sintesi: L'insieme delle funzioni biettive di un insieme in sé, con l'operazione di composizione.
---

Il **gruppo delle permutazioni** di un insieme $X$ è formato da tutti i modi di "rimescolare" gli elementi di $X$, cioè dalle funzioni biettive $X\to X$, con la composizione come operazione.

## Definizione

Una **permutazione** di $X$ è una funzione biettiva $\sigma\colon X\to X$. L'insieme $\operatorname{Sym}(X)$ delle permutazioni è un [[Gruppo|gruppo]] rispetto alla composizione, con $(\sigma\tau)(x)=\sigma(\tau(x))$ (si applica prima la permutazione a destra). Il neutro è l'identità e l'inverso è la funzione inversa. Per $X=\{1,\dots,n\}$ si scrive $S_n$, e $|S_n|=n!$.

Nella **notazione ciclica** $(a_1\ a_2\ \dots\ a_k)$ manda $a_1\mapsto a_2\mapsto\dots\mapsto a_k\mapsto a_1$ e lascia fissi gli altri elementi. Ogni permutazione è prodotto di cicli disgiunti, che commutano; il suo ordine è il minimo comune multiplo delle lunghezze dei cicli.

## Intuizione

Pensa a un mazzo di carte: ogni modo di rimescolarlo è una permutazione, e rimescolare due volte è comporre. Per $n\geq3$ l'ordine in cui si fanno i rimescolamenti conta.

## Esempi

- $S_3$ ha $6$ elementi: $\operatorname{id}$, $(1\ 2)$, $(1\ 3)$, $(2\ 3)$, $(1\ 2\ 3)$, $(1\ 3\ 2)$.
- Con $\sigma=(1\ 2\ 3)$ e $\tau=(1\ 2)$ si ha $\sigma\tau=(1\ 3)$ ma $\tau\sigma=(2\ 3)$: $S_3$ non è abeliano.

## Come si dimostra

Per $|X|\geq3$ basta esibire due permutazioni che non commutano, come nella sezione [[2026-10-28 - Gruppi ciclici, sottogruppi e permutazioni#6. Gruppo delle permutazioni|sul gruppo delle permutazioni]] della lezione del 28 ottobre.

## Vedi anche

- [[Gruppo]]
- [[Funzione biettiva]]
- [[Composizione di funzioni]]
- [[Ordine di un elemento]]
