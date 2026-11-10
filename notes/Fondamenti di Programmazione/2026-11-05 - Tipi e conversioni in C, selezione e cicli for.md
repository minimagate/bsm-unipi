---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-11-05'
title: Tipi e conversioni in C, selezione e cicli for
source: Lezione_15.pdf (slide 448-486)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-11-05 - Tipi e conversioni in C, selezione e cicli for.md
vault_hash: 2b89b2d1565e2e3edbbf3e9d8d4df110e3340c51414f98d086df7654e0d8d1f7
---

# Tipi e conversioni in C, selezione e cicli for

La lezione approfondisce i [[Tipo di dato|tipi]] semplici introdotti nella [[2026-11-03 - Introduzione al C, variabili e input-output|lezione 14]], le [[Conversione di tipo|conversioni]] fra tipi e l'[[Input e output in C|input/output]] con formato. Poi passa ai condizionali annidati, all'[[Istruzione switch|istruzione `switch`]], all'iterazione determinata e ai [[Ciclo for|cicli `for`]].

I frammenti sono codice C da mettere nel corpo di un programma, con `#include <stdio.h>` quando usano funzioni di ingresso e uscita. Salvo diversa indicazione, si assumono input validi e risultati rappresentabili nei tipi usati. Le precisazioni e le correzioni rispetto alle slide sono segnalate.

## 1. Tipi interi

Il tipo **`int`** rappresenta interi con segno in un intervallo finito. Nel caso a $n$ bit in complemento a due considerato dalle slide, l'intervallo è

$$
-2^{n-1}\leq x\leq2^{n-1}-1.
$$

Per esempio, con 32 bit si va da $-2147483648$ a $2147483647$. La dimensione effettiva dipende dall'implementazione e dalla piattaforma. I limiti si ottengono da **`INT_MIN`** e **`INT_MAX`**, definiti in `<limits.h>`.

Le operazioni introdotte sono `+`, `-`, `*`, `/`, `%` e i confronti `==`, `!=`, `<`, `>`, `<=`, `>=`. Per leggere e stampare `int` si usa `%d`.

```c
int x = 10;
int y = 3;
printf("%d %d\n", x / y, x % y);
```

produce `3 1`: **se entrambi gli operandi sono interi, `/` fa una divisione intera**. Occhio: assegnare il risultato a una variabile reale non basta per ottenere una divisione reale.

Esistono anche `short`, `long` e tipi senza segno, che le slide non approfondiscono.

## 2. Numeri in virgola mobile

### 2.1 Rappresentazione e costanti

I [[Numero in virgola mobile|numeri in virgola mobile]] approssimano i reali con precisione finita. **`float`** è il tipo base: non tutti i numeri reali sono rappresentabili esattamente. Nel caso usato dal corso occupa 4 byte, ma dimensione e caratteristiche dipendono dall'implementazione.

Si possono scrivere costanti in notazione decimale oppure scientifica:

```c
3.14
0.314E1
1234.5e-1
```

Le ultime due valgono rispettivamente $0.314\cdot10^1$ e $1234.5\cdot10^{-1}$. Il separatore decimale è il **punto**.

Una costante con il suffisso `f` o `F` ha tipo `float`; una costante floating senza suffisso, come `3.14`, ha tipo `double`:

```c
float x = 3.14f;
double y = 3.14;
```

Esistono anche `double` e `long double`, con caratteristiche proprie. *Correzione alla slide 451:* sono tipi in virgola mobile, non tipi interi.

Gli operatori aritmetici comprendono `+`, `-`, `*` e `/`; **`%` non si applica agli operandi floating**.

`<float.h>` mette a disposizione costanti come `FLT_MIN` e `FLT_MAX`. *Precisazione aggiunta:* `FLT_MIN` indica il minimo valore **positivo normalizzato**, non il valore più negativo del tipo; non esprime nemmeno la precisione.

### 2.2 Stampare valori floating

| Formato `printf` | Effetto |
|---|---|
| `%f` | Notazione decimale, normalmente con sei cifre dopo il punto |
| `%.3f` | Tre cifre dopo il punto |
| `%8.3f` | Tre cifre decimali, campo di ampiezza minima 8 |
| `%-8.3f` | Come sopra, con allineamento a sinistra |
| `%e` / `%E` | Notazione scientifica |

Per esempio:

```c
float x = 123.45f;
printf("|%f| |%8.3f| |%-8.3f|\n", x, x, x);
```

Nell'implementazione illustrata dalle slide produce

```text
|123.449997| | 123.450| |123.450 |
```

