import random
from pysat.solvers import Glucose3
from typing import List, Set, Tuple

class ClauseGenerator:
    """随机生成子句集的类"""
    
    def __init__(self, num_vars: int, num_clauses: int, seed: int = None):
        """
        初始化子句生成器
        
        参数:
            num_vars: 变量数量
            num_clauses: 子句数量
            seed: 随机数种子，用于结果可复现
        """
        self.num_vars = num_vars
        self.num_clauses = num_clauses
        if seed is not None:
            random.seed(seed)
    
    def generate_clauses(self, min_length: int = 1, max_length: int = None) -> List[List[int]]:
        """
        生成随机子句集
        
        参数:
            min_length: 子句最小长度
            max_length: 子句最大长度，默认为变量数量的一半
        
        返回:
            子句集，每个子句是变量或其否定的列表
        """
        if max_length is None:
            max_length = max(min_length, self.num_vars // 2)
        
        clauses = []
        for _ in range(self.num_clauses):
            # 随机确定子句长度
            clause_length = random.randint(min_length, max_length)
            # 随机选择变量
            vars_in_clause = random.sample(range(1, self.num_vars + 1), clause_length)
            # 随机确定每个变量是否取否定
            clause = [var if random.choice([True, False]) else -var for var in vars_in_clause]
            clauses.append(clause)
        
        return clauses

class SATSolver:
    """使用PySAT库解决SAT问题的类"""
    
    def __init__(self, clauses: List[List[int]]):
        """
        初始化SAT求解器
        
        参数:
            clauses: 子句集
        """
        self.clauses = clauses
    
    def solve(self) -> Tuple[bool, List[int]]:
        """
        求解SAT问题
        
        返回:
            (是否可满足, 模型)
            如果不可满足，模型为None
        """
        solver = Glucose3()
        
        # 添加子句到求解器
        for clause in self.clauses:
            solver.add_clause(clause)
        
        # 检查可满足性
        is_sat = solver.solve()
        
        # 获取模型（如果可满足）
        model = solver.get_model() if is_sat else None
        
        # 释放求解器资源
        solver.delete()
        
        return is_sat, model
    
    def verify_model(self, model: List[int]) -> bool:
        """
        验证模型是否满足所有子句
        
        参数:
            model: 模型，变量的赋值列表
        
        返回:
            模型是否有效
        """
        if model is None:
            return False
        
        # 将模型转换为变量赋值字典
        assignment = {abs(var): (var > 0) for var in model}
        
        # 检查每个子句是否被满足
        for clause in self.clauses:
            clause_satisfied = False
            for literal in clause:
                var = abs(literal)
                sign = literal > 0
                if assignment.get(var, False) == sign:
                    clause_satisfied = True
                    break
            if not clause_satisfied:
                return False
        
        return True

def main():
    # 参数设置
    num_vars = 10  # 变量数量
    num_clauses = 30  # 子句数量
    seed = 42  # 随机种子，设为None则使用随机种子
    
    # 生成子句集
    generator = ClauseGenerator(num_vars, num_clauses, seed)
    clauses = generator.generate_clauses(min_length=2, max_length=5)
    
    print(f"生成的子句集 ({len(clauses)} 个子句):")
    for i, clause in enumerate(clauses, 1):
        print(f"子句 {i}: {' ∨ '.join(map(str, clause))}")
    
    # 求解SAT问题
    solver = SATSolver(clauses)
    is_sat, model = solver.solve()
    
    # 输出结果
    if is_sat:
        print("\nSAT问题可满足")
        print("模型:")
        for var in range(1, num_vars + 1):
            value = None
            for literal in model:
                if abs(literal) == var:
                    value = literal > 0
                    break
            print(f"变量 {var}: {value}")
        
        # 验证模型
        if solver.verify_model(model):
            print("\n模型验证通过")
        else:
            print("\n模型验证失败（这表明存在错误）")
    else:
        print("\nSAT问题不可满足")

if __name__ == "__main__":
    main()    