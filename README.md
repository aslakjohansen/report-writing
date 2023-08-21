# Report Writing and Friends

The is a guide to Software Engineering and Software Technology students starting on their BSc/MSc project. It is a work in progress, and the progress is spread very unevenly.

## Dependencies

For building you will need:
- xelatex (with a number of fairly standard packages)
- biber
- the [functional](https://ctan.org/pkg/functional) latex package (just copy `functional.sty` to [doc](doc))
- make
- python 3

On Debian, this includes (at least) the following packages: `biber`, `fonts-firacode`, `texlive-bibtex-extra`, `texlive-lang-cjk`, `texlive-science`, `python3`, `texlive-xetex`

## Building

```shell
cd doc ; make
```

