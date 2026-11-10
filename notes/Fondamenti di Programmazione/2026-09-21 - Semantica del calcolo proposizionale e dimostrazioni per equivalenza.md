---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-09-21'
title: Semantica del calcolo proposizionale e dimostrazioni per equivalenza
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-09-21 - Semantica del calcolo proposizionale e dimostrazioni per equivalenza.md
vault_hash: 5b4e51be75bd5cf16e512e0c92872a8e728ef514d63766d75f7fa3a6ed105b5d
---

## 1. Semantica dei connettivi logici

I [[Connettivo logico|connettivi]] permettono di costruire nuove [[Proposizione|proposizioni]] a partire da proposizioni già note. Il valore di verità della proposizione composta dipende dai valori di verità delle sue componenti.

Indichiamo con

$$
\mathrm{Bool}=\{\mathsf f,\mathsf t\}
$$

l'[[Insieme|insieme]] dei **valori booleani**, dove $\mathsf f$ significa falso e $\mathsf t$ significa vero. La semantica dei connettivi è definita dalle [[Tavola di verità|tabelle di verità]].

### 1.1 Negazione, congiunzione e disgiunzione

| $P$ | $Q$ | $\neg P$ | $P\land Q$ | $P\lor Q$ |
|---|---|---|---|---|
| $\mathsf t$ | $\mathsf t$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf f$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf f$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf f$ | $\mathsf f$ |

Quindi:

- $\neg P$ è vera quando $P$ è falsa;
- $P\land Q$ è vera soltanto quando sia $P$ sia $Q$ sono vere;
- $P\lor Q$ è vera quando almeno una tra $P$ e $Q$ è vera.

### 1.2 Implicazione

L'[[Implicazione|implicazione]] richiede un po' di attenzione:

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| $\mathsf t$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf f$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ |

$P\Rightarrow Q$ afferma che ogni situazione in cui $P$ è vera è anche una situazione in cui $Q$ è vera. L'unico caso incompatibile con questa affermazione è quello in cui $P$ è vera e $Q$ è falsa. Se la premessa $P$ è falsa, l'implicazione è considerata vera.

La stessa condizione si esprime con:

$$
(P\Rightarrow Q)\equiv\neg(P\land\neg Q).
$$

### 1.3 Equivalenza e tabella riassuntiva

L'equivalenza $P\equiv Q$ è vera quando $P$ e $Q$ hanno lo stesso valore di verità.

| $P$ | $Q$ | $\neg P$ | $P\land Q$ | $P\lor Q$ | $P\Rightarrow Q$ | $P\equiv Q$ |
|---|---|---|---|---|---|---|
| $\mathsf t$ | $\mathsf t$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf f$ | $\mathsf f$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf f$ |
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |

## 2. Sintassi del calcolo proposizionale

Nel [[Calcolo proposizionale|calcolo proposizionale]] sia $\mathcal P=\{p,q,r,\ldots\}$ un insieme di **simboli proposizionali**, detto alfabeto. Le formule proposizionali sono tutte e sole quelle ottenute con le regole seguenti:

1. $\mathrm T$ e $\mathrm F$ sono formule proposizionali;
2. ogni $p\in\mathcal P$ è una formula proposizionale;
3. se $P$ e $Q$ sono formule proposizionali, allora lo sono anche

   $$
   \neg P,\qquad
   (P\land Q),\qquad
   (P\lor Q),\qquad
   (P\Rightarrow Q),\qquad
   (P\equiv Q).
   $$

$\mathrm T$ e $\mathrm F$ non sono elementi dell'alfabeto $\mathcal P$: indicano rispettivamente una formula sempre vera e una formula sempre falsa.

L'insieme delle formule costruibili dall'alfabeto $\mathcal P$ si indica con $\mathrm{Prop}_{\mathcal P}$, o più semplicemente con $\mathrm{Prop}$.

### 2.1 Grammatica libera da contesto

La sintassi si può descrivere con una grammatica libera da contesto:

```text
Prop ::= (Prop ≡ Prop)
       | (Prop ∧ Prop)
       | (Prop ∨ Prop)
       | (Prop ⇒ Prop)
       | ¬Prop
       | T
       | F
       | p | q | ...
```

In informatica questo formalismo è comunemente usato per specificare la sintassi di un linguaggio.

## 3. Formalizzazione di enunciati

### 3.1 I tre amici al cinema

Introduciamo l'alfabeto $\{a,b,c\}$:

- $a$: «Antonio va al cinema»;
- $b$: «Bruno va al cinema»;
- $c$: «Corrado va al cinema».

Le premesse sono:

- se Corrado va al cinema, allora ci va anche Antonio: $c\Rightarrow a$;
- condizione necessaria affinché Antonio vada al cinema è che ci vada Bruno: $a\Rightarrow b$.

Vogliamo stabilire quale delle formule seguenti sia una conseguenza logica delle premesse:

1. $c\Rightarrow b$;
2. $(\neg a\land\neg b)\land\neg c$;
3. $b\Rightarrow c$;
4. $\neg c\Rightarrow\neg b$.

Il punto non è solo tradurre le frasi, ma capire quali conclusioni sono vere in tutti i casi compatibili con le premesse.

### 3.2 Altri esempi

Poniamo:

- $p$: piove;
- $n$: ci sono nuvole;
- $c$: ci si copre;
- $r$: fa freddo;
- $v$: c'è vento;
- $ne$: nevica.

| Enunciato | Formalizzazione |
|---|---|
| Piove e fa molto freddo | $p\land r$ |
| Fa freddo, ma non piove | $r\land\neg p$ |
| Se ci sono nuvole e non c'è vento, allora piove | $(n\land\neg v)\Rightarrow p$ |
| Nevica, ma non fa freddo se ci si copre | $ne\land(c\Rightarrow\neg r)$ |
| Se ci si copre, allora fa freddo o nevica | $c\Rightarrow(r\lor ne)$ |
| Piove solo se ci sono nuvole e non c'è vento | $p\Rightarrow(n\land\neg v)$ |

> [!important]
> «$P$ solo se $Q$» si traduce $P\Rightarrow Q$: $Q$ è una condizione necessaria per $P$.

## 4. Interpretazioni e semantica delle formule

In generale il valore di verità di una formula dipende dai valori assegnati ai simboli proposizionali che contiene, proprio come il valore di un'espressione algebrica dipende dalle sue variabili.

Un'[[Interpretazione|interpretazione]] è una [[Funzione|funzione]]

$$
I:\mathcal P\longrightarrow\mathrm{Bool}.
$$

Si può rappresentare, per esempio, come

$$
I=\{p\mapsto\mathsf t,\ q\mapsto\mathsf f,\ r\mapsto\mathsf f\}.
$$

Le tabelle di verità rappresentano le funzioni che interpretano i connettivi:

$$
\begin{aligned}
\neg&:\mathrm{Bool}\to\mathrm{Bool},\\
\land,\lor,\Rightarrow,\equiv&:\mathrm{Bool}\times\mathrm{Bool}\to\mathrm{Bool}.
\end{aligned}
$$

### 4.1 Funzione di valutazione

Fissata un'interpretazione $I$, la semantica delle formule è data dalla funzione

$$
\llbracket\cdot\rrbracket_I:\mathrm{Prop}\longrightarrow\mathrm{Bool},
$$

definita ricorsivamente:

$$
\begin{aligned}
\llbracket\mathrm T\rrbracket_I&=\mathsf t,
&\llbracket\mathrm F\rrbracket_I&=\mathsf f,\\
\llbracket p\rrbracket_I&=I(p) &&\text{se }p\in\mathcal P,\\
\llbracket(P)\rrbracket_I&=\llbracket P\rrbracket_I,\\
\llbracket\neg P\rrbracket_I&=\neg\llbracket P\rrbracket_I,\\
\llbracket P\land Q\rrbracket_I&=\llbracket P\rrbracket_I\land\llbracket Q\rrbracket_I,\\
\llbracket P\lor Q\rrbracket_I&=\llbracket P\rrbracket_I\lor\llbracket Q\rrbracket_I,\\
\llbracket P\Rightarrow Q\rrbracket_I&=\llbracket P\rrbracket_I\Rightarrow\llbracket Q\rrbracket_I,\\
\llbracket P\equiv Q\rrbracket_I&=\llbracket P\rrbracket_I\equiv\llbracket Q\rrbracket_I.
\end{aligned}
$$

Per abuso di linguaggio, la stessa notazione serve sia per il connettivo sintattico sia per la corrispondente funzione booleana.

### 4.2 Esempio di valutazione

Consideriamo

$$
\varphi=(p\land q)\lor\neg r
$$

e l'interpretazione

$$
I=\{p\mapsto\mathsf t,\ q\mapsto\mathsf f,\ r\mapsto\mathsf f\}.
$$

Allora:

$$
\begin{aligned}
\llbracket(p\land q)\lor\neg r\rrbracket_I
&=(\mathsf t\land\mathsf f)\lor\neg\mathsf f\\
&=\mathsf f\lor\mathsf t\\
&=\mathsf t.
\end{aligned}
$$

La valutazione procede dalle sottoformule più semplici verso il connettivo principale.

## 5. Modelli e conseguenza logica

Siano $\varphi$ una formula e $I$ un'interpretazione. $I$ è un **modello** di $\varphi$ se e solo se rende vera la formula:

$$
I\models\varphi
\quad\Longleftrightarrow\quad
\llbracket\varphi\rrbracket_I=\mathsf t.
$$

La nozione si estende a un insieme di formule $\Gamma$:

$$
I\models\Gamma
\quad\Longleftrightarrow\quad
I\models\varphi\ \text{per ogni }\varphi\in\Gamma.
$$

Una formula $\varphi$ è [[Conseguenza logica|conseguenza logica]] di $\Gamma$ quando ogni modello di $\Gamma$ è anche modello di $\varphi$:

$$
\Gamma\models\varphi
\quad\Longleftrightarrow\quad
\text{per ogni }I,\ I\models\Gamma\Rightarrow I\models\varphi.
$$

> [!example] Esempio
> Sia $\Gamma=\{p,\ p\Rightarrow q\}$. I suoi modelli devono rendere vera $p$ e quindi anche $q$ (altrimenti $p\Rightarrow q$ sarebbe falsa). L'unico modello è $\{p\mapsto\mathsf t,\ q\mapsto\mathsf t\}$, che rende vera anche $q$: dunque $\Gamma\models q$.

## 6. Tavole di verità

Una tavola di verità elenca il valore di una formula per ogni possibile interpretazione dei simboli proposizionali che vi compaiono. Se i simboli distinti sono $n$, le interpretazioni possibili sono $2^n$.

Per

$$
\varphi=(p\land q)\lor\neg r
$$

si ottiene:

| $p$ | $q$ | $r$ | $p\land q$ | $\neg r$ | $\varphi$ |
|---|---|---|---|---|---|
| $\mathsf t$ | $\mathsf t$ | $\mathsf t$ | $\mathsf t$ | $\mathsf f$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf t$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf f$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf f$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf f$ |
| $\mathsf f$ | $\mathsf f$ | $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |

Il valore della formula è quello determinato dal **connettivo principale**, cioè l'unico connettivo che non compare come argomento di un altro connettivo.

## 7. Soddisfacibilità, tautologie e contraddizioni

Sia $\varphi$ una formula.

- $\varphi$ è **soddisfacibile** se esiste almeno un'interpretazione $I$ tale che $I\models\varphi$;
- $\varphi$ è una [[Tautologia|tautologia]] se è vera in ogni interpretazione:

  $$
  \models\varphi;
  $$

- $\varphi$ è una **contraddizione**, o è **insoddisfacibile**, se è falsa in ogni interpretazione.

Esempi fondamentali:

$$
p\lor\neg p
$$

è una tautologia, mentre

$$
p\land\neg p
$$

è una contraddizione. In generale, $\varphi$ è una tautologia se e solo se $\neg\varphi$ è una contraddizione.

### 7.1 Strategie di verifica

- Per dimostrare che una formula è soddisfacibile basta trovare una sola interpretazione che la renda vera.
- Per dimostrare che una formula non è una tautologia basta trovare una sola interpretazione che la renda falsa.
- Per dimostrare che una formula è una tautologia bisogna invece considerare tutte le interpretazioni oppure costruire una dimostrazione.

Per un insieme finito di premesse:

$$
\{\varphi_1,\ldots,\varphi_n\}\models\varphi
$$

si può verificare che

$$
(\varphi_1\land\cdots\land\varphi_n)\Rightarrow\varphi
$$

sia una tautologia.

### 7.2 Equivalenza tramite tavola di verità

Confrontando i valori di $P\Rightarrow Q$ e $\neg(P\land\neg Q)$ in tutte le interpretazioni si ottiene:

| $P$ | $Q$ | $P\Rightarrow Q$ | $\neg(P\land\neg Q)$ |
|---|---|---|---|
| $\mathsf t$ | $\mathsf t$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf t$ | $\mathsf f$ | $\mathsf f$ | $\mathsf f$ |
| $\mathsf f$ | $\mathsf t$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ | $\mathsf t$ |

