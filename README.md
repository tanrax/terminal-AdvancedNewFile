# Advanced New File

And it supports multiple arguments!

<p align="center">
    <img src="https://cdn.rawgit.com/tanrax/terminal-AdvancedNewFile/master/demo.svg">
</p>

## Use

```bash
ad [path file or folder]
```

## Install

``` bash
pip3 install advance-touch
```

## Examples

### Single folder

```bash
ad airport/plane/
```

```
airport/
├── plane/
```
---

### Multiple folders

```bash
ad airport/ station/ port/
```

```
airport/
station/
port/
```
---

### Single file with your hierarchy of folders

```bash
ad airport/plane/captain.txt
```

```
airport/
├── plane/
│   ├── captain.txt
```

---

### Folder and single file with your hierarchy of folders

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

### If your shell supports arguments expansion

```bash
ad airport/plane/{captain,passenger}.txt
```

```
airport/
├── plane/
│   ├── captain.txt
│   ├── passenger.txt
```
