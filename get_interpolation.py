import random
import matplotlib.pyplot as plt
import cubic_spline as spl

fig_points = 10
dim = 2 # dimension
res = 100 # resolution

# ctrl_pt = [[1]*dim for i in range(fig_points*3+1)] # custom points initialize

# random points
ctrl_pt_x = [i for i in range(fig_points*3+5)]
ctrl_pt_y = [random.random() for _ in range(fig_points*3+5)]
ctrl_pt = list(zip(ctrl_pt_x,ctrl_pt_y))

x_d,y_d = zip(*ctrl_pt[1:fig_points*3+2:3])

num_rg = [i/res for i in range(res)]
t_B = [[i**j for i in num_rg] for j in range(4)]

bezcurv = spl.bezier(ctrl_pt, t_B, fig_points)
hermcurv = spl.hermite(ctrl_pt, t_B, fig_points)
catcurv = spl.cardinal(ctrl_pt, t_B, fig_points)
bcurv = spl.b_spline(ctrl_pt, t_B, fig_points)

plt.scatter(x_d,y_d)
x,y = zip(*bezcurv)
plt.plot(x,y,"bezier")
x,y = zip(*hermcurv)
plt.plot(x,y,"hermite")
x,y = zip(*catcurv)
plt.plot(x,y,"catmull-rom")
x,y = zip(*bcurv)
plt.plot(x,y,"B-spline")

plt.legend()
plt.show()