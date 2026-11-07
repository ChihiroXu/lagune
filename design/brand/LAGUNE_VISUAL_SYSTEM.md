# LAGUNE Visual System

## Brand foundation

**Direction:** Natural · Analytical · Contemporary · Independent  
**Positioning:** A research platform for investigating spatial questions and communicating evidence.

The approved Concept A mark is `design/brand/LAGUNE_logo.svg`. It is a fixed brand asset: do not edit its paths, colors, proportions, ordering, or composition. Display it as an SVG with intrinsic proportions (`width` and `height: auto`); do not redraw it in CSS, crop it, recolor it, or apply filters.

## Color tokens

| Token | HEX | Use |
|---|---|---|
| Ocean Teal | `#285C59` | Primary actions, selected navigation, key data marks |
| Sea Glass | `#72A69A` | Secondary data, supportive highlights |
| Mist Green | `#DCE8DF` | Quiet panels, selected surfaces, separators |
| Sandstone | `#E9DFC9` | Editorial surfaces and warm map annotations |
| Earth Accent | `#C18B68` | Limited emphasis, field notes, warning state |
| Forest Ink | `#283735` | Headings, body text, dark surfaces |
| Background | `#F7F7F2` | Main canvas |
| Secondary Background | `#EEF3EF` | Grouped sections |
| Surface | `#FFFFFF` | Cards and form controls |
| Border | `#DCE3DE` | Rules, outlines, dividers |
| Secondary Text | `#657B77` | Captions and supporting labels |
| Error | `#A33D32` | Error-only semantic state; never a brand mark color |

Use Forest Ink for text on pale brand fills. Never use Sea Glass, Mist Green, Sandstone, or Earth Accent as small text on white. Pair state colors with explicit labels or icons; color must not be the only state cue. Use brand colors for identity, not to force scientific map ramps.

## Type and hierarchy

| Role | Family | Desktop | Mobile | Line height |
|---|---|---:|---:|---:|
| Display / page title | Manrope 600–700 | 48–64 px | 36–44 px | 1.05–1.15 |
| Section heading | Manrope 600 | 28–36 px | 24–30 px | 1.2 |
| Card / subsection heading | Manrope 600 | 18–22 px | 18–20 px | 1.3 |
| Body and UI | Inter 400–500 | 16 px | 16 px | 1.55 |
| Caption / metadata | Inter 400–500 | 12–14 px | 12–13 px | 1.45 |
| Data and coordinates | Inter 400–500, tabular figures | 13–15 px | 12–14 px | 1.4 |
| Code | JetBrains Mono 400–500 | 13–14 px | 12–13 px | 1.5 |
| Chinese interface | Source Han Sans / 思源黑体 | Match role | Match role | ≥ 1.5 |
| Chinese editorial text | Source Han Serif / 思源宋体 | 16–18 px | 16 px | 1.7 |

Use sentence case for interface headings. Reserve uppercase tracking for the descriptor and compact utility labels. Keep prose lines near 60–75 Latin characters or 30–38 CJK characters.

## Layout and spacing

- Use a 4 px spacing unit: 4, 8, 12, 16, 24, 32, 48, 64, 80 px.
- Center content in a max-width **1280 px** container. Use a 12-column desktop grid with 24 px gutters; collapse to 6 columns at 768–1023 px and 4 columns below 768 px.
- Desktop side padding: 32–48 px; tablet: 24 px; mobile: 16–20 px.
- Use 72–112 px between major desktop sections and 48–72 px on mobile.
- Align navigation, hero copy, project cards, research content, map panels, and footer to the same container edges.
- Prefer open layouts, thin dividers, and clear grouping. Avoid heavy shadows, dense card grids, and full-bleed gradients.

## Auxiliary graphic language

- Use `tidal-motif.svg` for a single low-contrast editorial accent, not as a repeated wallpaper.
- Contour lines: 1 px, 12 px minimum separation, Ocean Teal at 8–16% opacity; keep them away from dense text and data labels.
- Layered bands can frame a hero, research intro, or map caption. Do not copy or alter the fixed logo as a decorative pattern.
- Spatial grids use 40 px cells at 4–8% Ocean Teal opacity and appear only behind map or analysis surfaces.
- Treat all decorative geometry as non-data. A real map or chart must provide its own legend, units, source, and accessible contrast.

## Components and states

### Navigation

Use a 64–72 px header with the fixed SVG logo, clear section links, and one primary action at most. Keep the desktop navigation horizontal; on mobile, stack or collapse it using the host app's existing interaction pattern. Active links use Ocean Teal plus an underline or marker, not color alone.

### Buttons and links

- Primary: Ocean Teal fill, white text; hover uses a darker teal; pressed state shifts down 1 px; disabled state reduces contrast and removes the pointer cue.
- Secondary: transparent or white surface, 1 px Border outline, Forest Ink text; hover uses Secondary Background.
- Text links: Ocean Teal, underline on hover and in long-form content.
- Every keyboard focus target has a visible 3 px Sea Glass focus ring with offset.

### Cards, tags, and media

- Cards: white surface, 1 px Border, 12 px radius, 24 px padding; use a very light shadow only when separation cannot be achieved with whitespace.
- Tags: compact Mist Green or Secondary Background chips with Forest Ink labels. Add a visible text label for category and state.
- Image containers: consistent aspect ratio and crop, descriptive alt text, attribution where needed; no decorative frame around every image.
- Map containers: 16:9 or 3:2, minimum 320 px high on desktop, with title, legend, units, scale/context and data source adjacent to the map.

### Page sections

- Hero: concise positioning statement, one primary action, and a purposeful landscape/map image; avoid generic SaaS dashboards and tourism imagery.
- Projects: 3 columns on wide desktop, 2 on tablet, 1 on mobile; use clear discipline labels and concise project summaries.
- Research: editorial heading, short explanatory copy, then a readable list or two-column grid.
- Footer: Forest Ink or Background surface, aligned to the main container; group research areas, navigation, and contact/documentation links without decorative overload.

## Responsive behavior

Use 1024 px, 768 px, and 480 px breakpoints as starting points. At narrow widths, collapse multi-column layouts, preserve 16 px minimum body text, let maps retain a useful aspect ratio with horizontal overflow only for controls that require it, and keep touch targets at least 44 × 44 px. Verify the fixed logo at native size and never distort it to fit.

## Implementation assets

- `design/styles/tokens.css` is the canonical source for color, typography, spacing, layout, radius, and state tokens.
- `design/styles/components.css` provides framework-neutral component primitives and responsive layout helpers. It imports the token file; consumers should import this stylesheet rather than copy its declarations.
- `design/brand/tidal-motif.svg` is a separate editable decoration; it is not part of the logo asset.

The static Astro website in `website/` consumes these shared styles and brand assets directly. Keep website-specific styling limited to layout details that are not already covered by these shared primitives.
