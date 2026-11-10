---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-09-23'
title: Forme normali, tecniche di dimostrazione e logica del primo ordine
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine.md
vault_hash: cd0043c82dae7f694008d1acfd964dc97ca138e4823846db6c32a2585cbcac57
---

## 1. Dimostrare implicazioni

Una dimostrazione nel [[Calcolo proposizionale|calcolo proposizionale]] procede trasformando le formule con equivalenze o [[Implicazione|implicazioni]] note, giustificando ogni passaggio.

Un esempio fondamentale è il **tollendo tollens**:

$$
((P\Rightarrow Q)\land\neg Q)\Rightarrow\neg P.
$$

Infatti:

$$
\begin{aligned}
(P\Rightarrow Q)\land\neg Q
&\equiv (\neg P\lor Q)\land\neg Q
&&\text{(eliminazione di }\Rightarrow\text{)}\\
&\equiv \neg P\land\neg Q
&&\text{(complemento)}\\
&\Rightarrow \neg P
&&\text{(semplificazione di }\land\text{)}.
\end{aligned}
$$

## 2. Forme normali

Per confrontare formule o applicare metodi automatici di dimostrazione conviene portarle in una forma standard, detta [[Forma normale|forma normale]].

- Una **forma normale congiuntiva** (FNC) è una congiunzione di disgiunzioni di variabili proposizionali, eventualmente negate:

  $$
  (P_1\lor P_2\lor\cdots)\land(Q_1\lor Q_2\lor\cdots)\land\cdots
  $$

- Una **forma normale disgiuntiva** (FND) è una disgiunzione di congiunzioni di variabili proposizionali, eventualmente negate:

  $$
  (P_1\land P_2\land\cdots)\lor(Q_1\land Q_2\land\cdots)\lor\cdots
  $$

Occhio: portare una formula in forma normale può farne crescere parecchio la dimensione, soprattutto per effetto delle leggi distributive.

### 2.1 Confronto mediante forma normale

Consideriamo:

$$
\Phi_1=\neg((P\Rightarrow Q)\land(R\Rightarrow P))
$$

e

$$
\Phi_2=\neg(\neg Q\Rightarrow\neg P)\lor\neg(R\Rightarrow P).
$$

Portando $\Phi_1$ in FND:

$$
\begin{aligned}
\neg((P\Rightarrow Q)\land(R\Rightarrow P))
&\equiv\neg(P\Rightarrow Q)\lor\neg(R\Rightarrow P)\\
&\equiv\neg(\neg P\lor Q)\lor\neg(\neg R\lor P)\\
&\equiv(P\land\neg Q)\lor(R\land\neg P).
\end{aligned}
$$

Per $\Phi_2$ si ottiene:

$$
\begin{aligned}
\neg(\neg Q\Rightarrow\neg P)\lor\neg(R\Rightarrow P)
&\equiv\neg(Q\lor\neg P)\lor\neg(\neg R\lor P)\\
&\equiv(\neg Q\land P)\lor(R\land\neg P).
\end{aligned}
$$

Le due forme coincidono a meno della commutatività di $\land$; dunque $\Phi_1\equiv\Phi_2$.

## 3. Principio di risoluzione

Il [[Principio di risoluzione|principio di risoluzione]] permette di eliminare una variabile che compare positivamente in una clausola e negativamente in un'altra:

$$
(P\lor Q)\land(\neg P\lor R)\Rightarrow(Q\lor R).
$$

In forma più generale:

$$
(P\lor Q_1\lor\cdots\lor Q_n)
\land
(\neg P\lor R_1\lor\cdots\lor R_k)
\Rightarrow
Q_1\lor\cdots\lor Q_n\lor R_1\lor\cdots\lor R_k.
$$

Un caso particolare utile è:

$$
(P\lor Q_1\lor\cdots\lor Q_n)\land\neg P
\Rightarrow
Q_1\lor\cdots\lor Q_n.
$$

### 3.1 Esempio

