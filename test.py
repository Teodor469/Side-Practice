rolls_of_paper = int(input())
rolls_of_fabric = int(input())
glue_liters = float(input())
discount_percentage = int(input())

price_per_paper = 5.80
price_per_fabric = 7.20
price_per_glue = 1.20

total_paper_cost = rolls_of_paper * price_per_paper
total_fabric_cost = rolls_of_fabric * price_per_fabric
total_glue_cost = glue_liters * price_per_glue

total_material_cost = total_paper_cost + total_fabric_cost + total_glue_cost

discounted_price = total_material_cost * (1 - (discount_percentage / 100))

print(f"{discounted_price:.3f}")
