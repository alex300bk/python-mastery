total_cost = 0.0

with open("../../Data/portfolio.dat") as f:
    for line in f:
        data = line.split(" ")
        stock_name = data[0]
        stock_count = int(data[1])
        stock_price = float(data[2])
        local_stock_total = stock_count * stock_price
        print(f"{stock_name}: {local_stock_total:>10.2f}")
        total_cost += local_stock_total

print(f"Total stock cost {total_cost:>10.2f}")
