---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-10-12'
title: Semantica della logica del primo ordine
source: Lezione_07.pdf (slide 201-235)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-10-12 - Semantica della logica del primo ordine.md
vault_hash: f21889e7423d960a3b7309aee60e0e8d85ab91c85c698323eb9a853066224400
---

Nella [[2026-10-08 - Sintassi e semantica della logica del primo ordine|lezione precedente]] sono stati introdotti l'alfabeto, i termini, le formule e l'idea di [[Interpretazione|interpretazione]] $\mathcal{I} = (D, \alpha)$, rimandando la definizione formale della semantica. Questa lezione la completa: prima il valore dei **termini**, poi il valore di verità delle **formule** (con le regole per i quantificatori), poi i concetti di modello, validità e conseguenza logica, e infine i **sistemi di dimostrazione** con le leggi per i quantificatori.

Da qui in avanti si fissa un linguaggio del prim'ordine $L$ e si indicano con $\mathrm{Term}$ e $\mathrm{Fbf}$ gli insiemi dei termini e delle [[Formula ben formata|formule ben formate]] costruibili a partire da $L$. Come nel caso proposizionale, si vuole definire la funzione che dà il valore di verità di una formula in un'interpretazione:

$$
\mathcal{I} : \mathrm{Fbf} \to \mathrm{Bool}.
$$

---

## 1. Semantica dei termini

### 1.1 Termini chiusi

La semantica di un termine **chiuso** (senza variabili) nell'interpretazione $\mathcal{I} = (D, \alpha)$ è l'elemento di $D$ denotato da $\alpha(\mathit{term})$, ottenuto con due regole:

- **(R1)** se $\mathit{term}$ è la costante $c$, allora $\alpha(\mathit{term}) = \alpha(c)$;
- **(R2)** se $\mathit{term}$ è $g(t_1, \dots, t_n)$, allora $\alpha(\mathit{term}) = \alpha(g)(d_1, \dots, d_n)$, dove $d_i = \alpha(t_i)$ per $i = 1, \dots, n$.

**Esempio.** Linguaggio con $\mathcal{C} = \{a\}$, $\mathcal{F} = \{s\}$; interpretazione $D = \mathbb{N}$, $\alpha(a) = 0$, $\alpha(s)(n) = n + 1$. Allora

$$
\alpha(s(s(a))) = \alpha(s)\bigl(\alpha(s(a))\bigr) = \alpha(s)\bigl(\alpha(s)(\alpha(a))\bigr) = \alpha(s)\bigl(\alpha(s)(0)\bigr) = \alpha(s)(0+1) = (0+1)+1 = 2.
$$

Il termine $s(s(a))$ è un'espressione sintattica; il numero $2$ è l'elemento del dominio che essa denota.

### 1.2 Termini aperti e assegnamenti

Un termine può contenere variabili (per esempio $s(s(x))$). Serve dare semantica anche ai termini aperti perché, come vedremo, è ciò che permette di trattare le formule quantificate. Per farlo bisogna sapere a quali elementi del dominio si riferiscono le variabili.

> [!note] Assegnamento
> Dato un dominio $D$, un **assegnamento** è una [[Funzione|funzione]] $\rho : \mathcal{V} \to D$ che associa a ogni variabile un elemento di $D$.

Un assegnamento si scrive come insieme di coppie. Per esempio, con $\mathcal{V} = \{x, y, z\}$ e $D = \mathbb{N}$:

$$
\rho = \{x \mapsto 0,\; y \mapsto 3,\; z \mapsto 1\}.
$$

Se $\rho$ è un assegnamento, $\rho[d/x]$ è l'assegnamento che associa a $x$ il valore $d$ e sulle altre variabili si comporta come $\rho$:

$$
\rho[d/x](y) =
\begin{cases}
d & \text{se } y = x,\\
\rho(y) & \text{altrimenti.}
\end{cases}
$$

Per esempio, con $\rho$ come sopra, $\rho_1 = \rho[15/z] = \{x \mapsto 0,\; y \mapsto 3,\; z \mapsto 15\}$.

### 1.3 Semantica di un termine generico

Date un'interpretazione $\mathcal{I} = (D,\alpha)$ e un assegnamento $\rho$, la semantica di un termine qualunque, indicata con $\alpha_\rho(\mathit{term})$, estende (R1) e (R2) con una regola in più:

