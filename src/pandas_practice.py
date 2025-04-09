import pandas as pd
import matplotlib.pyplot as plt

def creat_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    
    该函数创建一个包含学生姓名、年龄、成绩和所在城市的数据框架，
    并将其保存为UTF-8编码的CSV文件。
    
    Returns:
        None
    """
    # 学生需要在此处实现代码
    data = {
        '姓名': ['张三', '李四', '王五'],
        '年龄': [20, 22, 21],
        '成绩': [85, 90, 88],
        '所在城市': ['北京', '上海', '广州']
    }
    df = pd.DataFrame(data)
    df.to_csv('data/data.csv', encoding='utf-8', index=False)


def load_data():
    """任务1: 读取数据文件"""
    # 学生需要在此处实现代码
    data = pd.read_csv('data/data.csv')
    return data


def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    # 学生需要在此处实现代码
    print(data.info())
    print(data.describe())

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    # 学生需要在此处实现代码
    num_cols = data.select_dtypes(include='number').columns
    for col in num_cols:
        mean_value = data[col].mean()
        data[col].fillna(mean_value, inplace=True)

    non_num_cols = data.select_dtypes(exclude='number').columns
    for col in non_num_cols:
        mode_value = data[col].mode()[0]
        data[col].fillna(mode_value, inplace=True)
    return data

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    # 学生需要在此处实现代码
    num_cols = data.select_dtypes(include='number').columns
    for col in num_cols:
        print(f"列 {col} 的均值: {data[col].mean()}")
        print(f"列 {col} 的标准差: {data[col].std()}")
        print(f"列 {col} 的最小值: {data[col].min()}")
        print(f"列 {col} 的最大值: {data[col].max()}")

def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    # 学生需要在此处实现代码
    plt.hist(data[column_name], bins=10)
    plt.xlabel(column_name)
    plt.ylabel('频数')
    plt.title(f'{column_name} 分布直方图')
    plt.show()

def save_processed_data(data):
    """任务7: 保存处理后的数据"""
    # 学生需要在此处实现代码
    data.to_csv('data/processed_data.csv', encoding='utf-8', index=False)

def main():
    """主函数，执行所有数据处理流程"""
    # 学生需要在此处组织代码流程
    creat_frame()
    data = load_data()
    show_basic_info(data)
    data = handle_missing_values(data)
    analyze_statistics(data)
    visualize_data(data)
    save_processed_data(data)


if __name__ == "__main__":
    main()
