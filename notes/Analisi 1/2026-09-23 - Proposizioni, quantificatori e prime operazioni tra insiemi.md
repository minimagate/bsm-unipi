---
type: lecture-note
course: Analisi 1
date: '2026-09-23'
title: Proposizioni, quantificatori e prime operazioni tra insiemi
source_transcript: _transcripts/Analisi 1/2026-09-23 - Proposizioni, quantificatori e prime operazioni
  tra insiemi.md
source_hash: sha256:5192cae4771ead651e830de0d25628e474de93d32564f11ce4a15e6904f1d9a1
teaching_model: anthropic/claude-opus-5.5
taught_at: '2026-09-23T14:13:25.396Z'
vault_path: Notes/Analisi 1/Lectures/2026-09-23 - Proposizioni, quantificatori e prime operazioni tra insiemi.md
vault_hash: 68d852933e04e46c963c340013efb042a902adcc7e4690a68ebb373b83d063a1
---

# Proposizioni, quantificatori e prime operazioni tra insiemi

## Collocazione nel corso di Analisi 1

Il corso è organizzato secondo una tecnica della **doppia passata**:

1. una prima passata, più generale, serve a capire quali sono gli oggetti e come si usano;
2. una seconda passata, più approfondita, serve a guardare “sotto il cofano”: definizioni, motivazioni e dimostrazioni più dettagliate.

L’idea è come imparare a guidare prima di studiare il motore: all’inizio si impara a usare volante, acceleratore e freno; dopo si va a vedere come funzionano davvero.

Il corso è diviso in quattro grandi parti:

1. **Preliminari**
   - logica elementare, insiemi e funzioni;
   - principio di induzione;
   - numeri reali e assioma di continuità;
   - funzioni elementari e grafici.
2. **Limiti**, cioè il calcolo infinitesimale.
3. **Calcolo differenziale**, in particolare lo studio di funzione.
4. **Calcolo integrale**, con integrali, equazioni differenziali e argomenti collegati.

Questa lezione è dedicata alla logica elementare e alle prime operazioni tra insiemi. Il docente chiarisce che non è un corso completo di logica: la presentazione è semplificata, ma basta come prima introduzione al linguaggio matematico.

---

## 1. Proposizioni e predicati

### 1.1 Definizione intuitiva di proposizione

Una **[[Proposizione|proposizione]]** è, informalmente, una frase di cui ha senso chiedersi se sia **vera** o **falsa**.

Esempi:

- “Oggi fa molto caldo” è una proposizione: ha senso stabilire se sia vera o falsa.
- “Il docente di Analisi 1 è giovane” è una proposizione, anche se bisognerebbe precisare cosa vuol dire “giovane”. Una volta fissato il significato, la frase è vera o falsa.
- “$7 \geq 5$” è una proposizione vera.

Non sono invece proposizioni:

- una domanda, come “Quanti siamo in aula?”;
- un comando o un’esortazione, come “Fate silenzio!”;
- in generale, una frase per cui non ha senso parlare di verità o falsità.

La logica proposizionale elementare, detta nel corso anche **logica di ordine zero**, studia proposizioni già complete, senza variabili indeterminate.

---

### 1.2 Predicati

Un **predicato** è una frase che contiene uno o più parametri (variabili) e diventa vera o falsa a seconda dei valori assegnati a questi parametri.

Esempio:

$$
x \geq 3.
$$

Questa non è ancora una proposizione, perché senza conoscere $x$ non si può dire se sia vera o falsa.

- Se $x=5$, l’enunciato $x\geq 3$ è vero.
- Se $x=1$, l’enunciato $x\geq 3$ è falso.

Sostituendo un valore alla variabile, il predicato diventa una proposizione.

Un altro esempio è:

> “Il docente $d$ è giovane”.

Il predicato dipende dal parametro $d$. Mettendo al posto di $d$ una persona concreta si ottiene una proposizione, vera o falsa.

Ci sono anche predicati con più parametri. Per esempio:

> “Allo studente $S$ piace la materia $M$”.

Si può indicare con $P(S,M)$. Il valore di verità dipende sia dallo studente sia dalla materia.