La prima stampa mostra l'approssimazione binaria del valore. Fissare tre decimali cambia solo la **rappresentazione in uscita**, non la precisione con cui il numero è memorizzato.

*Precisazione alla slide 452:* l'ampiezza è un **minimo**, non un limite che tronca il risultato. `1.234e+02` occupa già 9 caratteri: con `%8.3e` o `%-8.3e` non si aggiungono spazi per arrivare a otto, né si tagliano caratteri. Le spaziature mostrate nella slide non vanno quindi prese alla lettera.

### 2.3 Leggere valori floating

Con `scanf`, `%f` e `%e` possono leggere in un `float` sia la notazione decimale sia quella scientifica:

```c
float x, y;
scanf("%f", &x);
scanf("%e", &y);
```

Gli input `123.456` e `0.123456E+3` rappresentano lo stesso numero e vengono convertiti nello stesso tipo.

*Precisazione aggiunta, per distinguere input e output:* per leggere un `double` con `scanf` si usa `%lf`; in `printf`, invece, `%f` stampa sia un `float` sia un `double`, perché il `float` passato alla funzione viene promosso a `double`.

## 3. Caratteri e codici

Il tipo **`char`** rappresenta i caratteri tramite codici numerici. Di solito si usa ASCII o una codifica compatibile, ma non si può dare per scontato in ogni ambiente.

In ASCII, per esempio, `'0'` vale 48, `'A'` vale 65 e `'a'` vale 97. È però preferibile scrivere il carattere:

```c
char x = 'A';
char y = '\n';
char z = '#';
```

invece dei numeri `65`, `10` e `35`: il codice è più leggibile e non lega il programma a quei valori di codifica.

Gli **apici singoli** delimitano costanti carattere, gli **apici doppi** le stringhe: `'A'` e `"A"` sono cose diverse. E attenzione: **`'2'` non è il numero `2`**, è il codice del carattere che rappresenta quella cifra.

Con una codifica ASCII:

```c
int a = 'a';
printf("%c\n", a);
printf("%d\n", a);
```

stampa prima `a` e poi `97`. Lo specificatore determina come rappresentare in uscita il valore.

`sizeof(char)` vale 1 byte C e non supera `sizeof(int)`; nelle piattaforme comuni un byte contiene 8 bit. Gli operatori aritmetici sui caratteri lavorano sui loro valori numerici, con le promozioni descritte più avanti.

### 3.1 Input/output di un carattere

```c
char c;
scanf("%c", &c);
printf("%c\n", c);
```

In alternativa si possono usare

```c
int c;
c = getchar();
putchar(c);
```

`getchar` legge il prossimo carattere, `putchar` lo scrive. *Precisazione alla slide 458:* `getchar` restituisce un `int`, così può rappresentare anche il valore speciale `EOF`, che segnala la fine dell'input o un errore. L'esempio minimale assume che un carattere sia effettivamente disponibile.

## 4. Condizioni e operatori logici

Nel modello del corso `int` rappresenta anche i valori di verità: `0` è falso, ogni valore non nullo è vero. Gli operatori sono `!`, `&&` e `||` e restituiscono `0` oppure `1`.

```c
!0          /* 1 */
!5          /* 0 */
3 && 7      /* 1 */
0 || -2     /* 1 */
```

L'affermazione delle slide «non esiste un tipo booleano» va letta nel contesto del C originario: si veda la precisazione nella lezione 14.

## 5. Conversioni di tipo

Un'espressione ha sia un **valore** sia un **tipo**. Una [[Conversione di tipo|conversione di tipo]] può avvenire fra operandi, durante un assegnamento o in modo esplicito con un cast; più avanti la ritroveremo nel passaggio dei parametri e nei valori restituiti dalle funzioni.

### 5.1 Operandi di tipi diversi

Per i tipi e i casi semplici considerati dalle slide si usa lo schema

$$
\mathtt{int}\to\mathtt{long}\to\mathtt{float}
\to\mathtt{double}\to\mathtt{long\ double}.
$$

`char` e `short` subiscono prima le promozioni intere, normalmente a `int`; poi si determina un tipo comune per l'operazione. Per esempio:

```c
int x = 3;
double y = 2.5;
```

In `x + y` il valore di `x` viene convertito a `double`, si esegue la somma fra `double` e il risultato ha tipo `double`. Il tipo della **variabile** `x` resta `int`.

*Precisazione alla slide 462:* lo schema è una semplificazione per i casi trattati, non la regola completa per tutte le combinazioni in C, in particolare quelle con tipi senza segno: una promozione intera può richiedere `unsigned int` se `int` non può rappresentare tutti i valori di partenza.