- **(R0)** se $\mathit{term}$ è la variabile $x \in \mathcal{V}$, allora $\alpha_\rho(\mathit{term}) = \rho(x)$;
- **(R1)** se $\mathit{term}$ è la costante $c \in \mathcal{C}$, allora $\alpha_\rho(\mathit{term}) = \alpha(c)$;
- **(R2)** se $\mathit{term}$ è $g(t_1, \dots, t_n)$ con $g \in \mathcal{F}$, allora $\alpha_\rho(\mathit{term}) = \alpha(g)(d_1, \dots, d_n)$ con $d_i = \alpha_\rho(t_i)$.

**Esempio.** Stesso linguaggio e stessa interpretazione di prima ($\mathcal{V} = \{x, y\}$, $D = \mathbb{N}$, $\alpha(s)(n) = n+1$), con $\rho = \{x \mapsto 2,\; y \mapsto 10\}$:

$$
\alpha_\rho(s(s(x))) = \alpha(s)\bigl(\alpha_\rho(s(x))\bigr) = \alpha_\rho(s(x)) + 1 = \alpha(s)(\alpha_\rho(x)) + 1 = \alpha_\rho(x) + 1 + 1 = \rho(x) + 1 + 1 = (2+1)+1 = 4.
$$

Le slide lasciano per esercizio $\alpha_\rho(s(s(y))) = 12$ (si ottiene allo stesso modo con $\rho(y) = 10$).

---

## 2. Semantica delle formule

### 2.1 Perché serve l'assegnamento

Nel CP bastava un'interpretazione per dare un valore di verità a una formula. Nella LPO non basta, per due motivi:

- ci sono **formule aperte**: come in algebra il valore di $x + y$ si stabilisce solo sapendo a quali numeri si riferiscono $x$ e $y$, così il valore di $p(x,y)$ dipende da quali individui sono $x$ e $y$, oltre che dal significato di $p$;
- ci sono **formule quantificate**.

La semantica di una formula dipende quindi da una coppia $(\mathcal{I}, \rho)$. Per semplificare la notazione si scrive

$$
\mathcal{I}_\rho(\varphi)
$$

per il valore di verità della formula $\varphi$ data l'interpretazione $\mathcal{I}$ e l'assegnamento $\rho$.

### 2.2 Le regole (S0)-(S4): come nel CP

Il valore $\mathcal{I}_\rho(\varphi)$ si definisce per ciascuna regola sintattica di costruzione di $\varphi$:

- **(S0)** $\mathcal{I}_\rho(\mathrm{T}) = \mathrm{t}$ e $\mathcal{I}_\rho(\mathrm{F}) = \mathrm{f}$;
- **(S1)** se $\varphi$ è la formula atomica $p(t_1, \dots, t_n)$ e $\alpha_\rho(t_i) = d_i$ per $i = 1,\dots,n$, allora $\mathcal{I}_\rho(\varphi) = \alpha(p)(d_1, \dots, d_n)$; nel caso particolare $n = 0$ (lettera proposizionale) $\mathcal{I}_\rho(p) = \alpha(p)$;
- **(S2)** se $\varphi$ è $(P)$, allora $\mathcal{I}_\rho(\varphi) = \mathcal{I}_\rho(P)$;
- **(S3)** se $\varphi$ è $\neg P$, allora $\mathcal{I}_\rho(\varphi) = \neg\,\mathcal{I}_\rho(P)$;
- **(S4)** se $\varphi$ è $P \;\mathit{conn}\; Q$ con $\mathit{conn} \in \{\land, \lor, \Rightarrow, \equiv\}$, allora $\mathcal{I}_\rho(\varphi) = \mathcal{I}_\rho(P) \;\mathit{conn}\; \mathcal{I}_\rho(Q)$.

In (S3) e (S4) i simboli $\neg$ e $\mathit{conn}$ a destra dell'uguale sono le **funzioni semantiche** dei [[Connettivo logico|connettivi]], già introdotte per il CP. Queste regole sono del tutto analoghe a quelle proposizionali; l'unica novità è che le formule atomiche ora contengono termini, quindi per valutarle si usa (S1) insieme alla semantica dei termini.

### 2.3 Le regole (S5) e (S6): i quantificatori

