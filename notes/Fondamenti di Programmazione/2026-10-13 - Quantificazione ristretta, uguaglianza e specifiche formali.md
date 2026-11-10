---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-10-13'
title: Quantificazione ristretta, uguaglianza e specifiche formali
source: Lezione_08.pdf (slide 236-259)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-10-13 - Quantificazione ristretta, uguaglianza e specifiche formali.md
vault_hash: 054a0592b24ccd87763ff4a6e225b53fda406b71e5ad8a3898b7ad69537cb5f7
---

La lezione chiude la parte sulla [[Logica del primo ordine|logica del primo ordine]] (LPO) iniziata nelle lezioni del [[2026-10-08 - Sintassi e semantica della logica del primo ordine|8 ottobre]] e del [[2026-10-12 - Semantica della logica del primo ordine|12 ottobre]]: prima la **quantificazione ristretta** a un dominio, poi l'**uguaglianza**, poi due regole di inferenza per i quantificatori (**generalizzazione** e **skolemizzazione**). Dalla slide 249 inizia la seconda parte del corso, i **principi di programmazione imperativa**: linguaggi, semantica formale, stati e **specifiche** di problemi come coppie di asserzioni.

---

## 1. Quantificazione ristretta a un insieme

Spesso la quantificazione è ristretta agli elementi che soddisfano una formula $P$:

$$
(\forall x.\, P \Rightarrow Q) \qquad (\exists x.\, P \land Q)
$$

In queste formule $P$ è chiamata il **dominio** del [[Quantificatore|quantificatore]]. Per esplicitarlo si introducono due abbreviazioni ([[Quantificazione ristretta|quantificazione ristretta]]):

$$
(\forall x : P.\, Q) \;\text{ abbrevia }\; (\forall x.\, P \Rightarrow Q)
\qquad
(\exists x : P.\, Q) \;\text{ abbrevia }\; (\exists x.\, P \land Q)
$$

**Esempi:**

$$
(\forall x : \operatorname{studenteFPL}(x).\; \operatorname{vaAlCinema}(x) \lor \operatorname{vaAlTeatro}(x))
$$
$$
(\exists x : \operatorname{studenteFPL}(x).\; \operatorname{vaAlCinema}(x))
$$

Nota bene: con $\forall$ il dominio si lega con $\Rightarrow$, con $\exists$ con $\land$ (stessa scelta fatta nelle formalizzazioni delle lezioni precedenti).

### 1.1 Formule vacuamente vere o false

Sia $P$ una formula con $x$ libera e $\mathcal{I} = (D, \alpha)$ un'[[Interpretazione|interpretazione]]. Il dominio $P$ è **vuoto in $\mathcal{I}$** se $\mathcal{I}_\rho(\exists x.\, P) = \mathrm{f}$ o, equivalentemente, se per ogni $d \in D$ vale $\mathcal{I}_{\rho[d/x]}(P) = \mathrm{f}$ (nessun elemento di $D$ soddisfa $P$).

Allora:

1. $(\forall x : P.\, Q)$ è **vacuamente vera** in $\mathcal{I}$ se il dominio $P$ è vuoto in $\mathcal{I}$;
2. dualmente, $(\exists x : P.\, Q)$ è **vacuamente falsa** in $\mathcal{I}$ se il dominio $P$ è vuoto in $\mathcal{I}$.

**Dimostrazione di (1).** Si mostra che, se $P$ è vuoto in $\mathcal{I}$, allora $\mathcal{I}_\rho(\forall x.\, P \Rightarrow Q) = \mathrm{t}$ indipendentemente da $Q$:

$$
\begin{aligned}
&\mathcal{I}_\rho(\forall x.\, P \Rightarrow Q) = \mathrm{t}\\
\iff\;& \{\text{Elim-}\Rightarrow\}\quad \mathcal{I}_\rho(\forall x.\, \neg P \lor Q) = \mathrm{t}\\
\iff\;& \{\text{(S5), semantica di } \forall\}\quad \text{per ogni } d \in D,\; \mathcal{I}_{\rho[d/x]}(\neg P \lor Q) = \mathrm{t}\\
\iff\;& \{\text{(S4), semantica di } \lor\}\quad \text{per ogni } d \in D,\; \mathcal{I}_{\rho[d/x]}(\neg P) = \mathrm{t} \text{ oppure } \mathcal{I}_{\rho[d/x]}(Q) = \mathrm{t}\\
\iff\;& \{\text{(S3), semantica di } \neg\}\quad \text{per ogni } d \in D,\; \mathcal{I}_{\rho[d/x]}(P) = \mathrm{f} \text{ oppure } \mathcal{I}_{\rho[d/x]}(Q) = \mathrm{t}\\
\iff\;& \{\text{ipotesi: } P \text{ vuoto}\}\quad \mathrm{t}
\end{aligned}
$$

