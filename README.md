**ĐỀ TÀI XÂY DỰNG WEBSITE MÓN ĂN**
# 🍜 BÀI GIỚI THIỆU DỰ ÁN: WEBSITE "FOOD BÁ KHÍ"
> **Môn học:** Phát triển ứng dụng Web với Python & Django  
> **Sinh viên Nhóm 5:** 1.Trần Văn Anh Khoa , 2. Đỗ Văn Hậu , 3. Võ Hoàng Khanh , 4.Nguyễn Gia Huy
> **Lớp:** IT25M — Phân hiệu Trường Đại học Đông Á  
> **Trạng thái:** Đã hoàn thành các chức năng giao diện và logic cốt lõi  

---

## 🎙 1. LỜI MỞ ĐẦU & LÝ DO CHỌN ĐỀ TÀI

Kính chào Thầy giáo và các bạn! 

Trong học phần Phát triển Ứng dụng Web, em đã xây dựng dự án website thương mại điện tử ẩm thực mang tên **"Food Bá Khí"**.

* **Vấn đề thực tế:** Khi đi mua sắm hoặc đặt đồ ăn trực tuyến, người dùng thường phân vân về giá giữa các món ăn cùng loại hoặc muốn chọn ra 2-3 món để cân nhắc xem món nào hợp túi tiền hơn trước khi chốt đơn.
* **Giải pháp của dự án:** **Food Bá Khí** không chỉ mang lại giao diện đặt món trực quan, bắt mắt mà còn tích hợp tính năng **So sánh giá đa món ăn** ngay tại trang chủ, giúp người dùng dễ dàng đưa ra quyết định chọn món nhanh chóng.

---

## 🌟 2. GIỚI THIỆU CHI TIẾT CÁC MÀN HÌNH & CHỨC NĂNG

### 🥑 Trang chủ & Thực đơn hôm nay
* **Banner nổi bật:** Thiết kế tone màu cam tươi sáng, mang lại cảm giác ấm cúng cho web ẩm thực với thông điệp: *"Đồ ăn ngon, giao tận nơi - Chọn món yêu thích, so sánh giá và đặt hàng chỉ trong vài giây"*.
* **Danh sách thực đơn phong phú:** Hiển thị trực quan danh sách các món ăn thực tế kèm giá tiền rõ ràng:
  * *Bún đậu mắm tôm (35,000đ)*
  * *Phở bò (30,000đ)*
  * *Tiết canh (40,000đ)*
  * *Gỏi cuốn (25,000đ)*
  * *Gà quay lu / Gà lắc (45,000đ)*
  * *Nước mía (10,000đ), Nem nướng (45,000đ), Mì cay (45,000đ)*
  * *Sầu riêng (100,000đ), Gà nướng (250,000đ), Chè Thái (25,000đ)...*
* **Thanh công cụ tiện ích:** Cho phép tìm kiếm món ăn theo tên và bộ lọc sắp xếp thực đơn theo giá.

### ⚖️ Tính năng So sánh giá Món ăn (Điểm nhấn của web)
* Mỗi sản phẩm trong thực đơn đều được trang bị ô tích chọn (checkbox) ở góc trên.
* **Xử lý ràng buộc thông minh:** Khi người dùng bấm nút **"So sánh giá các món đã chọn"**, nếu chưa chọn đủ số lượng, hệ thống sẽ đưa ra thông báo nhắc nhở ngay:
  👉 *"Hãy chọn ít nhất 2 món để so sánh."*
* Tính năng này giúp người dùng tránh bấm nhầm và có trải nghiệm rõ ràng khi sử dụng web.

### 🔐 Màn hình Đăng ký & Đăng nhập
* **Trang Đăng ký:** Giao diện tối giản nhưng đảm bảo độ an toàn tài khoản với các quy tắc kiểm tra mật khẩu (độ dài tối thiểu 8 ký tự, kiểm tra tính trùng lặp, không chứa toàn số và ô xác nhận lại mật khẩu).
* **Trang Đăng nhập:** Thiết kế gọn gàng, hỗ trợ người dùng truy cập tài khoản nhanh chóng.

---

## 🛠 3. TỔNG QUAN CÔNG NGHỆ SỬ DỤNG

* **Backend:** Python + Django Framework (Xử lý điều hướng trang, phân trang và xác thực tài khoản).
* **Frontend:** HTML, CSS, JavaScript (Thiết kế giao diện phản hồi tốt, xử lý sự kiện tích chọn so sánh giá).
* **Database:** SQLite (Lưu trữ danh sách món ăn, danh mục và tài khoản).

---
*Hình ảnh dự án.
<img width="643" height="907" alt="image" src="https://github.com/user-attachments/assets/30c4172b-a60f-47dc-8b81-ee1614fa8abb" />

## 📁 4. CẤU TRÚC THƯ MỤC DỰ ÁN

```text
food_ba_khi/
├── food_ba_khi/          # Thư mục cấu hình dự án Django
│   ├── settings.py       # Cấu hình chuỗi kết nối, apps, static
│   ├── urls.py           # Điều hướng URL chính
│   └── wsgi.py
├── shop/                 # App chính của dự án
│   ├── static/           # Chứa file CSS, JS, Images
│   ├── templates/        # Chứa giao diện HTML (Trang chủ, Login, Register)
│   ├── admin.py          # Quản lý trang Admin
│   ├── models.py         # Định nghĩa cấu trúc dữ liệu
│   ├── views.py          # Xử lý logic nghiệp vụ
│   └── urls.py           # Định tuyến riêng cho App shop
├── db.sqlite3            # Cơ sở dữ liệu SQLite
├── manage.py             # Lệnh điều khiển dự án
└── requirements.txt      # Danh sách thư viện Python
