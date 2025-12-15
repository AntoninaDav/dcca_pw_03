-- Создание базы данных для анализа продаж отделов
-- Задание 5: продажи , планы продаж, отдел

-- Таблица отделов
CREATE TABLE IF NOT EXISTS branch (
    branch_id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    employees_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица план продаж
CREATE TABLE IF NOT EXISTS sales_plan (
    branch_id SERIAL PRIMARY KEY,
    monthly_plan INTEGER ,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица продаж
CREATE TABLE IF NOT EXISTS sales (
    branch_id SERIAL PRIMARY KEY,
    sales_amount INTEGER ,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Представление для расчета выручки авиакомпаний
CREATE OR REPLACE VIEW branch_sales AS
SELECT 
    b.branch_id,
    b.city ,
    b.employees_count,
    COUNT(DISTINCT b.branch_id) AS total_branch,
    SUM(b.employees_count) AS total_passengers_from_all_branch,
    SUM(s.sales_amount ) AS total_sales
FROM branch b
LEFT JOIN sales_plan p ON b.branch_id = p.branch_id
LEFT JOIN sales s ON b.branch_id = s.branch_id
GROUP BY a.airline_id, a.name, a.country
ORDER BY total_sales DESC NULLS LAST;