---

## 2. Quantificatori

### 2.1 Quantificare tutte le variabili

I principali **[[Quantificatore|quantificatori]]** sono:

- $\forall$, che si legge **per ogni**;
- $\exists$, che si legge **esiste almeno un**.

Il quantificatore esistenziale può essere seguito da “tale che”, che si scrive spesso così:

$$
\exists x \text{ tale che } P(x).
$$

Il “tale che” serve soprattutto a rendere la lettura più fluida e non è essenziale dal punto di vista logico.

Il punto fondamentale è questo:

> Un predicato diventa una proposizione quando tutte le sue variabili vengono:
>
> - sostituite con valori concreti, oppure
> - quantificate.

Se resta qualche variabile libera, l’espressione non è ancora una proposizione completa.

---

### 2.2 Esempi con un parametro

Consideriamo il predicato:

$$
P(x): x\geq 3,
$$

con $x\in\mathbb{R}$.

La proposizione

$$
\forall x\in\mathbb{R},\quad x\geq 3
$$

è falsa, perché per esempio $x=0$ non soddisfa la disuguaglianza.

La proposizione

$$
\exists x\in\mathbb{R}\text{ tale che }x\geq 3
$$

è vera, perché basta scegliere, ad esempio, $x=3$.

Consideriamo ora il predicato:

> “Il docente $d$ è giovane”.

La quantificazione universale produce:

$$
\forall d,\quad d\text{ è giovane}.
$$

Questa frase dice che ogni docente è giovane e, nell’esempio discusso, è falsa.

La quantificazione esistenziale produce:

$$
\exists d\text{ tale che }d\text{ è giovane}.
$$

Questa dice che esiste almeno un docente giovane, e può essere vera o falsa a seconda del contesto e di cosa si intende per “giovane”.

---

### 2.3 Esempi con due parametri

Consideriamo il predicato:

$$
P(S,B): \text{allo studente }S\text{ piace la birra }B.
$$

Disporre i quantificatori in modi diversi cambia completamente il significato.

#### Tutti gli studenti apprezzano tutte le birre

$$
\forall S\,\forall B,\quad P(S,B).
$$

In italiano:

> A ogni studente piacciono tutte le birre.

#### Esiste uno studente a cui piace almeno una birra

$$
\exists S\,\exists B,\quad P(S,B).
$$

In italiano:

> Esiste almeno uno studente a cui piace almeno una birra.

#### Ogni studente apprezza almeno una birra

$$
\forall S\,\exists B,\quad P(S,B).
$$

In italiano:

> Per ogni studente esiste almeno una birra che gli piace.

La birra può dipendere dallo studente: studenti diversi possono avere birre preferite diverse.

#### Esiste una birra apprezzata da tutti gli studenti

$$
\exists B\,\forall S,\quad P(S,B).
$$

In italiano:

> Esiste almeno una birra che piace a tutti gli studenti.

Qui la birra si sceglie una volta sola e deve andare bene per ogni studente.

#### Esiste uno studente a cui piacciono tutte le birre

$$
\exists S\,\forall B,\quad P(S,B).
$$

In italiano:

> Esiste almeno uno studente a cui piacciono tutte le birre.

#### Ogni birra piace ad almeno uno studente

$$
\forall B\,\exists S,\quad P(S,B).
$$

In italiano:

> Ogni birra piace ad almeno uno studente.

L’ordine dei quantificatori è quindi essenziale. In generale non si possono scambiare $\forall$ ed $\exists$ senza cambiare il significato dell’enunciato.

> [!warning]
> Le frasi
>
> $$
> \forall S\,\exists B\,P(S,B)
> $$
>
> e
>
> $$
> \exists B\,\forall S\,P(S,B)
> $$
>
> non dicono la stessa cosa. La prima lascia che la birra dipenda dallo studente; la seconda richiede una stessa birra gradita a tutti.

Con un predicato a due parametri, il docente osserva che si possono ottenere sei formulazioni diverse variando ordine e tipo dei quantificatori. Lascia poi come domanda il caso di un predicato con cinque parametri.

---

### 2.4 Perché si usano i quantificatori

