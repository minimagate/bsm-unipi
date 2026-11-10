---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-10-08'
title: Sintassi e semantica della logica del primo ordine
source: Lezione_06.pdf (slide 177-200)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-10-08 - Sintassi e semantica della logica del primo ordine.md
vault_hash: af93b0606c5993a1d83234b0860ca262ad20f0a0a5b451e61750a4964113d515
---

Questa lezione riprende da dove si era fermata [[2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine|la lezione sulle forme normali]], che si concludeva motivando la [[Logica del primo ordine|logica del primo ordine]] (LPO). Come per il [[Calcolo proposizionale|calcolo proposizionale]] (CP), si parte da un alfabeto e si danno le regole per costruire le frasi del linguaggio, le [[Formula ben formata|formule (ben formate)]]; poi si definisce il loro significato tramite le [[Interpretazione|interpretazioni]].

## 1. Ingredienti sintattici

### 1.1 Costanti e predicati

- **Costanti**: simboli con cui ci si riferisce a oggetti specifici, gli **individui** del dominio di interesse su cui si vogliono fare asserti. Esempi: $2$, $\mathrm{FPL}$. Per costanti generiche si useranno $a, b, c, \dots$
- **Predicati**: simboli che esprimono **proprietà** di singoli oggetti o **relazioni** tra oggetti del dominio. Esempi: $\operatorname{pari}(\_)$, $\operatorname{studente}(\_)$, $\operatorname{frequenta}(\_,\_)$. Per predicati generici si useranno $p, q, r, \dots$
- Le **lettere proposizionali** del CP rientrano tra i predicati: esprimono proprietà non riferite a individui (per esempio «piove», «fa caldo»), cioè sono predicati con zero argomenti.
- Restano i simboli $\mathrm{T}$ e $\mathrm{F}$, già noti dal CP.

Con questi ingredienti si costruiscono asserti semplici sugli elementi del dominio, le **formule atomiche**:

$$
\operatorname{pari}(2), \qquad \operatorname{frequenta}(\mathrm{carlo}, \mathrm{FPL}), \qquad p(a,b,c).
$$

Usando i [[Connettivo logico|connettivi]] del CP si ottengono formule non atomiche:

$$
\operatorname{ama}(\mathrm{carlo},\mathrm{cinema}) \land \operatorname{ama}(\mathrm{anna},\mathrm{cinema})
$$

$$
\operatorname{madre}(\mathrm{maria},\mathrm{carlo}) \land \operatorname{madre}(\mathrm{maria},\mathrm{anna}) \Rightarrow \operatorname{sorella}(\mathrm{anna},\mathrm{carlo})
$$

### 1.2 Variabili e quantificatori

Il CP non permette di esprimere proprietà che riguardano **tutti** gli individui o **alcuni** di essi, come «tutti gli uomini sono mortali» o «qualche studente di FPL non è toscano». Servono altri due ingredienti:

- le **variabili**: simboli ausiliari che si riferiscono a individui «generici» del dominio; di solito si usano le ultime lettere dell'alfabeto $x, y, z, x_1, x_2, \dots$
- i [[Quantificatore|quantificatori]]: universale $\forall$ ed esistenziale $\exists$.

Gli esempi precedenti diventano:

$$
\forall x.\bigl(\operatorname{uomo}(x) \Rightarrow \operatorname{mortale}(x)\bigr)
$$

$$
\exists x.\bigl(\operatorname{studente}(x) \land \operatorname{frequenta}(x,\mathrm{FPL}) \land \neg\operatorname{toscano}(x)\bigr)
$$

Le parentesi evidenziano la formula su cui «agisce» il quantificatore.

> [!note] Abbreviazione
> Quantificatori dello stesso tipo annidati si abbreviano:
> $$\forall x.\,\forall y.\,\forall z.\bigl(\operatorname{madre}(x,y) \land \operatorname{madre}(x,z) \Rightarrow \operatorname{fratelli}(y,z)\bigr)$$
> si scrive
> $$\forall x,y,z.\bigl(\operatorname{madre}(x,y) \land \operatorname{madre}(x,z) \Rightarrow \operatorname{fratelli}(y,z)\bigr).$$

