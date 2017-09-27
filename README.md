Simple script for the terminal that mimics the operation of **AdvancedNewFile** (Vim plugin)

## Use

```bash
advance [url]
```

## Example

```bash
advance airport/plane/
```

Result: airport(folder) > plane (folder)

```bash
advance airport/plane/captain.txt
```

Result: airport (folder) > plane (folder) > captain.txt (file)


## Install

Add an alias to .bashrc or .zshrc

```bash
## Advance new file
advance() {
	if [[ "$@" == */ ]] then
		mkdir -p $@
	else
		for f in "$@"; do mkdir -p "$(dirname "$f")"; done
		touch "$@"
	fi
}
```

or

```bash
cat $HOME/.bashrc | curl -F https://raw.githubusercontent.com/tanrax/terminal-AdvancedNewFile/master/script.sh
```

Then restart the Bash or Zsh

```bash
source $HOME/.bashrc
```

