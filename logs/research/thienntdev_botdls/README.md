# Dream League Soccer Auto Bot

Tool tự động chơi game Dream League Soccer với khả năng điều khiển nhiều giả lập và cày tài nguyên.

## Tính năng chính

### 🎮 Game Automation
- Di chuyển 360 độ bằng nút điều khiển
- Phán đoán tình huống và đưa ra quyết định thông minh
- Xử lý các tình huống đặc biệt: sút phạt, ném biên, đá góc, phát bóng
- Sử dụng linh hoạt các nút A, B, C và skill

### 🖥️ Multi-Emulator Support
- Điều khiển đồng thời ≥3 bản giả lập
- Quản lý từng giả lập độc lập
- Giao diện admin để bật/tắt từng giả lập

### 💰 Resource Farming
- Tự động cày vàng và kim cương
- Setup mục tiêu cày cho từng account
- Dừng cày khi đạt mục tiêu
- Tiếp tục cày các account chưa hoàn thành

### 🎯 Smart Game Detection
- Phát hiện trạng thái game tự động
- Xử lý quảng cáo xuất hiện
- Chuyển đổi giữa Career và Live mode

## Cài đặt

1. Cài đặt Python 3.8+
2. Cài đặt các thư viện:
```bash
pip install -r requirements.txt
```

## Sử dụng

1. Chạy file chính:
```bash
python main.py
```

2. Cấu hình các giả lập trong giao diện admin
3. Setup mục tiêu vàng/kim cương cho từng account
4. Bật chế độ tự động và theo dõi tiến trình

## Cấu trúc dự án

```
ai-bot-dls/
├── main.py                 # Entry point
├── core/                   # Core automation engine
├── emulator/              # Emulator controller
├── game_logic/            # Game decision logic
├── ui/                    # Admin interface
├── config/                # Configuration files
├── utils/                 # Utility functions
└── logs/                  # Log files
```

## Hướng dẫn sử dụng

Xem file hướng dẫn chi tiết tại `docs/USAGE.md`.

## Lưu ý

- Tool chỉ dành cho mục đích học tập và nghiên cứu
- Sử dụng có trách nhiệm và tuân thủ điều khoản game
- Cần cấu hình đúng vị trí các nút điều khiển trong game 