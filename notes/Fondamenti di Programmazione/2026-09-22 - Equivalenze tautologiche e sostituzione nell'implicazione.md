---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-09-22'
title: Equivalenze tautologiche e sostituzione nell'implicazione
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-09-22 - Equivalenze tautologiche e sostituzione nell'implicazione.md
vault_hash: 0cf7c192aa1bfd0dc230031a30466d3718ea560065620f951d002196b66eb4bd
---

La lezione sviluppa tecniche pratiche per dimostrare equivalenze e implicazioni nel [[Calcolo proposizionale|calcolo proposizionale]]. Il punto centrale è distinguere con attenzione:

- il significato semantico di una formula, verificabile con le [[Tavola di verità|tavole di verità]];
- la manipolazione sintattica delle formule tramite leggi già dimostrate;
- le condizioni sotto cui una sottoformula si può sostituire senza invalidare una dimostrazione.

## 1. Dimostrare leggi con le tavole di verità

Una legge proposizionale è un'[[Equivalenza logica|equivalenza]] valida per ogni [[Interpretazione|interpretazione]]. Per verificarla si usano simboli proposizionali $p,q,r,\ldots$: controllare la formula generale equivale a controllarne tutte le istanze.

Per esempio, la legge di unità

$$
(p \equiv \mathrm{T}) \equiv p
$$

è una [[Tautologia|tautologia]], perché le due espressioni $p \equiv \mathrm{T}$ e $p$ hanno lo stesso valore di verità per entrambi i possibili valori di $p$.

### 1.1 Leggi per congiunzione e disgiunzione

Per ogni formula $P,Q,R$ valgono le seguenti equivalenze.

**Commutatività**

$$
P\lor Q\equiv Q\lor P,
\qquad
P\land Q\equiv Q\land P.
$$

**Associatività**

$$
P\lor(Q\lor R)\equiv(P\lor Q)\lor R,
$$

$$
P\land(Q\land R)\equiv(P\land Q)\land R.
$$

**Idempotenza**

$$
P\lor P\equiv P,
\qquad
P\land P\equiv P.
$$

**Unità**

$$
P\land\mathrm{T}\equiv P,
\qquad
P\lor\mathrm{F}\equiv P.
$$

**Zero**

$$
P\land\mathrm{F}\equiv\mathrm{F},
\qquad
P\lor\mathrm{T}\equiv\mathrm{T}.
$$

**Distributività**

$$
P\land(Q\lor R)\equiv(P\land Q)\lor(P\land R),
$$

$$
P\lor(Q\land R)\equiv(P\lor Q)\land(P\lor R).
$$

Le leggi si dimostrano confrontando, riga per riga, i valori dei due membri in una tavola di verità.

### 1.2 Leggi della negazione

$$
\neg\neg P\equiv P
\qquad\text{(doppia negazione)}
$$

$$
P\lor\neg P\equiv\mathrm{T}
\qquad\text{(terzo escluso)}
$$

$$
P\land\neg P\equiv\mathrm{F}
\qquad\text{(contraddizione)}
$$

Le [[Leggi di De Morgan|leggi di De Morgan]] sono:

$$
\neg(P\land Q)\equiv\neg P\lor\neg Q,
$$

$$
\neg(P\lor Q)\equiv\neg P\land\neg Q.
$$

Inoltre:

$$
\neg\mathrm{T}\equiv\mathrm{F},
\qquad
\neg\mathrm{F}\equiv\mathrm{T}.
$$

### 1.3 Eliminazione di implicazione ed equivalenza

L'[[Implicazione|implicazione]] si può riscrivere senza usare $\Rightarrow$:

$$
P\Rightarrow Q\equiv\neg P\lor Q,
$$

oppure, applicando De Morgan,

$$
P\Rightarrow Q\equiv\neg(P\land\neg Q).
$$

Da qui segue anche:

$$
\neg(P\Rightarrow Q)\equiv P\land\neg Q.
$$