### 1.3 Simboli di funzione

Spesso serve riferirsi a oggetti che sono «funzione» di altri:

- «il successore di ogni numero pari è dispari»;
- «il clima di ogni città ne influenza il turismo».

Si introducono quindi i **simboli di funzione**: $f, g, h, \dots$ per funzioni generiche, e $+, -, *, /, \dots$ per le usuali [[Funzione|funzioni]] numeriche, nella consueta notazione infissa.

$$
\forall x.\bigl(\operatorname{pari}(x) \Rightarrow \operatorname{dispari}(x+1)\bigr)
$$

$$
\forall x.\bigl(\operatorname{citta}(x) \Rightarrow \operatorname{influenza}(\operatorname{clima}(x), \operatorname{turismo}(x))\bigr)
$$

Con variabili e funzioni, gli individui su cui agiscono i predicati possono quindi essere indicati da costanti, variabili o applicazioni di funzioni.

---

## 2. Alfabeto, termini e formule

### 2.1 Alfabeto

L'alfabeto di un linguaggio del primo ordine è costituito da:

| Componente | Contenuto |
|---|---|
| $\mathcal{V}$ | simboli di variabile |
| $\mathcal{C}$ | simboli di costante |
| $\mathcal{F}$ | simboli di funzione, ciascuno con la sua **arietà** (numero di argomenti) |
| $\mathcal{P}$ | simboli di predicato, ciascuno con la sua arietà (eventualmente $0$) |
| speciali | $\mathrm{T}$, $\mathrm{F}$ |
| connettivi | $\neg, \land, \lor, \Rightarrow, \equiv$ |
| quantificatori | $\forall, \exists$ |
| punteggiatura | `(` `)` parentesi, `,` virgola, `.` punto |

### 2.2 Termini

I **termini** denotano gli elementi del dominio di interesse (gli individui). Sono definiti **induttivamente**:

1. ogni costante $c \in \mathcal{C}$ è un termine;
2. ogni variabile $x \in \mathcal{V}$ è un termine;
3. se $g \in \mathcal{F}$ ha arietà $n$ e $t_1, \dots, t_n$ sono termini, allora $g(t_1, \dots, t_n)$ è un termine.

Esempi:

- $a$, con $a \in \mathcal{C}$;
- $x$, con $x \in \mathcal{V}$;
- $g(a)$, con $g \in \mathcal{F}$ di arietà $1$;
- $h(x, g(a))$, con $h \in \mathcal{F}$ di arietà $2$.

Per i simboli di funzione binari noti si usa la notazione infissa. Con $+, * \in \mathcal{F}$, il termine $x + (1 * z)$ in notazione prefissa si scriverebbe $+(x, *(1, z))$.

### 2.3 Formule ben formate

Le formule sono le frasi con cui si descrivono gli asserti di interesse, ottenute con le regole:

- **(F0)** $\mathrm{T}$ e $\mathrm{F}$ sono formule;
- **(F1)** se $p \in \mathcal{P}$ ha arietà $n$ e $t_1, \dots, t_n$ sono termini, allora $p(t_1, \dots, t_n)$ è una formula (**atomica**);
- **(F2)** se $P$ è una formula, allora $(P)$ è una formula;
- **(F3)** se $P$ è una formula, allora $\neg P$ è una formula;
- **(F4)** se $P$ e $Q$ sono formule, allora $P \land Q$, $P \lor Q$, $P \Rightarrow Q$, $P \equiv Q$ sono formule;
- **(F5)** se $P$ è una formula e $x \in \mathcal{V}$, allora $(\forall x.P)$ e $(\exists x.P)$ sono formule.

La regola (F1) comprende anche i predicati di arietà $0$, cioè le lettere proposizionali. Anche per i predicati binari noti ($=, <, \le, >, \dots$) si usa la notazione infissa: per esempio $x = y$ oppure $z \le g(x)$, con $=, \le \in \mathcal{P}$.

> [!warning] Termini e formule sono cose diverse
> Un termine denota un **individuo** (per esempio $x+1$); una formula denota un **valore di verità** (per esempio $\operatorname{dispari}(x+1)$). I predicati trasformano termini in formule; le funzioni trasformano termini in termini.

