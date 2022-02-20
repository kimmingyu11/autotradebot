import pyupbit

access = "t6tPZEm0qgHeH8a2dl8Ib1CgIemgr40ATEBxQfCJ"          # 본인 값으로 변경
secret = "oMPzmWdeoqfOIQnqRIRBr12ntbCtaL3Uof1rtVP5"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회