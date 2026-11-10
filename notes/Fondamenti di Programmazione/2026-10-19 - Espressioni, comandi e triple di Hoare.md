---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-10-19'
title: Espressioni, comandi e triple di Hoare
source: Lezione_09.pdf (slide 260-297)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-10-19 - Espressioni, comandi e triple di Hoare.md
vault_hash: 76b030d5f9ea4a2ac1e9f08aebf6ea25627f5db5c099af199b1f7b954ae3fada
---

# Espressioni, comandi e triple di Hoare

La lezione prosegue la parte sulla programmazione imperativa iniziata con la [[2026-10-13 - Quantificazione ristretta, uguaglianza e specifiche formali|lezione del 13 ottobre]], dove sono arrivati gli [[Stato|stati]] e le [[Specifica di un problema|specifiche]]. Qui si definiscono sintassi e semantica del piccolo linguaggio del corso: prima le **espressioni**, che calcolano valori a partire dallo stato, poi i **comandi**, che invece modificano lo stato. Si scrivono i primi [[Algoritmo|algoritmi]] e infine si introduce la **semantica assiomatica** con le [[Tripla di Hoare|triple di Hoare]], lo strumento che useremo per verificare la correttezza dei programmi.

Notazione già nota: $\mathrm{Ide}$ è l'insieme degli identificatori, $\mathrm{State}$ quello degli stati $\sigma:\mathrm{Ide}\to\mathrm{Val}$, con $\mathrm{Val}=\mathbb Z\cup\mathrm{Bool}$.

---

## 1. Espressioni

Le espressioni servono a rappresentare i dati, che qui sono solo interi o booleani. Nel paradigma imperativo il calcolo procede modificando lo stato, quindi le espressioni devono poter leggere i valori dello stato tramite gli **identificatori**. La sintassi è data in modo informale con poche regole, come per il [[Calcolo proposizionale|calcolo proposizionale]] e la [[Logica del primo ordine|LPO]].

### 1.1 Sintassi

**Espressioni atomiche:**

- **costanti intere** in notazione decimale con segno: `0`, `125`, `-5`, `3`, `-29`, …;
- **costanti booleane**: `true` e `false`;
- **identificatori**: elementi di $\mathrm{Ide}$.

`true` e `false` sono nomi riservati: non si possono usare come identificatori (più avanti ne incontreremo altri).

**Espressioni composte:**

- se `E` è un'espressione, lo sono anche `(E)` e `not E`;
- se `E`, `E'` sono espressioni, lo è `E op E'` con $\mathtt{op}\in\{+,-,*,\mathtt{div},\mathtt{mod}\}$;
- se `E`, `E'` sono espressioni, lo è `E bop E'` con $\mathtt{bop}\in\{=,\neq,>,>=,<,<=,\mathtt{or},\mathtt{and}\}$.

Si indica con $\mathrm{Exp}$ l'insieme delle espressioni e con $\mathrm{Const}=\mathrm{Num}\cup\mathrm{Bool}$ il sottoinsieme delle costanti intere ($\mathrm{Num}$) e booleane ($\mathrm{Bool}$).

**Precedenza degli operatori.** Le regole permettono di scrivere espressioni ambigue come `8+5*3`. Si assumono le precedenze usuali tra operatori numerici (quelle tra operatori logici le conosciamo già); in ogni caso le parentesi tolgono ogni dubbio: `(8+5)*3` contro `8+(5*3)`.

### 1.2 Semantica statica: il controllo dei tipi

L'espressione `(x + 5) and (x > y)` è sintatticamente corretta, ma non ha senso: `and` vuole due argomenti booleani, mentre `x + 5` è un intero. Serve quindi un controllo in più, il **controllo dei tipi** (*type checking*), che verifica che ogni operatore sia usato con argomenti del tipo giusto. Si parla di **semantica statica** perché basta guardare la struttura sintattica, senza calcolare alcun valore.

D'ora in avanti le espressioni si assumono sempre **staticamente corrette**. Occhio però: anche un'espressione staticamente corretta può dare errore quando viene valutata (per esempio una divisione per zero).

### 1.3 Semantica delle espressioni

Si definisce la **funzione di interpretazione semantica**

$$
\mathcal E:\mathrm{Exp}\times\mathrm{State}\to\mathrm{Val},
$$