- **(S5)** se $\varphi$ è $(\forall x.P)$, allora
$$
\mathcal{I}_\rho(\varphi) =
\begin{cases}
\mathrm{t} & \text{se } \mathcal{I}_{\rho[d/x]}(P) = \mathrm{t} \text{ per qualunque } d \in D,\\
\mathrm{f} & \text{altrimenti;}
\end{cases}
$$
- **(S6)** se $\varphi$ è $(\exists x.P)$, allora
$$
\mathcal{I}_\rho(\varphi) =
\begin{cases}
\mathrm{t} & \text{se } \mathcal{I}_{\rho[d/x]}(P) = \mathrm{t} \text{ per almeno un } d \in D,\\
\mathrm{f} & \text{altrimenti.}
\end{cases}
$$

L'assegnamento è indispensabile in queste regole: la sottoformula $P$ (la portata del [[Quantificatore|quantificatore]]) è tipicamente aperta, e per valutarla si «prova» ogni elemento $d$ del dominio come valore di $x$, modificando $\rho$ in $\rho[d/x]$.

### 2.4 Formule chiuse

Per le formule **chiuse** l'assegnamento non conta: la semantica dipende solo dall'interpretazione. Le slide enunciano il fatto senza dimostrarlo (la dimostrazione esula dagli scopi del corso):

