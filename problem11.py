import gurobipy as gp
from gurobipy import GRB

def find_nash_equilibrium(payoff_matrix):
    n = len(payoff_matrix)
    
    # Create a new model
    model = gp.Model("nash_equilibrium")
    
    # Create strategies variables for row player and column player
    row_strategies = [model.addVar(vtype=GRB.CONTINUOUS, lb=0, name=f"x{i}") for i in range(n)]
    col_strategies = [model.addVar(vtype=GRB.CONTINUOUS, lb=0, name=f"y{i}") for i in range(n)]
    
    # Set objective for row player
    row_obj_expr = gp.LinExpr()
    for j in range(n):
        col_payoffs = [payoff_matrix[i][j] for i in range(n)]
        row_obj_expr += col_strategies[j] * min(col_payoffs)
    model.setObjective(row_obj_expr, GRB.MAXIMIZE)
    
    # Add constraint for row player
    row_constr_expr = gp.LinExpr()
    for i in range(n):
        row_constr_expr += row_strategies[i]
    model.addConstr(row_constr_expr == 1)
    
    # Set objective for column player
    col_obj_expr = gp.LinExpr()
    for i in range(n):
        row_payoffs = [payoff_matrix[i][j] for j in range(n)]
        col_obj_expr += row_strategies[i] * max(row_payoffs)
    model.setObjective(col_obj_expr, GRB.MINIMIZE)
    
    # Add constraint for column player
    col_constr_expr = gp.LinExpr()
    for j in range(n):
        col_constr_expr += col_strategies[j]
    model.addConstr(col_constr_expr == 1)
    
    # Optimize model
    model.optimize()
    
    # Extract strategies
    row_strategy = [row_var.x for row_var in row_strategies]
    col_strategy = [col_var.x for col_var in col_strategies]
    
    return row_strategy, col_strategy

# Example usage
n = 3
payoff_matrix = [
    [3, 2, 1],
    [1, 4, 2],
    [2, 3, 5]
]

row_strategy, col_strategy = find_nash_equilibrium(payoff_matrix)
print("Row player strategy:", row_strategy)
print("Column player strategy:", col_strategy)
