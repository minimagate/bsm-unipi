---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-10-20'
title: Regole di inferenza per le triple di Hoare e invarianti
source: Lezione_10.pdf (slide 298-329)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-10-20 - Regole di inferenza per le triple di Hoare e invarianti.md
vault_hash: 4d21ea1793d9bd9f54574624ecc99fd8ff388fc8483da6a6038266047ed7ac5d
---

# Regole di inferenza per le triple di Hoare e invarianti

La [[2026-10-19 - Espressioni, comandi e triple di Hoare|lezione precedente]] ha definito la semantica di espressioni e comandi e introdotto le [[Tripla di Hoare|triple di Hoare]] $\{P\}\,C\,\{R\}$. Questa lezione costruisce il **proof system** per verificarle: regole per rafforzare la [[Precondizione e postcondizione|precondizione]] e indebolire la postcondizione, assiomi per `skip` e per l'assegnamento (con la funzione $\mathrm{def}$, che controlla che le espressioni siano definite), regole per sequenza e condizionale. Poi distingue [[Correttezza totale|correttezza totale]] e parziale e comincia a trattare il `while` con le proprietà [[Invariante di ciclo|invarianti]].

Promemoria: una tripla $\{P\}\,C\,\{R\}$ è soddisfatta se da ogni stato $\sigma\models P$ l'esecuzione di $C$ termina (con successo) in uno stato $\sigma'\models R$. $\{P\}$ indica anche l'insieme degli stati che soddisfano $P$.

---

## 1. La proprietà (P3) all'opera

Riprendiamo le proprietà (P1)-(P3) della lezione precedente. Le slide non ne danno le dimostrazioni, ma mostrano due esempi della più importante:

$$
\textbf{(P3)}\qquad\sigma[\mathcal E(E,\sigma)/x]\models P\quad\text{se e solo se}\quad\sigma\models P[E/x].
$$

**Primo esempio.**

$$
\begin{aligned}
&\sigma[\mathcal E(z+1,\sigma)/x]\models(x>y)\\
\equiv\;&\{\text{definizione di }\models\text{ e di }\mathcal E\}\quad(\sigma(z)+1)>\sigma(y)\\
\equiv\;&\{\text{definizione di }\models\}\quad\sigma\models(z+1)>y\\
\equiv\;&\{\text{sostituzione}\}\quad\sigma\models(x>y)[z+1/x]
\end{aligned}
$$

**Secondo esempio.**

$$
\begin{aligned}
&\sigma[\mathcal E(x+y,\sigma)/x]\models(x=z)\\
\equiv\;&\{\text{definizione di }\models\text{ e di }\mathcal E\}\quad(\sigma(x)+\sigma(y))=\sigma(z)\\
\equiv\;&\{\text{definizione di }\models\}\quad\sigma\models(x+y)=z\\
\equiv\;&\{\text{sostituzione}\}\quad\sigma\models(x=z)[x+y/x]
\end{aligned}
$$

---

## 2. Regole per pre- e postcondizioni

**Rafforzamento della precondizione:**

$$
\frac{P\Rightarrow P'\qquad\{P'\}\,C\,\{R\}}{\{P\}\,C\,\{R\}}\ (\mathrm{pre})
$$

