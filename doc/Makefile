TARGETS = \
	report-writing.pdf


all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm    ${TARGETS}

mrproper: clean
	touch d~ d.aux d.bbl d.bcf d.blg d.run.xml d.log d.out d.toc
	rm    *~ *.aux *.bbl *.bcf *.blg *.run.xml *.log *.out *.toc


report-writing.pdf: report-writing.tex
	pdflatex -shell-escape report-writing.tex
	makeindex report-writing.idx
	biber report-writing.bcf
	pdflatex -shell-escape report-writing.tex
	pdflatex -shell-escape report-writing.tex

