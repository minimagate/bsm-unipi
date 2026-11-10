---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-10-26'
title: Correttezza totale dei cicli, funzioni di terminazione e programmi annotati
source: Lezione_11.pdf (slide 330-354)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-10-26 - Correttezza totale dei cicli, funzioni di terminazione e programmi annotati.md
vault_hash: 48cb37d57dfde0ce97c15bc6fde914ec5bcaceccfc4ecde49f745261ae506365
---

# Correttezza totale dei cicli, funzioni di terminazione e programmi annotati

La [[2026-10-20 - Regole di inferenza per le triple di Hoare e invarianti|lezione precedente]] ha introdotto gli [[Invariante di ciclo|invarianti]] per dimostrare la **correttezza parziale** del `while`. Ora aggiungiamo ciò che serve per la [[Correttezza totale|correttezza totale]]: la guardia deve essere sempre definita e il ciclo deve terminare. Lo strumento centrale è una [[Funzione di terminazione|funzione di terminazione]], che associa agli stati un valore naturale strettamente decrescente a ogni iterazione.

I programmi usano il linguaggio didattico del corso, con `:=`, `while ... do ... endw` e `if ... then ... else ... fi`. Le annotazioni tra graffe sono asserzioni, non comandi da eseguire. Gli esercizi completati qui sono indicati come *svolgimento aggiunto*.

## 1. Invariante e guardia falsa: che cosa sappiamo all'uscita

Per la correttezza parziale vale la regola

$$
\frac{\{Inv\land E\}\ C\ \{Inv\}}
     {\{Inv\}\ \mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\ \{Inv\land\neg E\}}.
$$

L'invariante vale prima della prima valutazione della guardia e viene ristabilito dopo ogni esecuzione del corpo. **Non serve che valga dopo ogni singolo comando dentro al corpo**: basta che sia ripristinato prima della valutazione successiva della guardia.

Se il ciclo termina, l'invariante vale ancora e la guardia è falsa. Per dimostrare una postcondizione $Q$ si cerca quindi un $Inv$ tale che

$$
Inv\land\neg E\Rightarrow Q.
$$

Una proprietà sempre vera, come $2>0$, è invariante, ma di solito non contiene abbastanza informazione per ottenere $Q$.

### 1.1 Esempio geometrico: eliminare gli incroci

Sono dati $N$ punti blu e $N$ punti rossi nel piano, senza tre punti allineati. Vogliamo abbinarli con $N$ segmenti, ciascuno con estremi di colore diverso e senza intersezioni tra segmenti.

L'algoritmo è descritto informalmente:

```text
abbina ciascun punto blu a un diverso punto rosso;
while esistono due segmenti che si intersecano do
    sostituiscili con i due segmenti non incrociati
    che collegano ancora estremi di colore diverso
endw
```

Le istruzioni in linguaggio naturale sono pseudocodice. L'insieme $S$ resta sempre un abbinamento degli stessi punti: ogni punto appartiene a un solo segmento.

Definiamo

$$
good(s)\equiv\text{gli estremi di }s\text{ hanno colori diversi},
\qquad
good(S)\equiv\forall s\in S.\ good(s).
$$

L'inizializzazione stabilisce $good(S)$ e il corpo la preserva. All'uscita vale quindi

$$
good(S)\land\text{nessuna coppia di segmenti si interseca}.
$$

Questo risolve il problema **a condizione che il ciclo termini**. Per la terminazione serve un argomento in più, che vediamo più avanti.

## 2. Dalla correttezza parziale alla correttezza totale

Per garantire che l'esecuzione termini con successo bisogna controllare:

- che la guardia $E$ sia definita a ogni valutazione;
- che ogni esecuzione del corpo termini con successo;
- che il numero di iterazioni sia finito.

Il secondo punto è già coperto dalle triple sul corpo, che ora si interpretano in **correttezza totale**. Per il primo si usa $\mathrm{def}(E)$, introdotta nella lezione 10:

$$
\{Inv\land E\}\ C\ \{Inv\land\mathrm{def}(E)\}.
$$

