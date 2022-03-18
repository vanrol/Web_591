from public.page.sale_list_page import SaleFilterScreen
dic1 = {}
for kind in SaleFilterScreen.kinds_list():
    dic1[kind] = SaleFilterScreen.price01_list()
print(dic1)