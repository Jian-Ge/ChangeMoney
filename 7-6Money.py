#7-6记: 今天去面试碰到的题，手写实在难受，还是IDE懂我心，加油打工人!
if __name__ == "__main__":
    start()

def start():
    print("\n设置十块钱,五块钱,两块钱的张数：(格式<hs>,<hw>,<he>)")
    hs, hw, he = [int(i) for i in input().split(',')]
    total = hs * 10 + hw * 5 + he * 2
    print('当前设定拥有的钱总数为: %d\n' % total)
    print("请输入需要计算的总金额")
    n = int(input())
    while n > 0:
        calc(hs, hw, he, n)
        n = int(input())
    if n <= 0:
        print('需要计算的总金额不能小于或等于零')
        return
def calc(hs, hw, he, n):
    
    total = hs * 10 + hw * 5 + he * 2
    if n > total:
        print('输入金额超出总金额 %d' % total)
        return
    
    ns = n // 10
    ns = ns if (hs >= ns) else hs
    remainingMoney = n - ns * 10
    if ns > 0:
        if remainingMoney == 1 or remainingMoney == 3:
            ns -= 1
            remainingMoney += 10
    nw = remainingMoney // 5
    nw = nw if (hw >= nw) else hw
    remainingMoney -= nw * 5
    if nw > 0:
        if remainingMoney % 2 != 0:
            nw -= 1
            remainingMoney += 5
    ne = remainingMoney // 2
    ne = ne if (he >= ne) else he
    remainingMoney -= ne * 2
    if remainingMoney == 0:
        print('无需找零，使用%2d张十元，%d张五元，%d张两元' % (ns, nw, ne))
        start()
    else:
        print('需要找零，拥有%2d张十元，%d张五元，%d张两元' % (hs, hw, he))
        start()