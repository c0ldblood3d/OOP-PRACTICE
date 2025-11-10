from Product import Product, PremiumProduct

product1 = Product("Ноутбук", "Электроника", 1000.0)
premium_product1 = PremiumProduct("Смартфон", "Электроника", 800.0)
    
print("Обычный продукт:")
print(product1)
print(f"Первая буква категории: {product1.get_category_initial()}")
print(f"Цена после скидки 20%: {product1.apply_discount(20)}")
print()
    
print("Премиум продукт:")
print(premium_product1)
print(f"Первая буква категории: {premium_product1.get_category_initial()}")
print(f"Цена после 'скидки' 20%: {premium_product1.apply_discount(20)}")
print()
    
product2 = Product("Книга", "Литература", 50.0)
premium_product2 = PremiumProduct("Наушники", "Аудио", 200.0)
    
print("Сравнение скидок:")
print(f"Обычный продукт (скидка 20%): {product2.apply_discount(20)}")
print(f"Премиум продукт (скидка 20%): {premium_product2.apply_discount(20)}")