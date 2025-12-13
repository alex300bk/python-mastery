def portfolio_cost(path_to_portfoio: str) -> float:
    total_cost = 0.0
    with open(path_to_portfoio) as f:
        # print("Stock name:    Price")
        for line in f:
            data = line.split(" ")
            # stock_name = data[0]
            try:
                stock_count = int(data[1])
                stock_price = float(data[2])
                local_stock_total = stock_count * stock_price
                total_cost += local_stock_total
            except ValueError as e:
                print("Warning: Couldn't parse: ", repr(line))
                print(f"Reason: {e}")
            # print(f"{stock_name}: {local_stock_total:>15.2f}")
    return total_cost


portfolio_path = "../../Data/portfolio3.dat"
print(f"Total stock cost: {portfolio_cost(portfolio_path):>10.2f}")