La correttezza segue dalla definizione di tripla soddisfatta e dal fatto che $P\Rightarrow P'$ se e solo se $\{P\}\subseteq\{P'\}$: se $C$ funziona partendo da ogni stato di $\{P'\}$, funziona in particolare partendo dagli stati di $\{P\}$.

**Indebolimento della postcondizione:**

$$
\frac{\{P\}\,C\,\{R'\}\qquad R'\Rightarrow R}{\{P\}\,C\,\{R\}}\ (\mathrm{post})
$$

La correttezza si mostra in modo analogo. Messe insieme, le due regole danno

$$
\frac{P\Rightarrow P'\qquad\{P'\}\,C\,\{R'\}\qquad R'\Rightarrow R}{\{P\}\,C\,\{R\}}\ (\mathrm{pre\text{-}post})
$$

---

## 3. Assioma per `skip`

$$
\{P\}\ \mathtt{skip}\ \{P\}\qquad(\mathrm{skip})
$$

La correttezza è ovvia: `skip`, eseguito a partire da $\sigma$, lascia lo stato $\sigma$ com'è.

---

## 4. Quando un'espressione è definita: la funzione $\mathrm{def}$

Quando si esegue un comando che contiene un'espressione (come `x := E` o `if E' then C else C' fi`), l'espressione potrebbe non essere definita per due motivi:

1. **tipizzazione scorretta**, come in `x := 5 + true` o in `if 7 * 4 then C else C' fi`;
2. **tipizzazione corretta ma valore indefinito**, come in `x := 0; y := k div x`.

Il caso 1 non si presenta mai, perché il controllo dei tipi si assume già fatto in una fase preliminare di analisi statica. Per il caso 2 si introduce

$$
\mathrm{def}:\mathrm{Exp}\to\mathrm{Fbf},
$$

dove $\mathrm{Fbf}$ è l'insieme delle asserzioni ([[Formula ben formata|formule ben formate]] del primo ordine), in modo che per ogni stato $\sigma$

$$
\sigma\models\mathrm{def}(E)\quad\text{se esiste }v\in\mathrm{Val}\text{ tale che }\mathcal E(E,\sigma)=v.
$$

**Definizione per casi:**

$$
\begin{aligned}
\mathrm{def}(c)&=T &&c\in\mathrm{Const}\\
\mathrm{def}(x)&=T &&x\in\mathrm{Ide}\\
\mathrm{def}(E\ \mathtt{op}\ E')&=\mathrm{def}(E)\land\mathrm{def}(E') &&\mathtt{op}\in\{*,+,-,=,\neq,<,>,\leq,\geq,\mathtt{and},\mathtt{or}\}\\
\mathrm{def}(E\ \mathtt{op}\ E')&=\mathrm{def}(E)\land\mathrm{def}(E')\land E'\neq0 &&\mathtt{op}\in\{\mathtt{div},\mathtt{mod}\}\\
\mathrm{def}(\mathtt{not}\ E)&=\mathrm{def}(E)\\
\mathrm{def}((E))&=\mathrm{def}(E)
\end{aligned}
$$

In pratica le uniche fonti di indefinitezza sono `div` e `mod` con secondo argomento nullo.

**Esempio.**

$$
\begin{aligned}
&\mathrm{def}(x\ \mathtt{div}\ (z-y))\\
\equiv\;&\{\text{definizione di }\mathrm{def}\}\quad\mathrm{def}(x)\land\mathrm{def}((z-y))\land z-y\neq0\\
\equiv\;&\{\text{definizione di }\mathrm{def},\ z-y\neq0\equiv z\neq y\}\quad T\land\mathrm{def}(z-y)\land z\neq y\\
\equiv\;&\{\text{definizione di }\mathrm{def},\ \text{Unità}\}\quad\mathrm{def}(z)\land\mathrm{def}(y)\land z\neq y\\
\equiv\;&\{\text{definizione di }\mathrm{def}\}\quad T\land T\land z\neq y\\
\equiv\;&\{\text{Unità}\}\quad z\neq y
\end{aligned}
$$

---

## 5. Assegnamento

### 5.1 L'assioma

$$
\{\mathrm{def}(E)\land P[E/x]\}\ x:=E\ \{P\}\qquad(\mathrm{ass})
$$

dove $P[E/x]$ è l'asserzione $P$ in cui $E$ prende il posto di $x$. È la [[Regola dell'assegnamento|regola dell'assegnamento]].

**Intuizione.** Perché $P$ sia vera dopo l'assegnamento, la stessa $P$ deve essere vera **nello stato di partenza** una volta messo $E$ al posto di $x$. Inoltre $E$ deve essere definita nello stato di partenza, cioè la sua valutazione non deve dare errori.

**Occhio al verso:** l'assioma si usa **all'indietro**, dalla postcondizione alla precondizione.

$$
\begin{aligned}
&\{\,????\,\}\ x:=x+2\ \{x>y\}\\
&\{\mathrm{def}(x+2)\land(x>y)[x+2/x]\}\ x:=x+2\ \{x>y\}\\
&\{x+2>y\}\ x:=x+2\ \{x>y\}
\end{aligned}
$$

**Correttezza.** Segue dalla semantica dell'assegnamento, $\mathcal C(x:=E,\sigma)=\sigma[\mathcal E(E,\sigma)/x]$, e dalla proprietà (P3). Il congiunto $\mathrm{def}(E)$ garantisce che $\mathcal E(E,\sigma)$ esista, quindi che il comando termini con successo.

### 5.2 Esempi

- $\{T\}\ x:=5\ \{x=5\}$. Dall'assioma la precondizione è $\mathrm{def}(5)\land(x=5)[5/x]\equiv(5=5)\equiv T$.
- $\{x>2\}\ x:=5\ \{x=5\}$. Stessa postcondizione, ma ora la precondizione non è quella prodotta dall'assioma. Si conclude con la regola (pre), sapendo che $x>2\Rightarrow T$.
- $\{x=5\}\ x:=x+1\ \{x>2\}$. Analogamente con (ass) e (pre): $(x>2)[x+1/x]=x+1>2\equiv x>1$, e $x=5\Rightarrow x>1$.

### 5.3 La regola per l'assegnamento

Combinando (pre) con l'assioma si ottiene una regola più comoda per **verificare** una tripla già data:

$$
\frac{R\Rightarrow\mathrm{def}(E)\land P[E/x]}{\{R\}\ x:=E\ \{P\}}\ (\mathrm{ass})
$$

Non è altro che l'istanza di (pre)

$$
\frac{R\Rightarrow\mathrm{def}(E)\land P[E/x]\qquad\{\mathrm{def}(E)\land P[E/x]\}\ x:=E\ \{P\}}{\{R\}\ x:=E\ \{P\}}
$$

in cui la seconda premessa sparisce perché è un assioma. Verificare un assegnamento si riduce quindi a dimostrare una [[Implicazione|implicazione]] tra asserzioni.

---

## 6. Sequenza

$$
\frac{\{P\}\,C\,\{R\}\qquad\{R\}\,C'\,\{Q\}}{\{P\}\ C;C'\ \{Q\}}\ (\mathrm{seq})
$$

La correttezza deriva dalla semantica $\mathcal C(C;C',\sigma)=\mathcal C(C',\mathcal C(C,\sigma))$. L'idea è che $C'$ deve garantire la postcondizione nello stato di arrivo, ma $C'$ viene eseguito nello stato prodotto da $C$: l'asserzione intermedia $R$ fa da ponte.

**Esempio.** Verifichiamo

$$
\{x\geq y-1\}\ x:=x+1;\ y:=y-1\ \{x>y\}.
$$

Per (seq) serve un'asserzione intermedia $R$ con

1. $\{x\geq y-1\}\ x:=x+1\ \{R\}$;
2. $\{R\}\ y:=y-1\ \{x>y\}$.

Si **calcola $R$ all'indietro** con l'assioma (ass) applicato a (2):

$$
\{\mathrm{def}(y-1)\land(x>y)[y-1/y]\}\ y:=y-1\ \{x>y\}.
$$

Fissiamo quindi $R=\mathrm{def}(y-1)\land x>y-1$. Resta (1); con la regola (ass) basta dimostrare

$$
x\geq y-1\ \Rightarrow\ \mathrm{def}(x+1)\land\bigl(\mathrm{def}(y-1)\land x>y-1\bigr)[x+1/x].
$$

*Svolgimento dell'esercizio (mio).* I due $\mathrm{def}$ valgono $T$, e la sostituzione dà $x+1>y-1$, cioè $x>y-2$. Da $x\geq y-1>y-2$ segue la tesi.

---

## 7. Condizionale

$$
\frac{P\Rightarrow\mathrm{def}(E)\qquad\{P\land E\}\,C_1\,\{Q\}\qquad\{P\land\neg E\}\,C_2\,\{Q\}}{\{P\}\ \mathtt{if}\ E\ \mathtt{then}\ C_1\ \mathtt{else}\ C_2\ \mathtt{fi}\ \{Q\}}\ (\mathrm{cond})
$$

La correttezza segue dalla semantica del comando. In parole:

- nello stato iniziale bisogna valutare la guardia, quindi serve $\mathrm{def}(E)$;
- se nello stato iniziale vale $P\land E$, è il **ramo then** a dover terminare in uno stato che soddisfa la postcondizione;
- se vale $P\land\neg E$, è il **ramo else**.

### 7.1 Esempio: il massimo

Verificare

```
{m = 0}
if x < y
   then m := y
   else m := x
fi
{m = max(x, y)}
```

Per (cond) bisogna mostrare:

1. $m=0\Rightarrow\mathrm{def}(x<y)$. Immediata: $\mathrm{def}(x<y)=\mathrm{def}(x)\land\mathrm{def}(y)\equiv T$.
2. $\{m=0\land x<y\}\ m:=y\ \{m=\max(x,y)\}$. Con (ass) ci si riduce a $m=0\land x<y\Rightarrow\mathrm{def}(y)\land(m=\max(x,y))[y/m]$, cioè
   $$
   m=0\land x<y\Rightarrow y=\max(x,y).
   $$
3. $\{m=0\land x\geq y\}\ m:=x\ \{m=\max(x,y)\}$. Analogamente ci si riduce a
   $$
   m=0\land x\geq y\Rightarrow x=\max(x,y).
   $$

*Completamento (mio).* Le implicazioni 2 e 3 valgono per definizione di massimo: se $x<y$ il massimo è $y$, se $x\geq y$ è $x$. L'ipotesi $m=0$ non serve.

### 7.2 Variabili di specifica: trovare l'espressione mancante

Determinare $E$ in modo che sia verificata

$$
\{x=N\land y=M\}\ t:=E;\ x:=y;\ y:=t\ \{x=M\land y=N\}.
$$

$M$ e $N$ sono [[Specifica di un problema|variabili di specifica]]: non possono comparire nei comandi. La risposta la conosciamo già (lo scambio con variabile ausiliaria), ma qui la **ricaviamo** con le regole. Per (seq) servono $R_1$, $R_2$ con

1. $\{x=N\land y=M\}\ t:=E\ \{R_1\}$;
2. $\{R_1\}\ x:=y\ \{R_2\}$;
3. $\{R_2\}\ y:=t\ \{x=M\land y=N\}$.

Si procede all'indietro con (ass).

- Da (3): $\{\mathrm{def}(t)\land(x=M\land y=N)[t/y]\}\ y:=t\ \{x=M\land y=N\}$, quindi si fissa $R_2=(x=M\land t=N)$.
- Da (2): $\{\mathrm{def}(y)\land(x=M\land t=N)[y/x]\}\ x:=y\ \{x=M\land t=N\}$, quindi si fissa $R_1=(y=M\land t=N)$.
- Resta (1), $\{x=N\land y=M\}\ t:=E\ \{y=M\land t=N\}$. Con la regola (ass) basta trovare $E$ tale che
  $$
  x=N\land y=M\Rightarrow\mathrm{def}(E)\land(y=M\land E=N).
  $$

È evidente che la $E$ cercata è proprio $x$ (**e non $N$!!**, che non può comparire in un comando).

### 7.3 Esercizi delle slide

**Le seguenti triple sono soddisfatte? Perché?**

- $\{z=5\land y=7\land x=3\}\ x:=0;\ y:=z\ \mathtt{div}\ x\ \{z>4\}$
- $\{x=N\land y=M\}\ x:=y;\ y:=x\ \{x=M\land y=N\}$

*Risposta (mia).* Nessuna delle due. Nella prima, dopo `x := 0` il comando `y := z div x` divide per zero: l'esecuzione non termina con successo, anche se $z>4$ resterebbe vero. Formalmente, calcolando all'indietro serve $\mathrm{def}(z\ \mathtt{div}\ x)$, cioè $x\neq0$, dopo `x := 0`, e quindi $0\neq0$, che è falso. Nella seconda lo stato finale è $x=M$, $y=M$, come visto nell'esempio dello scambio sbagliato, quindi la postcondizione vale solo se $M=N$.

**Verificare**

```
{x = 5}
x := 3;
if (x = 3) then y := 7 else y := 5 fi
{x = 3 ∧ y = 7}
```

Per (seq) serve $R$ con (1) $\{x=5\}\ x:=3\ \{R\}$ e (2) $\{R\}\ \mathtt{if}\ (x=3)\ \mathtt{then}\ y:=7\ \mathtt{else}\ y:=5\ \mathtt{fi}\ \{x=3\land y=7\}$. A differenza degli altri esempi, qui **non si può usare l'assioma dell'assegnamento per trovare $R$**, perché il secondo comando è un condizionale. Un candidato naturale è $R=(x=3)$.

*Completamento (mio).*

- (1) Con (ass): $x=5\Rightarrow\mathrm{def}(3)\land3=3$, vera.
- (2) Con (cond): $x=3\Rightarrow\mathrm{def}(x=3)\equiv T$. Ramo then: $x=3\land x=3\Rightarrow\mathrm{def}(7)\land x=3\land7=7$, vera. Ramo else: la premessa $x=3\land\neg(x=3)$ è falsa, quindi l'implicazione richiesta da (ass) è vera.

### 7.4 Rafforzamento della precondizione

Si verifichi

```
{x ≥ 0 ∧ y ≥ 0}
if x div y > 0
   then z := x
   else z := y
fi
{z = x max y}
```

Siccome è un condizionale, bisogna prima dimostrare $x\geq0\land y\geq0\Rightarrow\mathrm{def}(x\ \mathtt{div}\ y>0)$. Ma $\mathrm{def}(x\ \mathtt{div}\ y>0)\equiv y\neq0$, e la precondizione non lo garantisce: con $y=0$ la guardia non è definita. Se vogliamo che la tripla sia soddisfatta, **dobbiamo rafforzare la precondizione** e verificare invece

$$
\{x\geq0\land y>0\}\ \mathtt{if}\ x\ \mathtt{div}\ y>0\ \mathtt{then}\ z:=x\ \mathtt{else}\ z:=y\ \mathtt{fi}\ \{z=x\max y\}.
$$

Per (cond):

1. $x\geq0\land y>0\Rightarrow y\neq0$, ovvia;
2. $\{x\geq0\land y>0\land(x\ \mathtt{div}\ y)>0\}\ z:=x\ \{z=x\max y\}$;
3. $\{x\geq0\land y>0\land\neg((x\ \mathtt{div}\ y)>0)\}\ z:=y\ \{z=x\max y\}$.

*Completamento di 2 e 3 (mio).* Con $x\geq0$ e $y>0$, si ha $x\ \mathtt{div}\ y>0$ se e solo se $x\geq y$. In 2 serve quindi $x\geq y\Rightarrow x=x\max y$; in 3 si ha $x\ \mathtt{div}\ y=0$, cioè $x<y$, e serve $x<y\Rightarrow y=x\max y$. Entrambe sono vere.

---

## 8. Correttezza totale e correttezza parziale

Finora $\{P\}\,C\,\{Q\}$ è soddisfatta se, per ogni $\sigma\models P$, l'esecuzione di $C$ da $\sigma$ **termina** in uno stato $\sigma'\models Q$. Si scrive

$$
\models_{tot}\{P\}\,C\,\{Q\}
$$

e si parla di **correttezza totale**: la validità della tripla implica anche la terminazione. Gli assiomi e le regole visti finora sono corretti rispetto a $\models_{tot}$ **grazie a $\mathrm{def}$**.

Esiste una nozione più debole: $\{P\}\,C\,\{Q\}$ è soddisfatta se, per ogni $\sigma\models P$, **se** l'esecuzione di $C$ da $\sigma$ termina, **allora** termina in uno stato $\sigma'\models Q$. Si scrive

$$
\models_{par}\{P\}\,C\,\{Q\}
$$

e si parla di **correttezza parziale**: la tripla non garantisce la terminazione. Per questa nozione le regole si possono indebolire, sostanzialmente ignorando $\mathrm{def}$:

$$
\{Q[E/x]\}\ x:=E\ \{Q\}\qquad(\mathrm{ass})_{par}
\qquad\qquad
\frac{P\Rightarrow Q[E/x]}{\{P\}\ x:=E\ \{Q\}}
$$

$$
\frac{\{P\land E\}\,C_1\,\{Q\}\qquad\{P\land\neg E\}\,C_2\,\{Q\}}{\{P\}\ \mathtt{if}\ E\ \mathtt{then}\ C_1\ \mathtt{else}\ C_2\ \mathtt{fi}\ \{Q\}}\ (\mathrm{cond})_{par}
$$

---

## 9. Il comando iterativo e le proprietà invarianti

### 9.1 Il problema

Ricordiamo la semantica del [[Comando iterativo|`while`]]:

$$
\mathcal C(\mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw},\sigma)=
\begin{cases}
\sigma&\text{se }\mathcal E(E,\sigma)=\mathbf f\\
\mathcal C(\mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw},\mathcal C(C,\sigma))&\text{se }\mathcal E(E,\sigma)=\mathbf t
\end{cases}
$$

