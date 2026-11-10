---
type: lecture-note
course: Fondamenti di Programmazione
date: '2026-11-03'
title: Introduzione al C, variabili e input-output
source: Lezione_14.pdf (slide 406-447)
teaching_model: anthropic/claude-opus-5.5
vault_path: Notes/Fondamenti di Programmazione/Lectures/2026-11-03 - Introduzione al C, variabili e input-output.md
vault_hash: e3b9a8c812dd6f677146177ba75a88ebca25abc4b4a4ce0c7cfe3ff140dbe39e
---

# Introduzione al C, variabili e input-output

Con questa lezione inizia la seconda parte del corso: gli [[Algoritmo|algoritmi]] scritti nel linguaggio didattico vengono tradotti nel [[Linguaggio C|linguaggio C]]. Restano centrali espressioni, [[Stato|stato]], assegnamenti e controllo dell'esecuzione; diventano espliciti dichiarazioni, tipi e operazioni di ingresso e uscita.

Più avanti nel corso arriveranno array, stringhe e matrici, funzioni e passaggio dei parametri, ricorsione, puntatori e strutture dinamiche. Qui si vedono i costrutti di base. Gli esempi completi usano `int main(void)` e `return 0;`; le correzioni e le precisazioni rispetto alle slide sono segnalate.

## 1. Origini del C

Il C nasce ai Bell Labs nel contesto dello sviluppo di UNIX. Ken Thompson aveva sviluppato il linguaggio B; nel 1972 Dennis Ritchie ne elaborò un'evoluzione con tipi più ricchi e un controllo efficiente dell'hardware: il C.

Riscrivere UNIX in C ne favorì la portabilità. Efficienza e controllo a basso livello resero il linguaggio importante per la programmazione di sistemi, e la sua sintassi ha influenzato, tra gli altri, C++, Java e C#.

Le slide prendono come riferimento iniziale l'**ANSI C del 1989**, con aggiunte successive.

## 2. Espressioni e identificatori

### 2.1 Dal linguaggio didattico al C

| Operazione | Linguaggio didattico | C |
|---|---|---|
| Somma, sottrazione, prodotto | `+`, `-`, `*` | `+`, `-`, `*` |
| Divisione intera | `div` | `/` con operandi interi |
| Resto | `mod` | `%` |
| Uguaglianza | `=` | `==` |
| Diversità | `≠` | `!=` |
| Confronti d'ordine | `<`, `<=`, `>`, `>=` | `<`, `<=`, `>`, `>=` |
| Congiunzione | `and` | `&&` |
| Disgiunzione | `or` | `\|\|` |
| Negazione | `not` | `!` |
| Assegnamento | `:=` | `=` |

Occhio: **`=` modifica una variabile, `==` confronta due valori.** Per esempio, `x = 3;` assegna a `x` il valore `3`, mentre `x == 3` verifica se `x` vale `3`.

Per le condizioni si usa la convenzione:

- `0` significa **falso**;
- qualsiasi valore diverso da `0` significa **vero**;
- gli operatori logici e di confronto restituiscono `0` oppure `1`.

*Precisazione rispetto alla slide 409:* l'assenza di un tipo booleano vale per il C originario da cui si parte, non per tutte le versioni successive del linguaggio. In queste note si segue l'uso di `int` proposto dal corso.

### 2.2 Identificatori

Un identificatore è formato da lettere, cifre e underscore `_`, non può iniziare con una cifra e non può coincidere con una parola chiave, come `if` o `while`. Il C distingue maiuscole e minuscole: `somma` e `Somma` sono nomi diversi.

Sono validi `media_studente`, `x_1`, `temp`; non lo sono `media-studente` e `1x`. Conviene inoltre evitare i nomi riservati all'implementazione.

Non tutti gli identificatori denotano variabili: possono anche essere nomi di funzioni o di tipi. *Correzione alla slide 431:* `main` è il nome della funzione principale, non una parola chiave come `if` e `while`.

## 3. Assegnamenti e blocchi

La forma elementare dell'assegnamento è

```c
x = espressione;
```

Si valuta l'espressione nello stato corrente e si sostituisce il valore associato a `x`. Per esempio, `x = x + 1;` usa il vecchio valore di `x` per calcolare il nuovo.

