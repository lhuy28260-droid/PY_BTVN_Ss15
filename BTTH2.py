atm_vault_balance = 50000000
user_account_balance = 10000000

def display_balances():
    """
    In ra màn hình số dư tài khoản hiện tại của người dùng.
    Phục vụ mục đích debug: In thêm lượng tiền mặt vật lý đang có trong ATM.
    """
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,.0f} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,.0f} VND")

def deposit_money(amount):
    
    global user_account_balance, atm_vault_balance
    user_account_balance += amount
    atm_vault_balance += amount
    return True

def check_withdrawal_rules(amount):
    
    # Bẫy 1 - Số tiền là bội số của 50,000
    if amount % 50000 != 0:
        return "INVALID_MULTIPLE", 0
    
    # Biến local tính phí
    fee = 1100
    total_deduction = amount + fee
    
    # Kiểm tra điều kiện rút
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS", total_deduction
    elif amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH", total_deduction
    else:
        return "OK", total_deduction

def execute_withdrawal(total_deduction, amount_to_dispense):
    
    global user_account_balance, atm_vault_balance
    
    # Trừ tiền
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    
    # Tính lại phí để in ra biên lai
    fee = total_deduction - amount_to_dispense
    
    # In biên lai
    print("Giao dịch đang xử lý...")
    print(f"Phí giao dịch: {fee:,.0f} VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,.0f} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,.0f} VND.")

def handle_deposit_feature():
    try:
        amount = int(input("Nhập số tiền muốn nạp: "))
        
        # Bẫy 2 - Nhập số âm / bằng 0
        if amount <= 0:
            print("Số tiền không hợp lệ.")
            return
            
        # Gọi hàm logic lõi
        if deposit_money(amount):
            print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,.0f} VND.")
            
    except ValueError:
        print("Lỗi: Dữ liệu không hợp lệ. Vui lòng nhập số nguyên.")

def handle_withdrawal_feature():
    try:
        amount = int(input("Nhập số tiền cần rút: "))
        
        # Bẫy 2 - Nhập số âm / bằng 0
        if amount <= 0:
            print("Số tiền không hợp lệ.")
            return
        
        # Gọi hàm kiểm tra logic rút tiền
        status, total_deduction = check_withdrawal_rules(amount)
        
        # Xử lý các trạng thái return từ hàm kiểm tra
        if status == "INVALID_MULTIPLE":
            print("Số tiền rút phải là bội số của 50,000")
        elif status == "INSUFFICIENT_FUNDS":
            print("Giao dịch thất bại: Số dư tài khoản không đủ để thanh toán tiền rút và phí.")
        elif status == "ATM_OUT_OF_CASH":
            print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
        elif status == "OK":
            # Gọi hàm thực thi trừ tiền
            execute_withdrawal(total_deduction, amount)
            
    except ValueError:
        print("Lỗi: Dữ liệu không hợp lệ. Vui lòng nhập số nguyên.")

def main():
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")
        
        choice = input("Vui lòng chọn giao dịch (1-4): ")

        if choice == '1':
            print("Chọn giao dịch (1-4): 1")
            display_balances()

        elif choice == '2':
            handle_deposit_feature()

        elif choice == '3':
            handle_withdrawal_feature()

        elif choice == '4':
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()