### 5.2 Conversione nell'assegnamento

In `x = espressione;`, il valore dell'espressione viene convertito al tipo di `x`:

```c
int i;
float x = 2.3f, y = 4.5f;
i = x + y;
printf("%d\n", i);
```

stampa `6`. La conversione da floating a intero elimina la parte frazionaria, **troncando verso zero**, purché il valore troncato sia rappresentabile (qui $2.3+4.5=6.8$ diventa `6`).

*Precisazione alla slide 463:* anche una conversione verso un tipo floating può perdere informazione: per esempio un `float` può non rappresentare esattamente tutti i valori di un `int`. E non bisogna aspettarsi che ogni conversione fuori intervallo produca un errore segnalato dal compilatore.

### 5.3 Cast e divisione

La sintassi del cast è

```c
(tipo) espressione
```

Supponiamo `somma = 7` e `n = 2`, entrambi `int`:

```c
media = somma / n;          /* risultato della divisione: 3 */
media = (float)somma / n;   /* risultato della divisione: 3.5 */
```

Nel primo caso la divisione intera viene eseguita **prima** della conversione al tipo di `media`. Nel secondo il cast agisce su `somma` prima di `/`, quindi anche `n` viene convertito e la divisione è in virgola mobile.

Il [[Conversione di tipo|cast]] ha precedenza più alta della divisione:

```c
(float)somma / n
```

significa `((float)somma) / n`. Invece `(float)(somma / n)` converte un risultato già troncato e non recupera la parte frazionaria. In questi esempi si assume `n != 0`.

## 6. Stream e input/output con formato

La libreria standard presenta l'input e l'output testuali come **stream**, sequenze di caratteri. Il carattere `\n` delimita le righe.

All'avvio si hanno tre stream standard:

| Stream | Uso | Collegamento tipico |
|---|---|---|
| `stdin` | Ingresso | Tastiera |
| `stdout` | Uscita ordinaria | Schermo |
| `stderr` | Messaggi di errore | Schermo |

Il sistema operativo può redirigerli, per esempio verso file. Grazie alla libreria il programma lavora sempre sullo stesso modello astratto, anche quando cambia il dispositivo effettivo.

`getchar` acquisisce il prossimo carattere; `printf` converte i valori secondo il formato richiesto e scrive i caratteri risultanti. La `f` di `printf` e `scanf` sta per **formatted**.

### 6.1 Valori in uscita, indirizzi in ingresso

```c
printf("%d %f %c\n", numero, misura, carattere);
scanf("%d%f", &numero, &misura);
```

Il primo argomento è una stringa di controllo; gli altri devono corrispondere ai rispettivi specificatori. In uscita si passano valori o espressioni, in ingresso gli indirizzi di variabili del tipo richiesto.

### 6.2 Sopprimere un campo in lettura

Mettendo `*` dopo `%` si legge un campo senza assegnarlo ad alcuna variabile:

```c
int g, m, a;
scanf("%d%*c%d%*c%d%*c", &g, &m, &a);
```

Nell'esempio della slide 468 si leggono date come `07/11/2026` oppure `07-11-2026`, scartando i due separatori e un carattere finale, tipicamente il fine riga. A `%*c` **non corrisponde alcun argomento**.

*Precisazioni aggiunte:* `%*c` scarta un carattere qualsiasi, quindi non controlla che il separatore sia `/` oppure `-`. L'ultimo `%*c` richiede un carattere anche dopo l'anno. Inoltre `%c`, a differenza dei formati numerici, non salta gli spazi bianchi: un fine riga rimasto nell'input può diventare il carattere letto.

## 7. Condizionali annidati e `else if`

Per classificare una temperatura si possono disporre le condizioni in cascata:

```c
if (temperatura > 30) {
    printf("Molto caldo\n");
} else if (temperatura > 20) {
    printf("Caldo\n");
} else if (temperatura > 10) {
    printf("Gradevole\n");
} else if (temperatura > 0) {
    printf("Freddo\n");
} else {
    printf("Molto freddo\n");
}
```

| Temperatura $t$ | Messaggio |
|---|---|
| $t>30$ | Molto caldo |
| $20<t\leq30$ | Caldo |
| $10<t\leq20$ | Gradevole |
| $0<t\leq10$ | Freddo |
| $t\leq0$ | Molto freddo |

