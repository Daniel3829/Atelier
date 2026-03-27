```markdown
# Design System Specification: The Academic Atelier

## 1. Overview & Creative North Star
**Creative North Star: "The Intellectual Sanctuary"**

This design system rejects the cluttered, utility-first aesthetic of traditional academic software. Instead, it adopts a "High-End Editorial" approach. We treat student data and institutional management with the same reverence as a premium digital publication. 

To break the "template" look, we utilize **Intentional Asymmetry** (e.g., wide left margins for headings paired with dense data tables) and **Tonal Depth**. We move away from rigid grids toward a layout that feels "curated" rather than "generated." By prioritizing breathing room (whitespace) and sophisticated typography, we establish a professional atmosphere that feels both authoritative and calm.

---

## 2. Colors & Surface Philosophy

### The "No-Line" Rule
Standard 1px borders are prohibited for sectioning. Structural boundaries must be defined exclusively through background color shifts. For example, a `surface_container_low` sidebar sitting against a `surface` background provides a cleaner, more modern distinction than a grey line.

### Surface Hierarchy & Nesting
We treat the UI as a series of physical layers—like stacked sheets of fine vellum.
- **Base Layer:** `surface` (#f7f9fb) for the main application canvas.
- **Content Blocks:** `surface_container_lowest` (#ffffff) for primary data cards to provide maximum "pop."
- **Recessed Areas:** `surface_container` (#eceef0) for global navigation or utility panels.

### The "Glass & Gradient" Rule
To elevate the "trustworthy" aesthetic into something "premium," use Glassmorphism for floating elements (like dropdowns or sticky headers). Use `surface_container_lowest` at 80% opacity with a `20px` backdrop blur. 
*Signature Touch:* For primary CTAs, use a subtle linear gradient from `primary` (#002045) to `primary_container` (#1a365d) at a 135-degree angle. This adds a "lithographic" depth that flat hex codes lack.

---

## 3. Typography: The Editorial Voice

We utilize a dual-sans-serif pairing to distinguish between "Display" (Brand/Identity) and "Functional" (Data/Interface) text.

*   **Display & Headlines (Manrope):** Use `display-lg` through `headline-sm` for page titles and section headers. The wider tracking and geometric builds of Manrope convey modern authority. Use `on_surface` (#191c1e) for high contrast.
*   **Body & Labels (Inter):** Use `body-md` and `label-md` for all system-critical information. Inter’s high x-height ensures legibility in dense academic tables.
*   **Hierarchy Note:** To achieve the editorial look, use a "High-Contrast Scale." Jump from a `display-md` page title directly to `body-sm` metadata. This gap creates a sophisticated, rhythmic layout.

---

## 4. Elevation & Depth

### The Layering Principle
Depth is achieved through **Tonal Layering** rather than traditional drop shadows.
*   **Level 0 (Deepest):** `surface_container_high` (#e6e8ea) for inactive background regions.
*   **Level 1 (Default):** `surface` (#f7f9fb) for the main workspace.
*   **Level 2 (Raised):** `surface_container_lowest` (#ffffff) for active cards and workspace modules.

### Ambient Shadows
Shadows should only be used on "Floating" elements (Modals, Popovers). 
- **Value:** `0px 12px 32px rgba(0, 32, 69, 0.06)`. 
Note the use of a `primary` tint in the shadow—this prevents the "dirty" look of grey shadows and makes the UI feel integrated with the deep blue brand.

### The "Ghost Border" Fallback
If a border is required for accessibility (e.g., in high-contrast mode), use a **Ghost Border**: `outline_variant` (#c4c6cf) at **15% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons
*   **Primary:** Gradient (`primary` to `primary_container`), `rounded-md` (0.75rem), `on_primary` text. No border.
*   **Secondary:** `surface_container_high` background with `primary` text. Provides a "tactile" feel without competing with the primary action.
*   **Tertiary:** Ghost style. No background; `primary` text. Use for "Cancel" or "Back" actions.

### Cards & Data Modules
Cards must use `rounded-lg` (1rem). **Prohibit dividers.** Separate content sections within a card using the Spacing Scale (e.g., a `8` (2.75rem) gap) or a subtle shift to `surface_container_low` for the card footer.

### Input Fields
Inputs should be "Soft Minimalist."
*   **Background:** `surface_container_low` (#f2f4f6).
*   **Border:** None, until focus.
*   **Focus State:** A 2px "Ghost Border" using `surface_tint` (#455f88).

### Academic-Specific Components
*   **The Status Pill:** Use `secondary_container` with `on_secondary_container` text for neutral states (e.g., "Pending"). Use `tertiary_fixed` for highlighted states (e.g., "Graduated").
*   **The Progress Track:** For degree or course completion, use a thick 8px bar. Background: `surface_container_highest`; Fill: `primary`.

---

## 6. Do’s and Don'ts

### Do
*   **Do** use the `24` (8.5rem) spacing token for top-level page margins to create an elite, gallery-like feel.
*   **Do** use `surface_container_lowest` for any element the user needs to interact with (The "Interaction White" rule).
*   **Do** capitalize `label-sm` text and add `0.05em` letter spacing for a professional, "architectural" look.

### Don’t
*   **Don’t** use black (#000000) for text. Always use `on_surface` (#191c1e) to maintain the "Deep Blue" tonal range.
*   **Don’t** use 1px dividers to separate list items. Use a `3` (1rem) vertical gap instead.
*   **Don’t** use "Standard Blue" for links. Use the `primary` token (#002045) with a `surface_tint` underline to maintain brand sophistication.
*   **Don’t** use `rounded-none`. Even the smallest component should have at least `rounded-sm` to maintain the "Soft Minimalism" approachable feel.