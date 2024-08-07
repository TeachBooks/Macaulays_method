import matplotlib.pyplot as plt

plt.figure(figsize=(3,3))
plt.plot([-1,0,0,1],[0,0,1,1])
plt.xlabel('$x$',loc='right')
plt.ylabel('$q$')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['top'].set_position('zero')
ax.xaxis.set_label_position('top')
ax.xaxis.set_ticks_position('top')
ax.axis('equal')
plt.xlim(-1,1)
plt.ylim(0,1)
# set label of xtick to \bar x
plt.xticks([0],['$\\bar x$'],)
plt.yticks([0,1])
# flip y axis
ax.invert_yaxis()
box = ax.get_position()
#plt.show()
plt.savefig('book/figures/heaviside.svg')