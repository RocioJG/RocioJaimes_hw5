Resultados_hw5.pdf: DispersionRC.pdf
Resultados_hw5.pdf: HistogramaR.pdf
Resultados_hw5.pdf: HistogramaC.pdf
Resultados_hw5.pdf: Q_max.pdf
Resultados_hw5.pdf: Hist_r1.pdf
Resultados_hw5.pdf: optimo1.pdf
Resultados_hw5.pdf: optimo.pdf
Resultados_hw5.pdf: Hist_r1.pdf
Resultados_hw5.pdf: Hist_r.pdf
Resultados_hw5.pdf: Hist_y1.pdf
Resultados_hw5.pdf: Hist_y.pdf
Resultados_hw5.pdf: Hist_x1.pdf
Resultados_hw5.pdf: Hist_x.pdf
optimo1.pdf: plots_canal_ionico.py
	python plots_canal_ionico.py
optimo.pdf: plots_canal_ionico.py
	python plots_canal_ionico.py
Hist_x.pdf: plots_canal_ionico.py
	python plots_canal_ionico.py
Hist_y.pdf: plots_canal_ionico.py
	python plots_canal_ionico.py
Hist_r.pdf: plots_canal_ionico.py
	python plots_canal_ionico.py
Hist_x1.pdf: plots_canal_ionico.py
	python plots_canal_ionico.py
Hist_y1.pdf: plots_canal_ionico.py
	python plots_canal_ionico.py
Hist_r1.pdf: plots_canal_ionico.py
	python plots_canal_ionico.py
plots_canal_ionico.py: Resultados_hw5.tex
	./a.out > Resultados_hw5.tex
Resultados_hw5.tex: ./a.out
	gcc canales_ionicos.c -lm
Q_max.pdf: circuitoRC.py
	python circuitoRC.py
HistogramaC.pdf: circuitoRC.py
	python circuitoRC.py
HistogramaR.pdf: circuitoRC.py
	python circuitoRC.py
DispersionRC.pdf: circuitoRC.py
	python circuitoRC.py