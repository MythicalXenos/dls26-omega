# Hướng dẫn chạy và sử dụng DLS Auto Bot

Tài liệu này hướng dẫn cài đặt, cấu hình và vận hành dự án trên Windows (Python 3.10) với 1–6 cửa sổ giả lập.

## 1) Yêu cầu môi trường

- Windows 10/11
- Python 3.8–3.11 (khuyến nghị 3.10)
- Trình giả lập Android: LDPlayer 9 / BlueStacks / Nox (khuyến nghị LDPlayer 9)
- Màn hình 16:9 (1280x720/1600x900/1920x1080)

## 2) Cài đặt

```bash
pip install -r requirements.txt
```

Nếu gặp lỗi OpenCV, thử:
```bash
pip uninstall opencv-python
pip install opencv-python==4.8.1.78
```

## 3) Cấu hình giả lập

Mở `config/settings.py` và sửa `EMULATOR_CONFIG` trỏ đúng đường dẫn executable thật của giả lập bạn.
- Ví dụ LDPlayer:
```python
'ldplayer': {
  'executable': r'C:\\LDPlayer\\LDPlayer9\\dnplayer.exe',
  'adb_port': 5555,
  'window_title': 'LDPlayer',
  'resolution': (1920, 1080)
}
```
- Đảm bảo tắt `DEV_CONFIG.mock_emulator`:
```python
DEV_CONFIG = {
  'mock_emulator': False,
  # ...
}
```

Mẹo cấu hình giả lập:
- Đặt độ phân giải mỗi cửa sổ 1280x720 hoặc 1600x900, 30 FPS.
- Tắt hiệu ứng nặng (anti-aliasing cao, frame boost).
- Camera trong game để side-view, zoom-out (nhìn rộng).

## 4) Hiệu chỉnh vị trí nút điều khiển

Dự án dùng tọa độ tương đối (0..1) nên phù hợp nhiều độ phân giải. Nếu cần, chỉnh trong `game_logic/action_executor.py` → `button_positions`:
```python
{
  'button_a': (0.8, 0.7),
  'button_b': (0.9, 0.7),
  'button_c': (0.85, 0.8),
  'skill_button': (0.75, 0.6),
  'joystick_area': (0.2, 0.7)
}
```
Có thể tinh chỉnh riêng per-bot bằng `ActionExecutor.set_button_position(...)` nếu các cửa sổ bố cục khác nhau.

## 5) Chạy bot

- Chạy trực tiếp (tạo 4 bot/4 giả lập theo mặc định):
```bash
python main.py
```
- Admin UI (điều khiển nhiều giả lập, mục tiêu farm): chạy `main.py` và dùng giao diện để Start/Stop bot.

Lưu ý: Hệ thống dùng chuột/keyboard Windows, nên thao tác sẽ lần lượt theo cửa sổ được focus (đã có lệch pha và delay hợp lý). Với 4–6 cửa sổ vẫn ổn.

## 6) Chạy 4–6 cửa sổ ổn định

- Giữ mỗi cửa sổ 1280x720/1600x900, 30 FPS.
- Nếu CPU cao:
  - Tăng `state_check_interval` trong `game_logic/game_bot.py` lên 0.3–0.5s.
  - Giảm log-level (INFO → WARNING/ERROR) trong `utils/logger.py` hoặc `config/settings.py` (LOGGING_CONFIG).
  - Tạm tắt HOG person trong `game_logic/computer_vision.py` nếu không cần.

## 7) Thị giác máy tính (CV) và đổi sân

- Bot chụp frame trực tiếp (không ghi file) để tăng tốc.
- Phát hiện bóng/field, ước lượng `opponent_pressure`, ước lượng `distance_to_goal` và xác định hướng tấn công `attacking_right` theo:
  - Phát hiện khung thành (cột trắng, sát biên) khi zoom-out.
  - Quỹ đạo bóng sau các pha thành công gần nhất.
- Khi đổi sân (hiệp 2), bot tự đảo hướng trong vài nhịp.

## 8) Học dần theo thời gian (càng chơi càng thông minh)

- Học mức hành động: cập nhật success_rate per-action.
- Học tham số chi tiết (SHOOT/PASS): `ActionParamTuner` (epsilon-greedy) lưu hiệu quả tham số theo bucket ngữ cảnh (khoảng cách tới goal, áp lực đối thủ) và tự động chọn lại tham số tốt dần.
  - Dữ liệu lưu tại: `data/param_tuner.json`.
  - Reward được ước lượng nhanh (không dùng OCR nặng) dựa trên ngữ cảnh và kết quả thực thi.
- Aiming khi sút: kéo joystick theo hướng trước khi nhấn A; `power` tỉ lệ theo `distance_to_goal` và có thể được tinh chỉnh bởi tuner.

## 9) Farm tài nguyên

- Chưa bật OCR đọc vàng/kim cương; hệ thống đang cộng vàng heuristic sau mỗi trận để có tiến độ (không ảnh hưởng gameplay).
- Có thể thêm OCR (pytesseract) sau khi ổn định.

## 10) Xử lý quảng cáo và trạng thái game

- Có đóng quảng cáo cơ bản (click góc thường gặp).
- Nhận diện trạng thái trận đấu/menu dựa trên màu sắc/biểu mẫu; có thể mở rộng bằng template UI tùy phiên bản game.

## 11) Troubleshooting nhanh

- OpenCV lỗi import: cài bản đề xuất ở trên.
- `pyautogui` không click đúng: chạy bot với quyền đủ, tắt overlay cản tab.
- Cửa sổ không focus: tiêu đề `window_title` trong `EMULATOR_CONFIG` phải khớp chuỗi tiêu đề thực tế.
- CPU 100% khi 6 cửa sổ: tăng `state_check_interval`, tắt HOG, giảm log.

## 12) Nâng cấp tương lai (khi muốn >6 cửa sổ)

- Thêm InputScheduler toàn cục để xếp hàng click/drag giữa bot → tránh tranh focus chuột.
- Chuyển sang input qua ADB/CLI của giả lập để không phụ thuộc chuột/focus (ổn định hơn khi 8–10 cửa sổ).

---

Nếu cần, có thể thêm tùy chọn “downscale khung hình trước CV” trong config để tăng FPS trên máy yếu. Với 4–6 cửa sổ như bạn đang chạy, không bắt buộc.