Una sequenza di istruzioni racchiusa fra graffe costituisce un **blocco**:

```c
{
    temp = x;
    x = y;
    y = temp;
}
```

Questo blocco scambia i valori di `x` e `y`, salvando il vecchio valore di `x` in `temp`. Il blocco vuoto `{}` non esegue operazioni e corrisponde, in questo uso, a `skip`.

In breve: le graffe delimitano il blocco, i punti e virgola chiudono le singole istruzioni come gli assegnamenti.

## 4. Condizionali e cicli: il ruolo delle graffe

### 4.1 Condizionale

Le due forme sono

```c
if (guardia)
    istruzione1;
else
    istruzione2;
```

```c
if (guardia)
    istruzione;
```

Nella seconda forma, se la guardia è falsa non succede nulla. Per calcolare il massimo di due valori:

```c
if (x > y) {
    m = x;
} else {
    m = y;
}
```

**Senza graffe, il ramo comprende una sola istruzione**, qualunque sia l'indentazione. Confrontiamo:

```c
if (x > y) {
    max = x;
    min = y;
}
```

```c
if (x > y)
    max = x;
min = y;
```

Nel secondo frammento `min = y;` viene eseguita sempre. Nel primo viene eseguita soltanto se `x > y`.

### 4.2 Iterazione `while`

Il [[Comando iterativo|`while`]] in C ha questa forma:

```c
while (guardia) {
    /* corpo */
}
```

La guardia viene controllata **prima** di ogni esecuzione del corpo; se è falsa al primo controllo, il corpo non viene eseguito.

```c
while (b > 0) {
    c = c + a;
    b = b - 1;
}
```

Per `b` inizialmente positivo, il decremento porta alla terminazione. Se si omettono le graffe:

```c
while (b > 0)
    c = c + a;
b = b - 1;
```

il decremento è fuori dal ciclo: `b` resta positivo durante tutto il corpo e il programma non arriva mai all'istruzione che dovrebbe farlo diminuire. Nel modello dell'esempio è questo il motivo per cui il ciclo non si ferma; nel C concreto bisogna poi tenere conto anche dei limiti dei tipi numerici.

Nel linguaggio didattico i confini erano segnati da `then`, `fi`, `do` ed `endw`. In C sono le istruzioni singole e i blocchi a stabilire dove finiscono i rami e il corpo.

## 5. Il primo programma completo

```c
#include <stdio.h>

int main(void)
{
    /* Stampa un messaggio sullo schermo. */
    printf("Ciao mondo!\n");
    return 0;
}
```

- **`#include <stdio.h>`** rende disponibili le dichiarazioni delle funzioni standard di ingresso e uscita, tra cui `printf` e `scanf`. È una direttiva di preprocessamento, non un'istruzione eseguita dal programma.
- **`main`** è la funzione da cui parte l'esecuzione dei programmi considerati nel corso. Le graffe ne delimitano il corpo.
- **`/* ... */`** delimita un commento: utile a chi legge, ignorato durante la traduzione. Un commento non chiuso è un errore.
- **`printf`** scrive il testo richiesto. La sequenza `\n` rappresenta il carattere di fine riga.
- **`return 0;`** conclude `main` segnalando il successo al sistema operativo.

*Precisazione di sintassi:* nelle slide compare anche la forma abbreviata `main()`. Qui il tipo di ritorno `int` è sempre esplicito, e `void` nella lista dei parametri indica che la funzione non riceve argomenti. Così gli esempi restano completi anche rispetto al riferimento ANSI C iniziale.

Chiamate consecutive a `printf` continuano a scrivere dal punto raggiunto dalla chiamata precedente, senza andare a capo da sole:

```c
printf("Ciao");
printf(" mondo!\n");
```

produce la stessa riga del primo programma. Invece

```c
printf("Ciao");
printf("mondo!\n");
```

produce `Ciaomondo!`, mentre `printf("Ciao\n");` seguito da `printf("mondo!\n");` produce due righe. Questi sono gli svolgimenti delle varianti proposte nella slide 425.

## 6. Variabili, dichiarazioni e memoria

