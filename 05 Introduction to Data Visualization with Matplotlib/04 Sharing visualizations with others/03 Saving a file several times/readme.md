## Saving a file several times

If you want to share your visualizations with others, you will need to save them into files. Matplotlib provides as way to do that, through the `savefig` method of the `Figure` object. In this exercise, you will save a figure several times. Each time setting the parameters to something slightly different. We have provided and already created `Figure` object.

**Instructions 1/3**

> Examine the figure by calling the plt.show() function.

**Instructions 2/3**

> Save the figure into the file my_figure.png, using the default resolution.

**Instructions 3/3**

> Save the figure into the file my_figure_300dpi.png and set the resolution to 300 dpi.

## Script
```
# Show the figure
plt.show()
```
```
# Save as a PNG file
fig.savefig('my_figure.png')
```
```
# Save as a PNG file with 300 dpi
fig.savefig('my_figure_300dpi.png', dpi=300)
```