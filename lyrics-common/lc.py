"""
This program reads text files and finds common works, 2-word phrases, 3-word
phrases etc., up to a limit of 5 by default, but that can be set by the
user on the command line. It's original purpose is to read song lyrics, so
it only considers phrases made up of words on the same line.
"""

import argparse
import os.path
import sys
import re


def _parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--max-length", dest="max_len", default=5, help="Maximum phrase length to check")
    parser.add_argument("fnames", nargs="+")
    return parser.parse_args()


def _read_file(fname):
    if not(os.path.exists(fname)):
        raise FileNotFoundError("The input file {} does not exist.".format(fname))
    with open(fname) as f:
        lines = [s.strip() for s in f.readlines()]
    return lines


def _words(line):
    cleaned = line.lower()
    cleaned = re.sub("[^ a-z0-9]+", "", cleaned)
    return re.split("\s+", cleaned)


def _phrases(n, words):
    phrases = set()
    end = len(words) - n + 1
    for i in range(end):
        phrases.add(" ".join(words[i: (i + n)]))
    return phrases


def _common_phrases(all_phrases):
    ns = len(all_phrases)
    if ns == 0:
        return set()
    s = set(all_phrases[0])
    for i in range(1, ns):
        s = s & all_phrases[i]
    return s


def main(args):
    try:
        songs = [_read_file(fname) for fname in args.fnames]
        words = [[_words(line) for line in song] for song in songs]

        nsongs = len(songs)
        nlines = [len(song) for song in songs]

        for n in range(1, args.max_len + 1, 1):
            length_phrases = list()
            for s in range(nsongs):
                song_phrases = set()
                for i in range(nlines[s]):
                    song_phrases.update(_phrases(n, words[s][i]))
                length_phrases.append(song_phrases)

            common = _common_phrases(length_phrases)
            print("Phrases of length {}".format(n))
            for phrase in common:
                print(phrase)
            print()
            print()
    except Exception as e:
        print("Error: " + e.msg, file=sys.stderr)


if __name__ == "__main__":
    print(" ".join(sys.argv), file=sys.stderr)
    args = _parse_command_line()
    main(args)