Il formalismo matematico serve a evitare le ambiguità del linguaggio comune: i simboli non sono un vezzo, ma permettono di dire con precisione ciò che si intende.

Prima regola pratica:

> Quando si scrive un predicato, bisogna specificare i quantificatori delle variabili coinvolte, altrimenti l’enunciato resta senza un significato completo.

---

## 3. Operazioni logiche tra proposizioni

Siano $P$ e $Q$ proposizioni. Le operazioni tra proposizioni si chiamano **[[Connettivo logico|connettivi logici]]**.

### 3.1 Negazione

La negazione di $P$ si indica con:

$$
\neg P
$$

e si legge “non $P$”.

La negazione afferma esattamente l’opposto di ciò che afferma $P$.

Esempi:

- se $P$ è $7\geq 5$, allora $\neg P$ è:

  $$
  \neg(7\geq 5),
  $$

  cioè $7<5$;
- se $P$ è “il docente è giovane”, allora $\neg P$ è “il docente non è giovane”.

---

### 3.2 Congiunzione: AND

La congiunzione di $P$ e $Q$ si indica con:

$$
P\land Q.
$$

Si legge “$P$ e $Q$”.

La proposizione $P\land Q$ è vera se e solo se sono vere entrambe $P$ e $Q$.

Esempi:

- “$7\geq 5$ e $2+2=4$” è vera;
- se almeno una delle due proposizioni è falsa, la congiunzione è falsa.

Il simbolo $\land$ ricorda la lettera iniziale dell’inglese “and”.

---

### 3.3 Disgiunzione: OR inclusivo

La disgiunzione si indica con:

$$
P\lor Q.
$$

Si legge “$P$ oppure $Q$”.

In logica “oppure” è normalmente **inclusivo**: $P\lor Q$ è vera se almeno una delle due proposizioni è vera, anche se lo sono entrambe.

Quindi $P\lor Q$ è falsa soltanto quando sono entrambe false.

Il simbolo $\lor$ ricorda la lettera $V$ del latino *vel*, che indica l’“oppure” inclusivo.

Da non confondere con l’“oppure” esclusivo del linguaggio comune, dove deve essere vera una sola alternativa e non entrambe.

---

### 3.4 Leggi di De Morgan per le proposizioni

La negazione di una congiunzione è:

$$
\neg(P\land Q)\equiv \neg P\lor\neg Q.
$$

Il significato è:

> Non è vero che $P$ e $Q$ sono entrambe vere.

Cioè:

> Almeno una delle due è falsa.

Può essere falsa $P$, $Q$, oppure entrambe.

Analogamente:

$$
\neg(P\lor Q)\equiv \neg P\land\neg Q.
$$

Infatti “non è vero che almeno una delle due è vera” vuol dire che sono entrambe false. Queste due equivalenze sono le **[[Leggi di De Morgan|leggi di De Morgan]]**.

In parole:

- la negazione di un “e” diventa un “oppure” tra le negazioni;
- la negazione di un “oppure” diventa un “e” tra le negazioni.

---

## 4. Negazione dei quantificatori

Queste equivalenze sono fondamentali e le useremo spesso.

### 4.1 Negazione del quantificatore universale

La negazione di:

$$
\forall x,\quad P(x)
$$

è:

$$
\neg\left(\forall x\,P(x)\right)
\equiv
\exists x\,\neg P(x).
$$

In italiano:

> Non è vero che $P(x)$ vale per ogni $x$

equivale a:

> Esiste almeno un $x$ per cui $P(x)$ è falsa.

In simboli:

$$
\neg\left(\forall x\,P(x)\right)
\equiv
\exists x\text{ tale che }\neg P(x).
$$

Esempio:

> Tutte le pecore sono nere.

Formalmente:

$$
\forall p,\quad (p\text{ è una pecora})\Rightarrow(p\text{ è nera}).
$$

La negazione è:

> Esiste almeno una pecora che non è nera.

Non significa che nessuna pecora sia nera: basta trovarne una non nera.

---

### 4.2 Negazione del quantificatore esistenziale

La negazione di:

$$
\exists x,\quad P(x)
$$

