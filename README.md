# list_cubic_spline

### Cubic Interpolation

![sample demonstration](https://github.com/nathanchenseanwalter/list_cubic_spline/blob/main/sample.png?raw=true)

Cubic interpolation (Bezier, Hermite, Cardinal, B-Spline) written in list comprehension and vectorization, no Numpy! Used to draw trajectories between points

Curve trajectories are all given by

```math
A \times B \times C
```

```math
A = \begin{bmatrix}
1 & t & t^2 & t^3
\end{bmatrix}
```

### Bezier
```math
B \times C = \begin{bmatrix}
1 & 0 & 0 & 0 \\
-3 & 3 & 0 & 0 \\
3 & -6 & 3 & 0 \\
-1 & 3 & -3 & 1 
\end{bmatrix}

\begin{bmatrix}
P_1 \\
H_1 \\
H_2 \\
P_2 
\end{bmatrix}
```

### Hermite
```math
B \times C = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
-3 & 3 & -2 & -1 \\
2 & -2 & 1 & 1 
\end{bmatrix}

\begin{bmatrix}
P_1 \\
P_2 \\
H_1 \\
H_2 
\end{bmatrix}
```

### Cardinal
```math
B \times C = \begin{bmatrix}
0 & 1 & 0 & 0 \\
-s & 0 & s & 0 \\
2s & s-3 & 3-2s & -s \\
-s & 2-s & s-2 & s 
\end{bmatrix}

\begin{bmatrix}
P_1* \\
P_2 \\
P_3 \\
P_4* 
\end{bmatrix}
```

### B-Spline
```math
B \times C = \begin{bmatrix}
1 & 4 & 1 & 0 \\
-3 & 0 & 3 & 0 \\
3 & -6 & 3 & 0 \\
-1 & 3 & -3 & 1 
\end{bmatrix}

\begin{bmatrix}
H_1 \\
H_2 \\
H_3 \\
H_4 
\end{bmatrix}
```

### Variable Description
$s$ is the tension, and can vary from 0 to 1. 0 is linear interpolation, 0.5 is Catmull-Rom</br>
$P$ denotes control points that lie on the curve</br>
$H$ denotes control points that don't lie on the curve (handles)</br>
(*) starred denotes points that aren't interpolated</br>