Nell'ultimo passo, per ogni $d$ il primo disgiunto è già vero, quindi $Q$ non conta. Il caso (2) è il duale (non svolto nelle slide): $\exists x.\, P \land Q$ richiede un $d$ che soddisfi $P$, e non ce n'è nessuno.

Una conseguenza pratica: «tutti gli studenti di FPL con tre teste vanno al cinema» è vera se nessuno studente ha tre teste, e lo stesso vale per qualunque cosa si affermi su di loro.

### 1.2 Leggi per quantificatori con dominio

**Unione di domini:**

$$
(\forall x : P \lor Q.\, R) \equiv (\forall x : P.\, R) \land (\forall x : Q.\, R)
\qquad
(\exists x : P \lor Q.\, R) \equiv (\exists x : P.\, R) \lor (\exists x : Q.\, R)
\qquad (\text{Dominio})
$$

Molte leggi dei quantificatori valgono anche con un dominio esplicito $R$, per esempio

$$
(\forall x : R.\, P \land Q) \equiv (\forall x : R.\, P) \land (\forall x : R.\, Q) \quad (\forall{:}\land)
\qquad
\neg(\exists x : R.\, P) \equiv (\forall x : R.\, \neg P) \quad (\text{De Morgan})
$$

Le slide chiedono di dimostrarle come esercizio, riconducendole alle leggi analoghe senza dominio.

---

## 2. Logica del primo ordine con uguaglianza

Molte formule coinvolgono il predicato binario di uguaglianza «$=$», con il significato atteso. Si considerano quindi linguaggi in cui $= \in \mathcal{P}$ e in cui, in ogni interpretazione, $t_1 = t_2$ è vera se e solo se $t_1$ e $t_2$ denotano lo stesso elemento del dominio. Formalmente, data $\mathcal{I} = (D, \alpha)$ e un assegnamento $\rho$:

$$
\mathcal{I}_\rho(t_1 = t_2) =
\begin{cases}
\mathrm{t} & \text{se } \alpha_\rho(t_1) = \alpha_\rho(t_2),\\
\mathrm{f} & \text{altrimenti.}
\end{cases}
$$

### 2.1 Legge di Leibniz

La [[Legge di Leibniz|legge di Leibniz]] dice:

$$
x = y \Rightarrow (P \equiv P[y/x]) \quad (\text{Leibniz})
$$

Se $x$ e $y$ sono identici, asserire $P(x)$ è la stessa cosa che asserire $P(y)$. Da questa legge ne segue un'altra utile:

$$
\begin{aligned}
&x = y \Rightarrow (P \equiv P[y/x])\\
\equiv\;& \{\text{Elim-}\equiv\}\quad x = y \Rightarrow (P \Rightarrow P[y/x]) \land (P[y/x] \Rightarrow P)\\
\Rightarrow\;& \{\text{Sempl-}\land\}\quad x = y \Rightarrow (P \Rightarrow P[y/x])\\
\equiv\;& \{\text{Sempl. sinistra-}\equiv\}\quad x = y \land P \Rightarrow P[y/x]
\end{aligned}
$$