che, data un'espressione e uno stato, restituisce il valore dell'espressione in quello stato. Per convenzione $\mathbf n$ indica l'intero corrispondente alla costante sintattica $\mathtt n\in\mathrm{Num}$, e $\mathbf{op}$ (risp. $\mathbf{bop}$) la funzione che interpreta il simbolo $\mathtt{op}$ (risp. $\mathtt{bop}$): per esempio a `+` corrisponde la somma $+:\mathbb Z\times\mathbb Z\to\mathbb Z$, ad `and` la congiunzione $\land:\mathrm{Bool}\times\mathrm{Bool}\to\mathrm{Bool}$.

$$
\begin{aligned}
\mathcal E(\mathtt{true},\sigma)&=\mathbf t\\
\mathcal E(\mathtt{false},\sigma)&=\mathbf f\\
\mathcal E(\mathtt n,\sigma)&=\mathbf n &&\mathtt n\in\mathrm{Num}\\
\mathcal E(\mathtt x,\sigma)&=\sigma(\mathtt x) &&\mathtt x\in\mathrm{Ide}\\
\mathcal E((\mathtt E),\sigma)&=\mathcal E(\mathtt E,\sigma)\\
\mathcal E(\mathtt{not}\ \mathtt E,\sigma)&=\neg\,\mathcal E(\mathtt E,\sigma)\\
\mathcal E(\mathtt E\ \mathtt{op}\ \mathtt E',\sigma)&=\mathcal E(\mathtt E,\sigma)\ \mathbf{op}\ \mathcal E(\mathtt E',\sigma) &&\mathtt{op}\in\{+,-,*,\mathtt{div},\mathtt{mod}\}\\
\mathcal E(\mathtt E\ \mathtt{bop}\ \mathtt E',\sigma)&=\mathcal E(\mathtt E,\sigma)\ \mathbf{bop}\ \mathcal E(\mathtt E',\sigma) &&\mathtt{bop}\in\{=,\neq,<,>,<=,>=,\mathtt{and},\mathtt{or}\}
\end{aligned}
$$

**Osservazioni.**

- Poiché le espressioni sono staticamente corrette, in una clausola come $\mathcal E(\mathtt E+\mathtt E',\sigma)=\mathcal E(\mathtt E,\sigma)+\mathcal E(\mathtt E',\sigma)$ non serve precisare che i due valori stanno in $\mathbb Z$.
- Anche ristretta alle espressioni staticamente corrette, $\mathcal E$ è una **funzione parziale**. Per esempio:

$$
\begin{aligned}
&\mathcal E(\mathtt{x\ div\ 0},\sigma)\\
=\;&\{\text{definizione di }\mathcal E\}\quad \mathcal E(\mathtt x,\sigma)\ \mathbf{div}\ \mathcal E(\mathtt 0,\sigma)\\
=\;&\{\text{definizione di }\mathcal E\}\quad \sigma(\mathtt x)\ \mathbf{div}\ 0\\
=\;&\{\perp\text{ valore indefinito}\}\quad \perp
\end{aligned}
$$

---

## 2. Comandi

Le espressioni calcolano valori che dipendono dallo stato; i **comandi** invece **modificano lo stato** quando vengono eseguiti. L'insieme dei comandi si indica con $\mathrm{Com}$.

### 2.1 Sintassi

| Comando | Sintassi | Condizione |
|---|---|---|
| vuoto | `skip` | |
| assegnamento | `x := E` | $\mathtt x\in\mathrm{Ide}$, $\mathtt E\in\mathrm{Exp}$ |
| sequenza | `C ; C'` | `C`, `C'` comandi |
| condizionale | `if E then C else C' fi` | `E` espressione booleana, `C`, `C'` comandi |
| iterativo | `while E do C endw` | `E` espressione booleana, `C` comando |

Nel condizionale `E` è la **guardia**, `C` il **ramo then** e `C'` il **ramo else**. Nel [[Comando iterativo|comando iterativo]] `E` è la **guardia** e `C` il **corpo**.

### 2.2 Semantica informale (operazionale)

Il significato di un comando `C` si descrive dicendo in quale stato finale $\sigma'$ ci porta la sua esecuzione partendo da uno stato iniziale $\sigma$.

