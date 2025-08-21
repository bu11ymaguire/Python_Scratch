def Celsius_to_Ferh(x):
      return x * 1.8 + 32

print("본 프로그램은 섭씨 온도를 화씨 온도로 변환해주는 프로그램입니다.")
cel = input("변환하고 싶은 섭씨 온도를 입력해 주세요: ")
celS = float(cel)
ferh = Celsius_to_Ferh(celS)

print(f"섭씨 온도: {celS}")
print(f"화씨 온도: {ferh}")
