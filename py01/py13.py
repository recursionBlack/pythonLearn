class Washer:
    height = 800
    def wash(self):
        print("我会洗衣服")
        print("方法中的self",self)
Washer.width = 400
print(Washer.width)
wa = Washer()
print(wa)
wa.wash()