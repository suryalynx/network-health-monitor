# 🖥️ Network & PC Health Monitoring Script

Skrip ini dibuat untuk memantau kondisi koneksi internet, performa perangkat, dan status keamanan sistem. Cocok digunakan oleh IT Support untuk diagnosa awal masalah jaringan & perangkat.

## Fitur
- Cek koneksi internet (ping ke Google)
- Monitor CPU, RAM, dan Disk Usage
- Cek status antivirus (sementara basic)
- Log otomatis ke file CSV harian

## Cara Menjalankan

### PowerShell:
```bash
powershell -ExecutionPolicy Bypass -File monitor.ps1
```

### Python:
```bash
pip install psutil
python monitor.py
```

## Contoh Output Log
```
2025-06-20 08:30:15, True, 23.5, 1223456, 3200000000, True
```

## Kontribusi
Pull Request sangat diterima. Buat fork dan silakan eksperimen.