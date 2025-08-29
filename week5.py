movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each, line_total)

# ---------- Part A: Input Loop ----------
while True:
    title = input("Enter a movie title (or 'done' to finish): ")
    if title.lower() == "done":
        break

    if title not in movies:
        print("Invalid choice. Available movies are:", list(movies.keys()))
        continue

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number for quantity.")
        continue

    price_each = movies[title]
    
    # apply group discount
    if qty >= 4:
        price_each *= 0.9   # 10% off
    
    line_total = price_each * qty
    purchases.append((title, qty, price_each, line_total))
    print(f"Added {qty} tickets for {title} (each ${price_each:.2f}, line ${line_total:.2f})")

print("\n--- RECEIPT ---")

# ---------- Part B: Receipt ----------
grand_total = 0
for title, qty, price_each, line_total in purchases:
    print(f"{title:15} x{qty:<3} @ ${price_each:.2f} = ${line_total:.2f}")
    grand_total += line_total

# member discount
is_member = input("Do you have a member code? (y/n): ").lower() == "y"
if is_member:
    grand_total *= 0.95   # 5% off

print(f"TOTAL: ${grand_total:.2f}\n")

# ---------- Part C: Sales Summary ----------
tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each, line_total in purchases:
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0.0) + line_total

print("--- SALES SUMMARY ---")
for title in movies:
    print(f"{title:15} Tickets: {tickets_by_movie.get(title,0):<3} Revenue: ${revenue_by_movie.get(title,0):.2f}")

# ---------- Part E: Analytics ----------
print("\n--- ANALYTICS ---")

# Top seller by tickets
top_title, top_qty = None, -1
for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title, top_qty = title, qty
print(f"Top seller by tickets: {top_title} ({top_qty} tickets)")

sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)
print("Movies sorted by revenue:", sorted_by_rev)

if purchases:
    total_tickets = sum(qty for _, qty, _, _ in purchases)
    avg_tickets = total_tickets / len(purchases)
    print(f"Average tickets per purchase: {avg_tickets:.2f}")