### 2.4 Esempi

| Enunciato | Formula |
|---|---|
| Tutti i numeri pari maggiori di due non sono primi | $(\forall x.\operatorname{pari}(x) \land x > 2 \Rightarrow \neg\operatorname{primo}(x))$ |
| Se $x$ è pari allora il successore di $x$ è dispari | $(\forall x.\operatorname{pari}(x) \Rightarrow \operatorname{dispari}(x+1))$ |
| «Se $x$ è pari allora $x+1$ è dispari» implica «se $4$ è pari allora $5$ è dispari» | $(\forall x.\operatorname{pari}(x) \Rightarrow \operatorname{dispari}(x+1)) \Rightarrow (\operatorname{pari}(4) \Rightarrow \operatorname{dispari}(5))$ |

Nell'ultima formula:

- simboli di variabile: $x$;
- simboli di costante: $1$, $4$, $5$;
- simboli di funzione: $+$;
- simboli di predicato: $\operatorname{pari}(\_)$, $\operatorname{dispari}(\_)$.

---

## 3. Variabili libere e legate

In una formula quantificata come $(\forall x.P)$ o $(\exists y.P)$, la sottoformula $P$ è la **portata** del quantificatore.

Un'occorrenza di una variabile $x$ è **legata** se compare nella portata di un quantificatore $\forall x$ o $\exists x$; altrimenti è **libera** (vedi [[Variabile libera e legata|variabili libere e legate]]). La nozione riguarda le singole **occorrenze**: la stessa variabile può comparire sia libera sia legata nella stessa formula.

Esempio:

$$
(\forall x.\,p(a, x)) \land q(x, y)
$$

- la $x$ in $p(a,x)$ è legata, perché sta nella portata di $\forall x$;
- la $x$ e la $y$ in $q(x,y)$ sono libere, perché le parentesi chiudono la portata prima di $q$.

### 3.1 Esercizio dalle slide

Individuare le occorrenze libere e legate in:

$$
\bigl(\forall y.\; z = y \land (x = y \lor (\exists x.\; x = z \lor z = y))\bigr)
$$

*Soluzione (non presente nelle slide):* la portata di $\forall y$ è tutto il resto della formula, la portata di $\exists x$ è $x = z \lor z = y$.

- tutte le occorrenze di $y$ sono **legate** da $\forall y$;
- tutte le occorrenze di $z$ sono **libere**, perché non c'è alcun quantificatore su $z$;
- la $x$ in $x = y$ è **libera**, perché sta fuori dalla portata di $\exists x$;
- la $x$ in $x = z$ è **legata** da $\exists x$.

La formula è quindi aperta, con variabili libere $x$ e $z$.

### 3.2 Formule aperte e chiuse

- Una formula è **aperta** se contiene occorrenze libere di variabili.
- Una formula è **chiusa** se non contiene variabili libere.
- Si scrive $P(x)$ per indicare esplicitamente che $x$ occorre libera in $P$.

Da qui in avanti ci occuperemo quasi solo di formule chiuse, perché il valore di verità di una formula aperta non è determinato. Sui naturali, con il significato atteso di $\operatorname{multiplo}$ e di $3$:

- $\operatorname{multiplo}(x, 3)$ può essere vera (se $x$ «sta per» $6$) o falsa (se $x$ «sta per» $7$): non si può dire finché non si fissa il valore di $x$;
- $\forall x.\operatorname{multiplo}(x, 3)$ è invece chiusa, e sui naturali è **falsa**.

È la stessa situazione già vista per $x + 1 = 2$, che non è una [[Proposizione|proposizione]] finché $x$ non è specificato ([[2026-09-25 - Stati, algoritmi e fondamenti della logica formale|lezione del 25 settembre]]).

### 3.3 Ridenominazione delle variabili legate

Le variabili legate sono solo dei **segnaposto**: indicano i punti in cui agisce un quantificatore. Per questo si possono ridenominare: $\forall x.\operatorname{multiplo}(x,3)$ e $\forall z.\operatorname{multiplo}(z,3)$ esprimono la stessa cosa.

