<p align="center">
    <img src="pet.png" width="200">
    <h1 align="center">⚡ Advanced New File ⚡</h1>
</p>

Add to your terminal the option to quickly create folders and files like a pro.

<p align="center">
    <img src="https://raw.githubusercontent.com/tanrax/terminal-AdvancedNewFile/master/demo.svg">
</p>

[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

## Use ⚙️

```bash
ad [path file or folder]
```

## Install 🔌

``` bash
pip3 install --user advance-touch
```

## Update 💾

``` bash
pip3 install --user --upgrade advance-touch
```

## 📚 Examples 📚

### Single folder 📁

```bash
ad airport/plane/
```

```
airport/
├── plane/
```
---

### Multiple folders 📁➕📁➕📁

```bash
ad airport/ station/ port/
```

```
airport/
station/
port/
```
---

### Single file with your hierarchy of folders 📁➡️📁➡️📝

```bash
ad airport/plane/captain.txt
```

```
airport/
├── plane/
│   ├── captain.txt
```

---

### Folder and single file with your hierarchy of folders 📁➕📁➡️📝

```bash
ad airport/ train-station/train.txt
```

```
airport/
├── plane/
train-station/
├── train.txt
```
---

### If your shell supports arguments expansion 📁➡️📁➡️📝🤖

```bash
ad airport/plane/{captain,passenger}.txt
```

```
airport/
├── plane/
│   ├── captain.txt
│   ├── passenger.txt
```
---

Thanks to the power of 🐍 Python 🐍

Pet created by [Freepik - Flaticon](https://www.flaticon.com/free-icons/folder)
