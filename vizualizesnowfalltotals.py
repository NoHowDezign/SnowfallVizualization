import pygal

bar_chart = pygal.Line()
bar_chart.title = 'Snowfall Totals from 1900 to 2010 in Portland, ME'
bar_chart.x_labels = map(str, range(1900, 2010))
bar_chart.x_title = 'Year (1900 to 2010)'
bar_chart.y_title = 'Snowfall Total (Inches)'

snowfallFile = open('test.txt', 'r')
snowfallFileString = snowfallFile.read()
snowfallTotals = snowfallFileString.split(',')
snowfallArray = []

for i in snowfallTotals:
  print i
  snowfallArray.append(float(i))

bar_chart.add('Snowfall Totals', snowfallArray)
bar_chart.render_to_file("snowfalltotals-line.svg")
