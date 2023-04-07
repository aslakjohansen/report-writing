TARGETS = \
	report-writing.pdf


all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm    ${TARGETS}

mrproper: clean
	touch d~ d.aux d.bbl d.bcf d.blg d.run.xml d.log d.out d.toc d.idx d.ilg d.ind d.pyg
	rm    *~ *.aux *.bbl *.bcf *.blg *.run.xml *.log *.out *.toc *.idx *.ilg *.ind *.pyg


report-writing.pdf: report-writing.tex references.bib */*.tex
	xelatex -shell-escape report-writing.tex
	makeindex report-writing.idx
	biber report-writing.bcf
	xelatex -shell-escape report-writing.tex
	xelatex -shell-escape report-writing.tex

