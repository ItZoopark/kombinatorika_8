alpha = 'КАЛИЙ'
count = 0
for c1 in alpha:
    for c2 in alpha:
        for c3 in alpha:
            for c4 in alpha:
                for c5 in alpha:
                    res = c1 + c2 + c3 + c4 + c5
                    if res.count('К') == 1 and res.count('А') == 1 and res.count('Л') == 1 and res.count(
                            'И') == 1 and res.count('Й') == 1:
                        if c1 != 'Й' and res.count('ИА') != 1:
                            count += 1
                        # print(res)

print(count)
