```
 ____  _           _     ____                    _        ____ _     ___
|  _ \(_) ___ ___ | |__ / ___| _   _ _ __  _ __ | |_   _ / ___| |   |_ _|
| |_) | |/ __/ _ \| '_ \\___ \| | | | '_ \| '_ \| | | | | |   | |    | |
|  _ <| | (_| (_) | | | |___) | |_| | |_) | |_) | | |_| | |___| |___ | |
|_| \_\_|\___\___/|_| |_|____/ \__,_| .__/| .__/|_|\__, |\____|_____|___|
                                    |_|   |_|      |___/
```

# Ricoh Supply CLI

Ricoh Supply CLI is a _"blazingly fast 🤣"_ Python CLI tool that allows checking Ricoh printers supply/toner status with SNMP protocol.

## 📦 Installation

Use the package manager [pdm](https://pdm.fming.dev/) to install. Run the below command inside the project directory.

```bash
pdm install
```

## 🔨 Usage

CLI app has only one parameter and that is the IP address of the printer.

```bash
python main.py 172.10.0.2
```

or

```bash
chmod +x main.py
./main.py 172.10.0.2
```

### 📋 Sample results

cmyk
```bash
> ./main.py 172.10.0.2
ip: 172.10.0.2 - model: MP C307 - serial: 11111111111

[====================================----] 90.0%  black
[============----------------------------] 30.0%  cyan
[============----------------------------] 30.0%  magenta
[========--------------------------------] 20.0%  yellow
```

only black
```bash
./main.py 172.10.0.3
ip: 172.10.0.3 - model: P 502 - serial: 22222222222

[============================------------] 70.0%  black
```

## 🎯 Tested Ricoh printer models
- IM C300 (cmyk)
- IM C3500 (cmyk)
- MP C307 (cmyk)
- P 502 (black)

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📰 License
[MIT](https://choosealicense.com/licenses/mit/)
