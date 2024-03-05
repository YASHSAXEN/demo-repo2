from django.shortcuts import render
from txtai.embeddings import Embeddings
from homepage.models import GemData
# from django.http import HttpResponseRedirect
from homepage.models import FlipkartData
import pandas as pd

# d1 = pd.read_csv('flipkart_data.csv')
# d2 = pd.read_csv('gem_data.csv')

product_name = list(GemData.objects.values_list('product_name'))
image_source = list(GemData.objects.values_list('image_source'))
ratings = list(GemData.objects.values_list('ratings'))
brand_name = list(GemData.objects.values_list('brand_name'))
price = list(GemData.objects.values_list('price'))
actual_price = list(GemData.objects.values_list('actual_price'))
category = list(GemData.objects.values_list('category'))

product_name1 = list(FlipkartData.objects.values_list('product_name'))
image_source1 = list(FlipkartData.objects.values_list('image_source'))
ratings1 = list(FlipkartData.objects.values_list('ratings'))
brand_name1 = list(FlipkartData.objects.values_list('brand_name'))
price1 = list(FlipkartData.objects.values_list('price'))
actual_price1 = list(FlipkartData.objects.values_list('actual_price'))
category1 = list(FlipkartData.objects.values_list('category'))

df = {"Product_Name":product_name,"Source":image_source,"Ratings":ratings,"Brand":brand_name,"Price":price,"Actual_price":actual_price,"Category":category}
demo = pd.DataFrame(df)
# demo = pd.DataFrame(d2)

df1 = {"Product_Name":product_name1,"Source":image_source1,"Ratings":ratings1,"Brand":brand_name1,"Price":price1,"Actual_price":actual_price1,"Category":category1}
demo1 = pd.DataFrame(df1)
# demo1 = pd.DataFrame(d1)

embeddings = Embeddings({
"path": "sentence-transformers/all-MiniLM-L6-v2"})



def Index(request):
    searched = ''
    status = True
    embeddings.load('gemdata_encodings')
    data = demo['Product_Name'] + demo['Ratings'] + demo['Brand'] + demo['Price'] + demo['Actual_price'] + demo['Category'] 

    if request.method == 'POST':
        status = False
        searched = request.POST.get('searched')

        if len(searched.strip()) == 0:
            status = True
            return render(request,'index.html',{'status':status,"searched":searched})

        res = embeddings.search(searched,20)
        # product_name = []
        # image_source = []
        # ratings = []
        # brand_name = []
        # price = []
        # actual_price = []
        category = []

        description = []
        for r in res:
            z = list(data[r[0]])
            a = list(GemData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values_list()[0])[1:]
            a[0] = ["-".join(a[0].split(' ')),"-".join(a[0].split(' '))+"&"+a[1]+"&"+"-".join(a[2].split(' '))+"&"+"-".join(a[3].split(' '))+"&"+a[4]+"&"+a[5]]
            # print("-".join(list(GemData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values_list()[0])[1].split(' ')))
            description.append(a)
            # product_name.append(GemData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values()[0]['product_name'])
            # image_source.append(GemData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values()[0]['image_source'])
            # ratings.append(GemData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values()[0]['ratings'])
            # brand_name.append(GemData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values()[0]['brand_name'])
            # price.append(GemData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values()[0]['price'])
            # actual_price.append(GemData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values()[0]['actual_price'])
            # category.append(GemData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values()[0]['category'])
            # print(f"Text: {data[r[0]]}")
            # print(f"Similarity: {r[1]}")
            # print()
        
        # data = {
        #     'product_name':product_name,
        #     'image_source':image_source,
        #     'ratings':ratings,
        #     'brand_name':brand_name,
        #     'price':price,
        #     'actual_price':actual_price,
        #     'category':category,
        #     'lengths':len(category)
        # }
        # y = GemData.objects.all().values()
        # to stop the form resubmission on the page refresh use HttpResponseRedirect instead of render after the submission of the form
        return render(request,'index.html',{
            'description':description[1:],
            'searched':searched,
            "status":status
            # 'product_name':product_name,
            # 'image_source':image_source,
            # 'ratings':ratings,
            # 'brand_name':brand_name,
            # 'price':price,
            # 'actual_price':actual_price,
            # 'category':category,
            # 'lengths':list(range(len(category)))
        })
    else:
        return render(request,'index.html',{'status':status,'searched':searched})

# def load_data(request):
#     Product_Name = data['Product_Name']
#     Source = data['Source']
#     Ratings = data['Ratings']
#     Brand = data['Brand']
#     Price = data['Price']
#     Actual_price = data['Actual_price']
#     Category = data['Category']
#     for i in range(len(Category)):
#         x = FlipkartData(product_name=Product_Name[i],image_source=Source[i],ratings=Ratings[i],brand_name=Brand[i],price=Price[i],actual_price=Actual_price[i],category=Category[i])
#         x.save()
#     return render(request,'load.html')
    
def Compare(request):
    if request.method == 'POST':
        embeddings.load('flipkart_encodings')
        productname = request.POST.get('productname').split("&")
        productname[2] = "-".join(productname[2].split("---"))
        productname[3] = " ".join(productname[3].split("-"))
        print(productname)
        data = demo1['Product_Name'] + demo1['Ratings'] + demo1['Brand'] + demo1['Price'] + demo1['Actual_price'] + demo1['Category'] 
        # embeddings.search return the list of tuples in whic each tuple contain 2 values first the index of the product and second its similarity
        res = embeddings.search(productname[0],1)
        description = []
        print(res)
        print(res[0][0])
        # for r in res:
        z = list(data[res[0][0]])
        # print(z)
        # print(list(GemData.objects.filter(product_name=productname[0],ratings="-".join(productname[1].split("---")),brand_name=productname[2],price=productname[3],actual_price=productname[4],category=productname[5]).values_list()))
        description.append(productname)
        # print(a)
        # a[0] = "-".join(a[0].split(' '))
        description.append(list(FlipkartData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values_list()[0])[1:])
        print(list(FlipkartData.objects.filter(product_name=z[0],ratings=z[1],brand_name=z[2],price=z[3],actual_price=z[4],category=z[5]).values_list()[0]))
        return render(request,'compare.html',{
            'description':description
            # 'product_name':product_name,
            # 'image_source':image_source,
            # 'ratings':ratings,
            # 'brand_name':brand_name,
            # 'price':price,
            # 'actual_price':actual_price,
            # 'category':category,
            # 'lengths':list(range(len(category)))
        })