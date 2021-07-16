from upbank_api_wrapper import accounts, categories

cat = categories.Categories()

print(cat.list_categories().text)

