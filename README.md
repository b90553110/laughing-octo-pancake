# laughing-octo-pancake

A small static webpage, ready to host on GitHub Pages.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | The page itself |
| `style.css` | All styling (light + dark themes) |
| `.nojekyll` | Tells Pages to serve the files as-is, without Jekyll |

## Publishing on GitHub Pages

1. Push this branch and merge it into your default branch (`main`).
2. On GitHub, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to *Deploy from a branch*.
4. Choose branch `main` and folder `/ (root)`, then **Save**.
5. Wait about a minute. The site appears at
   `https://b90553110.github.io/laughing-octo-pancake/`.

To publish straight from this branch instead, pick it in step 4 rather than `main`.

## Editing

Open `index.html` and change the headings, text and links; adjust colours in the
`:root` block at the top of `style.css`. There is no build step — commit and push,
and Pages redeploys automatically.

## Previewing locally

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000>.