Per dimostrare che

$$
((P\lor Q)\land(\neg P\lor R)\land(\neg Q\lor R))\Rightarrow R
$$

è una tautologia, si applica due volte la risoluzione:

$$
\begin{aligned}
(P\lor Q)\land(\neg P\lor R)\land(\neg Q\lor R)
&\Rightarrow(Q\lor R)\land(\neg Q\lor R)\\
&\Rightarrow R\land R\\
&\equiv R.
\end{aligned}
$$

La regola deriva dalla transitività dell'implicazione:

$$
\begin{aligned}
(P\lor Q)\land(\neg P\lor R)
&\equiv(\neg Q\Rightarrow P)\land(P\Rightarrow R)\\
&\Rightarrow(\neg Q\Rightarrow R)\\
&\equiv Q\lor R.
\end{aligned}
$$

La risoluzione è anche il meccanismo di calcolo alla base della **programmazione logica**.

## 4. Completezza funzionale dei connettivi

Un insieme di [[Connettivo logico|connettivi]] è **funzionalmente completo** se permette di esprimere tutti gli altri connettivi ([[Completezza funzionale|completezza funzionale]]).

L'insieme $\{\land,\neg\}$ è funzionalmente completo perché:

$$
P\Rightarrow Q\equiv\neg(P\land\neg Q),
$$

$$
(P\equiv Q)\equiv
\neg(P\land\neg Q)\land\neg(Q\land\neg P),
$$

$$
P\lor Q\equiv\neg(\neg P\land\neg Q).
$$

Anche $\{\lor,\neg\}$ e $\{\Rightarrow,\neg\}$ sono funzionalmente completi.

### 4.1 Il connettivo NAND

Il **NAND**, indicato con $\uparrow$, è definito da:

$$
P\uparrow Q\equiv\neg(P\land Q).
$$

| $P$ | $Q$ | $P\uparrow Q$ |
|---|---|---|
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf t$ | $\mathsf f$ |

Questo singolo connettivo è funzionalmente completo.

> [!example] Esempio
> Con il solo NAND si ricostruiscono gli altri connettivi: $\neg P\equiv P\uparrow P$ e $P\land Q\equiv(P\uparrow Q)\uparrow(P\uparrow Q)$, perché negare un NAND restituisce la congiunzione.

## 5. Tecniche di dimostrazione come tautologie

Molte tecniche matematiche di dimostrazione corrispondono a tautologie del calcolo proposizionale.

### 5.1 Dimostrazione per assurdo

Per dimostrare $P$ basta mostrare che, assumendo $\neg P$, si ottiene una contraddizione ([[Dimostrazione per assurdo|dimostrazione per assurdo]]):

$$
P\equiv(\neg P\Rightarrow\mathrm F).
$$

Se la tesi è un'implicazione $Q\Rightarrow R$, allora

$$
(Q\Rightarrow R)\equiv((Q\land\neg R)\Rightarrow\mathrm F).
$$

Quindi, per dimostrare che dall'ipotesi $Q$ segue $R$, si possono assumere insieme $Q$ e $\neg R$ e derivare una contraddizione.

#### Esempio

Dimostriamo per assurdo:

$$
(P\lor Q\Rightarrow R)\Rightarrow(P\Rightarrow R).
$$

Negando l'intera formula:

$$
\begin{aligned}
\neg((P\lor Q\Rightarrow R)\Rightarrow(P\Rightarrow R))
&\equiv(P\lor Q\Rightarrow R)\land\neg(P\Rightarrow R)\\
&\equiv(\neg(P\lor Q)\lor R)\land P\land\neg R\\
&\Rightarrow\neg(P\lor Q)\land P\\
&\equiv\neg P\land\neg Q\land P\\
&\equiv\mathrm F.
\end{aligned}
$$

### 5.2 Dimostrazione per controposizione

$$
(P\Rightarrow Q)\equiv(\neg Q\Rightarrow\neg P).
$$

