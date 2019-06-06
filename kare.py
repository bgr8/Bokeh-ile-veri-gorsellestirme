from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("kare.html")

p = figure(
    title = 'basit kare',
    plot_width=400, 
    plot_height=400,
    x_axis_label = 'x',
    y_axis_label = 'y'
)

# add a square renderer with a size, color, and alpha
p.square([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="olive", alpha=0.5, legend="Örnek")

# show the results
show(p)