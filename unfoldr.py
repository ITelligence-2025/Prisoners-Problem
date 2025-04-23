
def unfoldr(f):
    '''초기갑(seed)으로부터 연속적으로 just(value,nextseed)를 리턴받아 리스트를 생성, nothing이 반환되면 리스트 생성을 중단 
    '''
    def go(v):
        xr = v, v
        xs = []
        while True:
            mb = f(xr[0]) # Just((newSeed, value)) or Nothing
            if mb.get('Nothing'):
                return xs
            else:
                xr = mb.get('Just') # unpack (newSeed, value)
                xs.append(xr[1])
        return xs
    return lambda x: go(x)
'''xs.append(xr[1]): 즉 value만 누적

xr = (newSeed, value) → 다음 루프는 newSeed로 시작


'''
