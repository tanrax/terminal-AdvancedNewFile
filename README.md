Simple script for the terminal that mimics the operation of **AdvancedNewFile** (Vim plugin)

## Use

```bash
ad [url]
```

## Example

```bash
ad airport/plane/
```

Result: airport(folder) > plane (folder)

```bash
ad airport/plane/captain.txt
```

Result: airport (folder) > plane (folder) > captain.txt (file)


## Install

```bash
ADVANCE=/usr/local/bin/ad && curl -o $ADVANCE https://raw.githubusercontent.com/tanrax/terminal-AdvancedNewFile/master/bin/advance && chmod +x $ADVANCE && unset ADVANCE
```
