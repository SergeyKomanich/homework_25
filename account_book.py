list_book = [
            [34587, 'Learning Python, Mark Lutz', 4, 40.95],
            [98762, 'Programming Python, Mark Lutz', 5, 56.80],
            [77226, 'Head First Python, Paul Barry', 3, 32.95],
            [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
            ]

book_price = list(map(lambda x: (x[0], round((x[2] * x[3]), 2) + 10 if round((x[2] * x[3]), 2) < 100 else round((x[2] * x[3]), 2)), list_book))


print('№:', book_price[0][0], 'amount:', list_book[0][2], 'charge:', list_book[0][3], 'sum:', book_price[0][1])
print('№:', book_price[1][0], 'amount:', list_book[1][2], 'charge:', list_book[1][3], 'sum:', book_price[1][1])
print('№:', book_price[2][0], 'amount:', list_book[2][2], 'charge:', list_book[2][3], 'sum:', book_price[2][1])
print('№:', book_price[3][0], 'amount:', list_book[3][2], 'charge:', list_book[3][3], 'sum:', book_price[3][1])

print(book_price)
