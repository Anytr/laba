# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_mb = 1.44
pages = 100
lines = 50
symbols_per_line = 25
symbol_size = 4
disk_size_bytes = disk_size_mb * 1024 * 1024
book_size_bytes = pages * lines * symbols_per_line * symbol_size
books_count = round(disk_size_bytes / book_size_bytes)
print("Количество книг, помещающихся на дискету:", books_count)