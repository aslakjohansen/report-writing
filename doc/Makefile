TARGETS = \
	report-writing.pdf


all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm    ${TARGETS}

mrproper: clean
	touch d~ d.aux d.log d.out d.toc
	rm    *~ *.aux *.log *.out *.toc


report-writing.pdf: report-writing.tex
	pdflatex report-writing.tex
	pdflatex report-writing.tex