L'equivalenza si può eliminare in due modi:

$$
P\equiv Q\equiv(P\Rightarrow Q)\land(Q\Rightarrow P),
$$

$$
P\equiv Q\equiv(P\land Q)\lor(\neg P\land\neg Q).
$$

Queste leggi mostrano anche che tutte le formule si possono ricondurre a un insieme più piccolo di connettivi. Per leggibilità, e per rappresentare direttamente le tecniche di dimostrazione, conviene però tenere $\Rightarrow$ ed $\equiv$.

## 2. Dimostrazioni per equivalenze successive

Per dimostrare $P_1\equiv P_n$ si costruisce una catena:

$$
\begin{aligned}
P_1
&\equiv \{\text{giustificazione}\}\\
P_2
&\equiv \{\text{giustificazione}\}\\
&\ \vdots\\
P_n.
\end{aligned}
$$

Ogni passaggio sostituisce in una formula $R$ un'occorrenza di $P$ con $Q$, usando una legge $P\equiv Q$:

$$
R\equiv R[Q/P].
$$

La correttezza del passaggio è garantita dal [[Principio di sostituzione|principio di sostituzione]] per l'equivalenza. La tecnica però non decide al posto nostro quale legge applicare, da quale membro partire o come organizzare i passaggi: questo resta a carico di chi costruisce la dimostrazione.

### 2.1 Esempio

Si vuole dimostrare:

$$
P\lor(Q\lor R)\equiv(P\lor Q)\lor(P\lor R).
$$

Partendo dal secondo membro:

$$
\begin{aligned}
(P\lor Q)\lor(P\lor R)
&\equiv (Q\lor P)\lor(P\lor R) && \text{commutatività}\\
&\equiv Q\lor(P\lor(P\lor R)) && \text{associatività}\\
&\equiv Q\lor((P\lor P)\lor R) && \text{associatività}\\
&\equiv Q\lor(P\lor R) && \text{idempotenza}\\
&\equiv (Q\lor P)\lor R && \text{associatività}\\
&\equiv (P\lor Q)\lor R && \text{commutatività}\\
&\equiv P\lor(Q\lor R) && \text{associatività}.
\end{aligned}
$$

Nelle dimostrazioni successive si possono omettere alcuni passaggi ovvi di associatività, commutatività e idempotenza, purché la trasformazione resti chiara.

### 2.2 Complemento e assorbimento

Le **leggi di complemento** sono:

$$
P\lor(\neg P\land Q)\equiv P\lor Q,
$$

$$
P\land(\neg P\lor Q)\equiv P\land Q.
$$

La prima si dimostra così:

$$
\begin{aligned}
P\lor(\neg P\land Q)
&\equiv(P\lor\neg P)\land(P\lor Q) && \text{distributività}\\
&\equiv\mathrm{T}\land(P\lor Q) && \text{terzo escluso}\\
&\equiv P\lor Q && \text{unità}.
\end{aligned}
$$

Le **leggi di assorbimento** sono:

$$
P\land(P\lor Q)\equiv P,
\qquad
P\lor(P\land Q)\equiv P.
$$

Per esempio:

$$
\begin{aligned}
P\land(P\lor Q)
&\equiv(P\lor\mathrm{F})\land(P\lor Q) && \text{unità}\\
&\equiv P\lor(\mathrm{F}\land Q) && \text{distributività}\\
&\equiv P\lor\mathrm{F} && \text{zero}\\
&\equiv P && \text{unità}.
\end{aligned}
$$

> [!warning]
> Nelle trasformazioni si manipolano **simboli**, non valori semantici. Nella legge di unità deve comparire la costante proposizionale $\mathrm{F}$, non un simbolo proposizionale qualsiasi come $f$.

## 3. Tautologie, conseguenze logiche e controesempi

Un'inferenza è corretta se la formula che raccoglie premesse e conclusione è una tautologia. Date le premesse $c\Rightarrow a$ e $a\Rightarrow b$, la conclusione certa è $c\Rightarrow b$:

$$
((c\Rightarrow a)\land(a\Rightarrow b))\Rightarrow(c\Rightarrow b).
$$

Questa formula esprime la **transitività dell'implicazione** e si può ridurre a $\mathrm{T}$ con le leggi viste sopra.

Per mostrare che una formula **non** è una tautologia non serve costruire l'intera tavola di verità: basta trovare una sola interpretazione che la renda falsa.

Per esempio,

$$
((c\Rightarrow a)\land(a\Rightarrow b))\Rightarrow(b\Rightarrow c)
$$

è falsa se $b\mapsto\mathrm{t}$ e $c\mapsto\mathrm{f}$: con questi valori la conclusione $b\Rightarrow c$ è falsa, mentre la premessa è vera per entrambi i valori di $a$.

Analogamente,

$$
((a\Rightarrow b)\land\neg a)\Rightarrow b
$$

non è una tautologia: l'interpretazione $a\mapsto\mathrm{f}$, $b\mapsto\mathrm{f}$ rende vera la premessa e falsa la conclusione.

Il tentativo fallisce invece per

$$
((a\Rightarrow b)\land a)\Rightarrow b,
$$

perché con $a\mapsto\mathrm{t}$ e $b\mapsto\mathrm{f}$ la sottoformula $a\Rightarrow b$ è falsa, quindi l'intera premessa è falsa. La formula è infatti una tautologia: è il **modus ponens**.

### 3.1 Traduzione di inferenze in linguaggio naturale

L'inferenza «Se piove non esco; ieri sono uscito; dunque non pioveva» si formalizza come:

$$
((P\Rightarrow\neg E)\land E)\Rightarrow\neg P.
$$

È corretta perché la formula è una tautologia.

Al contrario, «Se piove non esco; ieri non pioveva; dunque sono uscito» diventa:

$$
((P\Rightarrow\neg E)\land\neg P)\Rightarrow E
$$

e non è una tautologia. Il controesempio $P\mapsto\mathrm{f}$, $E\mapsto\mathrm{f}$ rende vere le premesse ma falsa la conclusione.

## 4. Sintassi e parentesi

Le formule proposizionali sono stringhe costruite ricorsivamente. Una grammatica possibile è:

$$
\begin{aligned}
\mathit{Prop}::={}&(\mathit{Prop}\equiv\mathit{Prop})
\mid(\mathit{Prop}\land\mathit{Prop})
\mid(\mathit{Prop}\lor\mathit{Prop})\\
&\mid(\mathit{Prop}\Rightarrow\mathit{Prop})
\mid(\mathit{Prop}\Leftarrow\mathit{Prop})
\mid(\neg\mathit{Prop})\\
&\mid\mathrm{T}\mid\mathrm{F}\mid p\mid q\mid\cdots
\end{aligned}
$$

Con questa definizione completa, ogni occorrenza di un [[Connettivo logico|connettivo]] sta tra parentesi. Stringhe come $p\land\lor$, $\mathrm{T}\equiv\neg$ e $()$ non sono formule.

Le parentesi sono indispensabili perché strutture diverse possono avere valori di verità diversi. Per esempio,

$$
(P\Rightarrow\neg P)\Rightarrow Q
$$

e

$$
P\Rightarrow(\neg P\Rightarrow Q)
$$

non coincidono: per $P\mapsto\mathrm{f}$ e $Q\mapsto\mathrm{f}$ la prima è falsa, mentre la seconda è vera.

### 4.1 Convenzioni di precedenza

Per omettere parte delle parentesi si eliminano sempre quelle più esterne e si usano questi livelli di precedenza, dal più debole al più forte:

| Connettivo | Precedenza |
|---|---:|
| $\equiv$ | 0 |
| $\Rightarrow$ | 1 |
| $\land,\lor$ | 2 |
| $\neg$ | 3 |

