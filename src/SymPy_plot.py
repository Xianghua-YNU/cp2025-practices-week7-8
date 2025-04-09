import sympy as sp

# 定义符号变量
x, y, s, t = sp.symbols('x y s t')

# 任务 1: 使用 sympy.plot 绘制函数曲线 cos(tan(pi * x))
def plot_function():
    expr = sp.cos(sp.tan(sp.pi * x))
    p1 = sp.plot(expr, (x, -1, 1), title='Plot of cos(tan(pi * x))', xlabel='x', ylabel='y')
    return p1

# 任务 2: 使用 sympy.plot_implicit 绘制隐函数曲线 (e^y + cos(x)) / (x + y) = 0
def plot_implicit_function():
    expr = (sp.exp(y) + sp.cos(x)) / (x + y)
    p2 = sp.plot_implicit(sp.Eq(expr, 0), (x, -5, 5), (y, -5, 5),
                          title='Plot of (e^y + cos(x)) / (x + y) = 0',
                          xlabel='x', ylabel='y')
    return p2

# 任务 3: 使用 sympy.plot3d_parametric_surface 绘制参数曲面
def plot_parametric_surface():
    x_expr = sp.exp(-s) * sp.cos(t)
    y_expr = sp.exp(-s) * sp.sin(t)
    z_expr = t
    p3 = sp.plot3d_parametric_surface(x_expr, y_expr, z_expr, (s, 0, 8), (t, 0, 5 * sp.pi),
                                      title='Parametric Surface Plot',
                                      xlabel='x', ylabel='y', zlabel='z')
    return p3


if __name__ == "__main__":
    # 绘制函数曲线
    plot_function()
    # 绘制隐函数曲线
    plot_implicit_function()
    # 绘制参数曲面
    plot_parametric_surface()
    
