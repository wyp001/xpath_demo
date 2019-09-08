from lxml import etree

parser = etree.HTMLParser(encoding="utf-8")
html = etree.parse("zhilian.html",parser=parser)

# # 1.获取所有的tr标签
# # //span
# spans = html.xpath("//span")
# for span in spans:
#     print(etree.tostring(span,encoding="utf-8").decode("utf-8"))

# # 2.获取第2个span标签
# #  html.xpath("//span[2]")返回的是一个列表，由于该列表中只有一个元素，可以索引[0]获取到
# span = html.xpath("//span[2]")[0]
# print(etree.tostring(span, encoding="utf-8").decode("utf-8"))

# # 3。获取class等于zhilian-pc的span标签
# spans = html.xpath("//span[@class='zhilian-pc']")
# for span in spans:
#     print(etree.tostring(span,encoding="utf-8").decode("utf-8"))

# # 4.获取所有a标签的href属性值。这样获取的的值只是url的一部分，前面没有域名的那一部分
# # 例如url为https://www.baidu.com/aaa/bbb/ccc，href中的值只有aaa/bbb/ccc
# aList = html.xpath("//a/@href")
# for a in aList:
#     print("https://i.zhaopin.com/"+a)

# 5.获取所有的职位信息（纯文本）
#########例子开始#########
# trs = html.xpath("//tr[opstion()>1]")
# for tr in trs:
#     href = tr.xpath(".//a/@href")
#     print(href)
#########例子结束#########
divs = html.xpath("//div[@class='presentation-item']")
for div in divs:
    # 在某个标签下再次执行xpath函数，获取某个标签的子孙元素
    # 那么应该在//之前附加上一个点，代表在的当前的元素下获取
    # source_span = div.xpath('.//span[1]')[0]
    # print(etree.tostring(source_span, encoding="utf-8").decode("utf-8"))
    source = div.xpath('.//span[1]/text()')[0]
    # print(source)
    position = div.xpath('.//div[@class="fn-left position"]/text()')[0]
    # print(position)
    company = div.xpath('.//div[@class="fn-right company"]/text()')[0]
    # print(company)
    city = div.xpath('.//span[@class="city fn-left"]/text()')[0]
    # print(city)
    num = div.xpath('.//span[@class="num fn-left"]/text()')[0]
    # print(num)
    time = div.xpath('.//span[@class="time fn-left"]/text()')[0]
    # print(time)
    industry = div.xpath('.//span[@class="industry fn-right"]/text()')[0]
    # print(industry)

    # 将数据组装成一个json串
    position_conent = {
        "source":source,
        "position":position,
        "company":company,
        "city":city,
        "num":num,
        "time":time,
        "industry":industry
    }
    print(position_conent)