Non viene stabilita alcuna precedenza tra $\land$ e $\lor$.

Di conseguenza:

- $P\land Q\Rightarrow R\equiv R\lor P\Rightarrow S$ si legge come $((P\land Q)\Rightarrow R)\equiv((R\lor P)\Rightarrow S)$;
- $P\land Q\land R$ è sintatticamente ambiguo, ma si accetta grazie all'associatività di $\land$;
- $P\land Q\lor R$ è sintatticamente errato, perché non c'è precedenza tra $\land$ e $\lor$;
- $P\Rightarrow Q\Rightarrow R$ è sintatticamente errato se non si specifica l'associazione;
- $P\Rightarrow Q\equiv\neg P\lor Q$ si legge $(P\Rightarrow Q)\equiv(\neg P\lor Q)$.

> [!important]
> Quando si applica $P\Rightarrow Q\equiv\neg P\lor Q$, bisogna rispettare la struttura della sottoformula. Per esempio:
> $$
> P\Rightarrow(Q\land R)\equiv\neg P\lor(Q\land R),
> $$
> non $(\neg P\lor Q)\land R$.

## 5. Tecniche per dimostrare equivalenze

Per dimostrare $P\equiv Q$ ci sono tre strategie:

1. trasformare direttamente $P$ in $Q$;
2. ridurre separatamente $P$ e $Q$ a una stessa formula $R$;
3. se si vuole dimostrare che $P$ è una tautologia e il suo connettivo principale non è $\equiv$, mostrare $P\equiv\mathrm{T}$.

Tutte e tre si basano sul principio di sostituzione per l'equivalenza.

## 6. Dalle equivalenze alle implicazioni

Nella verifica dei programmi compaiono spesso implicazioni tautologiche. Un esempio schematico è:

> Se nello [[Stato|stato]] iniziale $x\mapsto A$ e $y\mapsto B$, allora il programma produce uno stato finale in cui $\mathit{prodotto}\mapsto A\times B$.

Un'implicazione $P\Rightarrow Q$ si può sempre dimostrare mostrando

$$
(P\Rightarrow Q)\equiv\mathrm{T}.
$$

Conviene però avere anche leggi il cui connettivo principale sia direttamente $\Rightarrow$, per costruire catene miste di equivalenze e implicazioni.

Alcune leggi fondamentali sono:

$$
(P\Rightarrow Q)\land P\Rightarrow Q
\qquad\text{(modus ponens)}
$$

$$
(P\Rightarrow Q)\land(Q\Rightarrow R)\Rightarrow(P\Rightarrow R)
\qquad\text{(transitività)}
$$

$$
P\land Q\Rightarrow P
\qquad\text{(semplificazione di $\land$)}
$$

$$
P\Rightarrow P\lor Q
\qquad\text{(introduzione di $\lor$)}.
$$

## 7. Perché la sostituzione per l'implicazione richiede cautela

Dal fatto che $P\Rightarrow Q$ non segue in generale che

$$
R\Rightarrow R[Q/P].
$$

Per esempio, la legge $P\land Q\Rightarrow P$ non autorizza la trasformazione

$$
\mathit{studia}\land\mathit{frequenta\_lezioni}\Rightarrow\mathit{supera\_esame}
$$

in

$$
\mathit{studia}\Rightarrow\mathit{supera\_esame}.
$$

La prima affermazione non implica che studiare, da solo, basti a superare l'esame.

L'analogia è con le disuguaglianze: sostituire un termine in posizione negativa può invertire il verso della relazione. Nel calcolo proposizionale la negazione $\neg$ fa da segno meno.

### 7.1 Occorrenze positive e negative

Una formula $P$ occorre **positivamente** in:

$$
P,
\qquad
P\lor Q,
\qquad
P\land Q,
\qquad
Q\Rightarrow P.
$$

Occorre invece **negativamente** in:

$$
\neg P,
\qquad
P\Rightarrow Q.
$$