Le due formule sono dunque [[Equivalenza logica|equivalenti]] in ogni interpretazione:

$$
\models(P\Rightarrow Q)\equiv\neg(P\land\neg Q).
$$

## 8. Dalle tavole di verità alle dimostrazioni

Le tavole di verità sono un procedimento meccanico, ma per una formula con $n$ simboli richiedono di esaminare $2^n$ casi. Il costo cresce in fretta; inoltre, nella logica dei predicati i modelli di una formula possono essere infiniti.

Si introduce quindi l'idea di costruire una **dimostrazione**, trasformando passo dopo passo le formule con leggi note.

### 8.1 Esempio aritmetico

Una dimostrazione familiare è:

$$
\begin{aligned}
(a+b)(a-b)
&=a(a-b)+b(a-b) &&\text{distributività}\\
&=(a^2-ab)+(ba-b^2) &&\text{distributività}\\
&=a^2-ab+ba-b^2 &&\text{associatività}\\
&=a^2+0-b^2 &&\text{commutatività e }-x+x=0\\
&=a^2-b^2 &&\text{elemento neutro}.
\end{aligned}
$$

Ogni passaggio è giustificato da una o più leggi e dal **principio di sostituzione per l'uguaglianza**:

> Se $A=B$, il valore di un'espressione $C$ non cambia sostituendo in essa $A$ con $B$.

In simboli:

$$
\frac{A=B}{C=C[B/A]},
$$

dove $C[B/A]$ indica l'espressione ottenuta da $C$ sostituendo $A$ con $B$.

## 9. Sostituzione per l'equivalenza

Nel calcolo proposizionale l'analogo del principio precedente è il [[Principio di sostituzione|principio di sostituzione]] per l'equivalenza:

$$
\frac{P\equiv Q}{R\equiv R[Q/P]}.
$$

Se $P$ e $Q$ sono equivalenti, una formula $R$ resta equivalente alla formula ottenuta sostituendo in essa $P$ con $Q$. A volte $R[Q/P]$ si indica anche con $R^Q_P$.

In questo contesto una **legge** è una tautologia, in particolare una tautologia che descrive una proprietà dei connettivi o che si usa come giustificazione in una dimostrazione.

### 9.1 Prime leggi dell'equivalenza

Per formule arbitrarie $P$, $Q$ e $R$ valgono:

| Legge | Formula |
|---|---|
| Riflessività | $P\equiv P$ |
| Simmetria | $(P\equiv Q)\equiv(Q\equiv P)$ |
| Transitività | $((P\equiv Q)\land(Q\equiv R))\Rightarrow(P\equiv R)$ |
| Associatività | $((P\equiv Q)\equiv R)\equiv(P\equiv(Q\equiv R))$ |
| Unità | $(P\equiv\mathrm T)\equiv P$ |

Ogni legge usata andrebbe verificata come tautologia. La verifica può essere immediata, fatta con una tavola di verità, derivata da leggi già introdotte oppure lasciata come esercizio.

### 9.2 Verifica della legge di unità

Per verificare

$$
(P\equiv\mathrm T)\equiv P,
$$

basta controllare i due possibili valori di $p$:

| $p$ | $p\equiv\mathrm T$ | $(p\equiv\mathrm T)\equiv p$ |
|---|---|---|
| $\mathsf t$ | $\mathsf t$ | $\mathsf t$ |
| $\mathsf f$ | $\mathsf f$ | $\mathsf t$ |

La formula è vera in entrambe le interpretazioni, quindi è una tautologia.

## 10. Schema concettuale

Il calcolo proposizionale distingue con chiarezza:

1. **sintassi**, che stabilisce quali formule sono ben formate;
2. **interpretazione**, che assegna valori booleani ai simboli proposizionali;
3. **semantica**, che calcola ricorsivamente il valore delle formule;
4. **modello**, cioè un'interpretazione che rende vera una formula o un insieme di formule;
5. **conseguenza logica**, che richiede che tutti i modelli delle premesse siano modelli della conclusione;
6. **dimostrazione**, che trasforma formule con leggi e regole di inferenza.

Le tavole di verità permettono di verificare le proprietà in modo semantico; le dimostrazioni per sostituzione offrono invece un metodo simbolico per trasformare una formula conservandone il valore di verità.

## Fonte

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 3, 29 settembre 2026, pp. 63-93 del materiale del corso. La prima pagina del PDF conclude la Lezione 2 e introduce le tabelle di verità; le restanti pagine costituiscono la Lezione 3.