Le slide anticipano due leggi:

$$
(\forall x.P) \equiv (\forall y.P[y/x]) \quad \text{se } y \text{ non compare in } P
$$

$$
(\exists x.P) \equiv (\exists y.P[y/x]) \quad \text{se } y \text{ non compare in } P
$$

dove $P[y/x]$ è la formula $P$ in cui tutte le occorrenze di $x$ sono sostituite da $y$.

> [!warning]
> La condizione «$y$ non compare in $P$» è essenziale. Per esempio (esempio aggiunto), in $\forall x.\,x \le y$ non si può ridenominare $x$ in $y$: si otterrebbe $\forall y.\,y \le y$, dove la $y$ che prima era libera è stata «catturata» dal quantificatore e il significato cambia.

---

## 4. Interpretazione e semantica

Come nel CP, la semantica di una formula chiusa si determina rispetto a un'**interpretazione**, che fissa il significato dei simboli:

- il **dominio** di interesse (un [[Insieme|insieme]]);
- a quali elementi del dominio corrispondono le costanti in $\mathcal{C}$;
- a quali funzioni sul dominio corrispondono i simboli di funzione in $\mathcal{F}$;
- a quali proprietà o relazioni corrispondono i predicati in $\mathcal{P}$.

Componendo i valori delle formule atomiche si ottiene il valore della formula complessiva. Il procedimento è simile a quello del CP, ma più complesso perché bisogna calcolare funzioni e predicati e gestire i quantificatori.

### 4.1 Esempio introduttivo

Consideriamo la formula chiusa

$$
(\forall x.\,p(x) \lor q(x)).
$$

- **Interpretazione 1**: dominio degli esseri umani, $p$ = «essere maggiorenne», $q$ = «essere minorenne». La formula è **vera**: ogni persona è maggiorenne o minorenne.
- **Interpretazione 2**: dominio dei numeri naturali, $p$ = «essere primo», $q$ = «essere pari». La formula è **falsa**: per esempio $9$ non è né primo né pari.

### 4.2 Definizione formale

Fissato un alfabeto $\mathcal{V}, \mathcal{C}, \mathcal{F}, \mathcal{P}$, un'interpretazione è una coppia

$$
\mathcal{I} = (D, \alpha)
$$

dove:

- $D$ è un insieme, il **dominio** dell'interpretazione;
- $\alpha$ è la **funzione di interpretazione**, che associa:
  - a ogni costante $c \in \mathcal{C}$ un elemento $\alpha(c) \in D$;
  - a ogni simbolo di funzione $g \in \mathcal{F}$ di arietà $n$ una funzione $\alpha(g) : D^n \to D$;
  - a ogni predicato $p \in \mathcal{P}$ di arietà $0$ (simbolo proposizionale) un valore di verità $\alpha(p)$;
  - a ogni predicato $p \in \mathcal{P}$ di arietà $n$ una funzione $\alpha(p) : D^n \to \mathrm{Bool}$.

Qui $D^n$ indica il [[Prodotto cartesiano|prodotto cartesiano]]

$$
D^n = \underbrace{D \times \cdots \times D}_{n \text{ volte}},
$$

cioè l'insieme delle $n$-uple di elementi di $D$.

### 4.3 Esempio: tre interpretazioni dello stesso alfabeto

Alfabeto: $\mathcal{C} = \{a, b, c\}$, $\mathcal{F} = \{\}$, $\mathcal{P} = \{p(\_)\}$, $\mathcal{V} = \{x, y\}$.

| | Dominio | $\alpha(a)$ | $\alpha(b)$ | $\alpha(c)$ | $\alpha(p)(x) = \mathrm{t}$ sse |
|---|---|---|---|---|---|
| $\mathcal{I}_1$ | città italiane | Milano | Roma | Pontedera | $x$ è capoluogo di provincia |
| $\mathcal{I}_2$ | $\{5, 10, 15\}$ | $5$ | $10$ | $15$ | $x$ è multiplo di $5$ |
| $\mathcal{I}_3$ | $\mathbb{N}$ | $5$ | $10$ | $15$ | $x$ è multiplo di $5$ |