è:

$$
\neg\left(\exists x\,P(x)\right)
\equiv
\forall x\,\neg P(x).
$$

In italiano:

> Non esiste alcun $x$ per cui $P(x)$ sia vera

equivale a:

> Per ogni $x$, $P(x)$ è falsa.

Le due regole fondamentali sono quindi:

$$
\boxed{
\neg\forall x\,P(x)\equiv\exists x\,\neg P(x)
}
$$

e

$$
\boxed{
\neg\exists x\,P(x)\equiv\forall x\,\neg P(x)
}
$$

---

### 4.3 Esempio con quantificatori annidati

Consideriamo:

$$
\forall S\,\exists B,\quad P(S,B),
$$

che significa:

> A ogni studente piace almeno una birra.

La negazione è:

$$
\neg\left(\forall S\,\exists B\,P(S,B)\right).
$$

Applicando le regole di negazione dei quantificatori:

$$
\exists S\,\forall B,\quad \neg P(S,B).
$$

In italiano:

> Esiste almeno uno studente a cui non piace nessuna birra.

L’ordine dei quantificatori cambia perché ogni negazione trasforma $\forall$ in $\exists$ e viceversa.

---

### 4.4 Esempio: uno studente che fallisce tutti gli esami ogni anno

Consideriamo l’enunciato:

> Per ogni anno esiste uno studente che fallisce tutti gli esami.

Indichiamo con $P(a,s,e)$ il predicato:

> Nell’anno $a$, lo studente $s$ fallisce l’esame $e$.

L’enunciato è:

$$
\forall a\,\exists s\,\forall e,\quad P(a,s,e).
$$

La negazione è:

$$
\exists a\,\forall s\,\exists e,\quad \neg P(a,s,e).
$$

In italiano:

> Esiste almeno un anno in cui ogni studente supera almeno un esame.

Occhio: la negazione non dice che in quell’anno tutti gli studenti superino tutti gli esami. Dice solo che ogni studente ha almeno un esame che non fallisce.

---

## 5. Implicazione

### 5.1 Definizione

L’**[[Implicazione|implicazione]]** si indica con:

$$
P\Rightarrow Q.
$$

Si legge:

> Se $P$, allora $Q$.

L’implicazione è falsa soltanto quando:

- $P$ è vera;
- $Q$ è falsa.

In tutti gli altri casi è vera.

Il significato logico è:

> Se la premessa $P$ è vera, allora la conclusione $Q$ deve essere vera.

Se $P$ è falsa, l’implicazione non impone nessuna condizione su $Q$: $Q$ può essere vera o falsa.

Per questo alcune implicazioni sembrano paradossali nel linguaggio naturale.

Per esempio:

$$
7\geq 5\Rightarrow 7<5
$$

è falsa, perché la premessa è vera e la conclusione è falsa.

Invece:

$$
2\geq 3\Rightarrow 4\geq 1
$$

è vera, perché la premessa $2\geq 3$ è falsa.

Analogamente:

$$
-5\geq 3\Rightarrow 25\geq 1
$$

è vera, perché la premessa è falsa, qualunque sia la conclusione.

> [!warning]
> Non confondere la verità di un’implicazione con la verità separata di premessa e conclusione. Un’implicazione con premessa falsa è sempre vera dal punto di vista logico.

---

### 5.2 Condizione sufficiente e condizione necessaria

L’implicazione

$$
P\Rightarrow Q
$$

si può dire in due modi equivalenti.

#### Condizione sufficiente

$P$ è una **condizione sufficiente** affinché valga $Q$.

Infatti, se $P$ è vera, questo basta a garantire che $Q$ sia vera.

#### Condizione necessaria

$Q$ è una **condizione necessaria** affinché valga $P$.

Infatti, se $P$ è vera, allora per forza $Q$ è vera.

Attenzione alla direzione:

$$
P\Rightarrow Q
$$

vuol dire che $P$ è sufficiente per $Q$, mentre $Q$ è necessaria per $P$.

Non vuol dire che $Q$ implichi $P$.

---

### 5.3 Negazione dell’implicazione

La negazione di un’implicazione è:

