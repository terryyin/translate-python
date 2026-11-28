"""
translate_po.py

CLI utility to add machine translations to localised message catalogues (messages.po)
produced by the native Python `gettext` localisation library.

Usage:

translate-po -I "locales/fr/LC_MESSAGES/messages.po" -P mymemory

For help, type:

translate-po -h

Edit the `messages.po.temp` output file as required and then rename to `messages.po`.

The `messages.po` text file must then be compiled to create the final `messages.mo`
runtime binary file.

See https://docs.python.org/3/library/gettext.html and https://babel.pocoo.org/en/latest/ 
for further guidance.

May provide a reasonable 'first pass' but will invariably require refinement.
Pay particular attention to:
- Strings containing Python braces {}.
- Strings containing abbreviations/truncations, acronyms and jargon.
- Noun/verb transpositions.

***************************************************************************
NB: excessive use is likely to result in a "Too many requests" error and/or
possible IP ban by the translation provider !!!
***************************************************************************

Created by semuadmin on 16 Nov 2026.
"""

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from time import sleep
from types import NoneType
from translate.translate import Translator


DELAY = 0.01
URL = "https://github.com/terryyin/translate-python"
COPYRIGHT = "\u00a9 2026 Terry Yin / Steve Smith - MIT License"
VERSION = "0.1.0"


def _convert(translator: Translator | NoneType, msg: str) -> str:
    """
    Translate string.
    """

    if translator is None:
        return msg
    return translator.translate(msg)


def _getstring(line: str) -> str:
    """
    Extract string from line.
    """

    return line.split('"')[1]


def process(**kwargs):
    """
    Process input file.
    """

    infile = kwargs.get("infile", "messages.po")
    provider = kwargs.get("provider", "mymemory")
    secret = kwargs.get("secret", "")
    outfile = infile + ".temp"
    translator = None
    count = 0
    locale = ""
    source = ""
    dest = ""
    status = ""

    print(f"Processing {infile} ...")

    with open(outfile, "w", encoding="utf-8") as fileout:
        with open(infile, "r", encoding="utf-8") as filein:
            for line in filein:
                ln = line
                if line[0:11] == '"Language: ':
                    locale = line[11:13]
                    translator = Translator(
                        from_lang="en", to_lang=locale, provider=provider, secret=secret
                    )  # nosec
                elif line[0:7] == 'msgid "':
                    status = "from"
                elif line[0:8] == 'msgstr "':
                    status = "to"
                if status == "from":
                    source += _getstring(line)
                elif status == "to":
                    dest = _convert(translator, source)
                    print(f"{source} {dest}")
                    ln = f'msgstr "{dest}"\n'
                    source = ""
                    status = ""
                fileout.write(ln)
                fileout.flush()
                count += 1
                sleep(DELAY)

    print(f" {locale=} - {count} lines written to {outfile}")


def main():
    """
    CLI entry point.
    """

    ap = ArgumentParser(
        epilog=f"\033[1m\033[91m{COPYRIGHT} - {URL}\033[0m",
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="Machine translation utility for localised message catalogues (messages.po)",
    )
    ap.add_argument("-V", "--version", action="version", version="%(prog)s " + VERSION)
    ap.add_argument(
        "-I",
        "--infile",
        help="Fully-qualified path to input messages.po file",
        required=True,
    )
    ap.add_argument(
        "-P",
        "--provider",
        help="Name of translation provider",
        default="mymemory",
    )
    ap.add_argument(
        "-S",
        "--secret",
        help="Secret passphrase required by translation provider",
        default="",
    )

    process(**vars(ap.parse_args()))


if __name__ == "__main__":

    main()