Valori di verità (valutazione ancora informale):

| Formula | $\mathcal{I}_1$ | $\mathcal{I}_2$ | $\mathcal{I}_3$ |
|---|---|---|---|
| $p(a)$ | t | t | t |
| $p(b)$ | t | t | t |
| $p(c)$ | f | t | t |
| $p(a) \land p(c)$ | f | t | t |
| $(\exists x.\,p(x))$ | t | t | t |
| $(\forall x.\,p(x))$ | f | t | f |
| $(\exists x.\,p(x)) \land (\exists y.\,\neg p(y))$ | t | f | t |

Osservazioni:

- $\mathcal{I}_2$ e $\mathcal{I}_3$ differiscono **solo nel dominio**, eppure $\forall x.\,p(x)$ è vera nella prima e falsa nella seconda. Il dominio conta anche per gli individui che non hanno un nome nel linguaggio: in $\mathbb{N}$ esiste per esempio $7$, che non è multiplo di $5$.
- Analogamente, in $\mathcal{I}_1$ basta Pontedera (che non è capoluogo) per rendere falsa $\forall x.\,p(x)$ e vera $\exists y.\,\neg p(y)$.

La definizione formale della semantica, in particolare per i quantificatori, è rimandata alle prossime lezioni.

---

## 5. Formalizzare enunciati

### 5.1 Linee guida

Per formalizzare un enunciato $E$ bisogna fornire:

- un alfabeto $\mathcal{A} = (\mathcal{C}, \mathcal{F}, \mathcal{P}, \mathcal{V})$ e un'interpretazione $\mathcal{I} = (D, \alpha)$;
- una formula che, in $\mathcal{I}$, sia vera **se e solo se** $E$ è vero.

Procedimento:

1. individuare il **dominio** $D$ di cui parla l'enunciato;
2. per ogni individuo $d \in D$ menzionato in $E$, introdurre una costante $c \in \mathcal{C}$ con $\alpha(c) = d$;
3. per ogni operatore $op$ menzionato in $E$ che, applicato a elementi di $D$, restituisce un elemento di $D$, introdurre un simbolo di funzione $f \in \mathcal{F}$ con $\alpha(f) = op$;
4. per ogni proprietà o relazione $R$ menzionata in $E$, introdurre un predicato $p \in \mathcal{P}$ con $\alpha(p) = R$;
5. scrivere la formula.

### 5.2 Esempio: numeri pari e primi

«Tutti i numeri pari maggiori di due non sono primi.»

- **Dominio**: $\mathbb{N}$.
- **Individui menzionati**: «due» → costante $2 \in \mathcal{C}$ con $\alpha(2) = 2 \in \mathbb{N}$.
- **Proprietà e relazioni**:
  - $\operatorname{pari} \in \mathcal{P}$, arietà $1$: $\alpha(\operatorname{pari})(n) = \mathrm{t}$ se $n$ è pari, $\mathrm{f}$ altrimenti;
  - $\operatorname{primo} \in \mathcal{P}$, arietà $1$: $\alpha(\operatorname{primo})(n) = \mathrm{t}$ se $n$ è primo, $\mathrm{f}$ altrimenti;
  - $> \in \mathcal{P}$, arietà $2$: $\alpha(>)(n, m) = \mathrm{t}$ se $n$ è maggiore di $m$, $\mathrm{f}$ altrimenti.
- **Formula**:

$$
(\forall x.\,\operatorname{pari}(x) \land x > 2 \Rightarrow \neg\operatorname{primo}(x))
$$

### 5.3 Esempio: gli amici al cinema

Enunciati:

1. Alberto non segue FPL ma va al cinema con Bruno o con Carlo.
2. Tutti gli studenti di FPL vanno al cinema.
3. Tutti gli studenti di FPL tranne uno vanno al cinema.

**Alfabeto e interpretazione**:

- dominio: l'insieme delle persone;
- costanti $A, B, C \in \mathcal{C}$ con $\alpha(A)$ = la persona Alberto, $\alpha(B)$ = la persona Bruno, $\alpha(C)$ = la persona Carlo;
- nessun simbolo di funzione;
- predicati:
  - $\operatorname{vaCinema}$, arietà $1$: $\alpha(\operatorname{vaCinema})(d) = \mathrm{t}$ se $d$ va al cinema;
  - $\operatorname{segueFPL}$, arietà $1$: $\alpha(\operatorname{segueFPL})(d) = \mathrm{t}$ se $d$ segue FPL;
  - $=$, arietà $2$, con il significato standard.

**Formule**:

$$
\neg\operatorname{segueFPL}(A) \land \bigl(\operatorname{vaCinema}(A) \land (\operatorname{vaCinema}(B) \lor \operatorname{vaCinema}(C))\bigr)
$$

$$
(\forall x.\,\operatorname{segueFPL}(x) \Rightarrow \operatorname{vaCinema}(x))
$$

$$
\exists x.\Bigl(\operatorname{segueFPL}(x) \land \neg\operatorname{vaCinema}(x) \land \forall y.\bigl(\operatorname{segueFPL}(y) \land \neg(x = y) \Rightarrow \operatorname{vaCinema}(y)\bigr)\Bigr)
$$

Il «ma» del primo enunciato si traduce con una congiunzione. Nel terzo enunciato, come già visto, non basta dire che uno studente non va al cinema: bisogna anche imporre che **tutti gli altri** ci vadano, ed è per questo che serve il predicato $=$.

Le slide chiedono di confrontare queste formule con quelle della [[2026-09-23 - Forme normali, tecniche di dimostrazione e logica del primo ordine|lezione precedente]], dove «studente di FPL» era reso con $\operatorname{studente}(x) \land \operatorname{frequenta}(x, \mathrm{FPL})$. Qui un unico predicato $\operatorname{segueFPL}$ rende le formule più compatte, ma si perde la possibilità di parlare di altri corsi: la scelta dell'alfabeto dipende da cosa si vuole esprimere.

### 5.4 Esercizio: parenti e antenati

«Due persone sono parenti se hanno un antenato in comune.»

- **Dominio**: l'insieme delle persone.
- **Costanti e operatori**: nessuno.
- **Predicati**:
  - $\operatorname{parenti}$, arietà $2$: $\alpha(\operatorname{parenti})(d_1, d_2) = \mathrm{t}$ se $d_1$ e $d_2$ sono parenti;
  - $\operatorname{antenato}$, arietà $2$: $\alpha(\operatorname{antenato})(d_1, d_2) = \mathrm{t}$ se $d_1$ è antenato di $d_2$.
- **Formula**:

$$
(\forall x.(\forall y.(\exists z.\,\operatorname{antenato}(z,x) \land \operatorname{antenato}(z,y)) \Rightarrow \operatorname{parenti}(x,y)))
$$

o, in forma abbreviata,

$$
(\forall x,y.\,(\exists z.\,\operatorname{antenato}(z,x) \land \operatorname{antenato}(z,y)) \Rightarrow \operatorname{parenti}(x,y)).
$$

L'antenato comune è un individuo che non ha nome nell'enunciato: per questo compare come variabile quantificata esistenzialmente, $\exists z$, all'interno della premessa.

### 5.5 Esercizio: il successore del successore

«Se un numero naturale è pari, lo è anche il successore del suo successore.»

- **Dominio**: $\mathbb{N}$.
- **Operatori menzionati**: «successore» → $\operatorname{succ} \in \mathcal{F}$, arietà $1$, con $\alpha(\operatorname{succ})(n) = n + 1$.
- **Predicati**: $\operatorname{pari}$, come prima.
- **Formula**:

$$
\forall x.\,\operatorname{pari}(x) \Rightarrow \operatorname{pari}(\operatorname{succ}(\operatorname{succ}(x)))
$$

Qui «successore» è un **operatore** (restituisce un individuo), quindi diventa un simbolo di funzione e non un predicato. Il termine $\operatorname{succ}(\operatorname{succ}(x))$ mostra l'annidamento previsto dalla definizione induttiva dei termini.

## Fonte

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 6, 8 ottobre 2026, slide 177-200 (file `Lezione_06.pdf`).
