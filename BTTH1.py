# Khởi tạo 2 biến toàn cục
inventory_stock = 100
total_revenue = 0.0

def add_stock(amount):
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")

def process_sale(quantity):
    global inventory_stock
    if inventory_stock >= quantity:
        return True
    else:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return False

def calculate_final_price(quantity, price):
    subtotal = quantity * price
    discount = 0.0
    
    # Nếu tổng tiền >= 1000, giảm giá 10%
    if subtotal >= 1000:
        discount = subtotal * 0.10
        
    # Tính tiền sau giảm giá và cộng 8% VAT
    after_discount = subtotal - discount
    vat = after_discount * 0.08
    final_total = after_discount + vat
    
    # In hóa đơn chi tiết
    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: ${price:.1f}")
    print(f"Tạm tính: ${subtotal:.1f}")
    if discount > 0:
        print(f"Giảm giá (10%): ${discount:.1f}")
    print(f"Thuế VAT (8%): ${vat:.1f}")
    print(f"Tổng thanh toán: ${final_total:.1f}")
    
    return final_total

def print_report():
    """
    Hàm này có nhiệm vụ truy xuất dữ liệu từ các biến toàn cục
    và in ra báo cáo tổng quan về Tồn kho hiện tại cũng như Tổng doanh thu.
    """
    global inventory_stock, total_revenue
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue:.1f}")

def main():
    global inventory_stock, total_revenue
    
    while True:
        print("\n=========== TECHSTORE MANAGEMENT SYSTEM ===========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("===================================================")
        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            try:
                print("--- NHẬP HÀNG ---")
                amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))
                
                # Bẫy 1 - Số âm
                if amount <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                else:
                    add_stock(amount)
                    
            # Bẫy 2 - Sai kiểu dữ liệu
            except ValueError:
                print("Lỗi: Dữ liệu nhập vào không hợp lệ. Vui lòng nhập số nguyên.")

        elif choice == '2':
            try:
                print("--- BÁN HÀNG ---")
                quantity = int(input("Nhập số lượng mua: "))
                # Bẫy 1 - Số âm cho quantity
                if quantity <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue
                
                price = float(input("Nhập đơn giá ($): "))
                # Bẫy 1 - Số âm cho price
                if price <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue
                
                # Gọi hàm kiểm tra kho và xử lý bán hàng
                if process_sale(quantity):
                    # Gọi hàm tính toán chi phí
                    final_total = calculate_final_price(quantity, price)
                    
                    # Hoàn tất giao dịch
                    inventory_stock -= quantity
                    total_revenue += final_total
                    print("Đã bán thành công!")
                    
            # Bẫy 2 - Sai kiểu dữ liệu
            except ValueError:
                print("Lỗi: Dữ liệu nhập vào không hợp lệ. Vui lòng nhập số.")

        elif choice == '3':
            print("Chọn chức năng (1-4): 3")
            print_report()

        elif choice == '4':
            print("Đã lưu dữ liệu. Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()