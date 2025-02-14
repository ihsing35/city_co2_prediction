import os
import sys

# 获取当前脚本所在的根目录
root_dir = os.path.dirname(os.path.abspath(__file__))

# 将 src 目录添加到系统路径中，以便可以找到模块
src_dir = os.path.join(root_dir, 'src')
sys.path.append(src_dir)

# 导入并运行主程序
from main import main

if __name__ == "__main__":
    main()
