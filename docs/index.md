![logo do projeto](assets/keyboard.png){ width="300" .center }
# Harmony Hub

Harmony Hub is a CLI to help you form scales, chord and harmonic fields.

The whole application Is based on a command called `harmony-hub`. This command has a sus-comman related to each action that the application can perform. Such as `scale` and``chord`.

## How to use?

### Scales

You can call the scales via command line. For example:


```bash
poetry run harmony-hub scale
```

Returning the degrees and notes corresponding to this scale:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Changing the root of the scale

The first CLI parameter is the root of the scale you want to display. This way you can change the returned scale. For example, the `Ab` scale:

```bash
poetry run harmony-hub Ab
```

Result in:

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Ab │ Bb │ C   │ Db │ Eb │ F  │ G   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Change the scale mode

You can change the key of the scale too! This is the second command line parameter. For example, the `E` minor scale:

```bash
poetry run harmony-hub E minor

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ E │ Gb │ G   │ A  │ B │ C  │ D   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

## Chords

```bash
poetry run harmony-hub chord
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Cipher variations

```bash
poetry run harmony-hub chord C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ Ab │
└───┴─────┴────┘
```
By the time you use major, minor, diminished and augmented chords



## More information about the CLI

To discover other options, you can use the `--help` flag:

```bash
poetry run harmony-hub --help

 Usage: harmony-hub [OPTIONS] COMMAND [ARGS]...                                 
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershe  Install completion for  │
│                             ll|pwsh]                 the specified shell.    │
│                                                      [default: None]         │
│ --show-completion           [bash|zsh|fish|powershe  Show completion for the │
│                             ll|pwsh]                 specified shell, to     │
│                                                      copy it or customize    │
│                                                      the installation.       │
│                                                      [default: None]         │
│ --help                                               Show this message and   │
│                                                      exit.                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ chord                                                                        │
│ scale                                                                        │
╰──────────────────────────────────────────────────────────────────────────────╯

```