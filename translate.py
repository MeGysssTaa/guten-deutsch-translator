# MIT License
#
# Copyright (c) 2019 DarksideCode
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import random


PREFIXES = [
    'das',
    'der',
    'die',
    'ein',
    'eine',
    'durch',
    'bis',
    'für',
    'ohne',
    'entlang',
    'gegen',
    'um',
    'bei',
    'mit',
    'seit',
    'aus',
    'zu',
    'nach',
    'von',
    'zwischen',
    'über'
]


SCARY_WORDS = [
    'Lebensabschnittpartner',
    'Unabhaengigkeitserklaerungen',
    'Freundschaftsbezeugung',
    'Rechtsschutzversicherungsgesellschaften',
    'Donaudampfschiffahrtsgesellschaftskapitän',
    'Siebentausendzweihundertvierundfünfzig',
    'Ezirksschornsteinfegermeister',
    'Siebenhundertsiebenundsiebzigtausendsiebenhundertsiebenundsiebzig',
    'Sozialversicherungsfachangestelltenauszubildender',
    'Weihnachtskeksdosendeckel',
    'Subatomarteilchenbeschleunigungsnaturmäßigkeitsuntersuchungsmaschine',
    'Rindfleischetikettierungsüberwachungsaufgabenübertragungsgesetz'
]


SUFFIXES = [
    'bar',
    'haft',
    'ig',
    'isch',
    'lich',
    'los',
    'reigh',
    'voll',
    't',
    'zt',
    'kt',
    'cht'
]


PUNCTUATION = ['.', ',', ':', '!', '?',' ;']


def main():
    english = input("Enter English sentence which needs to be translated in German:\n").strip().lower()
    enlen = len(english)

    if 16 <= enlen <= 10000 and ' ' in english:
        beginning = random.choice(PREFIXES)
        result = beginning[0].upper() + beginning[1:len(beginning)]
        words = english.split(' ')

        # Do the actual 'translation'
        for word in words:
            if random.random() > 0.45:
                result += ' '
                result += word[0].upper() + word[1:len(word)]

                if random.random() > 0.3:
                    result += random.choice(SUFFIXES)

                result += ' '

                if random.random() > 0.8:
                    result += random.choice(SCARY_WORDS)
                    result += ' '

                result += random.choice(PREFIXES)
            else:
                result += word

        # For the grammer nazi among us ("word1,word2" => "word1, word2")
        for punct in PUNCTUATION:
            result = result.replace(punct, punct + ' ')

        # Fix double-/triple-/n-spacing sometimes caused by the above gRaMMer FIx
        while '  ' in result:
            result = result.replace('  ', ' ')

        print("A German boi would say:")
        print("\n\"" + result + "\"\n")
    else:
        print("The sentence must be at least 16 and at most 10000 characters long and must contain spaces.")
        print("Just a normal English sentence, okay? don't break my script")


if __name__ == '__main__':
    main()
