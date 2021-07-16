from upwrapper import accounts, categories

cat = categories.Categories()

print(cat.list_categories().text)

