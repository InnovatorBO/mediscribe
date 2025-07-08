# Navigation Test Guide

## Testing the Dropdown Menu

1. **Open the website** at http://localhost:3000
2. **Check the dropdown button** - it should show "Home" initially
3. **Click the dropdown button** - the menu should open with 3 options:
   - Home
   - About  
   - Contact
4. **Click each menu item** - the page should change and show:
   - Home Page heading + "Insert content here"
   - About Page heading + "Insert content here"
   - Contact Page heading + "Insert content here"
5. **Check the dropdown button text** - it should update to show the current page name
6. **Click outside the dropdown** - the menu should close

## Expected Behavior

- ✅ Dropdown opens/closes on click
- ✅ Page content changes when selecting different pages
- ✅ Dropdown button shows current page name
- ✅ Smooth animations between page transitions
- ✅ Clean, minimal design with just headings and "Insert content here" text

## Files to Review

- `src/components/Navigation.svelte` - Dropdown menu component
- `src/App.svelte` - Main routing logic
- `src/pages/Home.svelte` - Home page
- `src/pages/About.svelte` - About page  
- `src/pages/Contact.svelte` - Contact page 