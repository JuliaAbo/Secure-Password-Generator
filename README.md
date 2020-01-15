# Secure-Password-Generator
A script that generates a secure password based on this xkcd comic about secure password generation: 
https://xkcd.com/936/

##How to Use

Type ./xkcdpwgen into your command line in order to run the program. It will generate a password, by default, of four words in a string. You can specify the following commands to change the contents of the generated password.

    -h, --help            show this help message and exit
    -w WORDS, --words WORDS
                          include WORDS words in the password (default=4)
    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words
                          (default=0)
    -n NUMBERS, --numbers NUMBERS
                          insert NUMBERS random numbers in the password
                          (default=0)
    -s SYMBOLS, --symbols SYMBOLS
                          insert SYMBOLS random symbols in the password
                          (default=0)
