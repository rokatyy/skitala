# skitala
Attack option not finished yet.
USAGE:
      encoding: -e <string> -f <file> -n <n>
      
      decoding: -d <string> -f <file> -n <n>
      
      attack: -a <string> -f <file> -n <minimum n> -m <maximum n>
For example:

for encoding text from file:
	./skitala_shifr -e -f 1.txt -n 3
for decoding text from file:
	./skitala_shifr -d -f 1.txt -n 3
for encoding text from string:
	./skitala_shifr -e "Hello" -n 3
for decoding text from string:
	./skitala_shifr -d "Hello" -n 3