(l'ultimo passo è la legge del CP che porta a sinistra della freccia la premessa, $A \Rightarrow (B \Rightarrow C) \equiv A \land B \Rightarrow C$; la spiegazione del nome è mia).

La legge di Leibniz è equivalente a $x = y \land P \equiv x = y \land P[y/x]$, che discende dalla [[Tautologia|tautologia]] del CP
$$
(P \Rightarrow (Q \equiv R)) \equiv (P \land Q \equiv P \land R),
$$
da dimostrare per esercizio. Riassumendo, omettendo i $\forall x,y$ per leggibilità, le forme equivalenti di (Leibniz) sono:

$$
x = y \Rightarrow (P \equiv P[y/x]) \qquad
x = y \land P \equiv x = y \land P[y/x] \qquad
(x = y \land P) \Rightarrow P[y/x]
$$

### 2.2 Leggi del singoletto

$$
(\forall x.\; (x = y) \Rightarrow P) \equiv P[y/x]
\qquad
(\exists x.\; (x = y) \land P) \equiv P[y/x]
\qquad (\text{Singoletto})
$$

L'idea: $x = y$ restringe il dominio a un solo elemento, quello denotato da $y$; quindi quantificare su $x$ equivale a sostituire $y$ al posto di $x$.

> [!example] Esempio
> Con $y = 3$ e $P = \operatorname{pari}(x)$: $(\exists x.\; x = 3 \land \operatorname{pari}(x)) \equiv \operatorname{pari}(3)$, e $(\forall x.\; x = 3 \Rightarrow \operatorname{pari}(x)) \equiv \operatorname{pari}(3)$. Il quantificatore sparisce e resta solo l'unico caso possibile.

**Dimostrazione della seconda** (dalle slide):

$$
\begin{aligned}
&(\exists x.\; x = y \land P)\\
\equiv\;& \{\text{Leibniz}\}\quad (\exists x.\; x = y \land P[y/x])\\
\equiv\;& \{\text{Distr.} (*)\}\quad (\exists x.\; x = y) \land P[y/x]\\
\equiv\;& \{(\exists x.\; x = y) \equiv \mathrm{T},\; \text{Unità}\}\quad P[y/x]
\end{aligned}
$$

Le slide chiedono: perché è corretto il passo $(*)$? *Risposta (mia):* la legge (Distrib.) richiede che $x$ non occorra nel congiunto che esce dal quantificatore, cioè in $P[y/x]$, ed è così perché la sostituzione ha tolto tutte le occorrenze libere di $x$ (assumendo $y$ diversa da $x$); inoltre richiede il dominio non vuoto, ipotesi standing nelle leggi dei quantificatori.

Nell'ultimo passo si usa $(\exists x.\; x = y) \equiv \mathrm{T}$, da dimostrare per esercizio. La prima legge (Singoletto) si ottiene dalla seconda con De Morgan (anch'essa lasciata per esercizio).

---

## 3. Regole di inferenza per i quantificatori

### 3.1 Generalizzazione

Per dimostrare $(\forall x.\, P)$ si può sostituire $x$ con un **nuovo** simbolo di costante $d$ e dimostrare $P[d/x]$:

$$
\frac{\Gamma \vdash P[d/x] \quad d \text{ nuova costante}}{\Gamma \vdash (\forall x.\, P)}
$$

Intuitivamente $d$ rappresenta un elemento *generico* del dominio, sul quale non si può fare alcuna assunzione (per questo deve essere nuova: non può comparire in $\Gamma$ né in $P$).

**Esempio.** Siano $P$ e $Q$ formule con $x$ libera e $\Gamma = \{(\forall x.\, P \Rightarrow Q),\; (\forall x.\, P)\}$. Si vuole $\Gamma \vdash (\forall x.\, Q)$, sia $d$ una costante nuova:

$$
\begin{aligned}
&(\forall x.\, P \Rightarrow Q) \land (\forall x.\, P)\\
\Rightarrow\;& \{\text{Elim-}\forall,\; d \text{ nuova}\}\quad (P[d/x] \Rightarrow Q[d/x]) \land P[d/x]\\
\Rightarrow\;& \{\text{modus ponens}\}\quad Q[d/x]
\end{aligned}
$$

Per generalizzazione si conclude $(\forall x.\, Q)$.

### 3.2 Skolemizzazione

La [[Skolemizzazione|skolemizzazione]] funziona così: se $(\exists x.\, P)$ è tra le premesse, per dimostrare una qualunque formula $Q$ si può aggiungere come ipotesi $P[d/x]$, con $d$ **nuova** costante:

$$
\frac{(\exists x.\, P) \in \Gamma \quad \Gamma, P[d/x] \vdash Q \quad d \text{ nuova costante}}{\Gamma \vdash Q}
$$

Intuitivamente: sapere $(\exists x.\, P)$ significa che esiste un elemento del dominio per cui $P$ vale; non sapendo quale sia, lo si chiama $d$. La costante $d$ è un **testimone** della verità di $(\exists x.\, P)$ senza riferirsi a un individuo specifico.

**Esempio.** Dimostrare $(\forall x.\, P \Rightarrow Q) \land (\exists x.\, P) \Rightarrow (\exists x.\, Q)$. Sia $d$ una costante nuova:

$$
\begin{aligned}
&(\forall x.\, P \Rightarrow Q) \land (\exists x.\, P)\\
\Rightarrow\;& \{\text{Skolemizzazione: si aggiunge } P[d/x] \text{ alle premesse}\}\quad (\forall x.\, P \Rightarrow Q) \land (\exists x.\, P) \land P[d/x]\\
\Rightarrow\;& \{\text{Elim-}\forall,\; \text{Sempl-}\land\}\quad (P[d/x] \Rightarrow Q[d/x]) \land P[d/x]\\
\Rightarrow\;& \{\text{Modus ponens},\; \text{Sempl-}\land\}\quad Q[d/x]\\
\Rightarrow\;& \{\text{Intro-}\exists\}\quad (\exists x.\, Q)
\end{aligned}
$$