> [!note] Formule chiuse
> Data un'interpretazione $\mathcal{I}$ e una formula chiusa $\varphi$, per ogni coppia di assegnamenti $\rho, \rho'$ si ha $\mathcal{I}_\rho(\varphi) = \mathcal{I}_{\rho'}(\varphi)$.

Per questo, per una formula chiusa si scrive semplicemente $\mathcal{I}(\varphi)$.

### 2.5 Esempio svolto

**Da mostrare**: la formula
$$
\varphi_1 = \bigl(\exists x.\; Q(x) \land (\forall y.\, P(x,y))\bigr)
$$
è vera nell'interpretazione $\mathcal{I} = (D, \alpha)$ con $D = \{a, b\}$ e

$$
\alpha(P)(x,y) =
\begin{cases}
\mathrm{t} & \text{se } (x = a \text{ e } y = a) \text{ oppure } (x = a \text{ e } y = b),\\
\mathrm{f} & \text{altrimenti,}
\end{cases}
\qquad
\alpha(Q)(x) =
\begin{cases}
\mathrm{t} & \text{se } x = a \text{ oppure } x = b,\\
\mathrm{f} & \text{altrimenti.}
\end{cases}
$$

Sia $\rho$ un assegnamento arbitrario (la formula è chiusa, quindi la scelta è irrilevante). Applicando le regole (S0)-(S6):

1. Per (S2), $\mathcal{I}_\rho\bigl((\exists x.\, Q(x) \land (\forall y.\, P(x,y)))\bigr) = \mathcal{I}_\rho(\exists x.\, Q(x) \land (\forall y.\, P(x,y)))$.
2. Per (S6) basta trovare **un** $d \in D$ per cui la portata è vera. Si prova $d = a$ e si mostra
$$
\mathcal{I}_{\rho[a/x]}\bigl(Q(x) \land (\forall y.\, P(x,y))\bigr) = \mathrm{t}.
$$
3. Per (S4) e (S2) il valore è $\mathcal{I}_{\rho[a/x]}(Q(x)) \land \mathcal{I}_{\rho[a/x]}(\forall y.\, P(x,y))$.
4. Primo congiunto, per (S1): $\alpha_{\rho[a/x]}(x) = a$ e $\alpha(Q)(a) = \mathrm{t}$.
5. Secondo congiunto, per (S5): bisogna provare **tutti** i valori di $y$.
   - con $y \mapsto a$: $\alpha_{\rho[a/x][a/y]}(x) = a$, $\alpha_{\rho[a/x][a/y]}(y) = a$ e $\alpha(P)(a,a) = \mathrm{t}$;
   - con $y \mapsto b$: $\alpha_{\rho[a/x][b/y]}(y) = b$ e $\alpha(P)(a,b) = \mathrm{t}$.

   Quindi $\mathcal{I}_{\rho[a/x]}(\forall y.\, P(x,y)) = \mathrm{t}$.
6. Si ottiene $\mathrm{t} \land \mathrm{t} = \mathrm{t}$, e quindi $\varphi_1$ è vera in $\mathcal{I}$.

Il testimone dell'esistenziale è $a$: il secondo elemento $b$ non basterebbe, perché $\alpha(P)(b, \cdot)$ è sempre falso.

### 2.6 Esercizio dalle slide

Calcolare il valore di verità di
$$
\varphi_2 = (\forall x.\; P(x) \Rightarrow Q(x) \land R(x))
$$
in $\mathcal{I} = (D, \alpha)$ con $D = \{a, b, c\}$ e

| | $a$ | $b$ | $c$ |
|---|---|---|---|
| $\alpha(P)$ | t | t | f |
| $\alpha(Q)$ | t | f | t |
| $\alpha(R)$ | f | t | f |

*Soluzione (non presente nelle slide):* si cerca un controesempio per $\forall$. Per $x = a$: $P(a) = \mathrm{t}$, $Q(a) = \mathrm{t}$, $R(a) = \mathrm{f}$, quindi $Q(a) \land R(a) = \mathrm{f}$ e l'implicazione $\mathrm{t} \Rightarrow \mathrm{f}$ è falsa. Dunque $\mathcal{I}(\varphi_2) = \mathrm{f}$. Il risultato non dipende da come si leggono le precedenze: anche con la lettura $(P \Rightarrow Q) \land R$ il caso $x = a$ dà $R(a) = \mathrm{f}$ e la formula resta falsa.

---

## 3. Modelli, validità, soddisfacibilità, conseguenza logica

Sia $\mathcal{I}$ un'interpretazione e $\varphi$ una formula chiusa.

- **Modello**: se $\varphi$ è vera in $\mathcal{I}$, $\mathcal{I}$ è un **modello** di $\varphi$ e si scrive $\mathcal{I} \models \varphi$. Per un insieme di formule $\Gamma$, $\mathcal{I} \models \Gamma$ significa che $\mathcal{I}$ è modello di tutte le formule di $\Gamma$.
- **Valida**: $\varphi$ è vera in **tutte** le interpretazioni; si scrive $\models \varphi$. È l'estensione del concetto di [[Tautologia|tautologia]].
- **Soddisfacibile**: $\varphi$ è vera in **almeno una** interpretazione; altrimenti è **insoddisfacibile** (corrisponde alle contraddizioni).

**Esempi dalle slide:**

- soddisfacibile: $p(a)$. Basta un'interpretazione che la renda vera, per esempio $D = \mathbb{N}$, $\alpha(a) = 44$, $\alpha(p)(x) = \mathrm{t}$ se $x$ è pari, $\mathrm{f}$ altrimenti;
- valida (come una tautologia): $(\forall x.\; p(x) \lor \neg p(x))$;
- insoddisfacibile (come una contraddizione): $(\exists x.\; p(x) \land \neg p(x))$.

### 3.1 Conseguenza logica

La [[Conseguenza logica|conseguenza logica]] parametrizza la validità rispetto a un insieme di formule $\Gamma$ (le premesse). $\varphi$ è **conseguenza logica** di $\Gamma$, e si scrive $\Gamma \models \varphi$, se e solo se $\varphi$ è vera in tutti i modelli di $\Gamma$: se un'interpretazione rende vere tutte le formule di $\Gamma$ ($\mathcal{I} \models \Gamma$), allora rende vera anche $\varphi$ ($\mathcal{I} \models \varphi$).

Caso particolare: $\{\} \models \varphi$, cioè $\models \varphi$, vale se e solo se $\varphi$ è valida.

---

## 4. Sistemi di dimostrazione

### 4.1 Idea

Come già osservato per il CP, il concetto semantico di conseguenza logica va affiancato da un metodo di calcolo con cui **dimostrare** che una formula segue da un insieme di premesse. L'idea della *proof theory* è individuare un insieme di [[Regola di inferenza|regole di inferenza]] che permettono di organizzare una dimostrazione come una sequenza di passi, ciascuno dei quali applica una regola per derivare una conclusione da premesse.

Una regola di inferenza ha la forma
$$
\frac{\delta_1, \dots, \delta_k}{\delta}
$$
con premesse $\delta_1,\dots,\delta_k$ e conseguenza $\delta$. Se $k = 0$ la regola si chiama **assioma**.

Il [[Calcolo proposizionale|CP]], come presentato nelle lezioni precedenti, è un proof system sull'insieme delle proposizioni: gli **assiomi** sono le leggi sui connettivi dimostrate con le [[Tavola di verità|tavole di verità]] e le **regole di inferenza** sono il [[Principio di sostituzione|principio di sostituzione]] per l'equivalenza e quello per l'implicazione (vedi [[2026-09-22 - Equivalenze tautologiche e sostituzione nell'implicazione|la lezione sulla sostituzione]]).

