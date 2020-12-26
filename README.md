# Deoplete Emoji

## Dependencies

- [deoplete][]

## Install

```vim
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'kloki/deoplete-emoji'
```

## Update emoji
```bash
pip3 install emojis
python3 generate.py > rplugin/python3/deoplete/sources/emoji/__init__.py

```

[deoplete]: https://github.com/Shougo/deoplete.nvim
