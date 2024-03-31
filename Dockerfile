FROM debian:12.2

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q && \
    apt-get install -y -qq --no-install-recommends \
        make \
        inkscape \
        perl \
        python3 \
        python3-pygments \
        wget \
        biber \
        fonts-firacode \
        texlive-bibtex-extra \
        texlive-lang-cjk \
        texlive-lang-chinese \
        texlive-science \
        texlive-xetex

RUN mkdir /workdir
RUN mkdir /workdir/doc
WORKDIR /workdir/doc

