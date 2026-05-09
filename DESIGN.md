---
name: CineAnime Interface
colors:
  surface: '#fcf8ff'
  surface-dim: '#ddd8e1'
  surface-bright: '#fcf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f2fb'
  surface-container: '#f1ecf5'
  surface-container-high: '#ebe6ef'
  surface-container-highest: '#e5e1ea'
  on-surface: '#1c1b21'
  on-surface-variant: '#474552'
  inverse-surface: '#312f36'
  inverse-on-surface: '#f4eff8'
  outline: '#787583'
  outline-variant: '#c9c4d4'
  surface-tint: '#5c50b2'
  primary: '#342588'
  on-primary: '#ffffff'
  primary-container: '#4b3fa0'
  on-primary-container: '#bfb7ff'
  inverse-primary: '#c7bfff'
  secondary: '#5d5e60'
  on-secondary: '#ffffff'
  secondary-container: '#dfdfe1'
  on-secondary-container: '#616365'
  tertiary: '#552d00'
  on-tertiary: '#ffffff'
  tertiary-container: '#764100'
  on-tertiary-container: '#fbb06a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e4dfff'
  primary-fixed-dim: '#c7bfff'
  on-primary-fixed: '#170065'
  on-primary-fixed-variant: '#443798'
  secondary-fixed: '#e2e2e4'
  secondary-fixed-dim: '#c6c6c8'
  on-secondary-fixed: '#1a1c1d'
  on-secondary-fixed-variant: '#454749'
  tertiary-fixed: '#ffdcc0'
  tertiary-fixed-dim: '#ffb876'
  on-tertiary-fixed: '#2d1600'
  on-tertiary-fixed-variant: '#6b3b00'
  background: '#fcf8ff'
  on-background: '#1c1b21'
  surface-variant: '#e5e1ea'
typography:
  headline-lg:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.5px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  stack-vertical: 12px
  inline-horizontal: 16px
  gutter-md: 16px
  margin-screen: 16px
  inset-bubble: 12px 16px
---

## Brand & Style

The brand personality is **Expert, Cinematic, Helpful, and Calm**. This design system bridges the gap between the structured elevation of Material Design 3 and the clarity and deference found in Apple's Human Interface Guidelines. 

The visual style is **Corporate / Modern**, characterized by high legibility and a focus on content. It avoids visual clutter to allow the cinematic recommendations and movie metadata to remain the primary focus. The interface evokes a sense of "quiet intelligence"—a digital librarian that is both authoritative and approachable.

## Colors

The palette is anchored by **Deep Indigo**, used for primary actions and user-originated message bubbles to provide a sense of grounded authority. The assistant’s presence is defined by a **Soft Off-White** (#F5F5F7), ensuring that long-form recommendations feel light and easy to read. 

Functional colors follow a neutral grayscale to maintain a "cinematic" focus:
- **Primary:** Deep Indigo for brand identity and active states.
- **Secondary/Surface:** Off-white for assistant-specific containers and background depth.
- **Neutral:** A range of grays for secondary text and borders, mirroring the HIG approach to legibility.

## Typography

The design system utilizes **Manrope** for its modern, balanced, and highly legible characteristics. As a clean sans-serif, it provides the "neutrality" required for an expert chatbot while maintaining a contemporary feel.

- **Headlines:** Used for movie titles and section headers, featuring semi-bold to bold weights for clear hierarchy.
- **Body Text:** Standardized at 16px to ensure readability during extended interactions.
- **Labels:** Used for metadata (release years, genres, durations), utilizing a medium weight and slight letter spacing for clarity in compact spaces.

## Layout & Spacing

This design system employs a **Fluid Grid** optimized for mobile viewports. The layout prioritizes vertical flow to support natural conversation threading.

- **Vertical Spacing:** A consistent 12px gap between message bubbles maintains a clear rhythm without wasting screen real estate.
- **Horizontal Padding:** A 16px safe area is maintained on the left and right edges of the screen to align with modern mobile standards.
- **Chat Alignment:** User messages are right-aligned with Deep Indigo backgrounds, while assistant messages are left-aligned with Soft Off-White backgrounds.

## Elevation & Depth

Elevation is used strategically to define the z-axis and interaction priority, drawing heavily from Material Design 3's shadow logic but applying Apple-style softness.

- **Headers:** 1dp elevation creates a subtle separation from the scrolling content area, often combined with a background blur (frosted glass) for depth.
- **Message Bubbles:** 2dp elevation provides a slight lift, making the conversation feel tactile and layered over the base surface.
- **Input Bar:** 8dp elevation ensures the message entry area sits at the highest level of the interface, signifying its constant availability for user action. 
- **Shadow Quality:** Shadows are diffused, low-opacity (10-15%), and slightly tinted with the Primary Indigo to avoid a "dirty" gray appearance.

## Shapes

The shape language is defined by **Rounded** corners to communicate a friendly and helpful persona. 

- **Message Bubbles:** Use a 16px (1rem) corner radius. For a more sophisticated feel, the corner closest to the screen edge can be slightly reduced to 4px to indicate the "origin" of the message.
- **Action Buttons:** Use a fully rounded (pill-shaped) style to distinguish them from content containers.
- **Movie Cards:** Use a 12px (0.75rem) radius to balance structural integrity with the overall softness of the system.

## Components

- **Message Bubbles:**
  - **Assistant:** #F5F5F7 background, black text, 16px radius, 2dp elevation.
  - **User:** #4B3FA0 background, white text, 16px radius, 2dp elevation.
- **Input Bar:** A fixed-bottom container with a 16px horizontal margin, an 8dp elevation shadow, and a 24px corner radius. It includes a subtle placeholder text and a "Send" icon button.
- **Content Cards:** For movie or anime results, cards should feature a 2:3 aspect ratio poster, a 12px radius, and use the typography levels for title (headline-md) and genre (label-md).
- **Suggestion Chips:** Horizontal scrolling chips for "Quick Replies" (e.g., "More like this," "Where to watch"). These use a low-contrast outline (1px solid #E5E5E7) and no shadow.
- **Headers:** A top navigation bar containing the brand name/logo and a "Clear Chat" or "Profile" icon, featuring a 1dp shadow and a soft backdrop blur effect.