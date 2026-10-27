---
name: Aura Minimalist Portfolio
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#454556'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#757588'
  outline-variant: '#c5c5d9'
  surface-tint: '#3540f9'
  primary: '#111ae4'
  on-primary: '#ffffff'
  primary-container: '#3742fa'
  on-primary-container: '#d7d8ff'
  inverse-primary: '#bec2ff'
  secondary: '#545f73'
  on-secondary: '#ffffff'
  secondary-container: '#d5e0f8'
  on-secondary-container: '#586377'
  tertiary: '#302fbf'
  on-tertiary: '#ffffff'
  tertiary-container: '#4a4cd8'
  on-tertiary-container: '#d8d7ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bec2ff'
  on-primary-fixed: '#00026c'
  on-primary-fixed-variant: '#0d16e3'
  secondary-fixed: '#d8e3fb'
  secondary-fixed-dim: '#bcc7de'
  on-secondary-fixed: '#111c2d'
  on-secondary-fixed-variant: '#3c475a'
  tertiary-fixed: '#e1e0ff'
  tertiary-fixed-dim: '#c0c1ff'
  on-tertiary-fixed: '#07006c'
  on-tertiary-fixed-variant: '#2f2ebe'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 56px
    fontWeight: '800'
    lineHeight: 64px
    letterSpacing: -0.03em
  display-xl-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '800'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.025em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.015em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.005em
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 3rem
  margin-mobile: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

The design system establishes a refined, high-caliber digital identity for personal profile and portfolio experiences. It combines high-end editorial minimalism with modern digital craft, cultivating an impression of technical mastery, precision, and restrained confidence. 

The aesthetic is anchored in vast, intentional negative space, pristine white surfaces, razor-sharp typographic hierarchy, and tactile neutral structures. Vibrant royal indigo accents are deployed with strict discipline—serving solely to pull focus toward critical interactions, case study outcomes, and contact pathways without creating visual clutter.

## Colors

The palette is light-first and highly disciplined, prioritizing contrast, clarity, and optical calmness.

- **Canvas & Surfaces**: The base canvas rests at pure `#ffffff`, paired with subtle secondary layer cards at `#f8fafc` and `#f1f5f9`. 
- **Borders & Dividers**: Borders maintain a soft slate profile at `#e2e8f0` (default) and `#cbd5e1` (interactive/hover states) to sculpt structure without heavy visual weight.
- **Typography & Neutrals**: Headings and primary copy leverage deep slate `#0f172a`, while secondary metadata uses `#64748b` and tertiary hints utilize `#94a3b8`.
- **Primary & Accent Roles**: Royal blue `#3742fa` commands focal touchpoints, backed by an indigo nuance `#6366f1` for gradients, tags, and micro-highlights.

## Typography

The typography relies entirely on Plus Jakarta Sans, utilizing geometric structure, wide apertures, and refined modern proportions to project clarity. 

Tracking is pulled slightly tight on all headings (`-0.015em` to `-0.03em`) to deliver modern editorial weight, while small labels receive subtle positive tracking (`+0.04em`) to preserve legibility when set in uppercase or inline tag modes. Line heights are spaced generously across body copy to ensure effortless reading across lengthy portfolio case studies and project briefs.

## Layout & Spacing

The layout operates on a 12-column responsive fluid grid bounded by a max-width container of `1200px` for optimal readability and balanced composition.

- **Desktop (1024px+)**: 12 columns, 24px gutters, and generous page-edge padding of 48px to preserve whitespace framing.
- **Tablet (768px - 1023px)**: 8 columns, 20px gutters, and 32px canvas margins.
- **Mobile (Below 768px)**: 4 columns, 16px gutters, and 20px canvas margins.

Spacing follows an 8-point rhythm scaled up to larger intervals for section demarcations (`4rem`, `6rem`, and `8rem`), allowing each project showcase and personal bio block to stand out independently without crowded visual competition.

## Elevation & Depth

Visual hierarchy favors layered flatness and delicate boundary control over heavy drop shadows.

- **Level 0 (Flat)**: Pure `#ffffff` background with `#e2e8f0` 1px borders.
- **Level 1 (Subtle Lift / Cards)**: Soft ambient shadow: `0 1px 3px rgba(15, 23, 42, 0.04), 0 1px 2px rgba(15, 23, 42, 0.02)` coupled with a `#f1f5f9` hairline outline.
- **Level 2 (Hover / Active Overlay)**: Lifted state for interactive project cards: `0 12px 24px -8px rgba(15, 23, 42, 0.08), 0 4px 8px -4px rgba(15, 23, 42, 0.03)`.
- **Accent Glaze**: Interactive primary elements and focused states incorporate an indigo glow: `0 0 0 3px rgba(55, 66, 250, 0.15)`.
- **Modals & Overlays**: Backdrop filter with `blur(8px)` paired with `rgba(255, 255, 255, 0.8)` for light, breathable overlays.

## Shapes

The design system incorporates geometric softness with a base token value of `0.5rem` (`8px`) for standard controls, scaling smoothly to create harmony:

- Standard elements (buttons, inputs, status badges): `8px` (`rounded-md`).
- Container panels, featured project media containers, and modal shells: `16px` (`rounded-lg`).
- Feature cards and hero highlights: `24px` (`rounded-xl`).
- Filter pills, live indicators, and tag toggles: Full pill shape (`9999px`).

## Components

- **Buttons**:
  - *Primary*: Solid `#3742fa` fill with white typography, slight scale shift (`scale: 1.01`) and subtle indigo bloom on hover.
  - *Secondary / Outline*: Pure white surface with `#e2e8f0` border, transitions to `#f8fafc` surface and `#1e293b` text on hover.
  - *Ghost*: Minimalist padding, no border, text transitions from `#64748b` to `#0f172a`.

- **Cards (Case Studies & Highlights)**:
  - White surface enclosed by a 1px border of `#e2e8f0`. On cursor hover, the card transforms with a `-2px` vertical translation, edge border shift to `#cbd5e1`, and subtle elevation shadow. Inner project imagery features a subtle 12px border radius.

- **Chips & Tags**:
  - Compact padding (`4px 10px`), pill-shaped, rendered in faint indigo neutral tint (`#eef2ff`) with `#3742fa` medium label text. Used for categorization such as skill tags, year, and client context.

- **Form Fields & Inputs**:
  - Clean white or `#f8fafc` background with a crisp `#e2e8f0` border. Transitions seamlessly on focus to a `#3742fa` stroke backed by a gentle `3px` focus ring glow (`rgba(55, 66, 250, 0.12)`).

- **Project Timeline / Experience List**:
  - Minimalist list rows separated by hairline `#f1f5f9` rules. Features subtle row background highlight (`#f8fafc`) on hover, preserving linear reading flow without heavy card boxes.

- **Checkboxes & Radios**:
  - Square (`6px` radius) and circular elements styled with `#e2e8f0` borders, snapping smoothly to `#3742fa` fill with crisp white vector indicators upon selection.