Quando l'occorrenza è annidata, si contano i passaggi negativi dalla sottoformula alla radice dell'intera formula:

- se sono in numero pari, l'occorrenza è positiva;
- se sono in numero dispari, l'occorrenza è negativa.

Le posizioni che introducono un passaggio negativo sono l'argomento della negazione e l'antecedente di un'implicazione. Se una stessa formula compare più volte, ogni occorrenza va classificata separatamente.

Esempi:

- in $P\Rightarrow(\neg R\Rightarrow Q)$, $P$ occorre negativamente, mentre $R$ e $Q$ positivamente;
- in $(P\Rightarrow\neg R)\Rightarrow Q$, $P$, $R$ e $Q$ occorrono tutti positivamente.

Le equivalenze confermano questa classificazione:

$$
P\Rightarrow(\neg R\Rightarrow Q)
\equiv\neg P\lor(R\lor Q),
$$

$$
(P\Rightarrow\neg R)\Rightarrow Q
\equiv(P\land R)\lor Q.
$$

### 7.2 Principio di sostituzione per l'implicazione

Se è stata stabilita $P\Rightarrow Q$, allora:

- se l'occorrenza sostituita di $P$ è **positiva** in $R$,
  $$
  R\Rightarrow R[Q/P];
  $$
- se l'occorrenza sostituita di $P$ è **negativa** in $R$,
  $$
  R\Leftarrow R[Q/P].
  $$

Il verso dell'implicazione si inverte quindi quando la sostituzione avviene in posizione negativa.

### 7.3 Esempi di dimostrazione

Per dimostrare

$$
(P\Rightarrow Q\land R)\Rightarrow(P\Rightarrow Q),
$$

si usa $Q\land R\Rightarrow Q$. L'occorrenza di $Q\land R$ nel conseguente di $P\Rightarrow(Q\land R)$ è positiva, quindi:

$$
P\Rightarrow Q\land R
\Rightarrow
P\Rightarrow Q.
$$

Per dimostrare

$$
(P\lor Q\Rightarrow R)\Rightarrow(P\Rightarrow R),
$$

conviene partire dalla conseguenza. Dalla legge $P\Rightarrow P\lor Q$, poiché $P$ occorre negativamente nell'antecedente di $P\Rightarrow R$, segue:

$$
P\Rightarrow R
\Leftarrow
P\lor Q\Rightarrow R.
$$

## 8. Schema generale di una dimostrazione di implicazione

Una dimostrazione di $P_1\Rightarrow P_k$ può alternare equivalenze e un passaggio implicativo giustificato:

$$
\begin{aligned}
P_1
&\equiv\cdots\equiv P\\
&\Rightarrow Q && \{P\Rightarrow Q\}\\
&\equiv\cdots\equiv P_k.
\end{aligned}
$$

Ogni trasformazione deve indicare la legge usata; se si usa una legge implicativa dentro una formula più grande, bisogna anche controllare la polarità dell'occorrenza sostituita.

## Esercizi suggeriti dalla lezione

1. Dimostrare con tavole di verità alcune leggi di congiunzione, disgiunzione e negazione.
2. Mostrare che $P\Rightarrow(\neg P\Rightarrow Q)$ è una tautologia, mentre $(P\Rightarrow\neg P)\Rightarrow Q$ non lo è.
3. Dimostrare il modus ponens riducendo $((P\Rightarrow Q)\land P)\Rightarrow Q$ a $\mathrm{T}$.
4. Trovare un controesempio per $((P\Rightarrow\neg E)\land\neg P)\Rightarrow E$.
5. Verificare che $(P\land Q)\lor R$ non è equivalente a $P\land(Q\lor R)$.
6. Classificare come positive o negative le diverse occorrenze di una stessa proposizione in formule annidate.

## Fonte

Dispensa **Lezione 4**, P. Mancarella, corso FPL (017AA), a.a. 2026/2027. La slide di apertura riporta la data del **1 ottobre 2026**.
