# Sum Till One

Sum Till One is a road game where you summarize digits from a number again and again until there is only one lefts. STO is funny and smart till it trains your brain in arithmetical way.

## Example

```Input: 4567 \n
4 + 5 + 6 + 7 = 22
2 + 2 = 4
Output: 4
```

## Installation

Download or clone **countgame.py** to any location on your disk.

## Usage
Use CLI (Terminal, PowerShell) to find and launch **countgame.py**. After you find it, just launch it in standart way:

```console
foo@bar:~$ python .\countgame.py
Enter your number:
```

Or you can even input your parameter as an argument by launching **countgame.py**:

```console
foo@bar:~$ python .\countgame.py 8365
4
```

Don't worry if your number contains additional symbols (like - in telephone number or / in dates) till **countgame.py** can sort it automatically:

```console
foo@bar:~$ python .\countgame.py +7 (123) 456-78-90
7
```
