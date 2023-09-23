![logo do projeto](assets/keyboard.png){ width="300" .center }
# Harmony Hub

## How to use?

### Scales

You can call the scales via command line. For example:


```bash
poetry run scales
```

Returning the degrees and notes corresponding to this scale:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Changing the tonic of the scale

The first CLI parameter is the root of the scale you want to display. This way you can change the returned scale. For example, the `Ab` scale:

```bash
poetry run scales Ab
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
poetry run scales E minor

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ E │ Gb │ G   │ A  │ B │ C  │ D   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

## More information about the CLI

To discover other options, you can use the `--help` flag:

```bash
poetry run scales --help

 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE] 
                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tônica do campo harmônico           │
│                                 [default: c]                        │
│   tonalidade      [TONALIDADE]  Tonalidade do campo harmônico       │
│                                 [default: maior]                    │
╰─────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                         │
╰─────────────────────────────────────────────────────────────────────╯
```