Si cerca una regola della forma

$$
\frac{\varphi_1\qquad\varphi_2\qquad\dots\qquad\varphi_k}{\{P\}\ \mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\ \{R\}}.
$$

L'esecuzione del `while` corrisponde a una sequenza $C_1;C_2;\dots;C_n;\dots$ in cui ogni $C_i$ coincide con $C$ e $n$ è il minimo numero di iterazioni che falsifica la guardia. In generale però **non si può stabilire a priori** né se il comando termina, né quante volte venga ripetuto il corpo.

Se si sapesse che la sequenza è finita, $\underbrace{C;C;\dots;C}_{k\text{ volte}}$, si potrebbe applicare più volte (seq):

$$
\frac{\{P\}\,C\,\{P_1\}\qquad\{P_1\}\,C\,\{P_2\}\qquad\dots\qquad\{P_{k-1}\}\,C\,\{R\}}{\{P\}\ \mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\ \{R\}}.
$$

### 9.2 L'idea dell'invariante

Non conoscendo $k$, bisogna ragionare **indipendentemente da $k$**. Si cerca un'unica asserzione $\mathit{Inv}$ (l'**invariante**) che prenda il posto di tutte le asserzioni intermedie $P,P_1,\dots,P_{k-1}$ e di quella finale. Ragionando in termini di correttezza parziale si può allora concludere

