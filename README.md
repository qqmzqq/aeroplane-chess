# Aeroplane Chess


## File structure

```
├── README.md
├── rules
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   └── base_rules.cpython-37.pyc
│   └── base_rules.py
├── demo.py
└── utils
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   ├── chess_piece.cpython-37.pyc
    │   ├── chessboard.cpython-37.pyc
    │   └── player.cpython-37.pyc
    ├── chess_piece.py
    ├── chessboard.py
    └── player.py

```

## Chessboard

```
G G   s ◯ ◯ ◯ r ◯ ◯ ◯     R R
G G     ◯     ◉     ◯     R R
        ◯     ◉     ◯
        y - - ◉ - - y       s
◯ ◯ ◯ b       ◉       g ◯ ◯ ◯
◯     |       ◉       |     ◯
◯     |       ◉       |     ◯
g ◉ ◉ ◉ ◉ ◉ ◉   ◉ ◉ ◉ ◉ ◉ ◉ b      * * * * * * * * * * * * * * * *
◯     |       ◉       |     ◯      * '◯' -> chessboard           *
◯     |       ◉       |     ◯      * '◉' -> battlefield          *
◯ ◯ ◯ b       ◉       g ◯ ◯ ◯      * 'X' -> chess pieces         *
s       r - - ◉ - - r              * 'x' -> shift to battlefield *
        ◯     ◉     ◯              * 's' -> ready area           *
Y Y     ◯     ◉     ◯     B B      * 'x -- ◉ -- x' -> shortcut   *
Y Y     ◯ ◯ ◯ y ◯ ◯ ◯ s   B B      * * * * * * * * * * * * * * * *


chessboard：7 * 4 + 6 * 4 = 52
battlefield：6 * 4 = 24
count: 76
```

*


