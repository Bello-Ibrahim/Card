# L15 Exploring Data with Charts

Course: AI-11 · Module: M3 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
A table of 1,700 numbers hides its patterns. A chart can show a gap, a cluster or a strange point in a few seconds. Charts are not only for final reports; they are one of the fastest ways to explore and check data.

## Explanation
pandas can draw charts directly from a DataFrame with `.plot()`. It uses **matplotlib** underneath, which Colab has installed. Three chart types cover most exploration:

- **Histogram** (`kind="hist"`): shows the **distribution** of one number column: which values are common, which are rare, and whether there are gaps or extreme values. `bins` sets the number of bars.
- **Bar chart** (`kind="bar"`): **compares** a number across categories, such as GDP per person by country in one year.
- **Scatter plot** (`kind="scatter"`): shows the **relationship** between two number columns. Each dot is one row. If the dots rise from left to right, the two values tend to rise together.

When you read a chart, look for four things: the general **pattern** (the trend or shape), **clusters** (groups of points), **gaps** (ranges with no data) and **outliers** (points far from the rest). Then ask whether a pattern could come from the way the data was collected rather than from the real world.

A chart is only useful if a reader understands it without asking you. Every chart needs a **title**, **axis labels with units**, and a note of the data source. When values cover a very wide range, such as income, a **log scale** spaces 1,000, 10,000 and 100,000 evenly, so small values are not squeezed into one corner.

A chart shows that two things move together. It does not show that one causes the other.

**Analogy:** Exploring a table without charts is like reading a list of the heights above sea level of 1,000 points on a map. The numbers are all there, but you will not see the mountain. A chart is the map drawn from those numbers: the shape appears at once, and you know where to look more closely.

## Worked Example
Rafael is preparing a teaching session for secondary-school teachers in Lisbon, Portugal. He uses the invented practice sample from L11 to show three kinds of chart.

The presenter runs the L11 sample cell, then:

```python
import matplotlib.pyplot as plt

ax = df["lifeExp"].plot(kind="hist", bins=6, title="Life expectancy (practice sample)")
ax.set_xlabel("Life expectancy (years)")
plt.show()
```

The histogram shows two groups: several values between about 55 and 64, and several between about 68 and 79, with few values in between.

```python
latest = df[df["year"] == 2007]
ax = latest.plot(kind="bar", x="country", y="gdpPercap", legend=False,
                 title="GDP per person, 2007 (practice sample)")
ax.set_ylabel("GDP per person (US$)")
plt.show()
```

The bar chart shows Chile far above the other five countries.

```python
ax = df.plot(kind="scatter", x="gdpPercap", y="lifeExp", logx=True,
             title="Richer countries, longer lives?")
ax.set_xlabel("GDP per person (log scale)")
ax.set_ylabel("Life expectancy (years)")
plt.show()
```

The dots generally rise from left to right. But three points sit high on the left: Vietnam has life expectancy above 70 with GDP per person below 2,500. Rafael notes this as a question for further reading, not a conclusion. He also reminds the teachers that these are invented practice numbers, and that the full dataset must be used for real statements.

## Common Mistake
Beginners often choose a chart because it looks attractive, not because it fits the question. A line chart connecting countries in alphabetical order suggests a trend that does not exist. Pick the chart by the question: distribution means a histogram, comparison means a bar chart, relationship means a scatter plot. A second mistake is leaving the default labels, such as "gdpPercap" with no unit, which forces the reader to guess.

## Key Takeaways
1. Use a histogram for a distribution, a bar chart for comparing categories, and a scatter plot for a relationship between two numbers.
2. Read each chart for patterns, clusters, gaps and outliers, and remember that moving together does not prove cause.
3. Give every chart a clear title, axis labels with units, and the data source.

## Hands-on Exercise
**Task:** Make 3 labelled charts from the Gapminder data and write one sentence of insight under each chart.
**Tools:** Google Colab (free) with pandas and matplotlib; the practice sample or the full Gapminder data.
**Steps:**
1. Load the data (L11).
2. Make a histogram of one number column. Try 2 different `bins` values and keep the clearer one.
3. Make a bar chart comparing one value across countries or continents for a single year.
4. Make a scatter plot of two number columns. Try `logx=True` for GDP per person.
5. Give each chart a title and axis labels with units.
6. Under each chart, add a text cell with one sentence of insight, for example "In this sample, life expectancy values form two groups: one below about 64 years and one above about 68 years."
**What good looks like:** Three different chart types, each with a title and labelled axes, and three insight sentences that describe what the chart shows without claiming a cause.
**Time:** about 25 minutes

## Review Flags
- [VERSION] pandas plotting options (kind, bins, logx, legend, title) and matplotlib behaviour can differ between library versions; check them in the current Colab runtime. Code was tested with pandas 3.0.6 and matplotlib 3.11.2.
- [VERIFY] Gapminder data source, access method and licence (carried from L11). The practice sample values are invented.