### 4.2 Dimostrazioni, correttezza, completezza

Una **dimostrazione** di $\varphi$ a partire da un insieme di premesse $\Gamma$ è una sequenza di formule $\varphi_1, \dots, \varphi_n$ tale che:

- ogni $\varphi_i$ è un elemento di $\Gamma$ oppure è ottenuta applicando una regola di inferenza a partire da $\Gamma$ e da $\varphi_1, \dots, \varphi_{i-1}$;
- $\varphi_n$ coincide con $\varphi$.

Si scrive $\Gamma \vdash \varphi$ se esiste una dimostrazione di $\varphi$ da $\Gamma$.

Un proof system è:

- **corretto** se $\Gamma \vdash \varphi$ implica $\Gamma \models \varphi$ (quello che si dimostra è davvero conseguenza logica);
- **completo** se $\Gamma \models \varphi$ implica $\Gamma \vdash \varphi$ (ogni conseguenza logica è dimostrabile).

Correttezza e completezza collegano un concetto puramente **sintattico** ($\vdash$) a uno **semantico** ($\models$). Le slide sottolineano che non ha senso considerare proof system non corretti; il CP è corretto e completo.

### 4.3 Dimostrazioni nella LPO

Il proof system del CP non basta per la LPO. Si continuano a usare tutte le leggi e le regole del CP per i connettivi, ma servono nuove leggi e nuove regole di inferenza per i **quantificatori** (e, più avanti, per l'uguaglianza). Le regole agiscono ancora su formule della forma $\varphi \equiv \psi$ e $\varphi \Rightarrow \psi$. Quelle introdotte nel corso formano un proof system **corretto** per la LPO. Esistono proof system corretti *e completi* per la LPO (deduzione naturale, calcolo dei sequenti), che però non verranno approfonditi.

### 4.4 Leggi generali e ipotesi

Come leggi generali si usano **formule valide** (l'analogo delle tautologie). Se $\Gamma$ contiene solo formule valide e $\Gamma \vdash \varphi$, allora per la correttezza $\Gamma \models \varphi$; ma ogni interpretazione è modello di formule valide, quindi $\models \varphi$: il risultato è valido.

Se in $\Gamma$ ci sono, oltre alle formule valide, anche altre formule (**ipotesi**), la dimostrazione non garantisce la validità di $\varphi$ ma il fatto che $\varphi$ sia conseguenza logica delle ipotesi. Se $\Gamma = \Gamma_1 \cup \Gamma_2$, con $\Gamma_1$ formato da formule valide e $\Gamma_2$ dalle ipotesi, la dimostrazione garantisce $\Gamma_2 \models \varphi$.

### 4.5 Principi di sostituzione generalizzati

I principi di sostituzione del CP devono poter usare anche formule presenti tra le premesse.

**Per l'equivalenza:**
$$
\frac{(P \equiv Q) \in \Gamma}{\Gamma \vdash R \equiv R[Q/P]}
$$
cioè: se $P$ e $Q$ sono equivalenti nelle premesse $\Gamma$, allora è dimostrabile da $\Gamma$ che $R$ e $R[Q/P]$ sono equivalenti.

**Per l'implicazione.** Prima si estende la nozione di occorrenza positiva/negativa alle formule quantificate: $P$ occorre **positivamente** in $(\forall x.P)$ e in $(\exists x.P)$ (i quantificatori non cambiano la polarità). Poi:

$$
\frac{(P \Rightarrow Q) \in \Gamma \quad P \text{ occorre positivamente in } R}{\Gamma \vdash R \Rightarrow R[Q/P]}
\qquad
\frac{(P \Rightarrow Q) \in \Gamma \quad P \text{ occorre negativamente in } R}{\Gamma \vdash R[Q/P] \Rightarrow R}
$$

**Esempi dalle slide**, con ipotesi $P \Rightarrow Q$:

$$
(\forall x.\; P \lor R) \land (\exists x.\; \neg P) \;\Rightarrow\; (\forall x.\; Q \lor R) \land (\exists x.\; \neg P)
$$

è **corretto**, perché la prima $P$ occorre positivamente. Invece

$$
(\forall x.\; P \lor R) \land (\exists x.\; \neg P) \;\Rightarrow\; (\forall x.\; Q \lor R) \land (\exists x.\; \neg Q)
$$

è **sbagliato**, perché la seconda $P$ occorre negativamente (sta sotto una negazione) e quindi la sostituzione con $Q$ andrebbe nel verso opposto.

### 4.6 Teorema di deduzione

Nel CP si dimostravano spesso implicazioni $P \Rightarrow Q$ costruendo una dimostrazione di $Q$ che usa $P$ come ipotesi. Ora la tecnica è giustificata dal [[Teorema di deduzione|teorema di deduzione]]:

$$
\Gamma \vdash P \Rightarrow Q \quad\text{se e solo se}\quad \Gamma, P \vdash Q.
$$

Per dimostrare $P \Rightarrow Q$ si può quindi dimostrare $Q$ usando sia le leggi generali (formule valide) sia $P$ come ipotesi.

> [!example] Esempio
> Per dimostrare $\models (\forall x.\,p(x)) \Rightarrow (\exists x.\,p(x))$ basta assumere $(\forall x.\,p(x))$ come ipotesi e derivare $(\exists x.\,p(x))$: per elim-$\forall$ si ottiene $p(a)$ per un termine $a$ qualsiasi, e per intro-$\exists$ da $p(a)$ si ottiene $(\exists x.\,p(x))$ (le due leggi sono nella sezione seguente).

---

## 5. Leggi per i quantificatori

Come nel CP le leggi fondamentali erano tautologie, per la LPO le leggi sono **formule valide**. Per convincersi della validità di una legge si può usare la definizione di validità oppure una dimostrazione che usi solo premesse valide.

### 5.1 Eliminazione dell'universale, introduzione dell'esistenziale

Due leggi riflettono il significato stesso dei quantificatori:

$$
(\forall x.\, P) \Rightarrow P[t/x] \quad (\text{elim-}\forall)
\qquad\qquad
P[t/x] \Rightarrow (\exists x.\, P) \quad (\text{intro-}\exists)
$$

dove $t$ è un termine e $P[t/x]$ è ottenuto da $P$ sostituendo tutte le occorrenze **libere** di $x$ con $t$. Se qualcosa vale per tutti, vale per un individuo particolare; se vale per un individuo particolare, allora esiste qualcuno per cui vale.

**Esempi:**

- $(\forall x.\; \operatorname{pari}(x) \land x > 2 \Rightarrow \neg\operatorname{primo}(x)) \;\Rightarrow\; \operatorname{pari}(7) \land 7 > 2 \Rightarrow \neg\operatorname{primo}(7)$ (elim-$\forall$);
- $(\forall x.\; \operatorname{uomo}(x) \Rightarrow \operatorname{mortale}(x)) \;\Rightarrow\; \operatorname{uomo}(\mathrm{Socrate}) \Rightarrow \operatorname{mortale}(\mathrm{Socrate})$ (elim-$\forall$);
- $\operatorname{pari}(10) \land 10 > 2 \;\Rightarrow\; (\exists x.\; \operatorname{pari}(x) \land x > 2)$ (intro-$\exists$).

### 5.2 Negazione e annidamento

$$
\neg(\forall x.\, P) \equiv (\exists x.\, \neg P)
\qquad
\neg(\exists x.\, P) \equiv (\forall x.\, \neg P)
\qquad (\text{De Morgan})
$$

Sono le [[Leggi di De Morgan|leggi di De Morgan]] estese ai quantificatori.

Quantificatori **dello stesso tipo** adiacenti si possono scambiare:

$$
(\forall x.\,(\forall y.\, P)) \equiv (\forall y.\,(\forall x.\, P))
\qquad
(\exists x.\,(\exists y.\, P)) \equiv (\exists y.\,(\exists x.\, P))
\qquad (\text{Annidamento})
$$

Le slide non danno una legge per scambiare $\forall$ ed $\exists$ adiacenti. L'ultimo esempio della [[2026-10-13 - Quantificazione ristretta, uguaglianza e specifiche formali|lezione successiva]] dimostra la validità di $(\exists y.\,\forall x.\,P) \Rightarrow (\forall x.\,\exists y.\,P)$, cioè solo un verso (l'inverso non viene trattato).

### 5.3 Legge della costante e dominio non vuoto

$$
(\forall x.\, P) \equiv P \quad\text{se } x \text{ non occorre in } P
\qquad
(\exists x.\, P) \equiv P \quad\text{se } x \text{ non occorre in } P
\qquad (\text{Costante})
$$

Queste leggi valgono **solo se il dominio di interpretazione non è vuoto**. Perché? Per (S5), $\mathcal{I}_\rho(\forall x.\, P) = \mathrm{f}$ se e solo se esiste $d \in D$ con $\mathcal{I}_{\rho[d/x]}(P) = \mathrm{f}$. Se $D = \{\}$ un tale $d$ non esiste, quindi $(\forall x.\, P)$ è **vacuamente vera**. Prendendo $P = \mathrm{F}$ (dove $x$ non occorre), senza la condizione si concluderebbe erroneamente
$$
\underbrace{\mathcal{I}_\rho(\forall x.\, \mathrm{F})}_{\mathrm{t}} = \underbrace{\mathcal{I}_\rho(\mathrm{F})}_{\mathrm{f}}.
$$
Analogamente, e le slide lo lasciano per esercizio, in un dominio vuoto $\mathcal{I}_\rho(\exists x.\, \mathrm{T}) = \mathrm{f}$ ma $\mathcal{I}_\rho(\mathrm{T}) = \mathrm{t}$.

### 5.4 Distribuzione dei quantificatori su $\land$ e $\lor$

$$
(\forall x.\, P \land Q) \equiv (\forall x.\, P) \land (\forall x.\, Q) \quad (\forall{:}\land)
\qquad
(\exists x.\, P \lor Q) \equiv (\exists x.\, P) \lor (\exists x.\, Q) \quad (\exists{:}\lor)
$$

$$
(\forall x.\, P) \lor (\forall x.\, Q) \Rightarrow (\forall x.\, P \lor Q) \quad (\forall{:}\lor)
\qquad
(\exists x.\, P \land Q) \Rightarrow (\exists x.\, P) \land (\exists x.\, Q) \quad (\exists{:}\land)
$$

Nelle ultime due leggi vale **solo l'implicazione**, non l'equivalenza.

- ($\forall{:}\land$): «tutte le persone sono alte e bionde» se e solo se «tutte le persone sono alte» e «tutte le persone sono bionde».
- Controesempio per ($\forall{:}\lor$): «tutte le persone sono maggiorenni o minorenni» è vera, ma non implica «tutte le persone sono maggiorenni» **o** «tutte le persone sono minorenni».

### 5.5 Distribuzione con variabile non presente, e indebolimento

Le leggi di **distribuzione** valgono, di nuovo, solo se il dominio non è vuoto:

$$
(\forall x.\, P \land Q) \equiv (\forall x.\, P) \land Q
\qquad
(\exists x.\, P \lor Q) \equiv (\exists x.\, P) \lor Q
\qquad\text{se } x \text{ non occorre in } Q \quad (\text{Distrib.})
$$

Le leggi di **indebolimento**:

$$
(\forall x.\, P) \Rightarrow (\forall x.\, P \lor Q)
\qquad
(\exists x.\, P) \Rightarrow (\exists x.\, P \lor Q)
\qquad (\text{Indebolimento-}\lor)
$$

$$
(\forall x.\, P \land Q) \Rightarrow (\forall x.\, P)
\qquad
(\exists x.\, P \land Q) \Rightarrow (\exists x.\, P)
\qquad (\text{Indebolimento-}\land)
$$

## Fonte

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 7, 12 ottobre 2026, slide 201-235 (file `Lezione_07.pdf`).
- Il testo delle slide è stato estratto automaticamente; dove i simboli erano rovinati (in particolare nel quadro di $\forall{:}\lor$ e $\exists{:}\land$ e nella legge Costante) ho ricostruito la formula dal contesto.