Una [[Dichiarazione di variabile|variabile]] è descritta da **nome, tipo, valore e indirizzo**. Il nome la identifica nel codice, il tipo determina i valori rappresentabili e le operazioni ammesse, il valore può cambiare, l'indirizzo individua la memoria occupata.

Le slide usano l'analogia della scatola: il nome è l'etichetta, il valore è il contenuto, il tipo dice che cosa ci può stare, l'indirizzo è la posizione. Per una data variabile tipo e indirizzo restano fissi per tutta la sua vita; il valore invece si può cambiare.

### 6.1 Dichiarare prima di usare

```c
int base;
int altezza;
int area;
float temperatura;
```

Le dichiarazioni permettono al compilatore di conoscere gli identificatori e i loro tipi. Se si dichiara `alfa` e poi si scrive `alba = alfa + 1;`, il nome `alba`, mai dichiarato, viene segnalato prima ancora dell'esecuzione.

Nello schema del corso, il corpo di `main` ha prima la parte dichiarativa e poi quella esecutiva.

Variabili dello stesso tipo possono essere dichiarate insieme:

```c
int base, altezza, area;
int x = 0;
int a, b, z = 0;
```

Nell'ultima dichiarazione è inizializzata **solo `z`**.

### 6.2 Dichiarazione e inizializzazione sono diverse

```c
int base;
```

dichiara una variabile locale, ma non le dà un valore iniziale utilizzabile. Bisogna scriverle un valore prima di leggerla, per esempio con `base = 3;` oppure con una lettura riuscita di `scanf`.

*Precisazione alla slide 432:* il valore di una variabile locale automatica non inizializzata è **indeterminato**. Non va trattato come un numero casuale su cui fare calcoli. Il discorso riguarda le variabili locali degli esempi, non tutte le categorie di variabili in C.

### 6.3 Primi tipi numerici

`int` rappresenta interi in un intervallo finito; `float` rappresenta numeri in [[Numero in virgola mobile|virgola mobile]], con precisione finita. Per esempio:

```c
int numero = 12;
float temperatura = 25.378f;
```

Le dimensioni effettive dipendono dall'implementazione; le slide citano il caso comune di `int` a 32 bit. Nota bene: `int` non è l'insieme matematico $\mathbb Z$.

## 7. Costanti simboliche: `const` e `#define`

Con `const` si dichiara una [[Costante simbolica|costante simbolica]], cioè un oggetto il cui valore non si può modificare con un assegnamento:

```c
const float PiGreco = 3.14f;
const int N = 100;
```

Il nome simbolico rende il codice più leggibile e permette di cambiare un parametro in un solo punto:

```c
area_cerchio = PiGreco * raggio * raggio;
```

Un'altra possibilità è una macro del preprocessore:

```c
#define Nmax 10
```

Il preprocessore sostituisce gli usi della macro con il testo associato prima della compilazione. La direttiva non termina con `;`.

La differenza concettuale è che **`const` dichiara un oggetto con un tipo**, mentre **`#define` definisce una sostituzione di testo**: la macro non è di per sé una variabile con una propria area di memoria.

## 8. Input e output con `scanf` e `printf`

In C l'ingresso e l'uscita ([[Input e output in C|input e output]]) passano da **funzioni di libreria**, non da comandi speciali del linguaggio.

### 8.1 Leggere un intero

```c
scanf("%d", &x);
```

`%d` chiede di convertire un numero decimale in un `int`; `&x` fornisce l'**indirizzo di `x`**, dove la funzione deve scrivere il risultato. Se la conversione riesce, il vecchio valore di `x` viene sostituito.

Quindi anche la lettura, come l'assegnamento, modifica lo stato. Gli esempi assumono che l'input sia corretto e rappresentabile nel tipo richiesto; la chiamata da sola non garantisce che l'utente rispetti questa ipotesi.

### 8.2 Stampare valori

```c
printf("Area: %d\n", area);
printf("Base: %d, altezza: %d\n", base, altezza);
```

A ogni specificatore deve corrispondere un argomento adatto, nello stesso ordine. `printf` riceve i **valori** da stampare; `scanf` riceve gli **indirizzi** delle variabili da riempire.

Stampare rende visibile una parte dello stato senza cambiare i valori delle variabili stampate.

