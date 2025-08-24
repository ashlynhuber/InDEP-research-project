import matplotlib.pyplot as plt
import score.BRCA

top_n = 20
highlight = scores.head(top_n)
colors = ['red' if kd else 'gray' for kd in highlight['Known_Driver']]

plt.bar(highlight.iloc[:,0], highlight['score'], color=colors)
plt.xticks(rotation=90)
plt.ylabel("Score")
plt.title("Top BRCA Predicted Drivers (Red = Known in CGC)")
plt.show()
