# we will look into data visualization - explore data 

import matplotlib.pyplot as plt

year = [1950,1970,19790,2010]
pop = [2.519,3.692,5.263,6.972]

plt.plot(year, pop)
plt.savefig("line-pop_year.png")

# above we have created a linegraph we then proceed to create a scatter plot below nd all that changes is the 
plt.scatter

year = [1950,1970,19790,2010]
pop = [2.519,3.692,5.263,6.972]

plt.scatter(year, pop)
plt.savefig("scatter-pop_year.png")

# we can then use plt.show() to view the created plots 

# HISTOGRAM
# this will mostly help us see the distribution of data 
# we can use this command to see more about the histogram help(plt.hist)
# if we dont specify the bin by default its 10


# CUSTOMIZATION
# different plot types - we can make a lot of customizations 
# The choice depends on the data and story we want to tell
# some info is important - we label the axis 

plt.xlabel("Year")
plt.ylabel("population")

# we can add the title
plt.title("World population projections")

# we can add customization to edit ticks 
plt.yticks([0,2,4,6,8,10])
# to make the label more understandable we can add anotehr argument on the ytick
plt.yticks([0,2,4,6,8,10], ["0","2B","4B","6B","8B","10B"])

# smaple code of some good customization 

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c =col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()