### 8.3 Esempio completo: area del rettangolo

```c
#include <stdio.h>

int main(void)
{
    int base, altezza, area;

    printf("Immetti base del rettangolo e premi INVIO\n");
    scanf("%d", &base);
    printf("Immetti altezza del rettangolo e premi INVIO\n");
    scanf("%d", &altezza);
    area = base * altezza;
    printf("Area: %d\n", area);
    return 0;
}
```

Con input `5` e `4` si ottiene `Area: 20`. Per leggerlo come calcolo geometrico si assumono dimensioni non negative, e il prodotto deve essere rappresentabile come `int`.

## 9. Massimo di una sequenza senza memorizzarla

Data una sequenza di lunghezza nota $N\geq1$, si legge il primo elemento direttamente in `max`, poi gli altri uno alla volta in `corr`, aggiornando il massimo quando serve. Non c'è bisogno di conservare tutti gli elementi in un [[Array|array]].

```c
#include <stdio.h>
#define N 10

int main(void)
{
    int i = 1;
    int corr, max;

    printf("Introduci il primo intero della sequenza\n");
    scanf("%d", &max);
    while (i < N) {
        printf("Introduci il prossimo intero della sequenza\n");
        scanf("%d", &corr);
        if (corr > max) {
            max = corr;
        }
        i = i + 1;
    }
    printf("Il massimo e': %d\n", max);
    return 0;
}
```

**Correzione alla slide 444:** con `i = 1` e una lettura già effettuata, la guardia deve essere `i < N`. La guardia stampata `i <= N` esegue altre $N$ letture e porta il totale a $N+1$.

*Spiegazione aggiunta con il metodo degli [[Invariante di ciclo|invarianti]].* All'inizio di ogni controllo, `i` è il numero degli elementi già letti e `max` è il loro massimo:

$$
1\leq i\leq N,
\qquad
max=\max\{a_1,\ldots,a_i\}.
$$

Il corpo legge $a_{i+1}$, aggiorna il massimo e incrementa `i`. La quantità $N-i$ diminuisce di uno. All'uscita `i = N` e il massimo riguarda l'intera sequenza. Se $N=1$, non si entra nel ciclo.

Inizializzare `max` al primo elemento funziona anche se tutti i numeri sono negativi; inizializzarlo a zero richiederebbe invece un'ipotesi in più sui dati.

## 10. Tipi semplici, tipi strutturati e `sizeof`

Un [[Tipo di dato|**tipo di dato**]] specifica un insieme di valori, le operazioni ammesse e una rappresentazione in memoria. I tipi permettono di ragionare sui dati senza occuparsi ogni volta della codifica binaria e consentono alcuni controlli prima dell'esecuzione.

- Un **tipo semplice** rappresenta un valore logicamente indivisibile, come un intero o un carattere.
- Un **tipo strutturato** aggrega componenti, come un array, una matrice o una data composta da giorno, mese e anno.

Il C offre tipi predefiniti e meccanismi per costruirne di nuovi.

```c
sizeof(int)
sizeof(float)
sizeof(char)
```

indicano lo spazio occupato dai rispettivi tipi, misurato in byte C. **`sizeof` è un operatore, non una funzione** (correzione alla slide 447).

> [!example] Esempio
> Un tipo strutturato per una data può raggruppare tre `int`, per giorno, mese e anno: `sizeof` di quella struttura sarà (almeno) la somma dello spazio dei tre campi, mentre un `int` da solo è un tipo semplice.

## Fonte e collegamenti

- Paolo Mancarella, *Fondamenti di Programmazione*, Lezione 14, 3 novembre 2026, slide 406-447, originale: [Lezione_14.pdf](file:///Users/michelangelogubinelli/Downloads/Lezione_14.pdf).
- Precedente: [[2026-10-29 - Aggiornamento degli array e tecniche di costruzione dei cicli]].
- Seguito: [[2026-11-05 - Tipi e conversioni in C, selezione e cicli for]].
- Le precisazioni sui booleani, su `main`, sull'inizializzazione e su `sizeof`, la correzione del ciclo del massimo e la sua lettura tramite invariante sono esplicitate nelle rispettive sezioni.
