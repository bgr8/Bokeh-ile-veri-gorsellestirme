from bokeh.plotting import figure, output_file, show

output_file("output.html")

p = figure()
p.line(x=[1, 2, 3], y=[4,6,2])

show(p)