Inoltre $\mathrm{def}(E)$ deve valere prima del primo controllo. Queste condizioni, da sole, non escludono che la guardia resti vera per sempre.

### 2.1 La sequenza degli stati

Indichiamo con

$$
\sigma_0,\sigma_1,\ldots,\sigma_i,\ldots
$$

gli stati che si incontrano all'inizio e dopo ciascuna iterazione, con $\sigma_{i+1}=\mathcal C(C,\sigma_i)$ quando la guardia è vera. Tutti soddisfano $Inv$.

Se associamo a ogni stato un naturale

$$
a_i=F(\sigma_i)
$$

e dimostriamo che $a_{i+1}<a_i$, la sequenza non può essere infinita: **non esiste una successione infinita strettamente decrescente di numeri naturali**.

La funzione $F$ è detta **funzione di terminazione**; la sua espressione nello stato si indica con $expt$ o, più brevemente, $t$.

Servono due proprietà distinte:

$$
\underbrace{Inv\Rightarrow expt\geq0}_{\text{ipotesi di terminazione}},
$$

$$
\underbrace{\{Inv\land E\land expt=V\}\ C\ \{expt<V\}}_{\text{ipotesi di progresso}}.
$$

$expt$ deve essere intera e definita negli stati considerati. $V$ è una [[Specifica di un problema|variabile di specifica]], fresca rispetto al programma: serve nel ragionamento a ricordare il valore di $expt$ prima dell'iterazione e il corpo non la modifica.

Nota bene: la sola non negatività non basta, perché una funzione costante non misura alcun progresso. E non basta nemmeno la sola diminuzione, perché una funzione intera potrebbe scendere all'infinito sotto zero. Anche una funzione reale positiva può diminuire per sempre, come $1,1/2,1/4,\ldots$.

## 3. La regola del `while` in correttezza totale

La regola delle slide è

$$
\frac{
\begin{gathered}
Inv\Rightarrow expt\geq0\\
\{Inv\land E\land expt=V\}\ C\ \{expt<V\}\\
\{Inv\land E\}\ C\ \{Inv\land\mathrm{def}(E)\}
\end{gathered}
}{
\{Inv\land\mathrm{def}(E)\}\
\mathtt{while}\ E\ \mathtt{do}\ C\ \mathtt{endw}\
\{Inv\land\neg E\}
}\quad(\mathrm{while}).
$$

Per una specifica generica $\{P\}\,W\,\{Q\}$ si aggiungono il collegamento iniziale e quello finale:

| Obbligo | Che cosa bisogna dimostrare |
|---|---|
| Ingresso | $P\Rightarrow Inv\land\mathrm{def}(E)$ |
| Invarianza | $\{Inv\land E\}\ C\ \{Inv\land\mathrm{def}(E)\}$ |
| Terminazione | $Inv\Rightarrow expt\geq0$ |
| Progresso | $\{Inv\land E\land expt=V\}\ C\ \{expt<V\}$ |
| Uscita | $Inv\land\neg E\Rightarrow Q$ |

Spesso $P$ da sola non basta a stabilire l'invariante. Si premette allora un comando di inizializzazione $CI$ e si dimostra

$$
\{P\}\ CI\ \{Inv\land\mathrm{def}(E)\}.
$$

Con la regola della sequenza si conclude $\{P\}\ CI;W\ \{Q\}$.

## 4. Esempio completo: somma dei primi interi

Sia $n$ un intero che il programma non modifica, e consideriamo

```text
{n > 0}
x := 0;
s := 0;
while x < n do
    s := s + x;
    x := x + 1
endw
```

Il ciclo somma gli interi da $0$ a $n-1$. Scegliamo

$$
Inv\equiv s=\sum_{i=0}^{x-1}i\ \land\ 0\leq x\leq n,
\qquad expt=n-x.
$$

### 4.1 Inizializzazione

Dopo `x := 0; s := 0`, la somma $\sum_{i=0}^{-1}i$ è vuota e vale $0$. Quindi l'invariante è vera; la guardia $x<n$ è sempre definita.

### 4.2 Invarianza: calcolo all'indietro

Vogliamo dimostrare

