# main.py
from numbers import (
    ticket_message_decorator,
    perfume_tickets,
    medicine_tickets,
    cosmetic_tickets
)

p = perfume_tickets()
m = medicine_tickets()
c = cosmetic_tickets()

get_perfume_ticket = ticket_message_decorator(lambda: next(p))
get_medicine_ticket = ticket_message_decorator(lambda: next(m))
get_cosmetic_ticket = ticket_message_decorator(lambda: next(c))

def main():
    print("欢迎来到药店自助取号机！")
    while True:
        print("请选择服务区域：")
        print("1. 香水区")
        print("2. 药品区")
        print("3. 化妆品区")
        choice = input("请输入选项（1-3）：")
        if choice == '1':
            get_perfume_ticket()
        elif choice == '2':
            get_medicine_ticket()
        elif choice == '3':
            get_cosmetic_ticket()
        else:
            print("无效选项，请重新选择。")
            continue
        again = input("是否需要为下一位客户取号？(y/n)：")
        if again.lower() != 'y':
            print("程序结束，感谢使用！")
            break

if __name__ == "__main__":
    main()