$$
\{\mathit{Inv}\}\ \mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\ \{\mathit{Inv}\}.
$$

Si possono fare due raffinamenti.

- **Postcondizione più forte.** Se il comando termina, termina in uno stato in cui la guardia è falsa:
  $$
  \{\mathit{Inv}\}\ \mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\ \{\mathit{Inv}\land\neg E\}.
  $$
- **Garantire l'invarianza.** Si chiede che $\mathit{Inv}$ resti vera dopo ogni iterazione, $\{\mathit{Inv}\}\,C\,\{\mathit{Inv}\}$. Ma ogni iterazione parte da uno stato in cui la guardia è vera, quindi si può rafforzare la precondizione:
  $$
  \{\mathit{Inv}\land E\}\,C\,\{\mathit{Inv}\}.
  $$

### 9.3 Le regole

Riassumendo:

$$
\frac{\{\mathit{Inv}\land E\}\,C\,\{\mathit{Inv}\}}{\{\mathit{Inv}\}\ \mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\ \{\mathit{Inv}\land\neg E\}}\ (1)
$$

che è **corretta rispetto a $\models_{par}$**.

Un invariante deve essere in qualche modo **significativo** per il comando: per esempio $T$ è invariante per qualunque ciclo (ogni stato soddisfa $T$), ma non dice nulla.

