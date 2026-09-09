def count_unique_visitors(visitors):

    unique = list(set(visitors))

    return len(unique)

print(count_unique_visitors(['Ada', 'Bola', 'Ada']))
print(count_unique_visitors([]))
print(count_unique_visitors(['chidi']))
print(count_unique_visitors(['Ada', 'Ada', 'Ada']))