### 3.3 Un altro esempio: scambio di quantificatori

Mostrare la validità di
$$
(\exists y.\,(\forall x.\, P)) \Rightarrow (\forall x.\,(\exists y.\, P)).
$$
Si scrive $P(x,y)$ per evidenziare che $x$ e $y$ occorrono libere in $P$. Per generalizzazione basta dimostrare, con $d$ costante nuova e $P(d,y)$ che indica $P[d/x]$,
$$
(\exists y.\,(\forall x.\, P(x,y))) \Rightarrow (\exists y.\, P(d,y)).
$$
Infatti:
$$
(\exists y.\,(\forall x.\, P(x,y))) \Rightarrow \{\text{Elim-}\forall\}\; (\exists y.\, P(d,y)).
$$
Per generalizzazione si conclude $(\forall x.\,(\exists y.\, P(x,y)))$.

*Nota (mia):* il passo Elim-$\forall$ avviene all'interno di $\exists y$, dove $\forall x.\,P(x,y)$ occorre positivamente; è quindi coperto dalla generalizzazione del principio di sostituzione per $\Rightarrow$ vista nella lezione precedente.

---

## 4. Programmazione imperativa: semantica formale e specifiche

Da qui il corso passa dalla logica ai programmi. Le slide 249-259 ricordano il programma di massima della parte 1 (concetti introduttivi, logica per la programmazione, principi di programmazione imperativa) e introducono i linguaggi di programmazione, gli stati e le specifiche.

### 4.1 Linguaggi e semantica

Un **linguaggio di programmazione** è un linguaggio artificiale con cui si esprimono [[Algoritmo|algoritmi]] in modo che un elaboratore possa eseguirli; un programma è la traduzione di un algoritmo in un certo linguaggio. Come ogni linguaggio ne vanno descritte:

- la **sintassi**: le frasi legali, cioè la struttura di un programma e come simboli e frasi di base si compongono per ottenere un programma valido. Per i linguaggi di programmazione (a differenza di quelli naturali) la sintassi può essere descritta rigorosamente con la teoria dei linguaggi formali (grammatiche libere, già accennate per il CP); nel corso ci si accontenta di una descrizione solo parzialmente formale;
- la **semantica**: il significato delle frasi sintatticamente corrette.

In molte applicazioni non basta che un programma «funzioni» o «sembri funzionare»: bisogna dimostrarne formalmente alcune proprietà (le slide citano controllo di centrali nucleari, apparecchiature mediche, software per e-banking e carte di credito). Per farlo, la semantica del linguaggio deve essere definita in modo rigoroso. Approcci principali:

| Approccio | Idea |
|---|---|
| **operazionale** | si definiscono la struttura degli stati e le transizioni di stato |
| **denotazionale** | domini semantici e funzioni di interpretazione per i costrutti del linguaggio |
| **assiomatico** | si annota il programma con asserzioni (formule) che ne descrivono le proprietà, e se ne dimostra la correttezza con regole di inferenza |

Nel corso si adotta il paradigma **imperativo**, in cui un programma è una sequenza di istruzioni (comandi) che agiscono su uno **stato**. Si vedrà brevemente una semantica denotazionale e, più estesamente, la semantica assiomatica di Hoare (1969) e Dijkstra (1976). Si considera un frammento di linguaggio con i costrutti essenziali, in cui i dati sono solo interi e booleani: $\mathbb{Z}$ gli interi, $\mathrm{Bool}$ i booleani, $\mathrm{Val} = \mathbb{Z} \cup \mathrm{Bool}$. Nell'ultima parte del corso si vedrà (parte di) un linguaggio reale, il [[Linguaggio C|C]].

### 4.2 Astrazione dello stato

Uno [[Stato|stato]] è un insieme di associazioni tra nomi simbolici (**identificatori**) e valori. Detto $\mathrm{Ide}$ l'insieme degli identificatori, è una [[Funzione|funzione]] parziale

$$
\sigma : \mathrm{Ide} \to \mathrm{Val}, \qquad \sigma = \{x_1 \mapsto v_1, \dots, x_k \mapsto v_k, \dots\}.
$$

$\mathrm{State}$ indica l'insieme di tutti gli stati. È la stessa struttura dell'assegnamento $\rho$ della LPO, con gli identificatori al posto delle variabili.

### 4.3 Specifiche

La prima fase della programmazione è la [[Specifica di un problema|specifica]] del problema: dati iniziali $\Longrightarrow$ risultati finali. Qui si scrive come coppia di asserzioni:

$$
\text{(proprietà dello) stato iniziale} \;\longrightarrow\; \text{(proprietà dello) stato finale}
$$

I dati iniziali e finali sono espressi come valori degli identificatori, quindi come asserzioni. Esempio, «determinare il massimo tra due valori naturali dati»:

$$
x \ge 0 \land y \ge 0 \;\longrightarrow\; z = x \max y
$$

da leggere: «a partire da uno stato iniziale $\sigma$ che soddisfa $x \ge 0 \land y \ge 0$, si vuole un algoritmo che porti in uno stato finale $\sigma'$ che soddisfa $z = x \max y$».

Le asserzioni sono formule del calcolo dei predicati con variabili libere; lo **stato fa il ruolo dell'assegnamento**. Dati un'asserzione $P$ e uno stato $\sigma$, $\sigma$ **soddisfa** $P$, e si scrive $\sigma \models P$, se e solo se $\mathcal{I}_\sigma(P) = \mathrm{t}$, dove $\mathcal{I}$ è l'interpretazione «attesa» (per esempio quella usuale dei numeri e dei loro operatori).

### 4.4 Una specifica troppo debole e le variabili di specifica

L'«algoritmo» «modifica lo stato associando $2$, $50$ e $50$ a $x$, $y$, $z$» rispetta formalmente la specifica precedente: da $\sigma = \{x \mapsto 20, y \mapsto 3\}$ si arriva a $\sigma' = \{x \mapsto 2, y \mapsto 50, z \mapsto 50\}$ e $\sigma' \models (z = x \max y)$, perché $x \max y = \max(2, 50) = 50$. Ma non è ciò che si voleva: il valore calcolato doveva essere il massimo dei valori *dello stato iniziale*, e inoltre $x$ e $y$ sono stati cambiati.

Serve poter parlare dei valori dello stato iniziale indipendentemente dalle modifiche successive. Si introducono le **variabili di specifica** (qui $X$ e $Y$), nomi simbolici che rappresentano i valori iniziali e che, diversamente dalle **variabili di programma** (gli identificatori in $\mathrm{Ide}$), non possono essere modificate dallo stato:

$$
x = X \land y = Y \land X \ge 0 \land Y \ge 0 \;\longrightarrow\; z = X \max Y
$$

Con questa specifica l'algoritmo precedente è sbagliato: da $\sigma = \{x \mapsto 20, y \mapsto 3\}$ si ha $X = 20$ e $Y = 3$, e si dovrebbe ottenere $z = 20$, non $50$. Un algoritmo corretto: «se il valore di $x$ è minore di quello di $y$, assegna a $z$ il valore di $y$, altrimenti il valore di $x$». Lo pseudo-algoritmo non fa riferimento alle variabili di specifica.

### 4.5 Altri esempi di specifica

| Problema | Stato iniziale | Stato finale |
|---|---|---|
| Raddoppiare un naturale dato | $x = A \land A > 0$ | $x = 2 \cdot A$ |
| Valore assoluto di un intero | $x = A$ | $x = \lvert A \rvert$ |
| Quoziente e resto della divisione intera (divisore non nullo) | $x = X \land y = Y \land X \ge 0 \land Y > 0$ | $X = q \cdot Y + r \land 0 \le r < Y$ |

Nell'ultimo esempio il risultato atteso è il valore associato ai nomi $q$ e $r$ nello stato finale.

### 4.6 Convenzione «con $x$, $y$ costanti»

La specifica può essere alleggerita evitando le variabili di specifica, aggiungendo la nota «con $x$, $y$ costanti»:

$$
x \ge 0 \land y > 0 \;\longrightarrow\; x = q \cdot y + r \land 0 \le r < y \qquad (\text{con } x, y \text{ costanti})
$$
$$
x \ge 0 \land y \ge 0 \;\longrightarrow\; z = x \max y \qquad (\text{con } x, y \text{ costanti})
$$

La nota indica per convenzione che l'algoritmo deve far sì che nello stato finale i valori di $x$ e $y$ siano gli stessi dello stato iniziale. In alcuni casi le variabili di specifica sono però inevitabili (per esempio nella specifica $x = A \land A > 0 \longrightarrow x = 2 \cdot A$, dove $x$ stesso cambia).

## Fonte

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 8, 13 ottobre 2026, slide 236-259 (file `Lezione_08.pdf`).
- Il testo delle slide è stato estratto automaticamente; dove i simboli erano rovinati ho ricostruito la formula dal contesto. Le parti segnate «mia» o «risposta (mia)» sono aggiunte che non compaiono nelle slide.
