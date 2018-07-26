# XKB Layout US - German Umlauts

Custom US based keyboard layout adding Umlauts via the right <ALT> key. Use this with `xkb` on Linux/Unix Systems and X11. Once installed the layout will show up as `English (US, intl., German) in your layout selector.

Tested with Arch Linux only.

## Installation

**IMPORTANT:** You're about to mess around with system files controlling the way your keyboard works. If things go south you may end up with a very strange state. Whatever you do, **create a backup** of any file you touch.

```
# Create a backup (Example)
sudo cp /usr/share/X11/xkb/symbols/us /usr/share/X11/xkb/rules/evdev.xml /root/
```

Append the contents of `intlde` to `/usr/share/X11/xkb/symbols/us`:

```
sudo cat intlde >> /usr/share/X11/xkb/symbols/us
```

Next, make the layout available to the various keyboard managers (e.g. KDE, Gnome, etc.) by adding the following block to the variants section of the US Layout. This is a bit tricky as you need to find the right spot in the XMl file first.

Variants are defined under `layoutList -> layout`. If you can't find that run a search for `US, intl.`. This should put you in the right spot. Just append the variant block below that:

```
<variant>
  <configItem>
    <name>intlde</name>
    <description>English (US, intl., German)</description>
  </configItem>
</variant>
```

Last but not least, activate the layout using your Desktop's layout manager.

## Usage

Once active, you'll be able to type `äÄ`, `öÖ`, `üÜ` and `ß` holding down your **right alt key** and optionally the shift key. No compose key nonesense but smooth on the fly typing.

| Combination       | Result |
|-------------------|--------|
| RAlt + a          | ä      |
| RAlt + o          | ö      |
| RAlt + u          | ü      |
| RAlt + Shift + a  | Ä      |
| RAlt + Shift + o  | Ö      |
| RAlt + Shift + u  | Ü      |
| RAlt + s          | ß      |


Have fun!

## Troubleshooting

So far this is a "works form me" repository. Feel free to open issues if things don't work fo you. Make sure to mention your exact OS versions and I'll see what I can do for you.

### The keyboard layout doesn't show up in my Keyboard manager

You may have some cache files that need to be deleted first. Try:

```
sudo rm /var/lib/xkb/*.xkm
```
