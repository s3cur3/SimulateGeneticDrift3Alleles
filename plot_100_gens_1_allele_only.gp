set multiplot
set title "Allele Frequencies Over Time"
set xlabel "Generation"
set ylabel "Allele Frequencies"
set origin 0,0.0
set xrange [0:100]
set yrange [0.0:1.0]
set nokey # don't put the file name in the plot
set style line 1 lt 1 lw 3 pt 3 linecolor rgb "red"
set style line 11 lt 2 lw 3 pt 2 linecolor rgb "red"
set style line 111 lt 3 lw 3 pt 0.1 linecolor rgb "red"
set style line 2 lt 1 lw 3 pt 3 linecolor rgb "blue"
set style line 3 lt 1 lw 3 pt 3 linecolor rgb "green"
set style line 4 lt 1 lw 3 pt 3 linecolor rgb "black"
set style line 5 lt 1 lw 3 pt 3 linecolor rgb "yellow"
set style line 6 lt 1 lw 3 pt 3 linecolor rgb "pink"
set style line 7 lt 1 lw 3 pt 3 linecolor rgb "cyan"
set style line 8 lt 1 lw 3 pt 3 linecolor rgb "purple"
set style line 9 lt 1 lw 3 pt 3 linecolor rgb "magenta"
set style line 10 lt 1 lw 3 pt 3 linecolor rgb "orange"
plot "output/frequency_over_time0.tsv" using 1:4 w l ls 1
#plot "output/frequency_over_time0.tsv" using 1:3 w l ls 11
#plot "output/frequency_over_time0.tsv" using 1:2 w l ls 111
plot "output/frequency_over_time1.tsv" using 1:4 w l ls 2
#plot "output/frequency_over_time1.tsv" using 1:3 w l ls 2
#plot "output/frequency_over_time1.tsv" using 1:2 w l ls 2
plot "output/frequency_over_time2.tsv" using 1:4 w l ls 3
#plot "output/frequency_over_time2.tsv" using 1:3 w l ls 3
#plot "output/frequency_over_time2.tsv" using 1:2 w l ls 3
plot "output/frequency_over_time3.tsv" using 1:4 w l ls 4
#plot "output/frequency_over_time3.tsv" using 1:3 w l ls 4
#plot "output/frequency_over_time3.tsv" using 1:2 w l ls 4
plot "output/frequency_over_time4.tsv" using 1:4 w l ls 5
#plot "output/frequency_over_time4.tsv" using 1:3 w l ls 5
#plot "output/frequency_over_time4.tsv" using 1:2 w l ls 5
plot "output/frequency_over_time5.tsv" using 1:4 w l ls 6
#plot "output/frequency_over_time5.tsv" using 1:3 w l ls 6
#plot "output/frequency_over_time5.tsv" using 1:2 w l ls 6
plot "output/frequency_over_time6.tsv" using 1:4 w l ls 7
#plot "output/frequency_over_time6.tsv" using 1:3 w l ls 7
#plot "output/frequency_over_time6.tsv" using 1:2 w l ls 7
plot "output/frequency_over_time7.tsv" using 1:4 w l ls 8
#plot "output/frequency_over_time7.tsv" using 1:3 w l ls 8
#plot "output/frequency_over_time7.tsv" using 1:2 w l ls 8
plot "output/frequency_over_time8.tsv" using 1:4 w l ls 9
#plot "output/frequency_over_time8.tsv" using 1:3 w l ls 9
#plot "output/frequency_over_time8.tsv" using 1:2 w l ls 9
plot "output/frequency_over_time9.tsv" using 1:4 w l ls 10
#plot "output/frequency_over_time9.tsv" using 1:3 w l ls 10
#plot "output/frequency_over_time9.tsv" using 1:2 w l ls 10