Quando si arriva a un `else`, le condizioni precedenti sono già false. Nel secondo ramo non serve riscrivere `temperatura <= 30`: è implicito nel percorso di esecuzione.

Due `if` indipendenti hanno un altro significato:

```c
if (temperatura > 30)
    printf("Molto caldo\n");
if (temperatura > 20)
    printf("Caldo\n");
```

Con `temperatura = 35` stampano **entrambi** i messaggi, mentre la cascata ne stampa uno solo.

### 7.1 A quale `if` appartiene un `else`?

Un `else` si associa all'**`if` precedente più vicino che non abbia già un `else`**, rispettando i blocchi:

```c
if (a >= 0)
    if (b >= 0)
        printf("b non negativo\n");
    else
        printf("b negativo\n");
```

L'ultimo ramo viene eseguito quando **`a >= 0` e `b < 0`**. Se `a < 0`, il frammento non stampa nulla.

Per associare l'`else` all'`if` esterno servono le graffe:

```c
if (a >= 0) {
    if (b >= 0)
        printf("b non negativo\n");
} else {
    printf("a negativo\n");
}
```

*Correzioni alla slide 472:* nel primo esempio non devono essere false entrambe le condizioni: la condizione esterna deve essere vera per raggiungere l'`if` interno. Inoltre `b >= 0` include lo zero; se si usa `a > 0`, il relativo `else` comprende anche `a == 0`. Qui messaggi e confronti sono resi coerenti.

## 8. Selezione a più vie con `switch`

L'[[Istruzione switch|`switch`]] sceglie un punto di ingresso in base al valore di un'espressione intera:

```c
switch (giorno) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        printf("Giorno lavorativo\n");
        break;
    case 6:
    case 7:
        printf("Week end\n");
        break;
    default:
        printf("Giorno non valido\n");
}
```

L'espressione viene valutata una volta, si cerca il `case` corrispondente e si parte da lì. Se nessun valore coincide si entra in `default`, se c'è; senza corrispondenza e senza `default` non viene eseguito alcun ramo.

I valori dei `case` devono essere **espressioni costanti intere**, distinte fra loro. Non si possono usare condizioni dipendenti da una variabile:

```c
/* Non valido: a < 0 non e' una costante intera. */
case a < 0:
```

Per distinguere negativo, nullo e positivo è appropriata una cascata di `if`.

*Precisazione aggiunta:* in C una variabile dichiarata `const int` non è per questo un'espressione costante intera utilizzabile come etichetta `case`, mentre una macro `#define` che si espande in un valore intero costante sì.

### 8.1 `break` e prosecuzione nei casi successivi

**Le etichette `case` non interrompono l'esecuzione.** Dopo l'ingresso si prosegue con le istruzioni successive fino a un `break` o alla fine dello `switch`. Questo comportamento si chiama **fall-through**.

Il raggruppamento `case 1: case 2:` sfrutta di proposito questa proprietà. Si può usare anche per stampare più risultati, come nell'esempio dei poligoni:

```c
switch (lati) {
    case 6: printf("esagono, ");
    case 5: printf("pentagono, ");
    case 4: printf("quadrilatero, ");
    case 3: printf("triangolo\n");
            break;
    case 2:
    case 1: printf("nessuno\n");
            break;
    default: printf("Valore non valido\n");
}
```

Con `lati = 5` si stampano pentagono, quadrilatero e triangolo. L'ordine dei casi è qui essenziale. *Normalizzazione dell'esempio della slide 478:* si usa il nome generale «quadrilatero» al posto di «rettangolo» e un messaggio di errore che copre anche gli input non positivi.

Nella slide 479 mancano invece i `break`: per `b = 3` vengono stampati «Numero primo», «Numero non primo» e «Valore non valido!». Per `b = 4` vengono stampati gli ultimi due messaggi.

C'è anche un errore indipendente: **1 non è primo**. Una versione corretta della classificazione fra 1 e 6 è

```c
switch (b) {
    case 2:
    case 3:
    case 5:
        printf("Numero primo\n");
        break;
    case 1:
    case 4:
    case 6:
        printf("Numero non primo\n");
        break;
    default:
        printf("Valore non valido!\n");
}
```

## 9. Iterazione determinata e variabili di controllo

Un'**iterazione determinata** esegue un numero di ripetizioni fissato all'ingresso nel ciclo. Il numero può essere noto già quando si scrive il programma oppure letto durante l'esecuzione.

Per stampare 100 asterischi:

```c
int i = 0;
while (i < 100) {
    putchar('*');
    i = i + 1;
}
```

`i` conta gli asterischi già stampati. All'uscita vale 100.