Per dimostrare $P\Rightarrow Q$ basta quindi dimostrare $\neg Q\Rightarrow\neg P$ ([[Contrapposizione|controposizione]]).

### 5.3 Dimostrazione per casi

$$
(P\Rightarrow Q)\land(\neg P\Rightarrow Q)\equiv Q.
$$

Per dimostrare $Q$ ([[Dimostrazione per casi|dimostrazione per casi]]) si sceglie una proposizione $P$ utile e si dimostra $Q$ separatamente sotto le ipotesi $P$ e $\neg P$.

### 5.4 Combinare due implicazioni

Vale la legge:

$$
(P\Rightarrow Q)\land(R\Rightarrow S)
\Rightarrow
(P\land R\Rightarrow Q\land S).
$$

La si può verificare per controposizione oppure trasformando direttamente le premesse:

$$
\begin{aligned}
(P\Rightarrow Q)\land(R\Rightarrow S)
&\equiv(\neg P\lor Q)\land(\neg R\lor S)\\
&\Rightarrow(\neg P\lor\neg R\lor Q)\land(\neg P\lor\neg R\lor S)\\
&\equiv(\neg P\lor\neg R)\lor(Q\land S)\\
&\equiv\neg(P\land R)\lor(Q\land S)\\
&\equiv P\land R\Rightarrow Q\land S.
\end{aligned}
$$

## 6. Che cosa esprime una dimostrazione

Un singolo passo

$$
P\mathrel{\mathrm{conn}}Q\qquad\{G\}
$$

è corretto se la formula

$$
G\Rightarrow(P\mathrel{\mathrm{conn}}Q)
$$

è una [[Tautologia|tautologia]]. Se $G$ è una legge, quindi $G\equiv\mathrm T$, resta semplicemente $P\mathrel{\mathrm{conn}}Q$.

Per una catena

$$
P_1\mathrel{\mathrm{conn}_1}P_2
\mathrel{\mathrm{conn}_2}\cdots
\mathrel{\mathrm{conn}_{n-1}}P_n,
$$

giustificata rispettivamente da $G_1,\ldots,G_{n-1}$, la dimostrazione rappresenta la tautologia

$$
\bigwedge_{i=1}^{n-1}
\left(G_i\Rightarrow(P_i\mathrel{\mathrm{conn}_i}P_{i+1})\right).
$$

Se le proprietà dei connettivi permettono di concludere $P_1\mathrel{\mathrm{conn}}P_n$, allora:

- se tutti i $G_i$ sono tautologie, si è dimostrato $P_1\mathrel{\mathrm{conn}}P_n$;
- se alcuni $G_i$ sono ipotesi non tautologiche, si è dimostrato

  $$
  G_{i_1}\land\cdots\land G_{i_k}
  \Rightarrow
  (P_1\mathrel{\mathrm{conn}}P_n);
  $$

- se un'ipotesi $H$ implica la congiunzione delle giustificazioni usate, si è dimostrato

  $$
  H\Rightarrow(P_1\mathrel{\mathrm{conn}}P_n).
  $$

### 6.1 Usare ipotesi non tautologiche

Per dimostrare $P\Rightarrow Q$ non serve sempre trasformare direttamente l'intera implicazione: si può assumere $P$ e mostrare che, sotto questa ipotesi, $Q$ è vera. Le giustificazioni che dipendono dall'ipotesi vanno indicate esplicitamente.

Per esempio:

$$
P\Rightarrow(P\land Q\equiv Q).
$$

Assumendo $P$:

$$
P\land Q\equiv\mathrm T\land Q\equiv Q.
$$

Un esempio più articolato è:

$$
(P\Rightarrow(Q\equiv R))\Rightarrow(P\land R\Rightarrow Q).
$$

Sotto l'ipotesi $P\Rightarrow(Q\equiv R)$:

$$
\begin{aligned}
P\land R
&\Rightarrow(Q\equiv R)\land R\\
&\equiv(Q\Rightarrow R)\land(R\Rightarrow Q)\land R\\
&\Rightarrow(Q\Rightarrow R)\land Q\\
&\Rightarrow Q.
\end{aligned}
$$

### 6.2 Sillogismo disgiuntivo

$$
(P\lor Q)\land(P\Rightarrow R)\land(Q\Rightarrow S)
\Rightarrow
(R\lor S).
$$

Assumendo $P\Rightarrow R$ e $Q\Rightarrow S$:

$$
P\lor Q\Rightarrow R\lor Q\Rightarrow R\lor S.
$$

Più precisamente, questa catena dimostra

$$
(P\Rightarrow R)\land(Q\Rightarrow S)
\Rightarrow
(P\lor Q\Rightarrow R\lor S),
$$

equivalente al sillogismo disgiuntivo grazie a

$$
P\Rightarrow(Q\Rightarrow R)
\equiv
(P\land Q\Rightarrow R).
$$

## 7. Formulario essenziale del calcolo proposizionale

Le leggi non vanno memorizzate tutte: servono soprattutto a riconoscere equivalenze, semplificare formule e giustificare i passaggi.

### 7.1 Equivalenza

$$
\begin{gathered}
P\equiv P,\\
(P\equiv Q)\equiv(Q\equiv P),\\
((P\equiv Q)\land(Q\equiv R))\Rightarrow(P\equiv R),\\
((P\equiv Q)\equiv R)\equiv(P\equiv(Q\equiv R)),\\
(P\equiv\mathrm T)\equiv P.
\end{gathered}
$$

### 7.2 Congiunzione e disgiunzione

Per entrambi valgono commutatività, associatività e idempotenza. Inoltre:

$$
\begin{aligned}
P\land\mathrm T&\equiv P,
&P\lor\mathrm F&\equiv P,\\
P\land\mathrm F&\equiv\mathrm F,
&P\lor\mathrm T&\equiv\mathrm T,\\
P\land(Q\lor R)&\equiv(P\land Q)\lor(P\land R),\\
P\lor(Q\land R)&\equiv(P\lor Q)\land(P\lor R).
\end{aligned}
$$

### 7.3 Negazione

$$
\begin{aligned}
\neg\neg P&\equiv P,\\
P\lor\neg P&\equiv\mathrm T,\\
P\land\neg P&\equiv\mathrm F,\\
\neg(P\land Q)&\equiv\neg P\lor\neg Q,\\
\neg(P\lor Q)&\equiv\neg P\land\neg Q,\\
\neg\mathrm T&\equiv\mathrm F,
&\neg\mathrm F&\equiv\mathrm T.
\end{aligned}
$$

### 7.4 Eliminazione dei connettivi

$$
\begin{aligned}
(P\Rightarrow Q)&\equiv(\neg P\lor Q),\\
(P\Rightarrow Q)&\equiv\neg(P\land\neg Q),\\
\neg(P\Rightarrow Q)&\equiv(P\land\neg Q),\\
(P\equiv Q)&\equiv(P\Rightarrow Q)\land(Q\Rightarrow P),\\
(P\equiv Q)&\equiv(P\land Q)\lor(\neg P\land\neg Q).
\end{aligned}
$$

### 7.5 Implicazione, complemento e assorbimento

$$
\begin{aligned}
(P\Rightarrow Q)\land P&\Rightarrow Q &&\text{(modus ponens)},\\
(P\Rightarrow Q)\land(Q\Rightarrow R)&\Rightarrow(P\Rightarrow R),\\
P\land Q&\Rightarrow P,\\
P&\Rightarrow P\lor Q,\\
P\lor(\neg P\land Q)&\equiv P\lor Q,\\
P\land(\neg P\lor Q)&\equiv P\land Q,\\
P\land(P\lor Q)&\equiv P,\\
P\lor(P\land Q)&\equiv P.
\end{aligned}
$$

Un'altra legge utile, detta **scambio**, è:

$$
(P\land Q\Rightarrow R)
\equiv
(P\land\neg R\Rightarrow\neg Q).
$$

## 8. Perché il calcolo proposizionale non basta

Il calcolo proposizionale permette di:

- costruire formule e interpretarne il significato;
- stabilire validità e soddisfacibilità;
- dimostrare equivalenze e conseguenze logiche.

Le proposizioni atomiche $P,Q,R,\ldots$ sono però **indivisibili**. Non mostrano la struttura interna degli enunciati e non permettono di parlare direttamente di individui, proprietà e relazioni.

Per esempio, l'enunciato «Alberto va al cinema con Bruno o va al teatro con Carlo» si può rappresentare come

$$
(AC\land BC)\lor(AT\land CT),
$$

ma nella formula scompaiono gli individui Alberto, Bruno e Carlo e la relazione «andare a».

Il calcolo proposizionale è inoltre inadeguato per:

- esprimere proprietà di insiemi infiniti, come «tutti i numeri pari maggiori di due non sono primi»;
- formulare proprietà generali che dipendono da una variabile, come «se $x$ è pari, allora $x+1$ è dispari»;
- descrivere in modo compatto proprietà che riguardano molti individui, come «tutti gli studenti di FPL vanno al cinema».

## 9. Verso la logica del primo ordine

La [[Logica del primo ordine|logica del primo ordine]] (LPO) estende il calcolo proposizionale introducendo:

- **termini**, per denotare gli individui del dominio;
- **predicati**, per esprimere proprietà e relazioni;
- [[Quantificatore|quantificatori]], per dire che una formula vale per tutti gli individui o per almeno uno.

Anche una formula di LPO assume un valore booleano rispetto a un'[[Interpretazione|interpretazione]], ma la sua valutazione è più complessa di quella proposizionale. Le formule vere in ogni interpretazione sono dette **valide**, in analogia con le tautologie. Non esistono tavole di verità finite che decidano in generale la validità: bisogna costruire una dimostrazione, e non sempre si riesce a trovarne una.

### 9.1 Esempi di espressività

«Tutti i numeri pari maggiori di due non sono primi»:

$$
\forall x.\bigl((\operatorname{pari}(x)\land x>2)\Rightarrow\neg\operatorname{primo}(x)\bigr).
$$

«Esiste almeno un numero naturale maggiore di due che non è primo»:

$$
\exists x.\bigl((x>2)\land\neg\operatorname{primo}(x)\bigr).
$$

«Se $x$ è pari, allora $x+1$ è dispari»:

$$
\forall x.\bigl(\operatorname{pari}(x)\Rightarrow\operatorname{dispari}(x+1)\bigr).
$$

La proprietà generale permette di ricavare istanze particolari, per esempio:

$$
\forall x.\bigl(\operatorname{pari}(x)\Rightarrow\operatorname{dispari}(x+1)\bigr)
\Rightarrow
(\operatorname{pari}(4)\Rightarrow\operatorname{dispari}(5)).
$$

«Tutti gli studenti di FPL vanno al cinema»:

$$
\forall x.\bigl(
(\operatorname{studente}(x)\land\operatorname{frequenta}(x,\mathrm{FPL}))
\Rightarrow
\operatorname{vaAlCinema}(x)
\bigr).
$$

Per esprimere che **esattamente uno** studente di FPL non va al cinema, non basta dire che ne esiste almeno uno: bisogna anche imporre che tutti gli altri ci vadano:

$$
\exists x.\Bigl(
\operatorname{studente}(x)
\land\operatorname{frequenta}(x,\mathrm{FPL})
\land\neg\operatorname{vaAlCinema}(x)
\land
\forall y.\bigl(
\operatorname{studente}(y)
\land\operatorname{frequenta}(y,\mathrm{FPL})
\land y\neq x
\Rightarrow
\operatorname{vaAlCinema}(y)
\bigr)
\Bigr).
$$

## Fonte

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 5, 2 ottobre 2026, slide 131-176.