- **`skip`**: da $\sigma$ si resta in $\sigma$.
- **`x := E`**: da $\sigma$ si passa a $\sigma'=\sigma[v/\mathtt x]$ con $v=\mathcal E(\mathtt E,\sigma)$. Lo stato è definito solo se è definito $\mathcal E(\mathtt E,\sigma)$.
- **`C ; C'`**: si esegue `C` a partire da $\sigma$, ottenendo $\sigma''$; poi si esegue `C'` a partire da $\sigma''$, ottenendo $\sigma'$.
- **`if E then C else C' fi`**: si esegue `C` a partire da $\sigma$ se $\mathcal E(\mathtt E,\sigma)=\mathbf t$, oppure `C'` a partire da $\sigma$ se $\mathcal E(\mathtt E,\sigma)=\mathbf f$.
- **`while E do C endw`**: se $\mathcal E(\mathtt E,\sigma)=\mathbf f$ si resta in $\sigma$; se $\mathcal E(\mathtt E,\sigma)=\mathbf t$ si esegue `C` ottenendo $\sigma''$ e poi si esegue di nuovo l'intero `while` a partire da $\sigma''$.

**Esempio (assegnamento e sequenza).** Sia $\sigma=\{\mathtt x\mapsto10,\mathtt y\mapsto0\}$.

1. `x := y` porta da $\sigma$ in $\sigma_1=\{\mathtt x\mapsto0,\mathtt y\mapsto0\}$.
2. `x := x + 1` porta da $\sigma_1$ in $\sigma'=\{\mathtt x\mapsto1,\mathtt y\mapsto0\}$.
3. Quindi la sequenza `x := y ; x := x + 1`, da $\sigma$, porta in $\sigma'=\{\mathtt x\mapsto1,\mathtt y\mapsto0\}$.

**Esempio (condizionale).** Il comando `if x>0 then skip else x := -x fi`:

- da $\sigma=\{\mathtt x\mapsto25\}$ lascia lo stato invariato, perché $\mathcal E(\mathtt{x>0},\sigma)=\mathbf t$;
- da $\sigma'=\{\mathtt x\mapsto-25\}$ porta in $\sigma''=\sigma'[25/\mathtt x]$, perché la guardia è falsa e si esegue `x := -x`.

### 2.3 Il comando iterativo come sequenza di esecuzioni del corpo

Detto a parole, eseguire `while E do C endw` vuol dire eseguire una sequenza, eventualmente vuota o infinita,

$$
C_1;\ C_2;\ C_3;\ \dots;\ C_k;\ \dots
$$

in cui ogni $C_i$ coincide con il corpo `C`. Sia $\sigma_0=\sigma$ lo stato iniziale e $\sigma_i$ lo stato ottenuto eseguendo $C_i$ a partire da $\sigma_{i-1}$. Per semplicità supponiamo che il corpo non contenga altri comandi iterativi. Ci sono due possibilità:

- **(a) la sequenza è finita**, del tipo $C_1;\dots;C_n$ con $n\geq0$, e lo stato finale è $\sigma_n$, dove
  $$
  n=\min\{i\geq0\mid\mathcal E(\mathtt E,\sigma_i)=\mathbf f\}.
  $$
  In particolare $n=0$ (il corpo non viene mai eseguito) quando la guardia è falsa già in $\sigma_0=\sigma$;
- **(b) la sequenza è infinita**, e $\mathcal E(\mathtt E,\sigma_i)=\mathbf t$ per ogni $i\geq0$.

**Esempi.**

- `while x>=y do x := x - 1 endw` **termina** sempre.
- `while x>=y do x := x + 1 endw` **potrebbe non terminare**.

*Verifica (mia):* nel primo, ogni iterazione diminuisce `x` di $1$ mentre `y` resta fissa, quindi prima o poi `x < y`. Nel secondo, se inizialmente `x < y` il ciclo termina subito (zero iterazioni); se invece `x >= y`, la guardia resta vera per sempre perché `x` cresce.

### 2.4 Semantica formale dei comandi

La semantica dei comandi è data dalla funzione di interpretazione

$$
\mathcal C:\mathrm{Com}\times\mathrm{State}\to\mathrm{State}.
$$

Si ricorda che $\sigma[v/\mathtt x]$ è lo stato $\sigma'$ tale che

$$
\sigma'(\mathtt y)=
\begin{cases}
v&\text{se }\mathtt y=\mathtt x,\\
\sigma(\mathtt y)&\text{altrimenti.}
\end{cases}
$$

**Riepilogo delle clausole:**