$$
\neg(P\Rightarrow Q)
\equiv
P\land\neg Q.
$$

Infatti $P\Rightarrow Q$ fallisce soltanto quando la premessa è vera e la conclusione è falsa.

In italiano:

> Un’implicazione è falsa quando la premessa è vera, ma la conclusione è falsa.

Questa equivalenza è molto importante:

$$
\boxed{
\neg(P\Rightarrow Q)\equiv P\land\neg Q
}
$$

---

### 5.4 Contraposizione

L’implicazione

$$
P\Rightarrow Q
$$

è equivalente alla sua **[[Contrapposizione|contraposizione]]**:

$$
\neg Q\Rightarrow\neg P.
$$

Quindi:

$$
\boxed{
P\Rightarrow Q
\equiv
\neg Q\Rightarrow\neg P
}
$$

Esempio:

> Studiare tutti i giorni implica superare l’esame.

Formalmente:

$$
\text{studio tutti i giorni}\Rightarrow\text{supero l’esame}.
$$

La contraposizione è:

> Se non supero l’esame, allora non ho studiato tutti i giorni.

$$
\text{non supero l’esame}
\Rightarrow
\text{non ho studiato tutti i giorni}.
$$

Da non confondere con:

> Se non studio tutti i giorni, allora non supero l’esame.

Quest’ultima sarebbe:

$$
\neg P\Rightarrow\neg Q,
$$

che non è equivalente a $P\Rightarrow Q$.

Si può infatti non studiare tutti i giorni e superare comunque l’esame: l’implicazione di partenza non lo esclude.

La contraposizione è alla base della **dimostrazione per assurdo** e delle dimostrazioni per contrapposizione: per dimostrare $P\Rightarrow Q$ si può dimostrare che dalla falsità di $Q$ segue la falsità di $P$.

---

## 6. Tavole di verità

Una **[[Tavola di verità|tavola di verità]]** elenca tutti i possibili valori di verità delle proposizioni coinvolte e ricava il valore dell’espressione composta.

### 6.1 Negazione

| $P$ | $\neg P$ |
|---|---|
| Vera | Falsa |
| Falsa | Vera |

### 6.2 Congiunzione

| $P$ | $Q$ | $P\land Q$ |
|---|---|---|
| Vera | Vera | Vera |
| Vera | Falsa | Falsa |
| Falsa | Vera | Falsa |
| Falsa | Falsa | Falsa |

La congiunzione è vera solo quando entrambe le proposizioni sono vere.

### 6.3 Disgiunzione inclusiva

| $P$ | $Q$ | $P\lor Q$ |
|---|---|---|
| Vera | Vera | Vera |
| Vera | Falsa | Vera |
| Falsa | Vera | Vera |
| Falsa | Falsa | Falsa |

La disgiunzione è falsa solo quando entrambe le proposizioni sono false.

### 6.4 Implicazione

| $P$ | $Q$ | $P\Rightarrow Q$ |
|---|---|---|
| Vera | Vera | Vera |
| Vera | Falsa | Falsa |
| Falsa | Vera | Vera |
| Falsa | Falsa | Vera |

L’unica riga in cui l’implicazione è falsa è quella con premessa vera e conclusione falsa.

### 6.5 Doppia implicazione

La doppia implicazione, o equivalenza, si indica con:

$$
P\Longleftrightarrow Q.
$$

È vera quando $P$ e $Q$ hanno lo stesso valore di verità.

| $P$ | $Q$ | $P\Longleftrightarrow Q$ |
|---|---|---|
| Vera | Vera | Vera |
| Vera | Falsa | Falsa |
| Falsa | Vera | Falsa |
| Falsa | Falsa | Vera |

La doppia implicazione esprime una condizione necessaria e sufficiente:

$$
P\Longleftrightarrow Q
\equiv
(P\Rightarrow Q)\land(Q\Rightarrow P).
$$

Il docente osserva inoltre che con negazione e implicazione si possono ricostruire le altre operazioni logiche. In particolare:

$$
P\Rightarrow Q
\equiv
\neg P\lor Q.
$$

