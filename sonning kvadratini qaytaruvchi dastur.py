print("son kiriting")
savol = "istalgan son kiriting: "
savol += "(dasturni to'xtatiw uchun 'exit'  sozini bosing):"
while True:
    qiymat = input(savol)
    if qiymat == 'exit'   :
        break
    else:
        print(float(qiymat)**2)
print("Dastur tugadi")