Per leggere $N$ interi e sommarli, con $N\geq0$:

```c
int lung, dato, somma = 0, conta = 0;
scanf("%d", &lung);
while (conta < lung) {
    scanf("%d", &dato);
    somma = somma + dato;
    conta = conta + 1;
}
printf("La somma e' %d\n", somma);
```

Per dieci interi basta fissare `lung = 10`. Le variabili `i` e `conta` sono **variabili di controllo**.

*Collegamento aggiunto con gli [[Invariante di ciclo|invarianti]]:* dopo `conta` iterazioni, `somma` è la somma dei primi `conta` dati letti e $0\leq conta\leq lung$. La funzione di terminazione è $lung-conta$. Se `lung = 0`, si stampa zero senza leggere elementi. Per lunghezze negative il codice non entra nel ciclo, ma l'input non soddisfa la specifica di una sequenza lunga $N\geq0$.

## 10. Il ciclo `for`

Il [[Ciclo for|`for`]] raccoglie in un'unica intestazione inizializzazione, guardia e aggiornamento:

```c
for (inizializzazione; guardia; aggiornamento) {
    /* corpo */
}
```

L'ordine è:

1. Eseguire l'inizializzazione una sola volta.
2. Valutare la guardia; se è falsa, uscire.
3. Eseguire il corpo.
4. Eseguire l'aggiornamento e tornare al controllo della guardia.

Per i cicli delle slide, questo equivale a

```c
inizializzazione;
while (guardia) {
    /* corpo */
    aggiornamento;
}
```

Per esempio, per stampare i numeri pari da 0 a `N` incluso:

```c
int i;
for (i = 0; i <= N; i = i + 2) {
    printf("%d ", i);
}
```

| Intestazione | Valori di `i` nel corpo |
|---|---|
| `for (i = 1; i <= 10; i = i + 1)` | $1,2,\ldots,10$ |
| `for (i = 10; i >= 1; i = i - 1)` | $10,9,\ldots,1$ |
| `for (i = -4; i <= 4; i = i + 2)` | $-4,-2,0,2,4$ |
| `for (i = 0; i >= -10; i = i - 3)` | $0,-3,-6,-9$ |

Le tre parti sono espressioni (in C anche l'assegnamento lo è). Si possono omettere, ma i **due punti e virgola restano**; se manca la guardia, è considerata vera. Le slide consigliano il `while` quando la struttura non segue il solito schema di inizializzazione, controllo e aggiornamento.

### 10.1 Massimo di dieci interi positivi

```c
int conta, dato, massimo;
massimo = 0;
for (conta = 0; conta < 10; conta = conta + 1) {
    scanf("%d", &dato);
    if (dato > massimo) {
        massimo = dato;
    }
}
printf("Il massimo e' %d\n", massimo);
```

Qui inizializzare a zero va bene perché **i dati sono positivi**. Per ammettere interi negativi qualsiasi si inizializza il massimo con il primo valore letto, come nella lezione 14.

## 11. Cicli annidati: tavola pitagorica

Il corpo di un ciclo può contenere un altro ciclo. Per stampare i prodotti da $1\cdot1$ a $10\cdot10$:

```c
int riga, colonna;
const int Nmax = 10;

for (riga = 1; riga <= Nmax; riga = riga + 1) {
    for (colonna = 1; colonna <= Nmax; colonna = colonna + 1) {
        printf("%d ", riga * colonna);
    }
    putchar('\n');
}
```

Il ciclo esterno sceglie la riga, quello interno attraversa tutte le colonne di quella riga. **`colonna = 1` viene rieseguito a ogni nuova riga.** Si stampano $10\cdot10=100$ prodotti.

L'a capo sta fuori dal ciclo interno e dentro quello esterno: viene eseguito una volta per riga, non dopo ogni prodotto.

## Fonte e precisazioni

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 15, 5 novembre 2026, slide 448-486, originale: [Lezione_15.pdf](file:///Users/michelangelogubinelli/Downloads/Lezione_15.pdf).
- Le precisazioni su limiti numerici, conversioni, `getchar`, formati di input e ampiezza dei campi evitano di estendere oltre il loro contesto le semplificazioni delle slide.
- Le correzioni degli esempi di `if` e `switch` sono esplicite; i collegamenti con invarianti e terminazione sono spiegazioni aggiunte.
- Le stringhe di stampa delle slide 481 e 485 sono normalizzate: si usa `%d`, senza la sequenza non valida `\%`, e testo ordinario al posto degli escape tipografici.