> [!example] Esempio
> Per `while x > 0 do x := x - 1 endw` un invariante utile è $\mathit{Inv}=(x\geq0)$. Preservato: $\{x\geq0\land x>0\}\ x:=x-1\ \{x\geq0\}$ è soddisfatta, perché $x>0$ implica $x-1\geq0$ sugli interi. All'uscita si ha $\mathit{Inv}\land\neg(x>0)$, cioè $x\geq0\land x\leq0$, quindi $x=0$.

Lo scopo iniziale era una tripla $\{P\}\ \mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\ \{R\}$ con $P$ e $R$ generiche. Si rafforzano allora le premesse di (1) con (pre-post):

$$
\frac{P\Rightarrow\mathit{Inv}\qquad\{\mathit{Inv}\land E\}\,C\,\{\mathit{Inv}\}\qquad\mathit{Inv}\land\neg E\Rightarrow R}{\{P\}\ \mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\ \{R\}}\ (\text{1-bis})
$$

Le tre premesse dicono che l'invariante vale all'inizio, è preservato da ogni iterazione e, insieme alla guardia falsa, implica la postcondizione. *Nota (mia):* (1-bis) è ottenuta da (1), quindi anch'essa garantisce solo la correttezza **parziale**; la terminazione del ciclo non è coperta dalle slide di questa lezione.

## Fonte

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 10, 20 ottobre 2026, slide 298-329 (file `Lezione_10.pdf`). La slide 298 ripete le proprietà (P1)-(P3) già enunciate alla fine della Lezione 9.
- Il testo delle slide è stato estratto automaticamente e i simboli rovinati sono stati ricostruiti dal contesto. Nella slide 304 i due casi di indefinitezza sono entrambi numerati «(1)»; qui sono numerati 1 e 2. Le parti segnate «mia» o «mio» non compaiono nelle slide.