> [!example] Esempio
> Verifichiamo $P\Rightarrow Q\equiv\neg P\lor Q$ riga per riga. Se $P$ è vera e $Q$ è falsa, $\neg P$ è falsa e $Q$ è falsa, quindi $\neg P\lor Q$ è falsa, come $P\Rightarrow Q$. In tutte le altre righe o $P$ è falsa (e allora $\neg P$ è vera) oppure $Q$ è vera: in entrambi i casi $\neg P\lor Q$ è vera, come l’implicazione.

---

## 7. Insiemi

### 7.1 Definizione intuitiva

Il concetto di **[[Insieme|insieme]]** non viene definito formalmente in questa lezione. Si usa l’idea intuitiva di una collezione di oggetti, detti **elementi** dell’insieme.

Un insieme si può presentare essenzialmente in due modi:

1. per elencazione degli elementi;
2. per proprietà caratteristica.

---

### 7.2 Rappresentazione per elencazione

Per elencazione si scrivono i suoi elementi tra parentesi graffe.

Esempio:

$$
A=\{2,3\}.
$$

Le parentesi graffe indicano che $A$ contiene gli elementi $2$ e $3$.

Nell’elencazione:

- l’ordine degli elementi non conta;
- un elemento ripetuto vale una volta sola.

Per esempio:

$$
\{2,3\}=\{3,2\}
$$

e

$$
\{2,2,3\}=\{2,3\}.
$$

L’insieme non è una lista ordinata: le ripetizioni non producono nuovi elementi.

---

### 7.3 Rappresentazione per proprietà

Un insieme si può definire descrivendo la proprietà che hanno i suoi elementi.

Per esempio, l’insieme degli studenti che frequentano Analisi 1 a Pisa si scrive:

$$
B=\{s:\ s\text{ è uno studente di Analisi 1 a Pisa}\}.
$$

Il simbolo “$:$” si legge “tale che”.

La scrittura indica tutti gli oggetti $s$ che soddisfano la proprietà specificata.

---

### 7.4 Esempio: i quadrati degli interi

Consideriamo l’insieme dei quadrati degli interi:

$$
A=\{n^2:n\in\mathbb{Z}\}.
$$

È una rappresentazione per proprietà: si fanno variare gli interi $n$ e si inserisce nell’insieme il valore $n^2$.

L’elenco comincia così:

$$
A=\{0,1,4,9,16,25,\ldots\}.
$$

Il valore $1$ compare sia come $1^2$ sia come $(-1)^2$, ma nell’insieme c’è una volta sola. Analogamente $4$ compare da $2^2$ e da $(-2)^2$, ma è un solo elemento.

La stessa proprietà si può scrivere in modo più esplicito:

$$
A=\{m\in\mathbb{N}:\exists a\in\mathbb{Z}\text{ tale che }m=a^2\}.
$$

Questa scrittura collega insiemi, predicati e quantificatori.

Il predicato

$$
m=a^2
$$

dipende da due parametri, $m$ e $a$.

Dopo aver quantificato $a$:

$$
\exists a\in\mathbb{Z}\text{ tale che }m=a^2,
$$

resta libero soltanto $m$. Si ottiene quindi un predicato a una variabile, cioè una proprietà di $m$.

L’insieme è formato da tutti i naturali $m$ per i quali questa proprietà è vera.

---

## 8. Operazioni tra insiemi

### 8.1 Appartenenza

La scrittura

$$
x\in A
$$

significa:

> $x$ è un elemento dell’insieme $A$.

La negazione è:

$$
x\notin A.
$$

Vuol dire che $x$ non è un elemento di $A$.

---

### 8.2 Intersezione

L’**[[Operazioni tra insiemi|intersezione]]** di due insiemi $A$ e $B$ si indica con:

$$
A\cap B.
$$

È l’insieme degli elementi che appartengono sia ad $A$ sia a $B$:

$$
A\cap B
=
\{x:x\in A\land x\in B\}.
$$

In altre parole, si prendono gli elementi comuni ai due insiemi.

---

### 8.3 Unione

L’unione di $A$ e $B$ si indica con:

$$
A\cup B.
$$

È l’insieme degli elementi che appartengono ad almeno uno dei due insiemi:

