from bokeh.plotting import figure, output_file, show

# örnek veriler
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# HTML çıktısı
output_file('lines.html')

p = figure(
    title = 'basit çizgi örneği',
    x_axis_label = 'x',
    y_axis_label = 'y'
)
# çizgi ekle
p.line(x, y, legend='Temp', line_width=2)

# göster
show(p)