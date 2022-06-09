#bankamatik uygulaması

accA = {
    "name" : "Bugra Cayir",
    "accNo" : "132452",
    "balance" : 3000,
    "additionalBalance" : 2000
}

accB = {
    "name" : "Buse Cayir",
    "accNo" : "949225",
    "balance" : 2000,
    "additionalBalance" : 1000
}

def withdrawMoney(acc, amount):
    print(f"Hello, {acc['name']}")

    if (acc['balance'] >= amount):
        acc['balance'] -= amount
        print("Here is your money!")
        balanceInquiry(acc)
    else:
        total = acc['balance'] + acc['additionalBalance']

        if (total >= amount):
            useAddBal = input("Do you want to use additional balance? (y/n): ")

            if useAddBal == "y":
                amountOfUsedFromAddBal = amount - acc["balance"]
                acc["balance"] = 0
                acc["additionalBalance"] -= amountOfUsedFromAddBal
                print("Here is your money!")
                balanceInquiry(acc)
            else:
                print(f"In your account numbered {acc['accNo']} has balance of {acc['balance']} and additional balance of {acc['additionalBalance']} money, which makes {acc['balance'] + acc['additionalBalance']} in total.")

        else:
            print("Sorry, your balance is not enough.")


def balanceInquiry(acc):
    print(f"In your {acc['accNo' ]} numbered account has a balance of {acc['balance']}$. Your additional balance is {acc['additionalBalance']}$.")

withdrawMoney(accA, 2000)

print("************************************")

withdrawMoney(accA, 3000)

#ayrıca para yatırma gibi bir fonksiyon daha yazılabilir. Ek hesap limiti de yap.
#ek hesaptan para çektikten sonra çektiğin tarihi kaydedip geri o parayı yüklediğin zamana kadar faiz uygulatabilirsin.
