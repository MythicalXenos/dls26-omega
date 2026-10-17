# DLS26 Fan Website

A comprehensive fan website for DLS26 built with HTML, CSS, Python, and more.

## 📋 Overview

This project is a multi-language fan website dedicated to DLS26, featuring player statistics, match history, team rankings, and community engagement features.

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3
- **Backend**: Python 3.8+, Flask
- **Database**: SQLite
- **Containerization**: Docker
- **Configuration**: JSON, YAML

## 📦 Project Structure

```
dls26/
├── main.py              # Main application entry point
├── config.py            # Configuration management
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── app.json            # Application manifest
├── config.yaml         # YAML configuration
├── Dockerfile          # Docker configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Docker (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/wasswacosmas/dls26.git
   cd dls26
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

### Docker Setup

```bash
docker build -t dls26 .
docker run -p 8000:8000 dls26
```

## 📊 Features

- ⚽ Player Statistics
- 🏆 Match History
- 📈 Team Rankings
- 💬 User Comments
- 🏅 Leaderboards

## 📝 Configuration

All configuration is managed through:
- `config.py` - Python configuration class
- `config.yaml` - YAML-based settings
- `.env` - Environment variables
- `app.json` - Application manifest

## 🔧 Development

### Running in Development Mode

```bash
export ENVIRONMENT=development
export DEBUG=True
python main.py
```

### Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**wasswacosmas**

- GitHub: [@wasswacosmas](https://github.com/wasswacosmas)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support, please open an issue on the GitHub repository.

---

**Last Updated**: 2026-06-16
