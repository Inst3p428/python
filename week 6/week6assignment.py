import matplotlib.pyplot as plt 
#Practice Tasks

#Create a bar chart showing 5 different countries and their population.
countries = ['Kenya', 'Tanzania', 'Rwanda','Burundi','Djibouti']
population = [55, 67, 14, 14, 1]

plt.bar(countries, population, color='skyblue')
plt.title("Country Population")
plt.xlabel("Countries")
plt.ylabel("Population")
plt.show()
#Create a pie chart showing how a student spends 24 hours of their day.
activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
hours = [8, 2, 8, 6]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Daily Activities")
plt.show()
#Make a line chart that shows temperature changes during the day (morning, noon, evening, night).


# Sample data
day = ['morning', 'noon', 'evening', 'night']
temperatures = [17, 25, 19, 15]

# Create a line plot
plt.plot(day, temperatures)
plt.title("Simple Line Plot")
plt.xlabel("Time day")
plt.ylabel("Temperature reading")
plt.show()