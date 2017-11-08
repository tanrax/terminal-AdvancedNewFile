Script for the terminal that mimics the operation of **AdvancedNewFile** (Vim plugin)

## Use

```bash
ad [path file or folder]
```

## Example

```bash
ad airport/plane/
```

Result:
```
airport/
├── plane/
```

```bash
ad airport/plane/captain.txt
```

```
airport/
├── plane/
│   ├── captain.txt
```


## Install

```bash
ADVANCE=/usr/local/bin/ad && curl -o $ADVANCE https://raw.githubusercontent.com/tanrax/terminal-AdvancedNewFile/master/bin/advance && chmod +x $ADVANCE && unset ADVANCE
```
