# 随机子句生成与SAT求解
贵州大学2025数理逻辑期末大作业项目二

授课老师：王以松教授

## 使用说明

随机生成子句集并使用 SAT 求解器计算其模型的 Python 项目实现。本项目使用python-sat库作为 SAT 求解器。

这个项目包含两个主要类：

`ClauseGenerator - 用于随机生成子句集，支持自定义变量数量、子句数量和随机种子。`

`SATSolver - 使用 PySAT 库中的 Glucose3 求解器解决 SAT 问题，并提供模型验证功能。`

主程序演示了如何使用这两个类来生成随机子句集并求解。可以通过修改main函数中的参数来调整子句集的规模和特性。

requirements.txt文件列出了所需的依赖库。

## 使用方法：

## 1、安装依赖：
```bash
pip install -r requirements.txt
```
## 2、运行程序：
```bash
python sat_generator_solver.py
```

程序会输出生成的子句集、可满足性结果和模型（如果存在），并验证模型的正确性。

## License
This project is licensed under the [MIT License](LICENSE).
