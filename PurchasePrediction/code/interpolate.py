import matplotlib 

cmap =  matplotlib.colors.Colormap( 'jet' )

print cmap
print dir(cmap)

cmap( range(0,100) )

