Hướng dẫn QtCamera360.py

1/Tải dlib 
link: https://blog.vietnamlab.vn/2018/01/24/dlib-phan-1-cai-dat-dlib-tren-ubuntu/

2/Tải pyQt:
https://gist.github.com/ujjwal96/1dcd57542bdaf3c9d1b0dd526ccd44ff

3/ tải file shape_predictor_68_face_landmarks.dat
https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat?fbclid=IwAR2PPbolCHzH95VncHKZqJnuq4ZZengQMrfFQIleyqr3zXfCnKCnaCdkwSU

*chạy file QtCamera360.py

Hướng dẫn chạy giao diện chỉnh màu - color transfer:
(Để tránh lỗi phát sinh, bấm các lựa chọn theo thứ tự từ trên xuống dưới)

*chạy file main.py

1. Chỉnh ảnh có sẵn (hình mẫu của sinh viên cung cấp)
Ảnh mẫu: source.jpg (chung file với main.py)
- Bấm "Select Image" -> chọn "source.jpg" -> chọn độ contrast & brightness -> bấm "Run" 
- Muốn cắt ảnh -> bấm "Cut Image" 
Bấm "Next..." để qua giao diện chỉnh màu
- bấm "Open" để hiển thị ảnh vừa được chỉnh ở phần trước
- bấm "Effects" để xem các mẫu hiệu ứng (hình góc là source.jpg)
- bấm chọn effect (bằng chữ số từ 1 -> 20)
- bấm "Next"

2. Chỉnh ảnh được lưu từ Camera: (tệp ảnh có tên là: output.jpg)
- Bấm "Select Image" -> chọn "output.jpg" chọn độ contrast & brightness -> bấm "Run" 
- Muốn cắt ảnh -> bấm "Cut Image" 
Bấm "Next..." để qua giao diện chỉnh màu
- bấm "Open" để hiển thị ảnh vừa được chỉnh ở phần trước
- bấm "Effects" để xem các mẫu hiệu ứng (hình góc là source.jpg)
- bấm chọn effect (bằng chữ số từ 1 -> 20)
- bấm "Next"

*Muốn chuyển sang chỉnh ảnh khác chỉ cần bấm "Select Image" và chọn ảnh khác (ảnh cùng folder với main.py)

*Sinh viên chạy demo trên sublime text (window) và VScode (ubuntu)

*Sinh viên có cung cấp video demo, link video demo: 
https://drive.google.com/file/d/1BfXF41LGgPBUSsswXzOBgWiCGk69Tz8i/view?usp=sharing