$$
A\cup B
=
\{x:x\in A\lor x\in B\}.
$$

L’“oppure” è inclusivo: un elemento che sta in entrambi gli insiemi sta comunque nell’unione.

---

### 8.4 Differenza tra insiemi

La differenza tra $A$ e $B$ si indica con:

$$
A\setminus B.
$$

È l’insieme degli elementi che appartengono ad $A$ ma non a $B$:

$$
A\setminus B
=
\{x:x\in A\land x\notin B\}.
$$

L’ordine conta:

$$
A\setminus B
\neq
B\setminus A
$$

in generale.

> [!example] Esempio
> Con $A=\{1,2,3\}$ e $B=\{2,3,4\}$ si ha $A\cap B=\{2,3\}$, $A\cup B=\{1,2,3,4\}$, $A\setminus B=\{1\}$ e $B\setminus A=\{4\}$.

---

## 9. Prodotto cartesiano

### 9.1 Definizione

Il **[[Prodotto cartesiano|prodotto cartesiano]]** di due insiemi $A$ e $B$ si indica con:

$$
A\times B.
$$

È l’insieme di tutte le coppie ordinate $(a,b)$ tali che:

$$
a\in A
\qquad\text{e}\qquad
b\in B.
$$

Formalmente:

$$
A\times B
=
\{(a,b):a\in A\land b\in B\}.
$$

Le coppie sono **ordinate**: in generale,

$$
(a,b)\neq(b,a).
$$

Il primo elemento della coppia viene da $A$, il secondo da $B$.

---

### 9.2 Esempio

Siano:

$$
A=\{3,* ,\square\},
\qquad
B=\{0,2\}.
$$

Allora:

$$
A\times B
=
\{
(3,0),(3,2),
(*,0),(*,2),
(\square,0),(\square,2)
\}.
$$

Il prodotto cartesiano si può vedere come una generalizzazione del piano cartesiano:

- la prima coordinata appartiene al primo insieme;
- la seconda coordinata appartiene al secondo insieme.

Se $A=B$ si considera $A\times A$. Anche in questo caso le coppie sono ordinate: $(a,b)$ e $(b,a)$ sono in generale diverse, anche se entrambi gli elementi appartengono allo stesso insieme.

---

## 10. Insieme delle parti

### 10.1 Definizione

Dato un insieme $A$, il suo **[[Insieme delle parti|insieme delle parti]]** è l’insieme di tutti i sottoinsiemi di $A$.

Si indica con:

$$
\mathcal{P}(A)
$$

oppure, in alcune convenzioni, con altri simboli analoghi.

Per definizione:

$$
\mathcal{P}(A)=\{B:B\subseteq A\}.
$$

Appartengono sempre all’insieme delle parti:

- l’insieme vuoto $\varnothing$;
- l’insieme $A$ stesso;
- tutti gli altri sottoinsiemi di $A$.

---

### 10.2 Esempio con tre elementi

Sia:

$$
A=\{3,*,\square\}.
$$

I suoi sottoinsiemi sono:

- il sottoinsieme con tre elementi:

  $$
  \{3,*,\square\};
  $$

- i sottoinsiemi con due elementi:

  $$
  \{3,*\},\qquad
  \{3,\square\},\qquad
  \{*,\square\};
  $$

- i sottoinsiemi con un elemento:

  $$
  \{3\},\qquad
  \{*\},\qquad
  \{\square\};
  $$

- il sottoinsieme con zero elementi:

  $$
  \varnothing.
  $$

In totale:

$$
\mathcal{P}(A)
=
\left\{
\varnothing,
\{3\},
\{*\},
\{\square\},
\{3,*\},
\{3,\square\},
\{*,\square\},
\{3,*,\square\}
\right\}.
$$

Quindi $\mathcal{P}(A)$ ha $8$ elementi.

---

### 10.3 Cardinalità dell’insieme delle parti

Se $A$ ha $n$ elementi, allora $\mathcal{P}(A)$ ha:

$$
2^n
$$

elementi.

Il motivo è che per ciascuno degli $n$ elementi di $A$ si può scegliere, indipendentemente dagli altri:

- di inserirlo nel sottoinsieme;
- di non inserirlo nel sottoinsieme.

Ci sono quindi due scelte per ogni elemento:

$$
\underbrace{2\cdot 2\cdot\ldots\cdot 2}_{n\text{ volte}}=2^n.
$$

---

### 10.4 Attenzione alla differenza tra elemento e sottoinsieme

Consideriamo ancora:

$$
A=\{3,*,\square\}.
$$

Le scritture

$$
3\in A
$$

e

$$
\{3\}\in\mathcal{P}(A)
$$

sono vere.

La prima significa che $3$ è un elemento di $A$.

La seconda significa che $\{3\}$ è un sottoinsieme di $A$, quindi un elemento dell’insieme delle parti di $A$.

Invece:

$$
3\in\mathcal{P}(A)
$$

è falsa in generale, perché $3$ non è un sottoinsieme di $A$: è un elemento di $A$.

La distinzione fondamentale è tra:

- un elemento, come $3$;
- l’insieme che contiene quell’elemento, come $\{3\}$.

---

## 11. Inclusione tra insiemi

### 11.1 Definizione

La relazione di **[[Sottoinsieme|inclusione]]** si indica con:

$$
A\subseteq B.
$$

Significa che ogni elemento di $A$ è anche elemento di $B$:

$$
A\subseteq B
\quad\Longleftrightarrow\quad
\forall x\,(x\in A\Rightarrow x\in B).
$$

L’inclusione è quindi una proposizione che riguarda due insiemi.

Non confondere:

$$
x\in A
$$

con:

$$
A\subseteq B.
$$

La prima è una relazione tra un elemento e un insieme; la seconda è una relazione tra due insiemi.

---

### 11.2 L’insieme vuoto

L’insieme vuoto è indicato con:

$$
\varnothing.
$$

Per ogni insieme $A$ vale:

$$
\varnothing\subseteq A.
$$

Infatti:

$$
\forall x\,(x\in\varnothing\Rightarrow x\in A)
$$

è vera perché non esiste alcun $x$ appartenente a $\varnothing$: per ogni $x$ l’implicazione ha premessa falsa.

L’insieme vuoto è dunque contenuto in ogni insieme.

Attenzione però alla differenza tra:

$$
\varnothing
$$

e

$$
\{\varnothing\}.
$$

- $\varnothing$ non contiene alcun elemento;
- $\{\varnothing\}$ contiene un elemento, cioè proprio l’insieme vuoto.

Pertanto:

$$
|\varnothing|=0,
\qquad
|\{\varnothing\}|=1.
$$

Inoltre:

$$
\mathcal{P}(\varnothing)=\{\varnothing\}.
$$

L’insieme delle parti dell’insieme vuoto ha un solo elemento: l’insieme vuoto stesso.

---

### 11.3 Notazioni ambigue per l’inclusione

Conviene usare notazioni non ambigue:

- $A\subseteq B$: $A$ è contenuto in $B$, con possibilità di uguaglianza;
- $A\subsetneq B$: $A$ è contenuto propriamente in $B$, quindi $A\neq B$.

Alcuni testi usano il simbolo $\subset$ in modi diversi:

- a volte come sinonimo di $\subseteq$;
- a volte solo per l’inclusione propria.

Per evitare ambiguità, meglio usare sempre:

$$
\subseteq
$$

quando si ammette l’uguaglianza, e

$$
\subsetneq
$$

quando la si esclude.

---

## 12. Convenzioni sui numeri naturali

La definizione dell’insieme dei **[[Numero naturale|numeri naturali]]** può variare:

- alcuni autori includono lo zero:

  $$
  \mathbb{N}=\{0,1,2,\ldots\};
  $$

- altri partono da $1$:

  $$
  \mathbb{N}=\{1,2,3,\ldots\}.
  $$

Non c’è un’unica convenzione universale, quindi bisogna controllare quale viene usata nel testo o nel corso.

In matematica le convenzioni e le notazioni vanno dichiarate con cura: anche piccole differenze possono portare a errori di interpretazione, come quando si confondono unità di misura diverse.
