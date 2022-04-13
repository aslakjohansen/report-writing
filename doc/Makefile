TARGETS = \
	report-writing.pdf


all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm    ${TARGETS}

mrproper: clean
	touch d~
	rm    *~


report-writing.pdf: report-writing.tex
	pdflatex report-writing.tex
	pdflatex report-writing.tex