$$
\{Inv\land x<n\}\ s:=s+x;\ x:=x+1\ \{Inv\}.
$$

Partendo dall'ultimo assegnamento, l'asserzione intermedia richiesta è

$$
R=Inv[x+1/x]
\equiv s=\sum_{i=0}^{x}i\ \land\ 0\leq x+1\leq n.
$$

Prima di `s := s + x` bisogna perciò avere

$$
R[s+x/s]
\equiv s+x=\sum_{i=0}^{x}i\ \land\ 0\leq x+1\leq n.
$$

Da $Inv$ e $x<n$ segue questa asserzione, perché

$$
\sum_{i=0}^{x}i=\left(\sum_{i=0}^{x-1}i\right)+x,
\qquad 0\leq x<n\Rightarrow0\leq x+1\leq n.
$$

Tutte le espressioni del corpo sono definite.

### 4.3 Terminazione e risultato

*Svolgimento aggiunto degli obblighi lasciati per esercizio.* Da $x\leq n$ segue $n-x\geq0$. Durante il corpo $n$ non cambia e $x$ aumenta di $1$, dunque, se prima $n-x=V$, dopo vale

$$
n-(x+1)=V-1<V.
$$

All'uscita, $Inv\land\neg(x<n)$ implica $x=n$, perciò

$$
s=\sum_{i=0}^{n-1}i.
$$

La precondizione delle slide è $n>0$; lo stesso programma e la stessa dimostrazione funzionano anche con $n\geq0$. Per $n=0$ il corpo non viene eseguito e il risultato è la somma vuota.

## 5. Terminazione dell'esempio geometrico

### 5.1 Perché contare gli incroci non basta

Una prima candidata è il numero di intersezioni presenti in $S$. È un naturale, ma **non è detto che diminuisca**: eliminare l'incrocio scelto può crearne altri con i segmenti rimanenti.

Sistemare un difetto in un punto non basta a far scendere il numero totale di difetti.

### 5.2 La lunghezza totale diminuisce

Scegliamo invece

$$
F(S)=\sum_{s\in S}\ell(s),
$$

dove $\ell(s)$ è la lunghezza del segmento $s$. Se $AB$ e $CD$ si incrociano in $E$ e vengono sostituiti da $AD$ e $CB$, la disuguaglianza triangolare dà

$$
\ell(AD)<\ell(AE)+\ell(ED),
\qquad
\ell(CB)<\ell(CE)+\ell(EB).
$$

Le disuguaglianze sono strette perché i punti dati non contengono terne allineate. Sommandole,

$$
\ell(AD)+\ell(CB)
<\ell(AB)+\ell(CD).
$$