$$
\begin{aligned}
\mathcal C(\mathtt{skip},\sigma)&=\sigma\\[2pt]
\mathcal C(\mathtt{x:=E},\sigma)&=\sigma[\mathcal E(\mathtt E,\sigma)/\mathtt x]\\[2pt]
\mathcal C(\mathtt{C;C'},\sigma)&=\mathcal C(\mathtt C',\mathcal C(\mathtt C,\sigma))\\[2pt]
\mathcal C(\mathtt{if\ E\ then\ C\ else\ C'\ fi},\sigma)&=
\begin{cases}
\mathcal C(\mathtt C,\sigma)&\text{se }\mathcal E(\mathtt E,\sigma)=\mathbf t\\
\mathcal C(\mathtt C',\sigma)&\text{se }\mathcal E(\mathtt E,\sigma)=\mathbf f
\end{cases}\\[2pt]
\mathcal C(\mathtt{while\ E\ do\ C\ endw},\sigma)&=
\begin{cases}
\sigma&\text{se }\mathcal E(\mathtt E,\sigma)=\mathbf f\\
\mathcal C(\mathtt{while\ E\ do\ C\ endw},\mathcal C(\mathtt C,\sigma))&\text{se }\mathcal E(\mathtt E,\sigma)=\mathbf t
\end{cases}
\end{aligned}
$$

Nella sequenza si può anche scrivere $\mathcal C(\mathtt{C;C'},\sigma)=\mathcal C(\mathtt C',\sigma')$ con $\sigma'=\mathcal C(\mathtt C,\sigma)$. La clausola del `while` è **ricorsiva**: definisce il comando in termini di sé stesso.

Anche $\mathcal C$ è una **funzione parziale**: basta pensare a un'iterazione che non termina, o a un semplice assegnamento come `x := y div 0`. Quando lo si vuole esplicitare si scrive $\mathcal C(\mathtt C,\sigma)=\perp$.

**Esempio (condizionale).** Sia $\sigma=\{\mathtt n\mapsto A,\mathtt r\mapsto0\}$ con $A$ costante intera.

$$
\begin{aligned}
&\mathcal C(\mathtt{if\ n>0\ then\ r:=n\ else\ r:=-n\ fi},\sigma)\\
=\;&\{\text{Ip: }A>0,\text{ dunque }\mathcal E(\mathtt{n>0},\sigma)=\mathbf t\}\quad\mathcal C(\mathtt{r:=n},\sigma)\\
=\;&\{\mathcal E(\mathtt n,\sigma)=\sigma(\mathtt n)=A\}\quad\sigma[A/\mathtt r]
\end{aligned}
$$

Se invece $A\leq0$, la guardia è falsa, si esegue `r := -n` e, poiché $\mathcal E(\mathtt{-n},\sigma)=-A$, si ottiene $\sigma[-A/\mathtt r]$.

**Esempio (sequenza).** Sia $\sigma=\{\mathtt x\mapsto A,\mathtt y\mapsto B\}$.

$$
\begin{aligned}
&\mathcal C(\mathtt{x:=y;\ y:=x},\sigma)\\
=\;&\{\text{definizione di }\mathcal C,\text{ sequenza}\}\quad\mathcal C(\mathtt{y:=x},\mathcal C(\mathtt{x:=y},\sigma))\\
=\;&\{\mathcal E(\mathtt y,\sigma)=\sigma(\mathtt y)=B;\ \sigma'=\sigma[B/\mathtt x]\}\quad\mathcal C(\mathtt{y:=x},\sigma')\\
=\;&\{\mathcal E(\mathtt x,\sigma')=\sigma'(\mathtt x)=B;\ \sigma''=\sigma'[B/\mathtt y]\}\quad\sigma''
\end{aligned}
$$

Lo stato finale è $\sigma''=\{\mathtt x\mapsto B,\mathtt y\mapsto B\}$: **il valore originale di `x` è perso**.

---

## 3. Primi algoritmi

Ogni esempio ha la sua specifica (stato iniziale → stato finale) e un algoritmo che la realizza.

### 3.1 Valore assoluto

Specifica: $\{\mathtt{numero}\mapsto A\}\ \longrightarrow\ \{\mathtt{risultato}\mapsto|A|\}$.

```
if (numero > 0)
    then risultato := numero
    else risultato := -numero
fi
```

### 3.2 Scambio dei valori di due variabili

Specifica: $\{\mathtt x\mapsto A,\mathtt y\mapsto B\}\ \longrightarrow\ \{\mathtt x\mapsto B,\mathtt y\mapsto A\}$.

Come abbiamo visto sopra, `x := y; y := x` **non** fa in generale quello che vogliamo. Serve un identificatore ausiliario:

```
temp := x;
x := y;
y := temp
```

| Comando | Stato dopo il comando (da $\{\mathtt x\mapsto10,\mathtt y\mapsto20\}$) |
|---|---|
| `x := y; y := x` | `x := y` → $\{\mathtt x\mapsto20,\mathtt y\mapsto20\}$; `y := x` → $\{\mathtt x\mapsto20,\mathtt y\mapsto20\}$ |
| `temp := x; x := y; y := temp` | $\{\mathtt{temp}\mapsto10,\mathtt x\mapsto10,\mathtt y\mapsto20\}$ → $\{\mathtt{temp}\mapsto10,\mathtt x\mapsto20,\mathtt y\mapsto20\}$ → $\{\mathtt{temp}\mapsto10,\mathtt x\mapsto20,\mathtt y\mapsto10\}$ |

La variabile `temp` è indispensabile per due motivi: l'assegnamento è **distruttivo** (il vecchio valore viene sovrascritto) e l'esecuzione è **sequenziale**.

### 3.3 Ordinare due interi positivi

Specifica: $\{\mathtt{num1}\mapsto A,\mathtt{num2}\mapsto B\}\ \longrightarrow\ \{\mathtt{num1}\mapsto\max(A,B),\mathtt{num2}\mapsto\min(A,B)\}$.

```
if (num1 < num2)
then
    temp := num1;
    num1 := num2;
    num2 := temp
else
    skip
fi
```

### 3.4 Elevamento a potenza

Specifica: $\{\mathtt{base}\mapsto A,\mathtt{esponente}\mapsto B\}$ con $A>0$ e $B\geq0$ $\longrightarrow$ $\{\mathtt{risultato}\mapsto A^B\}$.

L'algoritmo segue la definizione

$$
A^0=1,\qquad A^B=\underbrace{A\cdot A\cdots A}_{B\text{ volte}}\quad(B>0).
$$

```
risultato := 1;
while esponente > 0
do
    risultato := risultato * base;
    esponente := esponente - 1
endw
```

Si suppone che i valori iniziali di `base` ed `esponente` rispettino i requisiti della specifica.

---

## 4. Semantica assiomatica: le triple di Hoare

Nell'approccio **assiomatico** il significato dei costrutti è dato da un sistema di [[Regola di inferenza|regole]] con cui si **derivano proprietà** dei comandi e dei programmi.

### 4.1 Un programma annotato

Sia `Abs` l'algoritmo del valore assoluto (§3.1). Il suo significato si può descrivere con

$$
\{\mathtt{numero}\mapsto A\}\ \mathtt{Abs}\ \{\mathtt{risultato}\mapsto|A|\},
$$

da leggere così: «partendo da un qualunque stato $\sigma$ in cui a `numero` è associato il valore $\sigma(\mathtt{numero})$, l'esecuzione di `Abs` termina in uno stato in cui a `risultato` è associato $|\sigma(\mathtt{numero})|$». Qui le annotazioni coincidono in pratica con la specifica: descrivono il comportamento atteso.

### 4.2 Definizione

Una **tripla di Hoare** ha la forma

$$
\{Q\}\ C\ \{R\},
$$

dove $C$ è un comando e $Q$, $R$ sono **asserzioni**, cioè formule della LPO in cui possono comparire variabili dello stato. Dati i tipi del linguaggio, il dominio di interpretazione delle asserzioni comprende $\mathbb Z$, $\mathrm{Bool}$ e i sottoinsiemi di $\mathbb Z$.

- $Q$ è la [[Precondizione e postcondizione|precondizione]], $R$ la **postcondizione**.
- La tripla è **soddisfatta** se, per ogni stato $\sigma$ che soddisfa $Q$ ($\sigma\models Q$), l'esecuzione di $C$ a partire da $\sigma$ **termina** producendo uno stato $\sigma'$, e $\sigma'\models R$.

«Termina» significa **termina con successo** (senza errori). Esempio: $\{x>1\}\ \mathtt{x:=x+1}\ \{x>2\}$.

### 4.3 Tre modi di usare una tripla

1. **Semantica.** Dati $Q$ e $C$, trovare $R$ tale che $\{Q\}\,C\,\{R\}$ sia soddisfatta descrive il comportamento di $C$. Per esempio con
   `C = if (x < 10) then x := 1 else x := 2 fi`
   e $Q=(x>10)$, la postcondizione $R=(x=2)$ descrive il comportamento del comando.
2. **Specifica.** Dati $Q$ e $R$, trovare $C$ che soddisfi la tripla significa scrivere un programma che realizza la specifica. Con $Q=(x>0)$ e $R=(y=2\cdot x)$ vanno bene `y := x * 2`, `y := x + x`, `y := x; y := y * 2`, ma anche `y := 10; x := 5` (!!!).
   *Commento (mio):* l'ultimo comando soddisfa davvero la tripla, perché nello stato finale $y=10=2\cdot5=2x$. È il problema già visto con le specifiche troppo deboli: senza variabili di specifica non si impone che $x$ resti quello iniziale.
3. **Correttezza.** Dati $C$, $Q$ e $R$, dimostrare che $\{Q\}\,C\,\{R\}$ è soddisfatta equivale a una [[Correttezza totale|dimostrazione di correttezza]] di $C$ rispetto a $Q$ e $R$. Per esempio la divisione intera

   ```
   q := 0; r := x;
   while r ≥ y
   do
       q := q + 1;
       r := r - y
   endw
   ```

   soddisfa la tripla con $Q:\ x\geq0\land y>0$ e $R:\ x=y\cdot q+r\land0\leq r<y$.

### 4.4 Verifiche di correttezza

In questa parte del corso le triple si usano nel terzo senso, per verificare la correttezza dei programmi. L'obiettivo è **verificare una tripla**, cioè dimostrare che è soddisfatta, proprio come si dimostrava che una proposizione è una [[Tautologia|tautologia]] nel CP o che una formula è valida nella LPO. A questo scopo si introduce un **proof system** (assiomi e regole di inferenza) **corretto** per le triple, che sfrutterà anche tutte le leggi del calcolo proposizionale e dei predicati.

### 4.5 Notazioni

- $\mathrm{free}(P)$ è l'insieme delle [[Variabile libera e legata|variabili libere]] di un'asserzione $P$; per esempio $\mathrm{free}(x>y\land z\leq1)=\{x,y,z\}$.
- $P^\sigma$ è l'asserzione $P$ **istanziata** sullo stato $\sigma$, cioè con ogni variabile sostituita dal suo valore in $\sigma$. Poiché l'interpretazione del linguaggio delle asserzioni è fissata, $P^\sigma$ ha un valore di verità determinato. Esempio: con $\sigma=\{x\mapsto18,y\mapsto\mathrm{true},z\mapsto-8\}$ e $P=(x>0\land z<0)$,
  $$
  P^\sigma=(18>0\land-8<0)\equiv T.
  $$
- $\sigma\models P$ (lo stato **soddisfa** l'asserzione) se e solo se $P^\sigma\equiv T$.
- $\{P\}$ indica anche l'**insieme degli stati** che soddisfano $P$: $\{P\}=\{\sigma\mid\sigma\models P\}$.

### 4.6 Proprietà utili

Siano $E$ un'espressione, $P$ un'asserzione e $\sigma,\sigma'$ due stati.

- **(P1)** Se $\sigma(x)=\sigma'(x)$ per ogni $x\in\mathrm{free}(E)$, allora $\mathcal E(E,\sigma)=\mathcal E(E,\sigma')$.
- **(P2)** Se $\sigma(x)=\sigma'(x)$ per ogni $x\in\mathrm{free}(P)$, allora $\sigma\models P$ se e solo se $\sigma'\models P$.
- **(P3)** Per ogni variabile $x$:
  $$
  \sigma[\mathcal E(E,\sigma)/x]\models P\quad\text{se e solo se}\quad\sigma\models P[E/x].
  $$

In parole: (P1) e (P2) dicono che il valore di un'espressione e la verità di un'asserzione dipendono solo dalle loro variabili libere. (P3) dice che assegnare a $x$ il valore di $E$ e poi valutare $P$ equivale a valutare, nello stato di partenza, $P$ con $E$ al posto di $x$. È la base dell'[[Regola dell'assegnamento|assioma dell'assegnamento]], visto nella [[2026-10-20 - Regole di inferenza per le triple di Hoare e invarianti|lezione successiva]] insieme ad alcuni esempi di (P3).

> [!example] Esempio
> Sia $\sigma=\{x\mapsto3\}$, $E=x+1$ e $P=(x>3)$. Lo stato $\sigma[\mathcal E(E,\sigma)/x]=\{x\mapsto4\}$ soddisfa $P$, e infatti anche $\sigma\models P[E/x]=(x+1>3)$, perché $3+1>3$.

## Fonte

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 9, 19 ottobre 2026, slide 260-297 (file `Lezione_09.pdf`).
- Il testo delle slide è stato estratto automaticamente e i simboli rovinati sono stati ricostruiti dal contesto. Le parti segnate «mia» o «mio» non compaiono nelle slide.
