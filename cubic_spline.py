
def bezier(ctrl_pt, t_B , fig_points):
    qb_const = [[1,0,0,0],[-3,3,0,0],[3,-6,3,0],[-1,3,-3,1]]
    temp_ctrl_pt = [[ctrl_pt[i*3+n+1] for n in range(4)] for i in range(fig_points)]
    temp_B = [[[sum(a*b for a,b in zip(row,col)) for col in zip(*idx)] for row in qb_const] for idx in temp_ctrl_pt]
    curve = [[[sum(a*b for a,b in zip(row,col)) for col in zip(*idx)] for row in zip(*t_B)] for idx in temp_B]
    return [i for sub in curve for i in sub]

def hermite(ctrl_pt, t_B , fig_points):
    qb_const = [[1,0,0,0],[0,0,1,0],[-3,3,-2,-1],[2,-2,1,1]]
    temp_ctrl_pt = [[ctrl_pt[i*3+1],ctrl_pt[i*3+4],ctrl_pt[i*3+2],ctrl_pt[i*3+5]] for i in range(fig_points)]
    temp_B = [[[sum(a*b for a,b in zip(row,col)) for col in zip(*idx)] for row in qb_const] for idx in temp_ctrl_pt]
    curve = [[[sum(a*b for a,b in zip(row,col)) for col in zip(*idx)] for row in zip(*t_B)] for idx in temp_B]
    return [i for sub in curve for i in sub]

def cardinal(ctrl_pt, t_B, fig_points, tens=0.5):
    qb_const = [[0,1,0,0],[-tens,0,tens,0],[2*tens,tens-3,3-2*tens,-tens],[-tens,2-tens,tens-2,tens]]
    temp_ctrl_pt = [[ctrl_pt[i*3-2],ctrl_pt[i*3+1],ctrl_pt[i*3+4],ctrl_pt[i*3+7]] for i in range(fig_points)]
    temp_B = [[[sum(a*b for a,b in zip(row,col)) for col in zip(*idx)] for row in qb_const] for idx in temp_ctrl_pt]
    curve = [[[sum(a*b for a,b in zip(row,col)) for col in zip(*idx)] for row in zip(*t_B)] for idx in temp_B]
    return [i for sub in curve for i in sub]

def b_spline(ctrl_pt, t_B , fig_points):
    qb_const = [[1,4,1,0],[-3,0,3,0],[3,-6,3,0],[-1,3,-3,1]]
    temp_ctrl_pt = [[ctrl_pt[i*3-2],ctrl_pt[i*3+1],ctrl_pt[i*3+4],ctrl_pt[i*3+7]] for i in range(fig_points)]
    temp_B = [[[sum(a*b/6 for a,b in zip(row,col)) for col in zip(*idx)] for row in qb_const] for idx in temp_ctrl_pt]
    curve = [[[sum(a*b for a,b in zip(row,col)) for col in zip(*idx)] for row in zip(*t_B)] for idx in temp_B]
    return [i for sub in curve for i in sub]