Gli altri segmenti non cambiano, quindi $F(S')<F(S)$.

### 5.3 Perché qui una funzione reale è sufficiente

$F$ assume valori reali non negativi: questo, da solo, non proverebbe la terminazione. Ma gli abbinamenti possibili tra i punti dati sono **finiti**: scegliendo per ciascun punto blu un diverso punto rosso, ci sono $N!$ abbinamenti.

Anche l'insieme dei valori di $F$ è quindi finito. Una successione strettamente decrescente scelta da un insieme finito non può essere infinita. L'algoritmo termina e risolve il problema.

*Precisazione aggiunta:* la finitezza riguarda le configurazioni costruite sui punti iniziali fissati. Non stiamo considerando punti del piano che possano spostarsi liberamente.

## 6. Divisione intera mediante sottrazioni

La specifica è

$$
\{x\geq0\land y>0\}\ C\
\{x=qy+r\land0\leq r<y\},
$$

con $x,y$ non modificati dal programma.

```text
q := 0;
r := x;
while r >= y do
    q := q + 1;
    r := r - y
endw
```

Le slide propongono $Inv\equiv x=qy+r\land r\geq0$ ed $expt=r$.

*Svolgimento aggiunto.* Per rendere esplicita anche l'ipotesi usata nel progresso, manteniamo $y>0$ nell'invariante:

$$
Inv\equiv x=qy+r\land r\geq0\land y>0.
$$

**Inizializzazione.** Dopo `q := 0; r := x`, vale $x=0\cdot y+x$ e $r=x\geq0$; $y$ resta positivo.

**Invarianza.** Denotando con $q,r$ i valori prima del corpo, i nuovi valori sono $q'=q+1$ e $r'=r-y$. Allora

$$
q'y+r'=(q+1)y+(r-y)=qy+r=x.
$$

La guardia garantisce $r-y\geq0$; $y>0$ resta vero perché $y$ non cambia.

**Terminazione e progresso.** $Inv\Rightarrow r\geq0$. Se prima $r=V$, dopo $r'=V-y<V$, perché $y>0$.

**Uscita.** La guardia falsa dà $r<y$, che insieme all'invariante produce esattamente la postcondizione. Quindi $q=x\ \mathtt{div}\ y$ e $r=x\ \mathtt{mod}\ y$.

Il caso $y=0$ spiega perché la positività è essenziale: il corpo aumenterebbe $q$ senza far diminuire $r$, e il ciclo non terminerebbe.

## 7. Programmi annotati

Un [[Programma annotato|programma annotato]] rende visibili le asserzioni nei punti in cui servono per la prova:

```text
{P}
CI;
{inv: Inv} {ft: expt}
while E do
    {Inv ∧ E}
    C
endw
{Inv ∧ ¬E}
{Q}
```

Le annotazioni non sostituiscono gli obblighi di dimostrazione: servono a organizzarli (inizializzazione, preservazione, non negatività, diminuzione e implicazione finale). Le asserzioni tra i comandi di una sequenza si ricavano spesso **dal basso verso l'alto**, applicando l'[[Regola dell'assegnamento|assioma dell'assegnamento]].

## 8. Regole derivate

### 8.1 Congiunzione e disgiunzione

Per uno stesso comando $C$ si possono combinare dimostrazioni:

$$
\frac{\{P_1\}\ C\ \{Q_1\}\qquad\{P_2\}\ C\ \{Q_2\}}
     {\{P_1\land P_2\}\ C\ \{Q_1\land Q_2\}}
\quad(\mathrm{cong}),
$$

$$
\frac{\{P\}\ C\ \{Q\}\qquad\{R\}\ C\ \{Q\}}
     {\{P\lor R\}\ C\ \{Q\}}
\quad(\mathrm{disg}).
$$

La prima consente di dimostrare separatamente due proprietà dello stesso risultato; la seconda di distinguere casi nella precondizione.

### 8.2 Proprietà delle variabili non modificate

$\mathrm{change}(C)$ è l'insieme delle variabili che compaiono come destinazione di un assegnamento in $C$. È un insieme di variabili **potenzialmente** modificate: un ramo può non essere eseguito, oppure un assegnamento può lasciare il valore invariato.

Se nessuna variabile libera di $P$ può essere modificata da $C$, allora $P$ si conserva:

$$
\frac{\mathrm{free}(P)\cap\mathrm{change}(C)=\varnothing
\qquad\{R\}\ C\ \{Q\}}
{\{P\land R\}\ C\ \{P\land Q\}}
\quad(\mathrm{invariante}).
$$

Questa regola giustifica, per esempio, il fatto che $y>0$ si conservi attraverso il corpo della divisione: il corpo assegna solo a $q$ e $r$.

## Fonte e precisazioni

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 11, 26 ottobre 2026, slide 330-354, file originale `/Users/michelangelogubinelli/Downloads/Lezione_11.pdf`.
- Le dimostrazioni della somma e della divisione sono completate dove le slide propongono esercizi. Il conteggio $N!$ e le precisazioni sul ruolo delle annotazioni esplicitano il ragionamento delle slide.
- Nella slide 340 il collegamento iniziale è $P\Rightarrow Inv\land\mathrm{def}(E)$: una frase successiva contiene un refuso. Nella slide 351 la verifica dell'invarianza riguarda il **corpo**, non l'intero `while`. Nella slide 348 i triangoli utili sono $AED$ e $CEB$: $AEB$ e $CED$, nominati nel testo, sono allineati.
- Seguito: [[2026-10-27 - Verifica di programmi iterativi e introduzione agli array]].
