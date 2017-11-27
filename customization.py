import matplotlib.pyplot as plt
from random import shuffle
from matplotlib import rcParams


#plt.style.use('seaborn-dark-palette')
rcParams['font.family'] = 'monospace'
def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

data = create_random_list(50)
border_background_color = "darkslategray"

fig, ax = plt.subplots(facecolor="darkslategray")
plt.subplot(111, facecolor='darkslategray')
plt.plot(range(len(data)), data, 'C1')

plt.xlabel('X Axis', color="#afeeee")
plt.ylabel('Y Axis', color="#afeeee")
plt.title('Title Goes Here')
plt.grid(True)




plt.show()
