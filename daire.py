from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("line.html")

p = figure(
    title = 'basit daire',
    plot_width=400, 
    plot_height=400,
    x_axis_label = 'x',
    y_axis_label = 'y'
)

# add a circle renderer with a size, color, and alpha
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

# show the results
show(p)