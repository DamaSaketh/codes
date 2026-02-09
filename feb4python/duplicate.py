arrr=[1,2,3,4,1,4,7,8,9]
seen=set()
duplicates=set()

for num in arrr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print(duplicates)
print(seen)