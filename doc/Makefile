TARGETS = \
	report-writing.pdf

DEPS = \
	generated/tabulardata.tex \


all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm    ${TARGETS}

mrproper: clean
	touch d~ d.aux d.bbl d.bcf d.blg d.run.xml d.log d.out d.toc d.idx d.ilg d.ind d.pyg
	rm    *~ *.aux *.bbl *.bcf *.blg *.run.xml *.log *.out *.toc *.idx *.ilg *.ind *.pyg


generated/tabulardata.tex: ../src/tabulardata.py ../var/tabulardata.json
	../src/tabulardata.py ../var/tabulardata.json generated/tabulardata.tex


report-writing.pdf: report-writing.tex references.bib */*.tex ${DEPS}
	xelatex -shell-escape report-writing.tex
	makeindex report-writing.idx
	biber report-writing.bcf
	xelatex -shell-escape report-writing.tex
	xelatex -shell-escape report-writing.tex

