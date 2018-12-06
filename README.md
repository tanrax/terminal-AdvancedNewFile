# Advanced New File

<p align="center">
    <img src="https://cdn.rawgit.com/tanrax/terminal-AdvancedNewFile/master/demo.svg">
</p>

## Use

```bash
ad [path file or folder]
```

And it supports multiple arguments!

## Example

```bash
ad airport/plane/
```

```
airport/
├── plane/
```
---

```bash
ad airport/plane/captain.txt
```

```
airport/
├── plane/
│   ├── captain.txt
```

---

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

```bash
# If your shell supports arguments expansion
ad airport/plane/{captain,passenger}.txt
```

```
airport/
├── plane/
│   ├── captain.txt
│   ├── passenger.txt
```

---

## Install

``` bash
pip3 install advance-touch
```
