import os
from eth_account import Account

if __name__ == '__main__':
    # account = Account.create()
    # print('%s,%s'%(account.address,account.key.hex())) #.hex()格式化 转化为以0x开头的十六进制的字符串
    file_name = input('请输入文件名:')
    if os.path.exists(file_name):
        print("文件已存在，请换个名字：")
    else:
        j=1
        n = int(input('请输入需要创建的钱包数：'))
        for i in range(n):
            Account.enable_unaudited_hdwallet_features()
            account, mnemonic = Account.create_with_mnemonic()
            num = '第%d个钱包' % j
            print(num)
            line =('%s,%s,%s,%d' % (account.address, account.key.hex(), mnemonic, j)) #mnemonic助记词
            print(line)
            j = j + 1
            with open(file_name, 'a') as f: #a追加
                f.write(line + '\n')

    # with open('nft1','r') as 100f:
    #     data = f.readlines()
    # j = 1
    # for i in data:
    #     i = i.replace('\n','')
    #     print('第%d个钱包' % j)
    #     print(i.split(',')[1]) #打印私钥
    #     j = j+1

