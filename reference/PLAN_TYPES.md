# Plan Types

Shot-plan taxonomy used in the Plan column of the shotlist. Both the English label (visible to user) and the data-plan attribute (used by filter JS) are now in English. Older Cyrillic-coded HTMLs will need their filter JS updated; new shotlists use the codes below.

## Mapping

| Code | Full label | Badge class | Use for |
|---|---|---|---|
| `WS` | Wide shot | `p-ws` | Establishing, full body, location-heavy |
| `MS` | Medium shot | `p-ms` | Waist-up, dialogue, two-shots |
| `CU` | Close-up | `p-cu` | Head-and-shoulders, reactions |
| `ECU` | Extreme close-up | `p-ecu` | ECU on eyes, hands, props, screens |
| `MACRO` | Macro | `p-macro` | Pores, droplets, fabric textures |
| `PAN` | Pan | `p-pan` | Slow horizontal/vertical pans |
| `OS` | Off-screen sound | `p-os` | Audio cue, no visual change |
| `VO` | Voice-over | `p-vo` | Voice over the prior visual |
| `VO+MS` | VO · medium shot | `p-vo` | VO during a medium shot |
| `DISSOLVE` | Dissolve | `p-dis` | Transition between scenes |

## Usage

The HTML row uses the code in `data-plan` and the badge class for color, and shows the full label in the badge text:

```html
<tr data-scene="21" data-plan="ECU">
  <td class="c-num">21.4</td>
  <td class="c-plan"><span class="badge p-ecu">Extreme close-up</span></td>
  ...
</tr>
```

The plan filter dropdown uses the code as `<option value>` and the full label as the visible option text:

```html
<option value="ECU">Extreme close-up</option>
```

## When to invent a new code

Don't. If a shot doesn't fit, pick the closest existing code. The taxonomy is intentionally coarse — fine-grained distinctions go in the Camera column ("Push-in", "Slow pan", "Handheld dolly", etc.) not the Plan column.

## Camera column conventions

Free-form English. Common entries:
- `Static`
- `Handheld`
- `Wide / static`
- `Push-in`
- `Pull-out`
- `Dolly L→R` / `Dolly R→L`
- `Slow pan`
- `Crane up` / `Crane down`
- `Top-shot freeze`
- `One-er, 50mm`
- `Handheld, from inside`
- `—` for transitions like dissolves
