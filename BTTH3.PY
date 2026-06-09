# Toàn cục (Global Variables)
available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0

def calculate_ticket_cost(quantity, ticket_class):
    """
    Tính toán tổng chi phí đặt vé dựa trên số lượng và hạng ghế.
    
    Args:
        quantity (int): Số lượng vé khách hàng muốn mua.
        ticket_class (int): Hạng vé (1 cho Economy, 2 cho Business).
        
    Returns:
        float: Tổng tiền cuối cùng đã bao gồm 5% phí dịch vụ sân bay.
    """
    price = BASE_PRICE if ticket_class == 1 else BASE_PRICE * 1.5
    subtotal = quantity * price
    service_fee = subtotal * 0.05
    total_amount = subtotal + service_fee
    
    return float(total_amount)

def process_ticket_booking(quantity, ticket_class, total_amount):
    global available_seats, flight_revenue
    
    # Cập nhật dữ liệu hệ thống
    available_seats -= quantity
    flight_revenue += total_amount
    
    # Tính toán chi tiết để in biên lai
    price = BASE_PRICE if ticket_class == 1 else BASE_PRICE * 1.5
    subtotal = quantity * price
    service_fee = subtotal * 0.05
    class_name = "Economy" if ticket_class == 1 else "Business"
    
    # In ra vé xác nhận
    print("-> Xác nhận đặt chỗ:")
    print(f"Số lượng: {quantity} | Hạng: {class_name}")
    print(f"Tạm tính: ${subtotal:.1f}")
    print(f"Phí dịch vụ (5%): ${service_fee:.1f}")
    print(f"Tổng thanh toán: ${total_amount:.1f}")
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")

def process_ticket_refund(cancel_quantity):
    global available_seats, flight_revenue
    
    # Bẫy 2 - Hủy khống vé (Ghost Refund)
    if available_seats + cancel_quantity > 50:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return 0.0
        
    # Khách hàng chỉ được hoàn 80% giá cơ bản (không hoàn phí dịch vụ)
    refund_per_ticket = BASE_PRICE * 0.8
    total_refund = cancel_quantity * refund_per_ticket
    
    # Cập nhật hệ thống
    available_seats += cancel_quantity
    flight_revenue -= total_refund
    
    return float(total_refund)

def print_flight_status():
    """
    In ra báo cáo tình trạng chuyến bay hiện tại.
    Định dạng hiển thị bao gồm: Sức chứa tối đa, Số ghế đã đặt, 
    Số ghế trống hiện tại và Tổng doanh thu (kèm ký hiệu $).
    """
    global available_seats, flight_revenue
    booked_seats = 50 - available_seats
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: 50")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue:.1f}")

def handle_booking_feature():
    print("--- ĐẶT VÉ MÁY BAY ---")
    try:
        quantity = int(input("Nhập số lượng vé: "))
        
        # Bẫy 3 - Dữ liệu rác (số lượng vé)
        if quantity <= 0:
            print("Lỗi: Số lượng vé phải lớn hơn 0.")
            return
        
        # Bẫy 1 - Overbooking
        if quantity > available_seats:
            print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
            return

        ticket_class = int(input("Chọn hạng vé (1: Economy, 2: Business): "))
        
        # Bẫy 3 - Dữ liệu rác (hạng vé)
        if ticket_class not in [1, 2]:
            print("Lỗi: Hạng vé không hợp lệ. Chỉ chọn 1 hoặc 2.")
            return
        
        # Thực thi logic
        total_amount = calculate_ticket_cost(quantity, ticket_class)
        process_ticket_booking(quantity, ticket_class, total_amount)
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

def handle_refund_feature():
    print("--- HỦY VÉ & HOÀN TIỀN ---")
    try:
        cancel_quantity = int(input("Nhập số lượng vé muốn hủy: "))
        
        # Bẫy 3 - Dữ liệu rác (số âm/0)
        if cancel_quantity <= 0:
            print("Lỗi: Số lượng vé hủy phải lớn hơn 0.")
            return
        
        # Thực thi logic hoàn tiền
        refunded_amount = process_ticket_refund(cancel_quantity)
        
        if refunded_amount > 0:
            print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refunded_amount:.1f} (80% giá cơ bản).")
            print(f"Ghế trống hiện tại: {available_seats}")
            
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

def main():
    while True:
        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("=============================================")
        
        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            handle_booking_feature()
            
        elif choice == '2':
            handle_refund_feature()
            
        elif choice == '3':
            print_flight_status()
            
        elif choice == '4':
            print("Đã đóng hệ thống. Cảm ơn bạn đã sử dụng dịch vụ SkyBooking!")
            break
            
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()