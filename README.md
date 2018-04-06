# slominsky_generator

Python implementation of "Equal Division of N octave into M parts" generator.

From
"Thesaurus of Scales and Melodic Patterns" , Nicolas Slonimsky

## Description

Since slonimsky book is hugely algorithmic, I was inspired to implement the algorithm in Python and music21.

Note that this program supports only "Interpolation".
"Ultrapolation","Infrapolation" are not implemented yet.

## Features

- Generates score of all possibilities of "Equal Division of N octave into M parts" scales with given parameters as arguments.

## Requirement

- Python3
- music21 ver5
- itertools

## Usage

python slonim_gen.py [total octaves] [division] [number of interpolation notes] [midi note of start]

for example

python slonim_gen.py 2 3 3 64

Parameter conditions must be below.

- ([total octaves] * 12) % [division] == 0

- (([total octaves] * 12) / [division]) > [number of interpolation notes]

generates following result.

<img src="https://raw.githubusercontent.com/wiki/delphinus1024/slominsky_generator/image/result.png" style="width: 600px;"/>

## Installation

Not needed. Just call from python3.

## Author

delphinus1024

## License

[MIT](https://raw.githubusercontent.com/delphinus1024/slominsky_generator/master/LICENSE.txt)

