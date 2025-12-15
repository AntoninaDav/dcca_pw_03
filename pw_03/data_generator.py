"""
Генератор тестовых данных для задания 30: Анализ авиакомпаний
Создает три файла:
1. branch.csv - данные об авиакомпаниях
2. sales.xlsx - данные о продажах
3. sales_plan.json - данные о планах продаж
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta
import random

# Настройка генератора случайных чисел для воспроизводимости
np.random.seed(42)
random.seed(42)

def generate_branch_data(num_branches=1000):
    """Генерация данных об авиакомпаниях (CSV) - 1000 записей"""
    
    cities = [
        "Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань",
        "Нижний Новгород", "Челябинск", "Самара", "Омск", "Ростов-на-Дону",
        "Уфа", "Красноярск", "Воронеж", "Пермь", "Волгоград", "Краснодар",
        "Саратов", "Тюмень", "Тольятти", "Ижевск"
    ]
    
    branch_data = []
    
    for i in range(1, num_branches + 1):
        branch_id = f"branch{i:05d}"
        city = random.choice(cities)
        employees_count = random.randint(3, 100)
        
        branch_data.append({
            "branch_id": branch_id,
            "city": city,
            "employees_count": employees_count
        })
    
    # Сохраняем 1000 записей в CSV
    df_branch = pd.DataFrame(branch_data)
    df_branch.to_csv('data/branch.csv', index=False, encoding='utf-8')
    print(f"✓ Файл branch.csv создан ({len(branch_data)} записей)")
    return branch_data

def generate_sales_data(branches_data):
    """Генерация данных о продажах (Excel) - 1000 записей"""
    
    sales_data = []
    
    # Для каждой авиакомпании создаем хотя бы одну запись о продажах
    # Но всего должно быть 1000 записей
    for i in range(1000):
        # Выбираем случайную авиакомпанию
        branch = random.choice(branches_data)
        branch_id = branch['branch_id']
        
        sale_amount = random.randint(10_000, 500_000)
        
        sales_data.append({
            "branch_id": branch_id,
            "sales_amount": sale_amount
        })
    
    df_sales = pd.DataFrame(sales_data)
    df_sales.to_excel('data/sales.xlsx', index=False)
    print(f"✓ Файл sales.xlsx создан ({len(sales_data)} записей)")
    return sales_data

def generate_sales_plan_data():
    """Генерация данных о планах продаж (JSON) - 1000 записей"""
    
    sales_plan_data = []
    
    # Генерируем 1000 уникальных branch_id для планов продаж
    for i in range(1, 1001):
        branch_id = f"branch{i:05d}"
        monthly_plan = random.randint(8_000, 300_000)
        
        sales_plan_data.append({
            "branch_id": branch_id,
            "monthly_plan": monthly_plan
        })
    
    # Сохраняем в JSON
    with open('data/sales_plan.json', 'w', encoding='utf-8') as f:
        json.dump(sales_plan_data, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Файл sales_plan.json создан ({len(sales_plan_data)} записей)")
    return sales_plan_data

def main():
    """Основная функция генерации данных"""
    print("Генерация тестовых данных для анализа авиакомпаний...")
    print("=" * 50)
    
    # Создаем папку data если её нет
    if not os.path.exists('data'):
        os.makedirs('data')
        print("✓ Создана папка 'data'")
    
    # Генерируем данные - по 1000 записей в каждом файле
    print("Создание branch.csv (1000 записей)...")
    branch_data = generate_branch_data(1000)  # 1000 авиакомпаний
    
    print("Создание sales.xlsx (1000 записей)...")
    sales_data = generate_sales_data(branch_data)  # 1000 продаж
    
    print("Создание sales_plan.json (1000 записей)...")
    sales_plan_data = generate_sales_plan_data()  # 1000 планов продаж
    
    print("=" * 50)
    print(f"Сгенерировано по 1000 записей в каждом файле:")
    print(f"- branch.csv: {len(branch_data)} записей")
    print(f"- sales.xlsx: {len(sales_data)} записей")
    print(f"- sales_plan.json: {len(sales_plan_data)} записей")
    print("\nВсе файлы сохранены в папке 'data/'")

if __name__ == "__main__":
    main()